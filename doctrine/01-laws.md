# 01 — The Laws

Eighteen laws, in six groups. They hold at every tier. [`tiers/`](../tiers/) changes which
*artifacts* a project must produce; it never relaxes a law (CHARTER invariant 6, D-008).

**Numbers are assignment order, not file order.** L-18 sits inside group IV because that is where it
belongs, not at the end because that is where its number falls. The same rule the ledger states
about itself applies here: renumbering to make the file scan tidily would invalidate every existing
citation silently, which is worse than reading out of sequence.

**How to read an entry.** Each law states the rule, then three things that make it usable:

- **Attested** — which of the four source projects arrived at it. Three or four independent
  arrivals, across projects with no shared domain, is the strongest evidence available here
  (D-006). Single-attested laws are marked as such and should be treated as provisional.
- **The scar** — the concrete failure that produced the rule. A law without its scar is an
  assertion, and the first time following it is expensive, an assertion loses (D-003).
- **Off-software** — the rule restated for a domain with no code in it, which is the test that
  it is doctrine and not an idiom (D-002).

Sources are abbreviated: **VOC** (transcription platform), **OD** (civic mapping service),
**FR** (retrieval-architecture proof of concept), **DD** (personal research study).

---

## I. Authority

### L-1. One document wins.

Every corpus declares a precedence order, and when two artifacts disagree the lower one is
wrong rather than merely different.

- **Attested:** FR, DD, VOC — in near-identical language. FR: "Where this document conflicts
  with any other source, this document takes precedence." DD and VOC both: "the charter wins."
- **The scar:** VOC's specification drifted into what its own settlement pass called "partly
  fiction," describing unbuilt features as shipped. Recovery cost a dedicated pass over
  seventeen documents plus adversarial verification. The cause was not carelessness — it was
  that nothing declared which artifact was binding, so a spec/code disagreement was not
  *detectable as a contradiction*.
- **Off-software:** when your protocol document and your log disagree about what you have been
  doing, decide in advance which one is the record and which one is the intention.

### L-2. Decisions supersede by name, never by recency.

A later decision overrides an earlier one only when it explicitly names what it replaces.
Timestamps order the ledger; they do not resolve it.

- **Attested:** DD ("Recency alone does not win"), VOC ("a later decision wins only when it
  *names* what it overrides").
- **The scar:** both projects independently discovered that a bare `D-7` becomes ambiguous the
  moment a second ledger exists, and that ambiguity silently disables the supersession chain —
  the one mechanism that makes a ledger trustworthy. VOC ran two `D-` namespaces
  simultaneously and had to publish a disambiguation rule retroactively.
- **Off-software:** "I decided in June to do X" does not beat "I decided in March to do Y"
  unless the June entry says it is replacing the March one. Otherwise you have two live rules
  and will follow whichever you remember.

---

## II. Evidence

### L-3. Observation and inference are different things, and the artifact says which.

Every recorded item carries a typed marker: what was *seen* versus what is *concluded*. The
marker is a field, not a tone.

- **Attested:** all four, independently. OD tags root causes `(CONFIRMED)` and hypotheses
  `Leading hypothesis`. VOC labels every initial read `UNVERIFIED`. DD types every claim
  `opinion | heuristic | outcome | expert-cited`. FR classifies every assertion into a ten-type
  epistemic taxonomy. **This is the strongest convergence in the corpus and the single idea
  most worth taking if you take only one.**
- **The scar:** VOC maintains a standing table of six root causes that were recorded as fact and
  later refuted — "the recorded story" against "what was actually true." Every one of them had
  been plausible, and several had already been built on.
- **Off-software:** "I felt worse on Tuesday" is an observation. "The supplement made me feel
  worse" is an inference. Written in the same sentence, in the same voice, they become
  indistinguishable in a month — and you will act on the second while believing you recorded
  the first.

### L-4. A claim without a scope is a claim under suspicion.

Every non-trivial claim declares the conditions under which it holds. A claim asserted
universally is *flagged*, not trusted — it is treated as a possibly-overgeneralized narrow
claim until its scope is established.

- **Attested:** DD (mandatory `scope` field; unscoped claims tagged `ASSERTED-UNIVERSAL` and
  routed to scrutiny), FR (`INDEXICAL` as a first-class type; every interrogated claim carries
  `domain_scope` and `temporal_validity`).
- **The scar:** DD's rationale is exact — without a mandatory scope the corpus "would flatten
  'this worked for me, a 27M' into 'this works.'" The same project needed an explicit
  anti-contamination rule because extractors kept inheriting the *audience's* attributes into
  the claim's scope: advice given to a 28-year-old is universal unless it depends on being 28.
- **Off-software:** almost everything true about a body is true *of a body in a state*. "Fasted
  cardio works" is not a claim until it says for whom, at what training age, under what sleep
  debt. Unscoped, it is unfalsifiable — and therefore useless, not safe.

### L-5. Co-occurrence is not shared cause.

Two problems appearing together are two problems until a single cause is proven. Grouping is a
conclusion, not an observation.

- **Attested:** VOC ("Symptoms that co-occur on one screen invite a shared-cause story the code
  does not support"; "two bugs on one screen are still two bugs"), OD (bug *classes* are named
  and swept — but only after the shared mechanism is confirmed at a cited location).
- **The scar:** VOC recorded a shared-root hypothesis linking three findings, built triage
  around it, and then refuted it — the three had independent causes and one of the three fixes
  would have been wasted.
- **Off-software:** the most dangerous sentence in a symptom log is "and also." Fatigue and
  poor sleep and low mood on the same week is one week with three entries, not one syndrome,
  until something links them.

### L-6. Refutation is a result. Keep the wrong calls visible.

A disproven hypothesis is a successful outcome and is recorded as one. Retracted items stay in
the ledger, marked, rather than being deleted.

- **Attested:** VOC ("a refutation is a valuable result, not a failure. The ledger deliberately
  keeps its wrong calls visible"; and the sharper form — "an audit that quietly drops its wrong
  calls cannot be trusted about its right ones"), DD (a literal `## Caveats (owned, not hidden)`
  section, plus a "judgment ledger" of candidates rejected *and why*), OD (an
  `### Explicitly considered and rejected` section listing four optimizations with the reason
  each was refused, including one that would have looked like a win).
- **The scar:** VOC kept a retracted finding on the books with its original timestamp, reasoning
  that if the symptom resurfaces it will already have a first sighting. The deleted version of
  that record would have cost a second discovery.
- **Off-software:** the interventions you tried and abandoned are the most expensive data you
  own, and the easiest to lose. Without them you will re-run them.

---

## III. Sequence

### L-7. Nothing is changed during observation.

Observation and intervention are separated by a hard boundary. Not even a one-line obvious fix.

- **Attested:** OD (an entire live QA pass "diagnosed read-only, no code changed yet"; a
  separate performance analysis with "no code changed at analysis time"), VOC ("DO NOT FIX
  ANYTHING DURING INTAKE. Not even one-line 'obvious' fixes").
- **The scar:** VOC's own justification, in the operator's words, is that fixing ad hoc means
  "have it not be the best fix because another system was responsible — which we would have
  discovered had we gotten all the issues out first and categorized them." The deeper cost is
  worse: a change made mid-pass invalidates every observation after it, and you will not know
  which ones.
- **Off-software:** if you change three things during a two-week observation window, you have
  not observed two weeks. You have four fragments, none long enough to read.

### L-8. Validate small before you scale.

Prove the method on a sample you can check by hand, and put a GO/NO-GO gate at the boundary.

- **Attested:** DD (Stage 0 is a formal GO/NO-GO on ~200 hand-labeled units before any
  large-scale run), FR (`--limit N` on every expensive phase, "so quality can be validated
  before committing to all ~5,500").
- **The scar:** DD states it flatly — "if it fails, fix the method; do not discover it's broken
  after scraping a million units." The failure this prevents is not a wasted run. It is a
  completed run whose output looks fine and is wrong.
- **Off-software:** run the protocol for one week and read the data before committing to
  twelve. The question at the gate is not "is it working" but "would I be able to tell."

### L-9. The falsifier is written before the observation.

Acceptance criteria are numeric and pre-registered, and they include the observation that would
mean *this whole approach is fake*.

- **Attested:** FR (five numbered success criteria, all numeric or binary, including a
  degeneracy guard: if one output class exceeds 60% the classifier is not classifying), OD
  (before/after acceptance metrics fixed before any fix was written), DD (an explicit F1 and
  recall floor set before validation).
- **The scar:** the most instructive failure in the corpus. DD pre-registered an attribution
  gate of ≥0.90 — then discovered the number had been lifted from a *same-sample* ceiling that
  no model reaches on held-out data. Every model was failing a gate that was itself wrong. The
  ruling was recorded as "the gate was the artifact, not the model," and the gate was demoted
  to a monitored metric. **Pre-registration protects you from moving the goalposts; it does not
  protect you from putting them in the wrong field. Calibrate the gate on the condition you
  will actually measure under.**
- **Off-software:** decide before the twelve weeks what number would make you stop, and
  separately what result would make you conclude the measurement itself is not sensitive enough
  to tell you anything.

### L-10. One variable at a time, or the result is unattributable.

Changes that land together cannot be told apart afterward, however cleanly they coexist.

- **Attested:** FR (the entire experimental design reduces to "the only variable between systems
  is the knowledge architecture" — identical source, identical models, one difference), VOC (a
  collision analysis found eleven conflict sets, eight of them the "merge-cleanly-but-wrong"
  class).
- **The scar:** VOC's is the subtle one and worth stating in full. Two independently correct
  changes, made in parallel, can combine into a wrong result that no tool flags: a coordinate
  change and a camera change each correct alone and jointly mis-aimed; two branches each ruling
  differently on the same shared value. In its own words: "Merges clean. Both green." The
  conclusion drawn was that concurrency capacity "is bought by removing collisions, not by
  ignoring them," and that three concurrent workstreams was the honest safe maximum against a
  proposal of ten.
- **Off-software:** starting a new supplement, a new training block, and a new sleep schedule in
  the same week produces exactly one bit of information — better or worse — at the cost of three
  experiments.

---

## IV. Measurement

### L-11. Measure your own baseline. Trust no number quoted to you.

Before changing anything, take the measurement yourself and write it down. Numbers in
documents — including this framework's — are stale from the moment they are typed.

- **Attested:** VOC, strongly and repeatedly ("trust no number quoted to you… any test count
  written in any document — **including this one** — is stale the moment it is written. This bit
  the coordinator twice"). *Single-attested as an explicit rule*, though FR's separate
  read-only progress dashboard and DD's "measured-only, never inferred" invariant are the same
  instinct arriving by a different route. Treat as provisional pending a second attestation.
- **The scar:** a work brief circulated an ambient figure for a test count. The number was
  stale by roughly a hundred. The session that measured it first opened its report with "gates,
  measured by me — never quoted," which is now the house form.
- **Off-software:** the numbers in a health plan go stale faster than in almost any other
  domain, because the subject changes while you read. A baseline you did not take is a baseline
  you are guessing at.

### L-12. Verify at the right altitude.

The measurement must be capable of detecting the thing claimed. A proxy that cannot fail in the
way that matters proves nothing.

- **Attested:** VOC ("A layout fix needs a layout measurement. Passing a character check proves
  nothing about whether something reads correctly" — the test environment had no layout engine at
  all), OD (which knew and published what its own tooling could not measure: "headless preview
  produces no compositor frames," and maintained an explicit ledger of what was **owed to real
  devices**).
- **The scar:** VOC's definition of done had to be amended to say, in the first clause, "a human
  ran it, not just a test." OD shipped work with a written list of what had only been verified
  in a weaker environment, rather than letting the weaker verification stand in silently.
- **Off-software:** a scale measures mass, not body composition. A resting heart rate from a
  wrist device at 3 a.m. is not the same instrument as one taken sitting up at 7. Know which
  claim your instrument can actually refute, and record what it cannot.

### L-18. An instrument declares what it cannot do, before it is used.

Every instrument — a tool, a collaborator, the environment they act through — states its limits
before anything depends on them. The declaration is dated, keeps *what it can do* separate from
*what it is permitted to do*, and lists what could not be determined as **owed** rather than as
absent. An instrument that has not declared its error is not yet an instrument.

- **Attested:** VOC. *Single-attested and provisional* — the framework already applied this rule
  to per-window observations (L-12) and to quoted quantities (L-11), and applies it here to the
  measuring apparatus itself. The discharge is [`08-instruments.md`](08-instruments.md); this law
  states only the obligation.
- **The scar:** two, from one day. A collaborator surveying a platform it was about to build on
  reported broad capability from documentation; a second pass instructed only to *re-measure rather
  than re-read* overturned **thirty-two** claims, the largest class being documented capability the
  installation did not have. In the same survey it found that the project's own always-loaded
  governing instructions **were not in version control** — so every fresh session elsewhere
  inherited none of them, and had not for more than a thousand commits. Neither failure was a lie.
  Both were limits nobody had been required to state, discovered by something else looking.
- **Off-software:** before the twelve weeks, write down what your instruments cannot see — the meal
  you will not weigh, the night the watch is off, the symptom you have no scale for. Doing it first
  costs a paragraph. Doing it after is called explaining the result.

---

## V. Record

### L-13. Records are frozen; specifications are living.

A point-in-time record is annotated, never edited to reflect later truth. The document
describing current reality is rewritten freely. These are different artifact classes and never
the same file.

- **Attested:** VOC ("These are point-in-time historical records. Do not edit them to reflect new
  truth" — with the companion rule "if something here contradicts a living doc, the living doc
  wins"), DD ("Findings are frozen, append-only… corrections are addenda"), OD (an explicit
  addendum block: "It does not re-run or revise the Phase-1 validation; it only notes what
  shipped afterward so this document does not mislead about the live system").
- **The scar:** all three arrived at the same failure — a research document that is quietly
  updated becomes a document that appears to have been right all along, which destroys its value
  as evidence about what you actually knew and when.
- **Off-software:** last year's lab panel is frozen. Your current protocol is living. The moment
  you edit the old panel to match the new understanding, you lose the ability to ask why you
  concluded what you concluded.

### L-14. Vocabulary has exactly one home.

Every shared term, category, and scale is defined in one place, and every consumer renders from
that place rather than restating it.

- **Attested:** DD and FR independently, with near-identical stated rationale. FR: all consumers
  "derive their taxonomy text from here rather than each hard-coding their own copy that can
  silently drift." DD: definitions "live in ONE module… so they can't silently drift apart."
- **The scar:** VOC supplies the third data point negatively. A recurring copy defect was fixed
  by hand, repeatedly, and the audit's own summary of what happened is "every hand-fix drifted
  back." The drift stopped when the definition got one enforced home.
- **Off-software:** if "a good night's sleep" means seven hours in one document and "felt
  rested" in another, you cannot aggregate across them — and you will, without noticing.

---

## VI. Honesty

### L-15. Name what cannot be delegated — then stop there.

Identify in writing the part of the work that requires the human, and when the work reaches it,
stop rather than producing a plausible substitute.

- **Attested:** FR (a specification section titled "What This Document Does Not Specify,"
  ending "the quality of the evaluation is directly determined by the quality of this question
  set. It cannot be delegated"), VOC (a five-category theory of why a task lands on the human:
  accounts, secrets, external identity, legal authorship, and physical facts — "recognizing the
  category tells you *why* it landed on your plate").
- **The scar:** the best evidence in the corpus is an *absent* artifact. FR's evaluation
  directory is empty. The automation ran to the human bottleneck and halted there instead of
  generating its own test questions and grading itself against them — which would have produced
  a complete-looking result that measured nothing.
- **Off-software:** no tool can report how you feel, and no model can perform the blood draw,
  attend the appointment, or observe the physical fact. Those are not gaps in the system; they
  are the system's boundary, and the honest move is to mark them and wait.

### L-16. Make it work, or tell the truth. Never leave the lie.

An artifact that asserts something untrue about its own state is the highest-severity defect
class, above breakage. A thing that is broken and says so is safe; a thing that is broken and
reports success is not.

- **Attested:** VOC (verbatim: "Make it work, or tell the truth — never leave the lie"; also
  "honest walls over optimistic ones"), OD (a whole remediation pass named "make it honest," a
  triage entry describing a misleading interface as something that "feels like a lie," and a
  standing principle that the visible state must track what is actually true), DD (the
  distinction between how often something is asserted and whether it works, restated in the
  findings document, in every derived recommendation, and again at each point of use).
- **The scar:** OD had a feature that appeared to succeed and did nothing — submissions were
  accepted, confirmed to the user, and then invisible to everyone including the submitter. The
  commit that fixed it leads with the mechanism and the word "invisible." Nothing was *broken*;
  it reported success it had not achieved, so nobody looked.
- **Off-software:** a tracking system that silently drops a missed day is worse than one that
  shows the gap. The gap is the signal.

### L-17. When a defect class recurs, build a gate — not another fix.

The third instance of the same failure is evidence about the *mechanism*, not the instance. Fix
the mechanism.

- **Attested:** VOC ("fixing it member-by-member leaves the mechanism intact," against a
  recorded pattern of "every hand-fix drifted back" — the recurrence stopped only once a gate
  was added), OD (a coverage floor that may rise but never fall; services that refuse to start
  when their preconditions are unmet; and a standing practice of converting every production
  incident into a cheap always-on check whose description *is* the incident report).
- **The scar:** OD's sharpest instance ran a critical procedure twice in sequence and failed the
  build if the second run did anything at all — turning "we believe this is repeatable" into a
  fact checked on every change. Its rule for the guards themselves: "the guard is intentional —
  fix the cause, don't disable it."
- **Off-software:** if you have resolved to do something four times, the problem is not resolve.
  Change the environment so the failure is not available — that is a gate, and it is the only
  intervention with a track record.

---

## What is deliberately not a law

Stated so the omissions are visible rather than accidental:

- **Any specific cadence.** Daily logs, weekly reviews, and monthly retrospectives are useful
  and are not doctrine. Cadence belongs to the project.
- **Any specific toolchain.** Version control, file formats, and storage are implementation.
  Three of the four source projects used git; one was not even a repository and achieved
  provenance through a frozen specification and in-place deviation notes.
- **Completeness of the catalog.** An exhaustive inventory with an empty orphan list is
  powerful and is a Full-tier *artifact*, not a law. Requiring it of a small project is how you
  get a project that never starts.
- **Parallelism.** Fenced concurrent workstreams are a scaling technique with a real
  correctness cost (L-10). Most projects should not use it, and the source project that did
  concluded two was the recommended default.
