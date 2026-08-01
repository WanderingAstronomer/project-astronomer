---
# NOTE: this block freezes with the record (L-13). Annotate by addendum;
# never edit a frozen header to make a gate pass.
record_class: frozen
precedence: 4
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <what this run established>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# `<run / pass / intervention name>` — `<YYYY-MM-DD>`

> **POINT-IN-TIME RECORD: DO NOT EDIT TO REFLECT LATER TRUTH — ANNOTATE IF SUPERSEDED.**
>
> **Doc class:** frozen. This file records what was done and what came back, as understood on
> `<date>`. If something here is now known to be wrong, it stays, and an addendum below says so.
> Where this and a living document disagree, the living one wins on fact and this one stands on
> the historical record — **and neither file changes.**

`<Filename convention: date-suffixed — `<name>-<YYYY-MM-DD>.md`. The date in the filename is what
makes a frozen record obviously frozen at a glance in a directory listing, before anyone opens
it.>`

**Required at:** **Standard** — from the point where a run's numbers have to survive the next
revision of your understanding.

---

## Run metadata

| | |
|---|---|
| **What was run** | `<the intervention, pass, or procedure, in one line>` |
| **Why now** | `<the trigger — the finding, decision, or observation that caused this>` |
| **Started / ended** | `<live UTC>` — `<live UTC>` |
| **Operator / executor** | `<who, and which role>` |
| **Subject / population** | `<what it was run on, and how much of it>` |
| **Variables changed** | `<enumerate. If more than one, see the note below>` |
| **Held constant** | `<what was deliberately not changed, and how that was ensured>` |
| **Instruments** | `<what measured it, and what each instrument cannot detect>` |
| **Conditions** | `<the seeing — environment, state, anything else in play>` |
| **Governing decisions** | `<D-n, D-n>` |
| **Pre-registered gate** | `<quoted exactly as written before the run — see below>` |
| **Inputs frozen at** | `<pointer to the exact state of the inputs, precise enough to reproduce>` |

**On `Variables changed`:** one variable, or the result is unattributable (L-10). If more than one
changed, say so here, explicitly, and accept in writing that this run cannot tell them apart.
Two independently correct changes made together can combine into a wrong result that nothing
flags — the source corpus found eleven conflict sets in one analysis and eight of them were
exactly that class, each of which merged cleanly and passed every check. A run that bundled its
variables is not worthless; it is just answering a coarser question than it appears to, and the
place to say so is here rather than in the reader's head six months later.

---

## Metrics against the pre-registered gate

The gate is quoted **as it was written before the observation**, not as it reads in hindsight
(L-9). If it was amended between pre-registration and this run, both versions appear, with the
decision that amended it.

| Metric | Gate (pre-registered) | Measured | Result |
|---|---|---|---|
| `<name>` | `<threshold, with the condition it was calibrated under>` | `<value>` | `<PASS / FAIL>` |
| `<name>` | `<threshold>` | `<value>` | `<PASS / FAIL>` |
| `<degeneracy guard>` | `<the check that the output is not trivially uniform — e.g. no single class exceeds <n>%>` | `<value>` | `<PASS / FAIL>` |

**Baseline, measured here — never quoted** (L-11):

| Metric | Baseline (measured by me, `<UTC>`) | Final (measured by me, `<UTC>`) | Δ |
|---|---|---|---|
| `<name>` | `<value>` | `<value>` | `<±>` |

Numbers written in any document — including the brief that commissioned this run, and including
this framework — are stale from the moment they are typed. Take the baseline yourself before you
change anything, and record when you took it.

**Was the gate itself sound?** `<Answer this explicitly.>` A gate calibrated on a friendlier
condition than the one actually measured under will fail everything, and the failure will look
like a subject problem rather than an instrument problem. If that happened, say so here and
record the demotion in the ledger — *the gate was the artifact, not the subject.*

**Degeneracy check.** `<The distribution of the output across categories.>` This is the live
readout on your own falsifier, which is the point of having written one. Too uniform and the
process is not discriminating; too concentrated and it is not firing.

---

## What happened

`<Narrative. The mechanism, not the task list — "the chart was fed one quantity and told to
report another" rather than "fixed the chart." A reader six months from now learns something from
the first and nothing from the second.>`

## Failure modes observed

Everything that went wrong, including the things that were recovered from and the things that
turned out not to matter. A run record that lists only the failures that survived to the end is a
record of the writing, not the run.

| # | Failure mode | Where it appeared | Detected by | Recovered? | Would recur if |
|---|---|---|---|---|---|
| 1 | `<what went wrong, causally>` | `<where>` | `<what caught it — and whether it caught it on purpose>` | `<yes/no/partially>` | `<the condition that would bring it back>` |

**`Detected by` is the column that pays.** A failure caught by a check that was designed to catch
it is a working system. A failure caught by luck, by a human glancing at raw output, or after the
fact is an **undetected class** that happened to surface — and the honest entry says so, because
the next instance will not be lucky. Where a failure was caught by accident, the follow-up is a
gate, not a fix (L-17).

## Caveats (owned, not hidden)

State the weaknesses yourself, in your own words, in this section, under this heading. Name the
control that was not run, the comparison skipped, the sample that was convenient rather than
representative, the thing you decided not to check and why. **An owned caveat is a durable asset;
an unstated one is a landmine with your fingerprints on it** — and the difference between a
record that survives scrutiny and one that is destroyed by it is almost never the quality of the
work. It is whether the weaknesses were found by the author or by the reader.

- `<caveat>` — `<who chose to accept it, and what was traded for it>`
- `<caveat>` — `<…>`
- `<the control run that was not performed>` — `<why not, and by whose call>`

## What was not verified

- `<claim>` — `<at what altitude it was checked, and what that check could not have detected>`
- `<claim>` — *owed to a human* — `<which non-delegable category: identity, custody, acceptance,
  physical fact, or preference>`

Distinguish *proven in the real conditions* from *checked through a proxy* from *reasoned from
the source*. Collapsing all three into "verified" is the most common way a record overstates
itself while every individual sentence in it stays true.

---

## Human audit set

The sample a human must look at directly, chosen and listed **here**, so that "someone checked
it" becomes a specific, refusable claim rather than an impression.

| # | Item | Why this one | Checked? | By | Result |
|---|---|---|---|---|---|
| 1 | `<item ref>` | random draw, seed `<n>` | `<[ ]>` | | |
| 2 | `<item ref>` | the extreme value | `<[ ]>` | | |
| 3 | `<item ref>` | the boundary case | `<[ ]>` | | |
| 4 | `<item ref>` | the one that looked wrong | `<[ ]>` | | |

Compose the set from four kinds of item, because each catches something the others cannot: a
**random draw** (representativeness), an **extreme** (whether the tails are handled), a
**boundary** (whether the rules apply where they are hardest), and **whatever looked off**
(confident wrongness, which no aggregate will ever show you). Aggregates hide exactly the failure
that matters most — output that is uniformly plausible and uniformly wrong — and the only known
defense is a human reading a few raw records unaggregated.

**An unchecked audit set is an open item, not a formality.** If nobody has looked, the boxes stay
empty and the record says so.

---

## Addenda

> An addendum notes what has since become true. It **does not re-run or revise** anything above
> it. Nothing above this line is ever edited.

### `[<YYYY-MM-DD>]` — `<label>`

`<What changed. Which conclusions above are superseded, and by what, named explicitly.>`

---

## Worked example — metadata and caveats block

*From a small seed-propagation trial. Domain is illustrative only.*

| | |
|---|---|
| **What was run** | Bottom-heat propagation of `<variety>` at 21°C against the unheated bench |
| **Why now** | O-12 recorded three consecutive sowings germinating below half, all on the cold bench |
| **Started / ended** | 2026-02-14T09:10Z — 2026-02-28T09:00Z |
| **Subject / population** | 6 trays × 40 cells = 240 cells; 3 trays heated, 3 unheated |
| **Variables changed** | **One:** bottom heat. Same seed lot, same compost batch, same sowing depth, same watering schedule, same bench position rotated daily |
| **Instruments** | Soil probe `<model>`, ±1°C, read at 09:00 daily. Germination counted by eye — cannot distinguish a seed that never germinated from one that germinated and collapsed before the count |
| **Pre-registered gate** | "≥ 80% germination at day 14 in the heated trays, counted at 09:00" — set 2026-02-13, before sowing |

| Metric | Gate | Measured | Result |
|---|---|---|---|
| Germination, heated, day 14 | ≥ 80% | 62% (74/120) | **FAIL** |
| Germination, unheated, day 14 | *(no gate — control)* | 41% (49/120) | — |

**Was the gate sound?** Partly not. The 80% figure was taken from the seed packet, which states a
laboratory germination rate — measured on damp paper under controlled humidity, which is not the
condition being measured here and is not reachable in compost on a windowsill. The heated trays
outperformed the control by 21 points, which is the comparison the trial was actually designed to
make, while failing a threshold imported from a friendlier condition. The gate is demoted to a
monitored metric; the heated-versus-unheated contrast becomes the criterion. Recorded as `<D-n>`.

### Caveats (owned, not hidden)

- Trays were rotated daily to control for bench position, but the heated trays necessarily sat on
  the mat and the unheated ones did not — so "position" and "heat" are only partly separable, and
  a light gradient across the bench would show up here as a heat effect. Not controlled for.
  Accepted knowingly to keep the trial to one season.
- The count cannot distinguish non-germination from post-germination collapse. Damping-off was
  visible in tray 4 and is recorded as a failure mode, but the *number* in the table above absorbs
  both mechanisms into one figure. Any use of that 62% carries this.
- No blind counting. The same person set up the trial and counted the results, knowing which trays
  were heated. The counting was mechanical enough that this is probably minor — *probably* is
  doing real work in that sentence, and the cleanest fix, having someone else count unlabelled
  trays, was available and was not taken because it was inconvenient. My call.
