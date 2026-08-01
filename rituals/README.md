---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - blast_radius
  - the-ritual-routing-table
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Rituals

> **Doc status:** living.

Lightweight routable procedures for recurring frictions. When a session recognizes a known
situation, it routes here instead of improvising a response to it for the third time.

Every ritual has the same three parts and nothing more:

- **When** — how you recognize you are in this situation.
- **Do** — numbered steps.
- **Record** — what gets written, where, and into which ledger. Every ritual ends by writing its
  outcome down; a ritual that leaves no trace did not run.

Rituals hold the steps. [`doctrine/`](../doctrine/) holds the reasoning. **A ritual never
overrides a law.** If one appears to, the ritual is wrong and gets corrected —
[`doctrine/00-precedence.md`](../doctrine/00-precedence.md), and the charter above it.

## Routing table

| Situation | Ritual | Blast radius |
|---|---|---|
| "I am starting something and nothing has been declared yet." | [starting-a-project](starting-a-project.md) | — |
| "I have been handed a pile of documents I did not write." | [corpus-intake](corpus-intake.md) | Friction → Conflagration once a finding is published from a corpus whose coverage was never recorded |
| "I am about to search the corpus and act on what comes back." | [corpus-retrieval](corpus-retrieval.md) | Friction → Conflagration when the search is part of a repair already in progress |
| "I need to look at this properly before I touch it." | [observation-pass](observation-pass.md) | — |
| "I need to know something the project cannot observe for itself." | [external-research](external-research.md) | Friction |
| "The window is closed and I have a pile of raw entries." | [triage-pass](triage-pass.md) | — |
| "The cause I wrote down turns out to be wrong." | [hypothesis-refuted](hypothesis-refuted.md) | Conflagration |
| "This is far bigger than I declared it was." | [scope-surprise](scope-surprise.md) | Conflagration |
| "This document no longer describes reality." | [settling-a-document](settling-a-document.md) | Friction → Conflagration once the drift spans files |
| "Two rules are live and they disagree." | [conflicting-decisions](conflicting-decisions.md) | Friction → Conflagration once work rests on the losing entry |
| "That is the third time this has happened." | [recurring-defect](recurring-defect.md) | Conflagration |
| "I tried to determine the cause and I could not." | [unresolved](unresolved.md) | Friction |
| "I never measured this number. Someone else did, some time ago." | [instrument-drift](instrument-drift.md) | Friction → Conflagration once a decision rested on it |
| "Before I plan any of this — what can this environment actually do, and what am I allowed to do with it?" | [capability-interrogation](capability-interrogation.md) | Friction → Conflagration once a plan rests on a capability nobody measured |
| "The small version worked. Do I commit to the large one?" | [scale-up-gate](scale-up-gate.md) | — |

## Blast radius

**Friction** — a recoverable snag, handled inside the session that hit it.
**Conflagration** — a fire that ripples across work already planned. Stop, assess what rests on
it, and expect to re-plan rather than to patch.

This axis is deliberately **not** called severity. Astronomer already fixes a per-item severity
vocabulary (`stop` · `major` · `minor` · `question`) whose home is
[`doctrine/05-the-record.md`](../doctrine/05-the-record.md), and two live scales sharing one word
is precisely the drift L-14 exists to prevent. Blast radius asks *how far does this reach*;
severity asks *how much does this matter*. They are orthogonal — a `minor` item can be a
Conflagration if six decisions rest on it.

*This column was renamed after a review pass caught the collision. The original framing
documented the clash instead of removing it, which leaves the mechanism intact (L-17).*

The scheduled rituals — `starting-a-project`, `observation-pass`, `triage-pass`, and
`scale-up-gate` — carry no blast radius: they are procedures you run on purpose, not responses to
something going wrong. `corpus-intake` and `external-research` sit between the two kinds: scheduled,
but each with a way of going wrong that reaches past the session.

## Growth rule

**New friction with no ritual → write a new one here, same shape.** Three parts, 20–40 lines,
domain-neutral, laws cited by ID. Add a row to the table above. Do not write an essay; if the
reasoning needs more than a sentence, it belongs in doctrine and the ritual links to it.

This is also how the framework earns its validation: the charter's definition of done requires
that friction met by a real project is **written back here** (CHARTER, §6).

**Ritual or runbook?** A ritual is framework-level and domain-neutral — it ships with Astronomer
and applies to every project. A runbook is project-level and domain-specific, and appears the
second time *that project* hits *that* friction ([`tiers/`](../tiers/README.md), Standard). If the
procedure cannot be written without naming your subject, it is a runbook and it belongs in your
project, not here (D-004).

## These are living documents

Rituals are rewritten freely to match how the work is actually done. They state what the
procedure *is*, never how it evolved — the ledger holds that. A ritual that has been followed
twice and worked both times is still provisional; a ritual nobody follows is a defect in the
ritual, not in the people.
