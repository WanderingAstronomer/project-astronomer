# 03 — The Loop

Five phases. Each has an entry condition, an exit condition, and a list of actions that are
forbidden inside it. The forbidden lists are the part that matters — every one of them exists
because a source project did the forbidden thing and paid for it.

```
OBSERVE → TRIAGE → RESOLVE → ACT → RECORD → (OBSERVE)
```

The loop is not a project plan. It is what you run every time something surprises you, at
whatever scale the surprise deserves.

---

## OBSERVE

**Purpose.** Get everything that is actually happening onto the record, verbatim, before anyone
starts explaining it.

**Entry.** A decision to look, with a declared window. "I am observing X for two weeks" or "I
am running a pass over the whole surface today."

**Do**

- Record what happened, in the words it happened in. Verbatim first, interpretation second.
- Stamp each entry with a live timestamp and the **conditions of observation** — the
  astronomer's *seeing*. What instrument, what state, what else was going on. An observation
  without its conditions cannot be compared to another one later.
- Where you have an initial explanation, write it — labelled `UNVERIFIED`, in its own field,
  never blended into the description.
- Update the log **every entry**, not at the end of the session. A pass that is written up
  afterward is a pass filtered through what you concluded during it.

**Forbidden**

- **Any change to the subject.** Not one line. Not the obvious thing. This is a hard gate, not
  a guideline (L-7, D-014).
- Grouping items by apparent cause. That is TRIAGE's job and doing it here contaminates the
  raw record with a conclusion you cannot later separate out.
- Deciding something is not worth recording because it seems minor or you cannot reproduce it.
  Record it and mark it; VOC kept a retracted finding specifically so that a recurrence would
  already have a first sighting on the books.

**Exit.** The window closes, or the surface is covered. Mark it explicitly — the source project
that ran the largest audit wrote a literal `INTAKE CLOSED` marker into its ledger, because
without one, intake and triage overlap and the boundary silently stops existing.

---

## TRIAGE

**Purpose.** Sort what you have by **what you know about it**, and group by shared cause.

**Entry.** Observation window closed.

### Bucket by epistemic state, not by severity

This is OD's contribution and it is better than the severity scheme almost everyone reaches for
first. Severity tells you what you want to be true; epistemic state tells you what the item
actually needs next.

| Bucket | State | What it needs |
|---|---|---|
| **A** | Cause proven, with a citation | nothing — it is ready to act on |
| **B** | Direction clear, cause not formally proven | mechanical execution |
| **C** | Problem real, response contested | **a decision from the human** |
| **D** | Not a problem — a want | prioritization |
| **E** | Seen once / accepted / cannot reproduce | **nothing, deliberately** — parked with a reason |

Severity still gets recorded. It just is not the sort axis, because sorting by severity produces
a list of things you would like fixed, and sorting by epistemic state produces a list of things
that can actually move.

**Bucket E is the one people skip and the one that pays.** Without a written home, the
observed-once item and the accepted-tradeoff item re-enter the queue at every review forever,
and get re-investigated by whoever forgot. Parking is a real disposition and it needs a place.

### Clusters are the deliverable

Group items that share **one** root cause. Then, explicitly and in writing, separate the items
that merely co-occur (L-5). Two problems on one surface are two problems.

> "Clusters are the deliverable." — VOC

The output of TRIAGE is not a sorted list. It is a set of clusters, each with a hypothesised
single cause marked `UNVERIFIED`, plus a residue of items that resisted grouping — and that
residue is information, not failure.

**Forbidden**

- Acting on a cluster. The cluster is a hypothesis until RESOLVE proves it.
- Merging two items because they appeared together, without a mechanism that would explain
  both.

**Exit.** Every item has a bucket, an owner, and either a cluster or an explicit note that it
stands alone. Every decision the human owes is listed in one place — a triage pass that does not
end with a short list of questions for the human has probably absorbed those decisions silently.

---

## RESOLVE

**Purpose.** Prove the cause. Or refute it, which is equally good.

**Entry.** A cluster with a hypothesised cause.

**Do**

- Go to the actual source. Not the record of the source, not the summary, not last month's
  note. VOC's rule: "the spec has been wrong, the ledger has been wrong, and **you** will be
  wrong."
- Cite where you proved it, precisely enough for someone else to land on the same spot. A root
  cause without an address is not a root cause.
- Try to **refute** your own hypothesis before confirming it. Default to *not proven* when you
  cannot independently establish it — the bias must point at refutation, because the bias of an
  unaided investigator already points the other way.
- When you refute it, say so plainly and keep the refuted version (L-6).
- State the **blast radius** — what else touches this cause. Frequently the cluster was too
  small.

**Forbidden**

- **Acting from the hypothesis.** VOC states it directly: "Do not fix from the hypothesis." Its
  standing table of six recorded-then-refuted root causes is what that rule cost to learn.
- Accepting a cause because it explains the symptom. Plausibility is not evidence; several of
  those six were plausible and had already been built on.

**Exit.** Each cluster is `CONFIRMED` with a citation, `REFUTED` with a note, or `UNRESOLVED`
with a statement of what would settle it. All three are valid exits. `UNRESOLVED` is not
failure — it is the honest terminal state, and pretending otherwise is how a guess enters the
record as a finding.

---

## ACT

**Purpose.** Make the smallest reversible change that addresses the proven cause.

**Entry.** A `CONFIRMED` cause.

**Do**

- **One variable at a time** (L-10), or accept in advance and in writing that the result will be
  unattributable.
- Prefer the reversible option. Where a judgement call is not cheap to reverse, take the
  conservative one and record why — this is VOC's constraint on autonomous decisions and it
  generalizes past AI collaboration.
- Where the same failure class has now recurred three times, **build a gate instead of a third
  fix** (L-17).
- Classify the change size before starting — *minimal / medium / large*. Re-classing upward
  mid-flight is fine and expected; silently doing more than the plan is not. VOC's phrasing:
  "bigger scope = an explicit re-plan, not an in-session expansion."

**Forbidden**

- Bundling unrelated changes because you are already in there. That is how L-10 is violated by
  people who agree with L-10.
- Fixing something outside the scope you declared. Record it and leave it. If a workstream is
  fenced, the discovery goes in the report, untouched, with a citation.

**Exit.** The change is made, and the acceptance criterion pre-registered under L-9 has been
evaluated against reality — including when it says the change did not work.

---

## RECORD

**Purpose.** Make it so a stranger — including you in six months — can reconstruct what
happened and what it means.

Named as its own phase deliberately (D-013). Three of the four source projects folded recording
into execution, and recording is the first thing dropped under pressure. Giving it an entry
condition and an exit condition is what stops that.

**Do**

- **Freeze** what happened: a point-in-time record, annotated later but never edited (L-13).
- **Update** what is true: the living specification is rewritten to current reality. State what
  *is*, not the history of how it got there — the ledger and the commit tree hold history.
- **Append** any decision made, with a live UTC stamp and its reason (L-2).
- Record what you did **not** verify. VOC requires this as a named section in every returned
  work report, with the note that "owed by a human" is an acceptable and expected outcome.
- Record what you got **wrong** during the loop, including about your own work.

**The recording voice.** OD and VOC converged on the same shape for the entry that closes a
loop, and it is worth copying literally:

```
Subject:  the outcome — what is now true, stated as a result, not a task
Line 1:   the defect as a causal narrative — mechanism → consequence, in one sentence
Body:     what changed, grouped by area
Then:     verification evidence — what was checked, and at what altitude
Then:     what is still owed, and to whom
```

The second line is the one that carries the value. "Fixed the chart" is a task. "The chart was
fed a session count and told to call it words" is a mechanism — and a reader six months later
learns something from the second that they cannot get from the first.

**Exit.** The frozen record exists; the living document matches reality; the ledger has the
decision. If any of the three is missing, the loop has not closed — it has just stopped.
