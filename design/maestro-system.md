---
record_class: living
precedence: 6
confidence: UNVERIFIED
owns: []
verified_by: superseded by doctrine/06-delegation.md (D-064, 2026-10-10)
last_verified: 2026-10-10
---

> **SUPERSEDED 2026-10-10 by [`doctrine/06-delegation.md`](../doctrine/06-delegation.md) (D-064 to
> D-066).** The operator ratified this brief into doctrine an hour after it was written. Do not work
> from this file. It is kept because it records what was proposed before ratification, and where the
> doctrine departs from it. The departures: groups became folders by ruling (D-066), concurrency now
> counts writers (D-065 R3), the kit dissolved into [`install/FOUNDING.md`](../install/FOUNDING.md),
> and cross-workspace IDs use the ledger's existing `VOC-D-4` form, not `VOC:D375`.

# BRIEF — `maestro-system` — one operator, many groups, a Maestro over each

> **Status: design brief. The routing gate, the registry and the exchange log are proposed and
> not built.** Roles, pages, the handoff procedure and the escalation triggers were practised in
> one project for three weeks. That's one attestation, so all of it is `practice`, not law (D-043).
> No `AST-D-` number is claimed here. Ratification belongs to whoever picks this up.
>
> The concept is the operator's (2026-10-10). The operator's words: in every sidebar group "each
> group entertains a Maestro system. The Maestro, a conductor, and then the subservient sections
> and the occasional outlier." Maestros of different groups "message each other and then
> waterfall down to find answers or discover information through their conductors and then
> through their conductors into their sessions." And the boundary: "a maestro of one group should
> never talk directly to the conductor or sessions of another group unless the operator
> explicitly permits it."
>
> A ready-to-paste kit (first messages, templates and a registry row) lives beside this file in
> `maestro-system-kit/` (since dissolved into `install/FOUNDING.md`).

---

## 1. Read this first

1. **The interface never controls.** The defining failure was one session acting as both the
   operator's interface and the controller of the other sessions. Every message from every
   session leaked through to the operator. The fix was a split, and that split is the system.
   Once a group runs more than one session, it has a Conductor.
2. **Across groups, only Maestros talk.** Everything a group knows is reachable from another
   group, but only through the two Maestros, and only as a question and an answer. Nothing
   travels across as an instruction.
3. **Size is chosen, not grown into.** Three sizes: **Solo**, **Chamber** and **Orchestra** (§4).
   Choosing one is a ledger decision, the same as choosing a tier, and the two are separate axes.
4. **Instructions won't hold the boundary by themselves.** O-39: agreeing to a rule isn't evidence
   that the rule binds. So the cross-group boundary is meant to be held by a gate (§8), and until
   that gate exists the boundary is a habit. Say so wherever it matters.

## 2. Why this scope exists

Astronomer's delegation doctrine has one coordinator layer and one operator ([`06-delegation.md`](../doctrine/06-delegation.md)).
That held for a single project with two or three executors. It doesn't hold once:

- **one project grows past what one coordinator can handle.** In Vociferous Next, by 2026-10-09,
  that meant 6 to 9 live sessions, a lander, cloud sessions that can't reply, and a live
  production service;
- **one operator runs many projects at once.** The operator's sidebar on 2026-10-10 had 15 groups:
  a product company, client work, coursework, health, personal writing;
- **the operator wants to ask one project something another project knows** without becoming the
  courier.

Three things are missing: a split between interface and controller, a size ladder, and a governed
channel between groups. Each one has a scar (§10).

## 3. Roles

| Role | One per | Owns | Talks to | Never |
|---|---|---|---|---|
| **Operator** | person | Every judgement only they can make. Rulings, hands-on actions, permits. | Anyone in any group | Being the courier between groups |
| **Maestro** | group | The operator's interface: the decision ledger, briefs for new sections, the roadmap, the group's registry row, the exchange log | The operator; its own Conductor; other groups' Maestros | Building. Relaying chatter. Narrating landings. Talking to another group's Conductor or sections without a permit |
| **Conductor** | group (Chamber and up) | Control: routing, sequencing, file ownership, disputes within delegation, the Board, verifying claimed results | Its own Maestro; its own sections and outliers | Talking to the operator unprompted. Talking outside its group, ever |
| **Section** | goal | One fenced goal, end to end, and its own handoff | Its Conductor; other sections of its group where they share a seam (copying the Conductor) | Talking to the Maestro. Talking outside its group |
| **Outlier** | goal | A strategy or sensitive thread the operator steers personally | The operator directly. It sends its rulings to the Conductor, copying the Maestro, so they're recorded | Being steered by the Maestro or the Conductor |

Two helper roles exist inside a session and carry no address of their own:

- **Helpers** are subagents a session spawns. They report only to the session that spawned them.
- **The Lander** (Orchestra only) is a section whose goal is to merge, verify and deploy everyone
  else's work. It exists because one writer per shared target is the only arrangement that has
  survived (§10, scar 6).

**Mapping to Astronomer's roles:**

- Maestro is the Coordinator's operator-facing half: briefs, ledgers and sign-off.
- Conductor is the Coordinator's executor-facing half: fences, sequencing and read-only verification.
- Section is the Executor.
- The Lander, and any adversarial reviewer, is the Verifier.
- Outlier is an Executor whose coordinator is the Operator.

Neither half may implement. That rule is unchanged.

## 4. Sizes

The same laws apply at every size. A size adds roles and artifacts and never relaxes a rule.
Names are chosen to avoid colliding with the tier called Full (D-035 reasoning).

| Size | Who | Pages | Pick it when |
|---|---|---|---|
| **Solo** | Maestro alone. It does the work itself, with helpers. | None required. A decisions section in its own notes. | One stream of work at a time; one session's context holds it |
| **Chamber** | Maestro, Conductor, and up to three sections. The Conductor lands work. | Decisions (Maestro), Board (Conductor) | Two or more streams at once that touch the same files, or the operator catches themselves relaying between sessions |
| **Orchestra** | Maestro, Conductor, a Lander, many sections, outliers, and one-way sessions | Console, Decisions, Session Briefs, Board, Roadmap | A live service, users or money; more sections than one Conductor can fence by memory; anything where a bad merge is expensive |

**The forbidden size:** a Maestro with sections and no Conductor. That's exactly the defect §1.1
describes. A Solo Maestro that needs a second session promotes to Chamber first.

**Changing size** follows [`rituals/scale-up-gate.md`](../rituals/scale-up-gate.md). The ledger
entry names the size, the reason, and what would justify reversing it. Going down a size also
needs an entry. When an Orchestra drops to Chamber, the Lander's queue must be empty and verified
first.

**Concurrency is UNRESOLVED.** Doctrine says three concurrent executors is the honest maximum and
two is the default ([`06-delegation.md`](../doctrine/06-delegation.md)). Vociferous Next ran five
to nine at Orchestra size, held together by one Lander and file ownership, and still recorded
collisions (§10, scars 6 and 7). Proposal, unratified: the cap counts sections that **write to the
same shared tree**, per Conductor. Read-only sections, outliers and one-way sessions don't count.

## 5. Naming

1. **Group names are unique** on the operator's machine. The name is the address, so two groups
   with the same name make both Maestros ambiguous. Measured 2026-10-10: the sidebar held two
   groups named "Vociferous Next", one with 59 sessions and one with none.
2. **`Maestro (<Group>)` and `Conductor (<Group>)`**, with the exact sidebar group name in the
   parentheses. That way the operator can see who presides where, and any tool or gate can parse
   the group from the title.
3. **Sections and outliers are named by goal** ("Landing & Review", "Brand"), never by date and
   never by a persona. The group is already visible in the sidebar. Because bare names can repeat
   across groups, the Conductor addresses its sections **by session id from its roster**, never
   by bare name.
4. **A fork is not a Maestro.** Forking a Maestro session yields a copy named "Maestro (fork)",
   carrying the original's memory and none of its standing. Until the operator renames the fork
   and files it in a group, it sends nothing to anyone but the operator. Two sessions believing
   they are Maestro (G) is the cross-session version of two lanes claiming one ID (O-38).
5. **IDs are local to their group; references across groups carry a prefix.** Inside Vociferous a
   decision is `D375`. From another group it's `VOC:D375`, where the prefix is the group's
   registry slug. This is the [`00-precedence.md`](../doctrine/00-precedence.md) namespacing rule
   (a bare ID resolves to the local ledger), applied to groups.

## 6. Routing

### 6.1 The edge table

An edge not listed here is **unclassified, and unclassified is forbidden** (B-4 applied to
messages). A group's own `ORCHESTRATION.md` may remove edges. It may never add one. Only an
operator permit (§7.4) adds an edge, and only for a while.

| From → to | Allowed for |
|---|---|
| Operator → anyone | Anything |
| Maestro (G) ↔ Conductor (G) | Rulings going down; batched escalations coming up |
| Maestro (G) ↔ Maestro (H) | Exchanges (§7) only |
| Maestro (G) → a new section of G | Delivering its first message, when the operator starts it that way |
| Conductor (G) ↔ section or outlier of G | Everything inside the group |
| Section of G ↔ section of G | A shared seam, copying Conductor (G) when the plan changes |
| Outlier of G → Conductor (G), copying Maestro (G) | Recording the operator's rulings |
| Helper → its own session | Everything; helpers have no other address |

### 6.2 When the Conductor escalates to the Maestro

It escalates only when:

- a decision needs the operator;
- something needs the operator's hands;
- a section finished and should be retired, or a new one should start (with its brief);
- an incident touches users, data or a live service;
- a commitment is at risk;
- a dispute goes beyond its delegation;
- a phase exit criterion is met.

Everything else stays below the Maestro. When it does escalate, it sends one batched message, not
a stream.

### 6.3 When the Maestro speaks to the operator

The Maestro speaks only when:

- the operator spoke to it;
- something is waiting on them, sent as one short line pointing at the page;
- there's an incident or a commitment at risk;
- an exchange the operator started has an answer.

The pages are the main channel, and chat is kept to a minimum.

## 7. Exchanges: the waterfall between groups

### 7.1 What an exchange is

An **exchange** is one question asked of another group and its answer, under one ID, `X-<n>`,
numbered by the asking group. It's derived data (B-2). The answer leaving a group is egress, so
the answering group's data boundary decides what may leave (B-1, B-3).

| Kind | Meaning | Who may start it |
|---|---|---|
| **INQUIRY** | "What do you know about …?" Answering it is read-only in the answering group. | A Maestro, on the operator's words or on its own need |
| **NOTICE** | "Something here affects you." No reply is owed. | A Maestro |
| **REQUEST** | "Would your group do …?" | A Maestro, on the operator's words only |
| **ANSWER** | The reply to an inquiry or request, with sources and confidence | The receiving Maestro |

**A REQUEST doesn't transfer authority.** The receiving Maestro puts it on its own group's
Decisions page as an item for the operator, unless the operator's own words in the receiving
session already cover it. A Maestro's word counts as the operator's only inside its own group, and
only to the extent the operator granted that. It never carries across. Same rule as relayed
approval: a pasted "go" is not the operator's go.

### 7.2 The waterfall

```
Operator ─ "ask Vociferous whether the tester form went out" ─▶ Maestro (Health)
  Maestro (Health): log X-4 with the operator's words verbatim; look up Maestro (Vociferous Next) in the registry
  ─ INQUIRY X-4 ─▶ Maestro (Vociferous Next)
       1. answers from its own record if it can (pages, ledger, memory), citing the source, or
       2. asks Conductor (Vociferous Next), quoting X-4
            Conductor answers from the Board, or asks the owning section(s) by session id
            sections answer the Conductor, and the Conductor consolidates
       3. checks the answer against its data boundary before it leaves
  ◀─ ANSWER X-4 ─ Maestro (Vociferous Next)
  Maestro (Health): close X-4 in its log; tell the operator in one line, or on its page
```

**Rules for the waterfall:**

- **It doesn't recurse.** An inquiry goes down at most to the sections of the group asked. A
  section never starts an exchange. A Maestro that receives an X-ID already present in its log
  doesn't pass it on again, so loops die at the second hop.
- **Silence is never an answer.** An inquiry that can't be answered gets an ANSWER that says
  "could not determine", with what was tried and who would know.
- **The answer reports its own confidence**, using the confidence vocabulary in
  [`02-epistemics.md`](../doctrine/02-epistemics.md). Whatever the receiving group last *believed*
  about its own state is `UNVERIFIED` until it's checked against the source (a commit, the live
  service, the file).
- **Nothing is written because of an exchange.** No ledger entry, no code, no data changes in the
  answering group, unless a REQUEST went through that group's own operator ruling.
- **An offline peer** can be woken by session id when the operator started the exchange. If it
  can't be reached, the asking Maestro tells the operator. It doesn't guess the answer.

### 7.3 The envelope

The first line has to stand alone, because a receiver's operator may only see the first line.

```
X-4 INQUIRY from Maestro (Health) to Maestro (Vociferous Next): did the tester issue form go out?
Operator's words: "ask Vociferous whether the tester form went out" (2026-10-10, in Maestro (Health))
Question: has the tester issue form been sent to testers, and to whom?
Blocking: no
Answer to: Maestro (Health), quoting X-4
```

```
X-4 ANSWER from Maestro (Vociferous Next): not sent yet; the form is built, sending is the operator's hands.
Answer: <the answer>
Confidence: <a confidence token, doctrine/02-epistemics.md>
Sources: <pages, file paths, commit hashes, which section answered>
Could not determine: <or "nothing">
Withheld by data boundary: <what was left out, or "nothing">
```

### 7.4 Operator permits

A **permit** adds a forbidden edge for a while. For example: "Maestro (Health) may ask Brand
(Vociferous Next) directly about the logo files."

- **It comes from the operator's own words in the session that will act on it.** A permit relayed
  by another Maestro isn't a permit.
- **It names the edge, the topic, and when it ends.** It ends either when an X-ID closes or on a
  stated condition, never "until further notice".
- **It's logged in both groups' exchange logs**, with the operator's words quoted.
- **The receiving group's Conductor is told**, so it knows the traffic is legitimate.

## 8. Holding the boundary: the gate (NOT BUILT)

Instructions are the third instance here, so the gate is owed (L-17, O-64). The proposed gate
works like this:

- **A pre-send hook** on every cross-session message tool reads the registry (§9) and the sender's
  session id from the hook input. It looks up both ends of the edge and blocks any edge the §6.1
  table doesn't list, unless a live permit covers it.
- **A session that isn't in the registry** can message only its own operator. That covers forks
  and stray sessions.
- **The second line is the receiver.** A Conductor or section that receives a message whose sender
  isn't on its group's roster answers "not routed here: send through Maestro (<G>)" and tells its
  Conductor. On its own this second line is only an instruction, which is exactly why the gate
  comes first.

**What the gate is and isn't.** It catches accidents and drift. It doesn't catch a session
determined to get past it, because a session that can write files can write a permit. Written
plainly so nobody reads it as more.

## 9. The registry

The registry is one file per group, in one machine-level directory. Each Maestro writes only its
own group's file (one writer per file; O-38 is what happens with one shared file).

```
group: Vociferous Next          slug: VOC          sidebar id: cg-5144f485-…
size: Orchestra                 home: C:\Users\drew\Documents\DevSlop\vociferous\handoffs
maestro:   Maestro (Vociferous Next)    local_3719027b-…
conductor: Conductor (Vociferous Next)  local_f7154940-…
roster:    <section title, session id, role> for every live section and outlier
pages:     <name and URL for each page>
exchange log: <path>
data boundary: <path, or "none declared">
```

The registry is the list of approved destinations (B-4). A group that isn't in it can't be asked
or told anything.

## 10. Standing rules, each with its scar

| # | Rule | Scar |
|---|---|---|
| 1 | The interface never controls | One session was both Maestro and controller, so every session's traffic reached the operator. The fix: the 2026-10-09 three-layer split, "orchestrate instead of scramble" |
| 2 | Route, don't solve | A coordinator solved dictated items itself and missed what the operator saw at once. Rule from 2026-09-28: "You are not supposed to solve any of these problems" |
| 3 | Escalate only on the §6.2 triggers, batched | Eighteen decisions were sent to the operator in one afternoon (2026-10-01): "Y'all have a lot of questions for me." That gave rise to "Maestro's call" for small agreed questions, logged and visible |
| 4 | Never take a claimed result on trust | A run reported "MISSION COMPLETE" off a stale stop-word that had zero commits behind it; a dead reviewer was announced as "review posted"; two branches named in one queue left one of them unlanded. Check against the source: is the commit an ancestor of main, is it live, does the file exist |
| 5 | Liveness isn't progress | A batching coordinator never ran ("heartbeat: never") while four lanes kept heartbeating, so the board read as alive. Sessions blocked on permission prompts sat for 6h44m |
| 6 | One writer per shared target | Five lanes repaired citations, each correctly against its own parent and wrongly in their union. 103 green PRs went unmerged. The answer: one lander, one owner per page, one writer per registry file |
| 7 | Fences by file, claimed before touching | Two lanes restructured one component; a night loop and an attended session rewrote the same fences without either seeing the other's claim |
| 8 | Announce, wait, then write | A gating notice was sent in the same batch as the write it gated. The notice was refused, but 63 of the operator's records had already changed |
| 9 | Only the operator's own words authorize writes to the operator's or other people's data, and anything a safety check blocked | Relayed approvals were refused as laundering (2026-10-01) |
| 10 | Never route around a refusal, even with the operator's approval | A safety check stopped a security test as it began. The work moved to the operator's own session (2026-10-10) |
| 11 | Sandbox and live never share a store | A sandbox cleanup deleted 12 of the operator's real recordings through a shared default path |
| 12 | Leave a file, not an instruction | "You cannot instruct a future iteration. You can only leave it a file." A wrong flag copied into seven missions ran every lane uncapped |
| 13 | One-way sessions reply through an artifact | Cloud sessions can't message back, so their questions go at the top of the report they push |
| 14 | Handoffs argue for the operator's rulings | Rulings that weren't defended in the handoff were re-asked by successors |
| 15 | Order, not estimates | Rejected by the operator 2026-10-10: "it doesn't benefit us to put time estimates on anything. The only benefit is proper order." Phases begin with discovery; every step is tagged operator's hands, operator's ruling, or agent |

## 11. What makes this harder than it looks

- **The operator can still be flooded.** Several Maestros, each batching responsibly, add up to a
  flood. Nothing aggregates across groups yet. A cross-group Console is a candidate. It's not
  designed, and building one is a choice to make, not a default.
- **Names are mutable.** Titles can be changed by the operator, by the app (forks), or by a session
  renaming itself. That's why the registry keys on session id and keeps the title only as a label.
- **Session state isn't the truth.** A Board, a roster or a Maestro's memory is what the group last
  believed. After a reboot, peers show offline, and their last-reported state can be hours stale.
  Recovery reads the source first.
- **Groups aren't directories.** Astronomer's nested scopes are found by walking up the filesystem
  (`distribution-and-scope.md` §6.1). Several sidebar groups can share one folder, and one group
  can span several. So a group is a communication boundary, not a scope. It needs its own home
  folder declared in the registry.
- **Capabilities differ by surface.** Desktop sessions, Remote Control sessions and cloud sessions
  can each receive messages, but not all of them can reply. The edge table describes what's
  allowed. The registry has to record what each session can actually do.

## 12. Fit with Astronomer

| Astronomer piece | What this would add or change |
|---|---|
| [`06-delegation.md`](../doctrine/06-delegation.md) | Split the Coordinator into an interface half and a controller half; add the Outlier; add the §6.1 edge table as the delegation topology. The four role names stay; Maestro and Conductor are the names of the two halves, not new roles |
| [`07-boundaries.md`](../doctrine/07-boundaries.md) | An exchange answer leaving a group is egress (B-1 to B-4). The registry is the destination list |
| [`05-the-record.md`](../doctrine/05-the-record.md) | New prefix `X-<n>` for exchanges (free as of 2026-10-10). Cross-group references take a group prefix |
| [`tiers/README.md`](../tiers/README.md) | Size becomes a third axis beside tier and scope. Orchestra probably implies Full tier; Solo is compatible with any tier |
| `artifacts/` | New templates: exchange log, registry row, Board (it's not a triage board: it tracks sessions, not findings), Console |
| `rituals/` | New: a cross-group inquiry, granting a permit, promoting a size (extends scale-up-gate), forking or compacting a Maestro |
| `install/` or a fourth plugin | The Claude Code reference implementation: the routing hook, the registry tool, and Maestro, Conductor and handoff skills. Doctrine stays domain-neutral (D-002); everything that names the sidebar lives here |

**Conflicts to resolve before ratifying:**

- The concurrency cap (§4).
- The CLI bar (D-057). A registry *checker* is a measuring instrument and is allowed; a registry
  *writer* might count as scaffolding.
- O-66: skills barely fire in headless sessions, so a Maestro skill can't be the only thing that
  carries the rules. The gate and the registry have to.

## 13. Scope

**IN**

1. The five roles and the edge table.
2. The three sizes, and the rules for moving between them.
3. Naming.
4. Exchanges, the envelope and permits.
5. The registry format.
6. The gate's specification.
7. The kit.

**OUT**

1. Building the gate or the registry tool.
2. Changing doctrine files.
3. A cross-group Console.
4. Groups belonging to more than one operator. That's out for the same reason multi-operator trees
   are out of scope in `distribution-and-scope.md`.
5. Cloud-to-cloud exchanges.

## 14. Acceptance criteria (written so they can fail)

1. **The waterfall works end to end without a forbidden edge.** Two Chamber groups on one machine:
   an INQUIRY from Maestro (A) that only a section in B can answer comes back to the operator
   through Maestro (A) with its X-ID intact. Both groups' transcripts show no message on an edge
   the §6.1 table doesn't list. One forbidden message fails the criterion.
2. **The gate blocks what it should, and only that.**
   - Without a permit, it blocks Maestro (A) messaging Conductor (B).
   - With a live permit, it allows the message.
   - Once the permit's X-ID closes, it blocks it again.
   - It blocks every send from an unrenamed fork except to the operator.
   - It's observed failing on each case before it's trusted (the census rule).
3. **A REQUEST changes nothing until the operator rules.** A REQUEST sent to group B produces only a
   Decisions item in B. Nothing is written in B until the operator rules there.
4. **The registry tool catches the measured defects.** It reports the duplicate group name measured
   on 2026-10-10, and a Maestro title whose parentheses don't match its sidebar group.
5. **The Conductor's escalations stay on trigger.** Over one week at Chamber size, every message
   from the Conductor to the Maestro maps to a §6.2 trigger. One that doesn't map fails.

## 15. What I could not determine

- **Whether a pre-tool hook sees cross-session message tools** in every session surface (desktop,
  Remote Control, cloud). Desktop is likely. The others are unknown.
- **Whether a hook can read a session's sidebar group.** I found no evidence that it can. Hence the
  registry, which a hook can read.
- **Whether a session can be denied messaging to specific targets** by permission rules alone,
  rather than by a hook. The rules I know of match tools, not message recipients.
- **How the app titles a fork in every case.** One instance was observed ("Maestro (fork)",
  2026-10-10).
- **Whether one operator-level Console** across every group helps or just moves the flood (§11).

## Return

The proposer hands this back to the operator for three rulings:

1. **Adopt into Astronomer?** Doctrine changes plus a reference implementation, or a standalone kit
   that cites Astronomer.
2. **The REQUEST policy** in §7.1, and the concurrency cap in §4.
3. **The registry location**, and whether to build the gate first. Recommended: yes, the gate
   before a second group goes beyond Solo.
