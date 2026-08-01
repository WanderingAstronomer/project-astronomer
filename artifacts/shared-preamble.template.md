---
record_class: living
precedence: 6
confidence: <one of the six confidence tokens; home is doctrine/02-epistemics.md>
owns:
  - <the-shared-preamble>
verified_by: <who re-derived it, or blank>
last_verified: <YYYY-MM-DD, or blank>
---

# SHARED PREAMBLE — `<project name>`

> **Doc class:** living. **Deploy as `_SHARED-PREAMBLE.md`** — the underscore sorts it to the top
> of the directory, where a file that every other file depends on belongs.
>
> Included by reference into **every** brief, and identical everywhere on purpose. A rule that is
> restated per-brief drifts per-brief, and the drift is invisible because each copy reads fine on
> its own (L-14).

**Required at:** **Full** — created when the second parallel workstream is.

Read this in full before starting. It is not preamble in the ceremonial sense — it is the set of
rules that apply to all work in this project regardless of scope, and **every one of them was
learned the hard way.**

**Each rule carries the failure that produced it.** This is deliberate and it is not decoration
(D-003). A rule without its scar has no defense the first time following it is expensive — and
the only arguments a rule ever has are the expensive ones. The scar *is* the argument; strip it
and you are left with an assertion, which loses.

The war stories below are marked **inherited** where they come from the Astronomer source corpus
rather than from this project. Inherited scars are still evidence — they are just not *your*
evidence, and the distinction matters when someone proposes an exception. As this project
accumulates its own, add them at the bottom under `## Local rules`, each with its incident.

---

## 1. You are an executor, not a coordinator

You own **one fenced scope, end to end**: root-cause through to a recorded result, with your own
baseline, your own verification, and your own report. You do not delegate it, you do not split it,
and you do not widen it.

The inverse also binds whoever wrote your brief: a coordinator produces documents and governance,
and does not implement. If your brief arrives with the problem already solved, something has gone
wrong upstream — say so in your report.

**The scar (inherited).** The operator of the source project had to state the boundary out loud,
because it erodes on its own: *"You really aren't supposed to be doing any of the implementing
here. The only thing you're supposed to be doing is producing documents and governance… You're
just a coordinator for other external sessions."* The boundary erodes not through laziness but
through competence — the coordinator is usually capable of doing the work, and doing it is faster
in the moment. The corollary is the less obvious half: **a coordinator must not pre-solve the
brief.** Running a large precursor investigation and handing over the answer defeats the entire
purpose of an independent executor, because it anchors them on a conclusion they did not derive
and therefore cannot properly refute. The whole value of a second mind is its independence, and
pre-solving spends it before the work begins.

**What this means for you.** Derive it yourself. Where the brief hands you a hypothesis, it is
labelled `UNVERIFIED` and your job includes trying to kill it. A refutation is a successful
outcome and belongs in your report as one.

---

## 2. Measure your own baseline. Trust no number quoted to you.

Before changing anything, take the measurement yourself and write it down, with the time you took
it. Your report opens with a baseline-versus-final table under the heading **"measured by me —
never quoted."**

This includes numbers in your brief. It includes numbers in this file. It includes numbers in the
framework's own documentation.

**The scar (inherited, L-11).** A work brief circulated an ambient figure for a count that had
been true when someone typed it. It was stale by roughly a hundred. The session that noticed
opened its report with *"gates, measured by me — never quoted,"* which is now the house form. The
source project's own note on this is the part worth carrying: **it bit the coordinator twice** —
that is, it bit the person who had already learned the lesson once, which tells you the failure is
structural rather than a matter of care.

**Why it generalizes.** Any number in any document is stale from the moment it is typed, and the
rate of decay depends on the subject, not the document. This matters most where the subject
changes *while you read it*. Nothing about the number's presentation tells you which kind of
number you are looking at, so the only safe policy is to re-take the ones you are about to act on.

---

## 3. Verify at the right altitude

The measurement must be capable of **failing in the way that matters**. Before trusting any
check, ask three questions in order:

1. What exactly would have to go wrong for this to report a failure?
2. Is that the thing I am claiming?
3. If not — what is, and can I measure it here at all? If not, **say so and record the debt.**

**The scar (inherited, L-12).** A layout defect was signed off on a check that examined text.
The environment that check ran in had no layout engine in it at all — so it could not have
failed, regardless of the defect. The measurement was not weak; it was blind, and blindness reads
exactly like success. The project's definition of done had to be amended to lead with a clause
that should not have needed saying: *a human ran it, not just a test.*

**The scar (inherited, the good outcome).** The other source project handled the same problem
correctly and is worth copying. It published, in writing, what its own tooling could not measure —
and maintained a running ledger of what was **owed to real devices**. Work shipped with a list of
what had only been verified in a weaker environment attached to it, rather than letting the weaker
verification quietly stand in for the stronger one.

**In your report, distinguish three grades and never collapse them:** *proven under the real
conditions*, *checked through a proxy*, and *reasoned from the source*. Collapsing all three into
"verified" is the most common way a report overstates itself while every individual sentence in it
remains true.

---

## 4. Break it and confirm the check fires

For every check you add or intend to rely on: **arrange the condition it is supposed to catch, and
confirm it actually fires.** If it still passes, the check is decorative and you have learned
something more valuable than whatever you were originally testing.

**The scar (inherited).** The canonical instance is not a careless one, which is why it is the one
to carry. A check for non-determinism **passed while the exact forbidden non-determinism was
present** — both measurements happened to land inside the same millisecond, so the values matched.
The check was correctly written. The reasoning behind it was correct. It was simply blind to the
thing it existed to see. The fix was structural: control the clock, and forbid reading it
directly.

**The finding attached to this rule is the strongest single number in the corpus.** In the source
project's largest concurrent run, **every session found a real defect inside its own work this
way — without exception.** Not most. Every one. Treat a clean result here as evidence you have not
looked hard enough, and say so in your report if you cannot find one.

**Off-software, the same rule:** before trusting that a tracker will catch a missed day, miss a
day on purpose and confirm it shows up. Before trusting a log to surface a pattern, plant a known
pattern and see whether your review would find it. **An unexercised alarm is a hypothesis about an
alarm.**

---

## 5. Fences — and what to do when you find something outside yours

Your brief lists **what you own** and **what another lane owns**. Both lists are explicit. **If
your brief does not list something, you do not own it.**

**When you find a problem outside your fence: do not fix it.** Record it in your report, with a
citation precise enough for the owner to land on it, and keep going. This will feel wasteful. It
is not.

**The scar (inherited, L-10).** A collision analysis on a proposed concurrent run found eleven
conflict sets, and **eight of them were the merge-cleanly-but-wrong class** — two independently
correct changes that combine into a wrong result which nothing flags. The examples are worth
holding in mind because neither looks like a mistake at the time: a coordinate change and a camera
change, each correct in isolation and jointly mis-aimed; two workstreams each ruling differently
on the same shared value, each defensibly. The project's own four-word summary is the thing to
remember at the moment of temptation: **"Merges clean. Both green."**

The conclusion drawn was that concurrency capacity **is bought by removing collisions, not by
ignoring them** — and that against a proposal for ten parallel lanes, *three concurrent sessions
is the honest safe maximum and two is the recommended default.* One small piece of work that
de-conflicts a shared surface buys a parallel lane permanently; one opportunistic fix outside a
fence costs one, silently.

**Do not expand scope to be helpful.** Bigger scope is an explicit re-plan, not an in-session
expansion. Re-classing your declared change size upward mid-flight is expected and fine —
announce it. Silently exceeding it is not.

---

## 6. Decide, document, flag — and the cheap-to-reverse constraint

When you hit an ambiguity mid-flight and the operator is not available:

1. **Make the call.**
2. **Implement it.**
3. **Document it prominently**, under a heading that cannot be missed.
4. **Flag it:** *"judgement call — reverse this if wrong."*

With one hard constraint, and it is the part that makes the rest safe: **every such call must be
cheap to reverse. If it is not cheap to reverse, take the conservative option and say why.**

**The scar (inherited).** The operator's ruling is one sentence: **"A stalled session is worse
than a documented judgement call."** The failure it was written against is the session that stops
and waits — burning the scarce resource, which is the human's attention, on a question the
executor could have answered and flagged in thirty seconds. But the constraint is what keeps this
from being a licence: an irreversible call made autonomously is not a judgement call, it is a
decision taken on someone else's behalf without asking, and no amount of prominent documentation
converts it back.

The test is mechanical. *If this is wrong, what does it cost to undo?* Minutes — decide and flag.
A rewrite, a lost measurement, a destroyed baseline, an unrecoverable state — take the
conservative option, record that you took it and why, and let the operator overrule you later at
their convenience rather than at your guess.

---

## 7. No follow-up questions

Your brief is written to be self-contained precisely because **you cannot ask.** Do not stop, do
not return a list of clarifying questions, and do not produce a partial deliverable pending an
answer. Apply rule 6 instead: decide, document, flag.

The one exception is the **falsifier** in your acceptance criteria. If you hit the result that
means the framing itself was wrong — not that the work failed, but that the question was
mis-posed — **stop and report.** Routing around a falsifier is the one failure this whole
structure exists to prevent, and it is the one case where continuing produces a complete-looking
result that measures nothing.

The second exception is anything that lands in a **non-delegable category**: identity and
authority, custody of secrets, acceptance of terms or authorship, a physical fact that requires a
body in a place, or a **preference** — anything whose correct answer is *what the operator wants*
rather than *what is true*. Mark it, stop there, and hand it back. **"Owed by a human" is an
expected and acceptable outcome**, and it is the honest one.

**No scar — policy-derived (D-022).** This rule has an operator ruling behind it and no recorded
failure, and it is labelled that way rather than given a borrowed one. Its support is that a
stalled worker burns the scarce resource — the human's attention — on a question a documented
judgement call would have answered for free. That is an argument, not an incident, and under
D-003 it is weaker than every other rule on this page. Treat it accordingly: it is the rule to
break first if breaking one is warranted.

**The scar belongs to the exceptions (inherited).** The best evidence here is an *absent*
artifact. One source project's evaluation directory is **empty**, because its specification
declared the test-question set non-delegable and the automation ran to that boundary and halted
rather than generating its own questions and grading itself against them. That empty directory is
the most honest artifact in the corpus: producing a complete-looking result that measured nothing
would have been trivially easy. Note which way this evidence points — it argues for **stopping**,
and therefore supports the exceptions above, not the rule itself. It was attached to the rule in
an earlier draft, which is exactly the drift a scar is supposed to prevent.

A collaborator working *around* the instrument is producing fiction. When a step needs the human
and the human is not available, the correct output is a blocked item — never a plausible
substitute.

---

## 8. The report contract

Returned work carries six sections. Fill all six even when one is empty; an empty section is
information.

1. **What was done, and the cause established** — with citations, *including where the brief's
   hypothesis turned out to be wrong.*
2. **What was verified, and how** — distinguishing *proven under real conditions* / *checked
   through a proxy* / *reasoned from the source* (rule 3).
3. **Judgement calls made** — each flagged for review, each with its reversal cost (rule 6).
4. **Defects found inside your own work** — see rule 4. Every session in the largest source run
   found one. A report with none has almost certainly not looked, and saying "I looked and found
   none" is a claim you should be prepared to support.
5. **Found outside your fence** — untouched, cited, with enough detail for the owner to act
   (rule 5).
6. **What was not verified** — including what is owed to a human, and why.

**Sections 4 and 6 are what make a report evidence instead of advocacy.** A report that cannot say
what it failed to check is not reporting; it is presenting. Everything in sections 1–3 is
available to a session that did excellent work and to one that did confident, plausible, wrong
work — 4 and 6 are the only sections where the two look different.

Your report opens with the baseline-versus-final table from rule 2, and it is the first thing the
reader sees.

---

## Local rules

`<Rules this project learned itself. Same shape: the rule, then the incident that produced it,
then why it generalizes. A rule proposed without an incident goes in the decision ledger as a
proposal and waits — it is not added here until something has actually gone wrong, because a
preamble of untested rules is indistinguishable from a preamble of good intentions and gets read
with exactly that much attention.>`

### `<n>`. `<Rule.>`

**The scar (local, `<date>`).** `<What happened. Specifically, causally, with what it cost.>`

**Why it generalizes.** `<…>`
