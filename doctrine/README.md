# Doctrine

The reasoning layer. [`artifacts/`](../artifacts/) holds the shapes these arguments imply;
[`rituals/`](../rituals/) holds the procedures; [`install/`](../install/) holds the compressed,
enforceable form a collaborator actually reads each session.

**Living documents.** These state what the framework currently holds. History lives in
[`DECISIONS.md`](../DECISIONS.md) and the commit tree, not in change-log sections here
(L-13).

## Reading order

| | | Read it when |
|---|---|---|
| [`00-precedence.md`](00-precedence.md) | Which document wins when two disagree | Setting up a project — it is the shortest and prevents the most expensive failure |
| [`01-laws.md`](01-laws.md) | The seventeen laws, with attestation and scars | **Start here.** Everything else is derivation |
| [`02-epistemics.md`](02-epistemics.md) | Typed claims, scope, the evidence ladder, confidence | Before recording anything. This is the part that does the work |
| [`03-the-loop.md`](03-the-loop.md) | OBSERVE → TRIAGE → RESOLVE → ACT → RECORD | Whenever something surprises you |
| [`04-verification.md`](04-verification.md) | Adversarial verification, altitude, instrumentation, gates | Before believing a result — especially your own |
| [`05-the-record.md`](05-the-record.md) | The four record classes — living, frozen, append-only, disposable; ledgers; identifiers | When deciding where something goes |
| [`06-delegation.md`](06-delegation.md) | Roles, fences, briefs, the non-delegable categories | Before handing work to anyone, human or otherwise |
| [`07-boundaries.md`](07-boundaries.md) | What must not leave, and what a collaborator may run | Before a collaborator has filesystem access, a network, and a shell at once |

## If you read only one thing

**Observation and inference are different things, and the artifact says which** (L-3). All four
source projects invented some version of this independently, without shared domains or shared
code. It is the strongest signal in the corpus, and a project that adopts nothing else but marks
its claims `CONFIRMED` or `UNVERIFIED` will already be ahead of where it would otherwise be in
six months.

## A note on how these are written

Every law carries the concrete failure that produced it (D-003). This makes the documents longer
than a rule list and it is not decoration: a rule stated without its incident has no defense the
first time following it is expensive, and it loses. The scar *is* the argument.

Where a claim here is single-authored rather than extracted from a source project, it says so
inline and is listed in [`provenance/lineage.md`](../provenance/lineage.md) under "Original to
Astronomer." Those are the weakest parts of the framework and the first that should change.
