---
name: astronomer-observe
description: Run a read-only observation window — use when the operator reports something that happened, opens an intake pass, or asks to record, log, or sweep a surface before anything is diagnosed or fixed.
---

# Observation window

Purpose: get everything that actually happened onto the record, verbatim, before anyone explains
it. You are a recorder in this phase, not a diagnostician.

## Open the window

1. Take a live UTC timestamp by shell call — `date -u +"%Y-%m-%dT%H:%MZ"`, or
   `(Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mmZ")`. Never an ambient or remembered
   date.
2. Write the window header to the observation log: the live stamp, the declared scope ("the
   whole surface today", "the next two weeks"), and what would close it.
3. State the **conditions of observation** for the window: what instrument, what state, what
   else is going on. An observation without conditions cannot be compared to a later one.
4. Say plainly, in the session: nothing will be changed until this window closes.

## Record each item

One entry per item. Append it to the log **the moment it is captured** — never batch entries to
the end of the pass. A pass written up afterward is filtered through what you concluded during
it.

Each entry carries:

- `O-<n>` — a permanent ID. Never renumber, never reuse. A split becomes `O-14a` / `O-14b`.
- **Verbatim first.** The operator's own words, or the raw reading, quoted. Do not tidy grammar,
  do not summarize, do not translate into terminology.
- **Live timestamp** of the observation, and of the recording if they differ.
- **Conditions** — anything that limits or colors this specific reading.
- **Your reading**, if you have one — in its own separate field, labelled `UNVERIFIED`, never
  blended into the description.
- **Scope**, if the item is stated as a general claim. Unscoped is `ASSERTED-UNIVERSAL` and gets
  flagged, not accepted.

Where an item is stated as a conclusion ("X caused Y"), split it: record the observation as the
entry and the conclusion as a separate `UNVERIFIED` inference naming what it rests on.

## Forbidden inside the window

- **Any change to the subject.** Not one line. Not the obvious thing. A change made mid-window
  invalidates every observation after it and you will not know which ones.
- **Grouping items by apparent cause.** That is triage's job; doing it here contaminates the raw
  record with a conclusion you cannot later separate out.
- **Dropping an item** because it seems minor, or you cannot reproduce it, or it is probably
  nothing. Record it and mark it. A recurrence is worth much more when a first sighting already
  exists on the books.
- **Filling a gap.** If the operator did not report it, it did not happen. Do not infer the
  missing entry.

If you notice something you want to fix, record it as an observation and keep looking. Say out
loud that you are deferring it.

## Ask, do not assume

When an entry is missing its conditions, its timing, or its scope, ask the operator for that one
field. Do not reconstruct it. Where a required detail needs a physical fact, a preference, or
anything only they can supply, mark the entry incomplete and move on — a blocked field is honest,
an inferred one is fiction.

## Close the window

1. Take a fresh live timestamp.
2. Write `INTAKE CLOSED` as an explicit marker in the log, with that stamp and the item count.
   Without the marker, intake and triage overlap and the boundary silently stops existing.
3. Report: the count, the ID range, which entries are incomplete and what they are waiting on,
   and anything you deferred rather than fixed.
4. Do not begin triage in the same breath. Triage is the next phase and it needs the boundary.
