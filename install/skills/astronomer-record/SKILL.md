---
name: astronomer-record
description: Close a loop — use after a change has landed and been evaluated, at the end of an investigation or session, or whenever the operator asks to write something up, wrap up, or capture what happened.
---

# Record

Purpose: make it so a stranger — including the operator in six months — can reconstruct what
happened and what it means. Recording is its own phase because it is the first thing dropped
under pressure. The loop has not closed until all three outputs below exist; missing one means it
stopped, not that it closed.

## Output 1 — freeze the point-in-time record

Write a dated frozen record: `<name>-<YYYY-MM-DD>.md`, marked `frozen` at the top, stamped from a
live UTC reading (`date -u`) and never an ambient date.

It holds what was believed and observed **at this moment**. Once written it is annotated, never
edited. A later correction is an addendum that notes what changed without re-running or revising
the original — a research document quietly updated becomes a document that appears to have been
right all along, which destroys its value as evidence of what you knew and when.

Use the recording voice:

```
Subject:  the outcome — what is now true, stated as a result, not a task
Line 1:   the defect as a causal narrative — mechanism → consequence, in one sentence
Body:     what changed, grouped by area
Then:     verification evidence — what was checked, and at what altitude
Then:     what is still owed, and to whom
```

Line 1 carries the value, and it is the line most often written as a task instead. *"Fixed the
readout"* records that you were busy. *"The readout was fed one quantity and labelled with the
name of another"* records a mechanism — and a reader six months later learns something from the
second that the first cannot give them. Write the mechanism.

## Output 2 — update the living document to current reality

Rewrite the specification, catalog, or protocol so it states **what IS** — not how it got that
way. Strip any change-log the document has accreted. History lives in the ledger and the frozen
records; a living document that narrates its own timeline has to be reconstructed to be read.

Where the living document and a frozen record now conflict: the living one wins on fact, the
frozen one stands as history, and **neither file changes** to accommodate the other.

## Output 3 — append the decision

Run `astronomer-decide`. Live stamp, next `D-<n>`, the reason, `[operator]` if the human made the
call, `caveat (owned):` for anything you knowingly skipped.

## Record what was not verified

A named section, always present, never empty by omission. For each item: what was not checked,
why, and who it is owed to. "Owed by a human" is an expected and acceptable outcome.

State the **grade** of everything you did verify — proven in the real environment / checked in a
proxy / reasoned from the source. Collapsing the three into "verified" overstates the work while
every individual sentence stays true.

## Record what you got wrong

Including about your own work:

- Hypotheses `REFUTED` during the loop — kept, marked, with their original stamps. A record that
  quietly drops its wrong calls cannot be trusted about its right ones.
- Defects found inside your own output. A report with none has probably not looked.
- Judgement calls made without the operator, flagged *"reverse this if wrong."*
- Anything found outside your declared scope: cited, untouched, left that way.

## Forbidden

- Editing a frozen record, or a prior ledger entry, for any reason.
- Letting a living document keep a dated change-log.
- Deleting a spent plan or prompt. Banner it: `EXECUTED <date> — kept as a template.` The plan is
  the only surviving statement of what you *intended* — exactly what is needed when the outcome
  disappoints and you are working out whether the plan or the execution failed.
- Reporting success that was not achieved, or a number you did not measure this session.

## Close

State the three outputs and where they live, the token on each conclusion, and the shortest
honest sentence about what remains open.
