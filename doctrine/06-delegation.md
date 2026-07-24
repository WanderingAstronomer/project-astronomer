# 06 — Delegation

Astronomer assumes you are working with collaborators — AI, human, or both — and that the
failures of delegation are structural rather than personal. A capable collaborator given an
ambiguous boundary will produce confident, well-executed work in the wrong place.

---

## Roles

| Role | Owns | Explicitly does not |
|---|---|---|
| **Operator** | The subject. Every judgement a collaborator cannot make. Sequencing and timing. The non-delegable categories below. | Root-causing every item themselves; writing their own briefs |
| **Coordinator** | Documents and governance: briefs, ledgers, triage boards, sign-off. Verifying returned work against sources, read-only. | **Implementing.** Delegating implementation. Pre-solving a brief before handing it over |
| **Executor** | One fenced scope, end to end: root-cause through to a recorded result. Its own baseline, its own verification, its own report. | Touching another executor's scope; asking questions mid-flight |
| **Verifier** | Re-deriving one claim from scratch and trying to break it. | Confirming by default |

The **Operator / Coordinator** boundary is the one that erodes fastest, because the coordinator
is usually capable of doing the work and it is faster in the moment. VOC's operator had to state
it directly:

> "You really aren't supposed to be doing any of the implementing here. The only thing you're
> supposed to be doing is producing documents and governance… You're just a coordinator for
> other external sessions."

And the corollary, which is less obvious and equally important: **a coordinator must not pre-solve
the brief.** A handoff is a *brief*, not a solution. Running a large precursor investigation and
handing over the answer defeats the purpose of an independent executor — it anchors them on a
conclusion they did not derive and cannot properly refute.

---

## The operator is the instrument

In a domain you cannot experiment on, the human is not the manager of the observation. They
*are* the observation apparatus. VOC states it plainly:

> "They are the instrument here; your job is to be a rigorous recorder first and a surgeon
> second."

Three consequences:

- **Instrument time is the scarce resource.** Design the work so the human's attention is spent
  on what only they can produce, and not on transcription, formatting, or retrieval.
- **The instrument has known error.** Recall degrades, mood colours reporting, and attention is
  uneven. Capture close to the event, verbatim, with conditions attached — that is what an
  observation log is for.
- **A collaborator working *around* the instrument is producing fiction.** When a step needs the
  human and the human is unavailable, the honest outcome is a blocked item, not a substitute.

---

## Work that cannot be delegated

Name it in writing, before the work starts, and stop there when you reach it (L-15).

VOC derived five categories of human-only work — accounts, secrets, external identity, legal
authorship, and physical facts — and observed that recognizing the category tells you *why* it
landed on you, which is what makes it feel like structure instead of an obstacle.

Generalized below, **VOC's five collapse into the first four rows.** The fifth row is an Astronomer
addition and is not inherited from any source project; the note under the table says so. Read the
table as four attested categories plus one proposed one, not as VOC's list restated.

| Category | What it covers |
|---|---|
| **Identity & authority** | Anything requiring you to *be* you — accounts, signatures, consent, authorization |
| **Custody** | Secrets, credentials, keys, records only you may hold |
| **Acceptance** | Terms, liability, authorship — anything that attaches to a person |
| **Physical fact** | Anything requiring a body in a place: a measurement, a specimen, an appointment, a sensation |
| **Preference** | Anything whose correct answer is *what you want* — trade-offs between goods, not between right and wrong |

The last category is an Astronomer addition, not inherited from the source projects, and it is
the one that dominates outside software. *Single-authored — flagged for revision after first
real use.* A collaborator asked to optimize will silently choose an objective function, and it
will be a defensible one, and it will not be yours. Elicit the preference; do not infer it.

**The honest stop is the point.** FR's evaluation directory is empty because its specification
declared the test-question set non-delegable and the project halted there rather than generating
its own questions and grading itself against them. That empty directory is the most honest
artifact in the entire corpus: automation ran to the human bottleneck and stopped, instead of
manufacturing a complete-looking result that measured nothing.

---

## Fences

Every parallel workstream declares **what it owns** and **what it must not touch**. Both lists,
explicitly, in the brief.

> "Every file below has exactly one owner. If your brief does not list a file, you do not own
> it." — VOC

**When you find a problem outside your fence: do not fix it.** Record it in the report, with a
citation, and keep going. This feels wasteful and is not — a fix landing outside its fence is
precisely the "merge-cleanly-but-wrong" class (L-10): two independently correct changes that
combine into a wrong result nothing flags.

VOC's collision analysis found eleven conflict sets, **eight of them that class**. Its
conclusion is the honest one and worth quoting against your own optimism about parallelism:
against a proposal for ten concurrent workstreams, **"Three concurrent sessions is the honest
safe maximum. Two is the recommended default."** Capacity is bought by *removing* collisions,
not by tolerating them — one small refactor that de-conflicts a shared surface buys a parallel
lane permanently.

---

## Briefs

A brief is a self-contained work order for someone who cannot ask you a question. Structure,
proven across seven parallel lanes with zero collisions:

1. Pointer to the **shared preamble** — the rules common to all work, included by reference and
   identical everywhere on purpose
2. **Why this scope exists**
3. **Verified current state**, with citations — then, separately and labelled, the `UNVERIFIED`
   hypotheses
4. **What makes this harder than it looks** — the traps, named
5. **Scope: IN** and **Scope: OUT**, numbered
6. **What you own** / **What another lane owns — do not touch**
7. **Acceptance criteria**

The shared preamble is the innovation. One file, referenced by every brief, holding the rules
that were learned the hard way — with the war story attached to each, so the rule is understood
and not merely obeyed. VOC's carries the note that its rules "are what made the last five-session
concurrent run merge with zero file conflicts, and every one of them was learned the hard way."

The brief hands over **symptoms, verified facts, and hypotheses** — not a solution. Its own
words: *"Your brief is a brief, not a solution."*

---

## Decide, document, flag

When an executor hits an ambiguity mid-flight and the operator is not available:

1. Make the call.
2. Implement it.
3. Document it prominently, under a heading that cannot be missed.
4. Flag it as *"judgement call — reverse this if wrong."*

With one hard constraint: **every such call must be cheap to reverse. If it is not cheap to
reverse, take the conservative option and say why.**

> "A stalled session is worse than a documented judgement call." — VOC

This generalizes past AI collaboration. It is the correct policy for anyone working alone
against a decision that belongs to someone else.

---

## The report contract

Returned work carries six sections. The last three are what separate a report from advocacy.

1. **What was done, and the cause established** — with citations, including where the brief's
   hypothesis was wrong
2. **What was verified, and how** — naming the grade achieved rather than collapsing everything
   into "verified." The grades are defined once, in
   [`04-verification.md`](04-verification.md), and are not restated here (L-12, L-14)
3. **Judgement calls made** — flagged for review
4. **Defects found inside your own work** — VOC's finding is that *every* session in its largest
   run found one this way, without exception. A report with none has almost certainly not looked.
5. **Found outside your fence** — untouched, cited
6. **What was not verified** — where *"owed by a human"* is an expected and acceptable outcome

Sections 4 and 6 are the ones that make a report evidence instead of a pitch. A report that
cannot say what it failed to check is not reporting; it is presenting.
