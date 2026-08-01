---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - scope-surprise-procedure
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Scope surprise

> **Doc status:** living.

## When

The work you are doing has turned out to be much bigger than the change-size class you declared
for it. You said `minimal` and you are four layers deep; you said `medium` and it now touches
things nobody planned for.

Recognizable by: you are about to change something you did not name when you started; the reason
you have not stopped is that stopping now feels wasteful; you are telling yourself you are
*already in there*; the scope grew by discovery and the plan has not been told.

**Bigger scope is an explicit re-plan, not an in-session expansion.**

## Do

1. **Stop at the current boundary.** Do not finish the bigger version first and re-class
   afterwards — that is the same failure with a report attached.
2. **State the new class out loud**: `minimal` · `medium` · `large`. Re-classing upward is fine
   and expected. Silently exceeding the class is not
   ([`doctrine/03-the-loop.md`](../doctrine/03-the-loop.md), ACT).
3. **Say why it grew.** One sentence, causal: what you found, and why it makes the declared scope
   insufficient. "It was bigger than I thought" is not a reason; it is a restatement.
4. **Decide who owns the re-plan.** A re-class from `minimal` to `large` usually crosses back to
   whoever owns sequencing. If that person is unavailable, take the conservative option and record
   why — and only if the call is cheap to reverse
   ([`doctrine/06-delegation.md`](../doctrine/06-delegation.md)).
5. **Split rather than swell.** Keep the original declared change and land it alone. The
   discovered work becomes its own item with its own class, its own acceptance criterion, and its
   own place in the queue.
6. **Do not bundle.** Landing the discovered work alongside the original makes both results
   unattributable, however cleanly they coexist (L-10). This is how L-10 gets violated by people
   who agree with L-10.
7. **If the discovery is outside your fence, do not touch it at all.** Record it with a citation
   and keep going — two independently correct changes can combine into a wrong result that
   nothing flags.
8. **Re-check the acceptance criterion.** One pre-registered for the small version usually cannot
   detect whether the large version worked (L-9, L-12). Rewrite it before resuming, not after.

## Record

- `DECISIONS` — one entry: original class, new class, the causal reason, who owns the re-plan,
  and whether the work was split or expanded. Live UTC stamp.
- `TRIAGE BOARD` — the discovered work as its own item, bucketed by what you actually know about
  it. Usually B or C. It does not inherit the original item's bucket.
- The work report — under *found outside your fence* if it was, and under *judgement calls made*
  if you re-classed without the owner.

Exit condition: the declared scope and the executed scope are the same sentence again.
