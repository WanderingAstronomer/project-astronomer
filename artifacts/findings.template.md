# FINDINGS — `<project name>` — `<pass / stage name>` — `<YYYY-MM-DD>`

> **Doc class:** frozen. **Point-in-time record — do not edit to reflect later truth.**
> Corrections arrive as **addenda** below, dated, which state plainly that they do not revise
> what is above them. A findings document that is quietly updated becomes a document that appears
> to have been right all along, which destroys its only real value: evidence of what was known,
> and when.
>
> Where this document and the living specification disagree, **the living document wins on fact
> and this one stands on the historical record.** Both are true and neither file changes.

**Required at:** **Standard** — from the point where what the world *is* has to be separable from
what you decided about it.

---

## Verdict

# `<GO | NO-GO | GO WITH CONDITIONS | UNRESOLVED>`

`<One paragraph. What was decided and on what basis. If conditional, the conditions are numbered
below and each is checkable by someone who was not here.>`

**Gate:** `<the pre-registered criterion this was judged against, quoted exactly as it was
written before the observation — L-9>`
**Measured:** `<what actually came back>`
**Against:** `<pass | fail | the gate itself did not survive contact — see below>`

The verdict goes first because a findings document read from the top is read by someone deciding
whether to act. Burying the verdict under the evidence is how a `NO-GO` gets softened by page
three — not deliberately, but because the writer has spent longer with the evidence than with the
conclusion, and it shows.

**If the gate itself turned out to be wrong, say so here and demote it.** The most instructive
failure in the source corpus was a pre-registered threshold lifted from a friendlier measurement
condition than the one actually used — every candidate failed a gate that was itself the
artifact. Pre-registration protects you from moving the goalposts. It does not protect you from
having put them in the wrong field.

---

## Evidence tiers

Every finding is labelled with the tier of evidence supporting it. Conflating tiers overstates
the work, and it does so invisibly, because each individual sentence stays true.

| Tier | Means | May be used to |
|---|---|---|
| `T1 DIRECT` | the thing itself, observed or measured under the conditions the claim is about | assert the finding |
| `T2 PROXY` | measured through a stand-in that cannot fail in every way the real thing can | assert the finding **with the proxy named** and the gap stated |
| `T3 DERIVED` | reasoned from the source, no independent measurement taken | propose, not assert |
| `T4 REPORTED` | someone's account of it; inherits the strength of its source and no more | **hypothesis only** — never promoted to a factual finding on its own |

`<Adjust the tier names to this project if it has better ones — but keep the count small, keep
them defined here and only here (L-14), and keep the bottom tier explicitly barred from
promotion. The bottom tier is the one that gets quietly upgraded.>`

**Coverage is reported honestly.** A cell with two observations appears in the table with a two
next to it. It is not omitted. Omission reads as *no signal*; a visible small number reads as
*not yet enough*, which is what is true.

---

## Findings

<!--
  Finding shape. Numbered permanently — F-<n> is an address and is never reused.

  ### F-<n> — <the finding, stated as a conclusion, not a topic>
  **Confidence:** `<token>`
  **Evidence tier:** `<T1|T2|T3|T4>`
  **Scope:** <the conditions under which this holds. Mandatory — L-4>
  **Method:** <how this was established: what was done, in what order, by whom, with what
    instrument, and what would have made it come out differently>
  **Evidence:** <citations precise enough to return to>
  **Contradiction surface:** <what would directly refute this>
  **Rests on:** <F-n / O-n / D-n this depends on — an inference must name its inputs>
-->

### F-`<n>` — `<the finding>`

**Confidence:** `<one of the six confidence tokens — see doctrine/02-epistemics.md. Do not
abbreviate the set here; a four-token version of this slot shipped in the seeded corpus and the
tokens it dropped were UNVERIFIED and ACCEPTED>`
**Evidence tier:** `<T1|T2|T3|T4>`
**Scope:** `<conditions under which this holds>`
**Method:** `<what was done>`
**Evidence:** `<citations>`
**Contradiction surface:** `<what would refute this>`
**Rests on:** `<ids>`

`<Body — the reasoning, including where your first hypothesis was wrong.>`

The `Method:` line is not a formality and it is not the same as the evidence citation. Evidence
says *where you looked*; method says *what you did*, which is what a reader needs in order to
decide whether the finding could have come out any other way. A finding whose method cannot be
stated in three sentences was not established — it was noticed.

**Scope is mandatory.** A finding asserted without conditions is not strong, it is **unscoped**,
which is a defect state: mark it `ASSERTED-UNIVERSAL` and route it to scrutiny rather than
accepting it. And do not inherit the *audience's* attributes into the claim's scope — a
conclusion drawn for one context is a universal claim unless it actually depends on that context.
Confusing the two manufactures precision that was never asserted, in the direction of looking
more rigorous.

**If this document ranks anything by how often it was asserted, repeat the caveat at the point of
use:** frequency measures agreement among sources, not correctness. Nothing in a count crosses
that gap, and a ranked list without the caveat beside it will be read as a ranking of
effectiveness — every time, by everyone, including its author.

---

## Refuted and retracted

Kept, marked, with their original numbering and dates. **An audit that quietly drops its wrong
calls cannot be trusted about its right ones** — and if the symptom recurs, a retracted finding
means you already have a first sighting on the books instead of a fresh discovery.

### F-`<n>` — `REFUTED` — `<the claim as originally stated>`
**Originally recorded:** `<date>`, at `<confidence>`, on `<what basis>`
**Refuted by:** `<what killed it, cited>`
**What it cost:** `<what was built, planned, or believed on top of this before it fell>`

---

## Key decisions

Decisions taken during this pass. Each is already in the ledger with its full reasoning — this is
a pointer list, not a second home for them, because a decision with two homes has two versions
within a year.

| ID | Decision | Owner |
|---|---|---|
| `<D-n>` | `<one line>` | `<[operator] / collaborator>` |

---

## Open items carried forward

Unresolved at the close of this pass. Carried into `<the next pass / the triage board / the
ledger>` — this list is the handoff, and an item that is not on it has been dropped, whatever
anyone remembers.

- [ ] **`<Q-n / F-n>`** — `<what is open>` · *owed to:* `<human | next pass | external>` ·
  *blocks:* `<what>`
- [ ] **`<id>`** — `<…>` · *owed to:* `<…>` · *blocks:* `<…>`

**"Owed by a human" is an expected and acceptable outcome, not a gap in the work** (L-15). Where
the work reached something requiring identity, custody, acceptance, a physical fact, or a
preference, the honest result is a blocked item — not a plausible substitute produced to make the
list look finished.

---

## What was not verified

`<Stated plainly. What this pass did not check, could not check with the instruments available,
or deliberately deferred. Where verification was weaker than the claim needs, say so and record
the debt rather than letting the weaker check pass silently as the stronger one.>`

- `<claim>` — `<why it was not verified, and what would verify it>`

---

## Addenda

> **Convention.** An addendum is appended below with its own live date. It **does not re-run or
> revise anything above it** — it only notes what has since become true, so that this document
> does not mislead about the current state. Nothing above this line is ever edited, including
> anything now known to be wrong.

### `[<YYYY-MM-DD>]` — `<addendum label>`

`<What has changed since this document was frozen. Explicitly: which findings above are now
superseded, and by what. State the supersession by name — recency alone does not win (L-2).>`

---

## Worked example

*One entry from the damp-house observation window used throughout these templates. Domain is
illustrative only.*

### F-2 — The utility-room wall is wet from an intermittent supply-joint leak, not from rising damp.

**Confidence:** `CONFIRMED`
**Evidence tier:** `T1 DIRECT`
**Scope:** the utility-room wall behind the washing machine, in the condition observed between
2026-03-02 and 2026-03-08. Says nothing about the rear elevation, the back bedroom, or the
building's damp-proof course generally — those were separately observed and remain separately
unresolved.
**Method:** the joint was wrapped in dry tissue and the machine run through one full cycle; the
tissue was saturated at the joint and dry 100mm to either side. The test was then inverted — the
feed isolated and the wrap left in place for two hours with no machine use — and the tissue
stayed dry. The inversion is the load-bearing half: the first run alone would have been
consistent with water arriving at that height from any source, and could not have failed if the
hypothesis were wrong.
**Evidence:** O-4 (baseline readings 24.1 / 23.8 / 24.4 in pin mode, with an off-patch control at
9.2); photographs `<ref>`, `<ref>`; test log 2026-03-08T10:00Z.
**Contradiction surface:** a wall that stays at ~24 after the joint is remade, or an off-patch
control reading that rises to match, refutes this and puts rising damp back in play.
**Rests on:** O-4, and the instrument-error note recorded there — that meter cannot distinguish
current damp from historical damp that has since dried, so the reading alone never could have
settled this. The wrap test was necessary precisely because the instrument could not fail in the
right way (L-12).

The initial read at O-4 offered rising damp and the joint leak as equally plausible, and the
tide-marked edge that triggered the rising-damp reading turns out to be characteristic of both.
That initial read was not wrong to write down; it was wrong to act on, and it is recorded here as
half-refuted rather than quietly dropped.
