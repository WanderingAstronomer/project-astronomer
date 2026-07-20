# DECISIONS — Project Astronomer

The append-only decision ledger for this repository. Everything Astronomer says about ledgers
in [`doctrine/05-the-record.md`](doctrine/05-the-record.md) applies to this file first.

## Conventions

- Format: `[<UTC>] D-<n>: **<decision>** — <why>`. Stamp with a **live** UTC reading
  (`date -u`), never an ambient or injected date. Injected dates drift; live readings do not.
- **Recency alone does not win.** A later decision overrides an earlier one only when it
  *names* the decision it supersedes.
- A bare `D-<n>` resolves to **this ledger only**. References to another project's ledger are
  namespaced (`VOC-D-4`, `DD-D-016`). Ambiguous bare references are a supersession hazard.
- A decision resting on unproven evidence carries `blocks-on:` and stays `OPEN` until proven.
- Decisions made by the operator rather than by an AI collaborator are marked
  **[operator]**. The boundary is recorded, not assumed.
- Never edit a past entry. Amend with a new timestamped `AMENDS D-<n>:` line. An amendment does
  **not** consume a new number — it carries the number it amends.
- **Gaps in the sequence are normal and are never closed.** A missing number means nothing was
  ever recorded there; it does not mean something was removed. Renumbering to tidy a gap would
  break every historical reference silently, which is worse than the gap
  ([`doctrine/05-the-record.md`](doctrine/05-the-record.md)).

---

## Ledger

`[2026-07-20T20:56Z] D-001:` **This corpus ships as `PROVISIONAL`, not `VALIDATED`, and says so
in the README.** It was reconstructed from four projects that were not trying to produce a
framework at the time. Reconstruction after the fact is exactly the condition under which
narrative tidiness outruns evidence — the successes are visible and the abandoned approaches
are not. Calling it validated before a project has run a loop on it would be the first
violation of its own doctrine. `blocks-on:` CHARTER Definition-of-done §6.

`[2026-07-20T20:56Z] D-002:` **Doctrine must be statable without reference to code, tests, or
repositories.** Any rule that cannot survive that translation is a software idiom, not a law.
The test is cheap and immediate: rewrite the rule for someone tracking a chronic symptom. If
it still reads as advice, it is doctrine; if it collapses, it was an idiom wearing a law's
clothes. This is what makes the health project a real test rather than a demo.

`[2026-07-20T20:56Z] D-003:` **Every law is stated with the concrete failure that produced
it.** Inherited from vociferous, whose shared preamble records that its ten rules were "every
one of them learned the hard way," and from OpenDrop, whose contract-test docstrings *are* the
incident reports. A rule without its scar has no defense when following it is expensive — the
scar is the argument, and stripping it leaves only assertion.

`[2026-07-20T20:56Z] D-004:` **No domain-specific content lives in this repository.** No health
metrics, no software idioms, no worked examples drawn from one field. Domain material belongs
to the consuming project. A framework accumulates the shape of whatever it is used on first,
and the first user here would be health — which is precisely the generalization this is
supposed to prove.

`[2026-07-20T20:56Z] D-005:` **No scaffolding CLI in v0.** A generator would freeze the
artifact set before a single project has stressed it, and the cost of changing a shape after a
tool emits it is much higher than the cost of copying a template by hand. Revisit once
condition 6 of the definition of done is met. `next:` reassess after the first full loop.

`[2026-07-20T20:56Z] D-006:` **Provenance is a first-class column, and attestation count
decides status.** A pattern found in one source project is a *practice* and is marked as
single-attested; a pattern that three or four projects arrived at independently, without
sharing a domain, is a *law*. Independent convergence is the only validation signal available
here — there was no control group, and the projects did not coordinate.

`[2026-07-20T20:56Z] D-007:` **Astronomer governs itself under its own rules.** This file, and
`CHARTER.md`, are the dogfood. Where the framework is inconvenient to its own authors, the
friction is recorded rather than quietly exempted. Self-exemption is how a framework becomes
something everyone cites and nobody follows.

`[2026-07-20T20:56Z] D-008:` **Tiers may add required artifacts; they may never relax a law.**
Lite is smaller, not looser. If a law is droppable at low stakes it was never a law, and
belongs in the artifact set as an option. This keeps tiering from becoming a rigor-negotiation
surface.

`[2026-07-20T20:56Z] D-009:` **[operator]** **Astronomer ships as doctrine plus an installable
Claude layer, not as documentation alone.** A methodology that lives only in prose is
re-litigated at the start of every session. Encoding it in `CLAUDE.md` and skills makes the
rules load-bearing in the working session, where the decisions actually happen.

`[2026-07-20T20:56Z] D-010:` **[operator]** **The physical-health project lives in a separate
repository that installs Astronomer.** Two reasons, and the second is the load-bearing one:
personal health data should not sit in a corpus that may be shared, and — more importantly —
an external consumer is the only real test that the framework generalizes. Co-locating them
would let health-shaped assumptions leak into doctrine without anyone noticing.

`[2026-07-20T20:56Z] D-011:` **[operator]** **The framework is tiered: Lite / Standard /
Full.** Uniform full rigor is how frameworks die unused; principles-only is how they lose the
thing that made them work, which was the specific repeatable document shapes. Tiering scales
the artifact requirement to the stakes while D-008 keeps the laws fixed.

`[2026-07-20T20:56Z] D-012:` **The framework is named Astronomer for a substantive reason, and
the metaphor is held to that standard.** Astronomy is the mature science of rigorous inference
from *uncontrolled observation through an imperfect instrument* — which is the exact
predicament shared by a live production system, a human body, and a text corpus. Metaphor
terms are admitted only where they carry real methodological weight (seeing, ephemeris,
catalog, magnitude, unresolved); decorative space vocabulary is rejected.
`caveat (owned):` the sibling project vociferous already carries a space theme and its operator
has flagged that such metaphors can confuse users. That flag is about **user-facing product
copy**, not internal method vocabulary, so it does not bind here — but if Astronomer ever grows
a user-facing surface, it reopens. `blocks-on:` nothing today.

`[2026-07-20T20:56Z] D-013:` **The operating loop has five named phases: OBSERVE, TRIAGE,
RESOLVE, ACT, RECORD.** Four-phase versions in the source projects (vociferous's
intake/triage/root-cause/execute) omit a distinct RECORD step, and in practice the recording
then happens inside execution, where it is the first thing dropped under pressure. Naming it
as its own phase with its own exit condition is a deliberate divergence from the source.
*Single-authored divergence, not inherited — flagged for revision after first real use.*

`[2026-07-20T20:56Z] D-014:` **The boundary between OBSERVE and TRIAGE is a hard gate, not a
guideline.** Nothing is changed during observation — not even a one-line obvious fix.
Attested in two projects independently: OpenDrop's TRIAGE.md ran an entire QA pass producing
zero code changes, and vociferous's audit kickoff states "DO NOT FIX ANYTHING DURING INTAKE.
Not even one-line 'obvious' fixes." The reason is that a change made mid-observation
invalidates every subsequent observation in the pass, and you will not know which ones.

`[2026-07-20T20:56Z] D-015:` **Confidence is a typed token on the artifact, not a tone in the
prose.** `CONFIRMED`, `UNVERIFIED`, `REFUTED`, `PROVISIONAL`, `UNRESOLVED`. All four source
projects invented some version of this independently, which is the strongest convergence in the
corpus. Prose hedging degrades silently — a reader skims past "probably" but cannot skim past a
label in a field position.

`[2026-07-20T21:17Z] AMENDS D-015:` **The confidence vocabulary is six tokens — `CONFIRMED`,
`UNVERIFIED`, `REFUTED`, `PROVISIONAL`, `UNRESOLVED`, `ACCEPTED` — and its single home is
[`doctrine/02-epistemics.md`](doctrine/02-epistemics.md).** Every other document points at that
table and none restates it.

The seeded corpus shipped **three different memberships** of this vocabulary within hours of
writing L-14 ("vocabulary has exactly one home"): four tokens in the claim-fields table, five
here, six in the token table and in `doctrine/05`. Two independent reviewers found it separately,
neither having seen the other's report — which is both the finding and the best available
evidence that adversarial review works at all
([`doctrine/04-verification.md`](doctrine/04-verification.md)).

`ACCEPTED` is the token that went missing, and its absence is the informative part: it is the one
that records *a known imperfection deliberately kept*, which is precisely the category an author
summarizing their own work forgets, because it is the category that makes them look worse. Kept.

`caveat (owned):` this was found by review, not by a mechanism. Under L-17 a third recurrence
demands a gate rather than a third correction — a check that every vocabulary in the corpus has
exactly one enumeration. Not built. `next:` build it if the drift recurs.

`[2026-07-20T21:17Z] D-016:` **Astronomer's own documents form a framework layer above the project
layer, and a project charter cannot repeal a law.** The seeded precedence stack ordered a
project's artifacts and silently omitted doctrine and rituals — so the framework's own documents
had no declared standing, which is the exact defect `00-precedence.md` exists to prevent. Rituals
are living, subordinate to doctrine, and never override a law. A project needing to break a law
amends *Astronomer*, not its own charter: an exception that applies to only one project is not an
exception, it is a mistake.

`[2026-07-20T21:17Z] D-017:` **Rituals are framework-level and domain-neutral; runbooks are
project-level and domain-specific.** Both are triggered by the same event — the second time you
hit a friction — which made them collide on sight. The test is mechanical: if the procedure
cannot be written without naming your subject, it is a runbook and it belongs in your project
(D-004).

`[2026-07-20T21:17Z] D-018:` **The ritual axis is renamed "blast radius" (Friction /
Conflagration); "severity" belongs solely to the per-item scale** (`stop`/`major`/`minor`/
`question`). Two live scales were sharing one word. The first fix documented the collision and
warned against mixing them, which leaves the mechanism intact and re-teaches the trap to every
future reader (L-17). Renaming removes it. The two axes are orthogonal: blast radius asks *how
far does this reach*, severity asks *how much does this matter* — a `minor` item is a
Conflagration if six decisions rest on it.

`[2026-07-20T21:26Z] D-019:` **Ledgers and observation logs are frozen at the entry and living at
the file.** Neither appeared in any of `doctrine/05`'s three class lists, which left the two
most-written artifacts in the framework unclassified. The resolution is that the class applies to
the **entry**, not the file: an entry is fixed the moment it is written and is never edited, while
the file grows forever. This is what "append-only" already meant and what neither word alone
captures — "frozen" implies the file is closed, "living" implies entries may be revised, and both
readings are wrong.

`[2026-07-20T21:26Z] AMENDS D-004:` **D-004 governs the framework's subject matter, not its
illustrative examples.** As seeded, D-004 barred "worked examples drawn from one field" while
D-002 simultaneously required every law to be restated off-software — which cannot be done
without drawing on some field. Read literally the two decisions contradict, and a reviewer caught
it on its face. The settled reading: **no domain may be the framework's subject; any domain may
be its illustration**, provided examples rotate across unrelated fields so the framework does not
quietly acquire one domain's shape. Health specifically stays out of the examples, since it is
the first consumer and the generalization under test (D-010).

`D-020:` *Never allocated.* The preceding amendment was miscounted as consuming a number during
drafting. Left as a gap rather than renumbered, per the convention above — and kept visible
because a silent gap invites exactly the "did something get deleted?" question that the
convention exists to answer.

`[2026-07-20T21:26Z] D-021:` **The requirement to tier evidence is framework-level; the tiers
themselves are project-level.** `doctrine/02` requires honest evidence grading and describes two
different schemes from two source projects without canonizing either. Neither should be canon:
what counts as *direct* evidence is domain-dependent, and a framework-wide tier list would be
wrong in most domains it reached. A project therefore declares its own tiers in its charter,
under L-14's one-home rule. The default offered in the templates (`T1 DIRECT` / `T2 PROXY` /
`T3 DERIVED` / `T4 REPORTED`) is a starting point, not a vocabulary — projects are expected to
replace it. `caveat (owned):` this leaves cross-project comparison of evidence strength
impossible. That is the honest cost and it is accepted.

`[2026-07-20T21:26Z] D-022:` **Two of the shared preamble's eight rules rest on stated policy
rather than a recorded incident, and are marked as such.** D-003 requires every rule to carry its
scar; a review found that "you are an executor, not a coordinator" and "do not ask follow-up
questions" have operator rulings behind them but no documented failure. The executor rule has
since been given its real incident — a coordinator that drifted into implementing and was
corrected in the operator's own words — but the no-questions rule genuinely has none: it is a
working-style ruling, not a lesson. Rather than invent an incident, it is labelled
*policy-derived*. **A framework that manufactures plausible war stories to satisfy its own rule
about war stories has defeated the rule** (L-16).
