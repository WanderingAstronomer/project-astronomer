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
