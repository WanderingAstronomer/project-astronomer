# Capability interrogation

> **Doc status:** living.

The forward half of [instrument drift](instrument-drift.md). That ritual is repair, written for the
moment you discover a limit you have already relied on. This one runs before the work and costs a
paragraph per row.

Doctrine: [`../doctrine/08-instruments.md`](../doctrine/08-instruments.md) (K-1…K-6), obligation
L-18. Output: [capability inventory](../artifacts/capability-inventory.template.md) for the
environment and the collaborator, [operator profile](../artifacts/operator-profile.template.md) for
the human.

## When

- **At setup**, inside [starting a project](starting-a-project.md), before the first observation
  window opens.
- **Whenever the environment changes** in a way you know about: a permission granted or revoked, a
  tool installed or lost, a different machine, an account moved, a version bumped (K-4).
- **Whenever a limit surprises you mid-work.** The surprise is an observation (L-7); log it, finish
  the step if you honestly can, and re-run this at the boundary.

## The division of labour, and it is not negotiable

**The collaborator answers capability by measuring. The operator answers permission by deciding.**

Neither may answer the other's question. A collaborator that infers permission from the fact that
access exists has skipped the only party who can grant it; an operator asked to state a capability
is being asked to guess about their own tooling. K-1 exists because both errors were available in
the same hour.

## Do

1. **List the roles this project needs.** Start from the default set in
   [`08-instruments.md`](../doctrine/08-instruments.md), strike the rows that do not apply, and add
   any the project needs that the default set omits. Striking a row is a decision and goes in the
   ledger with its reason — an unneeded role removed deliberately is hygiene, and one removed
   silently is a gap nobody can see later.

2. **For each role, measure the candidate provider in place, now, yourself** (L-11, L-18). Not from
   documentation about the general case, and never from a previous session's inventory — that is the
   stale-number failure committed against yourself, and the template forbids it explicitly.

   **Probe read-only.** A probe that creates, edits or deletes has changed the thing it was
   measuring, which is L-7 at the scale of an environment. Where a capability can *only* be proven
   by writing, say so, describe the exact write that would prove it, and leave it unproven until
   the work legitimately performs it. An unproven capability that is honestly labelled is worth more
   than a proven one that cost you a mutation you did not intend.

3. **Record capability and permission in separate columns** (K-1). Both, for every role. "Present
   and forbidden" and "permitted and absent" are different states with different remedies, and a
   single column collapses them into a shrug.

4. **Ask the operator the permission questions, in one pass, plainly.** Not one at a time as the
   work reaches them — that converts a ten-minute setup into a week of interruptions, which is
   exactly the friction K-5 was written from. Where the answer is a trade-off between goods rather
   than between right and wrong, it is a **Preference** and must be elicited, never inferred
   ([`../doctrine/06-delegation.md`](../doctrine/06-delegation.md)).

5. **Write each role's fallback ladder** (K-3), most-preferred first, ending at a floor you would be
   willing to state out loud. The floor is a legitimate rung. What is forbidden is arriving there
   without having written it down, because an undeclared floor is indistinguishable from a working
   mechanism right up to the moment it is needed.

6. **Set decision rights** (K-5). The non-delegable categories are the floor and are not restated
   here. Above them, record in one place: what the collaborator settles alone, what it settles and
   logs, and what it stops for. Then hold it — a right recorded and then re-asked is not a right,
   it is a habit of asking.

7. **Record what could not be determined as owed**, not as absent. A capability you were unable to
   test is a debt with a name; a capability you omitted because testing was awkward is a hole with
   none. The model is a source project that shipped a written ledger of what was owed to real
   devices rather than letting a weaker verification stand in silently (L-12).

8. **Date it, and say who measured it** (K-4). An inventory with no date is a claim about an
   environment that may no longer exist.

## Do not

- **Do not copy the previous inventory forward.** Re-measure. This is the one prohibition in the
  template that is stated as forbidden rather than discouraged.
- **Do not write "no known limitations"** in the known-error section. That is the absence of an
  inventory wearing the shape of one, and it is the single most likely false sentence in the
  artifact.
- **Do not let the roles name a vendor.** The role is durable, the provider is an environment fact
  (K-2). A project whose charter requires a named product cannot survive the product, and one
  source project was not a repository at all.
- **Do not treat your own probe as authoritative on first run.** Output from an instrument you built
  and have not broken on purpose is `INFERENCE` (B-6). This framework's own gate reported fourteen
  defects on its first run and nine were artifacts of the gate.

## Record

- `OBSERVATIONS` — each measurement that surprised you, verbatim, with the command or the question
  that produced it.
- The **capability inventory** (living, dated) — roles, providers, capability, permission, ladders,
  and the owed list.
- The **operator profile** (living, dated) — the human half: what this operator is augmented by,
  where their reporting is strong and where it is thin, and what that implies for how work should be
  shaped.
- `DECISIONS` — the role set with any strikes and their reasons; the decision-rights band; and each
  Preference the operator settled, so it is not re-elicited next session.

## The failure this prevents, stated once

A collaborator surveyed a platform it was about to build a project on and reported broad capability
from documentation. A second pass, instructed only to re-measure rather than re-read, overturned
**thirty-two** claims. The same survey found the project's own always-loaded governing instructions
were not in version control, so every fresh session elsewhere inherited none of them, and had not
for more than a thousand commits.

Neither was a lie. Both were limits nobody had been required to state — and both were found by
something else looking.
