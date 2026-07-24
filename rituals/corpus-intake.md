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
3. **Assess readability per item, and do not trust the extension.** A `.pdf` is either extractable
   text or a picture of text; those are different instrument problems with different failure modes,
   and only one of them announces itself. Record `FULL` / `PARTIAL` / `NONE` per document.
4. **Name what could not be read, specifically.** *"Pages 40–61 are scans with no text layer"* is a
   usable record. *"Mostly worked"* is not. This is the field the whole artifact exists for — see
   why below.
5. **Give every item a permanent ID** (`S-<n>`), including the ones you were not allowed to open.
   A boundary-excluded document still gets a row, so that six months later its absence reads as a
   recorded decision rather than an unexplained gap.
6. **Change nothing.** Do not rename, reorganize, convert, or normalize the source material during
   intake. It is someone else's record; moving it destroys the link to whoever handed it over, and
   a conversion you performed is now between you and the evidence (L-7, L-13).
7. **Close the intake explicitly** before drawing anything from it, the same way an observation
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
