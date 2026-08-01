---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - the-boundary-rules
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# 07 — Boundaries

The framework already names two boundaries. [`06-delegation.md`](06-delegation.md) names work a
collaborator must not **do**. [`../artifacts/data-boundary.template.md`](../artifacts/data-boundary.template.md)
names material a collaborator must not **see**.

This file names the two that were missing: what must not **leave**, and what a collaborator may
**run**.

Both became live the moment an AI collaborator had standing filesystem access, a network, and a
shell at the same time. None of the four original source projects had all three, which is why none
of them formalized this and why everything here is newer and weaker than the rest of the doctrine.

> **Status: single-attested and provisional (D-006).** One outside project supplied the read-access
> scar; the egress and tooling rules are policy-derived and single-authored. They are marked
> individually below. Per D-022 the corpus does not manufacture an incident to satisfy its own rule
> about incidents — a rule with only a ruling behind it says so.

---

## I. Egress

### B-1. Read access and egress are different boundaries, and one does not imply the other.

Permission to read something is not permission to transmit it, summarize it outward, or use it to
form a request to anything outside the machine. Every boundary declaration states both, separately.

- **Attested:** BK (external, non-corpus). A directory the collaborator had standing access to held
  a subpoenaed privileged case file and raw financial exports, and a signed BAA covering the
  engagement was in tension with a privileged file nobody had flagged. That scar produced the
  RED/GREEN/YELLOW read classification (D-023). *The egress half is single-authored: BK classified
  what could be opened, not what could be sent.*
- **The scar:** the read boundary was drawn and the transmission question was never asked, because
  a directory listing does not prompt you to ask it. Access is a property you notice; egress is a
  property you have to go looking for.
- **Off-software:** a clinician may read a chart and may not photograph it. A friend may hear
  something and may not repeat it. Nobody confuses these, and every one of them is a case where the
  right to receive and the right to pass on are separately granted.

### B-2. A query is derived data. Information leaves without being copied.

Anything constructed *from* restricted material — a search phrase, a request parameter, a question
asked of an outside service — carries information out of the boundary even when it contains no
copied string. Derived transmission is governed as transmission.

- **Attested:** none. **Policy-derived** (D-022), from an operator ruling on a live engagement:
  *"What we must not do is use specific information that could be considered private or sensitive
  within the queries we launch."*
- **Why it needs saying:** "How do mid-size regional practices handle intake backlogs" copies
  nothing and discloses the sector, the scale, and the problem in one line. Ten such queries are a
  profile. A boundary written in terms of *copying* — do not quote, do not paste, do not attach —
  reads as complete and does not cover this at all, which is what makes it worse than an obvious
  gap.
- **Off-software:** you can breach a confidence without repeating a word of it, by asking a
  question only someone who had been told would think to ask. The information is in the shape of
  the question.

### B-3. What goes out is recorded, or the boundary is only an intention.

Outbound requests are logged — what was asked, in what form, to what destination, when. The record
is the mechanism; the resolve to be careful is not.

- **Attested:** none directly. **Structurally inherited** from L-17: a rule that depends on
  judgement at every instance is a rule that fails at the instance where you are tired. The gate for
  a predictable recurrence is built *before* the first recurrence when the recurrence is
  predictable.
- **The scar:** this rule is written in advance of its incident, and that is stated plainly rather
  than dressed up. What it rests on is that B-2's failure is **silent and unrecoverable** — nothing
  announces that a query disclosed too much, no error is raised, and the disclosure cannot be
  withdrawn. A boundary whose violations are invisible needs a record, because the record is the
  only thing that makes a violation findable afterward.
- **Off-software:** a visitor log is not a statement that visitors are suspected. It is what makes
  "who was here in March" answerable at all.

### B-4. An unlisted destination is unclassified, not permitted.

The same rule the read boundary already uses. A channel nobody classified is a stop-and-ask, never
an inference from a similar channel.

- **Attested:** BK, by direct extension — the read boundary's rule that an unlisted item is
  unclassified rather than GREEN.
- **The scar:** BK's account is exact about the mechanism. Tiers get inferred by analogy from
  neighbours, and the inference is invisible because it feels like recognition rather than a
  decision.
- **Off-software:** an address you have not been told to send to is not an address you may send to
  because it looks like the others.

---

## II. Self-authored tooling

### B-5. A collaborator may build tools inside the boundary, and the tool inherits the boundary.

Writing and running your own instrument is legitimate and often the honest way to answer a
completeness question ([`../rituals/observation-pass.md`](../rituals/observation-pass.md)). But a
script is a reader with no memory of what it was allowed to read, and a writer with no sense of what
it was allowed to change. Authorization is declared once, in the same place as the data boundary,
and covers: what it may read, where it may write, and whether it may reach the network.

- **Attested:** none. **Single-authored.**
- **The scar:** none yet, honestly. What it rests on is the asymmetry — a human reading the wrong
  file knows they did; a script reading the wrong file leaves no trace that anyone was there.
- **Off-software:** giving someone a key to run an errand is a different act from letting them into
  the building, and the difference is whether you said which rooms.

### B-6. Your own tool's output is `INFERENCE` until the tool has been verified. Then it is `OBSERVATION`.

A number produced by an instrument you built and have not tested is a claim about your code, not a
claim about the world. It is typed accordingly ([`02-epistemics.md`](02-epistemics.md)) and promoted
only after the instrument has been broken on purpose and seen to notice
([`04-verification.md`](04-verification.md)).

- **Attested:** VOC by extension — L-11's house form is *"measured by me, never quoted."* This rule
  is the missing half: *measured by me, with an instrument I have not checked* is not a measurement
  either.
- **The scar:** this framework's own, earned building its vocabulary gate. First run, the gate
  reported **fourteen defects. Nine were not defects** — the pattern could not tell a genuine
  token list from a prose comparison of two of its members (*"the Operator / Coordinator
  boundary"*), so it read ordinary sentences as malformed lists. Every one of the nine was
  plausible, cited a real file and line, and would have been "fixed." **The instrument was
  measuring at the wrong altitude
  (L-12) and reporting confidently at the right format.** Two of the fourteen were real. Believing
  the tool at first run would have damaged five files to satisfy a bug.
- **Off-software:** a new scale that reads three kilos light is not a discovery about your weight.
  Weigh a known object first — and the reason nobody does is that the new scale's readout looks
  exactly as authoritative as the old one's.

### B-7. Cheap-to-reverse decides what runs unattended; the boundary decides what runs at all.

Within an authorized boundary, a collaborator may run its own tools without asking each time —
subject to the standing constraint that irreversible actions are not taken unattended
([`03-the-loop.md`](03-the-loop.md), [`06-delegation.md`](06-delegation.md)). Mutating source
material is not cheap to reverse, whatever the diff looks like.

- **Attested:** VOC (the cheap-to-reverse constraint on autonomous decisions), extended here to
  execution.
- **The scar:** VOC's original — a judgement call made while unattended is fine if reversing it is
  cheap and a liability if it is not. The extension is that **a script makes many judgement calls
  per second and none of them are individually visible**, so the reversibility question has to be
  asked once, about the script, before it runs.
- **Off-software:** the reason you do not reorganize someone else's filing cabinet while they are
  out is not that you would do it badly. It is that they cannot see what changed.

---

## What this file does not settle

- **Whether a research cache counts as egress on refresh.** Reading a stored source is not
  transmission; re-fetching it is. Where the line falls for an automatic refresh is not decided
  here — [`../rituals/external-research.md`](../rituals/external-research.md) requires the fetch be
  recorded, which at least makes the question answerable after the fact.
- **Aggregate disclosure.** B-2 governs one query. Ten individually-clean queries can still compose
  into a profile, and nothing here detects that. The query log makes it *reviewable*; it does not
  make it *caught*.
- **Any specific tool, sandbox, or permission mechanism.** Implementation, and excluded from
  doctrine for the same reason as every other toolchain question
  ([`01-laws.md`](01-laws.md), "What is deliberately not a law").
