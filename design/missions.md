---
record_class: living
precedence: 6
confidence: UNVERIFIED
owns:
  - mission-concept
  - run-scoped-steering
  - mission-stop-condition
verified_by: reference implementation in vociferous-next `.claude/night/` — 19 falsifier probes, 58/58 suite green, receipt `gates-proven.json` 2026-08-20T05:24Z. THE CITATION IS DEAD: see the note below.
last_verified: 2026-08-20
---

<!-- confidence: was CONFIRMED until 2026-08-28. Downgraded because the citation can no longer be
     re-derived, which is the one thing CONFIRMED requires. `gates-proven.json` is a SINGLE-SLOT
     file that the harness overwrites on every run: measured 2026-08-28T17:2xZ it holds
     {"when": "2026-08-28T03:40:19Z", "passed": 85, "failed": 0}, and a grep for "2026-08-20T05:24"
     across the whole of night-state/ returns nothing. The cited 19-probe / 58-of-58 result is not
     disputed — it is simply no longer readable, and the harness is gitignored so there is no
     history to recover it from. UNVERIFIED is the honest token: recorded, plausible, uncheckable.

     Reopening condition: a durable receipt. The current file pins `script_sha` to the harness it
     proved (79fb55f1…95b81c5 = run-night.sh), so once the harness is under version control a
     receipt can cite a commit SHA instead of a mutable path, and this can be re-earned. -->


# CONCEPT — `missions` — one paragraph of natural language that steers an entire unattended run

> **Status.** The concept is the operator's (2026-08-20). A working reference implementation exists
> and is proven by falsifier in `vociferous-next`; this brief generalises it for Astronomer. The
> Astronomer-side questions in §7 are **open** and are why this is a brief rather than a ruling.
> No `AST-D-` number is claimed here — ratification belongs to whoever picks this up.

## 1. The concept, in one paragraph

A **mission** is an optional natural-language string supplied when an unattended loop is started.
It steers the whole session. It replaces the loop's **work-selection rule** and nothing else, it is
visible in every artifact the run produces, and it introduces one additional stop condition: a run
may end early by reporting its mission achieved.

```
night.ps1 8 -Mission 'Close out M6 and M7. If both are blocked, say why and spend the rest of
                      the time on the standing brief.'
```

The operator's own framing, and it is the design constraint: *"a high-level steering wheel attached
to pretty much what is a Ferrari."* A loop that runs well but only ever in one direction is a
capability you cannot aim.

## 2. The problem it solves, measured

An unattended loop needs a selection rule that requires no judgement, because a rule requiring
judgement is a rule that drifts across a thousand fresh context windows. `vociferous-next` uses
*"the lowest-numbered open issue that is not parked."* It is a good rule: it favours the oldest
work, it is immune to cherry-picking, and it cannot be gamed.

**And it is orthogonal to every other ordering the project cares about.** Measured 2026-08-20 on
that project: milestone `M6` had three open issues, **none of them blocked** — and the loop could
not reach them, because seventeen lower-numbered unblocked issues stood ahead. Milestones advanced
only by coincidence. The operator's read, before any of this was measured: *"it feels like we're
not moving the needle at the correct location in the project."* They were right, and the mechanism
was a rule working exactly as written.

The wrong fix is to change the default. The operator rejected that explicitly, and correctly:
*"The lowest numbered open issue is a fine default."* A default that needs no judgement should not
acquire judgement to serve an occasional goal.

**The right fix is a run-scoped override.** The default stays; the operator aims the run when they
have a reason to. This is the general shape: **standing policy in the artifact, intent at the
invocation.**

## 3. The invariants

These are what make a mission a steering wheel rather than a waiver. Each one is a way the feature
could otherwise degrade the loop it is steering.

**M-1 — A mission overrides SELECTION and nothing else.** It changes *which* work is picked, never
*what counts as that work being done*. Verification, decomposition, criterion-first, filing
discipline, reporting, the hard prohibitions, and every law remain in force. Without this stated
explicitly and in the injected text, `finish M6 and M7` reads as licence to declare things
finished — which is the false-success class (`L-16`) arriving by the front door.

**M-2 — A run without a mission is byte-identical to one before the feature existed.** Not
"behaves the same" — byte-identical in the composed brief. This is what makes the feature safe to
ship into a loop that already works, and it is cheap to assert mechanically.

**M-3 — A mission that fails to arrive stops the run.** Everywhere else an unattended harness
should degrade to a backstop rather than refuse, because refusing is how you jam the gate shut.
**Steering is the exception.** A run that silently dropped its mission would spend the night on the
default rule while every artifact said it was steered, and the supervisor reading it the next
morning would diagnose a selection bug that does not exist. A steering input that goes missing
without saying so is worse than one that never existed.

**M-4 — A mission is not a promise.** If it turns out blocked, impossible, or already satisfied,
the run says so with evidence and **falls back to the standing rule for the remaining time**.
Reporting a mission unachievable is a good outcome; pretending to pursue it is not. This is the
operator's *"or failing that, exhaust its usage… or exhaust its time."*

**M-5 — The mission is stated in every artifact the run produces.** Console header, the pull
request body, the run report. A steered run that does not announce it is a supervision trap.

**M-6 — The mission's stop-word is subject to the stale-stop-word hazard and gets the same
treatment.** See §5.

## 4. The three outcomes

A mission is a goal, so it has three ends and not two:

| Outcome | The run writes | The loop |
|---|---|---|
| **Achieved** | `MISSION COMPLETE`, with evidence above it | **stops** — a seventh stop condition |
| **Blocked / impossible** | a plain statement of why, in the progress file | **continues** on the standing rule |
| **Neither yet** | ordinary progress | continues on the mission |

Stopping with time left is **correct** when the mission is achieved: the operator asked for the
mission, not for the hours. The counterpart is that the completion line must be held to the
standard of a closing keyword — it ends a run that was already paid for, so writing it on a hunch
throws away granted time.

`MISSION COMPLETE` is deliberately **not** a synonym for the existing `DONE`. `DONE` means *there
is nothing worth doing*; `MISSION COMPLETE` means *the thing I was sent to do is done*. Collapsing
them would make an achieved mission indistinguishable from an exhausted queue in the record.

## 5. The stale-stop-word hazard, and why the fix ships with the feature

A stop-word written into a persistent progress file **survives the run that wrote it**. On
2026-08-18 `vociferous-next` lost an entire night to exactly this: the afternoon run ended by
writing `DONE`, the next run read that line before iteration 1, and exited in one second with
`iterations=0 commits=0` while printing *"complete"*. A run that does nothing and reports success
is the defect class that project cares most about.

Introducing a second stop-word without clearing it would be **the second instance of a defect class
that already has a fix**, which is precisely what `L-17` exists to prevent. So the reference
implementation clears a stale `MISSION COMPLETE` at startup, loudly, on the same reasoning as
`DONE`: at startup no iteration of *this* run has had a chance to write one, so any present is
stale by definition.

**The generalisable rule: any new stop-word inherits the full stale-stop-word treatment at the
moment it is introduced, not after it costs something.**

## 6. The reference implementation, and what it measured

Built and proven in `vociferous-next` `.claude/night/` on 2026-08-20. Reported here as evidence
that the concept survives contact, not as the design Astronomer must adopt.

- **Injection.** The mission is prepended to the standing brief as a delimited `RUN MISSION` block
  carrying M-1, M-4 and the completion standard in its own words. The composed brief is assembled
  once per run.
- **Transport.** Three inputs, precedence file → environment → argv. **The file path is primary**,
  because the operator's missions arrive *dictated* and therefore carry apostrophes, em-dashes and
  quotation marks by default, and PowerShell 5.1 strips double quotes out of native-command
  arguments and mangles UTF-8. Only the *path* crosses the shell boundary.
- **A defect this found, worth generalising.** PowerShell 5.1's `-Encoding utf8` **always** writes a
  byte-order mark, so the first end-to-end run delivered the operator's instruction with an
  invisible `U+FEFF` glued to its first word. Stripped at the reader rather than the writer, so any
  producer is covered. *If your mission can be authored on Windows, assume a BOM.*

**Falsifier: 19 mission probes, and the suite is 58/58 green** (receipt `gates-proven.json`,
`2026-08-20T05:24Z`). Each control was seen to fire on its condition and to stay quiet otherwise —
including the byte-identical-without-a-mission assertion (M-2), the refusal on an unreadable
mission file (M-3), the stale-stop-word clearing (M-6), and the negative case that
`MISSION COMPLETE` must **not** stop a run that carries no mission.

**A defect found in prior work while doing this**, reported per the projects' own rule: the
existing calibration probe `GATE 5c` asserted a classification label that is only printed *after*
the weekly-ceiling check. When the operator's real seven-day usage rose above the sandbox's default
ceiling, the run correctly stopped on the ceiling, the label was never printed, and the probe
reported a disagreement that did not exist. **The probe was coupled to the operator's usage level
— the one variable it had no business depending on.** Fixed by pinning the sandbox ceiling above
any value the field can take.

## 7. Open for Astronomer — the questions this brief does NOT settle

1. **Where does a mission sit in precedence?** It is operator instruction at *run* scope, which is
   narrower than a DECISION and wider than a single edit. The nesting model in
   `design/distribution-and-scope.md` gives instance / client / global; a mission is a **fourth,
   ephemeral scope below all of them** that expires with the run. That needs ratifying, not
   assuming — particularly whether a mission may ever contradict an instance-scope artifact. My
   recommendation: **it may not.** M-1 already says selection only, and a mission that could
   override a decision is an unlogged decision.
2. **Does the concept belong to the loop, or to Astronomer generally?** Stated generally, a mission
   is *run-scoped intent supplied at invocation*, which applies to any bounded autonomous pass —
   an observation window, a triage pass, an audit sweep. If it generalises, it wants a ritual
   (`rituals/mission.md`) rather than a note inside one project's harness.
3. **Should a mission be recorded, and where?** It steered real work and is currently reconstructible
   only from a console buffer and a PR body. A run that produced landed commits under a mission has
   a provenance question: *why this work and not the default work?* Candidate: the run report gains
   a required mission section. My recommendation: **yes, in the report, not the ledger** — a mission
   is intent, and only its outcomes are decisions.
4. **Mission templates.** `finish milestone N` and `clear label X` will recur. Whether Astronomer
   ships named missions, or keeps the surface deliberately natural-language-only, is a real fork.
   My weak preference is **natural language only for now** — the value measured here came from the
   operator saying an unanticipated thing, and a template vocabulary is a way of anticipating.

## 8. What I did not verify

- **No full night has been run under a mission.** Everything above is proven at the harness level —
  injection, transport, stop conditions, falsifier — and **not** at the level of *does a steered
  model actually select different work all night*. That is the claim that matters most and it is
  untested. It is also unfalsifiable in a sandbox: it needs one real run.
- **The reference implementation was smoke-tested at `0` hours**, which exercises composition,
  transport, announcement and the closing summary, but starts **no iteration**. The
  mission-completion stop path was proven against a *stub* that writes the line, not a model that
  decides to.
- **`MISSION COMPLETE` is taken on the run's word.** The harness reports it as unverified and does
  not check it. Whether an unattended run can be trusted to judge its own mission achieved is
  exactly the question `#672` answered *no* to for issue closure — 5 of 20 claimed issues were not
  actually done. **Expect the same rate here**, and treat a completed mission as a claim to audit
  rather than a result. This is the largest known weakness in the design.
- **Nothing here has been tested outside `vociferous-next`**, so every claim about generality is
  reasoned from the design rather than measured across instances (`L-4`: scope is
  `ASSERTED-UNIVERSAL` until a second instance says otherwise).
