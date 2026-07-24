---
name: astronomer-verify
description: Adversarially verify a claim, finding, cluster, or result — use before anything is promoted to CONFIRMED, before acting on a hypothesis, and whenever the operator asks whether something is actually true or wants work checked.
---

# Verification

Purpose: **destroy** the claim. This is not "checking the work." A verifier whose success
condition is confirmation is doing confirmation with extra steps.

Your success condition is finding the break.

## Step 0 — state the target

Quote the claim in one sentence, exactly as asserted, with its current token and its stated
scope. If it has no scope, that is the first defect: an unscoped claim is `ASSERTED-UNIVERSAL`
and cannot be verified as written. Get the scope first. If the claim is compound, split it —
compound claims verify to "partly."

## Step 1 — default toward refuted

Adopt the posture explicitly: **you will report `REFUTED` unless you can independently establish
the claim.** The asymmetry is deliberate. Whoever built the hypothesis is already biased toward
it; a neutral verifier does not correct that bias, they only fail to add to it.

## Step 2 — re-derive, do not re-read

Go to the **actual source** — not the record of the source, not the summary, not last month's
note. Reproduce the reasoning from scratch and see whether you land in the same place.

Re-reading the finding and agreeing that it sounds right is checking prose quality. If your only
input is the claim itself, you have verified nothing.

Where you can, work **blind**: derive your own answer before reading theirs, then compare. Where
blinding is impractical, at minimum make the comparison mechanical — a scoring step that is itself
a judgement call cannot referee a dispute about judgement.

## Step 3 — attack it

- **Contradiction surface** — what observation would directly contradict this? Go look for that.
- **Dependencies** — what must be true for it to hold? Test the weakest one.
- **Multi-context** — where is it false or partial?
- **Temporal validity** — is it time-invariant, or has it expired?
- **Alternative cause** — what else would produce exactly this evidence?

A claim whose contradiction surface you cannot state is not verifiable; report that, and say so
as the finding.

## Step 4 — break it and confirm the check fires

For **every check you intend to rely on**, arrange the condition it is supposed to catch and
confirm it actually fires. An unexercised alarm is a hypothesis about an alarm. The canonical
failure was not careless: a check passed while the exact forbidden condition was present, because
both readings landed inside the same interval — correct check, correct reasoning, blind to the
thing it existed to see.

## Step 5 — verify at the right altitude

Before trusting any measurement, answer three questions in writing:

1. What exactly would have to go wrong for this to report a failure?
2. Is that the thing being claimed?
3. If not — what is, and can it be measured here at all? If not, say so and record the debt.

Then **name the grade achieved**, never collapsing them into "verified": **Direct** — proven in the
real environment, under the conditions that actually apply · **Proxy** — checked through a
stand-in; say what the stand-in cannot detect · **Derived** — reasoned from the source, nothing
exercised.

Take any number yourself. Never quote one — including numbers from this project's own documents.
Report measurements as "measured by me," with the baseline.

## Step 6 — verdict

Emit exactly one token, plus the evidence address: `CONFIRMED` (cite where) · `REFUTED` (state the
break) · `PROVISIONAL` (name what reopens it) · `UNRESOLVED` (state what would settle it)

**These four are the subset a verifier may emit — not the whole vocabulary.** The six confidence
tokens are defined in doctrine `02-epistemics.md`. `UNVERIFIED` is the state a claim arrives in, so
a verifier never emits it; `ACCEPTED` records a deliberate choice to keep a known imperfection,
which is the operator's call and not a verification result.

`UNRESOLVED` is a legitimate result — the instrument reached its limit and the report says so.
Rounding it to `CONFIRMED` is how a guess enters the record as a finding.

Close with **what you did not verify**, and the grade achieved for each thing you did. "Owed to
the operator" is an expected outcome, not a gap in the work.
