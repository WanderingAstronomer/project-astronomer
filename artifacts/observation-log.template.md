---
record_class: append-only
precedence: 5
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <the-observation-log>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# OBSERVATION LOG — `<project name>` — `<window name>`

> **Doc class:** append-only — its own class, not a flavour of frozen (D-019). **Nothing in this
> file is ever edited or reordered.**
> Corrections arrive as new entries that name the entry they correct. If an entry turns out to be
> wrong, that is a fact about what you saw and believed, and it is worth more than a tidy log.

> **Nothing is changed during observation** (L-7). Not one line. Not the obvious thing. A change
> made mid-window invalidates every observation after it, and you will not know which ones.

**Required at:** **Lite** — the one artifact that cannot be reconstructed from memory afterward.

## Window

| | |
|---|---|
| **Declared window** | `<opened <UTC> — closes <UTC or condition>>` |
| **What is being observed** | `<the subject, stated narrowly enough that "covered" is checkable>` |
| **Instrument(s)** | `<what is doing the observing, including the human — and what each one cannot detect>` |
| **Known instrument error** | `<the error you already know about, published here so it can be subtracted rather than discovered>` |
| **Recorder** | `<who>` |

Declaring the window is what makes the intake boundary real. "I am observing X until Y" has an
exit condition; "I'm keeping an eye on things" does not, and it silently merges into triage.

## Entry grammar

Every entry carries these fields. None is optional, and the two that get dropped under time
pressure — `Conditions` and `Source` — are the two that make an entry re-checkable a year later.

| Field | What it holds | Why |
|---|---|---|
| `O-<n>` | permanent ID | an address that never changes. Retire, never reuse. A split entry keeps its ID and gains a suffix (`O-14a`, `O-14b`) |
| `<UTC>` | **live** timestamp, read at the moment of writing | ordering, and lag analysis. Never an ambient date |
| `Conditions` | the **seeing** — instrument, state, and everything else that was going on | an observation without its conditions cannot be compared to another one later, and comparison is the entire point of keeping a series |
| `Observed` | what happened, in the words it happened in | verbatim first. The moment you paraphrase, you have recorded your summary of the event, and you cannot get the event back |
| `Initial read` | your explanation, labelled `UNVERIFIED`, in its own field | L-3. Written in the same sentence as the observation, in the same voice, the two become indistinguishable in a month — and you will act on the second while believing you recorded the first |
| `Confidence` | a token from the charter's vocabulary | grades **the observation**, not the explanation. See below |
| `Source` | where this came from, precisely enough to return to it | the only defense against a record that gradually accumulates its own conclusions as inputs |

**The confidence token grades the observation, not the read.** `CONFIRMED` here means *I saw this
reliably* — not *my explanation is right*. A directly sensed, well-localised observation earns it
even when nobody has any idea what causes it. A second-hand report is `UNVERIFIED`. Something you
tried to pin down and could not is `UNRESOLVED`, which is a real result and not a failure to try
harder.

Those sentences say how the vocabulary **applies to an observation**; they are not definitions of
it. **The six tokens are defined once, in
`doctrine/02-epistemics.md`, section *Confidence tokens*, and are not
redefined here** (L-14, AMENDS D-015). This file previously defined three of them locally, which
is exactly the second-home mechanism that let the vocabulary ship with three different memberships
in the seeded corpus.

**The `Initial read` is `UNVERIFIED` at intake, always, without exception.** It is promoted —
or refuted — during RESOLVE, and the promotion is recorded on the triage board and in findings.
**It is never promoted by editing this file.**

**Write the entry now, not at the end of the session.** A pass written up afterward is a pass
filtered through what you concluded during it, and the filtering is invisible because you did it.

**Record it even if it seems minor, and even if you cannot reproduce it.** Mark it and move on.
One source project deliberately kept a retracted finding on the books with its original
timestamp, reasoning that if the symptom ever resurfaced it would already have a first sighting —
the deleted version of that record would have cost a second discovery.

---

## Entries

<!--
  Append only. Newest at the bottom. Never reorder, never edit.
  Entry shape:

  ### O-<n> — <short label> — `[<YYYY-MM-DDTHH:MMZ>]`
  **Conditions (seeing):** <instrument, state, context, everything else in play>
  **Observed:** "<verbatim>"
  **Initial read (`UNVERIFIED`):** <your explanation — and it stays UNVERIFIED here forever>
  **Confidence:** `<token>` — <what makes it that token>
  **Source:** <where this can be returned to and re-checked>
-->

### O-`<n>` — `<short label>` — `[<YYYY-MM-DDTHH:MMZ>]`

**Conditions (seeing):** `<…>`
**Observed:** "`<verbatim>`"
**Initial read (`UNVERIFIED`):** `<…>`
**Confidence:** `<token>` — `<justification>`
**Source:** `<…>`

---

`INTAKE CLOSED` `[<YYYY-MM-DDTHH:MMZ>]` — `<n>` entries, `<O-1>`–`<O-n>`. `<One line: what the
window covered, and — more usefully — what it did not.>`

> **The `INTAKE CLOSED` marker is a literal line in the file, not an understanding.** The source
> project that ran the largest observation pass wrote one, and the reason is mechanical: without
> an explicit marker, intake and triage overlap at the edges, the boundary stops existing, and
> nobody notices — because the first item triaged during intake looks exactly like an item
> triaged after it. Everything appended below this line is a **new window** with its own header,
> or it does not belong in this file.

---

## Worked examples

*Three entries from an observation window on a house with recurring damp. Domain is illustrative
only — the shape is the point.*

### O-3 — musty odour, back bedroom — `[2026-03-02T08:15Z]`

**Conditions (seeing):** First entry into the room that day; door and windows shut for
approximately nine hours overnight. Exterior 4°C, interior 18°C. 31 hours since rainfall ended
(34mm over the preceding two days, per the garden gauge). No instrument — this is nose only,
recorded on entering from the hallway. Noted for comparability: a second entry ten minutes later
did not register the odour at all, which is expected of olfactory adaptation and is why this
entry is stamped at *first* entry and why every later smell observation must be too.

**Observed:** "Musty — wet cardboard. Strongest at the back-left corner at floor level, gone by
about knee height. Not detectable standing in the doorway."

**Initial read (`UNVERIFIED`):** The back-left corner is directly below the gutter run on the
rear elevation. Possible water ingress through the external wall at that corner.

**Confidence:** `CONFIRMED` — directly sensed by the recorder, localised on two separate
mornings under matched conditions. The *observation* is solid; the *explanation* above has not
been checked against anything and is not entitled to any of this confidence.

**Source:** Direct sensory observation, `<recorder>`. Rainfall figure from the garden gauge,
read 2026-03-01T09:00Z, logged in `<rainfall sheet>`.

### O-4 — elevated moisture reading, wall behind washing machine — `[2026-03-02T09:40Z]`

**Conditions (seeing):** Utility room, machine pulled 60cm clear of the wall, which had not been
done in roughly two years. Meter `<model>`, pin mode, calibrated `<date>` against the supplied
check block. Wall is painted plaster over what is believed to be solid brick. **Known instrument
error, stated so it can be subtracted rather than discovered:** this meter's surface mode reads
high on painted plaster and its pin mode reads high in the presence of salts, which are exactly
what a long-standing damp patch deposits — so a high reading here is consistent with *current*
damp and with *historical* damp that has since dried, and this instrument cannot distinguish the
two. Same-day exterior conditions as O-3.

**Observed:** "Pin mode, 300mm above floor, centre of the patch: 24.1, 23.8, 24.4 across three
placements. Same height, 1.5m to the left, off the patch: 9.2. Discolouration is a rough oval
about 40cm across, edges tide-marked, dry to the touch."

**Initial read (`UNVERIFIED`):** Rising damp, or a slow leak from the machine's supply
connection. The tide-marked edge is characteristic of both, which is why this read cannot be
resolved from the reading alone.

**Confidence:** `CONFIRMED` — measured directly, three placements, with an off-patch control
reading taken at the same height for contrast. The control reading is what makes the number mean
anything; a lone 24.1 with nothing to compare it to would be `UNVERIFIED` at best.

**Source:** Meter reading, logged at the wall. Photograph `<ref>` taken before the machine was
pushed back, since the patch will not be visible again without moving it.

### O-9 — single loud pipe knock, not reproduced — `[2026-03-06T22:51Z]`

**Conditions (seeing):** Heating had been off approximately four hours; house quiet; heard from
the landing. No instrument.

**Observed:** "One sharp knock, somewhere in the run above the hall ceiling. Once. Waited twenty
minutes, nothing further."

**Initial read (`UNVERIFIED`):** Thermal contraction in the pipe run. Possibly unrelated to
anything else in this window.

**Confidence:** `UNRESOLVED` — heard clearly, but not localised and not reproduced across the
remaining nine days of the window despite two deliberate attempts to trigger it by cycling the
heating.

**Source:** Direct observation, `<recorder>`. Recorded despite being unreproducible, per the
standing rule above — if this recurs in a later window, it now has a first sighting with a date
on it, and the second occurrence will be the second data point instead of the first.

---

`INTAKE CLOSED` `[2026-03-15T19:30Z]` — 11 entries, O-1–O-11. Window covered the rear elevation,
the back bedroom, the utility room and the hall ceiling run. It did **not** cover the roof void,
which was never entered, or the front elevation, which was excluded when the window was declared
and remains unobserved — that is a gap in coverage, not an absence of findings.
