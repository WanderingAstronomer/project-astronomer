---
record_class: living
precedence: 6
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <collaborator-capability-roster>
  - <fallback-ladder>
  - <collaborator-known-errors>
  - <decision-rights-reserved-list>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# CAPABILITY INVENTORY — `<collaborator>` — `<YYYY-MM-DD>`

> **Doc class:** living. Rewritten whenever the environment changes, and **re-dated every time**. A
> capability inventory with no date is a claim about an environment that may no longer exist.

**Required at:** **Lite, conditional** — gated on a condition, not a tier: required whenever
something other than the operator is doing the observing. A solo human project does not need one; a
project where an AI collaborator reads the sources, runs the searches, and drafts the findings needs
it before the first window opens.

**Doctrine:** `doctrine/08-instruments.md` holds the reasoning and the rules (K-1…K-7) and owns the
default **role** set. The obligation is L-18. The procedure that produces this file is
`rituals/capability-interrogation.md`. Its human twin is
`artifacts/operator-profile.template.md` — write both in the same sitting.

Every instrument in this framework declares what it cannot detect. The observation log requires it
per window; the frozen record requires it per run. **This artifact applies the same rule to the
collaborator and to the environment it acts through**, which were otherwise the only instruments in
the corpus exempt from it — and the ones doing most of the observing.

## Why this exists

`doctrine/06-delegation.md` says *"the operator is the instrument"* and that the instrument has known
error. There was no parallel statement for a collaborator, so its limits were discovered per-task, by
hitting them, usually mid-window.

The framework's ritual for stale measurements (`rituals/instrument-drift.md`) is entirely
retrospective — every entry point begins *after* you have relied on a bad number. This is the
forward half: state the limits **before** the work, where they cost a paragraph, rather than after,
where they cost the pass.

> **Status: single-attested and provisional (D-006).** This artifact shipped as a structural argument
> with no incident behind it. It has one now. In a single day, a collaborator with standing
> filesystem access, a network and a shell surveyed a platform it was about to build on: it reported
> broad capability read from documentation, and a second pass instructed only to **re-measure rather
> than re-read** overturned thirty-two claims — the largest class being documented capability that
> installation did not have. The same survey found the project's own always-loaded governing
> instructions were not in version control, so every fresh session elsewhere inherited none of them,
> and had not for over a thousand commits. One project is a practice, not a law (CHARTER invariant
> 4) — but this is no longer a guess about what is worth declaring.

## What to state

### 1. Environment, as measured — not as assumed

`<Operating system, shell, working directory, what is installed and at what version.>`

**Measured now, by me, never quoted** (L-11, L-18) — including from this template. A capability list
copied from a previous session is exactly the stale number L-11 is about, and it will be wrong in
the direction of claiming too much.

### 2. Roles, providers, and the two columns that are not the same question

The role set comes from `doctrine/08-instruments.md`; strike what does not apply and add what is
missing, recording either in the ledger. **Capability and permission are separate facts** (K-1) and a
single column collapses "present and forbidden" into "absent," which have different remedies.

| Role | Provider here | Capability — *can it?* | Permission — *may I?* | How established |
|---|---|---|---|---|
| `<work-item store>` | `<what actually provides it>` | `<measured>` | `<operator's answer>` | `<the command run, or the question asked>` |
| `<relation graph>` | | | | |
| `<working set>` | | | | |
| `<change record>` | | | | |
| `<verification gate>` | | | | |
| `<durable prose>` | | | | |
| `<corpus retrieval>` | | | | |
| `<session inheritance>` | | | | |

Two failure states to name explicitly rather than average away:

- **Permitted and absent** — full rights over something that does not exist on this installation.
- **Present and forbidden** — the mechanism is right there and the credential cannot reach it.

**Corpus retrieval carries a third column the others do not** (K-7). Beside capability and
permission, record **what share of the index is foreign to this project's own thinking** — material
imported from a vendor, a client, or another team — as a measured fraction with the date it was
taken. An index is the one instrument here where a successful acquisition can make every unrelated
question harder to answer, and the share is the only number that sees it coming.

| | |
|---|---|
| Items in the index, total | `<measured>` |
| Of those, foreign to this project | `<measured>` · `<%>` · as of `<YYYY-MM-DD>` |
| Largest single foreign corpus | `<name>` · `<%>` |
| Pre-registered ceiling | `<the share at which this project stops importing>` — see `rituals/corpus-intake.md` |

**Never name a vendor in the Role column** (K-2). The role is durable; the provider is a fact about
today's environment and belongs in the second column, where it can change without amending the
project.

### 3. The fallback ladder

For each role: preferred provider first, then what is used when it is unavailable, ending at a floor
you are willing to state out loud (K-3).

| Role | Preferred | If unavailable | Floor — stated, not discovered |
|---|---|---|---|
| `<role>` | `<>` | `<>` | `<"not recorded anywhere, and I know it">` |

**The floor is a legitimate rung.** What is forbidden is arriving at it without having written it
down: an undeclared floor is indistinguishable from a working mechanism until the moment it is
needed, which is the L-16 defect at the level of a plan.

### 4. What can be read, and in what formats

| Format | Can read | Notes |
|---|---|---|
| `<plain text / markdown>` | `<yes>` | |
| `<PDF, text layer>` | `<yes / no / with what tool>` | |
| `<PDF, scanned images>` | `<no without OCR — and is OCR available?>` | the silent-failure case; see the source manifest |
| `<office documents, spreadsheets>` | `<>` | hidden sheets, tracked changes, comments? |
| `<images, audio, video>` | `<>` | |
| `<archives, mailbox exports>` | `<>` | attachments extracted, or dropped? |

### 5. What can be executed, and where it may write

`<Whether the collaborator may write and run its own tooling; what it may read; which paths it may
write to; whether it may reach the network>` — this is the authorization required by B-5,
`doctrine/07-boundaries.md`, and it belongs here or in the data boundary, once, not in both.

### 6. Network reach

`<What outbound channels exist at all, before the question of what is permitted.>` Capability and
permission are different facts and both are needed: a channel that exists but is forbidden is a
boundary item; a channel that is permitted but does not exist is a plan that will fail quietly.

### 7. Decision rights

`<What this collaborator settles alone; what it settles and logs; what it stops for.>`

The non-delegable categories in `doctrine/06-delegation.md` are the floor and are not restated here
(L-14). Above that floor, decision rights are a capability like any other and are set **once**, at
setup, by the operator (K-5) — then held. A right recorded and then re-asked every session is not a
right; it is a habit of asking, and it moves the cost onto the one instrument that cannot be
parallelised.

Bound by the standing constraint that irreversible actions are not taken unattended, and that a
judgement call made alone must be cheap to reverse (B-7).

### 8. Known error — the load-bearing section

`<Where this collaborator is systematically wrong, in a direction you can name.>` Not modesty
boilerplate. A usable entry names the bias and its direction, so it can be subtracted:

> **Completeness questions are under-reported.** Asked "where does X appear," careful reading
> returns a list that looks finished and is not. Measured once on this corpus: four readers, told
> exactly what to look for, found seven of ten sites — a ~30% undercount, in the direction that
> feels complete. Use a mechanical search as the instrument and reading as the interpreter for any
> question of the form "everywhere" (`rituals/observation-pass.md`).

> **Its own tooling reads as authoritative.** Output from a script the collaborator wrote is
> `INFERENCE` until the script has been broken on purpose and seen to notice (B-6). First run of
> this project's own vocabulary gate reported fourteen defects; nine were artifacts of the gate.

> **Capability is over-claimed from the general case.** Told that a configuration value was
> adjustable, one collaborator reported that repointing a subsystem needed no code. The value served
> two unrelated subsystems, so the change would have silently broken the one that was working. Read
> correctly in general, never measured at the seam — which is the direction K-6 names.

### 9. Instrument debt — what cannot be measured here at all

`<Things this environment cannot determine, listed so they are owed rather than guessed.>` The
model is a source project that shipped with a written ledger of what was owed to real devices,
rather than letting a weaker verification stand in silently (L-12). An honest wall beats an
optimistic one (L-16).

Include here anything a **read-only probe could not settle**. Where a capability can only be proven
by writing, record the exact write that would prove it and leave it owed — an unproven capability
that is honestly labelled is worth more than a proven one bought with a mutation nobody intended.

## Forbidden

- Copying this file forward from a previous session without re-measuring. That is the stale-number
  failure L-11 exists for, committed against yourself.
- Writing "no known limitations" in section 8. That is not an inventory, it is an absence of one —
  and it is the single most likely sentence in this whole artifact to be false.
- Discovering a capability limit mid-window and continuing without recording it. It is an
  observation (L-7); log it, and amend this file when the window closes.
- Confusing capability with permission. What the collaborator *can* reach and what it *may* reach
  are different questions with different owners; permission lives in the data boundary.
- Recording a role with no ladder. A role whose fallback is unwritten is a plan that stops at its
  first refusal with nothing to do next (K-3).
- Trusting your own declaration about yourself. It is written by the instrument being declared, and
  the bias runs toward claiming too much (K-6) — a self-asserted limit is `INFERENCE` until something
  has failed in the way it predicts.

## Lifecycle

Written before the first observation window, as part of `rituals/capability-interrogation.md`, which
runs inside `rituals/starting-a-project.md`. Rewritten and re-dated whenever the environment changes
— a new tool, a lost one, a different machine, a granted or revoked permission (K-4). Never frozen:
a stale capability inventory is a live risk, not a historical record. When a limit turns out to be
wrong, that correction goes in the decision ledger, because it means work done under the old
assumption may need re-checking.
