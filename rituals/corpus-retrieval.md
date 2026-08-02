---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - corpus-retrieval-procedure
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Corpus retrieval

> **Doc status:** living.

## When

You are about to ask a corpus a question — a search, a semantic query, a grep — and act on what
comes back. Also: any time you are about to conclude *"the project never wrote that down."*

The tell that you need this ritual and are not using it: you searched, you got a result, and you
used the result. Nothing in that sequence asked whether what came back was **the** answer or merely
**an** answer, and at corpus sizes past a few hundred documents those stop being the same thing.

Retrieval is a declared role with a fallback ladder (`doctrine/08-instruments.md`, K-7). This is how
the role is exercised without lying to yourself about what it returned.

## Do

1. **Say what you are looking for before you search.** One sentence: *"the document that owns X."*
   Written first, it is a falsifiable target. Written after, whatever came back will match it —
   which is not retrieval, it is confirmation with a search box in front of it.

2. **Pick the rung deliberately, and know which way each one fails.** They fail in *opposite*
   directions and the difference matters more than the ranking:

   | Rung | Fails by | Use when |
   |---|---|---|
   | Relevance ranking (semantic, embedding) | returning a **plausible wrong** answer, silently | you do not know the vocabulary the answer is written in |
   | Exact match (full text, regex) | returning **far too much**, loudly | you know a distinctive string |
   | Structural navigation (listing, index, table of contents) | returning nothing, obviously | you want *this project's own* thinking and know roughly where it lives |
   | A person who remembers | being unavailable, or wrong with confidence | nothing else has a rung |

   **The top rung is the only one that fails quietly**, so it is the one to distrust when a corpus
   is large or mixed. When you want what the project itself decided, prefer structural navigation
   over a semantic sweep — you are not looking for *related* material, you are looking for a
   specific document, and ranking will happily give you the first at the cost of the second.

3. **Scope before you search, not after.** A query against the whole corpus in a corpus that
   contains foreign material is a query mostly against the foreign material. Name the subtree.
   **Imported corpora are queried by explicit path**, never by a bare term.

4. **Cap the result set, and treat a capped result as a floor.** *"The first twenty of an unknown
   number"* is not an inventory, and every count derived from it carries that scope (L-4). An
   uncapped query against a large corpus does not fail — it returns more than you will read, and
   what you do not read is indistinguishable from what was not there.

5. **Check the rank of what came back before you quote it.** Where documents record their own
   precedence, read that field first. A search engine ranks by relevance; **relevance is not
   authority**, and the highest-scoring document is frequently the most detailed rather than the
   most senior. This step exists because a corpus quoted a `precedence: 6` document against a
   `precedence: 2` ruling while the rank was sitting in the file's own frontmatter.

6. **Before concluding an absence, change instrument.** *"Not findable"* and *"not written"* are
   different claims and only one of them is about the project. A negative from one rung is a
   negative about that rung. Drop to structural navigation and look with your eyes before writing
   down that something does not exist.

7. **When retrieval obstructs you, record it as an observation.** Not as a bad afternoon. A search
   that returned 364,155 characters is a **measurement of the instrument**, and it is the only
   evidence that will ever exist for K-7 in this project. Log it with the query and the figure.

## Do not

- **Do not treat a semantic score as a confidence token.** `0.611` is a distance in someone's
  embedding space. It is not `CONFIRMED`, it does not become `CONFIRMED` by being high, and the six
  tokens mean what `doctrine/02-epistemics.md` says they mean.
- **Do not report a count taken from a capped search** without its scope. This is the most common
  way an `ASSERTED-UNIVERSAL` claim enters a record while looking like a measurement.
- **Do not repair a search by widening it.** A query that returned too much and a query that
  returned the wrong thing want opposite corrections; widening the second is how a session ends up
  reading a vendor's documentation to answer a question about its own architecture.
- **Do not conclude the project is silent on something** from one instrument (step 6).
- **Do not adopt an error message's framing as a property of your environment.** An error reports
  what one component believed at one moment. *"Compiled without embeddings"* was read as *the
  feature is absent from this installation* and was actually *the wrong one of two binaries is
  pinned* — the other, same version number, larger, sat unused on the same machine. Four hours and
  five documents later the operator refused the claim and it took twenty minutes to break
  (`O-54`). **Retrieval providers are frequently more than one process**, and an error relayed
  through the one you can see is often about the one you cannot. Follow the error to the component
  that raised it before you write down what it means.
- **Do not quote another corpus's diagnosis as settled.** L-11 says trust no quoted *number*,
  including your own project's. The same applies to a quoted *cause*, and it is less obvious
  because a diagnosis arrives already reasoned. `O-55` measured a false diagnosis travelling from a
  framework into a consuming project and **overriding a correct local finding**, because consumers
  defer upstream by design. A cause you did not derive carries the grade of *the derivation you did
  not see*.

## Blast radius

**Friction** — a bad search costs the query, and you notice, because you did not find the thing.

**Conflagration** in one specific case, and it is the case that produced this ritual: **retrieval
fails hardest while you are using it to repair something.** A correction in progress is exactly when
you are searching for material you have not read and cannot recognise the absence of. Two of the
three measured instances behind K-7 obstructed a correction already underway. If a search is part of
a repair, its failure is not a snag — it is a second defect landing on top of the first, and the
repair will be published as complete.

## Record

- **The query, the rung, and the scope**, wherever the finding is written. *"Searched for X"* is not
  a method; *"regex `X` over `spec/**`, capped at 20, 14 returned"* is.
- **`OBSERVATIONS`** — any instance of retrieval failing, obstructing, or returning foreign material
  above the project's own. With the figure. These are the attestations K-7 does not yet have.
- **`CAPABILITY INVENTORY`** — if the foreign share has moved, re-measure it there and re-date the
  file (K-4). An index that has grown is an environment that has changed, even though nothing
  happened on any particular day (`O-44`).
- **A claim drawn from a capped or scoped search carries that scope** (L-4). *"Across the 40 files
  under `spec/`"* is a scoped claim. *"Across the corpus"*, from the same search, is false.
