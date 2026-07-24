# TRIAGE — `<project name>` — `<window / pass name>`

> **Doc class:** disposable. This document is permitted to be blunt, opinionated, addressed to
> whoever owns the work, and revised violently. That is its function. Giving yourself a
> sanctioned place to write badly is what keeps the permanent documents clean — without one, the
> mess ends up in the specification.
>
> **But:** if this board starts being cited outside the pass that produced it, it has stopped
> being disposable. Promote it to frozen, deliberately. *If you would be upset to lose it, it is
> not disposable, whatever the directory says.*

**Required at:** **Standard** — from the point where there are more findings than you can hold in
your head, and someone will act on them later.

**Entry condition:** the observation window is closed and the log carries an explicit
`INTAKE CLOSED` marker. Triage does not begin while intake is open — if it did, the first item
triaged during intake would look exactly like an item triaged after it, and the boundary would
stop existing without anyone noticing.

**Source:** `<observation log, window <name>, O-1–O-n>`

---

## Buckets — sorted by epistemic state, not by severity

Severity tells you what you *want* to be true. Epistemic state tells you what an item actually
needs next. Sorting by severity produces a list of things you would like fixed; sorting by
epistemic state produces a list of things that can move.

| Bucket | State | What it needs |
|---|---|---|
| **A** | Cause proven, with a citation | nothing — ready to act on |
| **B** | Direction clear, cause not formally proven | mechanical execution |
| **C** | Problem real, response contested | **a decision from the human** — every item here appears in the `Q-n` list at the bottom |
| **D** | Not a problem — a want | prioritization |
| **E** | Seen once / accepted / cannot reproduce | **nothing, deliberately** — parked, with the reason written down |

Severity is still recorded per item. It is just not the sort axis.

**Bucket E is the one people skip and the one that pays.** Without a written home, the
observed-once item and the deliberately-accepted tradeoff re-enter the queue at every review
forever, and get re-investigated by whoever forgot the last conclusion. Parking is a real
disposition and it needs a place with a reason next to it.

**Items move between buckets and keep both addresses.** An item promoted out of E is titled
`E4→B9`, not renumbered. This preserves every earlier reference while recording the movement; a
renumber silently breaks references that still resolve, to the wrong item.

## Item grammar

```
### <BUCKET><n> — <short label>
**Seen:** <O-n> (+ <O-n>, …)
**Root cause (`CONFIRMED`):** <mechanism> — cited at <exact address>
**Response:** <what to do — one action, not a programme>
**Effort:** `<S|M|L>`
**Risk:** <what the response could disturb>
**Severity:** `<stop|major|minor|question>`
**Status:** `<open | in-flight | done | parked | superseded by <id>>`
```

Four notes on the fields, each of which exists because the obvious version of it fails.

**`Seen` points at the log; it never restates it.** The moment triage paraphrases an observation,
there are two versions of what happened and no rule about which is binding.

**`Root cause` carries a confidence token and an address, or it is not a root cause.** Cited
precisely enough that someone else lands on the same spot. Where the cause is not established,
write `UNVERIFIED:` or `UNRESOLVED:` and leave it — an item can sit in B for a long time and be
perfectly healthy. What it cannot do is sit in A on a plausible story.

**`Risk` is a property of the cure, not the symptom.** Severity says how bad the problem is; risk
says what the response could disturb. They are routinely conflated, and the conflation
systematically hides the case that matters most — a `minor` problem with a high-risk fix, which
is the exact profile of a change that makes things worse.

**`Effort` is a wall-clock band, not a score.** `S` = minutes, `M` = an hour-ish, `L` =
multi-hour or needs design care before it can start. A band is a prediction you can be wrong
about; a 5 is not.

---

## A — cause proven

### A`<n>` — `<label>`
**Seen:** `<O-n>`
**Root cause (`CONFIRMED`):** `<mechanism>` — cited at `<address>`
**Response:** `<…>`
**Effort:** `<S|M|L>` · **Risk:** `<…>` · **Severity:** `<token>` · **Status:** `<…>`

## B — direction clear, cause not proven

### B`<n>` — `<label>`
**Seen:** `<O-n>`
**Root cause:** `UNVERIFIED:` `<the hypothesis, and what would confirm it>`
**Response:** `<…>`
**Effort:** `<S|M|L>` · **Risk:** `<…>` · **Severity:** `<token>` · **Status:** `<…>`

## C — problem real, response contested

### C`<n>` — `<label>`
**Seen:** `<O-n>`
**Root cause:** `<…>`
**Response:** **contested** — `<option 1>` vs `<option 2>`, and what separates them
**Effort:** `<S|M|L>` · **Risk:** `<…>` · **Severity:** `question` · **Status:** `owed to human — Q-<n>`

## D — wants

### D`<n>` — `<label>`
**Seen:** `<O-n, or "not observed — proposed">`
**Response:** `<…>` · **Effort:** `<S|M|L>` · **Status:** `<…>`

## E — parked, deliberately

### E`<n>` — `<label>`
**Seen:** `<O-n>`
**Parked because:** `<seen once and not reproduced | accepted tradeoff, reason stated | cannot be
observed with the instruments available>`
**Reopens if:** `<the condition that should pull this back out — without one, "parked" means
"forgotten">`

---

## Clusters

> **Clusters are the deliverable.** The output of triage is not a sorted list — it is a set of
> clusters, each with **one** hypothesised cause marked `UNVERIFIED`, plus a residue of items
> that resisted grouping. **The residue is information, not failure.**

> **Forbidden here:** acting on a cluster (it is a hypothesis until RESOLVE proves it), and
> merging two items because they appeared together without a mechanism that would explain both.

### C-`<n>` — `<cluster label>`

**Hypothesised single cause (`UNVERIFIED`):** `<one mechanism, stated causally: X causes Y
causes the observed Z>`
**Items:** `<A1, B3, B7>`
**Would be confirmed by:** `<the specific observation or test that would establish it>`
**Would be refuted by:** `<the observation that would kill it — write this down; a hypothesis
whose contradiction surface you cannot state is one you cannot test>`

**Co-occurring but explicitly NOT in this cluster:**

- `<item>` — `<why it is excluded, despite appearing in the same window / place / week>`
- `<item>` — `<why>`

This last block is not optional and is not padding. Two problems appearing together are two
problems until a single cause is proven (L-5). One source project recorded a shared-root
hypothesis linking three findings, built its triage around it, and then refuted it — the three
had independent causes, and one of the three planned responses would have been wasted entirely.
Writing down what you are *declining* to merge is how that gets caught before the work happens
rather than after.

### Unclustered residue

`<Items that resisted grouping, listed. Do not force them into a cluster to make the board look
finished. An honest residue of four is worth more than a tidy set of three clusters, one of
which is fiction.>`

---

## Decisions owed to the human

Every item in bucket C appears here, plus anything else where the correct answer is *what you
want* rather than *what is true* — trade-offs between goods, not between right and wrong. A
collaborator asked to optimize will silently choose an objective function, it will be a
defensible one, and it will not be yours.

**A triage pass that does not end with a short list of questions has probably absorbed those
decisions silently.** That is the failure this section exists to catch: not a wrong answer, but
an answer nobody remembers being asked for.

1. **Q-`<n>`** — `<the question, stated so it can be answered yes/no or by choosing a named
   option>`
   **Rests on:** `<C-n / item ids>` · **Blocks:** `<what cannot proceed until this is answered>`
   **Options:** `<option A — consequence>` / `<option B — consequence>`
   **Recommendation:** `<yours, and whether you would be comfortable being overruled>`

---

## Exit condition

Triage is closed when every item has a bucket, an owner, and either a cluster or an explicit note
that it stands alone — and when every decision owed to the human is in the list above rather than
distributed through the prose.

---

## Worked example

*Continuing the observation window from `observation-log.template.md` — a house with recurring
damp. Domain is illustrative only.*

### A1 — utility-room wall, elevated moisture
**Seen:** O-4
**Root cause (`CONFIRMED`):** the cold-feed compression joint behind the washing machine is
weeping under pressure, not continuously — which is why the patch is dry to the touch and
tide-marked. Cited: joint wrapped in tissue 2026-03-08T10:00Z, machine run on a full cycle, tissue
saturated at the joint and dry 100mm either side; photograph `<ref>`. Re-run dry with the machine
isolated: tissue dry after two hours.
**Response:** remake the joint. Leave the wall unrepaired and unpainted for one full season so the
patch can be re-measured against O-4's baseline of 24.1 — repairing the surface first would
destroy the only measurement that could tell you whether the fix worked.
**Effort:** `S` · **Risk:** low; isolating the feed is reversible and affects nothing else ·
**Severity:** `major` · **Status:** open

### B3 — back bedroom, musty odour at back-left corner
**Seen:** O-3, O-6
**Root cause:** `UNVERIFIED:` moisture ingress at the rear elevation below the gutter run.
Confirmable by observing the gutter under live rainfall from outside, which has not been done —
every observation so far is from inside, and from inside this hypothesis cannot fail.
**Response:** observe the rear elevation during the next sustained rainfall before doing
anything.
**Effort:** `S` (the observation) · **Risk:** none — it is an observation · **Severity:** `major`
· **Status:** open, waiting on weather

### C2 — replaster now, or monitor for a season
**Seen:** O-3, O-4, O-7
**Root cause:** partially established; C-1 below is unproven.
**Response:** **contested** — replastering now removes the visible problem and simultaneously
destroys the surface that would tell you whether the underlying cause was ever fixed. Monitoring
for a season keeps the instrument but leaves the room unusable through winter. This is a
trade-off between goods and is not resolvable from evidence.
**Effort:** `L` either way · **Risk:** replastering is not cheap to reverse and forecloses
measurement · **Severity:** `question` · **Status:** owed to human — Q-1

### E4→B9 — hall ceiling pipe knock
**Seen:** O-9
**Was parked** as seen-once and unreproduced. **Promoted** 2026-03-19 after a second occurrence
under matched conditions (O-14), which converted a single anomaly into a two-point series. Keeps
both addresses so that every reference written while it was in E still resolves.
**Root cause:** `UNVERIFIED:` thermal contraction in the run above the hall ceiling.
**Effort:** `M` · **Risk:** low · **Severity:** `minor` · **Status:** open

### C-1 — rear-elevation water ingress
**Hypothesised single cause (`UNVERIFIED`):** the rear gutter is blocked or has failed at the
back-left corner; overflow saturates the external wall; the wall's inner face is the back-left
corner of the back bedroom, at floor level, which is exactly where the odour localises.
**Items:** B3 (O-3, O-6), B5 (O-7)
**Would be confirmed by:** direct observation of the gutter during sustained rainfall, from
outside, plus a matching rise in the internal corner reading within 48h of a rain event.
**Would be refuted by:** the gutter running clear under load, or the internal reading failing to
track rainfall across three or more events.

**Co-occurring but explicitly NOT in this cluster:**

- **A1 (O-4, utility wall)** — same house, same fortnight, same symptom class, and it is a
  different problem. The utility room is on the opposite elevation, and A1's cause is
  independently `CONFIRMED` at a cited address. Merging these because both are "damp" would have
  produced one gutter repair and one wall that stayed wet, and — worse — a story that explained
  both, which is why nobody would have re-checked.
- **E4→B9 (O-9, pipe knock)** — appears in the same window and shares nothing but a ceiling void.
  No mechanism has been proposed that would explain both, and "they are both in the roof space"
  is a location, not a cause.

### Decisions owed to the human

1. **Q-1** — Replaster the back bedroom now, or leave it bare and monitor through one full
   winter?
   **Rests on:** C2, C-1 · **Blocks:** all remedial work on that room, and the room's use.
   **Options:** replaster now — room is usable this winter, and you permanently lose the ability
   to tell whether the ingress was fixed / monitor — room is unusable until spring, and the
   measurement survives.
   **Recommendation:** monitor, because C-1 is still `UNVERIFIED` and replastering over an
   unproven cause is the expensive version of guessing. I would be comfortable being overruled
   here — the cost of being wrong is one winter, not the fabric of the building, and the room's
   usability is a preference I do not own.
