# Starting a project

> **Doc status:** living.

## When

You are beginning work that will run on Astronomer and nothing has been declared yet — no
charter, no ledger, no precedence order. Also use this when adopting the framework over work
already in progress: in that case the existing material is **input to the first observation
window**, not settled record, however finished it looks.

## Do

1. **Choose a tier** — Lite, Standard, or Full ([`tiers/`](../tiers/README.md)). Choose on
   stakes and reversibility, not ambition. Tiers change which artifacts are required; they never
   relax a law (D-008). This choice is itself a decision: log it as `D-001` with the reasoning.
2. **Write the charter.** Mission; scope IN and scope OUT; the invariants that must not be
   violated; and a definition of done written as **testable predicates**, not aspirations.
3. **Declare the precedence order** inside the charter — explicitly, even if you adopt the
   default stack unchanged. An assumed order is not an order (L-1,
   [`doctrine/00-precedence.md`](../doctrine/00-precedence.md)).
4. **Choose the vocabularies** and give each exactly one home (L-14): confidence, severity,
   effort, change size, doc status. Name that home in the charter. Every later artifact renders
   from it rather than restating it.
5. **Fix the scrutiny gate now** — which claim types earn expensive verification and which never
   qualify for promotion. Decided in advance, in the charter or ledger; a gate decided per item
   is decided by how much you want the item to be true
   ([`doctrine/02-epistemics.md`](../doctrine/02-epistemics.md)).
6. **Name what cannot be delegated**, in writing, before any work starts (L-15): identity,
   custody, acceptance, physical fact, preference
   ([`doctrine/06-delegation.md`](../doctrine/06-delegation.md)).
7. **Open the ledger.** Append the decisions you have just made, each with a live UTC stamp, its
   reason, and `[operator]` where a human made the call rather than a collaborator.
8. **Open the observation log** — empty, with its ID scheme (`O-<n>`) and its **conditions**
   fields declared up front: instrument, state, what else was going on. Fields added later cannot
   be back-filled for entries already taken.
9. **Declare the first OBSERVE window.** State what you are observing, over what period, and what
   event closes it. Then stop planning and go look.

## Record

- `CHARTER` — mission, scope, invariants, precedence, vocabularies, definition of done.
- `DECISIONS` — the tier choice, the precedence adoption, the vocabulary set, the scrutiny gate,
  and the non-delegable list, as separate numbered entries. Separate, because they will be
  superseded separately.
- `OBSERVATIONS` — the log, opened and empty, with the first window's declaration as its header.

Do not begin ACT-phase work before that window closes (L-7). If something obviously needs fixing
on day one, it is an observation.
