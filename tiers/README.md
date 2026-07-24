# Tiers

Astronomer scales down. The **laws hold identically at every tier** — tiers change only which
*artifacts* a project is required to produce (D-008, CHARTER invariant 6).

This distinction is the whole point. A framework that relaxes its rigor for small projects
teaches you to negotiate with your own standards, and the negotiation does not stop at the tier
boundary. A framework that demands a full apparatus for a two-week experiment gets abandoned in
week three and takes its laws with it. Tiering the artifacts and fixing the laws is what lets
both survive.

**Lite is smaller, not looser.**

---

## Choosing

Pick the lowest tier that satisfies all of its conditions. When two tiers both seem to fit, take
the lower one — an under-tiered project can be promoted mid-flight in an afternoon, while an
over-tiered project is usually abandoned rather than demoted.

| | **Lite** | **Standard** | **Full** |
|---|---|---|---|
| **Contributors** | one | one or more, or an AI collaborator doing substantive work | multiple parallel workstreams |
| **Reversibility** | mistakes are cheap and reversible | mistakes cost real time or money | mistakes are expensive or irreversible |
| **Duration** | weeks | months | months to years |
| **Consequence of being wrong** | you learn something | you lose work | you harm something you cannot restore |
| **Will someone rely on your conclusions?** | no | possibly | yes |

---

## Lite — three artifacts

**Required:** [charter](../artifacts/charter.template.md) ·
[decision ledger](../artifacts/decisions.template.md) ·
[observation log](../artifacts/observation-log.template.md)

This is the minimum at which the framework is still itself. All three exist because each solves
a problem that shows up in week one, not week twenty:

- The **charter** stops scope from drifting silently. One page. Mission, what is out of scope,
  the invariants, and what "done" would mean.
- The **ledger** stops you from re-litigating a decision you already made and losing the reason
  you made it. This is the highest-value-per-minute artifact in the framework.
- The **observation log** keeps observation separate from inference (L-3), which is the thing you
  cannot reconstruct afterward. Everything else can be rebuilt from memory. This cannot.

Triage happens in your head or in a scratch file. Findings live in the log. Nothing is frozen
except the log itself, which is append-only.

**Lite is the right tier for most personal projects, and it is not a compromise.** Two of the
four source projects ran effectively at this tier for their first several months.

**Four conditional artifacts, gated on circumstance rather than stakes.** Each is required from
**Lite** upward once its condition holds, and skipped entirely when it does not:

| Artifact | Required when |
|---|---|
| [data boundary](../artifacts/data-boundary.template.md) | the collaborator's filesystem access reaches beyond the project's own work product — a shared drive, a client's raw files, another team's directory |
| [source manifest](../artifacts/source-manifest.template.md) | the project takes in material it did not author |
| [query log](../artifacts/query-log.template.md) | a data boundary exists **and** any outbound channel is permitted |
| [capability inventory](../artifacts/capability-inventory.template.md) | something other than the operator is doing the observing |

**These are not tiered, and the reason matters.** Their conditions have nothing to do with how much
is at stake. A one-person Lite project sitting next to a client's raw files, taking in documents it
did not write, with an AI collaborator doing the reading, needs all four — while a Full-tier project
working on a clean repository of its own making needs none of them. Tiering these would have left
the smallest projects the least protected, which is backwards, and it is the case where "Lite is
smaller, not looser" has actual teeth.

The three conditions after the first all became live at the same moment: when a collaborator has
standing filesystem access, a network, and a shell at once. None of the four source projects had all
three, which is why these are the newest and least-attested artifacts in the set
([`doctrine/07-boundaries.md`](../doctrine/07-boundaries.md)).

---

## Standard — adds triage, findings, and durable records

**Adds:** [triage board](../artifacts/triage-board.template.md) ·
[findings](../artifacts/findings.template.md) ·
[frozen record](../artifacts/frozen-record.template.md) ·
[runbooks](../artifacts/runbook.template.md)

The jump to Standard is driven by one thing: **someone will act on your conclusions later, and
that someone may be you with no memory of the context.**

- The **triage board** exists once you have more findings than you can hold in your head. Buckets
  A–E by epistemic state, clusters by shared cause, and — critically — a standing list of the
  decisions owed to a human.
- **Findings** separate *what the world is* from *what you decided about it*. Frozen at the point
  of issue; corrections are addenda.
- **Frozen records** capture a run, a pass, or a period so that its numbers survive the next
  revision of your understanding.
- **Runbooks** appear the second time you hit the same friction. Not before — a runbook written
  in advance of the friction is a guess about a procedure.

---

## Full — adds inventory, fences, and mechanical gates

**Adds:** [catalog](../artifacts/catalog.template.md) ·
[briefs](../artifacts/brief.template.md) ·
[shared preamble](../artifacts/shared-preamble.template.md) ·
[reports](../artifacts/report.template.md) · pre-registered gates

Full tier is for work that outgrows a single working memory — multiple parallel workstreams,
long horizons, or consequences you cannot walk back.

- The **catalog** is the exhaustive inventory, with the completeness guarantee: every item in
  scope is assigned to exactly one row, and the orphan list must come back empty. Its **edges**
  section — the seams between areas — was called "the most important artifact in the catalog" by
  the project that built one, because a plan that is locally coherent in every area can still be
  globally wrong at the joins.
- **Briefs** and the **shared preamble** exist the moment work is delegated to someone who cannot
  ask you a question mid-flight.
- **Reports** close the loop from a delegated workstream, with the two sections that make a
  report evidence instead of advocacy: defects found in your own work, and what you did not
  verify.
- **Gates** become mechanical (L-17) rather than remembered.

**A warning that belongs at this tier specifically.** Parallelism has a real correctness cost
(L-10): the source project that ran the largest concurrent effort found eleven collision sets,
eight of them the class where two independently correct changes combine into a wrong result that
nothing flags. Against a proposal for ten concurrent workstreams its conclusion was *"three is
the honest safe maximum. Two is the recommended default."* Reach Full tier for the catalog and
the fences long before you reach it for the concurrency.

---

## Tier is a decision, and it goes in the ledger

Record the tier and the reason on day one:

```
[<live UTC>] D-001: **This project runs at Standard tier.** Solo, but the conclusions will
drive decisions I cannot easily reverse, and I will not remember the context in six months.
Lite's three artifacts do not give me a place to freeze a finding.
```

**Promotion is normal.** A project that outgrows its tier is a project that is going well.
Promote by adding the artifacts, logging the decision, and — importantly — *not* retroactively
reformatting the work done at the lower tier. That work is a frozen record of how the project ran
then (L-13).

**Demotion is rarer and needs more care.** Dropping an artifact means dropping a place where
information was going. Say in the ledger where that information will go instead. "It will not be
recorded" is an acceptable answer, stated out loud; it is only a problem when it is the silent
answer.
