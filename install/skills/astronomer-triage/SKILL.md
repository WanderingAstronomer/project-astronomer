---
name: astronomer-triage
description: Turn a closed observation log into buckets and clusters — use after INTAKE CLOSED, or whenever the operator has a pile of items and asks what to do with them, what matters, or what goes together.
---

# Triage

Purpose: sort items by **what you know about them**, then group by shared cause. The output is
clusters and a short list of decisions owed to the operator — not a prioritized list of work.

## Preconditions

- The observation log carries an explicit `INTAKE CLOSED` marker. If it does not, stop: run
  `astronomer-observe` to close the window first. Triaging an open log means triaging a moving
  target.
- Work from the log only. Do not add items you thought of during triage — those open a new
  window.

## Step 1 — bucket every item

By epistemic state, not by severity. Severity tells you what you want to be true; epistemic
state tells you what the item actually needs next.

| Bucket | State | Needs |
|---|---|---|
| **A** | cause proven, with a citation | nothing — ready to act on |
| **B** | direction clear, cause not formally proven | mechanical execution |
| **C** | problem real, response contested | **a decision from the operator** |
| **D** | not a problem — a want | prioritization |
| **E** | seen once / accepted / cannot reproduce | **nothing, deliberately** — park with a reason |

Every item gets exactly one bucket. Record severity (`stop`/`major`/`minor`/`question`) as a
separate field — it is never the sort axis.

**Do not skip bucket E.** Without a written home, the seen-once item and the accepted-tradeoff
item re-enter the queue at every review forever and get re-investigated by whoever forgot.
Parking is a real disposition and the reason for parking is the whole entry.

An item that moves bucket later keeps both addresses (`E4→B9`). Never renumber.

## Step 2 — cluster by shared cause

Group items that share **one** root cause. Give each cluster a `C-<n>`, a one-sentence
hypothesised mechanism, and the token `UNVERIFIED`. The hypothesis is a hypothesis; it stays
labelled as one until RESOLVE proves it.

For each proposed cluster, answer in writing: **what mechanism would produce all of these?** If
you cannot state one, it is not a cluster.

## Step 3 — separate co-occurrence, explicitly

Under its own heading, list the items that appeared together and are **not** grouped, with the
reason. Two problems on one surface are two problems. Items that share a time, a place, a
session, or a surface share a *context*, not a cause.

This section is mandatory even when empty — write "none" rather than omitting it. Its absence is
how an unexamined shared-cause story survives.

Items that resisted grouping go in a residue list. The residue is information, not failure.

## Forbidden

- **Acting on a cluster.** It is a hypothesis until proven.
- **Merging two items because they appeared together** without a mechanism that explains both.
- Promoting a cluster's confidence because it is elegant, or because several items fit.
- Absorbing a contested call by picking the reasonable-looking option yourself.

## Step 4 — close with the decisions owed

End the pass with a single numbered list of **questions for the operator** — every bucket-C item
plus anything where you found yourself about to choose on their behalf. Give each a `Q-<n>`,
state the options, and state what each option costs.

A triage pass that does not end with a short list of questions has almost certainly absorbed
those decisions silently.

## Report

Counts per bucket · clusters with their `UNVERIFIED` mechanisms · the co-occurrence separations ·
the residue · the numbered questions. Say which items you were unsure how to bucket and why.
