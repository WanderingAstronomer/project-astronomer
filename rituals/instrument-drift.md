# Instrument drift

> **Doc status:** living.

## When

You discover that a number you have been relying on is stale, or was never measured by you.

Recognizable by: you cannot say who took the measurement or when; the figure came from a document
— including this framework's documents; you have repeated it often enough that it feels like
knowledge; or the subject has changed since the reading was taken.

**Every number in every document is stale from the moment it is typed** (L-11). That is a
statement about time, not about carelessness.

## Before any of that: take the baseline

Everything below is repair. It is written for the moment you *discover* a bad number, which is
always after you have already used it — step 1 is "stop using the number," and that presupposes it
is in use.

The cheap half of this ritual runs at the other end, before the work starts, and it now has its own
procedure: [capability-interrogation](capability-interrogation.md). Run that at setup and again
whenever the environment changes in a way you know about (K-4). What follows is the summary of why:

- **Measure what you are about to change, first.** A baseline you did not take is a baseline you
  are guessing at, and after the change there is no way back to it.
- **Declare what your instruments cannot detect**, in writing, where the next session will see it.
  For a human operator that is the observation log's `Known instrument error` field. For a
  collaborator doing the observing, it is the
  [capability inventory](../artifacts/capability-inventory.template.md) — and it is required from
  Lite upward whenever something other than the operator is doing the looking.
- **State the direction of a known bias, not just its existence.** "Roughly a 30% undercount on
  completeness questions" can be subtracted; "may be incomplete" cannot.

A limit declared in advance costs a paragraph. The same limit discovered mid-window costs the
window, because you cannot tell which observations it already touched.

## Do

1. **Stop using the number.** Not "flag it and continue" — anything you conclude from it in the
   meantime inherits the defect and will need re-checking too.
2. **Re-measure it yourself**, at the right altitude (L-12). The measurement must be capable of
   failing in the way that matters. Confirm you are measuring the same thing the old figure named,
   under conditions you can state.
3. **Record the delta explicitly.** Old figure, its source, its date if you can establish one; new
   figure, its conditions, its live timestamp; and the difference stated as a number. The house
   form is blunt and worth copying: **"measured by me — never quoted."**
4. **Find every decision that rested on it.** Search the ledger for the figure and for the
   reasoning that used it. Include decisions where the number was a threshold, a comparison point,
   or a justification for not doing something.
5. **Re-check each one against the new figure.** Three outcomes, all valid: the decision still
   holds for the same reason; it still holds for a different reason, which gets stated; or it does
   not hold and reopens.
6. **Check whether a gate was calibrated on the bad number.** If so, suspect the gate before the
   subject — a threshold lifted from the wrong condition makes everything fail a bar that was
   itself wrong. The ruling to reach for is *the gate was the artifact, not the subject*: demote it
   to a monitored metric and recalibrate on the condition you will actually measure under (L-9).
7. **Check what else came from the same source.** A source that supplied one stale figure supplied
   others. Treat the set as suspect until re-measured, rather than re-measuring only the one that
   broke.
8. **Give the number a home and a date** (L-14). One place, one owner, a visible timestamp. A
   figure with no expiry marker will be re-quoted, by you, within the year.

## Record

- `OBSERVATIONS` — the new measurement, with its conditions, as a normal entry.
- `SPECIFICATION` (living) — updated to the new figure, dated at the point of use.
- `FINDINGS` (frozen) — the delta, and where the stale number had spread. Frozen records that
  quoted it are **annotated, not corrected** (L-13): they are accurate evidence of what was
  believed.
- `DECISIONS` — one entry per decision reopened, naming the original entry, the corrected figure,
  and whether the decision survives. `caveat (owned):` name any decision you chose not to re-check
  and why.
