# Recurring defect

> **Doc status:** living.

## When

The same class of failure has now happened three times. Not three symptoms that look alike —
three instances of one mechanism.

Recognizable by: you are applying a fix you have applied before; a previous hand-fix has drifted
back; or you have resolved to be more careful about this before.

**The third instance is evidence about the mechanism, not about the instance.** Stop fixing
instances (L-17). If you have resolved to do something four times, the problem is not resolve.

## Do

1. **Confirm it is one class before treating it as one.** Three failures that co-occur in kind are
   three failures until a shared mechanism is proven at a cited location (L-5). If you cannot name
   the mechanism, you have a pattern-match, and building a gate on it will gate the wrong thing.
2. **Fix the current instance if it is live** — then stop, and do not fix a fourth by hand.
3. **Choose a gate** ([`doctrine/04-verification.md`](../doctrine/04-verification.md)):
   - **Ratchet** — a quality floor that may rise and may never fall.
   - **Refusal to start** — the work does not begin when its preconditions are unmet, rather than
     beginning and degrading.
   - **Idempotency check** — run the procedure twice; the second run must do nothing. Converts
     "we believe this is repeatable" into something checked every time.
   - **Posture check** — run the verification again under the *restricted* conditions that
     actually apply in practice, not the permissive ones you work under.
   - **Incident-derived check** — a cheap, always-on check whose description **is** the incident
     report.
4. **Prefer the gate that makes the failure unavailable** over the one that detects it. Detection
   still requires someone to act; unavailability does not.
5. **Break it and confirm the gate fires.** Arrange the exact condition the gate exists to catch,
   and check that it catches it. An unexercised alarm is a hypothesis about an alarm — the
   canonical failure is a correct check that was blind to the one thing it was built for.
6. **Write the incident into the gate's own description**, so it explains at the point of firing
   what went wrong the three times and what to do. Every failure message names the remedy.
7. **Do not switch it off to unblock work.** The guard is intentional: fix the cause. If a gate
   genuinely must be disabled, that is not a workaround — it is a **decision**, and it goes in the
   ledger with a reason and a condition for restoring it.

## Record

- `DECISIONS` — one entry naming the defect class, the three cited instances, the gate chosen and
  why that one, and the evidence that the gate fires. Any later suspension of the gate is its own
  entry, with `blocks-on:` the condition for turning it back on.
- `FINDINGS` (frozen) — the mechanism, with citations for all three instances.
- The gate itself, wherever gates live for this project, carrying the incident as its description.

Exit condition: the fourth instance would be caught without anyone remembering to look for it.
