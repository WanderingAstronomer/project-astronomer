---
record_class: append-only
precedence: 5
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <the-external-query-log>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# QUERY LOG — `<project name>`

> **Doc class:** append-only — its own class, not a flavour of frozen (D-019). **Nothing in this
> file is ever edited or reordered.** An entry records a request that has already left the machine.
> It cannot be withdrawn, so it is not rewritten either.

**Required at:** **Lite, conditional** — gated on a condition, not a tier: required whenever a data
boundary exists *and* any outbound channel is permitted. If nothing leaves the machine, this file is
not needed; say that in the boundary rather than leaving both blank.

Every outbound request is recorded here — what was asked, in what form, to what destination, when,
and what it was derived from (B-3, `doctrine/07-boundaries.md`).

## Why this exists

**The failure this guards is silent and cannot be undone.** A query that discloses too much raises
no error, returns a perfectly good answer, and leaves no trace. Nothing announces it at the time and
nothing surfaces it later. That is what separates egress from every other boundary in this
framework: a bad read can be stopped, a bad change can be reverted, a bad conclusion can be refuted.
A disclosure is final at the moment it happens.

So the record is not an audit ritual. It is the only mechanism that makes a violation **findable at
all** — and per L-17, a rule that depends on judgement at every instance fails at the instance where
you are tired.

**A query is derived data (B-2).** It carries information out even when it copies nothing. *"How do
mid-size regional practices handle intake backlogs"* contains no name, no figure, no quoted string,
and discloses the sector, the scale, and the problem in one line. Ten of those are a profile.

## The test, applied before the request goes out

> **Could someone who had never seen the source material have asked this question?**

If yes, it goes. If no, the specificity that makes the answer "no" is exactly what is leaking, and
the request does not go — it becomes a question for the human who owns the material (L-15).

## Entry grammar

| Field | What it holds |
|---|---|
| `E-<n>` | permanent ID. Retire, never reuse |
| `<UTC>` | **live** timestamp, read at the moment of sending — never an ambient date |
| `Destination` | the channel and the service. "The web" is not a destination; name it |
| `Sent` | **the request verbatim, exactly as transmitted.** Not a paraphrase. The paraphrase is the version that looks fine |
| `Derived from` | the `S-<n>` / `O-<n>` this question came out of, or `none — general knowledge` |
| `Abstraction check` | how the request was made general enough to pass the test above, or why it needed no abstraction |
| `Returned to` | where the result was stored, so it is not re-fetched (see ritual `external-research`) |

## Entries

`<Copy this block per request. Append only.>`

```
### E-<n> · <live UTC>
- **Destination:** <service / channel>
- **Sent:** "<verbatim request>"
- **Derived from:** <S-n, O-n, or "none">
- **Abstraction check:** <what was removed, or why nothing needed to be>
- **Returned to:** <path to the cached result>
```

### Worked example

```
### E-4 · 2026-07-24T14:02Z
- **Destination:** web search (public search engine)
- **Sent:** "typical intake backlog causes for small professional services firms"
- **Derived from:** S-11, S-14
- **Abstraction check:** the source names the firm, its city, its headcount, and the specific
  bottleneck. All four removed. What remains would be asked by anyone researching the sector
  cold — which is the test. An earlier draft read "regional two-partner practice with a 6-week
  intake queue"; that draft copied nothing and would have disclosed all four.
- **Returned to:** research/intake-backlog-causes-2026-07-24.md
```

The rejected draft is recorded on purpose. **The near-miss is the most useful thing in this file** —
it is the only evidence that the test is being applied rather than assumed, and a log with no
abstraction ever recorded is a log describing questions that were always safe, which is not what
these logs are for.

## Forbidden

- Logging the paraphrase instead of what was sent. The gap between them is where the leak lives.
- Sending first and logging after. The log is what makes you apply the test; written afterward it
  records a decision you did not consciously make.
- An unlisted destination. Unclassified is not permitted (B-4) — the same rule as an unlisted file.
- Treating a clean per-query record as proof of no disclosure. **Ten individually clean queries can
  still compose into a profile.** This log makes that reviewable; it does not make it caught, and
  `doctrine/07-boundaries.md` says so under "What this file does not settle."

## Lifecycle

Opened alongside the data boundary, before the first outbound request. Appended to at the moment of
each request. Never frozen, never edited, never pruned — a query log with old entries removed cannot
answer the only question it exists to answer.
