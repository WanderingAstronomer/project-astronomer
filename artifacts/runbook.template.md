---
record_class: living
precedence: 6
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <the procedure this runbook owns>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# RUNBOOK — `<situation name>`

> **Doc class:** living. Rewritten freely to match what actually works now. It states what to
> **do**, never the history of how the procedure evolved — that lives in the decision ledger. A
> runbook that accretes a change-log stops being readable at speed, and speed is the only reason
> it exists.

**Required at:** **Standard** — but gated on an event rather than a date: the second time you hit
the same friction, whatever tier you are running.

A runbook is written the **second** time you improvise the same response. Not the first — the
first time is an incident, and the response to it is a record. Not the fifth — by the fifth, the
improvisation has become folklore, three people are doing it three different ways, and the
disagreement is invisible because nobody has ever written it down side by side.

Every runbook is three parts and no more.

> **Runbook or ritual?** Both are triggered by the same event — the second time you hit a
> friction — and they collide on sight. The test is mechanical (D-017): **if the procedure cannot
> be written without naming your subject, it is a runbook and it belongs here, in your project.**
> If it can be written domain-neutrally, it is a *ritual*, it belongs to the framework, and one
> probably already exists — check `rituals/` before writing it, because a
> local copy of a framework procedure is a second home for a rule (L-14), and the two will drift.

---

## When

`<The trigger, stated so that someone who has never seen this situation can recognize it — and,
just as importantly, so that they can recognize when this is NOT it.>`

**This runbook applies when:**

- `<observable condition>`
- `<observable condition>`

**This runbook does NOT apply when:**

- `<the near-miss situation that looks identical from the outside>` — use `<other runbook>`
  instead
- `<the situation where following this would make things worse>`

The "does not apply" list is the half that gets skipped, and it is the half that prevents the
expensive failure. A runbook without one will be run against the situation that merely resembles
its trigger, confidently and by the book, which is worse than improvising — improvisation at
least proceeds carefully.

**Blast radius:** `<Friction | Conflagration>` — see the note at the bottom.

---

## Do

Numbered, ordered, and imperative. Each step states what to do and what you should see; a step
whose outcome is not observable cannot be confirmed, so the person running it will assume it
worked.

1. **`<Action.>`** → `<what you should see>`
   - If instead `<X>`: `<what that means, and where to go>`
2. **`<Action.>`** → `<what you should see>`
3. **STOP HERE IF `<condition>`.** `<Why — what this stop is protecting. A stop step with no
   reason attached gets skipped by whoever is in a hurry, which is everyone reading a runbook.>`
4. **`<Action.>`** → `<what you should see>`

**Preconditions checked at the top, scoped to this procedure only:**

- `<precondition>` — if missing: `<the remedy, named>`

Check what *this* procedure needs, not everything the project could ever need. And every failure
message names the remedy: "`<X>` is missing" is a diagnosis; "`<X>` is missing — do `<Y>`" is a
runbook entry that happens to fire at the right moment.

**No silent fallbacks.** If a precondition is unmet, this procedure stops, loudly. The
alternative is a run that completes on a degraded path and reports success — and a thing that is
broken and says so is safe, while a thing that is broken and reports success is not.

**Do not fix anything outside this procedure while running it.** Record it and leave it. A
runbook is executed under time pressure, which is exactly the condition under which an
opportunistic fix goes in unmeasured and untested (L-10).

---

## Record

What must exist when this is over. The procedure is not complete when the situation is resolved
— it is complete when the resolution is recorded, because the next person to hit this needs to
know it happened at all.

- [ ] **Observation log** — `<what to append: the trigger, the conditions, what was seen. Verbatim,
  live-stamped.>`
- [ ] **Decision ledger** — `<any judgement call made mid-procedure, with `caveat (owned):` if a
  shortcut was taken>`
- [ ] **Frozen record** — `<required for Conflagration; optional for Friction>`
- [ ] **This runbook** — `<update it if reality differed from the steps above. The moment a
  runbook is wrong and known to be wrong, every future run of it is a coin flip.>`
- [ ] **Occurrence count** — `<increment. See below.>`

**Occurrences:** `<n>` — `<dates>`

**On the third occurrence, stop writing fixes and build a gate** (L-17). The third instance of
the same failure is evidence about the *mechanism*, not about the instance — and fixing it
instance by instance leaves the mechanism intact. The source corpus's summary of what that costs
is four words long: *every hand-fix drifted back.* The recurrence stopped only once a gate
existed. Candidate gates: a **ratchet** (a floor that may rise and never fall), a **refusal to
start** when preconditions are unmet, an **idempotency check** (run it twice; the second run must
do nothing), a **posture check** (run the verification again under the restricted conditions that
actually apply, not the permissive ones you work under), or an **incident-derived check** whose
description *is* this runbook's trigger.

And the rule that protects every one of them: **the guard is intentional — fix the cause, do not
disable it.** A gate switched off to unblock work has not been consulted; it has been overruled,
and that is a decision that belongs in the ledger with a name on it.

---

## Blast radius

**Blast radius asks *how far does this reach*. Severity asks *how much does this matter*.** They
are orthogonal axes and they no longer share a word: `stop` / `major` / `minor` / `question` is
the per-item severity scale and belongs in your charter; Friction / Conflagration is blast radius
and belongs here (D-018). A `minor` item is a Conflagration if six decisions rest on it.

The rename is itself an instance of L-17 and worth understanding rather than just obeying. The
first version of this section kept both scales under the word "severity" and *warned the reader
not to confuse them* — which leaves the mechanism intact and re-teaches the trap to every future
reader, forever, one reader at a time. Renaming the axis removes the collision instead of
documenting it. When the same confusion recurs, do not write a better warning. Take the ambiguity
away.

| | **Friction** | **Conflagration** |
|---|---|---|
| **Reach** | Recoverable in-session. Contained to the work in front of you. | Ripples across the project. Other work, other people, or the record itself is affected. |
| **Who needs to know** | You, and the log | The operator, now — before you continue |
| **Record required** | Observation log entry | Observation log **and** a frozen record **and** a ledger entry |
| **Stop the work?** | No. Note it, continue, report at the end | **Yes.** Stop and surface it. A Conflagration handled quietly is a Conflagration handled twice |
| **Typical shape** | The step did not do what the runbook said; you found the way round | The situation invalidated observations elsewhere, changed a shared surface, or made a frozen record misleading |

The distinction earns its keep at the moment of judgement, when the honest answer is *"probably
just friction"* — and the follow-up question that resolves it is not *how bad is this* but **does
anything outside this session now need to be re-checked because of it.** If the answer is yes, it
is a Conflagration regardless of how small it felt, because the cost is not in the incident. It is
in every conclusion downstream that was drawn while it was true and nobody knew.

---

## Worked example

*From the volunteer stream-monitoring study used across these templates. Note that this procedure
**cannot be written without naming the subject** — sites, tube, field sheets — which is the
mechanical test that makes it a runbook rather than a ritual (D-017).*

### RUNBOOK — A returned field sheet has a turbidity value that is blank, illegible, or outside the plausible band

**When.** A volunteer's field sheet reaches transcription and the turbidity cell cannot be taken
at face value.

Applies when: the cell is blank; the digit is ambiguous; or the value is outside the band recorded
for that site in `PROC-001`. Does **not** apply when the value is merely *surprising* — a genuine
storm spike is exactly the observation this study exists to capture, and treating it as a
transcription defect is how a real signal gets quietly smoothed away. Surprising-but-legible goes
straight into the log with the conditions attached, and it is triage's problem, not this
procedure's.

**Blast radius:** Friction while the sheet is still in hand. **Conflagration** once the value has
been transcribed into `DATA-001`, because a wrong reading in the series is invisible from that
point onward and every seasonal comparison downstream is drawing on it.

**Do.**

1. **Do not infer the value.** → The cell stays blank. This is the whole procedure in one step,
   and it is the one that gets skipped, because the surrounding readings usually make the missing
   one look obvious. `E-002`'s contract is explicit: an unreadable field becomes a blank cell,
   **never an inferred value** — an inferred reading is indistinguishable from a measured one
   once it is in the spreadsheet, and it will be counted, averaged, and cited as an observation.
2. **Photograph the sheet before annotating it.** → The paper sheet is the verbatim record
   (`DATA-003`); once you write on it, the original state is gone.
3. **Ask the volunteer, if the sheet was returned within seven days.** → Recall past a week is
   not evidence, and a remembered reading recorded as a measured one is the same defect as step 1
   wearing a friendlier face. If they cannot recall it clearly, it stays blank.
4. **STOP HERE IF the value is out-of-band rather than illegible.** Do not correct it, do not
   drop it. An out-of-band value is either a real event or an instrument fault, and this procedure
   cannot tell which — hand it to triage as an observation with `UNRESOLVED` confidence. Deciding
   between those two here, under time pressure, at a desk, is guessing with a clipboard.
5. **Record the gap as a gap in `DATA-001`.** → A blank cell, not a zero and not an interpolation.
   A tracking system that silently fills a missing day is worse than one that shows the hole; the
   hole is the signal.

**Record.**

- [ ] Observation log: the sheet, the site, the date, what was unreadable, and what was done
- [ ] `DATA-001`: blank cell, flagged
- [ ] Ledger: only if a judgement call was made — e.g. accepting a volunteer's recall inside the
  seven-day window. Include `caveat (owned):` naming it, because that value is now weaker than
  everything around it and nothing in the spreadsheet will say so
- [ ] Occurrence count

**Occurrences:** 4 — 2026-03-14, 2026-04-02, 2026-04-29, 2026-05-11

**Past the third occurrence — gate, not a fix.** Four illegible turbidity cells in nine weeks is
not four careless volunteers; it is evidence about the *mechanism*, and the mechanism is that
`INST-004` reads in 5-unit steps while the field sheet offers a free-text box, which invites a
precision the instrument cannot produce and a handwriting problem that need not exist. The gate is
to reprint the sheet with the tube's actual steps as tick-boxes, so an out-of-band or
between-steps value becomes **unrecordable** rather than merely discouraged. That is one change to
the environment, and it retires this runbook — which is the outcome a recurring runbook should be
aiming at. `<Raise as a triage item; the reprint is a decision with a cost and it belongs to the
operator.>`
