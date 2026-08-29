#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify-listing-census.py -- the falsifier for listing-census.py.

WHY IT EXISTS
    `listing-census.py` produced the eviction figures in `O-69`, and those figures REFUTED a
    hypothesis. A refutation carried by an instrument nobody has broken is just a different
    unchecked claim, so this seeds defects into synthetic transcripts with a KNOWN answer and
    asserts each is caught.

    It was written after the census shipped, which is the wrong order and is recorded as a
    deviation in `AMENDS D-061` rather than quietly corrected.

THE FIXTURE IS SYNTHETIC AND SAYS SO
    Real transcripts are 1.6 GB and their true eviction counts are unknown -- that is the
    whole reason the census exists. So the fixture states its own answer, and the awkward
    shapes are there on purpose: a description containing a colon (which a delimiter-split
    parser mangles), a name-only entry written both with and without its trailing colon, a
    file with no listing at all, and an unparseable line.

Modelled on verify-census.py: copies nothing, builds a throwaway tree, removes it in a
finally. Exits 0 when every seeded defect fired, 1 when one slipped, 2 on setup error.
"""

from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CENSUS = os.path.join(HERE, "listing-census.py")


def listing(entries):
    """entries: list of (name, description-or-empty). Empty description == evicted."""
    lines = []
    for name, desc in entries:
        lines.append("- %s: %s" % (name, desc) if desc else "- %s:" % name)
    return "\n".join(lines)


def transcript(path, entries, ts="2026-08-28T10:00:00.000Z", extra_lines=()):
    rec = {
        "type": "user",
        "uuid": "u-0001",
        "sessionId": "s-0001",
        "timestamp": ts,
        "version": "2.1.250",
        "entrypoint": "claude-desktop",
        "attachment": {
            "type": "skill_listing",
            "isInitial": True,
            "skillCount": len(entries),
            "names": [n for n, _ in entries],
            "content": listing(entries),
        },
    }
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        for line in extra_lines:
            fh.write(line + "\n")


def run(root, out):
    r = subprocess.run(
        [sys.executable, CENSUS, "--root", root, "--out", out],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    rows = []
    if os.path.isfile(out):
        rows = [json.loads(l) for l in io.open(out, encoding="utf-8") if l.strip()]
    return r.returncode, (r.stdout or "") + (r.stderr or ""), rows


# ---- the seeded cases -----------------------------------------------------------------

def c1_known_eviction(d):
    """8 entries, 3 of them stripped. The census must say 3, not 0 and not 8."""
    proj = os.path.join(d, "proj-a")
    os.makedirs(proj)
    entries = [("alpha", "does alpha things"), ("beta", ""), ("gamma", "does gamma"),
               ("delta", ""), ("epsilon", "does epsilon"), ("zeta", ""),
               ("eta", "does eta"), ("theta", "does theta")]
    transcript(os.path.join(proj, "a.jsonl"), entries)
    return ("3 of 8 entries stripped -> must report exactly 3",
            lambda rows: len(rows) == 1 and rows[0]["entries_name_only"] == 3
            and rows[0]["entries_with_description"] == 5)


def c2_colon_in_description(d):
    """A description containing a colon must not read as a second entry."""
    proj = os.path.join(d, "proj-b")
    os.makedirs(proj)
    entries = [("alpha", "Use when: the thing happens: really"), ("beta", "plain")]
    transcript(os.path.join(proj, "b.jsonl"), entries)
    return ("a colon inside a description must not split the entry",
            lambda rows: len(rows) == 1 and rows[0]["entries_with_description"] == 2
            and rows[0]["entries_name_only"] == 0)


def c3_bare_name_no_colon(d):
    """An evicted entry rendered without its trailing colon still counts as evicted."""
    proj = os.path.join(d, "proj-c")
    os.makedirs(proj)
    path = os.path.join(proj, "c.jsonl")
    transcript(path, [("alpha", "described")])
    rec = json.loads(io.open(path, encoding="utf-8").readline())
    rec["attachment"]["content"] = "- alpha: described\n- beta\n- gamma:"
    rec["attachment"]["names"] = ["alpha", "beta", "gamma"]
    rec["attachment"]["skillCount"] = 3
    io.open(path, "w", encoding="utf-8", newline="\n").write(
        json.dumps(rec, ensure_ascii=False) + "\n")
    return ("bare `- beta` and `- gamma:` are BOTH evicted -> 2",
            lambda rows: len(rows) == 1 and rows[0]["entries_name_only"] == 2
            and sorted(rows[0]["evicted_names"]) == ["beta", "gamma"])


def c4_no_listing_anywhere(d):
    """A corpus with no listing must report zero, not crash and not invent one."""
    proj = os.path.join(d, "proj-d")
    os.makedirs(proj)
    with io.open(os.path.join(proj, "d.jsonl"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps({"type": "assistant", "uuid": "x", "timestamp": "2026-08-28T10:00:00Z"}) + "\n")
    return ("a corpus with no skill_listing -> 0 rows, exit 0",
            lambda rows: rows == [])


def c5_corrupt_line(d):
    """An unparseable line must be skipped, not fatal, and the good listing still found."""
    proj = os.path.join(d, "proj-e")
    os.makedirs(proj)
    transcript(os.path.join(proj, "e.jsonl"),
               [("alpha", "described"), ("beta", "")],
               extra_lines=['{"type": "user", "attachment": {"type": "skill_listing", TRUNCATED'])
    return ("a truncated line is skipped and the valid listing still counted",
            lambda rows: len(rows) == 1 and rows[0]["entries_name_only"] == 1)


CASES = [c1_known_eviction, c2_colon_in_description, c3_bare_name_no_colon,
         c4_no_listing_anywhere, c5_corrupt_line]


def main():
    if not os.path.isfile(CENSUS):
        print("SETUP ERROR: %s not found" % CENSUS)
        return 2
    print("falsifier for listing-census.py\n")
    tmp = tempfile.mkdtemp(prefix="verify-listing-census-")
    missed = 0
    try:
        for i, case in enumerate(CASES, start=1):
            d = os.path.join(tmp, "case%d" % i)
            os.makedirs(d)
            label, predicate = case(d)
            rc, out, rows = run(d, os.path.join(tmp, "out%d.ndjson" % i))
            ok = rc == 0 and predicate(rows)
            if ok:
                print("FIRED   C%d %s" % (i, label))
            else:
                missed += 1
                print("MISSED  C%d %s   <-- the census disagreed" % (i, label))
                print("        rc=%d rows=%s" % (rc, json.dumps(rows)[:300]))
        print()
        if missed:
            print("%d of %d cases disagreed. listing-census.py's output may not be "
                  "believed, and O-69 rests on it." % (missed, len(CASES)))
            return 1
        print("All %d cases hold. The census was observed producing the KNOWN answer on "
              "known input, including the shapes that break a naive parser." % len(CASES))
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
