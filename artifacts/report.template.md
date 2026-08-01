---
# NOTE: this block freezes with the record (L-13). Annotate by addendum;
# never edit a frozen header to make a gate pass.
record_class: frozen
precedence: 4
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <what this report concluded>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# `<lane id>` — `<scope name>` — RETURN

> **Doc class:** frozen. Submitted once. Not edited afterward — disputes, corrections, and
> follow-ups go in the decision ledger or in a new record, never back into this file. A report
> that can be revised after review is a report whose reviewers are reading a moving target.

**Required at:** **Full** — the return half of the brief; required wherever briefs are.

**Brief:** `<path/to/brief>` · **Executor:** `<who>` · **Window:** `<live UTC>` — `<live UTC>`
**Declared change size:** `<minimal | medium | large>` — `<held | re-classed upward to <x> at
<point>, because <why>>`

---

## Gates — measured by me, never quoted

| Metric | Baseline (measured `<UTC>`) | Final (measured `<UTC>`) | Δ | Gate | Result |
|---|---|---|---|---|---|
| `<name>` | `<value>` | `<value>` | `<±>` | `<pre-registered threshold>` | `<PASS/FAIL>` |
| `<name>` | `<value>` | `<value>` | `<±>` | `<threshold>` | `<PASS/FAIL>` |

**How each baseline was taken:** `<the method, in one line per metric — enough that someone could
reproduce the measurement and disagree with it>`

Every number in this table was measured by me at the times shown. **None of them is carried over
from the brief**, from a prior report, or from any document — those numbers are stale from the
moment they are typed, and one of them was stale by roughly a hundred the last time anyone
checked. If a figure in the brief disagrees with one here, the brief is wrong and this is the
correction; note it in section 1 so it gets fixed at the source rather than re-measured by the
next person.

`<If a baseline could not be taken — the state had already changed, the instrument was
unavailable — say so here explicitly. An absent baseline makes every delta below an estimate, and
that has to be visible in the table rather than discovered in the prose.>`

---

## 1. What was done, and the cause established

`<The narrative. Lead with the mechanism, not the task: "the count being displayed was a count of
sessions, labelled as a count of words" rather than "fixed the display." A reader six months from
now learns something from the first and nothing from the second.>`

**Cause (`CONFIRMED`):** `<mechanism>` — cited at `<address precise enough to land on>`
**How it was proven:** `<what was done, and — the load-bearing half — what would have made it come
out differently>`
**Blast radius:** `<what else touches this cause. Frequently the brief's scope was too small; say
so if it was.>`

### Where the brief was wrong

`<Mandatory section. The brief's UNVERIFIED hypotheses, each marked CONFIRMED or REFUTED, with
what refuted them. A refutation is a successful outcome and is reported as one — not apologized
for, and not omitted because the brief's author will read this.>`

- `<hypothesis from brief §3>` — **`REFUTED`** — `<what killed it, cited>`
- `<hypothesis from brief §3>` — **`CONFIRMED`** — `<what established it, cited>`
- `<fact from brief §3 that turned out not to be current>` — `<the correct value, measured>`

### Scope delivered

| Brief §5 IN | Status | Note |
|---|---|---|
| 1. `<item>` | `<complete / partial / blocked>` | `<…>` |
| 2. `<item>` | `<…>` | `<…>` |

---

## 2. What was verified, and how

Three grades, never collapsed into "verified". Collapsing them is the most common way a report
overstates itself while every individual sentence in it stays true.

| Claim | Grade | Method | What this could NOT have detected |
|---|---|---|---|
| `<claim>` | **proven — real conditions** | `<what was run, under what conditions>` | `<the failure mode this check is blind to>` |
| `<claim>` | **checked — proxy** | `<the stand-in, and why the real thing was not available>` | `<the gap between the proxy and the claim>` |
| `<claim>` | **reasoned — from source** | `<what was read and re-derived>` | `<everything a measurement would have caught>` |

**The last column is the one that carries the value.** Every check is blind to something; a report
that does not say what its checks were blind to has not verified the claim, it has surrounded it
with activity.

### Checks broken on purpose

For each check relied on: the condition it exists to catch was arranged, and the check was
confirmed to fire.

| Check | How it was broken | Fired? |
|---|---|---|
| `<check>` | `<the condition arranged>` | `<yes / NO — and what that revealed>` |

`<A "no" here is the most valuable row in the report. It means a check you were about to trust is
decorative, and you found out before relying on it rather than after.>`

---

## 3. Judgement calls made

Each one flagged for review, with its reversal cost. The cost column is what tells the reviewer
how urgently to look.

| # | Ambiguity | Call made | Cheap to reverse? | Reverse by |
|---|---|---|---|---|
| 1 | `<what was ambiguous, and why the brief did not settle it>` | `<what I decided>` | `<yes — <cost> / NO — took the conservative option instead>` | `<what to do to undo it>` |

**Judgement call — reverse this if wrong.** `<Restate the most consequential one in prose, under
this heading, so it cannot be skimmed past in a table.>`

`<Where a call was NOT cheap to reverse, the conservative option was taken and the reasoning is
recorded above. An irreversible call made autonomously is not a judgement call — it is a decision
taken on the operator's behalf without asking, and prominent documentation does not convert it
back.>`

---

## 4. Defects found inside my own work

`<Mandatory. In the source corpus's largest concurrent run, every session found a real defect
inside its own work by deliberately breaking its own checks — without exception. A report with
nothing here has almost certainly not looked.>`

| # | What was wrong | How I found it | Fixed? |
|---|---|---|---|
| 1 | `<the defect, causally>` | `<what surfaced it — and whether it was found on purpose or by luck>` | `<…>` |

`<If this section is genuinely empty, say so explicitly and describe what you did to look. "I
found none" is a claim; "I did not check" is a different claim; and the reader needs to know
which one this is.>`

---

## 5. Found outside my fence — untouched

Recorded and left alone, per the fence protocol. Each with a citation precise enough for the
owner to act without re-deriving it.

| # | What | Where (cited) | Owner | Severity | Why I did not touch it |
|---|---|---|---|---|---|
| 1 | `<the problem>` | `<address>` | `<lane / person>` | `<token>` | outside declared scope |

`<Nothing here was fixed, including anything that would have taken thirty seconds. A fix landing
outside its fence is the merge-cleanly-but-wrong class — two independently correct changes that
combine into a wrong result nothing flags.>`

---

## 6. What was not verified

| Claim / area | Why not | What would verify it | Owed to |
|---|---|---|---|
| `<…>` | `<instrument unavailable / out of scope / deliberately deferred>` | `<the check that would settle it>` | `<human / next lane / external>` |

**Owed to a human**, by category — identity and authority, custody, acceptance, physical fact, or
preference:

- `<item>` — **`<category>`** — `<what specifically is needed, and from whom>`

*"Owed by a human" is an expected and acceptable outcome, not a failure to finish.* Where the work
reached a boundary that required the operator, it stopped there rather than producing a plausible
substitute — and the substitute is the thing this section exists to prevent, because a
complete-looking result that measured nothing is indistinguishable from a real one until someone
acts on it.

---

## Open items handed back

- [ ] `<item>` — `<what it needs>` · *blocks:* `<what>`
- [ ] `<Q-n>` — `<decision owed to the operator>` · *options:* `<A / B>` · *my recommendation:*
  `<…>`, and `<whether I would be comfortable being overruled>`

## Ledger entries owed

`<Decisions taken during this work that belong in the project ledger, drafted here in ledger form
so they can be appended verbatim. Drafting them is the executor's job; appending them is the
coordinator's.>`

`[<live UTC>] D-<n>:` **`<decision>`** — `<why>` `caveat (owned):` `<…>`
