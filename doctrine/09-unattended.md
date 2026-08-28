---
record_class: living
precedence: 3
confidence: UNVERIFIED
owns:
  - unattended_loop
  - iteration_contract
  - stop_condition
  - context_tier
verified_by: extracted from one reference implementation with 52 recorded iterations; the doctrine itself has not been tested against a second
last_verified: 2026-08-28
---

# 09 — Unattended runs

Everything before this file assumes somebody is reading. [`03-the-loop.md`](03-the-loop.md) has
phases a person announces, [`06-delegation.md`](06-delegation.md) has briefs a person writes, and
[`04-verification.md`](04-verification.md) has results a person judges. This file is about what
happens when the loop runs for nine hours and nobody is there.

**It is derived, not invented.** One implementation has run this way since 2026-08-18, across
recorded iterations, and 403 of its 966 lines are comments that each record a dated failure. What
follows is those failures, stated without the repository they happened in.

---

## 1. The axiom: an iteration has amnesia

> *You are ONE ITERATION of an unattended loop. You have a fresh context window and no memory of any
> previous iteration. Everything you need is on disk or on the tracker. When you finish you exit, and
> the next iteration starts clean.*

Every rule below follows from that sentence, and a rule that does not follow from it belongs
somewhere else. A loop is not a long session; it is a series of short ones that share a filesystem.
Continuity lives on disk or it does not exist.

The consequence people get wrong: **you cannot instruct a future iteration.** You can only leave it
a file. An instruction addressed to "the next run" that is not written where the next run reads is
addressed to nobody.

## 2. Completed work is RECORD, not CONTEXT

The single most expensive lesson, and it is a context-window lesson before it is a discipline one.

The reference implementation fused its live state and its history into one file. That file grew
**13.7 KB per iteration** — roughly 780 KB over a twenty-hour run and about 1.8 MB over
forty-eight — and every iteration read all of it before doing any work. **The run degraded from the
tail backwards and did so silently**, because each iteration still looked healthy from inside.

The fix is a tier, not a trim:

| Tier | Holds | Read |
|---|---|---|
| 1 | Scope that spans runs | Once, at start. Never rewritten during a run |
| 2 | This run's mission | Once |
| 3 | Live state only — what is in flight now | In full, every iteration |
| 4 | The run record | Only to answer a specific question. **Never front to back** |

**Different lifetime, different reader.** Tier 3 is for the next iteration; tier 4 is for whoever
asks a question in three weeks. Mixing them is what produced the 13.7 KB.

Give tier 3 a numeric tripwire and an instruction for crossing it — *over this size means the
discipline has failed; say so, prune, and keep going.* The reference implementation's tripwire fired
and the loop applied the remedy itself, which is the only reason it is stated here as something that
works rather than something that sounds sensible.

## 3. Stop conditions are named, plural, and independent

A loop needs more than one way to stop, because each condition assumes an instrument that can fail.
The reference implementation carries **eight**, and the structure matters more than the numbers:

- a **proportional** budget ceiling — stop at a share of the period's allowance
- an **absolute** spend backstop — for when the usage figure becomes unreadable
- an **iteration cap** — a backstop, and it must be set far enough out that a run never sits on it
  as though it were the bound
- **consecutive failures** — a run of failures in a row is an outage, not a run
- a **backoff ceiling** on the doubling sleep between failures
- a **stop-word** the iteration can write when the work is done
- a **mission stop-word**, when the run was given a specific objective
- the **mission's own completion condition** — the only one an iteration can evaluate for itself

**A stop-word is an intra-run control and must not survive the run that wrote it.** A stale one from
a previous run stops the next run instantly, before it does anything, and the operator sees a clean
exit. Clear both at start, and say so in the log when you do.

## 4. The falsifier runs before the run does

An unattended loop is the worst place to discover that a control does not work, because nobody is
watching when it fails to fire. So: **the run refuses to start until every control has been observed
firing — on both halves.** Not "the gate is configured"; the gate was seen to block a bad input and
seen to pass a good one, in this configuration, today.

This is [`04-verification.md`](04-verification.md) applied to the machine that will run unwatched,
and it is the difference between a control and a hypothesis about a control. The reference
implementation proves twenty-two gates this way and writes a receipt naming the script hash it
proved, so a later reader can tell whether the receipt describes the harness that actually ran.

**A receipt in a single-slot file is a receipt you will lose.** The reference implementation
overwrites its own on every run, which retired a `CONFIRMED` claim elsewhere to `UNVERIFIED` when
the cited result became unreadable. Write receipts where history keeps them.

## 5. Selection: the default must need no judgement

An iteration with no memory cannot weigh priorities it cannot see. So the selection rule is an
ordered preference, and its default is chosen to be mechanical:

1. the item already in flight, if it has fewer than N attempts
2. otherwise the **lowest-numbered** unparked item
3. otherwise the housekeeping ladder

Lowest-number-first is deliberate: it favours the oldest work, it is immune to cherry-picking, and
**it needs no judgement to apply** — which is the property that matters when the thing applying it
has no context.

Two clauses bought by measured loss:

- **"Briefed well enough to execute" is not a filter.** A run once stopped three hours early
  reporting no pickable item, against dozens of unblocked ones, because few carried a "briefed"
  label. An unbriefed item is work to be decomposed, not work to skip.
- **Verify before dismissing.** Never conclude an item is stale, done or unexecutable from its
  description alone.

**A mission replaces rule 2 and nothing else.** Everything else still applies. A mission that
quietly suspends the fences is not a mission, it is a different loop.

## 6. Decomposition: the unit of work is the iteration

When the chosen item does not fit in one iteration, **the decomposition is that iteration's
deliverable** — split it until every leaf is executable in one unit, write the split down, and stop.
The next iteration picks a leaf.

Three fences hold that in place:

- **Ambiguity is resolved, not escalated.** Define the scope yourself, state the definition in your
  output, and defend it. *A rough working prototype that embodies a stated interpretation beats an
  abandoned task, and it gives the operator something concrete to disagree with, which a question
  does not.*
- **The criterion is pre-registered**, including for a decomposition iteration, where it is a
  criterion about the split. *"The suite passes" is not a criterion.*
- **Three bounds retries**: three attempts on one item then park it with the literal error; the same
  defect class three times means build the gate instead (L-17); three refused spellings of one
  command means the permission layer is the problem, not your syntax.

## 7. Filing is uncapped; PICKUP is capped

An autonomous loop that files its own work and then works on it will substitute its own agenda for
the tracker's, and will do so while looking productive. The asymmetry is the fix: **file as much as
you find, but pick up at most N self-filed items per run**, exempting only genuine emergencies.

This preserves decomposition — which must file freely to work at all — while bounding self-agenda
capture. It is the cheapest structural defence against a loop that spends a night on its own ideas.

## 8. A denial is a fact about the TOOL, never a fact about the WORLD

The sharpest rule in the source material, and the one most worth carrying:

> A denial licenses *"this tool is unavailable to me."* It NEVER licenses *"this capability does not
> exist"* or *"this class of work is impossible."* Those are claims about the world and need a
> measurement, not a refusal.

Before recording any capability as absent, probe it once through an already-allowed route; if that
is refused too, it is `UNRESOLVED` and **owed**, and you name both routes you tried.

**And the fence that keeps this from becoming permission-laundering, which must travel with it:**
clause two applies to establishing a **fact** — does this binary exist, is this path writable.
**Retrying a refused ACTION by another route is still forbidden.** *This action is refused* is the
guard working; *this spelling is refused* says nothing about the world. Extracting the first half
without the second produces a rule that reads as "route around your sandbox," which is the opposite
of what it is for.

## 9. The report is mandatory, and its negative sections are the valuable ones

Written to an exact path, kept current as you go rather than assembled at the end — **an iteration
killed by its timeout never reaches its exit step, so the work least likely to be recorded is the
work that ran longest.**

Three sections carry most of the value, and none of them is a summary of what happened:

- **what you could NOT determine** — the owed list, which is the only thing that keeps an unattended
  run honest about its own coverage
- **anti-duplication** — what you already tried, so the next iteration does not repeat it
- **the next three things you would do** — the queue handoff

A supervisor that greps for the report by exact name will report NO ARTIFACT for a naming slip,
which reads identically to a failed run. Pin the filename in the brief.

## 10. Checkpoint so the run is reviewable while it is still running

A twenty-commit wall at dawn is not reviewable, and holding it all to the end means a failure at
hour eight is discovered at hour nine. Snapshot at intervals into named, ordered segments, each
based on the last, and let the operator merge them bottom-up.

**Verify publication by asking the artifact, not the process.** A step that exits 0 has told you
about itself; querying the published thing tells you about the world. This is
[`02-epistemics.md`](02-epistemics.md)'s evidence ladder in the one place nobody is watching the
rungs.

---

## What this file does not know

`UNVERIFIED`, and the grade is the point. Every rule above is extracted from **one** implementation,
in **one** domain, run by **one** operator on **one** machine. Independent convergence is the only
validation signal this corpus accepts (`D-006`), and there is exactly one attestation here.

Three specific gaps: the numbers are deliberately absent because they are that implementation's, not
this doctrine's — a second implementation should derive its own ceilings and say what it derived them
from. Nothing here has been tested on a loop that is not a software repository, which is precisely
the generalisation `D-004` exists to force. And the reference implementation's own compliance was
never measured — the artifacts it produced are consistent with these rules being followed, which
proves that files were written and not that the rules were obeyed.
