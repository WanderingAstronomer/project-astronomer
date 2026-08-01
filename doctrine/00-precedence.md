---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - the-precedence-stack
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# 00 — Precedence

> **Status:** Authoritative for conflict resolution. Where any other document in an Astronomer
> project conflicts with the order declared here, this document decides which one is wrong.

Most corpora do not fail by containing an error. They fail by containing two documents that
disagree, with nothing to say which one is binding — so both survive, both get cited, and the
project quietly runs on whichever one the reader found first.

Every Astronomer project declares a precedence order on day one. It is the cheapest artifact in
the framework and the one that prevents the most expensive class of failure.

## The stack

Higher wins. When two artifacts disagree, the lower one is **wrong** — not "in tension," not
"a different perspective." It is wrong, and it gets corrected or annotated.

```
1. CHARTER            why this exists; the invariants. Amended only by explicit decision.
2. DECISIONS          what was decided, when, and by whom. Append-only.
3. SPECIFICATION      what is currently true. Living; rewritten to match reality.
4. FINDINGS           what was learned, at the time it was learned. Frozen.
5. OBSERVATIONS       what was seen, verbatim. Append-only.
6. EVERYTHING ELSE    notes, drafts, plans, conversation.
```

Two rules govern reading the stack:

**Reality outranks all of it.** The stack orders *documents against documents*. It does not
order documents against the world. If the specification says one thing and the actual system,
body, or corpus does another, the document is wrong and gets settled to reality — no matter how
high it sits. A charter that contradicts a measurement is a charter that needs amending.

**Frozen records are exempt from correction, not from being outranked.** A FINDINGS entry from
March that later turns out to be wrong is not edited. It stays, annotated. The living
specification carries the current truth; the frozen record carries what was believed in March,
which is itself a fact worth keeping. See [`05-the-record.md`](05-the-record.md).

## Two layers

The stack above orders a **project's** artifacts. Astronomer's own documents sit one layer
above it, and the two do not compete:

```
FRAMEWORK LAYER    doctrine → rituals          ships with Astronomer; domain-neutral
                        ↕
PROJECT LAYER      charter → decisions → ...    yours; domain-specific
```

- **A project charter is supreme within its project.** It decides scope, invariants,
  vocabularies, and tier.
- **A project charter cannot repeal a law.** Tiers change which artifacts are required; they
  never relax a law (D-008, CHARTER invariant 6). A project that needs to break a law does not
  amend its charter — it amends *Astronomer*, with an entry in this repository's ledger, because
  the exception applies to every future project or it is not an exception, it is a mistake.
- **Rituals are living, subordinate to doctrine, and never override a law.** A ritual that
  appears to contradict a law is wrong and gets corrected. Rituals hold steps; doctrine holds
  reasoning.
- **Rituals are framework-level and domain-neutral. Runbooks are project-level and
  domain-specific.** Same trigger — the second time you hit a friction — different home. If the
  procedure cannot be written without naming your subject, it is a runbook and it belongs in
  your project (D-004).

## Standing — who may change what

Precedence says which document wins. Standing says who may move one. It is stated here because the
answer differs by layer, and because leaving it unstated means it gets decided by whoever is at the
keyboard (D-042).

| To change | Who | Why |
|---|---|---|
| A **law** — add, amend, or regrade | The **operator**, by explicit recorded decision | It binds every future project, including ones with no relation to the one that prompted it. A collaborator may draft and argue for one; it does not land unratified |
| A **ritual** | A **collaborator**, on its own judgement, logged | Rituals are living, subordinate to doctrine, and cheap to reverse (B-7). A wrong ritual costs one reading; waiting for permission costs the friction that prompted it |
| An **artifact template** — adding one | The **operator** | A new template becomes *required* somewhere, which is a change to what every qualifying project owes |
| An **artifact template** — clarifying one | A **collaborator**, logged | Same reversibility test |
| A **runbook** | The **project**, never the framework | If the procedure cannot be written without naming your subject, it is not framework material (D-004, D-017) |
| A **grade** in the attestation registry | **Neither, alone.** Only an independent project's experience raises one | The author of a rule is the worst-placed party to judge how well attested it is, and the framework cannot corroborate itself |

Two rules cut across all of it.

**Anyone may propose. Proposing is not standing.** A collaborator that drafts a law, states its
scar, and argues for it has done its job correctly; the ratification is a separate act by a separate
party. Today's L-18 arrived exactly that way.

**No document is ever amended to satisfy a gate.** When a check and a document disagree, one of them
is wrong *on the merits* — decide which, fix that one, and record the reasoning. Rewording prose to
slip past a check is the same act as disabling the check, with the audit trail removed. The reverse
also holds: a gate producing a false positive is a defect in the gate, and *"the guard is
intentional"* is not a licence for the guard to be wrong.

## Declaring precedence

Every project states its stack explicitly, in its charter, even if it adopts the default
unchanged. The statement is what makes it enforceable; an assumed order is not an order.

The canonical form, attested in three of the four source projects almost word for word:

> This is the top of the authority stack. If anything in this corpus conflicts with this
> charter, **the charter wins.** Amend it deliberately, with a dated decision-ledger entry —
> never silently.

## Namespacing across projects

When one project cites another's decisions, the reference is **namespaced**. A bare `D-4` must
resolve to exactly one ledger — the local one. Cross-project references carry a prefix
(`VOC-D-4`, `DD-D-016`).

This looks like pedantry until two ledgers in the same corpus both reach `D-7`, at which point
every historical reference becomes ambiguous and the supersession chain — the mechanism that
makes the ledger trustworthy at all — silently stops working. One source project ran two
distinct `D-` namespaces (a cross-cutting spine ledger and an audit-local decision list) and had
to state the disambiguation rule explicitly after the fact.

## The scar

In one source project the specification had drifted into what its own settlement pass called
"partly fiction" — features described as built that were not, and shipped controls the spec
never mentioned. It took a dedicated multi-file pass, a fixed set of twenty rulings, and an
adversarial verification round to bring seventeen documents back to reality.

The drift was not caused by carelessness. It was caused by the absence of a rule saying which
artifact was binding when the spec and the code disagreed. Without that rule there is no such
thing as a *contradiction* — there are just two documents, and no reason to reconcile them.
