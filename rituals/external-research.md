# External research

> **Doc status:** living.

## When

You need something the project does not know and cannot observe for itself — how a thing is
normally done, what a standard says, what an external source reports. Route here before reaching
for an outside source, not after.

The tell that you are already outside this ritual: you are about to cite a figure you did not
retrieve yourself, from a document you have not opened, because you remember it.

## Do

1. **Check the cache first.** If the project has already retrieved something on this, read that.
   Re-fetching what you already hold costs an outbound request (B-3) and produces a second copy
   that will drift from the first (L-14). A cache that is not checked first is a directory, not a
   cache.
2. **Ask whether this is answerable from the project's own material.** An external source consulted
   before the local one produces a claim about the world where an observation was available. The
   local answer is `OBSERVATION`; the external one is `CITED`, and inherits the strength of its
   source, no more.
3. **Clear the request against the boundary before it goes out** (B-2). Could someone who had never
   seen the source material have asked this question? If not, the specificity that makes the answer
   "no" is what is leaking. Abstract it or do not send it.
4. **Log the request before you read the result** (B-3). `E-<n>`, live stamp, destination, the
   request **verbatim as sent**. Written after the answer arrives, the log records a decision you
   never consciously made.
5. **Retrieve it yourself.** Do not cite a source you have not opened. This is L-11's rule applied
   to retrieval: *"trust no number quoted to you"* covers the number a search result quotes from a
   document, which is a summary of a summary and is where the digit changes.
6. **Store what came back, with three dates that are not the same date.** When the source was
   *published*, when you *retrieved* it (`retrieved_at`), and when the claim it supports was
   *observed*. Collapsing them is how a five-year-old figure becomes this week's evidence.
7. **Cite precisely enough to return to it.** A citation that cannot be re-opened is a claim you
   have chosen to believe (`doctrine/02-epistemics.md`).
8. **Type it `CITED` and scope it** (L-3, L-4). An external source's claim holds under the
   conditions *it* studied, which are almost never yours. Unscoped, it is `ASSERTED-UNIVERSAL` and
   routes to scrutiny rather than into the findings.
9. **Record what you looked for and did not find.** An absent result is a real one and it is the
   single most re-run search in any project. Left unrecorded, you will pay for it again in three
   weeks.

## The staleness rule

A retrieved source has two clocks and they run at different speeds: **the source can change, and the
world the source describes can change.** A stale cache hit is not a wrong answer, it is an *old*
answer, and the difference matters when deciding whether to re-fetch.

`rituals/instrument-drift.md` governs a number you have been relying on. This governs the document
it came from. When a cached source is older than the thing it describes changes, treat it the way
you would treat any figure you did not measure yourself: re-retrieve, record the delta, and check
what rested on the old version.

## Record

- `QUERY LOG` — one `E-<n>` per outbound request, appended before the result is read.
- The cached result itself, stored where the next session will look, with `retrieved_at` on it.
- `OBSERVATIONS` — only if the retrieval was part of an open window; the result is `CITED`, never
  `OBSERVATION`.
- `DECISIONS` — only if what came back changed a decision. Say which source, and which entry.
- **The searches that returned nothing**, alongside the ones that did.

## Forbidden

- Sending the request before clearing it against the boundary. There is no undo on a disclosure.
- Citing a source you did not open, including one a search result summarized for you.
- Storing a result without its retrieval date. An undated cache entry is indistinguishable from a
  fresh one, and will be read as fresh.
- Promoting `CITED` to `OBSERVATION` because the source is reputable. Reputation is not the same
  measurement as having seen it yourself, and the ladder has no rung for "probably fine."
- Treating a clean per-request check as proof of no disclosure. **Ten individually clean requests
  can compose into a profile** — the log makes that reviewable, not caught
  (`doctrine/07-boundaries.md`).
