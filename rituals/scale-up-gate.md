# Scale-up gate

> **Doc status:** living.

## When

A small version of the work has finished and you are deciding whether to commit to the large
one. The pilot week is over, the sample has been processed, the first cohort is done — and the
next step costs materially more than the last one.

Route here **before** the expensive commitment, not after it (L-8). The tell that you skipped
this ritual: you are partway through a long run, something looks wrong, and you cannot tell
whether it was wrong from the start.

The gate exists because the failure it prevents is not a wasted run. It is a **completed run
whose output looks fine and is wrong** — and which you will believe, because it completed.

## Do

1. **Check the sample was checkable.** The point of a small run is that you can verify it by
   hand. If you could not actually inspect the output — too much, too fast, no ground truth —
   then the pilot proved the pipeline ran, not that it worked. Say which of the two you have.
2. **Evaluate against the pre-registered criterion**, not against your impression of how it
   went (L-9). If no criterion was registered before the pilot, you cannot pass this gate on
   this data — register one now and re-run, or record that you are proceeding without one and
   why.
3. **Check the falsifier fired at all.** Confirm the degeneracy guard, the null-bucket rate, or
   whatever you wrote as "this would mean the whole approach is fake" actually produced a reading
   (L-9, and [`doctrine/04-verification.md`](../doctrine/04-verification.md) — break it and
   confirm the check notices). A guard that has never returned a number is not a guard.
4. **Interrogate the gate itself, not just the result.** The sharpest recorded failure in the
   corpus is a pre-registered threshold that was *lifted from the wrong condition* — every
   subject failed a gate that was itself wrong. Ask: was this number calibrated on the condition
   I am actually measuring under? A gate that nothing can pass is a gate artifact.
5. **Fix the method, not the sample** (L-8). If the pilot failed, the output is not the
   deliverable — the diagnosis is. Name what specifically failed and what changes before the
   next attempt.
6. **Verdict: GO / NO-GO / GO-WITH-CONDITIONS.** Write it as one of those three words. "Looks
   promising" is not a verdict and will be read as GO by everyone including you.
7. **Bank the free fixes.** Whatever the pilot taught you about the method goes into the method
   *now*, before the large run, where it is cheap. Every rule learned this way carries the
   failure it fixes (D-003).
8. **Size the instrumentation to the run.** If the large version runs longer than you will
   watch, it needs a heartbeat and an out-of-band readout before it starts, not after it worries
   you ([`doctrine/04-verification.md`](../doctrine/04-verification.md)).

## Record

- `FINDINGS` — the verdict, frozen, with the numbers it rested on and the `Method:` line saying
  how the pilot was evaluated. A NO-GO is a finding, not a gap.
- `DECISIONS` — the GO/NO-GO as a ledger entry with its reason. If the gate itself was
  re-calibrated, that is its own entry naming what it supersedes (L-2), and it says so plainly:
  moving a threshold after seeing the data is legitimate only when the *reason* is a defect in
  the threshold, and the ledger is where that claim gets stated and dated.
- Frozen record — the pilot's raw numbers, so the large run has something to be compared against
  later.

A NO-GO here is the cheapest good outcome available to the project. It is not a delay; it is the
ritual working.
