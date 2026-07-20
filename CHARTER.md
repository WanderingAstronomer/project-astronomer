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
3. **The framework is a hypothesis until a project proves it.** This corpus is `PROVISIONAL`
   and says so in public. It does not claim validation it has not earned. (D-001)
4. **Provenance is a first-class column.** Every pattern names the project it came from. A
   pattern attested in one project is a practice; attested in three independently is a law.
   (D-006, inherited from data-dating)
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
| Precedence clause — "this document wins" (fractalized-rag, data-dating, vociferous) | This charter, and [`doctrine/00-precedence.md`](doctrine/00-precedence.md) |
| Append-only decision ledger, supersede-by-name (data-dating, vociferous) | [`DECISIONS.md`](DECISIONS.md), verbatim format |
| Frozen vs living records (all four) | This charter and doctrine are living; `provenance/` is frozen |
| Epistemic typing of claims (all four, independently) | [`doctrine/02-epistemics.md`](doctrine/02-epistemics.md) — the framework's core |
| Observe read-only before intervening (OpenDrop, vociferous) | [`doctrine/03-the-loop.md`](doctrine/03-the-loop.md) |
| Pre-registered numeric acceptance criteria (fractalized-rag, OpenDrop) | Definition of done, below |
| "What this does NOT specify" (fractalized-rag §11) | Scope, above, and the Status note in the README |
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
6. **A real project outside this repo has run one full OBSERVE→RECORD loop on it, and the
   friction it hit is written back here as a ritual or an amendment.**

Conditions 1–5 are met at seeding. **Condition 6 is not met and is the only thing standing
between this corpus and `VALIDATED`.** Until it is met, this framework is a well-argued guess.
