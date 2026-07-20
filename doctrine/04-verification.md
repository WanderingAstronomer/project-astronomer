# 04 — Verification

Verification is not "checking your work." It is the deliberate attempt to **destroy** a claim,
undertaken by someone whose success condition is destroying it. Anything less is confirmation
with extra steps.

---

## Default toward refuted

The verifier's instruction, taken almost verbatim from VOC's audit workflow:

> Verify it from scratch against the actual source — read the cited evidence, reproduce the
> reasoning, and try to **refute** it. **Default toward "refuted" if you cannot independently
> confirm it.**

The asymmetry is deliberate. An unaided investigator's bias already points at confirmation:
they built the hypothesis, it explains what they saw, and it is theirs. A verifier who is
neutral does not correct that bias — they only fail to add to it. The verifier has to be
pointed the other way to get an honest resultant.

**Re-derive, do not re-read.** Verification means reproducing the reasoning from the source, not
re-reading the finding and agreeing that it sounds right. If the verifier's only input is the
claim, they are checking prose quality.

---

## Verify independently, and blind where you can

DD ran its extraction and its gold-standard adjudication **in parallel, neither seeing the
other**, then aligned them by semantic equivalence and computed the agreement metrics
*deterministically in code, not by a model*. The design has three separable properties, all
portable:

1. **Blind** — the verifier does not see the answer being verified.
2. **Parallel** — neither run can anchor on the other.
3. **Adjudicated mechanically** — the comparison itself is not a judgement call, because a
   judgement call at the scoring layer reintroduces exactly the bias the design removed.

Where full blinding is impractical, keep the third property at minimum. A scoring step that is
itself a matter of opinion cannot referee a dispute about opinion.

**Diversity beats redundancy.** When a claim can fail in more than one way, give each verifier a
different lens — does the mechanism hold, does the measurement support it, does it reproduce —
rather than asking three verifiers the same question. Three identical checks find one class of
error three times.

---

## Cost-gate the expensive pass

Not everything earns full adversarial treatment. Both projects that formalized this gated on
epistemic type (see [`02-epistemics.md`](02-epistemics.md)): measured outcomes and
consensus-backed rules got the skeptic; pure opinion never became eligible for promotion at all.

Set the gate once, in advance, in the ledger. A gate decided per item at the moment of decision
is a gate decided by how much you want the item to be true.

---

## Break it and confirm the check notices

Generalized from VOC's mutation-testing rule, which is stated there as:

> For each meaningful test you add: **break the code it covers and confirm the test fails.** If
> it still passes, the test is decorative.

With the finding attached: **every session in that project's largest concurrent run found a real
defect inside its own work this way, without exception.**

The generalized form: **for every check you intend to rely on, arrange the condition it is
supposed to catch and confirm it actually fires.**

The canonical failure is worth carrying, because it is not a careless one. A check for
non-determinism *passed* while the exact forbidden non-determinism was present — both
measurements happened to land inside the same millisecond, so the values matched. The check was
correct, the reasoning was correct, and it was blind to the thing it existed to see. The fix was
to control the clock and forbid reading it directly.

Off-software: before trusting that a tracker will catch a missed day, miss a day on purpose and
confirm it shows up. Before trusting a symptom log to surface a pattern, plant a known pattern
and see whether your review would find it. **An unexercised alarm is a hypothesis about an
alarm.**

---

## Verify at the right altitude

The measurement must be able to fail in the way that matters (L-12).

The failure mode is a proxy that cannot detect the claimed effect and therefore always returns
"fine." VOC's instance: a text-level check standing in for a visual one, in an environment with
no layout engine at all — it could not have failed. OD's instance was handled better: it
published what its own tooling could not measure, and kept a running ledger of what was **owed
to real devices**, so weak verification never silently passed as strong.

Three questions before trusting a check:

1. What exactly would have to go wrong for this to report a failure?
2. Is that the thing I am claiming?
3. If not — what is, and can I measure it here at all? If not, say so, and record the debt.

**Distinguish the grades of verification in the write-up.** VOC requires reports to separate
"proven in the real environment" from "checked in a proxy" from "reasoned from the source," and
notes that its operator reads that distinction closely. Collapsing the three into "verified" is
the most common way a report overstates itself while every individual sentence stays true.

---

## Measure your own baseline

Before changing anything, take the measurement yourself and write it down (L-11). Numbers
quoted in documents are stale from the moment they are typed, including the ones in this
framework.

The house form, from a returned session report: **"Gates, measured by me — never quoted,"**
followed by a baseline-versus-final table.

This matters most where the subject changes while you read it. A software test count drifts when
someone else commits. A physiological baseline drifts because you are alive.

---

## Instrument anything that runs longer than you will watch

FR's pattern, for work that runs for hours or months unattended. Three parts:

**A heartbeat carrying running tallies**, not just position — `[142/5469] inserted=139 failed=3`.
Position alone tells you it is moving; tallies tell you it is moving *correctly*. The stated
reason is plain: without it "the operator is staring at a frozen screen with no signal."

**A separate read-only dashboard**, run out of band, answering four questions in a fixed order:

1. *Am I done?* — count, failures, remaining, percent
2. *Is the output degenerate?* — the distribution across categories, **checked against the
   pre-registered acceptance criterion** (L-9)
3. *Is it plausible?* — the top values by frequency
4. *Does it actually look right?* — the few most recent raw records, unaggregated

Item 4 is the one that catches confident wrongness, which no aggregate will show you. Item 2 is
a live readout on your own falsifier, which is the point of having written one.

**Checkpoint at the unit of expensive work.** FR committed after every single item, with the
reasoning that inference dominated the wall-clock so the overhead was noise — and in exchange, a
kill at any moment lost zero completed work. The general rule: when a unit of work is expensive
to redo, make it durable the moment it completes, and never batch durability for efficiency you
did not measure.

---

## Preflight: check what this step needs, and name the remedy

FR checked dependencies **scoped to the phase about to run**, not globally, and every failure
message named the fix rather than the problem. A phase that did not need a resource did not
demand it.

Two rules, both portable:

- **No silent fallbacks.** A missing precondition stops the work loudly. The alternative is a
  run that completes on a degraded path and reports success.
- **Every failure message names the remedy.** "X is missing" is a diagnosis. "X is missing —
  do Y" is a runbook entry that happens to fire at the right moment.

---

## Gates are mechanisms, not intentions

When the same class of failure recurs, the response is a mechanism that makes the failure
unavailable — not a better-executed version of the same fix (L-17).

Mechanisms observed across the corpus, generalized:

- **A ratchet** — a quality floor that may rise and may never fall.
- **A refusal to start** — the work does not begin when its preconditions are unmet, rather than
  beginning and degrading.
- **An idempotency check** — run the procedure twice; the second run must do nothing. This
  converts "we believe this is repeatable" into something checked every time.
- **A posture check** — run the verification a second time under the *restricted* conditions
  that actually apply in practice, not the permissive ones you develop under. OD found this
  caught a whole class of failure invisible in the permissive posture.
- **An incident-derived check** — every real failure becomes a cheap, always-on check whose
  description is the incident report. OD did this systematically; the docstrings *are* the
  postmortems.

And the rule protecting all of them, which OD states directly: **"the guard is intentional — fix
the cause, don't disable it."** A gate that gets switched off to unblock work has not been
consulted; it has been overruled, and that is a decision that belongs in the ledger.
