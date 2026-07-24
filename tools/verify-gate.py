#!/usr/bin/env python3
"""
verify-gate.py — break the corpus on purpose and confirm check-corpus.py notices.

WHY: doctrine/04-verification.md requires that a check be observed FAILING before it is
trusted. A gate that has only ever been seen passing is not known to work — it may be
passing because it is broken, and a check that cannot fail is worse than no check because
it manufactures confidence. rituals/recurring-defect.md states the same rule for gates
specifically: "break it and confirm it fires."

WHAT IT DOES: seeds one mutation per check, runs the gate, asserts the gate fails with the
expected signature, and restores the file. Every mutation is reverted whether or not the
assertion passes — the restore is in a finally block, and the script re-runs the gate at
the end to confirm the corpus is back to green.

Usage:  python tools/verify-gate.py
Exit:   0 every check was observed failing and the corpus was restored
        1 a check did NOT fire when its defect was present  <-- the gate is lying
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GATE = [sys.executable, str(ROOT / "tools" / "check-corpus.py")]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def run_gate() -> tuple[int, str]:
    proc = subprocess.run(GATE, cwd=ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    return proc.returncode, proc.stdout + proc.stderr


def expect_clean(label: str) -> bool:
    code, out = run_gate()
    if code == 0:
        return True
    print(f"  [ERROR] {label}: corpus is not clean to begin with.")
    print("    " + "\n    ".join(out.splitlines()[:12]))
    return False


# --------------------------------------------------------------- mutations

def mutate_vocabulary() -> tuple[Path, str, str]:
    """Drop `append-only` from the doc-status enumeration - the exact D-019 defect."""
    path = ROOT / "doctrine" / "05-the-record.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace(
        "`living` · `frozen` · `append-only` · `disposable`",
        "`living` · `frozen` · `disposable`",
        1,
    )
    if broken == original:
        raise RuntimeError("vocabulary mutation did not apply - the target text moved")
    return path, original, broken


def mutate_prose_count() -> tuple[Path, str, str]:
    """Miscount a vocabulary in a sentence - the form no list-shaped check can see."""
    path = ROOT / "doctrine" / "05-the-record.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace(
        "Astronomer recognizes four classes",
        "Astronomer recognizes three classes",
        1,
    )
    if broken == original:
        raise RuntimeError("prose-count mutation did not apply - the target text moved")
    return path, original, broken


def mutate_template_link() -> tuple[Path, str, str]:
    """Put a framework link back into a template, escaping the project root."""
    path = ROOT / "artifacts" / "charter.template.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace(
        "`doctrine/05-the-record.md`",
        "[`doctrine/05-the-record.md`](../doctrine/05-the-record.md)",
        1,
    )
    if broken == original:
        raise RuntimeError("template-link mutation did not apply - the target text moved")
    return path, original, broken


def mutate_manifest() -> tuple[Path, str, str]:
    """Add a skill to install/README.md that does not exist on disk."""
    path = ROOT / "install" / "README.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace(
        ".claude/skills/astronomer-record/SKILL.md",
        ".claude/skills/astronomer-record/SKILL.md\n.claude/skills/astronomer-phantom/SKILL.md",
        1,
    )
    if broken == original:
        raise RuntimeError("manifest mutation did not apply - the target text moved")
    return path, original, broken


def mutate_link() -> tuple[Path, str, str]:
    """Point a real link at a file that does not exist."""
    path = ROOT / "doctrine" / "README.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace("(01-laws.md)", "(01-laws-renamed.md)", 1)
    if broken == original:
        raise RuntimeError("link mutation did not apply - the target text moved")
    return path, original, broken


MUTATIONS = [
    ("vocabulary drift   (D-019: a record class goes missing from a list)",
     mutate_vocabulary, r"\[vocab:record_class\].*missing: append-only"),
    ("counted prose      (a sentence miscounts a vocabulary)",
     mutate_prose_count, r"\[vocab:record_class\].*prose counts 3 'classes'"),
    ("install manifest   (a listed skill has no directory)",
     mutate_manifest, r"\[manifest\].*astronomer-phantom.*does not exist on disk"),
    ("broken link        (a doctrine file is renamed, references are not)",
     mutate_link, r"\[link\].*01-laws-renamed\.md"),
    ("template link      (a template link escapes the project root)",
     mutate_template_link, r"\[link\].*escapes the project root"),
]


def main() -> int:
    print("Verifying the gate by breaking the corpus on purpose.\n")

    if not expect_clean("precondition"):
        return 1

    all_fired = True
    for label, mutate, signature in MUTATIONS:
        path, original, broken = mutate()
        try:
            path.write_text(broken, encoding="utf-8", newline="")
            code, out = run_gate()
            fired = code != 0 and re.search(signature, out) is not None
            status = "FIRED " if fired else "SILENT"
            print(f"  [{status}] {label}")
            if not fired:
                all_fired = False
                print(f"    expected output matching: {signature}")
                print("    " + "\n    ".join(out.splitlines()[:12]))
        finally:
            path.write_text(original, encoding="utf-8", newline="")

    print()
    if not expect_clean("restore"):
        print("The corpus was NOT restored cleanly. Check `git diff` before continuing.")
        return 1
    print("Corpus restored and clean.\n")

    if not all_fired:
        print("GATE VERIFICATION FAILED - at least one check did not notice its own "
              "defect. The gate is reporting success it has not earned (L-16).")
        return 1

    print("GATE VERIFICATION PASSED - every check was observed failing on a real defect "
          "and passing without it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
