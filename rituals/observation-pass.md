# Observation pass

> **Doc status:** living.

## When

You are about to look at something properly — a surface, a period, a subject — and you want the
result to be usable later. Route here whenever you catch yourself about to explain what you are
seeing while you are still seeing it, or about to fix one small obvious thing before continuing.

The tell that you are already outside this ritual: you have made a change and you are still
recording.

## Do

1. **Declare the window.** What you are observing, over what period, and what event closes it.
   Write it at the head of the log before the first entry. An undeclared window has no exit
   condition, so it never closes — it just stops being written in.
2. **Record verbatim first.** What happened, in the words it happened in. Interpretation is a
   separate field, written second, and only after the description stands on its own.
3. **Stamp conditions with every entry** — the astronomer's *seeing*. What instrument, what
   state, what else was going on. An observation without its conditions cannot be compared with
   another one later, which is the whole reason you are keeping a log.
4. **Type every entry** (L-3). Observation or inference — a field, never a tone. An initial
   explanation is recorded, labelled `UNVERIFIED`, in its own field, never blended into the
   description.
5. **Scope every non-trivial claim** (L-4). Under what conditions does it hold? Unscoped is a
   defect state, not a strong claim — mark it `ASSERTED-UNIVERSAL` and route it to scrutiny.
6. **Change nothing.** Not one line. Not the obvious thing. Not the ten-second thing (L-7,
   D-014). A change made mid-pass invalidates every observation after it, and you will not know
   which ones.
7. **Do not group** by apparent cause. Grouping is a conclusion, it belongs to TRIAGE, and done
   here it contaminates the raw record with an inference you can no longer separate out.
8. **Record the minor and the irreproducible anyway.** "Seen once, cannot reproduce" is an entry
   with a marker, not an omission. If it resurfaces in a year it already has a first sighting.
9. **Write the log every entry, not at the end.** A pass written up afterward is a pass filtered
   through what you concluded during it.
10. **Close it explicitly.** A literal `INTAKE CLOSED` marker with a live UTC stamp. Without one,
    observation and triage overlap and the boundary silently stops existing.

## Choosing the instrument: detection is not the same question as completeness

Before the window opens, decide which of two questions you are asking, because they want different
instruments and mixing them up produces a confident undercount.

- **"Does this happen at all?"** — a detection question. Reading, judgement, and an attentive
  collaborator are good at it. They notice the thing nobody thought to search for.
- **"Where does this happen, everywhere?"** — a completeness question. Reading is *bad* at it, and
  the failure is quiet: you get a list that looks finished.

**The scar, measured here, once.** A four-reader pass over this corpus, told exactly which defect
class to look for, reported **seven** sites. A mechanical search during the repair found **three
more, in files those readers had read** — roughly a 30% undercount, in the direction that feels
complete. Two of the three missed sites were the most load-bearing ones in the set.

The working rule that follows: **for a completeness question, the mechanical search is the
instrument and the reader is the interpreter — not the reverse.** Search first, exhaustively, then
have someone read the hits to decide which are real. Using a reader as the instrument and a search
as the spot-check inverts their strengths.

Record which one you used in the window's `Instrument(s)` field, and record the undercount if you
ever measure it. That figure is stale the moment it is written (L-11) — it is *this* pass, on *this*
corpus, and it should be re-measured rather than quoted.

## Record

- `OBSERVATIONS` — one entry per item, `O-<n>`, append-only and frozen once written. IDs are
  permanent: an item that later splits becomes `O-14a` / `O-14b` and is never renumbered.
- `DECISIONS` — only if the window itself was changed: extended, cut short, or re-scoped. Say why.
- The `INTAKE CLOSED` marker, in the log, at the end.

Anything you were tempted to fix during the pass leaves this ritual as an observation with an
`UNVERIFIED` hypothesis attached — never as a change.
