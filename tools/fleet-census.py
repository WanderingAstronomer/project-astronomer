#!/usr/bin/env python3
"""
fleet-census.py — measure the installed fleet before anything is shipped to it.

WHY THIS EXISTS (the incident is the description; see rituals/recurring-defect.md):

  On 2026-08-19 a design brief (`design/distribution-and-scope.md`) proposed a vendoring
  installer for ~30 hand-maintained instances. Its section 3 was headed "Verified current
  state" and called its numbers "the only load-bearing facts." Four of them were wrong, and
  each was wrong in the direction that makes an installer look safer than it is:

    1. "~30 project instances." Measured: NINE install points, across SEVEN distinct
       projects. Two of the nine are git WORKTREES of a third, so the same drift was being
       counted three times.

    2. "Genuine drift, entire surface: 3 files." Measured: of 57 managed files that do not
       match upstream HEAD, FORTY-EIGHT are clean older releases — byte-identical, after LF
       normalisation, to an upstream commit. They are STALE, not drifted. Only NINE are
       genuine local edits, and those reduce to FOUR distinct artifacts.

    3. "install/retrieval-setup.md (20 lines)" of instance drift. Measured: four of five
       instances are identical to upstream HEAD. The 20 lines are an UNCOMMITTED change in
       upstream's own working tree. The brief compared a dirty worktree against the fleet
       and attributed the difference to the fleet.

    4. Two orphaned capabilities. Measured: FOUR. The brief read one instance; a fourth
       capability, operator-approved elsewhere, sat in a project it never opened.

  The defect class is one thing, not four: a two-way clean/drifted split cannot tell an old
  release from a local edit, and every instance that is merely behind reads as customised.
  An installer built on that split refuses to update 48 files in a project that has edited
  none of them, hands the operator 48 decisions that are all the same decision, and teaches
  them to ignore the signal it exists to produce. That is the failure the brief names for
  CRLF in its own section 4.2, arriving by a second route it did not check.

  So the census classifies THREE ways, not two:

    current  — matches upstream HEAD (LF-normalised)
    stale    — matches some earlier upstream commit; safe to overwrite, names which
    drifted  — matches no upstream version that ever existed; never overwrite

  Only the third is a human decision. The measurement is the point: this file exists so the
  next person to propose shipping to the fleet has to look at it first.

WHAT IT DELIBERATELY DOES NOT DO

  It does not write, install, update, or move anything. It is a measuring instrument, run by
  hand, in the same class as check-corpus.py. CHARTER "Out of scope" and D-005 bar a
  scaffolding CLI; reading the fleet is not that, and building one is a decision this file
  does not make.

USAGE

  python tools/fleet-census.py                 # census the fleet under ~/Documents
  python tools/fleet-census.py --root DIR      # census somewhere else
  python tools/fleet-census.py --verbose       # list every file, not just the drifted ones
  python tools/fleet-census.py --verify        # seed known-bad fixtures, assert it fires

  Exit 0 when no genuine drift is found, 1 when there is, 2 on a usage error.
  --verify exits 0 only if every seeded defect was caught.
"""

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Where an instance's vendored tree has actually been found in the wild. This list is
# measured, not designed: five layouts exist because install/README.md named no home for the
# tree until D-052. Order matters only for reporting.
TREE_CANDIDATES = ["docs/astronomer", "astronomer", "<nested-dir>/astronomer"]

# The groups upstream owns. Anything else in an instance's tree is that instance's own.
MANAGED_GROUPS = ("doctrine/", "rituals/", "artifacts/", "tiers/", "provenance/")

SKIP_DIRS = {".git", "node_modules", "AppData", "venv", ".venv", "__pycache__", "dist", "build"}


# --------------------------------------------------------------------------- hashing

def nh(data: bytes) -> str:
    """Hash on LF-normalised content.

    Without this every Windows instance reports total drift forever: a raw-byte compare of
    this corpus reported 46 of 47 files changed when 45 were identical, the whole delta
    being one byte per line.
    """
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def nh_file(p: Path) -> str:
    return nh(p.read_bytes())


# --------------------------------------------------------------------------- upstream

class Upstream:
    """Upstream's history, indexed lazily, so a file can be dated instead of just judged."""

    def __init__(self, repo: Path):
        self.repo = repo
        self._head = {}
        self._hist = {}
        self._dates = {}

    def _git(self, *args) -> bytes:
        return subprocess.run(
            ["git", *args], cwd=self.repo, capture_output=True, check=False
        ).stdout

    def head_hash(self, rel: str):
        if rel not in self._head:
            blob = self._git("show", f"HEAD:{rel}")
            self._head[rel] = nh(blob) if blob else None
        return self._head[rel]

    def history(self, rel: str):
        """[(norm_hash, commit, date)] for this path, newest commit first."""
        if rel not in self._hist:
            out = []
            commits = self._git(
                "log", "--all", "--format=%H", "--", rel
            ).decode(errors="replace").split()
            for c in commits:
                blob = self._git("show", f"{c}:{rel}")
                if not blob:
                    continue
                if c not in self._dates:
                    self._dates[c] = self._git(
                        "log", "-1", "--format=%ad", "--date=short", c
                    ).decode(errors="replace").strip()
                out.append((nh(blob), c[:8], self._dates[c]))
            self._hist[rel] = out
        return self._hist[rel]

    def classify(self, rel: str, local: Path):
        """-> (status, detail). status in current|stale|drifted|unknown-path"""
        h = nh_file(local)
        head = self.head_hash(rel)
        if head is None:
            return "unknown-path", ""
        if h == head:
            return "current", ""
        for hh, commit, date in self.history(rel):
            if hh == h:
                return "stale", f"{commit} ({date})"
        return "drifted", ""


# --------------------------------------------------------------------------- discovery

def is_worktree(inst: Path):
    """Return the parent repo path if inst is a git worktree, else None.

    Worktrees matter: they are checkouts of ONE repository, so counting them as separate
    instances multiplies one project's drift by the number of checkouts. The brief's fleet
    was inflated exactly this way.
    """
    g = inst / ".git"
    if g.is_file():
        try:
            txt = g.read_text(errors="replace").strip()
        except OSError:
            return None
        if txt.startswith("gitdir:"):
            gd = txt.split(":", 1)[1].strip()
            marker = "/.git/worktrees/"
            if marker in gd.replace("\\", "/"):
                return gd.replace("\\", "/").split(marker)[0]
    return None


def find_instances(root: Path):
    found = []
    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        base = os.path.basename(dirpath)
        if base == "skills" and os.path.basename(os.path.dirname(dirpath)) == ".claude":
            inst = Path(dirpath).parent.parent
            if inst == REPO:
                continue
            try:
                names = os.listdir(dirpath)
            except OSError:
                continue
            if any(n.startswith("astronomer-") for n in names):
                found.append(inst)
    return sorted(set(found))


def locate_tree(inst: Path):
    for c in TREE_CANDIDATES:
        if (inst / c).is_dir():
            return c
    return None


def managed_pairs(inst: Path, tree):
    """[(upstream_rel, local_path)] for everything upstream owns in this instance."""
    pairs = []
    if tree:
        tdir = inst / tree
        for p in sorted(tdir.rglob("*")):
            if p.is_file():
                rel = p.relative_to(tdir).as_posix()
                if rel.startswith(MANAGED_GROUPS):
                    pairs.append((rel, p))
    sk = inst / ".claude" / "skills"
    if sk.is_dir():
        for d in sorted(sk.iterdir()):
            if d.is_dir() and d.name.startswith("astronomer-"):
                for p in sorted(d.rglob("*")):
                    if p.is_file():
                        rel = f"install/skills/{d.name}/{p.relative_to(d).as_posix()}"
                        pairs.append((rel, p))
    return pairs


# --------------------------------------------------------------------------- census

def census(root: Path, verbose=False, quiet=False):
    up = Upstream(REPO)
    instances = find_instances(root)
    totals = {"current": 0, "stale": 0, "drifted": 0, "unknown-path": 0}
    drift_index = {}
    projects = {}
    rows = []

    for inst in instances:
        wt_parent = is_worktree(inst)
        # Normalise before grouping. A worktree's .git file spells its parent with forward
        # slashes while Path spells it with backslashes on Windows, so the naive key filed a
        # repo and its own worktrees under two different projects and over-counted the fleet.
        key = str(Path(wt_parent).resolve() if wt_parent else inst.resolve()).lower()
        projects.setdefault(key, []).append(inst)

        tree = locate_tree(inst)
        counts = {"current": 0, "stale": 0, "drifted": 0, "unknown-path": 0}
        stale_by = {}
        drifted = []
        for rel, p in managed_pairs(inst, tree):
            status, detail = up.classify(rel, p)
            counts[status] += 1
            totals[status] += 1
            if status == "stale":
                stale_by[detail] = stale_by.get(detail, 0) + 1
            elif status in ("drifted", "unknown-path"):
                drifted.append((rel, status))
                drift_index.setdefault(rel, []).append((inst, key))
            if verbose:
                rows.append((str(inst), rel, status, detail))

        if not quiet:
            print("=" * 78)
            label = str(inst)
            print(label)
            marks = [f"tree={tree or 'NONE'}"]
            if wt_parent:
                marks.append(f"WORKTREE of {wt_parent}")
            print("  " + "  ".join(marks))
            print(
                f"  current={counts['current']}  stale={counts['stale']}  "
                f"drifted={counts['drifted']}  novel={counts['unknown-path']}"
            )
            for c, n in sorted(stale_by.items(), key=lambda kv: -kv[1]):
                print(f"    {n:3d} files match upstream {c} - safe to update")
            for rel, status in drifted:
                tag = "LOCAL EDIT" if status == "drifted" else "NOT UPSTREAM"
                print(f"    {tag}: {rel}")

    if verbose and not quiet:
        print("\n" + "=" * 78)
        print("EVERY MANAGED FILE")
        for inst, rel, status, detail in rows:
            print(f"  {status:12s} {detail:18s} {inst} :: {rel}")

    if not quiet:
        print("\n" + "=" * 78)
        print(f"install points : {len(instances)}")
        print(f"distinct projects : {len(projects)}   (worktrees folded into their repo)")
        for k, v in projects.items():
            if len(v) > 1:
                print(f"    {k} has {len(v)} checkouts: {', '.join(str(x) for x in v)}")
        print(
            f"\ncurrent={totals['current']}  stale={totals['stale']}  "
            f"drifted={totals['drifted']}  novel={totals['unknown-path']}"
        )
        print(
            "\nstale is not drift: those files are clean older releases and an update may "
            "overwrite them.\nOnly the drifted and novel files below are a human decision."
        )
        owners = set()
        for rel, hits in sorted(drift_index.items(), key=lambda kv: -len(kv[1])):
            keys = {k for _, k in hits}
            owners |= keys
            note = "" if len(hits) == len(keys) else f"  (in {len(keys)} project, {len(hits)} checkouts)"
            print(f"  {len(hits):2d}x  {rel}{note}")
        print(
            f"\n{len(drift_index)} distinct artifacts need a human decision, "
            f"across {len(owners)} of {len(projects)} projects.\n"
            "Everything else is mechanical."
        )

    return totals, drift_index


# --------------------------------------------------------------------------- verify

def verify():
    """Seed a known defect per classification and assert the census reports it.

    A classifier is not believed because it returned a clean result. verify-gate.py already
    holds this discipline for the corpus gate; this is the same discipline for this one.
    """
    up = Upstream(REPO)
    checks = []

    tmp = Path(tempfile.mkdtemp(prefix="fleet-census-verify-"))
    try:
        src = REPO / "doctrine" / "01-laws.md"
        rel = "doctrine/01-laws.md"
        head_bytes = subprocess.run(
            ["git", "show", f"HEAD:{rel}"], cwd=REPO, capture_output=True, check=False
        ).stdout

        # 1. an untouched HEAD copy must read `current`
        a = tmp / "current.md"
        a.write_bytes(head_bytes)
        checks.append(("current file reads current", up.classify(rel, a)[0] == "current"))

        # 2. the same content with CRLF endings must STILL read `current` (D3)
        b = tmp / "crlf.md"
        b.write_bytes(head_bytes.replace(b"\n", b"\r\n"))
        checks.append(("CRLF copy still reads current", up.classify(rel, b)[0] == "current"))

        # 3. a genuine local edit must read `drifted`
        c = tmp / "edited.md"
        c.write_bytes(head_bytes + b"\nthis line was never upstream\n")
        checks.append(("edited file reads drifted", up.classify(rel, c)[0] == "drifted"))

        # 4. a real older release must read `stale`, not `drifted` — the whole point
        hist = up.history(rel)
        older = None
        head_h = up.head_hash(rel)
        for hh, commit, date in hist:
            if hh != head_h:
                older = (hh, commit, date)
                break
        if older is None:
            checks.append(("older release reads stale", False, "no older version in history"))
        else:
            blob = subprocess.run(
                ["git", "show", f"{older[1]}:{rel}"], cwd=REPO,
                capture_output=True, check=False,
            ).stdout
            d = tmp / "old.md"
            d.write_bytes(blob)
            status, detail = up.classify(rel, d)
            checks.append((
                f"older release reads stale (not drifted) [{older[1]}]",
                status == "stale",
            ))

        # 5. worktree detection must fire on a real worktree layout
        wt = tmp / "wt"
        wt.mkdir()
        (wt / ".git").write_text("gitdir: C:/somewhere/parent/.git/worktrees/wt\n")
        checks.append(("worktree detected", is_worktree(wt) == "C:/somewhere/parent"))

        # 6. and must NOT fire on a normal repo
        nr = tmp / "nr"
        (nr / ".git").mkdir(parents=True)
        checks.append(("plain repo not called a worktree", is_worktree(nr) is None))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    ok = True
    for check in checks:
        name, passed = check[0], check[1]
        note = f"  ({check[2]})" if len(check) > 2 else ""
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}{note}")
        ok = ok and passed
    print(f"\n{sum(1 for c in checks if c[1])}/{len(checks)} verification checks passed")
    return 0 if ok else 1


# --------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--root", default=str(Path(os.path.expanduser("~")) / "Documents"))
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()

    if args.verify:
        return verify()

    root = Path(args.root)
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    totals, drift_index = census(root, verbose=args.verbose)
    genuine = totals["drifted"] + totals["unknown-path"]
    return 1 if genuine else 0


if __name__ == "__main__":
    sys.exit(main())
