---
record_class: append-only
precedence: 5
confidence: CONFIRMED
owns:
  - the-observation-log
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# OBSERVATIONS — Project Astronomer

> **Doc class:** append-only — its own class, not a flavour of frozen (D-019). **Nothing in this
> file is ever edited or reordered.**
> Corrections arrive as new entries that name the entry they correct. If an entry turns out to be
> wrong, that is a fact about what was seen and believed, and it is worth more than a tidy log.

> **Nothing is changed during observation** (L-7). Not one line. Not the obvious thing. A change
> made mid-window invalidates every observation after it, and you will not know which ones.

This log exists because Astronomer did not have one. The framework requires a charter, a ledger,
and an observation log at Lite tier — its own minimum — and from seeding on 2026-07-20 until this
file was opened it maintained the first two only. That is `O-18` below, and it is the observation
that most directly indicts the corpus under D-007.

---

## Window W-1 — corpus self-survey

| | |
|---|---|
| **Scope** | The whole Astronomer corpus as committed at `32dae56` plus uncommitted working-tree changes: `doctrine/` (8 files), `artifacts/` (13), `rituals/` (12), `install/` (8), `provenance/`, `CHARTER.md`, `DECISIONS.md`, `README.md`, `tiers/` |
| **Opened** | `2026-07-24T19:55Z` |
| **Closing condition** | Every file in the five directories above read in full, and the four survey areas reported |
| **Purpose** | Establish what is actually true about the corpus before extending it for its first real consumer. Nothing was to be changed during the pass |
| **Instrument(s)** | Four parallel AI subagents, read-only, each given a disjoint area and instructed to report `file:line` citations and to omit quality judgements. Plus the operator's session, reading the same files directly |
| **Known instrument error** | (1) The subagents read excerpts, not always whole files — coverage of long files is not guaranteed exhaustive, and `O-19`/`O-20` below were found *after* the pass by direct grep, confirming the gap is real. (2) Each subagent was told what to look for, so the pass is biased toward finding the categories it was asked about and blind to categories nobody named. (3) No subagent saw another's output; cross-area contradictions could only be caught in synthesis, by one reader. (4) The reader synthesizing the results is the same one who will write the fixes, which is the exact non-independence `04-verification.md` warns about |

---

## Entries

### `O-1` · `2026-07-24T20:05Z`
- **Conditions:** grep + full read across all five directories; four independent readers.
- **Observed:** D-019 (`DECISIONS.md`) established `Append-only` as a fourth record class. Seven sites in the corpus enumerated three: `doctrine/05-the-record.md:8,12,134`, `artifacts/README.md:15-17`, `artifacts/charter.template.md:157`, `install/skills/astronomer-start/SKILL.md:41-46`, `doctrine/README.md:20`.
- **Initial read:** `UNVERIFIED` — the same defect class as `AMENDS D-015`, recurring. If so, the L-17 trigger recorded at `DECISIONS.md:139` has fired.
- **Confidence:** `CONFIRMED` — the enumerations were read directly.
- **Source:** survey areas 1, 2, 4.

### `O-2` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `install/skills/astronomer-start/SKILL.md:41-46` did not merely omit the fourth class. It read: *"Organize by the same three record classes … do not invent a fourth."*
- **Initial read:** `UNVERIFIED` — a new project following this skill would file its ledger and observation log under a class doctrine says is the wrong reading, on day one, while believing it was following the framework.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 3.

### `O-3` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `artifacts/findings.template.md:79` rendered the `Confidence:` slot as `<CONFIRMED | PROVISIONAL | UNRESOLVED | REFUTED>` — four of six tokens. The dropped tokens were `UNVERIFIED` and `ACCEPTED`.
- **Initial read:** `UNVERIFIED` — `ACCEPTED` is the token `DECISIONS.md:133-135` records as the one that goes missing every time, for a stated reason: it is the token that records a known imperfection deliberately kept.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 2.

### `O-4` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `artifacts/observation-log.template.md:38-42` *defined* three confidence tokens locally, in a template that carried no link to `doctrine/02-epistemics.md`.
- **Initial read:** `UNVERIFIED` — a second home for half the framework's most-used vocabulary; the mechanism L-14 exists to prevent, in the artifact most often copied into a new project.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 2.

### `O-5` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** 10 of 12 artifact templates stated no required-at tier in-file. Only `data-boundary.template.md:14` and `catalog.template.md:12` did.
- **Initial read:** `UNVERIFIED` — CHARTER definition-of-done condition 2 requires purpose, structure, lifecycle, **and** tier from every template. If so, condition 2 was not met at seeding.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 2.

### `O-6` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `provenance/lineage.md`'s section-level provenance table (`:77-111`) covers `doctrine/00`–`06` and `tiers/`. It has no rows for the `rituals/` layer (11 files), the Friction/Conflagration vocabulary (D-018), the `artifacts/` template set, or the `Append-only` class (D-019).
- **Initial read:** `UNVERIFIED` — CHARTER definition-of-done condition 4 requires no unattributed patterns. If so, condition 4 was not met at seeding either.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 4.

### `O-7` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `CHARTER.md:86` states: *"Conditions 1–5 are met at seeding."*
- **Initial read:** `UNVERIFIED` — read against `O-5` and `O-6`, this is a document asserting something untrue about its own state, which L-16 names the highest-severity defect class in this framework, above breakage.
- **Confidence:** `CONFIRMED` — the sentence is there; whether it is false depends on `O-5` and `O-6`, which is why this entry does not assert that.
- **Source:** `CHARTER.md`.

### `O-8` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `install/skills/astronomer-start/SKILL.md` carried five relative links of the form `../../doctrine/…` and `../../tiers/…`. From that file's location they resolve to `install/doctrine/` and `install/tiers/`, neither of which exists. After install into `.claude/skills/astronomer-start/` they resolve to `.claude/doctrine/`, which the install instructions never create. The other five skills carry no such links.
- **Initial read:** `UNVERIFIED` — the newest skill (D-023, four days old) is the only one with the defect, suggesting the convention was established by the other five and not consulted when the sixth was written.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 3.

### `O-9` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `install/README.md:94` stated *"Five are the loop's phases."* The five loop-phase skills are observe / triage / verify / decide / record. The loop's phases are OBSERVE / TRIAGE / RESOLVE / ACT / RECORD. `astronomer-decide` is not a phase, and **ACT has no skill**.
- **Initial read:** `UNVERIFIED` — the sentence is false as written, and the interesting part is what it conceals: the phase with no skill is the one where changes are actually made.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 3.

### `O-10` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** two different five-member lists of the non-delegable categories. `doctrine/01-laws.md:282-283` attributes to VOC: *accounts, secrets, external identity, legal authorship, physical facts*. `doctrine/06-delegation.md:56` says *"VOC derived five categories"* and presents a table whose fifth row, `Preference`, is disclaimed thirteen lines later as an Astronomer addition.
- **Initial read:** `UNVERIFIED` — the table is VOC's five collapsed to four plus one new one, presented as though it were VOC's five. Attribution defect, not a membership defect.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 1.

### `O-11` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `doctrine/05-the-record.md:97` states *"IDs are permanent addresses. Never renumber. Retire, never reuse."* `:141-143` of the same file states that numbers are *slots* and *"the number may be refilled by something unrelated."* Forty-five lines apart, with no carve-out naming the distinction.
- **Initial read:** `UNVERIFIED` — reconcilable (filename slots are not record IDs), but a reader applying the second rule to a `Q-` or `F-` number does exactly what the first rule calls worse than a dangling pointer.
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 1.

### `O-12` · `2026-07-24T20:05Z`
- **Conditions:** as `O-1`.
- **Observed:** `doctrine/02-epistemics.md:50-57` presents a seven-type epistemic ladder introduced by *"Both projects that built one converged…"*. The two projects' taxonomies were ten-type (FR) and four-type (DD). The seven-type ladder is neither, and carried no single-authored marker.
- **Initial read:** `UNVERIFIED` — `doctrine/README.md:37-39` requires single-authored claims to say so inline and be listed in lineage. This one did neither, in the file the README calls "the part that does the work."
- **Confidence:** `CONFIRMED`.
- **Source:** survey area 1.

### `O-13` · `2026-07-24T20:10Z`
- **Conditions:** grep for `web|search|network|egress|outbound|transmit|upload|query` across all 1,371 lines of `doctrine/`.
- **Observed:** zero occurrences. No treatment of an outbound channel as an event, no rule distinguishing verbatim private content from a query synthesized from it. The nearest concept, `doctrine/06-delegation.md:63-64` **Custody**, governs who may *hold* a secret, not what may leave. In `artifacts/`, the entire coverage was one conditional prose bullet at `data-boundary.template.md:54-56`.
- **Initial read:** `UNVERIFIED` — the data boundary as written is a *string-copying* boundary, not an *information-flow* boundary. Reading a RED file locally and then searching the open web on a distinctive pattern derived from it violates no stated rule.
- **Confidence:** `CONFIRMED` — the grep is exhaustive over the directory.
- **Source:** survey areas 1, 2, 3.

### `O-14` · `2026-07-24T20:10Z`
- **Conditions:** grep for `ingest|manifest|extractab|OCR|source document` across `artifacts/`, `rituals/`, `install/`.
- **Observed:** zero hits. No source-document ID prefix in `doctrine/05-the-record.md:105-111` (which defines `D- O- C- Q- F-`), no extraction-failure handling anywhere. The word "INTAKE" in this corpus means the observation window, not document ingestion.
- **Initial read:** `UNVERIFIED` — the artifact set models *observing a subject* and *deciding about it*, and has no model of *the collaborator as a system with inputs it consumed*.
- **Confidence:** `CONFIRMED`.
- **Source:** survey areas 2, 3.

### `O-15` · `2026-07-24T20:10Z`
- **Conditions:** full read of `rituals/instrument-drift.md`; grep for `capabilit` across `artifacts/`.
- **Observed:** zero hits for `capabilit`. `instrument-drift.md` is entirely retrospective — its trigger is *"You discover that a number you have been relying on is stale"* and step 1 is *"Stop using the number,"* which presupposes it is already in use. `doctrine/06-delegation.md:45` says "the instrument has known error" of the **human operator**; there is no parallel statement for an AI collaborator.
- **Initial read:** `UNVERIFIED` — every other instrument in the framework must declare what it cannot detect (`observation-log.template.md:16-17`). The collaborator is the only instrument exempt, and it is the one doing most of the observing.
- **Confidence:** `CONFIRMED`.
- **Source:** survey areas 1, 2, 3.

### `O-16` · `2026-07-24T20:10Z`
- **Conditions:** full read of `doctrine/02-epistemics.md`, `04-verification.md`.
- **Observed:** the mandatory claim record (`02:26-33`) has `observed_at` and no retrieval field. No caching concept, no re-fetch policy, no rule against citing a source you did not retrieve yourself. `DECISIONS.md:166` (D-024) needed exactly this and recorded it as an improvised `caveat (owned):` because no doctrine rule existed to hang it on.
- **Initial read:** `UNVERIFIED` — publication date, fetch date, and observation date are three different facts sharing one field.
- **Confidence:** `CONFIRMED`.
- **Source:** survey areas 1, 4.

### `O-17` · `2026-07-24T20:10Z`
- **Conditions:** grep for `script|tool|sandbox|execute` across `doctrine/`, `rituals/`, `install/`.
- **Observed:** no authorization model for a collaborator writing and running its own code. `doctrine/04-verification.md:124-147` presumes long-running scripts exist and governs operator *visibility* into them, but says nothing about who authored or authorized them. No ruling on the epistemic status of a collaborator's own tool output. The only mandated shell execution in the whole corpus is `date -u`.
- **Initial read:** `UNVERIFIED` — L-11's "measured by me" and L-12's altitude rule both gesture at the self-authored case without naming it. A number produced by an unverified script the collaborator wrote is being treated as an `OBSERVATION` by default.
- **Confidence:** `CONFIRMED`.
- **Source:** survey areas 1, 3.

### `O-18` · `2026-07-24T20:12Z`
- **Conditions:** directory listing of the repository root.
- **Observed:** the root contained `CHARTER.md`, `DECISIONS.md`, `README.md`. No observation log. `tiers/README.md:34-36` requires all three at Lite, described there as *"the minimum at which the framework is still itself."*
- **Initial read:** `UNVERIFIED` — Astronomer has been running below its own Lite minimum since seeding, while `CHARTER.md:48-50` claims it *"maintains its own charter and ledger under its own rules."* The claim is true and the omission is what it does not mention.
- **Confidence:** `CONFIRMED`.
- **Source:** repository root; `tiers/README.md`.

### `O-19` · `2026-07-24T20:18Z`
- **Conditions:** direct grep **after** the four-subagent pass had closed, during the repair of `O-1`.
- **Observed:** `install/README.md:123` classed `OBSERVATIONS.md` as *"Frozen."* — a site not reported by any of the four subagents.
- **Initial read:** `UNVERIFIED` — an eighth site for `O-1`, missed by a survey that was specifically looking for this defect class.
- **Confidence:** `CONFIRMED`.
- **Source:** grep during repair.

### `O-20` · `2026-07-24T20:18Z`
- **Conditions:** as `O-19`.
- **Observed:** `artifacts/observation-log.template.md:3` and `artifacts/decisions.template.md:3` both carried the doc-class banner *"frozen (append-only)."* Neither was reported by the survey.
- **Initial read:** `UNVERIFIED` — the two templates for the two append-only artifacts were themselves mis-classed, which is the most load-bearing possible location for this defect. With `O-19` this makes ten sites, against seven reported.
- **Confidence:** `CONFIRMED`.
- **Source:** grep during repair.

---

`INTAKE CLOSED` · `2026-07-24T20:21Z` · **20 entries** (`O-1`–`O-20`).

**Instrument note recorded at close, per `O-19` and `O-20`:** the four-subagent survey reported
seven sites for the record-class defect. Direct grep during repair found three more, in files the
survey had read. **The instrument under-reports by roughly 30% on exhaustive-enumeration questions**
— it finds the class reliably and the membership incompletely. Any future pass that needs
completeness rather than detection should use grep as the instrument and subagents as the
interpreter, not the reverse. That figure is measured here, once, on one pass, and should be
re-measured rather than quoted (L-11).

---

`INTAKE OPEN` · `2026-07-26T22:55Z` · **window: the instruments overhaul.**

**Conditions for this window unless an entry says otherwise:** an AI collaborator with standing
filesystem access to this repository and to one consuming project, a network, and a shell. Work
performed while adding L-18, `doctrine/08-instruments.md`, the capability-interrogation ritual, and
the operator profile. Every entry below was found *while doing something else*, which is the pattern
`O-19`/`O-20` already recorded about this corpus.

### `O-21` · `2026-07-26T23:00Z`
- **Conditions:** as the window.
- **Observed:** the `law` vocabulary in `tools/vocabularies.json` carried **no `exempt_files`**, while `confidence` and `record_class` each carried exemptions for `DECISIONS.md` and `OBSERVATIONS.md`. Adding L-18 made the gate fail on `DECISIONS.md:300`, where `D-029` quotes *"the seventeen laws"* as an example of the counted-prose form it had just taught the gate to read.
- **Initial read:** `UNVERIFIED` — the flagged text is inside an append-only file and is accurate as written; there is no legal edit that clears it. The gate's exemption design had anticipated exactly this conflict for two vocabularies and missed it for the third.
- **Confidence:** `CONFIRMED`. Fixed by exemption (D-036), not by editing the ledger.
- **Source:** `python tools/check-corpus.py` during the L-18 edit.
- **Also:** the gap was undetectable before today. `law` had gained no member since seeding, so the exemption was never exercised. **A guard with an unexercised branch is a hypothesis about that branch** (`04-verification.md`).

### `O-22` · `2026-07-26T23:02Z`
- **Conditions:** as the window.
- **Observed:** registering the new `conditional_artifact` vocabulary caused an immediate failure at `install/README.md:158` — *"up to four conditional artifacts"* — a site the author had not found and was not looking for. The author had located and corrected only `tiers/README.md`.
- **Initial read:** `UNVERIFIED` — one registration, one pre-existing undetected drift site, found in the same minute.
- **Confidence:** `CONFIRMED`.
- **Source:** `python tools/check-corpus.py` immediately after editing `vocabularies.json`.
- **Also:** this is the registry's own stated limit closing on itself. Its comment says *"Adding a vocabulary to the corpus without adding it here is the failure this file cannot catch."* The fifth conditional artifact would have been exactly that failure, and registering it cost one JSON block.

### `O-23` · `2026-07-26T23:01Z`
- **Conditions:** as the window.
- **Observed:** the first draft of `artifacts/operator-profile.template.md` referenced framework files as markdown links (`[...](../doctrine/06-delegation.md)`). The gate rejected three of them with *"template link escapes the project root — Templates are copied to a project. Reference framework files by bare backticked path, not by link."*
- **Initial read:** `UNVERIFIED` — a new author independently reproduced the exact defect the check exists to catch, without having read the convention.
- **Confidence:** `CONFIRMED`. The existing templates use backticked bare paths throughout; the convention was correct and undocumented outside the gate.
- **Source:** `python tools/check-corpus.py` on first run against the new template.
- **Also:** this is the install layer's condition-5 property being defended mechanically rather than by review. `AMENDS D-033` proved the layer installs; this check is what keeps it installing.

### `O-24` · `2026-07-26T23:09Z`
- **Conditions:** as the window.
- **Observed:** the exemption added for `O-21` did not generalise. Registering `conditional_artifact` and then *recording that registration* in `O-22` tripped the counted-prose check a second time, at `OBSERVATIONS.md:205`, because `O-22` quotes `up to four conditional artifacts` verbatim — the drift site it exists to record.
- **Initial read:** `UNVERIFIED` — the same gate-design gap, second instance, in the same sitting, and the second instance was **caused by documenting the first**.
- **Confidence:** `CONFIRMED`. Fixed by the same exemption pattern, plus an authors' rule written into `tools/vocabularies.json` naming the requirement for any future `count_nouns` vocabulary.
- **Source:** `python tools/check-corpus.py`, then `python tools/verify-gate.py` refusing to run at all — *"precondition: corpus is not clean to begin with."*
- **Also:** **two instances is a pattern, not yet a mechanism.** L-17 escalates on the *third*, and the rule it would then demand is written down in advance: a check that fails when a `count_nouns` vocabulary lacks the two append-only exemptions, rather than a third hand-written exemption. Recording the trigger now is cheaper than recognising it later, and it is the one thing L-17 says to do before the third time.

---

`INTAKE CLOSED` · `2026-07-26T23:10Z` · **4 entries** (`O-21`–`O-24`).

**Instrument note recorded at close.** All four entries were found by a **mechanical check**, none by
reading. `O-21`, `O-22` and `O-24` were found by `check-corpus.py` at the moment of the edit that
caused them; `O-23` was found by the same gate rejecting a convention the author did not know existed.
Against the previous window's measured ~30% under-report on exhaustive-enumeration questions
(`O-19`/`O-20` close note), this window adds a cleaner statement of the same asymmetry: **the author
of a change is the worst available instrument for finding what the change broke, and the cost of the
gate is now measured at three defects it caught in one sitting that review had already missed.**

That figure is one sitting, one author, and is stale from the moment it was typed (L-11).

---

`INTAKE OPEN` · `2026-07-26T23:45Z` · **window: the grades and case-law pass.**

**Conditions:** as the previous window. Work performed while separating the two senses of "law",
building `provenance/attestation.json` and its check, and wiring the install layer.

### `O-25` · `2026-07-26T23:40Z`
- **Conditions:** as the window.
- **Observed:** the counted-prose check failed on two sentences that were **not drift**: `doctrine/01-laws.md` *"Six laws are `settled`"* and `CHARTER.md` *"twelve of eighteen laws sat at two"*. Both count a **subset** by grade; the check's model only knows how to compare a count against full membership.
- **Initial read:** `UNVERIFIED` — a false positive, and the first temptation was to reword the prose to slip past it, which is the act D-042 now forbids.
- **Confidence:** `CONFIRMED`, and **the resolution was the document's, not the gate's.** A subset count in prose is a stale number waiting to happen: *"six are settled"* is wrong the moment a grade changes, and the registry is the live home for it (L-11, L-14). The grades are now named by member and never counted. The check was suspicious for a better reason than it knew.
- **Source:** `python tools/check-corpus.py` on the first draft of the grade section.
- **Also:** this is the only instance so far where the guard fired on non-drift and was still right. Worth keeping distinct from a genuine false positive, because the remedy is opposite: this one improved the document, and a genuine false positive would have required fixing the gate.

### `O-26` · `2026-07-26T23:47Z`
- **Conditions:** as the window. Found by reading the install layer deliberately, not by a check.
- **Observed:** two drift sites in `install/`, both invisible to the gate by construction. `install/CLAUDE.md.template` enumerated the laws and **stopped at L-17** — L-18 had been added to the corpus two commits earlier and never reached the file a session actually reads. `install/skills/astronomer-start/SKILL.md` said *"the four **condition-gated** artifacts"* against five.
- **Initial read:** `UNVERIFIED` — neither is catchable today. The `law` vocabulary has `check_enumerations: false` with a stated reason (law IDs appear as citations everywhere, so matching would be all false positives), and the artifact count survived because the skill writes *"condition-gated"* where the registry's noun is *"conditional artifacts"* — **a paraphrase defeats the noun match.**
- **Confidence:** `CONFIRMED`. Both corrected in this pass.
- **Source:** manual sweep of `install/` while wiring Step 3.
- **Also:** **the gate's blind spots concentrate in the install layer**, which is the worst possible place for them — doctrine drift misleads a reader who can check the source, while install-layer drift misleads a session *before it has read anything else*. Two instances now. L-17 escalates on the third, and the mechanism it would demand is stated in advance: a check that the template's law enumeration matches the `law` vocabulary exactly, which is tractable precisely because the template renders one law per line in a fixed form. Not built. If it recurs, build that.

---

`INTAKE CLOSED` · `2026-07-26T23:48Z` · **2 entries** (`O-25`–`O-26`).

**Instrument note at close.** One entry came from a mechanical check, one from reading — and they
divide exactly along the line the previous window's note predicted. The check found the thing it was
built to find, in a form it half-understood. **Reading found the two things no check was watching**,
and both were in the layer that governs a session's first move. Neither instrument would have found
the other's finding.

---

`INTAKE OPEN` · `2026-07-27T00:20Z` · **window: the first real install.**

**Conditions:** Astronomer installed into `vociferous-next` — a running project, 1,035 commits, with
its own charter, ledger, specification and skills already in place. Everything below was observed
while performing the install, and **none of it was visible from reading `install/README.md`**, which
had been read carefully twice.

### `O-27` · `2026-07-27T00:25Z`
- **Conditions:** as the window.
- **Observed:** the consuming project's decision ledger already used `D-<n>` and stood at `D-056`. `install/README.md` Step 3 instructs the creation of a project `DECISIONS.md`.
- **Initial read:** `UNVERIFIED` — following the instruction would have created a second live `D-` namespace in one corpus.
- **Confidence:** `CONFIRMED`. Refused; layer 2 mapped onto the existing ledger with `AST-D-<n>` declared for this repo's entries.
- **Also:** the sting is that `00-precedence.md` cites this exact hazard **and attributes it to that same project**, which had already run two `D-` namespaces once and published a disambiguation rule retroactively. The framework quoted the scar and then shipped an instruction that reproduces it. **D-035 dodged the mirror-image collision on `I-` deliberately, four hours earlier.** Anticipating the subtle case while shipping the obvious one is its own lesson.

### `O-28` · `2026-07-27T00:20Z`
- **Conditions:** as the window.
- **Observed:** `git check-ignore -v .claude/CLAUDE.md` in the consuming project returned `.gitignore:44:.claude/*`, and `git ls-files .claude/` returned exactly one path. The install target named in Step 1 was **untracked**, and had been for 1,035 commits.
- **Initial read:** `UNVERIFIED` — a fresh clone inherited one skill file and no operating instructions at all, silently.
- **Confidence:** `CONFIRMED`. Filled file placed at the repository root instead; Step 1 amended to require `git check-ignore` before copying.
- **Also:** the framework's own condition-5 test copied the layer into an **empty scratch directory**, where nothing is gitignored and this cannot occur. **The test that proved installability was structurally incapable of finding this.**

### `O-29` · `2026-07-27T00:40Z`
- **Conditions:** as the window. Measured with a link-resolution script written for the purpose — its output is `INFERENCE` under B-6, so it was exercised against a known-good and a known-bad path before its results were used.
- **Observed:** vendoring `doctrine/` and `rituals/` exactly as instructed left **20 broken cross-references** in the copy. Doctrine cites `../artifacts/`, `../tiers/` and `../provenance/` throughout. Vendoring those three as well reduced it to 10, all pointing at `tools/` and `install/`.
- **Initial read:** `UNVERIFIED` — the instruction names two directories and the doctrine depends on five.
- **Confidence:** `CONFIRMED`, by measurement before and after.
- **Also:** every link *inside* the vendored doctrine now resolves. The remaining ten are framework-repo references and are expected; `tools/` is deliberately not vendored because it checks the framework corpus and a copy would check a copy.

### `O-30` · `2026-07-27T00:30Z`
- **Conditions:** as the window.
- **Observed:** the eight skills registered with the harness **in-session, immediately on copy**, into a `.claude/skills/` that already contained an unrelated project skill.
- **Initial read:** `UNVERIFIED` — first evidence of installability against a non-empty destination.
- **Confidence:** `CONFIRMED`, **Direct** grade — observed in the real environment.
- **Also:** this is the one observation in this window that went the framework's way, and the only one the prior empty-directory test predicted.

---

`INTAKE CLOSED` · `2026-07-27T00:43Z` · **4 entries** (`O-27`–`O-30`).

**Instrument note at close, and it is the finding of the whole window.** Three of four entries are
defects in `install/README.md`, and **not one was findable by reading it.** The document had been
read closely twice — once to plan the install, once to execute it — and produced no flags. Every
defect required a destination that already **contained something**: an existing ledger, an existing
`.gitignore`, an existing doctrine tree with relative links.

`AMENDS D-033` recorded the install layer passing its condition-5 test by being copied into an empty
scratch directory, and graded it **Direct** because it ran in a real environment. That grade was
correct and the test was still blind: **an empty directory cannot collide with anything**, so the one
property it could never examine is the one that produced every defect here. A verification can be
Direct, honest, and structurally incapable of failing in the way that matters (L-12).

---

`INTAKE OPEN` · `2026-08-01T20:54Z` · **window: the first consumer's five days of practice,
transferred back.**

| | |
|---|---|
| **Scope** | Everything `vociferous-next` (VOC) grew *around* the Astronomer install between `2026-07-27` and `2026-08-01`, compared against this corpus at `4a33900`. Not the application — only the collaborator layer, the corpus, and the instruments |
| **Opened** | `2026-08-01T20:54Z` |
| **Closing condition** | Every artifact present in the consuming install and absent here identified, and every claim about a difference measured rather than read |
| **Purpose** | Discharge the obligation `install/README.md` states — *"when it produces friction, that friction is data owed back to the framework"*. `D-045` discharged that for the install **procedure**; this window is for the install's **first five days of use** |
| **Instrument(s)** | One session with filesystem access to both repositories, `git`, `python`, and the consuming project's Obsidian MCP over its own `docs/` tree. Byte-level diff for the drift baseline; direct measurement for every count |
| **Known instrument error** | (1) **Most entries here are transfers, not first-hand observations.** Where an entry restates something VOC observed, it is cited `VOC-O-<n>` and its grade is *this corpus reading that log*, not this corpus re-deriving the finding. Entries marked **measured here** were taken by this session directly. (2) **VOC is one of the four source projects** (`provenance/attestation.json`), so nothing in this window is independent corroboration of a rule already attested to VOC — it raises no grade, and `attestation.json` is not touched by this window. (3) The reader taking these measurements is the one who will write the amendments, which is the non-independence `04-verification.md` names. (4) The comparison is against **one** consuming install; every generalisation below is `INFERENCE` and labelled |

---

### `O-31` · `2026-08-01T20:56Z` — measured here
- **Conditions:** byte-level diff of every file this repository and the consuming install share, after normalising line endings.
- **Observed:** all 10 `doctrine/`, 15 `rituals/`, 16 `artifacts/`, and 8 `install/skills/` files are **identical**. Not one was edited in place.
- **Initial read:** `UNVERIFIED` — either the framework needed no local correction, or local correction went somewhere else.
- **Confidence:** `CONFIRMED` by diff. The second reading is the right one: **every difference between the two is net-new practice that grew beside the vendored copy rather than inside it.** A framework that is never edited by its consumers is not thereby validated; it may simply be being routed around.
- **Also:** this is what made the rest of the window cheap. There is no merge to untangle — only a transfer.

### `O-32` · `2026-08-01T20:57Z` — measured here
- **Conditions:** `grep -rin` across the whole corpus for `obsidian`, `semantic`, `embedding`, `wikilink`, `backlink`, `knowledge graph`, `vault`.
- **Observed:** **zero** occurrences in any sense relevant to retrieval. The single hit is `doctrine/04-verification.md:31`, using *"semantic equivalence"* about inter-rater agreement.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED`. `doctrine/08-instruments.md`'s roles table carries **Durable prose** — *"tracked files in the repository"* — which is a **storage** claim. There is no role for **finding** anything in that store, and no ladder for what to do when you cannot.
- **Also:** the omission is invisible at small scale and only appears past the size at which a human stops knowing every filename. That is the shape K-4 describes for a capability declaration, applied to the corpus itself.

### `O-33` · `2026-08-01T21:02Z` — measured here
- **Conditions:** measured mechanically over the consuming project's `docs/` tree.
- **Observed:** **750** markdown files, **703** carrying YAML frontmatter. Field frequency: `confidence:` **700** · `title:` **391** · `provenance:` **391** · `precedence:` **310** · `verified_by:` **310** · `last_verified:` **310** · `status:` **310** · `owns:` **309**. Also present: `supersedes:`.
- **Initial read:** `UNVERIFIED` — a local documentation convention.
- **Confidence:** `CONFIRMED`, and that first reading is wrong. Six of those fields are **this framework's own vocabulary**: `confidence:` is the six tokens (`02-epistemics.md`), `precedence:` the layer number (`00-precedence.md`), `status:` the record class (L-13), `owns:` the single-home rule (**L-14**), `verified_by:`/`last_verified:` the grade and its expiry (`04-verification.md`, K-4), `supersedes:` supersession-by-naming (**L-2**). The consuming project independently rendered the doctrine as a **queryable schema**.
- **Also:** `tools/vocabularies.json` already maps 17 vocabularies to one home each. That *is* `owns:` — implemented centrally, for vocabularies only. The consuming project found the distributed form: 309 documents each declaring the fact it is canonical for. The framework already believed the idea and shipped the narrow version.

### `O-34` · `2026-08-01T21:02Z` — measured here
- **Conditions:** first line of every `artifacts/*.template.md`.
- **Observed:** **0 of 16** artifact templates carry YAML frontmatter. The only occurrence of the word in this corpus is `install/README.md:189`, about *skill* frontmatter.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED`. Every artifact this framework ships is prose-only, so every fact in `O-33`'s schema is unavailable to any mechanical reader of a project that follows the templates as written.

### `O-35` · `2026-08-01T20:59Z` — transferred, `VOC-O-15`
- **Conditions:** read from the consuming project's observation log, not re-derived. VOC measured it in one session on `2026-07-30`.
- **Observed:** retrieval poisoning, three measured instances. (1) A semantic query for *"technology stack: backend framework, database, frontend framework…"* returned a vendor navigation link at **0.611**, ranked above several of the project's own architecture documents. (2) A full-text search for a decision ID returned **364,155 characters across 1,694 lines** and was abandoned. (3) A regex search for a provider name returned **224,288 characters across 4,742 lines** and was abandoned. Corpus at the time: **719 notes, 390 of them one vendor's documentation — 54%**.
- **Initial read:** `UNVERIFIED` here — this corpus did not take the measurements.
- **Confidence:** `CONFIRMED` **as a faithful transfer** (the log is quoted). The *finding* carries VOC's own grade, which was `CONFIRMED` by three independent instances, **two of which obstructed a correction already in progress**.
- **Also:** this is the first instrument in the framework where a **fully successful** intake degrades the instrument for every other question. Every role in `08-instruments.md` is additive; this one is not.

### `O-36` · `2026-08-01T21:05Z` — measured here, and a fourth instance of `O-35`'s class
- **Conditions:** measured this session against the consuming project's vault via its MCP.
- **Observed:** `search_metadata` returns **full note bodies**, not paths. `field=confidence, operator=exists` returned **2,693,553 characters across 91,689 lines**. `field=precedence, operator=exists` returned **797,038 characters across 32,658 lines**. Both exceeded the tool's own output ceiling and were unusable; the counts in `O-33` were taken with `grep` instead.
- **Initial read:** `UNVERIFIED` — possibly a defect in one MCP build.
- **Confidence:** `CONFIRMED` by two instances in one session. **The sharpest form of the class:** the one query that could navigate a corpus *by precedence* — this framework's central organising concept — is the one that cannot be run. `O-35`'s three instances were content searches, where volume is at least expected; a metadata query has no reason to return bodies at all.
- **Also:** by L-17 this is past the threshold for a gate rather than a fourth workaround. It also belongs upstream to the MCP implementation, which is outside this corpus.

### `O-37` · `2026-08-01T21:00Z` — transferred, `VOC-O-14`
- **Conditions:** read from the consuming project's log and its gate's docstring.
- **Observed:** a session quoted `product/05-tech-stack.md` as authority on a provider choice. That file carries **`precedence: 6` in its own frontmatter** and contradicted a precedence-2 ruling stamped nine hours earlier. VOC's summary: *"The document announced its own rank while I was reading it."*
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` — VOC graded it a recurrence, the **ninth** of its documentation-drift class, and built a gate rather than a ninth fix.
- **Also:** the machine-readable rank existed and was ignored, which cuts both ways. It is evidence *for* `O-33`'s schema — the field was there to be checked — and evidence that a field nothing surfaces at read time is a field nobody reads. `00-precedence.md` has no instruction to check the rank of a document before quoting it, because until `O-33` there was nowhere for a rank to be written.

### `O-38` · `2026-08-01T21:00Z` — transferred
- **Conditions:** read from the consuming project's operating instructions and its ID-collision gate, whose docstring records the incidents.
- **Observed:** **four** ledger entries independently claimed the identifier `D-103`; one reached the trunk and three sat on unmerged branches. Separately, two sessions allocated the range `E-48`…`E-52` in one research log on the same day. Every copy was locally valid; the collision appeared only at merge.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` — the gate's docstring cites the four entries with timestamps, and the repair is recorded.
- **Also, and this is why it is in *this* log:** the shape is *an append-only file whose next ID is "one more than the highest I can see", read by branches that cannot see each other.* **This framework mandates exactly that structure** — permanent IDs that are never reused (`05-the-record.md`), append-only ledgers, gaps never closed — and warns about none of its failure modes. `DECISIONS.md` and this file have the identical exposure. The first of the three instances the gate cites is the two-`D-`-namespace scar this corpus already quotes in `00-precedence.md`.

### `O-39` · `2026-08-01T21:00Z` — transferred
- **Conditions:** read from the consuming project's capability inventory, section 8, where it is recorded as measured on `2026-07-28`.
- **Observed:** a procedural rule the collaborator had read, agreed to, and restated was **violated four times in one session — the fourth within an hour of explicitly re-committing to it out loud**. VOC's own reading: *"This is not a knowledge failure — the rule was known, correct, and recently rehearsed at the moment of each violation."*
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` as transferred; VOC graded it measured and built a `PreToolUse` gate in response.
- **Also:** this is the most general thing in the window and the most uncomfortable. K-6 already says a collaborator's self-declaration is biased toward claiming too much. This is the operational form: **a collaborator's agreement to a rule is not evidence that the rule will bind it.** The framework's entire install layer is rules a collaborator agrees to.

### `O-40` · `2026-08-01T21:00Z` — transferred
- **Conditions:** read from the consuming project's operating instructions, recorded `2026-07-29`.
- **Observed:** an enforcement hook resolved its own script by a relative path. When the path failed to resolve, the hook exited with the refuse code and **refused every tool needed to repair it.** The gate jammed shut on its own repair.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` — the response is recorded and load-bearing: *everything fails open; any exit code other than the refuse code permits the call.*
- **Also:** general to any gate, including `tools/check-corpus.py`, which is run by hand and therefore cannot jam anything. The lesson survives the difference: **a gate that fails closed can lock you out of its own repair**, and the safe default for a gate whose job is raising the cost of a slip is to fail open.

### `O-41` · `2026-08-01T21:00Z` — transferred
- **Conditions:** read from the consuming project's capability inventory, section 8, recorded `2026-07-29`.
- **Observed:** in bringing up that hook's falsifier suite, three defects were found **in the test harness** rather than in the code under test. The worst: a repository-root variable resolved two directory levels up instead of three, so **45 of 46 probes ran green against a directory that was not the repository.** Relative paths were joined onto the wrong root consistently, so no assertion could see it. Only the single probe that `stat`s a real file exposed it.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` as transferred.
- **Also:** this corpus ships `tools/verify-gate.py` on exactly this principle and has no scar of its own for it. **A passing suite is evidence about the suite before it is evidence about the code** — L-12 aimed at the harness rather than at the subject.

### `O-42` · `2026-08-01T21:00Z` — transferred
- **Conditions:** read from the consuming project's capability inventory, section 9, where three subagent roles are recorded as measured by probe on `2026-07-29`.
- **Observed:** a read-only auditing role was defined by giving it **nine tools and no writer of any kind**. VOC's note: read-only *by absence*, which *"is stronger than a permission refusal because there is nothing to prompt around, and it is the enforcement the MCP's own `read` profile promised and failed to deliver"* — that profile served all 18 tools and permitted note creation under both documented routes.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` as transferred, **with the honest half carried across**: a second role, intended as read-only, holds a shell and can therefore write. It is read-only by construction, not by enforcement. **The role itself reported that gap unprompted and declined to run the bypass because doing so would have created the file.**
- **Also:** `06-delegation.md` describes roles by responsibility and says nothing about constructing one so that it *cannot* exceed its role. Absence is a stronger mechanism than instruction, and it is available wherever a role's tools are declared rather than described.

### `O-43` · `2026-08-01T21:00Z` — transferred
- **Conditions:** read from the consuming project's operating instructions; the figures are VOC's, measured `2026-07-31`.
- **Observed:** three properties of a work-item queue, each measured. (1) With a required-check policy that invalidates every open change whenever any change lands, the cost of a queue is **quadratic in its depth** — 103 unmerged items produced 122 runs at about 5.4 job-minutes, roughly **662 job-minutes**, plus about 550 more for one refresh pass. (2) Batch boundaries come from **overlapping line ranges, not shared filenames**: on a 94-item queue that turned 69 shared files into **86** genuinely conflicting pairs and freed **29** items to land in any order. (3) During a discovery pass the open-item count ran **86 to 117** while **70 of the 117** closed on merge.
- **Initial read:** `UNVERIFIED` — plausibly properties of one hosting platform.
- **Confidence:** `CONFIRMED` as transferred. The **generalisation past that platform is `INFERENCE`** and is labelled so wherever it is used: a verification gate with a freshness requirement makes queue cost quadratic; a conflict graph is computed on ranges rather than containers; and during a discovery pass the item count measures *looking*, not progress.
- **Also:** (3) is an anti-metric. Read as progress it inverts the signal, and `08-instruments.md` currently names a **Working set** role with no warning that its most obvious number lies during exactly the phase this framework spends most of its time in.

### `O-44` · `2026-08-01T21:04Z` — measured here
- **Conditions:** `vault_info` against the consuming project's corpus, compared against the figure its own capability inventory records for `2026-07-29T06:37Z`.
- **Observed:** the inventory records **319 notes / 342 files / 9,921,029 bytes**. Measured now: **751 notes / 774 files / 16,538,294 bytes**. The corpus **2.35 times'd in three days**, and the declaration does not know. The same file's containers, databases and language versions are dated `2026-07-27` and are described in it as *"two days stale"*; they are five.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` by direct measurement against the file's own recorded figure.
- **Also:** K-4 says a declaration is re-measured *when the environment changes*, and names the changes as *"a granted permission, a new tool, a different machine, a moved account."* **Corpus growth is not on that list**, and it is the one that happens continuously without any event to notice. A rule whose trigger is a discrete event cannot catch a change that is monotonic.

---

`INTAKE CLOSED` · `2026-08-01T21:14Z` · **14 entries** (`O-31`–`O-44`).

**What this window did not look at.** The consuming application — no source outside its `docs/`,
`.claude/` and `scripts/` trees was read, and no test of its was run except the two falsifier suites
cited in `O-37`. The consuming project's own `CLAUDE.md` was read as evidence but not audited against
its sources. `install/CLAUDE.md.template` was **not** diffed against the filled file it produced;
that comparison is owed and would answer a question this window only raises — which of the consumer's
additions had no slot in the template versus which had a slot and outgrew it.

**Instrument note at close.** Ten of fourteen entries are **transfers**, and the framework did not
observe them. That is the correct grade and it is also the finding: this corpus has no channel for a
consuming project's practice except a session that goes and reads it. `D-045` established that
install-procedure friction comes back by amendment. **Nothing establishes how five days of *use*
comes back**, and the answer here was one operator noticing that his two repositories had drifted.

**The one thing that went the framework's way** is `O-31`. Nothing was edited in place, so the
vendored doctrine is still the doctrine — the divergence is entirely additive and every item above
transfers cleanly. Had the consumer improved its local copy instead, this window would have been a
merge, and `install/README.md`'s do-not-edit rule for vendored trees is what prevented it.

---

`INTAKE OPEN` · `2026-08-01T21:50Z` · **window: K-7's remedy, measured on the project that produced
K-7.** Narrow by design — one question, asked because the rule had just been written with its remedy
marked `UNVERIFIED`, and the instrument to test it was sitting right there.

### `O-45` · `2026-08-01T22:00Z` — measured here
- **Conditions:** measured on the consuming project's own retrieval instrument, before and after a single configuration change. The provider supports exclusion globs; the corpus was excluded from the **search index only**, not moved or deleted. One variable (L-10).
- **Observed:** indexed notes **752 → 358**; excluded **0 → 394**, which is the vendor corpus exactly. Foreign share of what search can see: **52.5% → 0%**. On the three queries `O-35` recorded: `search_text` for a decision ID went from **364,155 characters across 1,694 lines, abandoned** to **22 ranked project documents, read in full**. `search_regex` for a decommitted vendor's name went from **224,288 characters** to **102,483** — **down 54%, and still unusable**. `search_semantic` **could not be run at all** (see `O-46`). **Read-by-explicit-path still reaches excluded material**, verified against a note inside the excluded tree.
- **Initial read:** `UNVERIFIED` — one change, one instrument, one session.
- **Confidence:** `CONFIRMED` for the first two rows, by direct before/after measurement on the real instrument. **Scope: one project, one retrieval provider, one exclusion glob** (L-4). It is not evidence that segregation works in general, and it raises no attestation grade — this is the same project that produced K-7.
- **Also, and this is the finding rather than the headline:** **the regex row did not improve enough to matter, and the reason generalises.** Its residual is **the project's own notes**, not the vendor's. Exclusion cures a *foreign-share* problem and does nothing for a corpus that is simply large about its own subject — and **the two are indistinguishable from the symptom**, which is a search returning more than anyone will read. A project that fixes its foreign share and expects search to work will be wrong for a reason it has no way to see from the failure.

### `O-46` · `2026-08-01T22:00Z` — measured here
- **Conditions:** as `O-45`, attempting to re-run the first of `O-35`'s three queries.
- **Observed:** `search_semantic` **fails outright** — *"daemon binary compiled without embeddings feature"*. The provider is at version `2.3.2` and its embeddings default is off. `O-35`'s instance (1) recorded a semantic query returning a specific similarity score on `2026-07-30`, so the capability existed then.
- **Initial read:** `UNVERIFIED` — possibly a version change, possibly a hybrid path that never needed embeddings.
- **Confidence:** `UNRESOLVED`. **What would settle it:** the provider version that produced `O-35`, which nobody recorded. Until then the fact stands and the cause does not.
- **Also:** this is the retrieval ladder's **top rung**, absent, on the instrument of the project that wrote the ladder — discovered only because something went looking. It is the exact shape `08-instruments.md` warns about in the ladder note: relevance ranking is *"the only rung that silently returns a worse answer rather than no answer"*, and here it does not even fail silently, it simply is not there. **A ladder is a claim about rungs, and a rung nobody has stood on this week is a hypothesis.**

### `O-47` · `2026-08-01T22:00Z` — measured here
- **Conditions:** the same session's K-4 re-measurement of the consuming project's capability inventory, its first full pass since `2026-07-27`.
- **Observed:** four facts had changed underneath a declaration that reported none of them. Repository **1,035 → 1,093** commits. Open work items **31 → 48**. The refinement endpoint **200 → 401**. And the credential **gained a scope** — `project` — whose absence that file recorded as instrument debt, with a note that re-scoping was the operator's to do. It had been done; nothing told the file.
- **Initial read:** `UNVERIFIED`.
- **Confidence:** `CONFIRMED` by direct measurement against the figures the file itself recorded.
- **Also:** **three of the four are capability *gains*, and K-4 is written as though drift means decay.** A declaration that is stale in the direction of under-claiming is still wrong, and it is worse than it looks: it makes a project route around a capability it already has, and it produces exactly the `UNRESOLVED` debt entry that says *"stopped at, operator-owned"* about something the operator already granted. K-4 says re-measure when the environment changes; **nothing says the change might be in your favour.**

---

`INTAKE CLOSED` · `2026-08-01T22:03Z` · **3 entries** (`O-45`–`O-47`).

**What this window did not look at.** Whether segregation holds on any other retrieval provider,
whether the excluded corpus is reachable by every tool or only the two that were tried, and why the
embeddings feature is absent. The window tested **one** remedy on **one** instrument, immediately
after writing the rule it tests, by the session that wrote it — which is the non-independence
`04-verification.md` names and is the reason none of this raises a grade.

---

`INTAKE OPEN` · `2026-08-01T22:25Z` · **window: a second consuming project re-vendored the corpus
and reported back.** The subject is that project's report, not that project.

### `O-48` · `2026-08-01T22:32Z` — measured here
- **Conditions:** a second project with Astronomer installed re-vendored from `4a33900` to `6cd9f65` and sent back a written report. Reading the report, and checking its two falsifiable claims against this corpus directly rather than accepting them.
- **Observed:** the report's sentence *"Left open as `D-044`"* appears one paragraph after it cites `AST-D-049`. **`D-044` is an allocated entry in this repository's own ledger.** Checked here: the `AST-D-<n>` convention appears in `install/README.md` at five places, and **zero times in `install/CLAUDE.md.template`** — the file a session actually loads. Also checked: the report's claim that `L-18` sits between `L-12` and `L-13` is **correct** (file order is `L-1`…`L-12`, `L-18`, `L-13`…`L-17`), and it had self-corrected an earlier `tail`-induced misreading before asserting it.
- **Initial read:** `UNVERIFIED` — possibly one session being loose with a prefix.
- **Confidence:** `CONFIRMED` as the **third instance of the namespace class**, not a slip. (1) A source project ran two live `D-` namespaces and published a disambiguation rule after the fact — the scar `00-precedence.md` cites. (2) `install/README.md` instructed the first real install to create a rival `DECISIONS.md`; caught only by refusing it (`D-045b`). (3) This. **The rule existed and was correct; it was in the wrong file.**
- **Also, and this is the part worth keeping:** this is `D-044`'s own finding recurring, on `D-044`'s own number, by coincidence. That entry moved the instruments material into the install layer because *"doctrine a session never reads is not in force"* — and the same defect was two files away the whole time, on a different rule, unnoticed for as long as the framework has had two ledgers. **A fix that relocates one rule does not relocate the class.**
- **Action:** gate, not a fourth restatement (L-17). `check_template_carries()` asserts that rules load-bearing at session time appear in the always-loaded file, and that the README still explains anything the template carries — both directions, because the mirror image is the same gap.

### `O-49` · `2026-08-01T22:32Z` — measured here
- **Conditions:** the same report states it re-measured dangling links in its vendored copy at **2, "both expected."** Measuring the same thing here rather than accepting or disputing it.
- **Observed:** a real five-directory vendored copy — this framework's other consumer — carries **11 dangling relative links across 9 distinct targets**. Nine originate in `CHARTER.md` and `DECISIONS.md` and point at `tools/` and `install/`; two are unfilled template placeholders. `O-29` recorded **10** for the same shape on 2026-07-27.
- **Initial read:** `INFERENCE`, and it is not that either measurement is wrong — the reporting project probably vendored a **smaller set**, omitting `CHARTER.md`, `DECISIONS.md` and `artifacts/`, which is permitted (`install/README.md` makes the first two conditional on *"if you want `AST-D-<n>` citations to resolve"*).
- **Confidence:** `UNRESOLVED`. **What would settle it:** the vendor set that project actually copied — one directory listing, which this session does not have.
- **Also:** if the inference holds, the two findings are the same finding. **A project that skips the optional ledger has no `AST-D-` citation that resolves anywhere in its tree**, which removes the last thing that would have made the missing prefix visible — and `O-48` is what that looks like from the outside. The install layer treats vendoring the ledger as a convenience; it is also the only local evidence that a second namespace exists.

---

`INTAKE CLOSED` · `2026-08-01T22:33Z` · **2 entries** (`O-48`–`O-49`).

**What this window did not look at:** the reporting project itself. Nothing of its filesystem was
read, no claim about its state was verified at the source, and `O-49` is `UNRESOLVED` precisely
because settling it needs one directory listing this session did not take. Every finding here is
about **this corpus**, derived from a report about it.

---

`INTAKE OPEN` · `2026-08-01T22:55Z` · **window: the second consuming project measured its own
retrieval surface and found most of its corpus missing.** Its report is the subject; its filesystem
is `RED` under this session's data boundary and was not read.

### `O-50` · `2026-08-01T23:02Z` — measured here
- **Conditions:** the reporting project claimed *"the root cause is that `install/README.md` names `.claude/` as the default home for the governance corpus."* Checking that against the file rather than accepting it.
- **Observed:** **`install/README.md` names no home for the vendored tree at all.** It says vendor the five directories *"as siblings under one parent"* and stops. It does name `.claude/` repeatedly — for `CLAUDE.md` (line 107), for the eight skills (line 160–170), and as the collaborator's workspace (line 258, *"commonly `.claude/`"*).
- **Confidence:** the claim as stated is `REFUTED`. **The defect underneath it is `CONFIRMED` and is worse:** the one location a reader is repeatedly shown is `.claude/`, the location that actually matters is left blank, and nothing anywhere warns that a hidden directory is invisible to default tooling. Two installs, two different answers — one chose `docs/astronomer/`, one chose `.claude/`.
- **Also:** this is what an unspecified default looks like from the outside. Nobody made a wrong decision; the framework declined to make one and both readings were defensible.

### `O-51` · `2026-08-01T23:00Z` — measured here
- **Conditions:** the same report's tooling claim, re-derived on this machine against a two-directory fixture rather than accepted from its figures (L-11).
- **Observed:** `rg` without `--hidden` returns **only** the non-hidden file. `rg --hidden` returns both. Python `glob("**/*.md", recursive=True)` returns **only** the non-hidden file. `os.walk` returns both. `find` returns both. The report adds Obsidian's indexer to the blind list, which this session did not test.
- **Confidence:** `CONFIRMED` for the four tools measured here; `CITED` for Obsidian. **Three of five common instruments cannot see a corpus under a dotted path**, and the two that can are the two nobody reaches for first.
- **Also, and it is the sharpest part of the report:** its **second** instance was its own measurement script, written *minutes after* it documented the first. Knowing about the blind spot did not prevent it. That is `O-39`'s finding in a new domain — a rule known, correct and freshly rehearsed does not thereby bind — and it is the strongest argument yet that this class wants a mechanism rather than a warning.

### `O-52` · `2026-08-01T23:02Z` — inference, labelled
- **Conditions:** relating `O-50` to `K-7` and to `AST-D-045`.
- **Observed (the two facts):** `AST-D-045` recorded that `.claude/` is gitignored in many repositories, which made a filled `CLAUDE.md` invisible to every clone. `O-50` records that `.claude/` is invisible to most search tooling, which makes a vendored corpus unfindable.
- **Initial read:** `INFERENCE`, and it is the useful one — these are **one class, not two coincidences**: *`.claude/` is a directory other tools treat specially, and the install layer keeps putting load-bearing material there without saying so.* Two instances.
- **Confidence:** `PROVISIONAL`. **Reopens on a third instance**, at which point L-17 requires a mechanism rather than a third warning. Not built now, deliberately — `tools/README.md` records that this corpus builds gates on the third and argues itself into them earlier at its own cost.
- **Also:** it interacts badly with the role added today. A poisoned index ranks your own material low; a hidden directory means it is **not in the index at all**, and `corpus-retrieval.md` step 6 already names *not findable* / *not written* as indistinguishable. **K-7 assumed the corpus was in the index.** Nothing said so.

---

`INTAKE CLOSED` · `2026-08-01T23:03Z` · **3 entries** (`O-50`–`O-52`).

**What this window did not look at:** the reporting project. Its folder is `RED` and was not read;
every claim about it here is quoted from its report and labelled as such. Obsidian's indexer was not
tested. Whether any *other* framework instruction points at a hidden path was not swept for.

---

`INTAKE OPEN` · `2026-08-02T00:50Z` · **window: one question — can the framework's own retrieval
provider see the framework's own install location?**

### `O-53` · `2026-08-02T00:52Z` — measured here
- **Conditions:** a purpose-built fixture vault in scratch space, served by the same `obsidian-mcp` binary this project uses, on a spare port so the live server was untouched. Three markdown files: **two** under `.claude/doctrine/`, **one** under `notes/`. The binary's own startup log reports the index size, so the measurement needed no client.
- **Observed:** `tantivy BM25 index built notes=1`. **The indexer saw one file of three.** Both files under the dotted path were skipped. The live server was verified unaffected afterward (362 notes, exclusions intact).
- **Initial read:** `UNVERIFIED` — possibly a fixture artifact.
- **Confidence:** `CONFIRMED`. The count is exact and the fixture is trivial. This makes **four** instruments measured here with the same blind spot — `rg` (default), Python `glob(recursive=True)`, Obsidian's own app (`CITED`, still not re-derived), and now the MCP server. Against two that see through it: `os.walk` and `find`.
- **Also, and this is why it is its own entry rather than a line in `O-51`:** the other three are general-purpose tools this framework does not recommend. **This one is the retrieval provider a project would stand up *because* `08-instruments.md` told it to fill the corpus-retrieval role.** So the framework points at a home in one file and at an instrument that cannot read that home in another, and a project following both correctly ends up with a search engine over the fraction of its corpus that is not governance. **That is worse than no index**, because an index confers authority: `corpus-retrieval.md` step 6 says *not findable* and *not written* are indistinguishable, and an empty result from a real search engine reads as settled.

---

`INTAKE CLOSED` · `2026-08-02T00:53Z` · **1 entry** (`O-53`).

**What this did not look at:** whether the provider has a setting that changes this (its `--help`
exposes `OBSIDIAN_EXCLUDE_PATHS` but nothing about *including* hidden paths, and that was not
pursued), and whether Obsidian's own application behaves identically — still `CITED` from the
consuming project's report, not re-derived here.

---

`INTAKE OPEN` · `2026-08-02T01:00Z` · **window: the operator refused a claim in this log, and was
right.** Opened because `O-46` was challenged, not because anything new happened.

### `O-54` · `2026-08-02T01:35Z` — measured here. **`O-46` is `REFUTED`.**
- **Conditions:** the operator said the semantic-search claim *"cannot possibly be true"* and that the instrument works. Re-testing rather than defending, then following the error rather than the conclusion.
- **Observed:** `search_semantic` still failed with the same text, so the symptom was real. But the text says *"**Daemon** RPC error"*, and the provider is **two processes, not one**. Enumerating them found **two `obsidian-semanticd.exe` binaries, both version `2.3.2`**: one at `AppData/Roaming/obsidian-semantic/bin/` of **9,923,072 bytes**, one at `~/.cargo/bin/` of **12,845,568 bytes**. `manifest.json` **pins `binary_path` and `binary_sha256` to the smaller one**, and the MCP server bootstraps whatever the manifest names. Swapping in the larger binary moved the error to `vault not ready; call ensure_vault first`, then — with embeddings enabled — to `API key required: set OBSIDIAN_EMBEDDING_API_KEY or OPENAI_API_KEY`. Also measured: the MCP **server** binary reports `local embedding backend not compiled`, so its local path is genuinely absent; the daemon's `fastembed-cache` is **empty**; and a `5,092,054`-byte `embeddings.bin` from `2026-07-29` exists for one vault, which is when `O-35`'s semantic query worked.
- **Confidence:** `REFUTED` for `O-46`. The feature is **not** absent from the installation. The wrong binary was pinned, and behind it the remaining blocker is a **credential** — which is custody, was not supplied, and was not sought. **Semantic search has still not been observed working**, so the correct statement is *"blocked on an operator-supplied credential,"* not *"unavailable,"* and certainly not *"compiled without embeddings."*
- **Also — the failure is not the wrong answer, it is the shape of the reasoning.** `O-46` quoted an error message and adopted its framing as a property of the environment. It then graded itself `UNRESOLVED` and named *"the version that produced `O-35`"* as what would settle it — which sounds like rigour and was the wrong question, because **both binaries are version `2.3.2`**. A version string cannot distinguish them; only size and behaviour can. **The honest-looking `UNRESOLVED` was worse than a bare guess**, because it closed the question with a plausible investigation nobody would re-open.

### `O-55` · `2026-08-02T01:35Z` — measured here
- **Conditions:** tracing where `O-46`'s claim travelled before it was refuted, roughly four hours later.
- **Observed:** it reached **five documents and one outbound brief** — this log (`O-46`), the ledger (`D-050`'s caveat), the consuming project's capability inventory (twice) and its always-loaded `CLAUDE.md`, and a written handoff to a **second** consuming project that had independently and correctly identified the credential as its blocker. That brief told it the credential was moot.
- **Confidence:** `CONFIRMED` by grep across both repositories.
- **Also, and this is the entry worth keeping:** the second project had the right answer and was told by this one that it was wrong. **A false claim from an upstream corpus does not merely sit there — it overrides correct local findings**, because the consumer defers to the framework by design. `L-11` says trust no quoted number *including this file's*; this is the same rule for a quoted **diagnosis**, and the corpus had no equivalent warning. The install layer now carries the diagnostic ladder itself (`install/retrieval-setup.md`) so the next project reads error text against a table instead of against a conclusion someone else drew.

---

`INTAKE CLOSED` · `2026-08-02T01:36Z` · **2 entries** (`O-54`–`O-55`).

**What is still not known.** Whether the local-embedding path can be made to work on this machine at
all (the server binary lacks the feature; whether a build with it exists was not pursued), and
whether semantic search functions once a credential is supplied — **nobody has seen it work**, and
this window did not change that. The credential is custody and was not sought.

---

`INTAKE OPEN` · `2026-08-19T22:04Z` · **window: the fleet that a design brief proposed shipping an
installer to, measured before anything was shipped.** Opened because
`design/distribution-and-scope.md` §11 instructed that the
normalised comparison be run across the whole fleet *"before step 1"* and that two runtime unknowns
be settled with a fixture — *"Do this first"* — and neither had been done. Nothing in any instance
was modified during the pass (L-7). Instrument: [`tools/fleet-census.py`](tools/fleet-census.py),
written for this window and verified by [`tools/verify-census.py`](tools/verify-census.py) before
its clean output was used.

### `O-56` · `2026-08-19T22:11Z` — measured here. **The brief's fleet size is `REFUTED`.**
- **Conditions:** the brief opens *"Astronomer lives in ~30 project instances maintained by hand"* and repeats the figure in `D11` and §9. It cites no measurement for it. Searching `~/Documents` for any directory holding `.claude/skills/astronomer-*`.
- **Observed:** **9 install points**, in `Photopipe`, `<instance-C>`, `<worktree-A>`, `<worktree-B>`, `vociferous-next`, `Franklin`, `<instance-E>`, `Presentations/The Engineer's Dilemma`, `<instance-D>`. Four of the nine are **outside `DevSlop/` entirely** and would have been missed by a sweep of the directory the brief was written in. Of the nine, `<worktree-A>` and `<worktree-B>` carry a `.git` **file**, not a directory, reading `gitdir: .../vociferous-next/.git/worktrees/...`; `git worktree list` confirms all three are checkouts of one repository. **Distinct projects: 7.**
- **Confidence:** `CONFIRMED`. Exact count, reproducible by `python tools/fleet-census.py`.
- **Also, and this is why the worktree finding is not a footnote:** the same drift is present in all three checkouts, so a census that treats them as instances reports one project's four artifacts as nine and **triples the apparent cost of the very problem the installer exists to solve**. It also means an installer would write to three working copies backed by **one git index**. The brief's §5.5 fan-out loop (`for d in ~/Documents/DevSlop/*/`) does exactly that, and would additionally have missed the four install points outside `DevSlop/`.

### `O-57` · `2026-08-19T22:11Z` — measured here. **`stale` and `drifted` are different things, and the brief's design cannot tell them apart.**
- **Conditions:** the brief's §5.3 lockfile classifies every managed file as **clean** or **drifted**, and §5.4 has `astro update` refuse to touch anything drifted. Classifying all 444 managed files across the 9 install points against upstream, on LF-normalised content, and — where a file did not match `HEAD` — against **every commit in upstream's history** for that path.
- **Observed:** **387 match `HEAD`.** Of the 57 that do not, **48 are byte-identical to a commit upstream actually shipped** — 45 of them in `<instance-C>` alone, all matching `4a33900e` (2026-07-26). That project has **edited nothing**; it is simply 45 files behind. Only **9** files match no upstream version that ever existed, and those fold to **4 distinct artifacts across 2 of the 7 projects**.
- **Confidence:** `CONFIRMED`. The classifier was observed failing first: `tools/verify-census.py` removes the history lookup and confirms the stale check goes red.
- **Also — the cost of the two-way split, stated concretely.** Under §5.4 as written, adopting the installer in `<instance-C>` refuses 45 files, writes 45 `.incoming` files, and hands the operator **45 decisions that are all the same decision**. That is the failure the brief names for itself in §4.2 — *"the operator learns to ignore the one signal the system exists to produce"* — reached by a second route it did not check. **The brief diagnosed the disease and missed the second vector.**

### `O-58` · `2026-08-19T22:11Z` — measured here. **The largest drift the brief reported is not in the fleet.**
- **Conditions:** the brief names `install/retrieval-setup.md` as the one drift *"large enough to be a real divergence rather than an addition"* (20 lines) and schedules it for hand review in §8 step 1. Diffing each instance's copy against upstream `HEAD` rather than against upstream's working tree.
- **Observed:** **four of five instances that carry the file are identical to `HEAD`** — zero diff lines. The fifth, `Photopipe`, does not have the file at all. The 20 lines are the `PROMOTED 2026-08-04` block recording `COAW-D-041`, and they are an **uncommitted change in upstream's own working tree**, visible in `git status` as a modified `install/retrieval-setup.md` at the moment the brief was written.
- **Confidence:** `CONFIRMED` by diff against `git show HEAD:install/retrieval-setup.md`.
- **Also:** the brief measured a **dirty working tree** against the fleet and attributed the difference to the fleet. The direction of the error matters more than its size — it reported that *the fleet had diverged from upstream* when in fact *upstream had unpublished work*. The remedy is not review; it is a commit. `O-57`'s reclassification has the same root: `skills/astronomer-start`, the brief's third drift, is **stale** — it matches `4a33900e`, and upstream later added `K-7`.

### `O-59` · `2026-08-19T22:11Z` — measured here
- **Conditions:** the brief records **2** orphaned capabilities, both found in `vociferous-next`, and notes *"drift is bidirectional; the mechanism must be two-way."* Checking every install point rather than one.
- **Observed:** **4.** The two named (`rituals/deliberation-thread.md`, `skills/astronomer-supervise/`) plus `rituals/README.md`'s row for the first — and a **fourth in a project the brief never opened**: `<instance-D>`' `astronomer-intake/SKILL.md` carries a 27-line addition, *"Step 2a — scan for what expires, before you scan for what is readable,"* stamped `TRIAL — added 2026-08-03T12:20Z, operator tentatively approved (<instance-D> D-029)`. It carries its own scar: an 8-file corpus was counted, converted, manifested and closed before anyone read the handoff note saying the deliverable was due **that same day**.
- **Confidence:** `CONFIRMED`.
- **Also:** it is a rule with a scar and an operator approval, living in exactly one directory on this machine, in a project outside the one the brief surveyed. An installer that ran before harvesting would have overwritten it — the brief's own §8 ordering (*harvest precedes installation*) was right, for a reason it had only half-measured. **A survey of one instance cannot find what only another instance learned**, which is the same shape as `O-55`: the framework's reach is wider than the window that measures it.

### `O-60` · `2026-08-19T22:15Z` — measured here. **Both runtime unknowns settled; the brief's `D4` and `D5` are `REFUTED`.**
- **Conditions:** the brief calls these *"the two highest-value unknowns"*, says to settle them by building a two-level fixture and observing what a session actually reads *"before implementing"*, and to **re-brief rather than work around** an answer that goes against the design. Two fixtures built: `parent/` and `parent/child/`, each with a distinct `CLAUDE.md` token and a distinctly-named skill. In fixture A the git repository root is at `parent/`; in fixture B it is at `child/`. A real `claude` session was run in `parent/child/` in each.
- **Observed:** **A** — both `PARENTMD_7Q4X` and `CHILDMD_9R2Y` present; `parentprobe` listed *and invoked*, returning `PARENTSKILL_5T8Z`. **B** — both `CLAUDE.md` tokens still present, but the skill probe returned the sentinel **`NOSKILL`**. So `CLAUDE.md` walks up to the **filesystem root and crosses repository boundaries**, while `.claude/skills/` walks up only to the **repository root** and does not cross.
- **Confidence:** `CONFIRMED`, falsified in both directions — the negative case was made to return a sentinel rather than merely omit a name from a list, so a silent listing failure could not be mistaken for absence. Corroborated by the vendor's published behaviour, which was read **after** the fixture, not before.
- **Also — the answer is neither branch the brief prepared for, and that is the finding.** §7.1 anticipated two outcomes: skills resolve from ancestors (so "everything once per chain") or they do not (so "skills at every scope"). Measured, **both docs and skills resolve upward and stop in different places**, so the correct unit is not the chain but **the repository**. The measured fleet already shows both shapes: `<instance-D>` is one repository spanning two scopes, so one skills install serves both; the seven projects under `DevSlop/` are seven repositories at one scope each. **A design shipped on either anticipated branch would have been wrong for half the fleet.**

### `O-61` · `2026-08-19T22:15Z` — measured here
- **Conditions:** running `tools/check-corpus.py` after the design directory joined the corpus. Not planned; the gate was run only to confirm nothing had been broken.
- **Observed:** **three failures, all pre-existing in the brief as delivered.** Two are the counted-prose check reading *"### 5.1 Ownership classes"* and reporting *"prose counts 1 'classes', registry has 4"* — the `1` is the **section number** `5.1`, matched because a word boundary sits between the period and the digit. The third is real: the brief declares *"supersedes: design/nested-scopes.md"* in prose while **both files still claimed `owns: scope-resolution`**, so a vocabulary had two homes in violation of `L-14`.
- **Confidence:** `CONFIRMED`. The false positive reproduces on any heading of the form `N.M <count-noun>`; the ownership collision was fixed by releasing the superseded file's claims.
- **Also, and it cuts both ways:** the gate caught a genuine `L-14` defect **in the document proposing to distribute the corpus**, which is the gate working. It also produced a false positive that `00-precedence.md` names in advance — *"a gate producing a false positive is a defect in the gate, and 'the guard is intentional' is not a licence for the guard to be wrong."* Both were fixed on the merits, neither by exemption: the regex now refuses a digit glued to a preceding period or digit, and `verify-gate.py` still passes. **A brief proposing to ship the corpus to nine projects did not itself pass the corpus gate**, and nothing would have caught that except running it.

---

`INTAKE CLOSED` · `2026-08-19T22:15Z` · **6 entries** (`O-56`–`O-61`).

**What this did not look at.** Whether the 7 projects want to nest at all — `<instance-D>` is the
only measured two-level structure, and it arrived without a design. Whether `<instance-E>`'s
skills-without-a-vendored-tree is deliberate or an incomplete install; it is clean either way, which
is precisely why the census cannot tell. Whether the fixture result holds for a repository boundary
established by something other than `.git` — only git was tested. And **nothing was measured about
whether an installer would work**, because none exists: this window measured the ground it would
land on, not the landing.

---

`INTAKE OPEN` · `2026-08-19T22:22Z` · **window: CHARTER definition-of-done condition 5, run as a
test instead of read as an assertion.** Condition 5 says *"The install layer can be dropped into an
empty repository and produce a working Lite project without editing any file in this repo."* It has
been claimed met since `2026-07-24` and had never been executed end to end from an empty directory.
A throwaway repository was created and `install/README.md` followed literally, then a real `claude`
session was run inside the result.

### `O-62` · `2026-08-19T22:26Z` — measured here. **Condition 5 holds, and is now `CONFIRMED` by execution.**
- **Conditions:** an empty `git init` directory. `install/README.md` steps 1–3 followed as written: vendor `doctrine/ rituals/ artifacts/ tiers/ provenance/` under the non-hidden parent `docs/astronomer/`, do not vendor `tools/`, fill `CLAUDE.md.template` at the repository root, copy the eight skills to `.claude/skills/`. No file in this repository was edited to make it work.
- **Observed:** the collaborator layer, the skills and the doctrine are all **tracked by git** — the `AST-D-045` failure mode did not recur, because the template landed at the repository root rather than under `.claude/`. All five documented placeholders exist in the template and all five are documented in the README; none survived unfilled. A session started in the result **knew the project name and tier from `CLAUDE.md`**, listed **all eight `astronomer-*` skills**, and answered *"What does `L-9` require?"* with *"The falsifier is written first — numeric, calibrated on the real measuring condition"* — which is `01-laws.md` `L-9` correctly, not a plausible invention. Asked mid-window to *"just go fix"* an obvious cause, it **refused under `L-7`**, quoted *"Not one line. Not the obvious thing,"* named hard rule 4, and said the apparent cause might mask another.
- **Confidence:** `CONFIRMED`. Two rows of this file's own *"Verify the install"* table were executed against a real session rather than assumed, and both passed.
- **Also:** the install is **twenty minutes of copying and produces a project that behaves**, which is the claim the framework has been making about itself for four weeks without anyone running it from empty. It was worth running. It also found three defects that only appear when you actually do it — `O-63`.

### `O-63` · `2026-08-19T22:26Z` — measured here
- **Conditions:** the same install, checked for unfilled placeholders and for markdown links that do not resolve **in the vendored copy** rather than upstream.
- **Observed:** three defects, none fatal, all invisible from inside this repository. **(1)** `install/README.md`'s closing section read *"CHARTER definition-of-done §6 is the only condition standing between this framework and `VALIDATED`"* — **four hundred lines below a status box in the same file saying `VALIDATED` as of `2026-08-01`**. One file, two answers about its own status. **(2)** The vendoring instruction offered *"plus this repo's `CHARTER.md` and `DECISIONS.md`"*; taking exactly that leaves the copied ledger citing an `OBSERVATIONS.md` that was never copied — a citation that resolves upstream and silently does not in the consuming project. **(3)** The stated exemption *"links into `tools/` and `install/` are the only ones expected to dangle"* omits **template-relative links**: `artifacts/charter.template.md` links to the `DECISIONS.md` the *filled* charter will sit beside, which cannot resolve until the template is copied out.
- **Confidence:** `CONFIRMED`. All three reproduce on a clean install; all three are fixed, and the fix for (2) is *take all three governance files or none*.
- **Also, and it is the same shape as `O-58`:** every one of these is a defect **you cannot see from where the document is written.** `tools/check-corpus.py` verifies every link *in this repository*, and all three of these links are fine here — they only break after the corpus is copied somewhere with a different shape. **The corpus gate checks the corpus; nothing checked the copy**, and the install layer is precisely the part of this framework whose correctness lives in the copy. A one-off harness found them in minutes; it is deliberately not shipped, because CHARTER "Out of scope" bars tooling that validates projects (`D-005`) and this window was not the place to test that bar.

---

`INTAKE CLOSED` · `2026-08-19T22:30Z` · **2 entries** (`O-62`–`O-63`).

**What this did not look at.** The remaining ten rows of the *"Verify the install"* table — two were
executed, the rest are still assumed. Step 0a (adoption over work in progress), Step 4 (retrieval)
and Step 5 (role bounds) were **not** exercised; the test was a greenfield Lite install and says
nothing about the adoption path, which is the harder one and the one `AST-D-045` came from. Whether
the install works on a non-Windows filesystem, and whether it works for a project that already has a
`D-` ledger, are both untested.
