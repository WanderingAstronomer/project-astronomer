#!/usr/bin/env python3
"""
verify-census.py — break fleet-census.py on purpose and confirm its --verify notices.

WHY: doctrine/04-verification.md requires that a check be observed FAILING before it is
trusted. fleet-census.py ships its own --verify suite, and a suite that has only ever been
seen green is indistinguishable from one that cannot go red. This script makes it go red on
demand, once per defect, and asserts the right check is the one that fails.

The three defects seeded here are not hypothetical. Each is a mistake that was actually made
while the census was being written or that the design brief it refutes actually made:

  1. LF normalisation removed. This is D3. Without it a raw-byte compare of this corpus
     reported 46 of 47 files changed when 45 were identical, and every Windows instance
     reports total drift forever.

  2. History lookup removed, leaving a two-way clean/drifted split. This is the brief's
     defect: 48 files that are clean older releases get reported as local edits, and the
     operator is handed 48 decisions that are all the same decision.

  3. Worktree detection disabled. Without it one project's three checkouts count as three
     instances and its drift is counted three times. The brief's fleet was inflated this way.

WHAT IT DOES: copies the census into a throwaway tree beside a copy of this repo's .git,
applies one mutation, runs --verify there, and asserts the expected check reported [FAIL].
Nothing in this repository is modified — the mutations are never written to tools/.

Usage:  python tools/verify-census.py
Exit:   0 every seeded defect was caught
        1 a defect slipped through  <-- that check has no teeth
"""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CENSUS = ROOT / "tools" / "fleet-census.py"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NORM = r'return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()'
STALE = (
    '        for hh, commit, date in self.history(rel):\n'
    '            if hh == h:\n'
    '                return "stale", f"{commit} ({date})"\n'
)
WORKTREE = 'if marker in gd.replace("\\\\", "/"):'

SABOTAGES = [
    (
        "LF normalisation removed (D3)",
        NORM,
        "return hashlib.sha256(data).hexdigest()",
        "CRLF copy still reads current",
    ),
    (
        "history lookup removed (the two-way clean/drifted split)",
        STALE,
        "",
        "older release reads stale (not drifted)",
    ),
    (
        "worktree detection disabled (inflates the fleet)",
        WORKTREE,
        "if False:",
        "worktree detected",
    ),
]


def main() -> int:
    src = CENSUS.read_text(encoding="utf-8")
    tmp = Path(tempfile.mkdtemp(prefix="verify-census-"))
    ok = True
    try:
        shutil.copytree(ROOT / ".git", tmp / ".git")
        (tmp / "tools").mkdir()

        # A clean copy must pass first, or a later [FAIL] proves nothing.
        (tmp / "tools" / "fleet-census.py").write_text(src, encoding="utf-8")
        base = subprocess.run(
            [sys.executable, "tools/fleet-census.py", "--verify"],
            cwd=tmp, capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        print(f"[{'PASS' if base.returncode == 0 else 'FAIL'}] unmutated census verifies clean")
        if base.returncode != 0:
            print(base.stdout)
            return 1
        ok = base.returncode == 0

        for name, old, new, expect in SABOTAGES:
            if old not in src:
                print(f"[FAIL] setup: sabotage target not found for {name}")
                ok = False
                continue
            (tmp / "tools" / "fleet-census.py").write_text(
                src.replace(old, new, 1), encoding="utf-8"
            )
            proc = subprocess.run(
                [sys.executable, "tools/fleet-census.py", "--verify"],
                cwd=tmp, capture_output=True, text=True, encoding="utf-8", errors="replace",
            )
            line = next(
                (ln.strip() for ln in proc.stdout.splitlines() if expect in ln),
                "<check not found in output>",
            )
            caught = proc.returncode != 0 and line.startswith("[FAIL]")
            print(f"[{'PASS' if caught else 'FAIL'}] seeded: {name}")
            print(f"         expected to fail : {expect}")
            print(f"         census reported  : {line}")
            ok = ok and caught
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("\nevery seeded defect was caught" if ok else "\na seeded defect slipped through")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
