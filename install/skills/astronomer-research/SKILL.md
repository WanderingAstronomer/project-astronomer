---
name: astronomer-research
description: Retrieve something from outside the project, safely and citably — use before any web search, external lookup, or outbound request, whenever a claim needs a source the project cannot observe for itself, and whenever the operator asks what the accepted practice or the published figure is.
---

# External research

Purpose: get an outside answer without leaking the inside, and without acquiring a citation you
cannot return to. This operationalizes ritual `external-research`.

Two things go wrong here and they fail in opposite ways. A query can disclose more than intended —
silently, permanently, with no error raised. And a retrieved claim can enter the record as though it
were observed, when it was only read.

## Step 1 — check what the project already holds

Look in the research cache before reaching outward. Re-fetching costs an outbound request and
produces a second copy that will drift from the first (L-14).

A cache nobody checks first is a directory, not a cache.

## Step 2 — ask whether this is answerable from the project's own material

An external source consulted before the local one turns an available observation into a citation. A
local answer is `OBSERVATION`; an external one is `CITED` and inherits the strength of its source,
no more.

## Step 3 — clear the request against the boundary, before it goes out

**A query is derived data.** It carries information out even when it copies nothing. *"How do
mid-size regional practices handle intake backlogs"* contains no name, no figure, no quoted string,
and discloses the sector, the scale, and the problem in one line.

Apply the test:

> **Could someone who had never seen the source material have asked this question?**

If **yes** — send it. If **no** — the specificity that makes the answer "no" is exactly what is
leaking. Abstract it, or turn it into a question for the human who owns the material (L-15).

There is no undo. A disclosure raises no error, returns a good answer, and cannot be withdrawn.

## Step 4 — log it before you read the result

Append `E-<n>` to the query log: live stamp, destination, and **the request verbatim as sent** — not
a paraphrase. The paraphrase is the version that always looks fine.

Written after the answer arrives, the log records a decision you never consciously made. Written
first, it is what makes you apply Step 3 at all.

Record the abstraction you performed, including drafts you rejected. **The near-miss is the most
useful line in the log** — it is the only evidence the test is being applied rather than assumed.

## Step 5 — retrieve it yourself

Do not cite a source you have not opened, including one a search result summarized for you. That is
L-11 applied to retrieval: a figure quoted by a snippet is a summary of a summary, and that is where
the digit changes.

## Step 6 — store it with three dates that are not the same date

When the source was **published**, when you **retrieved** it (`retrieved_at`), and when the claim it
supports was **observed**. Collapsing them is how a five-year-old figure reads as this week's
evidence.

Store it where the next session will look, so Step 1 can find it.

## Step 7 — type it and scope it

`CITED`, always — never `OBSERVATION`, however reputable the source. Reputation is not the same
measurement as having seen it yourself, and the ladder has no rung for "probably fine."

Scope it (L-4). An external claim holds under the conditions *that source* studied, which are almost
never yours. Unscoped, it is `ASSERTED-UNIVERSAL` and routes to scrutiny rather than into findings.

## Forbidden

- Sending before clearing against the boundary.
- Logging a paraphrase instead of what was sent. The gap between them is where the leak lives.
- An unlisted destination — unclassified is not permitted, the same rule as an unlisted file.
- Citing a source you did not open.
- Storing a result with no retrieval date. An undated cache entry is indistinguishable from a fresh
  one and will be read as fresh.
- Treating clean per-request checks as proof of no disclosure. **Ten individually clean requests can
  compose into a profile.** The log makes that reviewable; it does not make it caught.

## Record

`QUERY LOG` (one `E-<n>` per request, appended **before** the result is read — destination, verbatim
request, what it was derived from, the abstraction performed) · the cached result, stamped
`retrieved_at` · `DECISIONS` (only if what came back changed one — name the source and the entry) ·
**the searches that returned nothing**, which is the most re-run search in any project.
