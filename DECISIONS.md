---
record_class: append-only
precedence: 2
confidence: CONFIRMED
owns:
  - the-decision-ledger
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

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
- **File order is not ledger order.** D-023 and D-024 sit physically above D-016–D-022 because that
  is where drafting put them. The **timestamp** orders this ledger (L-2); position in the file does
  not, and never did. Reordering to tidy it would mean rewriting entries that are append-only, so
  it will not happen. Read by stamp, not by scroll position.

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

`[2026-07-24T17:25Z] D-023:` **A twelfth artifact — the data boundary — and a sixth skill —
`astronomer-start` — are added, sourced from a fifth, external, non-corpus project (`BK`) that used
Astronomer as an analytical lens on its own AI-collaborator setup and independently converged on a
RED/GREEN/YELLOW access classification and a collaborator-workspace layout, neither of which the
seeded framework had.** The operator requested this integration and its scope (a new
project-scaffolding skill, plus a review pass on the five existing skills) and authorized this
repository as the destination; the shape of the additions — the artifact, the skill, the
placement inside `starting-a-project` rather than as new doctrine — is this session's synthesis,
not a call the operator made directly, and is recorded as such rather than tagged `[operator]`
by default. **Marked single-attested and provisional (D-006):** one outside source, and that
source did not run a full loop on the framework (CHARTER definition-of-done condition 6 remains
unmet — see `provenance/lineage.md`, Addendum 2026-07-24, for the full accounting, including the
honest caveat that this is *not* the condition-6 evidence the corpus is waiting on). `next:`
revisit both patterns' status once a second, independent project converges on either.

`[2026-07-24T17:25Z] D-024:` **The five existing loop-phase skills were checked against
Anthropic's official Agent Skills authoring guidance (`docs.claude.com`) and found already
compliant** — descriptions are third-person and state both what-and-when, bodies sit well under
the 500-line guidance, and none carries a bundled reference file needing progressive-disclosure
restructuring. **One change was considered and rejected:** renaming the five skills to strict
gerund form (the docs' stated preference, e.g. `observing-a-window`). Rejected because Anthropic's
own guidance lists noun-phrase and action-oriented names as acceptable alternatives and explicitly
warns against inconsistent naming *within* one skill library — renaming one skill or all five to
match a generic external convention would break every existing cross-reference throughout this
corpus (`CLAUDE.md.template`, `rituals/`, `tiers/`) for a cosmetic gain, which is exactly the kind
of change-without-a-scar this framework's own doctrine argues against. `caveat (owned):` this
finding is a point-in-time check against the guidance as fetched today; it is not re-verified
against future revisions of Anthropic's docs.

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

`[2026-07-24T20:29Z] D-025:` **The vocabulary drift recurred, so the gate that `AMENDS D-015`
pre-authorized is built: [`tools/check-corpus.py`](tools/check-corpus.py).** D-019 promoted
`append-only` to a record class in its own right and **ten sites across the corpus went on
enumerating three classes for four days.** The worst,
[`install/skills/astronomer-start/SKILL.md`](install/skills/astronomer-start/SKILL.md), did not
merely omit the fourth class — it instructed the reader *"do not invent a fourth,"* which would
have filed a new project's ledger and observation log under a class doctrine calls the wrong
reading, on day one, while the project believed it was following the framework. `AMENDS D-015`
closed with *"Not built. `next:` build it if the drift recurs."* This is the recurrence, and L-17
is explicit that the answer to a defect **class** is a mechanism rather than a third hand-fix — the
source corpus's own record of hand-fixing this class is *"every hand-fix drifted back."* The gate
checks three things: vocabulary membership against a registry with one declared home each, the
install manifest against the skill directories actually on disk, and every relative link. It is
verified by [`tools/verify-gate.py`](tools/verify-gate.py), which seeds one real defect per check
and asserts the gate fails — `04-verification.md` requires a check be observed *failing* before it
is trusted, since a gate only ever seen passing may be passing because it is broken. `caveat
(owned):` the gate cannot see a vocabulary nobody registered, and it cannot see drift stated in
prose — *"Astronomer recognizes three classes"* was one of the ten sites and **would not have been
caught.** Both limits, and five more, are printed on every `--verbose` run rather than left to be
discovered. `caveat (owned):` it is run by hand. Automating it moves toward the tooling D-005 bars,
so that would be its own decision.

`[2026-07-24T20:29Z] D-026:` **`ACCEPTED` went missing for the third time, and the correction sweep
is recorded rather than quietly applied.** `artifacts/findings.template.md` rendered its
`Confidence:` slot as four tokens, dropping `UNVERIFIED` and `ACCEPTED`; the observation-log
template independently *defined* three tokens locally, giving half the framework's most-used
vocabulary a second home in the artifact most often copied into a new project. `AMENDS D-015`
already recorded *why* `ACCEPTED` is the one that always goes — it is the token that records a known
imperfection deliberately kept, which is the category an author summarizing their own work forgets
because it is the category that makes them look worse. Three occurrences of the same disappearance,
for the same stated reason, is not carelessness; it is a mechanism, and D-025 is the response to
it.

`[2026-07-24T20:29Z] D-027:` **Astronomer opens its own observation log
([`OBSERVATIONS.md`](OBSERVATIONS.md)), having run without one since seeding.**
`tiers/README.md` requires charter, ledger, and observation log at Lite — *"the minimum at which the
framework is still itself"* — and this repository maintained the first two only, for four days,
while `CHARTER.md` claimed it *"maintains its own charter and ledger under its own rules."* That
claim was true and the omission is what it did not mention. D-007 says the friction is recorded
rather than quietly exempted, so: the framework's own authors skipped the artifact that is hardest
to write and easiest to defer, which is the same artifact every consuming project will be tempted
to skip, for the same reason. `caveat (owned):` the twenty entries in it were written from a survey
conducted *today*, not contemporaneously with the seeding they describe — they are observations
about the corpus as it stands, not a reconstruction of the four days in between, and the log says
so at the top.

`[2026-07-24T20:36Z] D-028:` **Template links resolve from the project root a template is copied
to, framework references are bare backticked paths and never links, and `../` in a template link is
a defect.** The corpus was using two conventions at once and neither was declared:
`charter.template.md` linked `DECISIONS.md` — correct at a project root, broken where the file
actually sits — while its neighbours linked `../doctrine/…`, correct where they sit and broken the
moment they are copied. Both cannot be right, and the reason to prefer the destination is that a
template's whole purpose is to be moved. Framework paths in particular cannot be linked at all,
because `install/README.md` fills a per-project `<doctrine path>` placeholder — the same reasoning
that fixed the five broken links in `astronomer-start`. Six template links converted;
[`tools/check-corpus.py`](tools/check-corpus.py) now checks templates against the root base and
rejects `../`, so this cannot silently revert.

`[2026-07-24T20:36Z] D-029:` **The gate learned to read counted prose, because the sentence form is
how the D-019 drift actually survived.** As first built, the gate checked lists and would not have
caught *"Astronomer recognizes three classes"* — a sentence sitting directly above a table listing
four, and one of the ten sites. It now checks that any sentence *counting* a registered vocabulary
matches the registry, which extends to `the seventeen laws` and `the five phases`. **This was the
gate's own largest stated gap, closed one commit after it was stated.** `caveat (owned):` the
remaining form — a membership asserted in prose without a number, *"living, frozen and disposable
are the record classes"* — is still invisible. The hole is narrower, not closed, and `tools/README.md`
says so. All five checks are now verified by seeded breakage in
[`tools/verify-gate.py`](tools/verify-gate.py).

`[2026-07-24T20:36Z] D-030:` **For a completeness question the mechanical search is the instrument
and the reader is the interpreter — not the reverse — and `rituals/observation-pass.md` now says
so.** Measured on this corpus: a four-reader pass, told exactly which defect class to look for,
reported seven sites; a mechanical search during the repair found **three more, in files those
readers had already read.** Roughly a 30% undercount, in the direction that feels complete, and two
of the three missed sites were the most load-bearing in the set — the doc-class banners on the two
append-only templates themselves. The distinction the ritual now draws is between *"does this happen
at all"* (detection — reading is good at it, and notices what nobody thought to search for) and
*"where does this happen, everywhere"* (completeness — reading is bad at it, and fails quietly).
`caveat (owned):` one measurement, one pass, one corpus. It is stale from the moment it is typed
(L-11) and is written into the ritual as a scar, not as a constant to quote.

`[2026-07-24T20:46Z] D-031:` **A seventh doctrine file, [`doctrine/07-boundaries.md`](doctrine/07-boundaries.md),
names the two boundaries the framework was missing: what must not leave, and what a collaborator may
run.** `06-delegation.md` already named work a collaborator must not *do*, and the data boundary
named material it must not *see*. Neither covers **egress** — and a survey of all 1,371 lines of
doctrine found **zero occurrences** of web, search, network, egress, outbound, or transmit. The
boundary as it stood was a *string-copying* boundary, not an *information-flow* boundary: reading a
RED file locally and then searching the open web on a pattern derived from it violated no stated
rule. Seven numbered rules, B-1 to B-7, each with an off-software restatement (D-002). A new file
rather than an extension of `06-delegation.md`, because Custody governs who may *hold* a secret,
which is a different question from what may leave, and burying the second inside the first makes it
undiscoverable. **`caveat (owned):` this is the weakest material in the corpus and
`provenance/lineage.md`'s 2026-07-24 addendum says so in detail.** The BK addendum had one outside
project converging on two patterns; this has **no outside project at all**, because the enabling
condition — a collaborator with filesystem access, a network, and a shell simultaneously — is one
none of the four source projects had. Two of eleven rows carry a scar this corpus actually paid for;
the rest are structural arguments, which is how the seeded corpus's weakest material got in. `next:`
revisit if a second, unrelated project arrives independently at an egress boundary.

`[2026-07-24T20:46Z] D-032:` **Four artifacts are gated on circumstance, not on tier, and the
distinction is deliberate.** The data boundary, [source manifest](artifacts/source-manifest.template.md),
[query log](artifacts/query-log.template.md), and
[capability inventory](artifacts/capability-inventory.template.md) are each required from **Lite**
upward once their condition holds, and skipped when it does not. The reason they are not tiered is
that **their conditions have nothing to do with stakes.** A one-person Lite project sitting next to
a client's raw files, taking in documents it did not write, with an AI collaborator doing the
reading, needs all four — while a Full-tier project working on a clean repository of its own making
needs none. **Tiering them would have left the smallest projects the least protected, which is
backwards**, and it is the case where "Lite is smaller, not looser" (D-008) has actual teeth. Two
rituals (`corpus-intake`, `external-research`) and two skills (`astronomer-intake`,
`astronomer-research`) ship with them. The manifest check built in D-025 caught the new skills as
unwired the moment they existed — the first time that gate has fired on a real change rather than a
seeded one.

`[2026-07-24T20:46Z] D-033:` **`CHARTER.md` claimed definition-of-done conditions 1–5 were met at
seeding. Two were not. The claim is corrected in place, and the correction is stated rather than
quietly satisfied.** Condition 2 required every template to state its required-at tier: **ten of
twelve did not.** Condition 4 required `provenance/lineage.md` to leave no pattern unattributed: the
entire `rituals/` layer, the Friction/Conflagration vocabulary, the `artifacts/` template set, and
the `Append-only` class had **no rows at all.** Both are now met — tiers stated in all fifteen
templates, provenance addressed by dated addendum since that file is frozen (L-13). **A charter
asserting a condition it has not met is exactly the defect class L-16 puts above breakage** — *a
thing that is broken and says so is safe; a thing that is broken and reports success is not* — and
satisfying the conditions without recording that they had been mis-claimed would have been the same
defect in a quieter form. `caveat (owned):` neither gap was found by anyone checking the charter's
claim. Both surfaced in a survey looking for something else, which means **the definition of done
was not itself under any recurring check** — and conditions 1, 3, and 5 are asserted here on the
strength of that same survey. Condition 6 remains unmet and remains the only thing between this
corpus and `VALIDATED`.

`[2026-07-26T23:05Z] D-034:` **L-18 — *an instrument declares what it cannot do, before it is used* —
is added as the eighteenth law.** `[operator]` mandate: *"aggressively promote the capability
inventory… aggressively overhaul Project Astronomer to fit our needs and the needs of anything in the
future. Do not treat it as delicate and unmodifiable."* The framework already required a declaration
of error from the observation log per window and the frozen record per run, and had exempted the two
instruments doing most of the observing — the collaborator and the environment it acts through. This
closes that. **Why a law and not only a new doctrine file:** the obligation is domain-neutral, holds
at every tier, and is cited by four artifacts; a rule that governs the other rules' inputs is not a
subsection. It is **single-attested (VOC) and provisional**, and says so in place, per condition 1 of
the definition of done. Placed inside group IV beside L-11 and L-12 rather than appended at the end,
so numbers are assignment order and file order is meaning — stated in the file to stop a future
tidy-up from renumbering and silently breaking every citation (L-2). `caveat (owned):` adding the
first law since seeding cost exactly two prose edits, one registry line, and one exemption — the
counted-prose check found the third site itself. That is the cheapest possible version of this change
and it is cheap *because* D-029 built the check; without it, "eighteen laws" and "seventeen laws"
would now both be live in the corpus.

`[2026-07-26T23:05Z] D-035:` **`doctrine/08-instruments.md` holds the discharge of L-18 as six rules,
prefixed `K-`, and the default capability-role set is project-level rather than framework-level.**
K-1 capability and permission are separate facts; K-2 name the role, then bind the provider; K-3 every
role declares its fallback before it is needed; K-4 a declaration expires; K-5 decision rights are a
capability; K-6 the declaration is written by the instrument being declared and is not trusted for
that reason. **`K-` and not `I-`** because the first consuming project already numbers six invariants
`I-1`…`I-6` and cites them constantly, so a bare `I-3` would resolve to two things — the exact
ambiguity L-2 exists to prevent and that one source project had to publish a disambiguation rule to
escape. Choosing the prefix around a known collision cost nothing; discovering it later costs every
historical reference. **The role set registers like `evidence_tier`:** projects are expected to add
and strike rows, so the gate enforces internal consistency of the default only (D-021's precedent).
This is what keeps L-1's exclusion of toolchain intact — the *role* is doctrine, the *provider* is an
environment fact, and a framework that named a vendor could not survive the vendor or the
air-gapped case. `caveat (owned):` every K-rule is attested by VOC alone. Two of the six (K-2, and the
ladder in K-3) rest on argument rather than incident, and say so.

`[2026-07-26T23:05Z] D-036:` **The `law` vocabulary gains `exempt_files` for `DECISIONS.md` and
`OBSERVATIONS.md`, matching `confidence` and `record_class`.** Adding L-18 failed the gate at
`DECISIONS.md:300`, where D-029 quotes *"the seventeen laws"* as an example of the counted-prose form
it had just taught the gate to read. The quoted count was true when written; the file is append-only;
there is no legal edit that clears the failure. Editing it would falsify the incident record (L-13)
and satisfy a gate by damaging the evidence it exists to protect — the shape of the D-033 defect, one
layer down. **The gate's exemption design had anticipated this conflict for two vocabularies and
missed it for the third**, and the gap was undetectable until a law was actually added, because `law`
had gained no member since seeding (`O-21`). **An unexercised branch of a guard is a hypothesis about
that branch** (`04-verification.md`). `caveat (owned):` the exemption is now a place the gate does not
look — a genuinely wrong law count inside the ledger would pass. Accepted, because the alternative is
a check that can never go green on an append-only file, and a gate that cannot go green teaches you
to ignore it.

`[2026-07-26T23:05Z] D-037:` **The operator profile becomes the fifth conditional artifact, and its
condition is *augmentation*, not stakes.** `[operator]` — required from Lite upward whenever the
operator's input reaches the collaborator through anything that transcribes, dictates, translates,
batches or otherwise reshapes intent before it arrives. `06-delegation.md` established first and most
plainly that **the operator is the instrument** and that the instrument has known error, and then gave
that instrument nowhere to state it; the collaborator got a capability inventory and the human got
nothing. This is the twin. It is **the only artifact in the set that declares the error of a human**,
and the least attested thing in the corpus — single-authored, one project, provisional. Registered as
a `conditional_artifact` vocabulary in the same commit, which immediately failed the gate at
`install/README.md:158` — a fifth-artifact drift site the author had not found and was not looking
for (`O-22`), i.e. the registry's own stated blind spot closing on itself for the cost of one JSON
block. **Deliberate tension recorded rather than smoothed (CHARTER invariant 5):** the template
forbids an inferred profile the operator has never read, and the operator explicitly instructed that
this project's profile be **inferred** — *"honestly you can infer the dictation profile safely."*
Those reconcile only one way: delegating authorship is itself an elicited Preference, and the drafted
profile stays `UNVERIFIED` until the operator has read it. Inference is authorized; agreement is
still required. `blocks-on:` no filled profile exists yet for the consuming project, because
Astronomer is not installed there.

`[2026-07-26T23:05Z] D-038:` **The capability inventory is promoted from a structural argument to a
single-attested artifact with a scar, and gains the interrogation ritual that produces it.** Its own
status note read *"It is a structural argument — the collaborator is an instrument, instruments
declare their error — not a scar"*, and that sentence is now false. In one day a collaborator with
standing filesystem access, a network and a shell surveyed a platform it was about to build on and
reported broad capability read from documentation; a second pass instructed only to **re-measure
rather than re-read** overturned thirty-two claims, the largest class being documented capability
that installation did not have. The same survey found the consuming project's own always-loaded
governing instructions were not in version control, so every fresh session elsewhere inherited none
of them, and had not for more than a thousand commits. The artifact gains the two-column
capability/permission table (K-1), the per-role fallback ladder (K-3), and the decision-rights band
(K-5); `rituals/capability-interrogation.md` is the forward half of `instrument-drift.md` and states
the division that makes it work — **the collaborator answers capability by measuring, the operator
answers permission by deciding, and neither may answer the other's question.** `caveat (owned):`
promotion is one rung, not two. One project is a practice; three independent arrivals are a law
(CHARTER invariant 4), and this has one.

`[2026-07-26T23:45Z] D-039:` **"Law" carried two incompatible senses and now carries one, with
evidence tracked separately as a GRADE.** `01-laws.md` used *law* to mean **binding at every tier**;
CHARTER invariant 4 used it to mean **attested in three independent projects**. The largest group of
laws sat at two attestations — a state the invariant did not name at all — so the corpus asserted a
promotion standard it did not apply to its own vocabulary. **This is an L-14 violation in the most
load-bearing vocabulary in the framework, and L-14 is itself only `converging`.** Resolved by
separating the two claims rather than renaming anything: all eighteen laws remain binding, identifiers
are untouched so no citation breaks, and a grade — `practice` / `converging` / `settled` — records the
evidence. **Grade does not modulate obedience**; a `practice` law is followed exactly as a `settled`
one is, because "Lite is smaller, not looser" applies to evidence as well as to tiers. `caveat
(owned):` this is a **demotion** for the laws now labelled `converging`, and that is the intended
direction. The alternative — a constitutional layer entrenching them — was considered and dropped,
because entrenchment protects material that has not earned protection.

`[2026-07-26T23:45Z] D-040:` **This corpus is case law, not statute, and says so in
`doctrine/01-laws.md`.** `[operator]` — reached by working the analogy properly rather than adopting
it: a constitution is **text-supreme**, and `00-precedence.md` already puts *reality above the entire
document stack*, which is a sentence no constitution can contain. Common law fits because every rule
here exists on the strength of something that happened, and four of its mechanisms were already
built: the scar is the holding (D-003), single-authored material is dictum, attestation count is
precedential weight, and L-2's supersede-by-name is overruling-by-name. **What the framing forbids is
the useful half:** reading the text more carefully is not a way to settle a question — when a rule and
a measurement disagree, the measurement wins and the rule is amended. No interpretive move is
available that saves the text. A separate constitutional layer above Astronomer was proposed and
**dropped** in the same conversation: with the same subject it would be a second home for one fact,
which is this corpus's sharpest scar.

`[2026-07-26T23:45Z] D-041:` **Definition-of-done condition 6 is named RATIFICATION.** Nothing about
the requirement changed; what changed is that it stops reading like an unticked checklist item. Under
D-040 this corpus is case law, and **case law is ratified by practice, not by assent** — which is
precisely why condition 6 is the only condition that has never moved while the other five were met,
found to be mis-claimed, corrected, and met again. Neither the operator nor a collaborator can satisfy
it by agreeing to it. `blocks-on:` a project outside this repository running one full OBSERVE→RECORD
loop.

`[2026-07-26T23:45Z] D-042:` **Standing is stated: who may change a law, a ritual, a template, a
runbook, and a grade.** Precedence said which document wins and nothing said who may move one, so it
defaulted to whoever was at the keyboard. Laws and new templates require the operator, because they
bind every future project; rituals and template clarifications are a collaborator's call, logged,
because they are cheap to reverse (B-7). **A grade may be changed by neither party alone** — only an
independent project's experience raises one, since the author of a rule is the worst-placed party to
judge how well attested it is. Two cross-cutting rules: **anyone may propose, and proposing is not
standing** (L-18 arrived that way today — drafted and argued by a collaborator, ratified by the
operator); and **no document is ever amended to satisfy a gate**, because rewording prose to slip past
a check is disabling the check with the audit trail removed. The converse is also recorded: a gate
producing a false positive is a defect in the gate, and *"the guard is intentional"* is not a licence
for the guard to be wrong.

`[2026-07-26T23:45Z] D-043:` **Attestation gets a living home and the corpus gets its first epistemic
check.** `provenance/attestation.json` carries the grade, source list and sunset for every law;
`check_attestation()` in `tools/check-corpus.py` asserts that the registry and the `law` vocabulary
describe the same set, that each count matches its source list, that each grade matches its band, and
that **anything below `settled` states what would raise it.** Checks 1–3 ask whether the documents
agree with each other; this one asks whether the corpus meets the standard it published. It was
buildable only after D-039, and necessary because the counts lived **only in a frozen file** (L-13)
that cannot carry a new law or a correction — `provenance/lineage.md` remains the frozen evidence this
registry was derived from, which is the frozen/living split and not a second home. **The sunset
assertion is the load-bearing one:** six sites said "provisional" with no expiry and no forcing
function, so provisional material accumulated permanently. The review trigger is an **event — the next
install** — carried once at the top of the registry (L-14), with the step in
`rituals/starting-a-project.md`. Verified per `04-verification.md`: two mutations seeded in
`verify-gate.py`, both observed firing, seven of seven checks now exercised. `caveat (owned):` the
check cannot tell whether a credited source project *actually* arrived at the rule independently. That
judgement was made once by a reader who could see all four corpora and is not re-derivable from the
registry; a wrongly-credited source passes silently, and only re-reading the sources would catch it.
Stated in the gate's own docstring rather than left implied.

`[2026-07-26T23:48Z] D-044:` **The install layer now carries the instruments material, because
doctrine a session never reads is not in force.** K-1…K-6, the capability interrogation and the
operator profile landed in `doctrine/` and `artifacts/` in the previous commit and reached **none** of
the eight skills — and `install/` is the compressed, enforceable form a collaborator actually reads
each session (`doctrine/README.md` says so). A rule that exists only in the reasoning layer is a rule
that runs when someone remembers to go looking, which is the condition L-17 exists to replace.
`astronomer-start` Step 3 becomes the interrogation — roles bound to providers, capability and
permission in separate columns, read-only probing, a ladder per role, and **decision rights set once**
— plus a new Step 3b for the operator profile, and the install's own review of Astronomer's
`would_attest` fields. `install/CLAUDE.md.template` gains L-18. `caveat (owned):` **two drift sites in
`install/` were found by reading and neither was catchable** (`O-26`). The template's law enumeration
stopped at L-17, and the skill counted four condition-gated artifacts against five — the first because
`law` enumerations are deliberately unchecked, the second because *"condition-gated"* paraphrases the
registry's *"conditional artifacts"* and a paraphrase defeats the noun match. **The gate's blind spots
concentrate in the layer that governs a session's first move**, which is the worst place for them.
Two instances; L-17 escalates on the third, and the mechanism is named in `O-26` rather than built.

`[2026-07-27T00:43Z] D-045:` **The first real install happened, and `install/README.md` was wrong in
four places — amended from the friction, which is the first half of condition 6.** Astronomer was
installed into `vociferous-next` at Full tier on 2026-07-27. **Ratification is NOT claimed and the
corpus stays `PROVISIONAL`:** condition 6 requires a project outside this repository to run a full
OBSERVE→RECORD loop *and* write the friction back, and only the second half is discharged here. The
window is open with four entries; the loop is not closed. The four frictions, each now fixed in
`install/README.md`:

**(a) The instructions had no step for adopting over work already in progress.** They assume a
project with nothing declared. The consuming project already had a charter, invariants, a living
specification and frozen findings under other names — only *observations* had no home — so the
install was an act of **declaration over existing artifacts**, and there was no step for it. New
Step 0a. Note the `astronomer-start` skill *description* already covered this case, so the gap was
in the README alone.

**(b) The `D-` namespace collision was not anticipated, and it is the expensive one.** The
instructions say to create a project `DECISIONS.md`. The consuming project's ledger was already at
`D-056` and this one is at `D-044`, so obeying would have put **two live `D-` namespaces in one
corpus** — the exact supersession hazard `00-precedence.md` names, and which it attributes to *that
same project* having done it once before. Refused at install time; layer 2 was mapped onto the
existing ledger with a stated namespacing rule (`AST-D-<n>`). `caveat (owned):` **the framework
anticipated the mirror image and missed this one.** `K-` was chosen over `I-` in D-035 precisely to
dodge a collision with that project's invariants — while the instruction to create a rival `D-`
ledger sat unexamined in the install layer. Anticipating the subtle case and shipping the obvious
one is worth recording as its own lesson.

**(c) Step 1 names a destination that is commonly gitignored.** `.claude/CLAUDE.md` was ignored in
the consuming project by `.claude/*`, so the file that *"decides whether the install worked"* would
have been invisible to every clone. That project had run **1,035 commits with its instruction file
untracked** and nobody aware. The instruction now requires `git check-ignore -v` before copying, and
offers the repository root as the tracked alternative. **Inheritance is the whole point of that file,
and an untracked copy is indistinguishable from a working install.**

**(d) Vendoring as instructed produces a doctrine full of dangling links.** Measured: copying
`doctrine/` and `rituals/` exactly as written left **twenty broken cross-references**, because
doctrine cites `../artifacts/`, `../tiers/` and `../provenance/` throughout. The instruction now names
the full vendor set, excludes `tools/` with its reason, and requires a README at the top of the
vendored tree naming the pinned commit and the do-not-edit rule — because an improved copy is an
undeclared fork whose divergence is invisible.

`caveat (owned):` all four were found by **performing** the install, not by reading these
instructions, which had been read carefully twice. A procedure verified only by review is a procedure
whose failures are still in front of it — `AMENDS D-033` proved the layer *installs* into an empty
directory, and that test could not have surfaced any of these four, every one of which requires a
destination that already contains something.

`[2026-07-24T20:52Z] AMENDS D-033:` **Condition 5 is no longer asserted on survey strength — it was
run.** The install layer was copied into an empty scratch directory exactly as
[`install/README.md`](install/README.md) instructs: `CLAUDE.md.template` with its five placeholders
filled, all eight skills with directory names preserved, doctrine and rituals vendored as siblings,
and the three Lite artifacts copied from `artifacts/`. Result: **a working Lite project, with no
file in this repository edited to make it work.** No unfilled placeholders remained; the one
markdown link in the copied charter resolved at the destination; both vendored framework paths it
names exist where the filled `<doctrine path>` implies. That is a **Direct** grade — proven in the
real environment, not reasoned from the source (`04-verification.md`) — and it is the first
condition in the definition of done to carry one. Conditions 1 and 3 are still asserted from
reading, and this entry does not upgrade them. `caveat (owned):` the test proves the layer
*installs*. It does not prove a session then *follows* it, which is condition 6 and is still
unmet.

`[2026-08-01T21:34Z] D-046:` **Retrieval is a role, and `K-7` says a shared index has finite signal
— adding to it can subtract.** `doctrine/08-instruments.md` named seven roles, of which **Durable
prose** — *"tracked files in the repository"* — is a **storage** claim. Nothing in the corpus named
the role of *finding* anything in that store: measured 2026-08-01, the whole framework contained
**zero** occurrences of any retrieval concept (`O-32`). The roles table gains **Corpus retrieval**
with its own fallback ladder, and section II gains **K-7**. The rule is the one genuinely new shape
here: every other instrument in that file is additive, and this is the first where a **fully
successful** acquisition degrades the instrument for every other question. Measured, VOC: one
vendor's documentation imported at full quality reached **390 of 719 notes — 54%** — after which a
semantic query for the project's own technology stack ranked a vendor navigation link at `0.611`
above its own architecture documents, and two further searches returned 364,155 and 224,288
characters and were abandoned unread (`O-35`). **Two of the three obstructed a correction that was
already in progress**, which is why the retrieval ritual grades its blast radius Conflagration only
in that case. A fourth instance of the same class was measured independently three days later, and
is the sharpest: `search_metadata` for `precedence` returned 797,038 characters, so the one query
that could navigate a corpus *by rank* is the one that cannot be run (`O-36`). `caveat (owned):`
**single-attested, VOC, and the corpus cannot corroborate it** — VOC is one of the four source
projects. `caveat (owned):` the one measured share is **54%**, and that is a point at which the
instrument had *already* failed, not a threshold. No project has measured where it starts. Quoting
54% as a limit would be the borrowed number L-11 forbids, and `08-instruments.md` says so under what
it does not settle. `caveat (owned):` **the obvious remedy is unverified.** Segregating foreign
material into its own index is what the intake ritual and the install now recommend, and **nobody
has done it** — the project that hit K-7 responded with a rule its collaborator is asked to
remember, which `O-39` is direct evidence against.

`[2026-08-01T21:34Z] D-047:` **The header block: this framework's own vocabularies become
queryable, and `owns:` makes L-14 checkable for the first time.** Every document class in
`doctrine/05-the-record.md` was *"stated at the top of the file"* as prose — readable, and not
answerable to a question like *"show me every `CONFIRMED` document nobody has re-verified since
March."* Measured 2026-08-01: **0 of 16** artifact templates carried any machine-readable metadata
(`O-34`), while the first consuming project had independently rendered six of this framework's own
vocabularies as YAML frontmatter across **703 of its 750 documents** (`O-33`) — `confidence:` on
700, `precedence:` on 310, `owns:` on 309. **This was found, not designed**, and that is the
strongest argument for it: an outside project reached for the same six concepts without being told
to. The block ships in all 16 templates and in 34 of this repository's own files (invariant 5).
**`owns:` is the load-bearing field and the only one that is not a restatement.** L-14 has asserted
since the beginning that a vocabulary has exactly one home, and until now the rule was enforceable
only by someone who already knew where the home *was*; `owns:` makes it a claim the document makes
about itself, so two documents claiming one fact is a mechanical contradiction rather than a
discovery. Note what the framework already half-believed: `tools/vocabularies.json` maps 17
vocabularies to one home each, which is the same idea implemented centrally and only for
vocabularies. `caveat (owned):` **the benefit is `PROVISIONAL` and the counter-evidence is already
in the record.** The same project that carries the schema also produced `O-37`, where a document's
`precedence: 6` sat machine-readable in its own header and it was quoted as authority against a
precedence-2 ruling anyway. **A field nothing reads at the moment of reading is a field nobody
reads.** The condition that reopens this: a project carries the block for a full loop and no gate,
query or session ever consults it. `caveat (owned):` two exemptions are taken by name rather than by
silence — `provenance/lineage.md` is frozen and a retrofitted header is an edit to it, and the eight
`SKILL.md` files carry harness-required frontmatter that the gate will not trade for a tidier schema.
An **append-only** file does get a block, which is a stated exception written into the doctrine: the
append-only rule protects entries, and a header is not an entry.

`[2026-08-01T21:34Z] D-048:` **Two checks added to the corpus gate — the header block, and ID
collisions — and the ID one is ported on someone else's incidents rather than waiting for our own.**
The gate went from 7 checks to **14, every one observed firing** by `tools/verify-gate.py` on
2026-08-01, measured here. The header check validates shape, membership against the registry, and
one implication that had never cost anything before: **`confidence: CONFIRMED` obliges `verified_by`
and `last_verified`**, because `02-epistemics.md` defines that token as *independently re-derived,
cite where* and nothing enforced the second half. **On its first run it found six real problems, two
of them in the pass that installed it** — `doctrine/05-the-record.md` is the registered home of
`effort` and did not claim it, and four *templates* claimed to own facts that belong to the
documents they produce. A template is not a record and cannot be the single home for anything.
**The ID-collision check is a deliberate exception to `rituals/recurring-defect.md`**, which asks
for three instances before a gate. This corpus has **zero** and the gate is built anyway, because
the framework **mandates the structure that collides**: append-only files, permanent addresses, gaps
never closed, and a next ID that is *"one more than the highest I can see"*, read by branches that
cannot see each other. VOC paid for it — **four** entries claimed one identifier and two sessions
allocated one range on the same day (`O-38`). Waiting for our own third instance means waiting to
damage `DECISIONS.md` and `OBSERVATIONS.md`, which is where the whole framework's authority lives.
The port is adapted rather than copied: `AMENDS D-<n>` carries the number it amends and must **not**
count as an allocation, and a naive port flagged all three of this ledger's amendments on the first
run. It also adds the inverse the original does not have — an amendment naming a decision that was
never made. `caveat (owned):` it sees **one working tree**. It catches a collision at the moment a
merge resolution is wrong and **cannot** predict one between branches that have not met; nothing
local can, and claiming otherwise would be the false-capability defect it exists to catch.
`caveat (owned):` this session's own first attempt to falsify the two new vocabulary checks was
**invalid** — renaming `### K-7.` to `### K-7-RENAMED.` left the substring intact, both checks
reported green, and the gate was briefly believed broken when the test was. That is `O-41`
reproduced within an hour of recording it, by the session that recorded it.

`[2026-08-01T21:34Z] D-049:` **[operator] Condition 6 is met. The corpus is `VALIDATED`, and the
word is worth less than it sounds.** `vociferous-next` installed Astronomer at Full tier on
2026-07-27 and ran a full OBSERVE→RECORD loop on it. The closing loop is its 2026-07-30 window:
opened `18:32Z`, four entries, `INTAKE CLOSED` at `18:38Z`; one item resolved to a `CONFIRMED` cause
with a citation; **a gate built rather than a ninth hand-fix** under L-17; the outcome recorded in
its ledger, its living documents and its operating instructions. Verified here rather than accepted
— that gate's falsifier suite was run from this session and **8 of 8 passed, measured by me**. The
second half of the condition, *the friction written back*, is this pass: `O-31`–`O-44`, one
capability rule, one ritual, two gate checks, five amended documents. Operator's call, taken on the
record. **Three limits, stated where they cannot be missed.** (1) **Ratification is not
attestation** — no grade in `provenance/attestation.json` moved and the file was not touched; every
law still rests on exactly the source projects it names. (2) **The ratifying project is one of the
four sources.** Condition 6 says *outside this repo* and `vociferous-next` is outside this repo, so
the condition is met **as written** — but it is not outside the framework's provenance, and a
framework run by a project it was partly extracted from is the weakest form of ratification that
still satisfies the condition. The addendum to `provenance/lineage.md` already anticipated exactly
this and its constraint still binds: *"Not this framework being used again by the same operator —
that tests whether it is usable, which is a different question from whether it is right."* Condition
6 asks the **usable** question. The **right** question is open. (3) **`VALIDATED` is not
`finished`** — the same pass that ratified the corpus added four new unresolved questions to
`doctrine/08-instruments.md`. `caveat (owned):` the whole of this entry was written by the
collaborator that also did the work being ratified, which is the non-independence
`04-verification.md` names, and no second reader has been over it. **What would move this further:**
a project with no hand in writing this framework installing it and running a loop. Named here so it
is a target rather than a hope.

`[2026-08-01T21:34Z] AMENDS D-001:` **The corpus no longer ships as `PROVISIONAL`.** D-001 fixed the
status at `PROVISIONAL` on 2026-07-20 with the reasoning that the framework was reconstructed from
four projects that were not trying to produce a framework, and that until one ran a full loop every
claim was a hypothesis about what worked. **That reasoning was right and is now discharged** on
condition 6 alone (D-049). The six sites that stated the old status are updated: `CHARTER.md`
invariant 3 and its definition-of-done section, `README.md`, `install/README.md`, and an
**annotation** — not an edit — appended to the frozen `provenance/lineage.md`, whose closing claim
that *"Condition 6 of the definition of done remains unmet"* was accurate when written and is now
historical. `artifacts/charter.template.md` needed no change; it always carried the status as a
choice for the consuming project to make. `caveat (owned):` D-001's original text is untouched, as
an amendment requires — it is the record of what was believed on 2026-07-20, and it was correct.

`[2026-08-01T22:03Z] D-050:` **K-7's remedy is no longer a recommendation nobody has tried — and
the half that failed is the more useful half.** `D-046` shipped K-7 with its remedy marked
`UNVERIFIED`, on the grounds that segregating a foreign corpus out of an index is the obvious
answer and no project had done it. Within the hour the project that produced K-7 did it, by
configuration rather than by a rule: the foreign corpus is excluded from the **search index only**,
and reached by explicit path. **Measured before and after** (`O-45`): indexed notes 752 → 358,
excluded 0 → 394, foreign share of what search can see **52.5% → 0%**, and a query that had returned
364,155 characters and been abandoned returned **22 ranked project documents**. Read-by-path into
the excluded tree still works, which is what makes it segregation and not deletion. `08-instruments.md`,
`corpus-intake.md` and `install/README.md` are updated from *"nobody has done it"* to `CONFIRMED` at
one project, one provider, one glob — **and no attestation grade moves**, because this is the same
project that produced the rule (`provenance/attestation.json` untouched, again).

**The finding is the row that did not improve.** A regex search on the same corpus fell only 54% —
224,288 characters to 102,483 — and is still unusable, because **its residual is the project's own
notes rather than the vendor's**. Exclusion cures a foreign-share problem and does nothing for a
corpus that is simply large about its own subject, **and the two are indistinguishable from the
symptom** — both present as a search returning more than anyone will read. A project that fixes its
share and expects search to work will be wrong for a reason the failure cannot show it. That
sentence is now in the doctrine, and it is worth more than the success above it.

`caveat (owned):` measured by the session that wrote the rule, on the instrument it wrote the rule
about, minutes later. Non-independence, named. `caveat (owned):` **the retrieval ladder's top rung
turned out to be absent on that very instrument** (`O-46`) — semantic search errors with *"compiled
without embeddings"* — so the "after" figures describe a two-rung ladder, and the rung `O-35`'s
worst instance came from could not be re-tested at all. The improvement is real and it is measured
on a smaller instrument than the one the rule was written from. `caveat (owned):` a `K-4`
re-measurement in the same pass found **three capability *gains*** the declaration had missed
(`O-47`), including a credential scope whose absence it recorded as operator-owned debt after the
operator had already granted it. **K-4 is written as though drift means decay; it does not**, and
that is now an open question in `08-instruments.md` rather than a fix.

`[2026-08-01T22:33Z] D-051:` **A rule that bites at session time lives in the file a session
loads — and that is now a gate, because relocating one rule never relocated the class.** `D-044`
moved the instruments material into the install layer on the finding that *"doctrine a session
never reads is not in force."* Measured 2026-08-01 (`O-48`): the `AST-D-<n>` namespacing rule
appears **five times in `install/README.md` and zero times in `install/CLAUDE.md.template`** — so
for as long as this framework has had two ledgers, the rule preventing their confusion lived only
in a document read once, at install time, by someone who then never opens it again. A second
consuming project's session duly wrote a bare `D-044` one paragraph after citing `AST-D-049`, and
**could not have known better from the file it actually reads.** That is the **third** instance of
the namespace class — after the original two-`D-`-namespace scar `00-precedence.md` cites, and
`D-045(b)`, where the install layer told the first real install to build a rival ledger and was
caught only by refusing it. L-17 says the third instance gets a mechanism. The template gains the
rule; `check_template_carries()` asserts it stays there, **and asserts the reverse** — that the
README still explains anything the template carries, because an installer told to fill in a rule
nothing explains is the same gap pointing the other way. Gate is 7 checks → 8, falsifier suite 14
mutations → 15, all observed firing.

`caveat (owned):` the check tests that a **string** is present. It cannot tell whether the rule is
stated well, and it certainly cannot make a session obey it — `O-39` measured a rule read, agreed
to and restated out loud being violated four times in one hour. This raises the floor from *absent*
to *present*, which is the whole claim. `caveat (owned):` `TEMPLATE_MUST_CARRY` has **one** row and
must stay near one. Every row is an incident that already happened; adding rows because they seem
wise is how the template stops being compact, which `install/README.md` names as the way the
install fails in practice. `caveat (owned):` **found by an outside reader, not by this corpus.** The
gate's own docstring had said *"FOUR CHECKS"* while running eight, uncaught, because `tools/` is
exempt from the counted-prose check — corrected in the same commit, and it is the same class one
level up.

`[2026-08-01T22:41Z] AMENDS D-051:` **The count in that entry is wrong: the gate went from six
check functions to seven, not "7 → 8".** Measured now, and this time by counting rather than by
recalling: `main()` calls **7** `check_*` functions; `verify-gate.py` seeds **15** mutations; a real
run emits **15** `FIRED` lines. `D-051`'s *"falsifier suite 14 mutations → 15"* is correct. Its
*"Gate is 7 checks → 8"* is not, under either reading — there were six functions before
`check_template_carries()` and there are seven now, and if "checks" meant distinct exercised
behaviours the figures were 14 and 15, which the same sentence already gave. `D-048`'s *"7 checks to
14"* is correct and refers to falsifier-exercised checks, which is the sense `D-043` and
`tools/README.md` already use; the two entries were counting different things in the same word,
which is how the error got in.

**Kept rather than corrected in place, and worth the space:** this is L-11 committed by the entry
that was congratulating itself for building a gate — a number I did not measure, written into an
append-only record, in a corpus whose own hard rule 6 says every count is stale on sight. It was
found while assembling a brief for another project, by checking a figure before quoting it to
someone else. **Nothing in the gate can catch this**: `tools/` is exempt from the counted-prose
check, and no check counts the checks. That exemption has now produced two defects in one day — the
`"FOUR CHECKS"` docstring and this — which is the second instance of a class, not yet the third.
Named here so the third is recognisable.

`[2026-08-01T23:03Z] D-052:` **The vendored tree gets a stated home, and it must not be a hidden
directory — because three of five common instruments cannot see one.** A second consuming project
put the vendored corpus under `.claude/` and found **64 of its 84 markdown files invisible to its
own search**. Its root-cause claim — that `install/README.md` names `.claude/` as the governance
home — is `REFUTED` (`O-50`): **the file names no home at all**. It says *"as siblings under one
parent"* and stops, while naming `.claude/` three separate times for `CLAUDE.md`, for the skills,
and for the collaborator's workspace. The defect is the blank, not a wrong default: two installs
read it two ways, both defensibly, and one of them is unsearchable.

**Measured here rather than accepted** (`O-51`, L-11): `rg` without `--hidden` and Python's
`glob(recursive=True)` both skip dot-directories entirely; `os.walk` and `find` do not. The report
adds Obsidian's indexer, `CITED` and not re-derived. The instruction now names `docs/astronomer/` as
the known-good shape, requires a non-hidden parent, and carries the measurement.

**Why this is worse than it sounds, and it is `D-046`'s blind spot.** K-7 says a shared index has
finite signal and adding to it can subtract — **which assumed the corpus was in the index.** A
poisoned index ranks your own material low; a hidden directory means it is not there at all, and
`corpus-retrieval.md` step 6 already names *not findable* and *not written* as indistinguishable
from the symptom. The role shipped this morning with a ladder, and did not consider that the corpus
might be invisible to every rung of it.

`caveat (owned):` **not gated, and that is a judgement call.** This is the **second** instance of
the class *`.claude/` is a directory other tools treat specially, and this layer keeps putting
load-bearing material there without saying so* — `AST-D-045` was the first, where `.claude/` being
gitignored made the filled `CLAUDE.md` invisible to every clone. L-17 fires on the third. Recorded
as `PROVISIONAL` at `O-52` with the reopening condition named, rather than built now.
`caveat (owned):` the reporting project's own second instance was **its measurement script, written
minutes after it documented the first** — knowing about the blind spot did not prevent it, which is
`O-39` in a new domain and argues the third instance will arrive sooner than a warning can stop it.
`caveat (owned):` this session did not sweep the corpus for *other* instructions pointing at hidden
paths. Owed.

`[2026-08-02T00:53Z] AMENDS D-052:` **Stronger than recorded, and the reason is worse: the
instrument the framework tells you to stand up cannot read the location the framework most often
names.** `D-052` counted *"three of five common instruments"* blind to dotted paths. Measured since
(`O-53`): the `obsidian-mcp` server — the exact provider a project would install to fill the
**corpus retrieval** role `D-046` added this morning — indexed **1 of 3** files in a fixture whose
other two sat under `.claude/`. That is **four of six**, and the fourth is not a general-purpose
tool the framework is silent about. It is the recommended one.

**So the framework contradicts itself across two files.** `install/README.md` names `.claude/` three
times and, until `D-052`, named no home for the vendored corpus. `doctrine/08-instruments.md` tells
a project to stand up a retrieval provider. Follow both correctly and you get a search engine over
the fraction of your corpus that is *not* governance — **which is worse than having no index at
all**, because a real search engine returning nothing reads as an answer. `corpus-retrieval.md` step
6 already names that failure and did not anticipate it arriving by construction on day one.

`caveat (owned):` this does **not** make it a third instance. It is more evidence inside `O-50`'s
instance, not a new one, and the `PROVISIONAL` at `O-52` stands with its reopening condition
unchanged — L-17 fires on a third *instance*, and inflating evidence into instances to reach a gate
sooner is the same error as ignoring the count. `caveat (owned):` whether the provider has an
opt-in for hidden paths was **not** pursued; its `--help` exposes an exclusion variable and nothing
about inclusion. If one exists, the fix is a documented setting rather than a relocation, and this
entry is then over-stated.

`[2026-08-02T01:36Z] AMENDS D-050:` **Its closing caveat is `REFUTED` and must not be read as
written.** That caveat says *"the retrieval ladder's top rung turned out to be absent on that very
instrument (`O-46`) — semantic search errors with 'compiled without embeddings'"*. The rung is
**not absent**. Measured (`O-54`): the provider is two processes, a `manifest.json` pins which
semantic-daemon binary is used, and it pinned a **9,923,072**-byte build without embeddings while a
**12,845,568**-byte build *with* them sat unused on the same machine — **both version `2.3.2`**.
Swapping it moved the error twice more, ending at `API key required`. So the true statement is
**blocked on an operator-supplied credential**, which is custody and was not sought. Everything
`D-050` says about *exclusion* — 752 → 358 indexed, 52.5% → 0% foreign, 364,155 characters → 22
ranked documents, read-by-path preserved — was measured correctly and stands unchanged.

**What this costs `D-050`'s figures:** its "after" numbers describe a **two-rung ladder** because
the third rung was misconfigured, not missing. That does not make them wrong — BM25 and regex were
measured directly — but the entry's framing of them as the ladder's full extent is now known to be
an artifact of a defect, not a property of the tool.

`[2026-08-02T01:36Z] D-053:` **The retrieval provider gets a written bring-up, because every
project that has filled this role got it wrong in a different way and none of the three failures is
in any vendor's documentation.** New: [`install/retrieval-setup.md`](install/retrieval-setup.md), a
**reference implementation and explicitly not doctrine** — CHARTER invariant 1 keeps tooling out of
the laws, so the *role* stays in `08-instruments.md` (K-7), the *procedure* in
`rituals/corpus-retrieval.md`, and one worked example lives in the install layer where `.claude/`,
`gh` and `git check-ignore` already live. It carries what is not written down anywhere else: **the
provider is two processes** and semantic can be broken while search is healthy; **a manifest pins
which binary is used**, so a more capable one elsewhere is silently ignored; **two binaries of the
same version can differ in features** and only size and behaviour distinguish them; and **the
ladder of error messages**, each naming a different layer, as a table to read against instead of a
conclusion to adopt.

Three failures answered, one per project: a corpus 52.5% foreign displacing its own architecture
documents from its own searches (`O-35`); a corpus placed under a dotted path where four of six
instruments cannot see it (`O-50`, `O-53`); and taking an error message's framing as a property of
the environment for four hours (`O-54`).

`caveat (owned):` **the document stops at `API key required` and says so in a box.** Steps 0–2 are
`CONFIRMED` end to end; step 3 is `CONFIRMED` as a diagnosis and `UNVERIFIED` as a completion,
because **nobody has observed semantic search working** and the credential is non-delegable
(`06-delegation.md`). A guide that implied otherwise would be the L-16 defect it exists to prevent.
`caveat (owned):` single-attested, one provider, one machine, one operating system. The **failure
shapes** are claimed to generalize; the commands are not. `caveat (owned):` the framework had no
warning that a **quoted diagnosis** is as unreliable as a quoted number — `O-55` measured a false
claim from this corpus overriding a *correct* finding in a consuming project, because consumers
defer to the framework by design. L-11 covers numbers and did not cover this.

`[2026-08-19T22:18Z] D-054:` **The fleet was measured before anything was shipped to it, and the
design brief's `§3` is superseded by the measurement.** `design/distribution-and-scope.md` proposed
a vendoring installer on the strength of a section headed *"Verified current state"* whose numbers
it called *"the only load-bearing facts."* Four were wrong (`O-56`–`O-59`): the fleet is **9 install
points across 7 projects**, not ~30; two of the nine are **git worktrees** of a third, so one
project's drift was counted three times; the largest reported drift was an **uncommitted change in
upstream's own working tree**, not instance drift at all; and there are **4** orphaned capabilities,
not 2 — the fourth carrying an operator approval (`<instance-D> D-029`) and living in exactly one
directory on this machine.

**The ruling is not "the numbers were wrong."** It is that the brief's `§5.3` lockfile classifies a
managed file **two** ways — clean or drifted — and that split cannot distinguish *an old release*
from *a local edit*. Measured: of 57 managed files not matching `HEAD`, **48 are byte-identical to a
commit upstream actually shipped**, 45 of them in one project that has edited nothing. Under `§5.4`
as written, adopting the installer there refuses 45 files and hands the operator **45 decisions that
are all the same decision** — the exact failure the brief names for CRLF in its own `§4.2`, arriving
by a route it did not check. **Managed files classify three ways from here on: `current`, `stale`,
`drifted`**, and `stale` names the commit it matches.

The instrument is [`tools/fleet-census.py`](tools/fleet-census.py), and it is a **measuring
instrument, not an installer** — it writes nothing. It is verified by
[`tools/verify-census.py`](tools/verify-census.py), which seeds three defects (LF normalisation
removed, history lookup removed, worktree detection disabled) and confirms each is caught, because
`04-verification.md` does not let a check be trusted until it has been seen failing.

`caveat (owned):` the census dates a stale file against **upstream's** git history, so it cannot run
from inside an instance that lacks that history. This means `tools/` is **not one shippable group**,
and the brief's open question about distributing `tools/` is now sharper rather than answered.
`caveat (owned):` one machine, one operator, one operating system — the fleet is what is on this
disk, and a project on another machine is not in the count.

`[2026-08-19T22:18Z] D-055:` **`D4` and `D5` of `design/distribution-and-scope.md` are `REFUTED` by
fixture, and the hosting unit is the *repository*, not the chain.** The brief named these two
runtime questions its highest-value unknowns, said to settle them with a two-level fixture *before
implementing*, and instructed that an answer against the design be met by **re-briefing rather than
working around**. Both were settled (`O-60`) and both went against the design, so the brief was
re-briefed: it now opens with a `§0` correction, and `§3`, `§6.7`, `§7.1`, `§10` and `§11` are
corrected in place with each correction stating itself.

Measured: **`CLAUDE.md` walks up to the filesystem root and crosses repository boundaries, loaded in
full at launch. `.claude/skills/` walks up only to the repository root and does not cross.** `D4`
split core on *how a file is reached* (path citation versus runtime) and concluded skills must
install at every scope; they must not. `D5` made the **chain** the hosting unit; the correct unit is
**one docs host per chain, one skills host per repository the chain spans**. The measured fleet
already contains both shapes, which is why either anticipated branch would have been wrong for half
of it.

Two consequences worth stating separately from the rule. **First**, the brief's `§6.7` proposed
composition-by-reference so that depth cost would be *"sublinear"*; ancestors are loaded eagerly by
the runtime, so **depth cost is linear and unavoidable**, no `--budget` flag can refuse what has
already been loaded, and the brief's acceptance criterion 12 was withdrawn because it could never
have passed. **Second**, a descendant in its own repository inherits its ancestors' `CLAUDE.md` but
**not** their skills — so the always-loaded file will cite rituals the session cannot invoke. That
gap is now the first question Part B has to answer, and it did not exist before this was measured.

`caveat (owned):` only a `.git`-established repository boundary was tested. `caveat (owned):` this
refutes a **brief**, which is precedence 6 — no law, ritual or template moved, and no grade in
`provenance/attestation.json` was touched.

`[2026-08-19T22:18Z] D-056:` **The counted-prose check no longer reads a section number as a count,
and a superseded document no longer owns a vocabulary.** Running the corpus gate over the design
directory produced three failures, all pre-existing in the brief as delivered (`O-61`). Two were a
**false positive**: `### 5.1 Ownership classes` matched on the `1` of `5.1`. `00-precedence.md`
already rules on this case — *"a gate producing a false positive is a defect in the gate, and 'the
guard is intentional' is not a licence for the guard to be wrong"* — so the gate was fixed, not
exempted: the pattern now refuses a digit glued to a preceding period or digit. `verify-gate.py`
still passes, so the check was not merely quieted. The third failure was real and is an `L-14`
violation: `design/nested-scopes.md` declared itself superseded in prose while still claiming
`owns: scope-resolution` alongside the document that superseded it. **A superseded document owns
nothing**; its claims were released and the file kept.

Separately and on the merits, the brief's *"ownership classes"* were renamed **ownership roles**.
Minting a second `class` vocabulary beside `record_class` is a genuine collision hazard for a
reader, not only for the gate, and `L-14` is about homes rather than words. This is a rename to
remove the ambiguity, **not** a rewording to slip past a check — the distinction `00-precedence.md`
draws, and the reason the gate defect was fixed in the same pass rather than left to absorb it.

`[2026-08-19T22:18Z] D-057:` **`astro` is not built, and is blocked on the operator, not on
design.** CHARTER "Out of scope" bars *"tooling that generates or validates projects"* and cites
`D-005`, which reads *"No scaffolding CLI in v0 ... Revisit once condition 6 of the definition of
done is met."* **Condition 6 was met on `2026-08-01` (`D-049`)**, so `D-005`'s own sunset has fired
and the bar is revisitable — but it has not been revisited, and a design brief cannot lift a charter
bar by proposing work that violates it. Under `00-precedence.md` the charter is the top of the
stack and is amended only by explicit dated decision; under its Standing table, *"anyone may
propose; proposing is not standing."*

So: `§9`'s `IN` list is **not implemented**, deliberately. What was built instead is the measurement
the brief itself demanded first, which is not tooling that generates or validates a *project* — it
reads a fleet and writes nothing, in the same class as `check-corpus.py`, whose own ledger entry
took care to note that automating it *"moves toward the tooling `D-005` bars."*

`blocks-on:` an operator decision on whether `D-005`'s sunset is exercised. Until that entry exists,
`astro install` / `update` / `contribute` / `raise` remain out of scope. `next:` if the operator
lifts it, `§8` step 1 — **harvest the four artifacts** — runs before anything is written to any
instance, because one of the four exists in a single directory on this machine and an install would
overwrite it.

`[2026-08-19T22:30Z] D-058:` **The install layer was executed from an empty directory for the first
time, and the vendoring instruction is corrected to what a copy actually needs.** CHARTER
definition-of-done condition 5 — *"the install layer can be dropped into an empty repository and
produce a working Lite project without editing any file in this repo"* — has been claimed met since
`2026-07-24` on inspection. It is now `CONFIRMED` **by execution** (`O-62`): a throwaway repository,
`install/README.md` followed literally, then a real session in the result which knew its project and
tier, listed all eight skills, cited `L-9` correctly, and **refused a mid-window fix under `L-7`**
quoting *"Not one line. Not the obvious thing."* Two rows of this file's own verification table,
run rather than assumed.

Three defects surfaced that are invisible from inside this repository (`O-63`), and all three are
fixed here:

1. **`install/README.md` contradicted itself about the framework's own status** — its closing
   section still said condition 6 was *"the only condition standing between this framework and
   `VALIDATED`"*, four hundred lines below a status box saying `VALIDATED` as of `2026-08-01`. The
   stale claim sat in the section a new project reads **last**, when it is deciding what it owes
   back. Corrected under CHARTER invariant 7, in place and marked, rather than quietly.
2. **The vendoring instruction produced a dangling citation.** It offered *"plus this repo's
   `CHARTER.md` and `DECISIONS.md`"*; the ledger cites the observation log constantly, so taking
   exactly those two leaves a copied ledger pointing at an `OBSERVATIONS.md` that was never copied.
   **The rule is now: take `CHARTER.md`, `DECISIONS.md` and `OBSERVATIONS.md` together, or none of
   them.**
3. **The dangle exemption was incomplete.** *"Links into `tools/` and `install/` are the only ones
   expected to dangle"* omits **template-relative** links — `artifacts/charter.template.md` points
   at the ledger the *filled* charter will sit beside, which resolves only after the template is
   copied out. Three kinds are now named, and anything else that dangles is called a vendoring
   mistake rather than a known exception.

**The finding under all three is one finding, and it is the same shape as `O-58`.**
`tools/check-corpus.py` verifies every link **in this repository**, and all three of these were fine
here — they break only after the corpus is copied into a differently-shaped tree. **The corpus gate
checks the corpus; nothing checked the copy**, and the install layer is exactly the part of this
framework whose correctness lives in the copy.

`caveat (owned):` a **greenfield Lite** install is what was tested. Step 0a (adoption over work
already in progress), Step 4 (retrieval) and Step 5 (role bounds) were not exercised, and adoption
is the harder path — it is where `AST-D-045` came from. Ten of the twelve *"Verify the install"*
rows remain assumed. `caveat (owned):` one operating system, one filesystem.
`caveat (owned):` the harness that found these was a throwaway and is **not** shipped — CHARTER "Out
of scope" bars tooling that validates projects (`D-005`), and whether that bar should hold for an
install self-check is a live question this entry does not decide. `next:` run the adoption path
(Step 0a) against a project that already has a `D-` ledger, which is the untested half.

`[2026-08-28T19:43Z] D-059:` **The framework had no way to tell whether its own skills were ever
used, so every claim about them was quoted rather than measured.** `fleet-census.py` answers *what is
installed*; nothing answered *what fired*. `tools/skill-census.py` does, keyed on `attributionSkill`
— a top-level string on `assistant` records marking the whole span a skill was active. It ships with
`make-skill-fixture.py` (synthetic transcripts with a **known** span count) and
`verify-skill-census.py` (the falsifier, with `--selftest` to break the verifier itself). Read-only in
the sense `tools/README.md` draws the line, so `D-005` is not engaged: a measuring instrument is not
tooling that generates or validates projects, which is the argument both existing instruments already
carry.

**Counting `Skill` tool calls would have undercounted about six-fold**, because most spans have no
`Skill` call anywhere near them. Measured across 3,286 files / 1.63 GB in 10.6 s, parsing 2.6% of
lines: **454 spans across 26 skills**, from 235,147 assistant records. **135 of the 163 skills the
model was actually offered never fired once.** By entrypoint, `claude-desktop` **453** spans against
`sdk-cli` **one** — an unattended loop whose skill system is effectively inert. In the consuming
project specifically, `astronomer-start`, `astronomer-intake` and `astronomer-verify` never fired at
all, while firing 18/2/1 times elsewhere in the corpus: reachable, never reached for.

**The falsifier went red first, which is the only reason any of the above is reportable.** Against
the initial implementation: 13 spans on a fixture holding 12, and two seeded defects unnoticed — a
session duplicated across two files was double-counted, and a structurally corrupt attribution was
dropped in silence. Both are `L-16`'s false-success class.

`caveat (owned):` **the largest correction is one the fixture could not have caught, and it is `L-12`
verbatim.** *"A human turn closes a span"* is right for the main conversation and wrong for a
subagent, whose `type: "user"` records are the harness feeding it rather than a person speaking.
Applied indiscriminately it fragmented single activations into slivers — **3,174 of 3,404 spans
closing on a "human turn", 3,315 of those in subagent lanes, 967 of them one record long** — while
the fixture passed throughout, because it contained no subagent records at all. The fixture now
carries one and the corrected corpus reports 454. A check that cannot fail as it matters proves
nothing, and this one could not, for the rule that mattered most.

`caveat (owned):` one of the four fixes was an interface defect in the census's own output. Anomalies
were first emitted as a dict of counters, and a consumer taking `len()` of that reads the number of
counter *names* — a constant, however many anomalies occur. That is precisely how a silent drop stays
silent. They are now a list of records, each naming its file.

`caveat (owned):` the roster of 163 is derived from `skill_listing` attachments found in the corpus,
not from an authoritative registry, so *"135 never fired"* is bounded by what the transcripts happened
to record. `caveat (owned):` measured on one machine, one operator, one 75-day window.
`next:` the census is the input to a triage pass over what the absences mean; it does not interpret
them, and this entry does not either.

`[2026-08-28T20:12Z] D-060:` **Astronomer ships through BOTH channels, and the deciding constraint is
not that the plugin channel failed — it is that 150 existing citations live in records L-13 forbids
rewriting.** `design/distribution-and-scope.md` chose a vendoring installer (`D1`) after evaluating
four mechanisms, and — measured — never evaluated a fifth: the words *"plugin"* and *"marketplace"*
appear **zero times** in its 823 lines and zero times across all 63 markdown files in this corpus. The
gap mattered, because the stated reason for rejecting packaging (*"installs into `node_modules` /
`site-packages`, not where the runtime must find it"*) is precisely the objection a plugin does not
have, and the *"lands at two directories"* objection that killed submodules dissolves too, since one
plugin serves both roles.

**Three gates were pre-registered before the probe was built, with the decision rule written first:
3/3 → single channel, 2/3 → plugin ships skills and doctrine stays vendored, ≤1/3 → vendored only.**
A real marketplace and plugin were built carrying `doctrine/` and `rituals/` — 26 files, 244 KB —
validated (`claude plugin validate`, both manifests), installed, and then removed.

- **`G1` resolution — PASS.** The payload travels: `doctrine/`, `rituals/` and `skills/` all land at
  `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`, and `01-laws.md` arrives intact at
  27,441 bytes (**MEASURED**). That `${CLAUDE_PLUGIN_ROOT}` substitutes inside a skill's markdown body
  is **CITED**, not measured — `reference/claude-code/skills.md:409`, *"In a plugin skill, Claude Code
  substitutes `${CLAUDE_PLUGIN_ROOT}` … in the same two places"*.
- **`G2` permission — PASS, with a design requirement rather than a yes.** The same line continues:
  *"Using the same variable in both places lets a skill run a bundled script **without a permission
  prompt**."* So the no-prompt path is real and conditional: a skill must declare the same
  `${CLAUDE_PLUGIN_ROOT}` path in its `allowed-tools` frontmatter as it names in its body. **CITED,
  not measured** — the runtime check needs a session that did not exist when the plugin was installed,
  and `claude -p` could not authenticate to spawn one.
- **`G3` citation — PASS, by admitting there are two audiences.** The machine form
  `${CLAUDE_PLUGIN_ROOT}/doctrine/01-laws.md` is version-stable *as a string*, which is what matters;
  the resolved path is not, and `plugins-reference.md:724` says so outright — *"changes when the plugin
  updates … treat it as ephemeral"*. Measured: the cache carries a bare `0.0.1/` with **no symlink and
  no `latest` alias**, so no stable literal path exists. The human form is the upstream public URL,
  which a reader of a GitHub issue can actually follow.

**Two measurements decided more than the gates did.** A 244 KB corpus costs **~72 tokens always-on**
(`claude plugin details`), because inert payload is reachable without being loaded — the plugin channel
is nearly free, and `K-7`'s poisoning concern does not apply to it at all. And a `grep` rooted in a
consuming repository finds **nothing** in that corpus: readable by path, invisible to search. That is
the same trade the vault exclusion makes, and it is a cost, not a defect.

**So the ruling is both channels, and the reason is migration, not capability.** New consumers install
the plugin: no vendoring step, central updates, 72 tokens. `vociferous-next` keeps its vendored tree,
because **150 `doctrine/NN-*.md` citations across 40 files** point at relative paths, many of them
inside frozen records that `L-13` forbids rewriting. A corpus cannot be migrated by repointing
citations it is not permitted to touch. The vendored tree is therefore not a fallback for a failed
mechanism; it is what a live consumer with a history looks like.

`caveat (owned):` **`G1`'s runtime half and the whole of `G2` are CITED, never observed.** The
documentation is the version installed on this machine and it is unambiguous, but this corpus's own
hard rule 8 asks that grades of verification be distinguished, and a documented capability is not a
measured one. **`PROVISIONAL`**, and the condition that reopens it is named: Phase 4 builds the real
marketplace, and the first thing it must do is run the probe from a session in an unrelated repository
under default permissions, and record whether the read prompts. If it prompts despite a correct
`allowed-tools` declaration, this entry is wrong and the single-channel half of it collapses.

`caveat (owned):` the probe carried 26 files. A full install is larger, and nothing here measured
whether payload size changes install behaviour, the 256 MiB copy ceiling, or update cost.
`caveat (owned):` `D-005` was not engaged and is not settled by this entry. A marketplace distributes;
it does not generate or validate projects. `AST-D-057` still leaves that bar to the operator.
`next:` Phase 4 — build `astronomer-market`, and measure `G1b` and `G2` on it before anything else.

`[2026-08-28T20:14Z] D-061:` **`O-67`'s eviction hypothesis gets a controlled test, and the criterion
is written here before any of its data exists.** The claim is that the per-turn skill listing budget —
which drops the descriptions of the **least-invoked** skills first when it overflows — is why 135 of
163 offered skills never fire, because a skill with no history loses its description, which keeps its
history empty. That is a plausible mechanism attached to a real measurement, and plausible mechanisms
attached to real measurements are exactly what this corpus exists to distrust.

**One variable.** `skillListingBudgetFraction` raised from its default `0.01` to `0.04` at
`2026-08-28T20:0xZ`, user settings, previous file preserved at `settings.json.bak-2026-08-28`. Nothing
else changed: no skill was rewritten, no plugin enabled or disabled, no description touched. A second
change before the re-measurement makes the result unattributable (`L-10`) and the honest response then
is to say so rather than to interpret it.

**Baseline, measured before the change:** 135 of 163 offered skills never fired across the whole
corpus; in one session sampled during the same pass, the listing carried **108 entries, 73 with
descriptions, 35 name-only**, interleaved rather than truncated at the tail.

**Criterion, pre-registered.** Re-run `tools/skill-census.py` after **at least seven days** of ordinary
use, then:

- **CONFIRMED** if the name-only share falls toward zero **and** `astronomer-triage`,
  `astronomer-verify` and `astronomer-record` each fire at least once in the new window. Both halves
  are required.
- **REFUTED** if the name-only share falls but the never-fired set is materially unchanged. That
  outcome says eviction is real and is **not** what suppresses selection — which would be the more
  valuable result, because it would send the router work in Phase 6 somewhere else entirely.
- **UNRESOLVED** if the window is too quiet to judge. State the volume rather than reading a trend
  into three sessions.

`caveat (owned):` the roster of 163 comes from `skill_listing` attachments found in transcripts, not
from an authoritative registry, so both the baseline and the re-measurement are bounded by what the
harness happened to record. `caveat (owned):` seven days of one operator's ordinary use is not a
controlled workload, and a week that happens to contain a different kind of work will move these
numbers for reasons that have nothing to do with the budget. Say so if it does.
`caveat (owned):` **this test was approved before it was run, which means the temptation it guards
against is mine** — the criterion above is the one to be held to, not a better one discovered after
seeing the result.
