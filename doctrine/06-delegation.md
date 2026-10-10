---
record_class: living
precedence: 3
confidence: PROVISIONAL
owns:
  - non_delegable
  - role
  - ensemble_size
  - exchange_kind
  - ensemble-roles
  - group-routing
  - cross-group-exchange
  - operator-permit
  - workspace-sovereignty
verified_by: corpus gate (tools/check-corpus.py); the ensemble rests on VOC practice 2026-09-22 to 2026-10-10, ratified by the operator as D-064 to D-066
last_verified: 2026-10-10
---

<!-- confidence: was CONFIRMED until 2026-10-10. The ensemble half of this file (Roles through
     Holding the boundary) is ratified by the operator but rests on one project's practice, and the
     gate that holds the workspace boundary is not yet installed. PROVISIONAL, with the reopening
     condition named: install/maestro/gate.py installed, and the two-workspace waterfall in
     "Acceptance" observed once end to end. The older half (non-delegable work, fences, briefs, the
     report contract) is unchanged and was CONFIRMED on 2026-08-01. -->

# 06 — Delegation: the ensemble

Astronomer assumes you are working with collaborators — AI, human, or both — and that the
failures of delegation are structural rather than personal. A capable collaborator given an
ambiguous boundary will produce confident, well-executed work in the wrong place.

From D-064, delegation has a shape. One operator runs any number of **workspaces**. Each
workspace is a folder, and each has a **Maestro** presiding over it. The Maestro's own work is
fenced by a **Conductor** and done by **sections**. Workspaces ask each other questions only
Maestro to Maestro. The file a new session receives to found a workspace is
[`install/FOUNDING.md`](../install/FOUNDING.md). This file is the reasoning behind it.

---

## The workspace

**Every group is grounded in a folder, and its Maestro presides over that folder** (D-066). In the
operator's words: *"That will be their workspace. They will preside over it like a god."*

- **The folder is the territory.** Everything in it belongs to the workspace. The workspace's
  ledger is the top authority there, under the operator and the framework's laws. A workspace
  charter still cannot repeal a law ([`00-precedence.md`](00-precedence.md)).
- **No other workspace writes in it.** No session from another group edits a file there,
  whatever it's asked and whoever asks.
- **Nesting.** A session belongs to the deepest workspace whose folder contains it. That's the same
  walk-up rule as nested scopes (`design/distribution-and-scope.md` §6.1).
- **The name.** The folder carries the group's name where the operator manages it. Where the two
  differ, the registry records both.

---

## Roles

| Role | One per | Owns | Explicitly does not |
|---|---|---|---|
| **Operator** | person | The subject. Every judgement a collaborator cannot make. Rulings, permits, sequencing, and the non-delegable categories below | Being the courier between workspaces; writing their own briefs |
| **Maestro** | workspace | The operator's interface. The workspace ledger and decisions page, briefs for new sections, the roadmap, the registry row, the exchange log. At Solo size, the work itself | **Directing sections** once a Conductor exists. Relaying chatter. Pre-solving a brief. Talking to another workspace's Conductor or sections without a permit |
| **Conductor** | workspace, from Chamber up | Control: routing, sequencing, file ownership, disputes within delegation, the Board. Verifying returned work against sources, read-only | **Implementing.** Speaking to the operator unprompted. Speaking outside its workspace, ever |
| **Section** | goal | One fenced scope, end to end: root cause through to a recorded result. Its own baseline, verification, report and handoff | Touching another section's fence; messaging the Maestro; messaging outside its workspace |
| **Outlier** | goal | A thread the operator steers personally: strategy, brand, anything sensitive. It reports the operator's rulings to the Conductor, copying the Maestro, so they are recorded | Being steered by the Maestro or the Conductor |
| **Verifier** | claim | Re-deriving one claim from scratch and trying to break it. The **Lander**, a section that merges and verifies everyone else's work, is the standing Verifier at Orchestra size | Confirming by default |

Helpers, the subagents a session spawns, have no address of their own. They answer only to the
session that spawned them.

**The interface never controls (L-19).** The boundary that erodes fastest used to be operator and
coordinator, and VOC's operator had to state it directly:

> "You really aren't supposed to be doing any of the implementing here. The only thing you're
> supposed to be doing is producing documents and governance… You're just a coordinator for
> other external sessions."

The second boundary eroded in the same project two months later. One session acted as both the
operator's interface and the controller of eight others, so every session's traffic reached the
operator. The fix was a split, *"orchestrate instead of scramble"* (VOC, 2026-10-09). That split
is why the Coordinator is now two roles. The Maestro faces the operator and the Conductor faces
the work. Neither one implements.

**A brief must not be pre-solved.** A handoff is a *brief*, not a solution. Running a large
precursor investigation and handing over the answer defeats the purpose of an independent
section. It anchors the section on a conclusion it didn't derive and can't properly refute.

---

## Sizes

The same laws apply at every size. A size adds roles and artifacts and never relaxes a rule
(CHARTER invariant 6). Size is a third axis, alongside tier and scope. Tier is what's at stake,
scope is where the rules apply, and size is how many voices there are. Choosing a size is a
ledger decision.

| Size | Who | Pages | Choose it when |
|---|---|---|---|
| **Solo** | The Maestro alone, doing the work with helpers | None required | One stream of work at a time, and one context holds it |
| **Chamber** | A Conductor joins the Maestro, and up to a handful of sections do the work. The Conductor lands it | Decisions (Maestro), Board (Conductor) | Two streams touch the same files, or the operator catches themselves relaying between sessions |
| **Orchestra** | Chamber plus a Lander, outliers and one-way sessions | Console, Decisions, Session Briefs, Board, Roadmap | A live service, users or money. A bad merge is expensive |

**The forbidden arrangement:** a Maestro with sections and no Conductor. That's L-19's scar. A
Solo Maestro that needs a second session promotes to Chamber first, through
[`rituals/scale-up-gate.md`](../rituals/scale-up-gate.md). A workspace demotes only when its
landing queue is empty and verified.

**Concurrency counts writers, not sessions** (D-065, R3, which supersedes the old cap of three
sessions). A Conductor allows at most two sections to write to the same shared target at once.
Above two, a Lander serialises that target. Read-only sections, outliers and one-way sessions
don't count. The measurement behind the old cap stays as the scar: eleven conflict sets, **eight
of them the merge-cleanly-but-wrong kind**. Capacity is bought by removing collisions, not by
tolerating them. One small refactor that de-conflicts a shared surface buys a parallel lane
permanently.

---

## Naming

1. **Group names are unique** on the operator's machine. A name is an address. Two groups with
   one name make both Maestros ambiguous (measured 2026-10-10, removed by D-065 R5).
2. **`Maestro (<Group>)` and `Conductor (<Group>)`**, using the exact group name, so the operator
   can see at a glance who presides where, and a gate can parse it.
3. **Sections and outliers are named by goal**, never by date and never by persona. Bare names
   repeat across workspaces, so a Conductor addresses its sections **by session id** from the
   roster.
4. **A fork is not a Maestro.** A forked Maestro carries the original's memory and none of its
   standing. It messages nobody but the operator until the operator renames it and files it in a
   workspace. D-065 R6 is the first instance.
5. **Identifiers are local.** A bare `D-375` resolves to the local ledger. From another workspace
   it's `VOC-D-375`, using the registry slug ([`05-the-record.md`](05-the-record.md)).

---

## Routing

An edge not listed here is **unclassified, and unclassified is forbidden** (B-4 applied to
messages). A workspace's own `ORCHESTRATION.md` may remove edges but never add them. Only an
operator permit adds one, and only for a while.

| From → to | For |
|---|---|
| Operator → anyone | Anything |
| Maestro ↔ its Conductor | Rulings going down; batched escalations coming up |
| Maestro ↔ another workspace's Maestro | Exchanges only |
| Maestro → a new section of its own workspace | That section's first message |
| Conductor ↔ its sections and outliers | Everything inside the workspace, addressed by session id |
| Section ↔ section of the same workspace | A shared seam, copying the Conductor when the plan changes |
| Outlier → Conductor, copying the Maestro | Recording the operator's rulings |

**The Conductor escalates to the Maestro only on these triggers:**

- a decision needs the operator;
- something needs the operator's hands;
- a section should be retired or started (with its brief);
- an incident touches users, data or a live service;
- a commitment is at risk;
- a dispute goes beyond the delegation;
- a phase exit criterion is met.

It sends one batched message, not a stream.

**The Maestro speaks to the operator only when:**

- the operator spoke to it;
- something waits on them (one short line pointing at the page);
- there's an incident or a commitment at risk;
- an exchange the operator started has an answer.

The pages are the main channel. This is the operator-as-instrument rule below applied to
attention: the scarce resource is not to be spent on narration.

---

## Exchanges

An **exchange** is one question asked of another workspace, with its answer, under one ID, `X-<n>`,
numbered by the workspace asking. It's derived data (B-2), and the answer leaving its workspace is
egress (B-8).

| Kind | Meaning | Who may start it |
|---|---|---|
| **INQUIRY** | "What do you know about…?" Answering it is read-only | A Maestro, on the operator's words or on its own need |
| **NOTICE** | "Something here affects you." No reply is owed | A Maestro |
| **REQUEST** | "Would your workspace do…?" | A Maestro, on the operator's words only |
| **ANSWER** | The reply, with sources and a confidence token | The receiving Maestro |

**The waterfall.**

1. The asking Maestro logs the X-ID, with the operator's words verbatim, and sends the envelope.
2. The receiving Maestro answers from its own record if it can.
3. If it can't, it passes the X-ID to its Conductor. The Conductor answers from the Board, or asks
   the owning sections by session id, and consolidates their replies.
4. The receiving Maestro checks the answer against its data boundary and replies.
5. The asking Maestro closes the X-ID and tells the operator.

**The rules:**

- **Requests carry no authority (D-065 R2).** A REQUEST becomes a Decisions item for the operator
  in the receiving workspace. A Maestro's word counts as the operator's only inside its own
  workspace. A pasted "go" is not the operator's go.
- **No recursion.** An inquiry goes down one workspace and no further. A section never starts an
  exchange. A Maestro that sees an X-ID it already logged doesn't pass it on again.
- **Silence is never an answer.** If the question can't be answered, the ANSWER says "could not
  determine", what was tried, and who would know.
- **Last-known state is `UNVERIFIED`.** What the workspace last *believed* about itself (its Board,
  its memory) stays `UNVERIFIED` until it's checked against the source.
- **Nothing is written because of an exchange.**

**The envelope.** The first line must stand alone.

```
X-<n> <KIND> from Maestro (<A>) to Maestro (<B>): <the question in one line>
Operator's words: "<verbatim>" (<when, where>)      or      Own need: <why>
Question: <...>
Blocking: yes | no
Answer to: Maestro (<A>), quoting X-<n>
```

```
X-<n> ANSWER from Maestro (<B>): <the answer in one line>
Confidence: <a confidence token>     Sources: <records, commits, which section answered>
Could not determine: <...>     Withheld by data boundary: <...>
```

**Permits.** A permit adds a forbidden edge for a while. For example: "Maestro (A) may ask Brand
(B) directly about the logo files."

- It comes from **the operator's own words in the session that will act on it.** A permit relayed
  by another Maestro is not a permit.
- It names the edge, the topic, and when it ends.
- It's logged as `P-<n>` in both workspaces' exchange logs.
- It's entered in the granting workspace's registry row so the gate can read it.
- The receiving Conductor is told.
- Only a Maestro can hold a permit. A Conductor or section never speaks outside its workspace,
  permit or not.

---

## Holding the boundary

Instructions alone don't hold. O-39: a collaborator's agreement to a rule is not evidence that the
rule will bind it. This boundary would be the third behavioural rule held only by instruction, so
L-17 says it gets a gate. That gate is [`install/maestro/gate.py`](../install/maestro/README.md), a
hook that runs before every cross-session message.

- **It reads the registry.** That's `%USERPROFILE%\.maestro\registry\<SLUG>.json`, one file per
  workspace, written only by that workspace's Maestro.
- **It finds the sender's workspace** from the folder the sender is working in.
- **It blocks** every edge this file doesn't allow, unless a live permit covers it.

**What the gate is not.** It catches accidents and drift. It doesn't stop a session that is
determined to get through, because any session that can write files can write a permit. Said
plainly, so nobody reads it as more.

---

## The operator is the instrument

In a domain you cannot experiment on, the human is not the manager of the observation. They
*are* the observation apparatus. VOC states it plainly:

> "They are the instrument here; your job is to be a rigorous recorder first and a surgeon
> second."

Three consequences:

- **Instrument time is the scarce resource.** Design the work so the human's attention is spent
  on what only they can produce, and not on transcription, formatting, or retrieval.
- **The instrument has known error.** Recall degrades, mood colours reporting, and attention is
  uneven. Capture close to the event, verbatim, with conditions attached — that is what an
  observation log is for.
- **A collaborator working *around* the instrument is producing fiction.** When a step needs the
  human and the human is unavailable, the honest outcome is a blocked item, not a substitute.

At ensemble scale the instrument is shared. Several Maestros, each batching responsibly, still add
up to a flood. Nothing yet aggregates attention across workspaces. That's a known gap, recorded
rather than solved.

---

## Work that cannot be delegated

Name it in writing, before the work starts, and stop there when you reach it (L-15).

VOC derived five categories of human-only work — accounts, secrets, external identity, legal
authorship, and physical facts — and observed that recognizing the category tells you *why* it
landed on you, which is what makes it feel like structure instead of an obstacle.

Generalized below, **VOC's five collapse into the first four rows.** The fifth row is an Astronomer
addition and is not inherited from any source project; the note under the table says so. Read the
table as four attested categories plus one proposed one, not as VOC's list restated.

| Category | What it covers |
|---|---|
| **Identity & authority** | Anything requiring you to *be* you — accounts, signatures, consent, authorization |
| **Custody** | Secrets, credentials, keys, records only you may hold |
| **Acceptance** | Terms, liability, authorship — anything that attaches to a person |
| **Physical fact** | Anything requiring a body in a place: a measurement, a specimen, an appointment, a sensation |
| **Preference** | Anything whose correct answer is *what you want* — trade-offs between goods, not between right and wrong |

The last category is an Astronomer addition, not inherited from the source projects, and it is
the one that dominates outside software. *Single-authored — flagged for revision after first
real use.* A collaborator asked to optimize will silently choose an objective function, and it
will be a defensible one, and it will not be yours. Elicit the preference; do not infer it.

**At ensemble scale, two more rules sit on the categories above:**

- **Only the operator's own typed words authorise** an irreversible write to the operator's data or
  other people's data, and anything a safety check stopped. A relayed approval is not theirs.
- **Never route around a refusal**, even with the operator's approval. Hand the work to the
  operator's own session instead.

Both come from VOC (2026-10-01 and 2026-10-10).

**The honest stop is the point.** FR's evaluation directory is empty because its specification
declared the test-question set non-delegable and the project halted there rather than generating
its own questions and grading itself against them. That empty directory is the most honest
artifact in the entire corpus: automation ran to the human bottleneck and stopped, instead of
manufacturing a complete-looking result that measured nothing.

---

## Fences

Every parallel workstream declares **what it owns** and **what it must not touch**. Both lists,
explicitly, in the brief.

> "Every file below has exactly one owner. If your brief does not list a file, you do not own
> it." — VOC

**When you find a problem outside your fence: do not fix it.** Record it in the report, with a
citation, and keep going. This feels wasteful and is not — a fix landing outside its fence is
precisely the "merge-cleanly-but-wrong" class (L-10): two independently correct changes that
combine into a wrong result nothing flags.

**One writer per shared target.** One Lander, one owner per page, and one writer per registry
file. Five lanes once repaired citations, each correctly against its own parent and wrongly in
their union, and 103 green pull requests sat unmerged. A fence covers the files, the claim made
before touching them, and the single place they land.

---

## Briefs

A brief is a self-contained work order for someone who cannot ask you a question. Structure,
proven across seven parallel lanes with zero collisions:

1. Pointer to the **shared preamble** — the rules common to all work, included by reference and
   identical everywhere on purpose
2. **Why this scope exists**
3. **Verified current state**, with citations — then, separately and labelled, the `UNVERIFIED`
   hypotheses
4. **What makes this harder than it looks** — the traps, named
5. **Scope: IN** and **Scope: OUT**, numbered
6. **What you own** / **What another lane owns — do not touch**
7. **Acceptance criteria**

The shared preamble is the innovation. One file, referenced by every brief, holding the rules
that were learned the hard way — with the war story attached to each, so the rule is understood
and not merely obeyed. VOC's carries the note that its rules "are what made the last five-session
concurrent run merge with zero file conflicts, and every one of them was learned the hard way."

The brief hands over **symptoms, verified facts, and hypotheses** — not a solution. Its own
words: *"Your brief is a brief, not a solution."* At ensemble scale the brief also names the
section's Conductor and its workspace, and it says the section never messages outside that
workspace.

**Order, not estimates.** Steps are listed in dependency order and tagged as the operator's hands,
the operator's ruling, or agent work. Each phase begins with discovery. A brief carries no time
estimates (VOC, 2026-10-10: *"The only benefit is proper order."*).

---

## Decide, document, flag

When a section hits an ambiguity mid-flight and nobody above it can rule:

1. Make the call.
2. Implement it.
3. Document it prominently, under a heading that cannot be missed.
4. Flag it as *"judgement call — reverse this if wrong."*

With one hard constraint: **every such call must be cheap to reverse. If it is not cheap to
reverse, take the conservative option and say why.**

> "A stalled session is worse than a documented judgement call." — VOC

The same rule applies one level up. A Maestro may make small agreed wording or behaviour calls,
and approve a section's recommended fix, logged as **"Maestro's call"** where the operator can see
it. Money, schema, accounts, anything public, the operator's data, protected files, and anything
the operator ruled on personally always go up.

---

## The report contract

Returned work carries six sections. The last three are what separate a report from advocacy.

1. **What was done, and the cause established** — with citations, including where the brief's
   hypothesis was wrong
2. **What was verified, and how** — naming the grade achieved rather than collapsing everything
   into "verified." The grades are defined once, in
   [`04-verification.md`](04-verification.md), and are not restated here (L-12, L-14)
3. **Judgement calls made** — flagged for review
4. **Defects found inside your own work** — VOC's finding is that *every* session in its largest
   run found one this way, without exception. A report with none has almost certainly not looked.
5. **Found outside your fence** — untouched, cited
6. **What was not verified** — where *"owed by a human"* is an expected and acceptable outcome

Sections 4 and 6 are the ones that make a report evidence instead of a pitch. A report that
cannot say what it failed to check is not reporting; it is presenting.

**Never take a claimed result on trust.** A run once reported "MISSION COMPLETE" from a stale
stop-word with zero commits behind it. A reviewer that had died was announced as "review posted".
A Conductor checks each claim against its source before recording it.

---

## Acceptance

These are the conditions that would move this file back to `CONFIRMED`. They are written so they
can fail.

1. **The waterfall, observed once end to end.** Two workspaces on one machine. An INQUIRY from
   Maestro (A) that only a section in B can answer reaches the operator through Maestro (A) with
   its X-ID intact. No message in either workspace travels an edge the routing table doesn't list.
2. **The gate, observed failing before it is trusted.** It blocks Maestro (A) → Conductor (B)
   without a permit. It allows the edge with a live permit, and blocks it again once the permit
   ends. It blocks an unfiled fork. Each case is seen failing on a seeded defect first.
3. **A REQUEST changes nothing until the operator rules.** A REQUEST to B produces only a Decisions
   item in B. Nothing is written there before the operator's ruling.
