---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - corpus-intake-procedure
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Corpus intake

> **Doc status:** living.

## When

You have been handed material the project did not author — a folder of documents, an export, an
archive, someone else's working files — and you are about to start reading it.

The tell that you are already outside this ritual: you have read four documents and could not say
how many there are in total.

## Do

1. **Do not open anything yet.** The boundary comes first. If the material sits anywhere the data
   boundary does not already cover, that boundary is written or extended *before* the first file is
   opened — reading a document to work out whether you were allowed to read it is the one order
   that cannot be undone (`ritual starting-a-project`, step 1).
2. **Count it before you characterize it.** How many items, what formats, what size distribution.
   This is cheap, it is mechanical, and it is the number every later claim about coverage rests on.
   Forty documents and four thousand are different projects, and you cannot tell which you are in
   from the first ten.
3. **Count the destination too, and work out the share** (K-7). Steps 1 and 2 look at the material.
   This step looks at what it is landing *in*. If the incoming corpus will be searched alongside
   the project's own material — one index, one default query surface — then compute
   `incoming ÷ (existing + incoming)` **before** the import, and **pre-register the share at which
   you would not do it.** Write the number down first; a threshold chosen afterward is chosen to
   permit whatever you already did.

   This is the only step in this ritual that can tell you an intake should not happen. Everything
   else here makes an intake *honest*; this one asks whether it is *free*, and it is not. One
   measured case: a vendor corpus reached **54%** of the index, after which a query for the
   project's own architecture returned that vendor's navigation links above it. Nothing about the
   intake was wrong. **A successful import is the case K-7 is about** — a failed one damages
   nothing, because nothing lands.

   If the share is uncomfortable and the material is still wanted, the response is **segregation,
   not omission**: a separate index, or a path the default query does not reach, with retrieval
   from it done by explicit path (`rituals/corpus-retrieval.md`). Record which you chose.

   **Segregation is measured, once** (`O-45`): one project excluded a 52.5% vendor corpus from
   its search index and the foreign share of what search could see went to zero, while
   read-by-path still reached the excluded material. **It did not fix everything**, and the
   part it missed is the part worth knowing — a search whose volume comes from the project's
   *own* material is untouched by excluding anything foreign, and the two are indistinguishable
   from the symptom.

4. **Assess readability per item, and do not trust the extension.** A `.pdf` is either extractable
   text or a picture of text; those are different instrument problems with different failure modes,
   and only one of them announces itself. Record `FULL` / `PARTIAL` / `NONE` per document.
5. **Name what could not be read, specifically.** *"Pages 40–61 are scans with no text layer"* is a
   usable record. *"Mostly worked"* is not. This is the field the whole artifact exists for — see
   why below.
6. **Give every item a permanent ID** (`S-<n>`), including the ones you were not allowed to open.
   A boundary-excluded document still gets a row, so that six months later its absence reads as a
   recorded decision rather than an unexplained gap.
7. **Change nothing.** Do not rename, reorganize, convert, or normalize the source material during
   intake. It is someone else's record; moving it destroys the link to whoever handed it over, and
   a conversion you performed is now between you and the evidence (L-7, L-13).
8. **Close the intake explicitly** before drawing anything from it, the same way an observation
   window closes. Then, and only then, open the first observation window over the material.

## Why the "not read" field is the point

**A failed extraction does not look like a failure.** It returns a page count, no error, and almost
no text — identical in shape to a document that genuinely said little. Nothing distinguishes *"this
source was thin"* from *"this source was not read"*, and the second one silently narrows what every
downstream conclusion actually rests on.

That is L-12 at the ingestion layer: the instrument has to be capable of failing in the way that
matters, and the default one fails invisibly. It is also L-16 — a process reporting a success it has
not achieved is the highest-severity defect class in this framework, above outright breakage.

`PARTIAL` is the state that costs you. `FULL` and `NONE` are obvious at a glance; `PARTIAL` looks
exactly like `FULL` from anywhere downstream.

## Blast radius

**Friction** — recoverable inside the session, as long as it is caught before conclusions are drawn.

**Conflagration** once a finding has been published from a corpus whose coverage was never
recorded. At that point you cannot tell which conclusions were drawn from the whole thing, and
re-establishing that means re-reading everything — the same recovery cost as an observation window
that was contaminated mid-pass.

**Conflagration of a second, slower kind when step 3 was skipped**, and this one does not announce
itself at all. The damage is not to conclusions drawn from the imported corpus — those may be
perfect. It is to every *unrelated* question the project asks afterward, each of which now competes
with the import for the same answer slots. There is no failed intake to point at and no finding to
re-check. What you get instead is a project that gradually stops being able to find its own
thinking, and reads that as *not having written it down*.

The recovery cost is asymmetric with the import cost, which is the part worth knowing in advance:
importing is one afternoon, and separating an index afterward means re-deciding, per document, what
should have been two collections from the start.

## Record

- `SOURCE MANIFEST` — one `S-<n>` per document, including excluded ones, with extraction state and
  what specifically could not be read.
- `DATA BOUNDARY` — written or extended first, if the material reaches beyond what is already
  classified.
- `DECISIONS` — the intake itself: what corpus, from whom, under what authorization, and the
  coverage you ended up with. If a portion could not be read, that is a `caveat (owned):` on every
  finding drawn from it.
- Any claim later drawn from a `PARTIAL` corpus carries that in its **scope** (L-4). "Established
  from the 68% of the corpus that was machine-readable" is a scoped claim; without the scope it is
  `ASSERTED-UNIVERSAL`.
- `CAPABILITY INVENTORY` — the **share** from step 3, measured before and after, in the corpus
  retrieval row, with the date (K-7, K-4). This is the one number that makes the next intake
  decidable rather than arguable, and the project that has it can answer *"can we take another
  one?"* without re-measuring the whole index.
- `DECISIONS` — if the material was **segregated** rather than merged, that is a decision with a
  reason and a stated retrieval path, not an implementation detail. A future session searching the
  default surface and finding nothing needs to know the other collection exists.
