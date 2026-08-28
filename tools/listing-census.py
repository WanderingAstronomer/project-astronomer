#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""listing-census.py -- what the skill listing actually looked like, turn by turn.

WHAT IT ANSWERS
    Claude Code injects a listing of every skill's name and description at the start of a
    session. That listing is capped at a share of the context window, and WHEN IT OVERFLOWS
    IT DROPS THE DESCRIPTIONS OF THE LEAST-INVOKED SKILLS FIRST -- the name survives, so the
    skill stays invocable and stops being chosen. A skill with no invocation history is
    first against the wall, which keeps its history empty.

    This measures that eviction: how large the listing was, how many entries kept their
    description, and WHICH names were reduced to a bare name.

WHY NOT `/context` OR `/doctor`
    Both report it, and both are interactive surfaces. This reads the `skill_listing`
    attachment out of the transcripts instead, which has three advantages: it is
    non-interactive, it is HISTORICAL -- so a change to the budget can be measured against
    what came before rather than against a memory -- and it records what the model was
    ACTUALLY given rather than what the configuration implies it should have been.

    It also reaches skills that have no on-disk presence. Measured 2026-08-28: this machine
    carries 54 SKILL.md files on disk against ~163 offered in-session, so roughly eighty
    arrive from an account-side source no local enumeration surface exposes. A disk-based
    census of the listing would silently miss half of it.

READ-ONLY, and the D-005 argument is the same one tools/README.md draws for the other
instruments: this reads transcripts and writes only the file the caller names. A measuring
instrument is not tooling that generates or validates projects.

Pure stdlib. Exits 0.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
from collections import Counter

GATE = '"skill_listing"'
# A listing entry is `- name: description`. An evicted one is `- name:` with nothing after,
# or `- name` alone. Matching the SHAPE rather than a delimiter, because a description that
# itself contains a colon must not read as two entries.
ENTRY_RE = re.compile(r"^-\s+([A-Za-z0-9._:-]+)\s*:?\s*(.*)$")


def find_attachment(obj):
    if isinstance(obj, dict):
        if obj.get("type") == "skill_listing":
            return obj
        for v in obj.values():
            got = find_attachment(v)
            if got is not None:
                return got
    elif isinstance(obj, list):
        for v in obj:
            got = find_attachment(v)
            if got is not None:
                return got
    return None


def parse_listing(content):
    """-> (with_description, name_only, [names that lost their description])"""
    withd, nameonly, evicted = 0, 0, []
    for line in (content or "").splitlines():
        m = ENTRY_RE.match(line.strip())
        if not m:
            continue
        name, desc = m.group(1), m.group(2).strip()
        if desc:
            withd += 1
        else:
            nameonly += 1
            evicted.append(name)
    return withd, nameonly, evicted


def iter_files(root, limit=None):
    n = 0
    for dirpath, _dirs, files in os.walk(root):
        for fn in sorted(files):
            if not fn.endswith(".jsonl"):
                continue
            yield os.path.join(dirpath, fn)
            n += 1
            if limit and n >= limit:
                return


def main(argv=None):
    ap = argparse.ArgumentParser(description="Census of the injected skill listing.")
    ap.add_argument("--root", default=os.path.join(os.path.expanduser("~"), ".claude", "projects"))
    ap.add_argument("--out", default="listing-census.ndjson")
    ap.add_argument("--since", default=None, help="ISO date; only listings at or after it")
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args(argv)

    rows = []
    scanned = 0
    for path in iter_files(a.root, a.limit):
        scanned += 1
        try:
            fh = io.open(path, encoding="utf-8", errors="replace")
        except Exception:
            continue
        with fh:
            for line in fh:
                if GATE not in line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception:
                    continue
                att = find_attachment(rec)
                if att is None:
                    continue
                ts = rec.get("timestamp") or ""
                if a.since and ts[:10] < a.since:
                    continue
                content = att.get("content") or ""
                withd, nameonly, evicted = parse_listing(content)
                names = att.get("names") or []
                rows.append({
                    "timestamp": ts,
                    "project": os.path.basename(os.path.dirname(path)),
                    "session_id": rec.get("sessionId"),
                    "harness_version": rec.get("version"),
                    "entrypoint": rec.get("entrypoint"),
                    "skill_count_declared": att.get("skillCount"),
                    "names_listed": len(names),
                    "listing_chars": len(content),
                    "entries_with_description": withd,
                    "entries_name_only": nameonly,
                    "evicted_names": evicted,
                })

    rows.sort(key=lambda r: r["timestamp"] or "")
    with io.open(a.out, "w", encoding="utf-8", newline="\n") as out:
        for r in rows:
            out.write(json.dumps(r, ensure_ascii=False) + "\n")

    print("files scanned      %d" % scanned)
    print("listings found     %d" % len(rows))
    if not rows:
        print("\nNo skill_listing attachment found. That is a finding, not an empty result:")
        print("either the harness stopped emitting it, or --since excluded everything.")
        return 0

    first, last = rows[0], rows[-1]
    print("window             %s .. %s" % (first["timestamp"][:19], last["timestamp"][:19]))
    print()
    print("%-21s %8s %8s %9s %9s" % ("", "chars", "listed", "with-desc", "name-only"))
    for label, r in (("earliest", first), ("latest", last)):
        n = r["entries_with_description"] + r["entries_name_only"]
        pct = (100.0 * r["entries_name_only"] / n) if n else 0.0
        print("%-21s %8d %8d %9d %9d  (%.1f%% evicted)"
              % (label, r["listing_chars"], r["names_listed"],
                 r["entries_with_description"], r["entries_name_only"], pct))

    ev = Counter()
    for r in rows:
        ev.update(r["evicted_names"])
    if ev:
        print("\nmost often reduced to a bare name (of %d listings):" % len(rows))
        for name, n in ev.most_common(12):
            print("   %-44s %d" % (name, n))
    else:
        print("\nNo entry lost its description in any listing -- the budget is not "
              "overflowing, and the eviction mechanism is dormant here.")

    print("\nwrote %s" % os.path.abspath(a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
