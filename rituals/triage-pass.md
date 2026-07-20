# Triage pass

> **Doc status:** living.

## When

An observation log is closed — the `INTAKE CLOSED` marker is written — and you are holding a pile
of raw entries with no shape. Route here before anything gets fixed, prioritized, or promised.

If the log is not closed, you are in [observation-pass](observation-pass.md), not here.

## Do

1. **Bucket every entry by epistemic state, not by severity.** Severity tells you what you want
   to be true; epistemic state tells you what the item actually needs next
   ([`doctrine/03-the-loop.md`](../doctrine/03-the-loop.md)).

   | Bucket | State | Needs |
   |---|---|---|
   | **A** | Cause proven, with a citation | nothing — ready to act on |
   | **B** | Direction clear, cause not formally proven | mechanical execution |
   | **C** | Problem real, response contested | **a decision from the human** |
   | **D** | Not a problem — a want | prioritization |
   | **E** | Seen once / accepted / cannot reproduce | **nothing, deliberately** — parked with a reason |

2. **Record severity separately.** It still gets written down; it is just not the sort axis.
   Sorting by severity yields things you would like fixed. Sorting by epistemic state yields
   things that can move.
3. **Fill bucket E honestly.** It is the one people skip and the one that pays. Without a written
   home, the seen-once item and the accepted-tradeoff item re-enter the queue at every review
   forever, and get re-investigated by whoever forgot.
4. **Group into clusters** — items sharing **one** root cause, each with an ID (`C-<n>`) and its
   hypothesised cause marked `UNVERIFIED`.
5. **Separate co-occurrence explicitly and in writing** (L-5). Two problems on one surface are two
   problems until a mechanism is proven that explains both. State that mechanism per cluster — if
   you cannot state it, the cluster is a coincidence with a name.
6. **Keep the residue.** Items that resisted grouping stay ungrouped, noted as standing alone.
   The residue is information, not failure.
7. **Do not act on any cluster.** It is a hypothesis until RESOLVE proves it. Every cluster leaves
   this ritual `UNVERIFIED`, without exception.
8. **List the decisions owed to the human**, numbered, in one place, at the end. Everything in
   bucket C, plus any trade-off between goods rather than between right and wrong (L-15). A pass
   that does not end with that list has absorbed those decisions silently.

## Record

- `TRIAGE BOARD` (disposable) — every item with a bucket, an owner, and either a cluster ID or an
  explicit note that it stands alone. Items that move between buckets keep both addresses
  (`E4→B9`); nothing is renumbered.
- `OBSERVATIONS` — unchanged. Triage never edits the log it reads.
- `TRIAGE BOARD` — the questions owed to the human as `Q-<n>`, numbered in one place, each open
  until answered and each naming what it rests on and what it blocks.
- `DECISIONS` — the **answers**, once given, as new ledger entries. An answer never gets written
  back over the question.

Exit condition: every item bucketed, every cluster hypothesised and unverified, the human's list
handed over.
