---
record_class: append-only
precedence: 5
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <corpus-coverage>
  - <what-could-not-be-read>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# SOURCE MANIFEST — `<project name>` — `<intake name>`

> **Doc class:** append-only — its own class, not a flavour of frozen (D-019). An entry records what
> a document yielded **at intake, with the instrument used then**. Re-extracting later with a better
> instrument is a new entry naming the old one, never an edit to it.

**Required at:** **Lite, conditional** — gated on a condition, not a tier: required whenever the
project takes in material it did not author. A two-person Lite project handed forty client PDFs
needs this more than a Full-tier project working entirely on its own output.

The observation log records what you **saw**. This records what you were **able to read** — and,
more importantly, what you were not.

## Why this exists

**A failed extraction does not look like a failure.** A scanned PDF returns a page count, no error,
and almost no text. A spreadsheet with three hidden sheets returns one. An email export drops
attachments silently. In every case the tooling reports success, the content is thin, and nothing
distinguishes *"this document said little"* from *"this document was not read."*

That is L-12 at the ingestion layer: the instrument must be capable of failing in the way that
matters, and here the default instrument fails **invisibly**. It is also L-16 — a process that
reports success it has not achieved is the highest-severity defect class in this framework.

**File extension does not tell you readability.** A `.pdf` is either extractable text or a picture
of text, and those are different instrument problems with different failure modes. You cannot know
which without checking, and the check is cheap compared to concluding from a corpus you only
partly read.

## Entry grammar

| Field | What it holds | Why |
|---|---|---|
| `S-<n>` | permanent ID. Retire, never reuse | every later claim cites the source it came from, precisely enough to return to it |
| `Name` | the file, as it arrived | renaming on intake severs the link to whoever handed it over |
| `Boundary tier` | `RED` / `GREEN` / `YELLOW` from the data boundary | a manifest row for a RED item records that it exists and was **not** opened. That is a real entry, not an omission |
| `Format` | what it actually is, not what the extension claims | |
| `Size / extent` | bytes, pages, rows, duration — whatever the unit is | tells you what "partial" cost you |
| `Instrument` | what did the reading, and its version | an extraction is only reproducible if you know what did it |
| `Extraction` | `FULL` · `PARTIAL` · `NONE` | three states, not two. `PARTIAL` is the one that gets rounded to `FULL` |
| `Not read` | **what specifically could not be extracted, and why** | the load-bearing field. Blank means "nothing was missing," not "I did not check" |
| `Intake <UTC>` | live stamp | |

## Extraction states

- **`FULL`** — everything the document contains is now available to read.
- **`PARTIAL`** — some content extracted, some did not. **Name what did not.** "Pages 40–52 are
  scanned images, not extracted" is a usable entry; "mostly worked" is not.
- **`NONE`** — nothing usable came out. This is a legitimate, complete entry. A document that could
  not be read is a fact about your coverage and belongs in the record; leaving it out silently
  converts a known gap into an unknown one.

**`PARTIAL` is the state this artifact exists for.** `FULL` and `NONE` are both obvious at a glance.
`PARTIAL` looks exactly like `FULL` from downstream, and it is the one that quietly narrows what
your conclusions actually rest on.

## Entries

`<Copy this block per document. Append only.>`

```
### S-<n> — <name as it arrived>
- **Boundary tier:** <RED | GREEN | YELLOW>
- **Format:** <what it actually is>
- **Size / extent:** <pages, rows, bytes, duration>
- **Instrument:** <what read it, and its version>
- **Extraction:** <FULL | PARTIAL | NONE>
- **Not read:** <specifically what, and why — or "nothing">
- **Intake:** <live UTC>
```

### Worked examples

```
### S-7 — 2024-annual-review.pdf
- **Boundary tier:** GREEN
- **Format:** PDF, 61 pages — pages 1-39 digital text, pages 40-61 scanned images
- **Size / extent:** 61 pages, 8.2 MB
- **Instrument:** <extractor and version>
- **Extraction:** PARTIAL
- **Not read:** pages 40-61 are scans with no text layer; no OCR was run. This is roughly a third
  of the document and includes every appendix table. Any claim about the appendices is unsupported
  until this is re-extracted.
- **Intake:** 2026-07-24T15:40Z

### S-8 — custody-file-2019.pdf
- **Boundary tier:** RED
- **Format:** not examined
- **Size / extent:** not examined
- **Instrument:** none — not opened
- **Extraction:** NONE
- **Not read:** the entire document. RED under the data boundary (privileged). Listed here so that
  its absence from the analysis is a recorded decision rather than an unexplained gap.
- **Intake:** 2026-07-24T15:41Z
```

The `S-8` entry is the shape worth copying. **A boundary-excluded document still gets a row.**
Otherwise, six months later, nobody can tell whether it was excluded on purpose or simply missed —
and those are very different facts about your coverage.

## Forbidden

- Recording an extraction as `FULL` without having checked that it was. The default is not `FULL`;
  the default is unknown until you look.
- Leaving `Not read` blank when you did not check. Write "not checked" — that is a different claim
  from "nothing was missing," and conflating them is what makes a partial corpus look complete.
- Opening a document to classify it. The boundary tier comes from the data boundary, which is
  written first, by the human. Reading it to decide whether you were allowed to read it is the one
  order that cannot be undone.
- Drawing a conclusion from a corpus without saying what portion of it you could read. A finding
  over a `PARTIAL` corpus carries that in its scope (L-4).

## Lifecycle

Opened before the first document is read, alongside the data boundary. Appended per document during
intake. Never edited — a re-extraction with a better instrument is a new entry that names the entry
it supersedes, so the record still shows what you were working from when you drew the conclusions
you drew.
