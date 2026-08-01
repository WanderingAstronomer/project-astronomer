---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - capability_rule
  - capability_role
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# 08 — Instruments

[`06-delegation.md`](06-delegation.md) establishes that **the operator is the instrument** and that
the instrument has known error. [`07-boundaries.md`](07-boundaries.md) establishes what a
collaborator may **run** and what must not **leave**.

This file names what was missing between them: **a collaborator, and the environment it acts
through, are also instruments — and an instrument that has not declared its error is not yet an
instrument.** That obligation is law-grade and is stated once, as L-18
([`01-laws.md`](01-laws.md)). What follows is how it is discharged.

> **Status: single-attested and provisional (D-006).** Every rule here is attested by **VOC** only.
> K-1…K-6 come from a single day in which a collaborator with standing filesystem access, a network
> and a shell mapped a platform it was about to build on; **K-7 comes from the same project five
> days later**, which makes it a second occasion and *not* a second attestation — VOC is one
> project however many times it is asked. One project is a practice, not a law (CHARTER invariant
> 4). The scars are real and are cited; the convergence is absent. Per D-022 no incident is
> manufactured to satisfy the rule about incidents — where a rule rests only on an argument, it
> says so.
>
> **The corpus status changing to `VALIDATED` (D-049) does not touch any grade here.** Ratification
> is a fact about the framework having been run; attestation is a fact about how many independent
> projects arrived at a given rule. These rules still rest on one.

**Why `K-`.** These rules are prefixed `K-` (capability), not `I-`, because the first project that
will consume them already numbers six invariants `I-1`…`I-6` and cites them constantly. A bare
`I-3` inside that project would resolve to two things, which is the ambiguity L-2 exists to prevent
and which one source project had to publish a disambiguation rule to escape. Choosing the prefix to
avoid the collision costs nothing; discovering it later costs every historical reference.

---

## I. What must be established

### K-1. Capability and permission are separate facts, established separately.

What an instrument **can** do is measured. What it **may** do is asked. Neither implies the other,
and a declaration that reports only one of them is not a declaration.

- **Attested:** VOC. A capability survey of a platform found the mechanism for a feature fully
  present in the interface and the credential lacking the scope to reach it — capability yes,
  permission no. In the same survey the credential held full administrative rights over a
  subsystem that **did not exist** on that installation — permission yes, capability no. Both
  errors were available in the same hour, in opposite directions.
- **The scar:** the survey's first pass reported "an agent can run the lifecycle through this
  platform" on the strength of the interface alone. Thirty-two claims were subsequently refuted by
  a second pass whose only instruction was to re-measure rather than re-read, and the largest
  single class was *documented capability that this installation did not have.* The general form
  had been read correctly. The instance had never been measured.
- **Off-software:** a clinic that has the equipment and not the accreditation, and a clinician who
  has the licence and no equipment, are both unable to run the test — for reasons that require
  different questions to discover, and that no single question finds.

### K-2. Name the role. Then bind the provider.

A project requires *a place where work items live with identity and state.* It does not require any
named product. The **role** is durable and belongs to the project; the **provider** is a fact about
the environment and belongs to the capability declaration.

- **Attested:** none for the rule; **single-authored.** The argument is inherited rather than
  observed: L-1's own list of what is deliberately *not* a law excludes toolchain — "version
  control, file formats, and storage are implementation" — and records that of four source projects
  one was not a repository at all and achieved provenance through a frozen specification.
- **The scar:** VOC's, and it is a near miss rather than a failure. A platform capability study
  produced an excellent answer shaped entirely around one vendor's feature names. Folded into a
  framework as written, it would have made every future project require that vendor, and would have
  silently excluded the air-gapped case that the studied project had itself declared an invariant.
  The defect was caught in review, which is not a mechanism (L-17).
- **Off-software:** "we need a shared calendar" survives the company changing calendar software.
  "we need Outlook" does not, and it was never what was needed.

### K-3. Every role declares its fallback before the fallback is needed.

Absent capability is the **normal case**, not the exception. Each role carries a ladder: the
preferred provider, what is used when it is unavailable, and the rung at which the honest answer is
*this is not recorded anywhere.*

- **Attested:** VOC, by extension of a practice rather than a stated rule. One source project kept a
  standing ledger of what was **owed to real devices** rather than letting a weaker verification
  pass silently (L-12), which is the same move applied to measurement instead of storage.
- **The scar:** VOC's platform survey is mostly a catalogue of absences — a scope not granted, a
  view type no interface can create, a documentation surface that does not resolve, a whole class of
  field available only to organizations. A declaration that recorded only what was *present* would
  have been an accurate document from which no work could be planned, because every plan would have
  stopped at its first refusal with nothing written about what to do instead.
- **Off-software:** the lowest rung is not failure. "This will not be recorded, and I know it" is a
  usable state; "this will be recorded" followed by silence is not, and it is the L-16 defect.

### K-4. A capability declaration expires.

It is dated. It is re-measured when the environment changes — a granted permission, a new tool, a
different machine, a moved account — and the re-measurement is an event, not a courtesy.

- **Attested:** VOC. L-11's rule that a quoted number is stale on sight, applied to the environment
  rather than to a quantity. L-18 states the general obligation; this rule states its half-life.
- **The scar:** the same survey found the studied project's own always-loaded governing instructions
  were **not in version control**, so any fresh session on any other machine inherited none of
  them. That had been true for over a thousand commits. Nobody had lied: the capability was real
  where it was measured, and had never been re-measured anywhere else.
- **Off-software:** a key that opened the door in March is a claim about March.

---

## II. What follows from it

### K-5. Decision rights are a capability, and are interrogated like any other.

How much a collaborator may settle unattended is a fact about *this* project — established at
setup, recorded in the declaration, and cited rather than renegotiated. The reserved categories
(the non-delegable table in [`06-delegation.md`](06-delegation.md)) are the floor; everything above
it is set once.

- **Attested:** VOC. The source project's standing rule already had both halves — *"a stalled
  session is worse than a documented judgement call"*, bounded by *"every such call must be cheap
  to reverse"* — but held them as a per-session understanding rather than a recorded project fact.
- **The scar:** across one working day the collaborator returned roughly sixteen decisions to the
  operator, of which about half were reserved and about half were sequencing and bookkeeping calls
  it was equipped to make. The operator's summary was that there was *"a lot of work that I have to
  do that you could handle."* Nothing was wrong with the rule; it had no home, so it was
  re-derived, differently, every time. **A rule that lives only in a conversation is re-negotiated
  at the start of every conversation.**
- **Off-software:** the useful version of "use your judgement" names the three things that are not
  yours to judge. Without that list it is not delegation, it is an invitation to guess where the
  line is.

### K-6. The declaration is written by the instrument that is being declared, and it is not trusted for that reason.

A collaborator states its own limits, which is the only party positioned to measure them and the
worst positioned to be honest about them. The bias has a known direction: **toward claiming too
much.** Compensate mechanically (B-6, [`04-verification.md`](04-verification.md)) — a limit the
collaborator asserts about itself is `INFERENCE` until something has failed in the way the limit
predicts.

- **Attested:** VOC. The refutation pass exists precisely because the first pass could not be
  trusted about itself; its instruction was to default to refuted when it could not independently
  confirm, and it overturned thirty-two claims.
- **The scar:** the same collaborator asserted that a provider change required no code, having read
  that the endpoint was configurable. One configuration value served two unrelated subsystems, so
  the change would have silently broken the one that was working. It was caught by probing the
  seam, not by reading about it — the claim had been confidently wrong in the direction of claiming
  too much, which is the direction K-6 names.
- **Off-software:** self-report is indispensable and is not evidence. It is the only source for how
  something feels and the weakest source for what actually happened.

### K-7. A shared index has finite signal, and adding to it can subtract.

Every other rule in this file treats capability as additive: an instrument you gain is an instrument
you have. **Retrieval is the exception.** A corpus and the index over it are two instruments, not
one, and material added to the second competes for a fixed number of answer slots with everything
already there. A *fully successful* acquisition — nothing corrupted, nothing unread, coverage
complete — can still degrade the ability to find anything else.

So an index carries a second declaration beside its capability: **what share of it is foreign to the
project's own thinking**, measured rather than estimated, before the material lands and again after.

- **Attested:** VOC, single, and the corpus cannot corroborate it (`provenance/attestation.json`).
  Three measured instances in one session (`O-35`), plus a fourth of the same class measured
  independently three days later (`O-36`).
- **The scar:** one vendor's documentation was imported at high quality and reached **390 of 719
  notes — 54% of the corpus**. A semantic query for the project's *own* technology stack then
  ranked a vendor navigation link above its own architecture documents; two further searches
  returned 364,155 and 224,288 characters and were abandoned unread. **Two of the three obstructed
  a correction that was already in progress** — the index failed hardest at the moment it was being
  used to repair something. Nothing had gone wrong with the intake. `rituals/corpus-intake.md`
  counted the source and recorded full coverage, exactly as instructed, because it had no step that
  looks at the destination.
- **Off-software:** a filing cabinet where one client's papers fill six of eleven drawers. Nothing
  is lost and every drawer is correctly labelled; finding anything belonging to any other client
  now takes six times as long, and the person who filed it did nothing wrong.

---

## The roles

The default set. A project adds roles it needs and strikes roles it does not; the *set* is
project-level, the *rule that each row carries a provider and a fallback* is not.

| Role | What it must provide | Typical provider, software | Typical provider, off-software |
|---|---|---|---|
| **Work-item store** | items with identity, state, and history | an issue tracker | a numbered list in a bound log |
| **Relation graph** | blocking and containment between items | dependency and parent links | indentation, and "waiting on" notes |
| **Working set** | what is in hand now, versus later | one open milestone | a page headed *this week* |
| **Change record** | what changed, when, why, and reversibly | commits and reviewed merges | dated entries, initialled |
| **Verification gate** | a check that fails *before* work lands | required automated checks | a second person's signature |
| **Durable prose** | doctrine, decisions, scars | tracked files in the repository | a binder that leaves the room with you |
| **Corpus retrieval** | what bears on a question, without knowing its address | an index searched by relevance | a librarian, or a card catalogue |
| **Session inheritance** | what a new collaborator reads before acting | an always-loaded instruction file | the briefing sheet on top of the binder |

**Session inheritance is the row most often assumed and least often checked**, and it is the row
whose absence is invisible from inside a session that already has the knowledge.

**Corpus retrieval is the row most often confused with the row above it.** *Durable prose* is where
the record is kept; *corpus retrieval* is whether anything in it can be found. A project small
enough that one person knows every filename provides the second role out of that person's memory
and never notices it is a role at all — which is why the ladder below ends where it does, and why
this row is the one that fails on a schedule nobody is watching (`O-32`, `O-44`). It is also the only
row governed by K-7, because it is the only one where **adding** to the instrument can subtract from
it.

## The fallback ladder

Each role's ladder is written in the declaration, most-preferred first, ending at an honest floor.
The worked shape, for the roles above:

- **Work-item store** → tracked issues → a tracked file listing items → the operator's memory,
  *declared as not recorded*
- **Relation graph** → native links → a stated field inside each item → **not recorded**; the
  operator names what is next at pick time
- **Verification gate** → a required automated check → a manual checklist run before landing → a
  post-hoc review, *declared as detection rather than prevention*
- **Corpus retrieval** → an index that ranks by relevance → exact-match search over the whole
  corpus → a directory listing read by hand → **not indexed**; whoever wrote it remembers where it
  is, *declared, and named as a person*
- **Session inheritance** → an always-loaded tracked file → a file the collaborator is told to read
  → re-briefing every session, *declared, and budgeted*

**Two notes on the retrieval ladder specifically**, both measured (`O-35`, `O-36`). The rungs are
ordered by *power*, and power is not the same as reliability: relevance ranking is the top rung and
the **first** to fail under K-7, because it is the only rung that silently returns a *worse* answer
rather than no answer. Exact-match below it fails loudly, by returning too much. And the floor here
is worse than the floor of any other role — *not recorded* is a state you can plan around, while
**not findable** looks exactly like *not written*, which is how a project rediscovers what it
already knew.

**The floor is a legitimate rung.** What is forbidden is arriving at it without saying so — an
undeclared floor is indistinguishable from a working mechanism until the moment it is needed, which
is L-16 at the level of a plan.

## The interrogation

A declaration is produced by asking, not by assuming: measure what the environment can do, ask the
operator what it may do, and record what could not be determined as owed. The procedure is
[`../rituals/capability-interrogation.md`](../rituals/capability-interrogation.md); it runs inside
[`starting-a-project`](../rituals/starting-a-project.md) and again whenever
[`instrument-drift`](../rituals/instrument-drift.md) fires. Its output is
[`../artifacts/capability-inventory.template.md`](../artifacts/capability-inventory.template.md),
paired with [`../artifacts/operator-profile.template.md`](../artifacts/operator-profile.template.md)
for the human half.

## What this file does not settle

- **Whether a role can be provided by a party rather than a tool.** "A second person's signature"
  is listed as a verification provider, and nothing here governs the case where the provider is
  someone who might be unavailable.
- **How to detect a capability that was silently withdrawn.** K-4 requires re-measurement on a
  *known* change. A permission revoked without notice is caught at the next interrogation and not
  before, and nothing here shortens that interval.
- **Aggregate capability.** Each role is assessed alone. A plan that is feasible role-by-role can
  still be infeasible in combination — the same unresolved shape B-2's aggregate-disclosure gap has,
  and it is unsolved here for the same reason.
- **Any specific platform, credential model, or probe.** Implementation, excluded from doctrine for
  the reason L-1 excludes every other toolchain question.
- **What share of an index may be foreign before K-7 bites.** The one measured figure is 54%, and it
  is a point at which the instrument had *already* failed — not a threshold, and the corpus has no
  observation of the share at which it starts to. A project pre-registers its own number
  (`rituals/corpus-intake.md`) and reports what it measured; quoting 54% as a limit would be exactly
  the borrowed number L-11 forbids.
- **Whether segregating an index actually restores it.** The obvious response to K-7 is to hold
  foreign material in a separate index, or behind a path the default query does not reach. **Nobody
  has done it.** The one project that hit K-7 responded with a rule its collaborator is asked to
  remember, which `O-39` is the direct evidence against. The remedy is `UNVERIFIED` and is owed.
- **How a monotonic change triggers K-4.** A declaration expires on an *event*, and an index that
  grows every day presents none. `O-44` measured a corpus 2.35× its declared size with nothing
  having "changed" in the sense K-4 names. Whether the trigger should be a magnitude, a period, or
  a check at read time is unsettled.
