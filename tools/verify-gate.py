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


def mutate_attestation_grade() -> tuple[Path, str, str]:
    """Claim `settled` on evidence that does not support it.

    L-3 is the only law in the registry at four sources, so `"count": 4` is unique and this
    mutation cannot land on the wrong entry. Dropping it to 2 makes the entry claim `settled`
    on a `converging` count AND desynchronises count from the source list, so it also proves
    the count-versus-sources assertion. This is the corpus overstating its own evidence, which
    is the exact defect the check was added for (D-039).
    """
    path = ROOT / "provenance" / "attestation.json"
    original = path.read_text(encoding="utf-8")
    broken = original.replace('"count": 4', '"count": 2', 1)
    if broken == original:
        raise RuntimeError("attestation mutation did not apply - the target text moved")
    return path, original, broken


def mutate_attestation_sunset() -> tuple[Path, str, str]:
    """Strip the sunset off a provisional law - the accumulation failure D-039 closed.

    L-18's would_attest is targeted by its opening words, which appear nowhere else.
    """
    path = ROOT / "provenance" / "attestation.json"
    original = path.read_text(encoding="utf-8")
    broken = re.sub(
        r'"would_attest": "A second project that independently requires an instrument[^"]*"',
        '"would_attest": ""',
        original,
        count=1,
    )
    if broken == original:
        raise RuntimeError("sunset mutation did not apply - the target text moved")
    return path, original, broken


def mutate_header_missing() -> tuple[Path, str, str]:
    """Strip a living document's header block entirely."""
    path = ROOT / "rituals" / "corpus-retrieval.md"
    original = path.read_text(encoding="utf-8")
    end = original.find("\n---", 3)
    if not original.startswith("---") or end == -1:
        raise RuntimeError("header mutation did not apply - no block to strip")
    broken = original[end + 5:].lstrip("\n")
    return path, original, broken


def mutate_header_class() -> tuple[Path, str, str]:
    """Put a value in record_class that is not in the record_class vocabulary."""
    path = ROOT / "rituals" / "corpus-retrieval.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace("record_class: living", "record_class: evergreen", 1)
    if broken == original:
        raise RuntimeError("header class mutation did not apply - the target text moved")
    return path, original, broken


def mutate_header_confirmed_uncited() -> tuple[Path, str, str]:
    """Claim CONFIRMED and delete the citation it obliges.

    This is the one that matters. 02-epistemics.md defines CONFIRMED as independently
    re-derived, CITE WHERE -- and until this check existed, nothing anywhere made the second
    half of that sentence cost anything.
    """
    path = ROOT / "rituals" / "corpus-retrieval.md"
    original = path.read_text(encoding="utf-8")
    broken = re.sub(r"(?m)^verified_by: .*\n", "", original, count=1)
    if broken == original:
        raise RuntimeError("header citation mutation did not apply")
    return path, original, broken


def mutate_header_two_homes() -> tuple[Path, str, str]:
    """Two documents claim the same fact -- L-14, made mechanical.

    The defect this whole corpus keeps re-committing (AMENDS D-015, D-019), aimed at for the
    first time by a check that does not need a reader to already know where the home is.
    """
    path = ROOT / "rituals" / "corpus-retrieval.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace(
        "  - corpus-retrieval-procedure",
        "  - corpus-retrieval-procedure\n  - corpus-intake-procedure",
        1,
    )
    if broken == original:
        raise RuntimeError("two-homes mutation did not apply - the target text moved")
    return path, original, broken


def mutate_id_collision() -> tuple[Path, str, str]:
    """Two ledger entries claim one address - the four-way D-103 collision, in miniature."""
    path = ROOT / "DECISIONS.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace("] D-002:", "] D-001:", 1)
    if broken == original:
        raise RuntimeError("id collision mutation did not apply - the entry form moved")
    return path, original, broken


def mutate_id_blind() -> tuple[Path, str, str]:
    """Change the entry form so the pattern matches nothing.

    The failure this guards is a gate reporting `0 collisions` because it can no longer see
    any IDs -- which reads exactly like a clean corpus. O-41: a passing suite is evidence
    about the suite before it is evidence about the code.
    """
    path = ROOT / "OBSERVATIONS.md"
    original = path.read_text(encoding="utf-8")
    broken = re.sub(r"(?m)^### `O-(\d+)`", r"### O-\1", original)
    if broken == original:
        raise RuntimeError("id blindness mutation did not apply")
    return path, original, broken


def mutate_id_dangling_amendment() -> tuple[Path, str, str]:
    """Amend a decision that was never made."""
    path = ROOT / "DECISIONS.md"
    original = path.read_text(encoding="utf-8")
    broken = original.replace("AMENDS D-015:", "AMENDS D-999:", 1)
    if broken == original:
        raise RuntimeError("dangling amendment mutation did not apply")
    return path, original, broken


def mutate_template_rule() -> tuple[Path, str, str]:
    """Drop the namespacing rule from the always-loaded file, leaving it only in the README.

    That is not a hypothetical: it was the corpus's actual state until 2026-08-01, and it took a
    consuming project's session writing a bare `D-044` beside an `AST-D-049` to surface it.
    """
    path = ROOT / "install" / "CLAUDE.md.template"
    original = path.read_text(encoding="utf-8")
    broken = re.sub(r"AST-D-", "D-", original)
    if broken == original:
        raise RuntimeError("template rule mutation did not apply - the rule text moved")
    return path, original, broken


MUTATIONS = [
    ("vocabulary drift   (D-019: a record class goes missing from a list)",
     mutate_vocabulary, r"\[vocab:record_class\].*missing: append-only"),
    ("template rule      (a session-critical rule lives only in the README)",
     mutate_template_rule,
     r"\[template\].*does not carry the AST- ledger namespacing rule"),
    ("id collision       (two ledger entries claim one address)",
     mutate_id_collision, r"\[id\] DECISIONS\.md: ledger entry 'D-001' is allocated 2 times"),
    ("id blindness       (the entry form moves and the check sees nothing)",
     mutate_id_blind, r"\[id\] OBSERVATIONS\.md: found no observation IDs at all"),
    ("id dangling amend  (an amendment with no subject)",
     mutate_id_dangling_amendment, r"\[id\] DECISIONS\.md:\d+ amends 'D-999'"),
    ("header absent      (a living document carries no header block)",
     mutate_header_missing, r"\[header\] rituals/corpus-retrieval\.md has no header block"),
    ("header class       (record_class is not in the vocabulary)",
     mutate_header_class, r"\[header\].*record_class 'evergreen' is not in"),
    ("header citation    (CONFIRMED with nothing to cite)",
     mutate_header_confirmed_uncited,
     r"\[header\].*claims confidence: CONFIRMED but has no 'verified_by'"),
    ("header two homes   (L-14: one fact claimed by two documents)",
     mutate_header_two_homes,
     r"\[header\] L-14: 'corpus-intake-procedure' is claimed by both"),
    ("counted prose      (a sentence miscounts a vocabulary)",
     mutate_prose_count, r"\[vocab:record_class\].*prose counts 3 'classes'"),
    ("install manifest   (a listed skill has no directory)",
     mutate_manifest, r"\[manifest\].*astronomer-phantom.*does not exist on disk"),
    ("broken link        (a doctrine file is renamed, references are not)",
     mutate_link, r"\[link\].*01-laws-renamed\.md"),
    ("template link      (a template link escapes the project root)",
     mutate_template_link, r"\[link\].*escapes the project root"),
    ("attestation grade  (a law claims settled on converging evidence)",
     mutate_attestation_grade, r"\[attestation\] L-3 claims count 2 but lists 4 source"),
    ("attestation sunset (a provisional law loses its path out of provisional)",
     mutate_attestation_sunset, r"\[attestation\] L-18 is graded 'practice' with no"),
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
