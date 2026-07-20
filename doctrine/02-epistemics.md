# 02 — Epistemics

This is the part of Astronomer that does the work. Everything else is scaffolding around it.

The framework exists for subjects you cannot experiment on. In that setting the limiting factor
is never how much you observe — it is whether, six months later, you can tell what you *saw*
from what you *concluded*. All four source projects hit that wall and all four independently
built the same instrument: **typed claims**.

---

## The atomic unit is a claim, not a document

The record is not "the session," "the day," or "the article." It is the individual assertion,
extracted, with its own type, scope, and confidence.

> "The atomic record is a **claim**, not a post. A single comment can yield zero, one, or
> several claims." — DD

This matters because aggregation only works over comparable units. A day's log entry containing
four observations and two conclusions cannot be counted, sorted, or contradicted. Six typed
claims can.

A claim carries, at minimum:

| Field | What it holds | Why it is mandatory |
|---|---|---|
| `assertion` | the claim in one sentence | forces one claim per record |
| `type` | its epistemic class (below) | tells you what it is worth |
| `scope` | the conditions under which it holds | L-4 — unscoped is flagged, not trusted |
| `confidence` | one of the six tokens — see [below](#confidence-tokens) | L-3 — a field, not a tone |
| `source` | where it came from, precisely enough to re-check | lets a future reader re-derive it |
| `observed_at` | live timestamp | ordering, and lag analysis |

`source` is the field most often softened and should not be. It exists so that a claim can be
returned to its origin and re-verified — which is the only defense against a corpus that
gradually accumulates its own conclusions as if they were inputs.

---

## The epistemic ladder

Type is not topic. Topic tells you what a claim is *about*; type tells you what it is *worth*
and what it takes to promote it.

Both projects that built one converged on cutting the categories by epistemic status rather
than subject matter. The generalized ladder:

| Type | What it is | How it may be used |
|---|---|---|
| `OBSERVATION` | something directly seen or measured | may be counted, aggregated, and cited as fact about the instance |
| `OUTCOME` | a measured before/after on a specific intervention | the highest-value type; earns full scrutiny |
| `HEURISTIC` | an asserted general rule | context-contingent — **scope is load-bearing here**; the workhorse type |
| `OPINION` | a preference or value judgment | aggregates into sentiment; **may never be promoted to a factual finding** |
| `CITED` | an appeal to external authority or data | inherits the strength of its source, no more |
| `INFERENCE` | a conclusion drawn from other claims | must name the claims it rests on |
| `TRANSITIONAL` | asserts nothing | the mandatory null bucket |

Two design rules make this work, and both were learned rather than designed:

**The null bucket is mandatory.** `TRANSITIONAL` exists so that a classifier — human or model —
is never forced to manufacture signal from noise. FR made this explicit and then monitored its
share as a health metric: too little means the extractor is hallucinating claims from filler;
too much means it is under-firing. DD independently set a ceiling on its equivalent for exactly
the same reason. **The rate of "nothing here" is a live readout on whether your classification
is working at all**, and it costs nothing to watch.

**The ladder is exhaustive and exclusive.** Exactly one type per claim. If something does not
fit, the ladder is wrong and gets amended by decision — it does not get a second type.

---

## Scope, and the universal-claim trap

Every claim declares the conditions under which it holds. A claim asserted without conditions
is not *strong* — it is **unscoped**, which is a defect state, and it is marked
`ASSERTED-UNIVERSAL` and routed to scrutiny rather than accepted.

The failure this prevents, in DD's own words: without a mandatory scope the corpus "would
flatten *this worked for me, a 27M* into *this works*."

There is a second, subtler trap that project had to write an explicit rule against, and it
generalizes cleanly: **do not inherit the audience's attributes into the claim's scope.**
Advice given *to* a 28-year-old is a universal claim unless it depends on being 28. Confusing
the recipient's context for the claim's context manufactures precision that was never asserted —
and it manufactures it in the direction of looking more rigorous.

---

## The interrogation frame

FR applied five fixed questions to every claim that qualified for deep treatment. They are
domain-independent and are the most portable single tool in this framework:

1. **Multi-context** — in what contexts is this true, false, or partial?
2. **Dependencies** — what must be true for this to hold?
3. **Contradiction surface** — what would directly contradict this?
4. **Domain scope** — what assumptions about the domain must hold?
5. **Temporal validity** — is this time-invariant, or when does it expire?

Question 3 is the one that earns its place. A claim whose contradiction surface you cannot state
is a claim you cannot test, and writing that surface down is what turns a belief into a
hypothesis. Question 5 is the one most often skipped and most often needed: a great many claims
are true and *expiring*, and nothing in an unaugmented record marks the difference between a
finding and a finding's corpse.

---

## Consensus is not effect size

The most-repeated caveat across the corpus, and the one DD restated in its findings document, in
every derived recommendation, and again at each point of use:

> "Consensus measures agreement among advice-givers, not correctness."

How often a claim appears is a fact about the *sources*. Whether it works is a fact about the
*world*. Nothing in a frequency count crosses that gap, and a report that presents a ranked list
without saying so will be read as a ranking of effectiveness — every time, by everyone,
including its author.

Where the two are both tracked, they are separate columns with separate names, and the caveat is
repeated where the numbers are used rather than once in a preamble nobody rereads.

---

## Grade evidence honestly, including its coverage

Two rules, both attested:

**Tier the evidence and never conflate tiers.** DD ran a two-tier split — *artifact-grade* (real
artifacts directly observed) against *attitude-grade* (people reporting on them) — and labeled
every finding with which tier supported it, on the reasoning that "conflating them would
overstate the study." An external reference set went further and ranked prior work as
peer-reviewed / first-party / anecdotal, with the anecdotal tier explicitly marked
**hypotheses only**.

**Report thin coverage as thin.** From DD's charter: coverage per cell is reported honestly —
"thin cells are labeled thin, not silently omitted." A subgroup with two observations is not
absent from the table; it is present, with a two next to it. Omission reads as *no signal*;
a visible small number reads as *not yet enough*, which is what is true.

---

## Cost-gate your scrutiny

Not every claim earns expensive verification, and pretending otherwise means either
verifying nothing properly or stalling.

DD gated by type: `OUTCOME` claims and consensus-backed `HEURISTIC` clusters got the full
adversarial pass; pure `OPINION` aggregated into sentiment and was *never eligible* for
promotion to a factual finding. FR gated the same way — only three of its ten types qualified
for deep interrogation, about 42% of the corpus.

The rule generalizes: **the ladder is also a triage function for where to spend attention.**
Decide the gate once, in the charter or the ledger, rather than per claim in the moment — which
is where motivated reasoning enters.

---

## Confidence tokens

Fixed vocabulary. Typed, not prose (D-015). A reader skims past "probably"; they cannot skim
past a label in a field position.

| Token | Meaning |
|---|---|
| `CONFIRMED` | independently verified against the source; cite where |
| `UNVERIFIED` | recorded, plausible, not checked — the default for anything new |
| `REFUTED` | actively disproven; **kept in the record** (L-6) |
| `PROVISIONAL` | accepted for now, with a named condition that would reopen it |
| `UNRESOLVED` | tried to determine, could not; the honest terminal state |
| `ACCEPTED` | known to be imperfect and deliberately kept; the reason is stated |

`UNRESOLVED` deserves defending. In astronomy, *unresolved* is a respectable result — the
instrument reached its limit and the observation reports that limit rather than guessing at
structure. Most records have no such category, so the ambiguous case gets rounded to whichever
neighbouring state the writer found more comfortable. Give it a name and it stops disappearing.
