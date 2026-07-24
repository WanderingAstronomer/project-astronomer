---
name: astronomer-intake
description: Take in a body of documents the project did not author and record what was and was not readable — use when the operator hands over a folder, an export, an archive, or a client corpus, before any of it is read or analyzed, and whenever a conclusion needs to state what portion of a corpus it actually rests on.
---

# Corpus intake

Purpose: turn "here is a pile of documents" into a counted, ID'd, coverage-known corpus **before**
the first observation window opens over it. This operationalizes ritual `corpus-intake`.

The failure this prevents is quiet. A failed extraction returns a page count, no error, and almost
no text — indistinguishable from a document that genuinely said little. Every conclusion downstream
then rests on a corpus you only partly read, and nothing says so.

## Step 1 — the boundary comes first

If any of this material sits outside what the data boundary already covers, **stop.** Get the
boundary written or extended before opening anything.

Reading a document to decide whether you were allowed to read it is the one order that cannot be
undone. If there is no data boundary at all, run `astronomer-start` step 1 first.

## Step 2 — count before you characterize

How many items, what formats, what size spread. Mechanical, not interpretive — use a directory
listing and a file-type check, not a reading pass.

Forty documents and four thousand are different projects, and the first ten do not tell you which
one you are in. Every later claim about coverage rests on this number.

## Step 3 — assess readability per item, and do not trust the extension

A `.pdf` is either extractable text or a picture of text. Those are different instrument problems
with different failure modes, and only one of them announces itself. Check; do not infer from the
suffix.

Record one of three states per document:

- **`FULL`** — everything in it is now available to read.
- **`PARTIAL`** — some content came out, some did not. **Name what did not.**
- **`NONE`** — nothing usable. A complete, legitimate entry.

`PARTIAL` is the state this whole step exists for. `FULL` and `NONE` are obvious at a glance;
`PARTIAL` looks exactly like `FULL` from anywhere downstream.

## Step 4 — one permanent ID per item, including the ones you may not open

Every document gets `S-<n>` in the source manifest — including RED items, which get a row recording
that they exist and were **not** opened.

Without that row, six months later nobody can tell whether a document was excluded deliberately or
simply missed. Those are very different facts about your coverage.

## Step 5 — name what could not be read, specifically

*"Pages 40–61 are scans with no text layer; no OCR run; this is a third of the document and includes
every appendix table"* is a usable record.

*"Mostly worked"* is not.

If you did not check, write **"not checked"** — that is a different claim from "nothing was
missing," and conflating the two is what makes a partial corpus look complete.

## Step 6 — close intake, then open the window

State the coverage you ended up with, as a number: how many items, how many `FULL` / `PARTIAL` /
`NONE`. Log the intake in the ledger — what corpus, from whom, under what authorization, with what
coverage.

Then open the first observation window. Intake is not observation; it establishes what you are able
to observe.

## Forbidden

- Opening anything before the boundary covers it.
- Renaming, reorganizing, converting, or "tidying" the source material. It is someone else's
  record, and a conversion you performed now sits between you and the evidence (L-7, L-13).
- Recording `FULL` without having checked. The default is unknown, not `FULL`.
- Omitting a document because you were not allowed to read it.
- Drawing any conclusion from the corpus without stating what portion of it you could read. A
  finding over a `PARTIAL` corpus carries that in its scope (L-4) — *"established from the 68% that
  was machine-readable"* is a scoped claim; without it, the claim is `ASSERTED-UNIVERSAL`.

## Record

`SOURCE MANIFEST` (one `S-<n>` per document — tier, format, extent, instrument, extraction state,
and what specifically could not be read) · `DATA BOUNDARY` (written or extended first, if the
material reached beyond it) · `DECISIONS` (the intake, its authorization, and the coverage achieved,
with a `caveat (owned):` naming any unread portion).
