---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - conflicting-decisions-procedure
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Conflicting decisions

> **Doc status:** living.

## When

Two entries in the ledger tell you to do different things, or a decision conflicts with the
charter, or you have just noticed you have been following one rule while another was also live.

Also route here on the quieter version: a bare `D-<n>` reference that could resolve to more than
one ledger. That ambiguity silently disables the supersession chain, which is the only mechanism
that makes a ledger trustworthy at all.

**Never resolve by recency.** The later entry is not the winner for being later.

## Do

1. **Check the reference resolves first.** A bare ID resolves to the **local** ledger only.
   Cross-project references carry a prefix. If the conflict evaporates once the IDs are
   namespaced, it was a citation defect — fix the citation and stop.
2. **Check for supersession by naming** (L-2). Does either entry explicitly name the other as
   replaced? If yes, the conflict is already resolved and the ledger just reads badly. Note it and
   stop.
3. **If neither names the other, both are live.** This is the real case. You do not get to infer
   which one won from the dates.
4. **Apply precedence** ([`doctrine/00-precedence.md`](../doctrine/00-precedence.md)). Higher
   wins; the lower is **wrong**, not "in tension." Charter over decisions, decisions over
   specification, specification over findings, findings over observations.
5. **Check reality outranks all of it.** If either entry contradicts an actual measurement, the
   document is wrong regardless of where it sits — including the charter. Verify against the
   source before adjudicating between two documents (L-11).
6. **Resolve by writing a new entry that names both.** Which survives, which is superseded, why.
   Never edit either original: the ledger is append-only, and the losing entry is evidence about
   what you believed and when.
7. **If the charter itself is wrong, amend it deliberately** — with its own dated ledger entry
   saying what changed and why. A charter amended silently is a corpus with no top of stack, which
   is the failure the stack exists to prevent.
8. **Establish what was built under the losing rule.** Anything decided or done while the wrong
   entry was live is suspect and gets re-checked. This is what turns the friction into a
   conflagration; do it before someone else discovers it.

## Record

- `DECISIONS` — one new entry: both IDs named, which survives, the precedence or evidence that
  decided it, and a live UTC stamp. Mark `[operator]` if a human made the call.
- `DECISIONS` — a separate `AMENDS D-<n>:` line where an existing entry needs annotation. Amend,
  never edit.
- `CHARTER` — only if amended, and only with the ledger entry from step 7 already written.
- The list of work performed under the losing rule, routed back into triage with the bucket its
  evidence now supports.
