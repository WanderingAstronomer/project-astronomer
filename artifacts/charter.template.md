---
record_class: living
precedence: 1
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <the-mission>
  - <the-invariants>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# CHARTER — `<project name>`

> **Doc class:** living. **Corpus status:** `<PROVISIONAL | VALIDATED | ...>`
>
> This is the top of the authority stack. If anything else in this corpus conflicts with this
> charter, **the charter wins.** Amend it deliberately, with a dated entry in
> [`DECISIONS.md`](DECISIONS.md) — never silently.

**Required at:** **Lite** — every tier requires it; it is the document that makes a contradiction
detectable at all (L-1).

<!--
HOW TO USE THIS TEMPLATE
  Copy to CHARTER.md at the root of your project. Fill every angle-bracket slot. Do not delete
  a section because it looks like ceremony — the precedence block and the vocabularies are the
  two that feel most optional and cost the most when missing (doctrine/00, L-14).
  Write this before the first observation. A charter written after the fact is a rationalization
  with a header.
-->

## Mission

`<One paragraph. What this project is for, stated so that an outsider could tell whether it had
succeeded. Not what you will do — what will be true when it is done.>`

The measure of success is not `<the thing easily mistaken for success here: activity, volume,
completeness, how good the record looks>`. It is `<the outcome that would still count if nobody
were watching>`.

## Scope

**In scope**

- `<area — a noun phrase, not a task. One line each.>`
- `<area>`
- `<area>`

**Out of scope (for now)**

- `<area>` — `<why it is out.>` (`<D-n>`)
- `<area>` — `<why it is out.>` (`<D-n>`)

A scope exclusion without a stated reason gets re-litigated every month by whoever did not hear
the original argument, and eventually one of those re-litigations succeeds quietly. The reason
is the part that holds; the exclusion alone is just a preference with a bullet point.

## Invariants — do not violate

1. **`<Invariant, stated as an imperative.>`** `<The failure it prevents, concretely. Not "for
   quality" — the specific bad outcome.>` (`<D-n>`)
2. **`<Invariant.>`** `<Why.>` (`<D-n>`)
3. **`<Invariant.>`** `<Why.>` (`<D-n>`)
4. **No fiction.** A document describing something not yet built, not yet measured, or not yet
   decided says so, in that document, at the top. (`<D-n>`)

Every invariant carries the decision that established it. An invariant with no decision ID
behind it is a preference promoted by repetition, and it will lose the first argument it is in —
which will be the argument where following it is expensive, because that is the only kind of
argument invariants have.

## Precedence

Higher wins. When two artifacts disagree, the lower one is **wrong** — not "in tension," not "a
different perspective." It is wrong, and it gets corrected or annotated.

```
1. CHARTER            why this exists; the invariants. Amended only by explicit decision.
2. DECISIONS          what was decided, when, and by whom. Append-only.
3. SPECIFICATION      what is currently true. Living; rewritten to match reality.
4. FINDINGS           what was learned, at the time it was learned. Frozen.
5. OBSERVATIONS       what was seen, verbatim. Frozen, append-only.
6. EVERYTHING ELSE    notes, drafts, plans, conversation.
```

`<Adopt unchanged, or state your deviation here with the reason. Declaring the default
explicitly is what makes it enforceable — an assumed order is not an order.>`

**This stack orders *your* artifacts. Astronomer's own documents sit one layer above it** (D-016):

```
FRAMEWORK LAYER    doctrine → rituals          ships with Astronomer; domain-neutral
                        ↕
PROJECT LAYER      charter → decisions → …     yours; domain-specific
```

This charter is supreme **within this project** — it decides scope, invariants, vocabularies, and
tier. It **cannot repeal a law.** A project that needs to break a law does not amend its own
charter; it amends Astronomer, in Astronomer's ledger, because an exception that applies to one
project only is not an exception — it is a mistake. Tiers change which artifacts are required;
they never relax a law (D-008).

Three rules govern reading this stack.

**Reality outranks all of it.** The stack orders documents against documents. It does not order
documents against the world. Where a document and the actual `<subject: system, body, corpus,
site, instrument>` disagree, the document is wrong and gets settled to reality, no matter how
high it sits.

**Frozen records are exempt from correction, not from being outranked.** A finding from
`<month>` that later turns out to be wrong is not edited. It stands, annotated. The living
specification carries the current truth; the frozen record carries what was believed at the
time, which is itself a fact worth keeping.

**Namespacing.** A bare `D-<n>` in this corpus resolves to **this project's ledger only**.
References to another project's ledger are prefixed: `<PRJ>-D-<n>`. This looks like pedantry
until two ledgers in the same corpus both reach `D-7`, at which point every historical reference
becomes ambiguous and the supersession chain silently stops working.

## Vocabularies

Fixed, small, and each with **exactly one home** — every other document in this project renders
from that home rather than restating it (L-14). Restated definitions drift apart silently, and
you will aggregate across them without noticing.

The homes are split by layer (D-016). **Confidence is framework-level**: its home is doctrine, and
this charter points at it. **Severity, effort, change size, and your type vocabulary are
project-level**: their home is this section, and everything else in your project points here.

**Confidence** — a typed token in a field position, never a tone in the prose (L-3, D-015).

**Six tokens: `CONFIRMED` · `UNVERIFIED` · `REFUTED` · `PROVISIONAL` · `UNRESOLVED` · `ACCEPTED`.**

**Their single home is `doctrine/02-epistemics.md`, and this
charter deliberately does not restate their definitions** — it points at them (AMENDS D-015).
Restating them here would put a second copy in the corpus, and a second copy is how a vocabulary
drifts. That is not a hypothetical: the seeded framework shipped **three different memberships of
this exact vocabulary within hours of writing the law against it** (L-14), and the token that went
missing each time was `ACCEPTED` — the one that records *a known imperfection deliberately kept*,
which is precisely the category an author summarizing their own work forgets, because it is the
one that makes them look worse.

`<If this project genuinely needs a different set, that is an amendment to Astronomer's doctrine
with an entry in Astronomer's ledger — not a local redefinition here. A vocabulary that varies
per project cannot be aggregated across projects, which is most of the reason to have one.>`

**Severity** — a property of the symptom. Distinct from **blast radius** (Friction /
Conflagration), which asks how far something reaches rather than how much it matters (D-018); see
`rituals/README.md`. The two are orthogonal — a `minor` item is a
Conflagration if six decisions rest on it.

| Token | Means |
|---|---|
| `stop` | `<work halts until this is resolved>` |
| `major` | `<materially wrong; scheduled deliberately>` |
| `minor` | `<real, small, batched>` |
| `question` | needs a human decision — a *disposition*, not a magnitude |

**Effort** — wall-clock bands, not points. Points are unfalsifiable; a band is a prediction you
can be wrong about.

| Band | Means |
|---|---|
| `S` | `<minutes>` |
| `M` | `<an hour-ish>` |
| `L` | `<multi-hour, or needs design care before it can start>` |

**Change size** — declared *before* starting: `minimal` · `medium` · `large`. Re-classing upward
mid-flight is expected and fine. Silently exceeding the declared class is not.

**Doc class** — `living` · `frozen` · `append-only` · `disposable`, stated at the top of every
file. **Framework-level, like confidence**: the home is
`doctrine/05-the-record.md` and this charter points at it rather
than defining it. `append-only` is a class in its own right, not a flavour of frozen (D-019) — it
is the one your ledger and your observation log take, and the one a three-member version of this
list quietly dropped in six places for four days after it was added.

## Cost gate for scrutiny

`<Which claims earn expensive verification, decided once, here.>` Not everything earns an
adversarial pass, and pretending otherwise means either verifying nothing properly or stalling.
Set the gate in advance: a gate decided per item, at the moment of decision, is a gate decided by
how much you want the item to be true.

- Full adversarial verification: `<claim types, e.g. measured outcomes; anything a downstream
  decision rests on>`
- Recorded and monitored, not interrogated: `<claim types>`
- Never eligible for promotion to a factual finding: `<claim types, e.g. preference and
  sentiment>`

## Definition of done (`<v0>`)

`<Project>` `<v0>` is complete when all of the following are true. Each is a testable predicate,
not a feeling. Where a predicate contains a number, the number is pre-registered here **before**
the observation that will be measured against it (L-9) — and it is calibrated on the condition
you will actually measure under, not on a ceiling from a friendlier condition.

1. `<Predicate. Must be checkable by someone who was not involved.>`
2. `<Predicate with a pre-registered number: "≥ <n> <units>, measured <how, under what
   conditions>">`
3. `<Predicate.>`
4. `<Predicate.>`
5. **`<The falsifier: the observation that would mean this whole approach is fake.>`** `<Not the
   threshold for failure — the result that would mean the measurement itself cannot tell you
   anything. A definition of done without one of these can only ever confirm.>`

**Status:** `<Conditions 1–n are met as of <date>. Condition <n> is not met and is the only thing
standing between this corpus and <next status>.>` State this honestly and in public. A definition
of done whose status is not tracked is a wish list.
