---
record_class: living
precedence: 6
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <operator-known-errors>
  - <operator-preferences>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# OPERATOR PROFILE — `<operator>` — `<YYYY-MM-DD>`

> **Doc class:** living. Rewritten when the operator's tooling or condition changes, and **re-dated
> every time**. A profile with no date is a claim about a person as they were.

**Required at:** **Lite, conditional** — gated on a condition, not a tier: required whenever the
operator's input reaches the collaborator through **augmentation** rather than directly. Typing into
a chat window is direct. Anything that transcribes, dictates, translates, summarizes, batches, or
otherwise reshapes intent before it arrives is augmentation, and it changes what arrives in ways the
collaborator will otherwise misread as the operator's own voice.

This is the twin of the capability inventory (`artifacts/capability-inventory.template.md`). That
artifact declares the **collaborator's** error, because the collaborator is an instrument (L-18).
This one declares the **operator's**, because `doctrine/06-delegation.md` established first and most
plainly that *the operator is the instrument* — and then never gave that instrument a place to state
its error.

> **Status: single-authored and provisional (D-006).** No source project ran an augmented operator,
> so nothing here is attested by independent convergence. It is a structural argument — the operator
> is an instrument, instruments declare their error (L-18) — plus one project's observations. Amend
> it from what actually bites.

## Why this exists

A collaborator reads what arrives and infers the person from it. Every one of those inferences is
wrong in a specific direction when the input has been reshaped on the way in, and none of them
announce themselves:

- Length reads as emphasis. Under dictation it is often just **fluency**.
- Structure reads as deliberation. If a tool imposed the structure, the deliberation may be the
  tool's.
- A single long message reads as a single ask. It is frequently **many**, and the ones in the middle
  are the ones that get dropped.
- High input volume reads as high engagement, and therefore as high **review** capacity. Those are
  different resources and are frequently opposite.

State the augmentation once, here, and let the collaborator derive the rest at read time. Do not
enumerate the derivations — see the last section for why.

## What to state

### 1. The augmentation

`<What stands between the operator's intent and what the collaborator receives. Name the mechanism,
not the brand — the profile survives the tool.>`

Cover, if they apply: how input is produced; whether it is transcribed or typed; whether anything
post-processes it before it arrives; whether that post-processing is **configurable by the operator**
and configured differently for different kinds of work; and how much of the operator's total input
arrives this way. *Roughly all of it* and *some of it* imply very different defaults.

### 2. The shape of what actually arrives

| | |
|---|---|
| **Typical length** | `<a sentence / a page / twenty minutes of speech>` |
| **Topics per message** | `<one / several / many, unsignalled>` |
| **Pre-structured?** | `<raw stream / structured by a tool / structured deliberately by the operator>` |
| **Self-corrections mid-message** | `<rare / common — and are they marked?>` |
| **Fidelity of the record** | `<verbatim / cleaned / summarized — and is the original still available?>` |

The **topics-per-message** row is the one that changes behaviour most and is least visible. A
channel that reliably carries many items per message needs an explicit coverage pass, because
answering the last paragraph *feels* like answering the message.

### 3. Bandwidth asymmetry — the load-bearing row

`<Input capacity versus review capacity, stated as an asymmetry rather than a level.>`

An operator who can produce far more instruction than they can afford to review is not a
high-throughput operator; they are a **bottlenecked** one, and the bottleneck has moved to a place
the collaborator can accidentally flood. This is the fact from which delegation depth should be
derived, and it is why decision rights are a capability to be set once (K-5,
`doctrine/08-instruments.md`) rather than negotiated per exchange.

State it in a form that can be acted on: *"can produce an hour of specification in a sitting; can
review perhaps three substantive artifacts a day."*

### 4. Known error, with direction

`<Where this operator's reporting is systematically strong, and where it is thin — in a direction
you can subtract.>`

Not modesty boilerplate, and not a character assessment. The same standard the capability inventory
holds itself to: a usable entry names the bias and its direction.

> Example of the form: *"Ordering is reliable within a topic and unreliable across topics — the
> sequence of steps inside one problem is trustworthy; the relative priority of two problems raised
> in the same message is not, and should be confirmed rather than inferred from the order they were
> spoken in."*

Include, where they apply: what the operator reliably notices and reliably does not; whether
strength of language tracks strength of preference; and whether an unanswered question in a long
message means *not important* or means *lost*.

### 5. Settled preferences — a pointer, not a copy

`<Where the operator's already-elicited preferences live.>`

They live in the **decision ledger** and are cited from here (L-14). Copying them into this file
creates a second home for a fact whose whole value is having one, and this artifact is rewritten
often enough that the copy would drift within a month.

### 6. What follows — derived at read time, not listed here

`<Nothing. This section is deliberately empty of content and is not a placeholder to fill.>`

The implications of sections 1–4 are **derived by the session that reads them**, against the work in
front of it. They are not enumerated in advance, for the reason the framework refuses to enumerate
cadence: a fixed list of behaviours goes stale against a living operator, gets followed after it
stops being true, and is the more dangerous failure precisely because it looks like diligence.

What the collaborator owes this artifact is a **reading**, not a lookup. If a derivation turns out to
be load-bearing and recurring, it does not belong here either — it belongs in the ledger as a
decision, or in a project runbook as a procedure.

## Forbidden

- **Inferring the augmentation from the writing.** It cannot be done reliably and the failure is
  silent. Ask.
- **Copying this forward without re-measuring.** Same prohibition, same reason, as the capability
  inventory. People change and their tooling changes faster.
- **Writing that the operator has no known error.** That is not a profile.
- **Treating a long input as one ask** when section 2 says otherwise. The middle items are the ones
  that vanish, and the operator will not always notice they vanished.
- **Recording anything the operator has not agreed to.** This is a document about a person. It is
  written *with* them, shown to them, and corrected by them — an inferred profile they have never
  read is a set of assumptions with a filename.
- **Using it as an excuse.** A known error is subtracted, not invoked. "The input was long" does not
  discharge the obligation to answer all of it.

## Lifecycle

Written at setup, inside `rituals/capability-interrogation.md`, alongside the capability inventory —
the two halves of the same question, asked at the same time. Rewritten and re-dated when the
operator's tooling, capacity, or condition changes. Never frozen: a stale profile about a person is a
live risk, not a historical record.

When a stated bias turns out to be wrong, that correction goes in the decision ledger, because work
shaped around the old assumption may need re-checking.
