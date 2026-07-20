# Settling a document

> **Doc status:** living.

## When

A living document has drifted from reality. It describes things that were never built, omits
things that exist, or carries a claim nobody has checked since it was written.

Recognizable by: you have started warning people which parts of it to trust; or you reached for it
to answer a question and went to the source instead.

**Only living documents are settled.** A frozen record that turns out to be wrong is annotated,
never rewritten (L-13) — that is [hypothesis-refuted](hypothesis-refuted.md), not this.

## Do

1. **Fix the ruling set first — before touching any document.** A small, fixed, numbered list of
   calls applied everywhere: what this corpus states, what it omits, which token goes where, how
   unbuilt things are marked. Ruling per-file instead produces a corpus consistent nowhere.
2. **Settle one file interactively, as the exemplar.** Work it through with whoever owns the
   rulings, arguing the edge cases in the open. Rulings discovered here join the set; the exemplar
   is what the rest are measured against.
3. **Settle the rest against those rulings** — mechanically, without renegotiating. If a file
   cannot be settled without a new ruling, stop, add it to the set, and note which already-settled
   files it invalidates.
4. **Strip to current reality, not history.** A living document states what *is*. Dated update
   notes and change-logs come out; the ledger holds history
   ([`doctrine/05-the-record.md`](../doctrine/05-the-record.md)).
5. **Verify adversarially, with a fix loop.** Take each surviving claim back to the actual source,
   re-derive it, and try to break it. **Default toward refuted when you cannot independently
   confirm it.** Re-derive, do not re-read — if the only input is the claim, you are checking prose
   quality ([`doctrine/04-verification.md`](../doctrine/04-verification.md)). Fix what fails and
   re-verify; one pass is not a loop.
6. **Honesty cuts both ways.** Remove overstatements *and* state understated things plainly. A
   settlement that only deletes is a retreat, and it leaves real capability undocumented and
   therefore unused.
7. **Mark, do not delete, what is not yet built** — at the top of the document describing it. A
   thing that is absent and says so is safe; a thing that is absent and reads as present is the
   highest-severity defect class (L-16).
8. **Sweep for cross-file consistency last.** One term, one meaning, one home (L-14). Pointers
   still resolve, tokens match the vocabulary, no two files answer the same question differently.

## Record

- The settled documents themselves (living) — rewritten, no change-log inside them.
- `DECISIONS` — the ruling set, entered as decisions with live UTC stamps. These outlive the pass
  and are cited by the next one.
- A frozen settlement record — what drifted, what the drift was caused by, what was verified and
  at what altitude, and what remains unverified. `caveat (owned):` name the claims you settled by
  reasoning rather than by returning to the source.
