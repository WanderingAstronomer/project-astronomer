# Hypothesis refuted

> **Doc status:** living.

## When

A root cause you recorded turns out to be wrong. The evidence you went back for does not support
it, or supports something else, or the thing you fixed did not behave the way the cause predicted.

**This is a success path.** A refutation is a result, not a failure (L-6) — you learned it at the
cheapest moment you were going to. The tell that you should be here and are not: you are
explaining why the original cause is *still basically right*.

## Do

1. **Write the refutation down before anything else**, with a citation — where you looked, what
   you found, why it is incompatible. A refutation without an address is an opinion about a
   hypothesis.
2. **Keep the refuted version visible.** Do not delete, do not rewrite. Mark it `REFUTED` in the
   field position, retain its original timestamp, and leave it where a reader will meet it. An
   investigation that quietly drops its wrong calls cannot be trusted about its right ones.
3. **Establish the blast radius.** List everything that rested on the refuted cause:
   - clusters grouped under it — the grouping may now be co-occurrence (L-5)
   - changes already made because of it
   - decisions in the ledger whose reasoning cites it
   - anything downstream that was skipped or deprioritized *because* this cause explained it
4. **Reopen what the radius touched.** Each item returns to the bucket its evidence now supports —
   usually B or C, sometimes E. Reopening is mechanical; do not argue items out of it because
   redoing them is expensive.
5. **Check the changes already made.** A change built on a refuted cause is not automatically
   wrong — it may work for a reason nobody has stated. Per change: keep with a corrected
   rationale, or revert. Both are valid; silence is not.
6. **State what is true now** — `CONFIRMED` with a citation, or `UNRESOLVED` with what would
   settle it ([unresolved](unresolved.md)). Do not swap one `UNVERIFIED` story for a more
   comfortable one and stop there.
7. **Ask what made it plausible.** If the same shape of reasoning produced the last refutation
   too, that is a recurring defect needing a gate, not a third correction
   ([recurring-defect](recurring-defect.md), L-17).

## Record

- `FINDINGS` (frozen) — the original entry stays, annotated `REFUTED` with a dated addendum. Never
  edited into agreement with the present.
- `SPECIFICATION` (living) — rewritten to current truth, with no change-log of how it got there.
- `DECISIONS` — one entry naming the refuted cause, the blast radius, and which downstream items
  reopened. Where a decision's reasoning cited the refuted cause, append a new entry naming it;
  never edit the old one.
- A standing table of recorded-then-refuted causes, kept where it will be read. Its length is a
  sign the method is working, not an embarrassment.
