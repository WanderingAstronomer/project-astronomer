---
name: astronomer-decide
description: Append an entry to the decision ledger — use whenever a call is made, a prior decision is reversed or amended, an approach is chosen over an alternative, or the operator says "let's go with" anything.
---

# Append a decision

Purpose: make a call resumable by a stranger, including the operator in six months. The ledger is
append-only and it is the cheapest high-value artifact in the framework.

## Step 1 — take a live timestamp. Always.

Run the shell call. Every time. Never an ambient date, never the date in the conversation
context, never a date you remember from earlier in the session.

```
date -u +"%Y-%m-%dT%H:%MZ"
```
```
(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mmZ")
```

Injected dates drift, and a ledger ordered by drifting timestamps cannot be resolved — which
disables the supersession chain, the one mechanism that makes the ledger trustworthy at all.

## Step 2 — allocate the next ID

`D-<n>`, sequential, never reused. Read the end of the ledger to find the last one. If two
decisions are made at once they get two entries; a compound entry cannot be superseded cleanly.

## Step 3 — write the entry

```
[<live UTC>] D-<n>: **<the decision, as a decision>** — <why>
```

The decision is one sentence in the imperative or declarative, not a description of a discussion.
The reason is what a reader needs to disagree with you competently: the alternative considered,
the evidence, and what would change the call.

Tags, applied where they apply:

- **`[operator]`** — the human made this call, not you. Put it immediately before the decision
  text. The boundary is recorded, never assumed. If you are unsure who owns a call, ask; do not
  mark it either way by default.
- **`blocks-on:`** — the decision rests on evidence not yet proven. Name what would settle it.
  The entry stays `OPEN` until then.
- **`caveat (owned):`** — state the weakness yourself: the control you did not run, the sample
  you did not check, the shortcut you knowingly took, and who chose it. An owned caveat is a
  durable asset; an unstated one is a landmine with your fingerprints on it.
- **`next:`** — a condition under which this is revisited.

## Step 4 — supersession, by naming only

A later decision overrides an earlier one **only when it names the one it replaces**. Recency
alone never wins. Write `Supersedes D-<n>.` inside the new entry.

- Never edit the superseded entry. It stays exactly as written.
- To correct rather than replace, append a new stamped line: `AMENDS D-<n>: <what changed>`.
- Bare `D-<n>` resolves to **this project's ledger only**. Any cross-project reference is
  namespaced with a prefix. An ambiguous bare reference is a supersession hazard.

## Forbidden

- Editing, reflowing, renumbering, or tidying any prior entry. Append-only means append-only.
- Deleting a decision that turned out wrong. A reversal is a new entry that names it.
- Marking a decision `[operator]` that the operator did not actually make.
- Recording a decision that belongs to the operator — identity, custody, acceptance, physical
  fact, or preference — as though you made it. Stop and ask instead.
- Stamping from anything but a live reading.

## Confirm

Echo the appended entry back, and state the ID, the live stamp you read, whether it supersedes
anything, and any open `blocks-on:`.
