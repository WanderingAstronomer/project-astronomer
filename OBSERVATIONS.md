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
