---
record_class: living
precedence: 1
confidence: CONFIRMED
owns:
  - the-mission
  - the-invariants
  - the-definition-of-done
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# CHARTER — Project Astronomer

> This is the top of the authority stack. If anything else in this corpus conflicts with this
> charter, **the charter wins.** Amend it deliberately, with a dated entry in
> [`DECISIONS.md`](DECISIONS.md) — never silently.

## Mission

Extract, name, and make installable the operating methodology that four unrelated projects
independently converged on, so that it can be applied to a new project on day one instead of
rediscovered over eighteen months.

The measure of success is not that the framework is admired. It is that a project built on it
reaches a correct conclusion faster, and knows which of its conclusions are load-bearing.

## Scope

**In scope**

- The doctrine: laws, epistemics, the operating loop, verification, recording, delegation.
- The artifact set: templates with a stated purpose, structure, and lifecycle.
- Tiering: which artifacts are required at which stakes level.
- The install layer: making an AI collaborator enforce the doctrine in-session.
- Provenance: which source project each pattern came from, and what it cost to learn.

**Out of scope (for now)**

- Any domain-specific content. No health metrics, no software idioms, no dating heuristics.
  Domain material belongs in the project that consumes Astronomer, never here. (D-004)
- Tooling that generates or validates projects. A CLI would calcify the framework before a
  single project has proven it. (D-005)
- Retrofitting the four source projects onto the framework. They are the evidence, not the
  customers.

## Invariants — do not violate

1. **The framework must survive a non-software project.** Any law, artifact, or ritual that
   cannot be stated without reference to code, tests, or repositories is not doctrine — it is
   a software idiom, and belongs in an appendix, if anywhere. (D-002)
2. **Every law carries its scar.** No rule is stated without the concrete failure that
   produced it. A rule without its incident gets argued away the first time it is expensive.
   (D-003, inherited from vociferous)
3. **The framework is a hypothesis until a project proves it.** One has now: this corpus is
   `VALIDATED` as of `2026-08-01` (D-049, `AMENDS D-001`), on condition 6 and nothing wider.
   It does not claim validation it has not earned — and **ratification is not attestation.**
   Every law still rests on exactly the source projects it names, and the framework's newest
   rules still rest on one. (D-001, D-049)
4. **Provenance is a first-class column.** Every pattern names the project it came from, and
   carries a **grade** for how much evidence stands behind it: `practice` (one independent
   project), `converging` (two), `settled` (three or four). The grade is separate from whether
   a rule *binds* — every law binds at every tier regardless of grade
   ([`doctrine/01-laws.md`](doctrine/01-laws.md)). The middle grade was added by D-039: the
   original wording named only one and three, and the largest group of laws sat at two, in a
   category this invariant did not define. Grades live in
   [`provenance/attestation.json`](provenance/attestation.json) and are checked mechanically.
   (D-006, inherited from data-dating; extended by D-039)
5. **Astronomer governs itself.** This repo maintains its own charter and ledger under its own
   rules. Where the framework is inconvenient to its own authors, that is recorded, not
   smoothed. (D-007)
6. **Tiers may add artifacts; they may never relax a law.** Lite is smaller, not looser.
   (D-008)
7. **No fiction.** A document describing something not yet built says so, in that document,
   at the top. (Inherited from vociferous: "strip fiction; state current truth.")

## Methodology — inherited patterns and how they map

| Inherited pattern (source) | Mapping here |
|---|---|
| Precedence clause — "this document wins" (<instance-F>, data-dating, vociferous) | This charter, and [`doctrine/00-precedence.md`](doctrine/00-precedence.md) |
| Append-only decision ledger, supersede-by-name (data-dating, vociferous) | [`DECISIONS.md`](DECISIONS.md), verbatim format |
| Frozen vs living records (all four) | This charter and doctrine are living; `provenance/` is frozen |
| Epistemic typing of claims (all four, independently) | [`doctrine/02-epistemics.md`](doctrine/02-epistemics.md) — the framework's core |
| Observe read-only before intervening (OpenDrop, vociferous) | [`doctrine/03-the-loop.md`](doctrine/03-the-loop.md) |
| Pre-registered numeric acceptance criteria (<instance-F>, OpenDrop) | Definition of done, below |
| "What this does NOT specify" (<instance-F> §11) | Scope, above, and the Status note in the README |
| Shared preamble included by reference (vociferous) | [`artifacts/shared-preamble.template.md`](artifacts/shared-preamble.template.md) |

## Definition of done (v0)

Astronomer v0 is complete when all of the following are true. Each is a testable predicate,
not a feeling.

1. Every law in `doctrine/01-laws.md` cites at least two independent source projects, or is
   explicitly marked single-attested.
2. Every artifact template states its purpose, its structure, its lifecycle, and the tier at
   which it becomes required.
3. Every tier lists its required artifacts explicitly, and no tier omits a law.
4. `provenance/lineage.md` maps every doctrine section to the source project(s) it came from,
   with no unattributed patterns.
5. The install layer can be dropped into an empty repository and produce a working Lite
   project without editing any file in this repo.
6. **RATIFICATION — a real project outside this repo has run one full OBSERVE→RECORD loop on
   it, and the friction it hit is written back here as a ritual or an amendment.**

   Named as ratification by D-041, because that is what it is and calling it a checklist item
   understated it. **This corpus is case law** ([`doctrine/01-laws.md`](doctrine/01-laws.md)),
   and case law is ratified by practice rather than by assent. Neither the operator nor a
   collaborator can satisfy this condition by agreeing to it — only a project running the loop
   can, which is why it is the one condition that has never moved while the other five were
   met, corrected, and met again.

### Status — corrected 2026-07-24

The seeded version of this section read *"Conditions 1–5 are met at seeding."* **Two of them were
not**, and neither was found by anyone checking the claim — both surfaced in the corpus's first
self-survey, four days later:

- **Condition 2** — ten of twelve artifact templates stated no required-at tier anywhere in the
  file. A template copied whole into a project carried no statement of the tier that required it.
  Now stated in all fifteen.
- **Condition 4** — [`provenance/lineage.md`](provenance/lineage.md) had no provenance rows for the
  entire `rituals/` layer, the Friction/Conflagration vocabulary, the `artifacts/` template set, or
  the `Append-only` record class added by D-019. Addressed by dated addendum, since that file is
  frozen and is annotated rather than edited (L-13).

Conditions 1, 3, and 5 were met at seeding and remain met. **Conditions 1–5 are met as of
2026-07-24** (D-033).

This correction is stated rather than applied quietly, because a charter asserting a condition it
has not met is precisely the defect class L-16 puts above breakage — *a thing that is broken and
says so is safe; a thing that is broken and reports success is not* — and silently satisfying the
conditions afterward would have been the same defect in a quieter form.

### Condition 6 — met `2026-08-01`

**All six conditions are now met, and the corpus is `VALIDATED`** (D-049). What discharged it,
stated precisely enough to be argued with:

`vociferous-next` installed Astronomer at Full tier on `2026-07-27` and ran a full
OBSERVE→RECORD loop on it between then and `2026-08-01`. The loop that closes the condition is its
`2026-07-30` window: opened `18:32Z`, four entries, `INTAKE CLOSED` at `18:38Z`; one item resolved
to a `CONFIRMED` cause with a citation; a **gate built rather than a ninth hand-fix** under L-17;
and the outcome recorded in its ledger, its living documents, and its operating instructions.
Verified here rather than accepted: that gate's falsifier suite was run from this session on
`2026-08-01` and **8 of 8 passed, measured**. The friction is written back as `O-31`–`O-44`, one
new capability rule, one new ritual, two new gate checks and five amended documents.

**Three things this does not mean**, each of which would be easy to read into it:

1. **Ratification is not attestation.** Condition 1 is about how many independent projects arrived
   at each law; this is about whether the framework survives being *used*. No grade in
   `provenance/attestation.json` moves, and the file was not touched.
2. **The ratifying project is one of the four sources.** Condition 6 says *outside this repo*, and
   `vociferous-next` is outside this repo — the condition is met as written. But it is not outside
   the framework's provenance, and a framework being run by a project it was partly extracted from
   is the weakest form of ratification that still satisfies the condition. **Recorded rather than
   smoothed** (invariant 5). The strong form — a project with no hand in writing this — has not
   happened, and `D-049` names it as what would raise the grade further.
3. **`VALIDATED` is not `finished`.** It is the status the definition of done defines, nothing
   more. The corpus acquired four new unresolved questions in the same pass that ratified it; they
   are listed in `doctrine/08-instruments.md` under what that file does not settle.

### Checking conditions 2, 3, and 4 mechanically

Parts of the above are now machine-checkable, because they drifted twice before anything caught
them (D-025):

```bash
python tools/check-corpus.py --verbose
```

Vocabulary membership, the install manifest, and every relative link. It is run by hand — automating
it moves toward the tooling D-005 bars — and it is itself verified by `tools/verify-gate.py`, which
seeds a real defect per check and asserts the gate fails. See
[`tools/README.md`](tools/README.md) for what it deliberately does not check.
