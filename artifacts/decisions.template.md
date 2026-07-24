# DECISIONS — `<project name>`

> **Doc class:** append-only — its own class, not a flavour of frozen (D-019). Entries are never
> edited. The file grows forever; nothing in it changes. Growth is not editing — say this out loud
> to whoever will one day want to tidy it up.

**Required at:** **Lite** — one of the three artifacts without which the framework is not itself.

The append-only decision ledger for this project. It is the cheapest artifact in the framework
and the highest-value one: roughly ninety seconds of writing per entry, and it is the difference
between a project that can be resumed and one that has to be re-derived.

## Conventions

- **Format:** `[<UTC>] D-<n>: **<decision>** — <why>`. Stamp with a **live** UTC reading, taken
  at the moment of writing. Never an ambient date, never one carried in from context, never
  "today" as you believe it to be. Injected dates drift, and a ledger ordered by drifting
  timestamps cannot be resolved — which removes the only thing that makes the ordering mean
  anything.
- **Recency alone does not win.** A later decision overrides an earlier one **only when it names
  the decision it supersedes.** Timestamps order the ledger; they do not resolve it. Two entries
  that disagree and neither of which names the other are two live rules, and you will follow
  whichever you remember.
- **Namespacing.** A bare `D-<n>` resolves to **this ledger only**. References to another
  project's ledger are prefixed (`<PRJ>-D-<n>`). Ambiguous bare references are a supersession
  hazard: the moment a second ledger reaches the same number, every historical reference still
  resolves — to the wrong thing, which is worse than not resolving at all.
- **`blocks-on:`** — a decision resting on evidence that has not been established carries this
  tag and stays `OPEN` until the evidence exists. A decision that quietly depends on an unproven
  claim is indistinguishable, later, from one that was actually established.
- **`caveat (owned):`** — state the weakness yourself, in the entry, in your own words. Name the
  control you did not run, the comparison you skipped, the thing you chose not to check. An owned
  caveat is a durable asset; an unstated one is a landmine with your fingerprints on it.
- **`next:`** — a decision deliberately deferred, with the condition that should reopen it.
- **Mark who decided.** Decisions made by the operator rather than by a collaborator are marked
  **[operator]**. The boundary between "the human chose this" and "this was chosen on the human's
  behalf" is recorded, not assumed — because six months later it is unrecoverable, and it is
  exactly the distinction you will need.
- **Never edit a past entry.** Amend with a new timestamped `AMENDS D-<n>:` line. An amendment
  states what changed and confirms what still stands.
- **IDs are permanent addresses.** Never renumber. Retire, never reuse. A decision that splits
  keeps its ID and gains a suffix (`D-<n>a`, `D-<n>b`) rather than being renumbered — a renumber
  breaks every reference that still resolves, to the wrong entry.

---

## Ledger

<!--
  Newest at the bottom. Copy an entry shape below and fill it. Do not reorder.
  Entry shape:

  `[<YYYY-MM-DDTHH:MMZ>] D-<n>:` **<The decision, stated as a ruling in one sentence.>** <Why —
  the reasoning, the alternative rejected, and what it cost or would have cost. This is the part
  a future reader needs and the part that gets skipped.>
  `supersedes D-<n>:` <what changed and why the earlier ruling no longer holds>
  `blocks-on:` <the evidence this rests on that does not yet exist>
  `caveat (owned):` <the weakness you are choosing to accept, named by you>
  `next:` <the condition that should reopen this>
-->

`[<YYYY-MM-DDTHH:MMZ>] D-<n>:` **`<decision>`** — `<why>`

---

### Worked examples

*Two real-shaped entries from a small volunteer stream-monitoring study, included so the
conventions are visible in use rather than described. Domain is illustrative only.*

`[2026-04-11T07:22Z] D-007:` **Turbidity is sampled at a fixed clock hour, not at a fixed
interval after rainfall.** Interval-after-rain sampling was the obvious design and is the wrong
one here: storm duration varies by a factor of five across events, so "four hours after rain
stopped" describes a different physical condition every time and the resulting series cannot be
compared against itself. A fixed hour produces a comparable series and pushes rainfall down into
the conditions field of each observation, where it is recorded rather than baked in. The cost is
real and accepted — a fixed hour will miss the peak of a fast-clearing event.
`blocks-on:` no paired samples yet exist showing the fixed-hour series still detects a
post-storm rise at all. Until one storm has been sampled both ways, this trades sensitivity for
comparability on reasoning alone, and the trade could be bad. Stays `OPEN`.

`[2026-05-30T18:04Z] D-008:` **[operator]** **The upstream control site is dropped; the study
reports as single-site from this date forward.** `supersedes D-005:` the two-site paired design
is no longer available — access to the upstream site was withdrawn by the landowner on
2026-05-28. A substitute 400m further upstream was considered and rejected: it sits above a
tributary confluence and on a different substrate, so it would have functioned as a *different
site wearing the control's name*, and every later reader would have compared the two series
believing they were paired. Reporting the design change is worse-looking and correct.
`caveat (owned):` the study can no longer separate catchment-wide change from site-specific
change. That is a permanent limitation on every finding drawn from data after 2026-05-28, not a
temporary gap, and it was chosen knowingly over pausing the study for a season to find a real
paired site. Findings after this date must carry it at the point of use, not once in a preamble.

`[2026-06-14T06:58Z] AMENDS D-007:` fixed hour moved from 07:00 to 08:00 local. The first month
showed the 07:00 slot colliding with the weekday road-sweep discharge upstream of the sampling
point — a recurring contaminant that was entering the *series* instead of being recorded in the
*conditions*, which is precisely the failure the fixed-hour design was chosen to prevent. The
original ruling stands unchanged; only the hour moves. Samples 2026-04-11 through 2026-06-13 are
flagged in the observation log rather than discarded — they are still evidence, of a series with
a known weekday artifact.
