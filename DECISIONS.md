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
