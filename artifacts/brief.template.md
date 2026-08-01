---
record_class: disposable
precedence: 6
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <the scope of this one piece of work>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# BRIEF — `<lane id>` — `<scope name>`

> **Doc class:** disposable until executed, then frozen. On completion, banner it
> `EXECUTED <YYYY-MM-DD> — kept as a reusable template. Re-baseline before re-running.` and keep
> it. The instinct to delete a finished plan is strong and wrong: the brief is the only surviving
> statement of what you **intended**, which is exactly what you need when the outcome disappoints
> and you are working out whether the plan failed or the execution did.

> **A brief is a self-contained work order for someone who cannot ask you a question.** Every
> ambiguity you leave here becomes a judgement call made by someone with less context than you,
> at a moment when stopping to ask is not available.

> **Your brief is a brief, not a solution.** Hand over symptoms, verified facts, and labelled
> hypotheses. Do **not** run a large precursor investigation and hand over the answer — that
> anchors an independent executor on a conclusion they did not derive and therefore cannot
> properly refute. The value of a second mind is entirely in its independence, and pre-solving
> spends it before the work starts.

**Required at:** **Full** — from the moment work is handed to someone who cannot ask you a
question mid-flight.

---

## 1. Read this first

**Shared preamble:** [`<path/to/_SHARED-PREAMBLE.md>`](<path>) — **required reading, in full,
before starting.**

Included by reference and identical in every brief on purpose. It holds the rules that apply to
all work here, each with the failure that produced it, so the rule is understood rather than
merely obeyed. If it conflicts with anything below, **this brief wins on scope and the preamble
wins on method** — and if that ever feels ambiguous in practice, that is a defect in one of the
two documents and it should come back in your report.

---

## 2. Why this scope exists

`<Two or three paragraphs. What is wrong, what it costs, and why this particular slice was cut
out of the larger problem. Causal, not administrative — "the readings from the north site have
been unusable since the sensor was moved, and every seasonal comparison downstream is drawing on
them" rather than "north site cleanup."`

`An executor who understands why a scope exists will make better decisions at its edges than one
who has only been told where the edges are, and the edges are where all the judgement calls
happen.>`

**Governing decisions:** `<D-n, D-n>`
**Originating observations:** `<O-n, O-n>` · **Triage items:** `<A1, B3, C-2>`

---

## 3. Verified current state

**Everything in this section has been checked against the actual subject and is cited.** Treat it
as fact — but re-measure anything you are about to change (L-11), because these numbers were true
when they were written and that is the only guarantee they carry.

- `<fact>` — verified `<how>`, at `<citation precise enough to land on>`, `<date>`
- `<fact>` — verified `<how>`, at `<citation>`, `<date>`

### UNVERIFIED — hypotheses, not facts

**Nothing in this section has been established.** It is written down because it is the best
current guess and withholding it would waste your time — not because it is true. Where your work
touches one of these, **your job includes trying to refute it**, and a refutation is a successful
outcome that belongs in your report.

- `UNVERIFIED:` `<hypothesis>` — `<what suggested it>` · **would be refuted by:** `<what>`
- `UNVERIFIED:` `<hypothesis>` — `<what suggested it>` · **would be refuted by:** `<what>`

The separation of these two sections is the single most load-bearing thing in this document. Run
together, in the same voice, a verified fact and a plausible guess become indistinguishable within
a week — and the guess is the one that gets built on, because it explains more.

---

## 4. What makes this harder than it looks

The traps, named. Each one is here because it has already caught someone, or because the shape of
the work makes it near-certain.

- **`<Trap.>`** `<Why the obvious approach fails here, specifically.>`
- **`<Trap.>`** `<…>`
- **`<Trap.>`** `<…>`

`<If you genuinely cannot name a trap, say "none identified" rather than padding this section —
but be suspicious of that answer. A scope with no traps is usually a scope that has not been
looked at closely enough to have any yet.>`

---

## 5. Scope

### IN — numbered

1. `<deliverable, stated as an outcome>`
2. `<deliverable>`
3. `<deliverable>`

### OUT — numbered

1. `<explicitly excluded>` — `<why, and where it is being handled instead>`
2. `<explicitly excluded>` — `<why>`
3. **Anything not listed under IN.** Scope is a whitelist, not a starting point.

Numbered so that your report can refer to them by number and so that a partial delivery is
legible — "1 and 2 complete, 3 blocked on `<Q-n>`" is information; "mostly done" is not.

---

## 6. Fences

### What you own

`<Enumerate. Every item below has exactly one owner, and for the duration of this work it is
you.>`

- `<item / area / file / surface>`
- `<item>`

**If this brief does not list something, you do not own it.**

### What another lane owns — do not touch

| Item | Owner | If you need something here |
|---|---|---|
| `<item>` | `<lane id>` | record it in your report, cited, and continue |
| `<item>` | `<lane id>` | `<…>` |

### When you find a problem outside your fence

**Do not fix it.** Record it in your report with a citation and keep going. This feels wasteful
and is not.

A fix landing outside its fence is precisely the merge-cleanly-but-wrong class: two
independently correct changes that combine into a wrong result which nothing flags. The source
corpus's collision analysis found eleven conflict sets and **eight of them were that class** —
each of which passed every check it was subjected to. The same analysis concluded that against a
proposal for ten concurrent lanes, *three concurrent sessions is the honest safe maximum, and two
is the recommended default* — capacity is bought by removing collisions, not by tolerating them.

---

## 7. Acceptance criteria

Pre-registered, here, before the work starts (L-9). Each is a predicate someone who was not
involved can evaluate. "Works correctly" is not one.

1. `<criterion — numeric or binary, with the condition it is measured under>`
2. `<criterion>`
3. `<criterion>`
4. **Baseline recorded.** You measured `<what>` yourself before changing anything, and your
   report opens with baseline-versus-final. Not quoted from this brief — **measured by you.** Any
   number in this document is stale from the moment it was typed, including the ones above.
5. **Every check you added or relied on has been broken on purpose and confirmed to fire.** A
   check that has never failed is a hypothesis about a check.

**The falsifier:** `<the result that would mean this whole approach is wrong — not that the work
failed, but that the framing was mistaken. If you hit it, stop and report; do not route around
it.>`

**Change size, declared before starting:** `<minimal | medium | large>`. Re-classing upward
mid-flight is expected and fine — say so in the report. Silently doing more than this is not:
bigger scope is an explicit re-plan, not an in-session expansion.

---

## Return

Your report follows the six-section contract in `report.template.md`. Two
of its sections are the ones that make a report evidence rather than a pitch, and both are
mandatory even when empty:

- **Defects found inside your own work** — every session in the source corpus's largest
  concurrent run found one this way, without exception. A report with none has almost certainly
  not looked.
- **What was not verified** — where *"owed by a human"* is an expected and acceptable outcome,
  not a failure to finish.

**Do not ask follow-up questions.** If you hit an ambiguity, apply decide-document-flag: make the
call, implement it, document it under a heading that cannot be missed, and flag it as *"judgement
call — reverse this if wrong."* The hard constraint is that **every such call must be cheap to
reverse; if it is not cheap to reverse, take the conservative option and say why.** A stalled
session is worse than a documented judgement call.
