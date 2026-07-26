# Starting a project

> **Doc status:** living.

## When

You are beginning work that will run on Astronomer and nothing has been declared yet — no
charter, no ledger, no precedence order. Also use this when adopting the framework over work
already in progress: in that case the existing material is **input to the first observation
window**, not settled record, however finished it looks.

## Do

0. **If the collaborator's filesystem access reaches beyond this project's own work product,
   declare the data boundary first** — before opening anything. Three named tiers: RED (do not
   open, each with its reason), GREEN (read freely, named affirmatively), YELLOW (ask first, case
   by case). An unlisted item is unclassified, not GREEN
   ([`artifacts/data-boundary.template.md`](../artifacts/data-boundary.template.md)). Then declare
   the collaborator's own workspace — separate from the project's artifacts — with a `README.md`
   pointing to a "read this first" living state-of-play doc.
0b. **Declare what may leave, separately from what may be read** — permission to read is not
   permission to transmit (B-1, [`doctrine/07-boundaries.md`](../doctrine/07-boundaries.md)). Fill
   this in even when the answer is "nothing"; an unstated egress boundary reads as an unrestricted
   one. **A query is derived data** (B-2): anything built *from* restricted material carries
   information out with no copied string in it. If any outbound channel is permitted, open the
   [query log](../artifacts/query-log.template.md).
0c. **If something other than the operator is doing the observing, run
   [capability-interrogation](capability-interrogation.md)** — the procedure that discharges L-18.
   It produces the
   [capability inventory](../artifacts/capability-inventory.template.md): the roles this project
   needs and what actually provides each, with **capability and permission in separate columns**
   (K-1), a fallback ladder per role (K-3), the decision-rights band (K-5), and **where the
   collaborator is systematically wrong, with a direction**. Every other instrument in this
   framework declares what it cannot detect; this is the one that was exempt.

   **Set decision rights here, once, and then hold them.** The non-delegable categories are the
   floor (step 6); above that floor, what the collaborator settles alone is an operator call made
   at setup. Left unset it gets re-derived differently every session, and the cost lands on the one
   instrument that cannot be parallelised.
0c-bis. **If the operator's input arrives through augmentation rather than directly, write the
   [operator profile](../artifacts/operator-profile.template.md)** in the same sitting — anything
   that transcribes, dictates, translates, batches or otherwise reshapes intent before it reaches
   the collaborator. Not a courtesy: length reads as emphasis, structure reads as deliberation, and
   a single long message reads as a single ask, and all three are wrong in a knowable direction when
   a tool shaped the input. Write it **with** the operator — an inferred profile they have never
   read is a set of assumptions with a filename.
0d. **If the project is taking in material it did not author, run
   [corpus-intake](corpus-intake.md) before the first window** — count it, check per-item
   readability, and record what could not be read. A failed extraction returns a page count, no
   error, and almost no text.
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

- The **data boundary** (read tiers *and* egress) and the collaborator's **workspace README**, if
  Step 0 applied — before anything else, since they gate what may be read while writing everything
  below. Plus the **query log**, **capability inventory**, **operator profile**, and **source
  manifest** wherever 0b–0d applied. These are gated on circumstance, not on tier: a Lite project
  next to a client's files needs all of them, and a Full-tier project on a clean repository of its
  own making needs none ([`tiers/`](../tiers/README.md)).
- `CHARTER` — mission, scope, invariants, precedence, vocabularies, definition of done.
- `DECISIONS` — the tier choice, the precedence adoption, the vocabulary set, the scrutiny gate,
  and the non-delegable list, as separate numbered entries. Separate, because they will be
  superseded separately.
- `OBSERVATIONS` — the log, opened and empty, with the first window's declaration as its header.

Do not begin ACT-phase work before that window closes (L-7). If something obviously needs fixing
on day one, it is an observation.
