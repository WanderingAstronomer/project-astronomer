# Lineage

> **Frozen record.** Point-in-time: this is the extraction as performed on 2026-07-20, from the
> four source projects in the state they were in on that date. Do not edit it to reflect later
> understanding — annotate if superseded.

Provenance is a first-class column (CHARTER invariant 4, D-006). This file is the receipt for
every pattern in the doctrine: where it came from, how many projects arrived at it
independently, and what it cost them to learn.

---

## The source projects

Four projects, no shared domain, no shared codebase, not coordinated, and none of them written
with a framework in mind. That independence is the only validation signal available here — there
was no control group and no pre-registration, so **convergence across unrelated domains is
doing all the epistemic work.**

| Code | Project | What it is | Scale at extraction |
|---|---|---|---|
| **VOC** | `vociferous-next` | Transcription and refinement platform; medical/compliance posture | ~20 doc trees, 19 catalogued systems, 452 catalogued items, multi-session concurrent workstreams |
| **OD** | `OpenDrop` | Civic donation-location mapping service, publicly deployed | 61 commits, 8 blocking CI gates, four permanent docs plus disposable working docs |
| **FR** | `<instance-F>` | Retrieval-architecture proof of concept | 986-line authoritative specification written before any code; not a git repository |
| **DD** | `data-dating` | Personal research study — **non-software** | 4 commits, 23 files, four-tier authority stack |

**DD matters disproportionately.** It is the only source project that was not software, and it
is therefore the only existing evidence that the methodology survives the translation Astronomer
is betting on. Its charter contains a literal two-column table mapping inherited patterns from
its sibling projects onto a non-software domain — which is, in miniature, exactly what this
repository is.

**FR matters for a different reason.** It is not under version control, and it still achieved
provenance: a frozen authoritative specification, deviations recorded as prose *at the site of
each deviation* with its justification, and bugs memorialized as named regression checks whose
descriptions are the incident reports. This is the proof that Astronomer is tooling-agnostic —
the discipline is the artifact set, not the version control.

---

## Attestation matrix

Every law, with its independent arrivals. Three or more is strong; two is a law; one is marked
provisional and should be treated as a hypothesis about method rather than a finding.

| Law | VOC | OD | FR | DD | Count |
|---|:--:|:--:|:--:|:--:|:--:|
| L-1 One document wins | ● | ○ | ● | ● | **3** |
| L-2 Supersede by name | ● | | | ● | **2** |
| L-3 Observation ≠ inference | ● | ● | ● | ● | **4** |
| L-4 Scope is mandatory | | | ● | ● | **2** |
| L-5 Co-occurrence ≠ shared cause | ● | ● | | | **2** |
| L-6 Refutation is a result | ● | ● | | ● | **3** |
| L-7 No changes during observation | ● | ● | | | **2** |
| L-8 Validate small first | | | ● | ● | **2** |
| L-9 Falsifier written first | | ● | ● | ● | **3** |
| L-10 One variable at a time | ● | | ● | | **2** |
| L-11 Measure your own baseline | ● | ○ | ○ | ○ | **1** ⚠ |
| L-12 Verify at the right altitude | ● | ● | | | **2** |
| L-13 Frozen vs living | ● | ● | | ● | **3** |
| L-14 Vocabulary has one home | ○ | | ● | ● | **2** |
| L-15 Name the non-delegable | ● | | ● | | **2** |
| L-16 Never leave the lie | ● | ● | | ● | **3** |
| L-17 Gate, don't re-fix | ● | ● | | | **2** |

● explicit and stated as a rule · ○ present in practice or by a different route, not stated as a rule

**L-11 is the framework's weakest law** and is marked so in the doctrine. It is stated
explicitly and forcefully in exactly one project. The three circles beside it are adjacent
instincts arriving by other routes — a live read-only progress dashboard, a "measured-only, never
inferred" invariant — not the same rule. It stays in because its scar is unusually specific and
because its failure mode is unusually cheap to check for. It should be the first law reviewed
after a real project runs on this framework.

---

## Section-level provenance

| Doctrine section | Primary sources | The pattern taken |
|---|---|---|
| `00-precedence` | FR, DD, VOC | The precedence clause, near-verbatim in three projects; VOC's settlement pass supplies the failure case |
| `01-laws` | all four | See matrix above |
| `02-epistemics` — typed claims | DD, FR | Claim as the atomic unit; taxonomy cut on epistemic status rather than topic |
| `02-epistemics` — the null bucket | FR, DD | `TRANSITIONAL` and its degeneracy ceiling as a live health signal on the classifier |
| `02-epistemics` — scope trap | DD | Mandatory scope, `ASSERTED-UNIVERSAL`, and the audience-attribute contamination rule |
| `02-epistemics` — interrogation frame | FR | The five fixed questions; taken essentially unchanged |
| `02-epistemics` — consensus ≠ effect | DD | Restated by that project at every point of use, deliberately |
| `02-epistemics` — evidence tiers, thin coverage | DD | Two-tier grading; thin cells labelled rather than omitted |
| `03-the-loop` — phases | VOC | Intake → triage → root-cause → execute; **RECORD added here** (D-013), not inherited |
| `03-the-loop` — buckets A–E | OD | Bucketing by epistemic state rather than severity; bucket E in particular |
| `03-the-loop` — clusters | VOC | "Clusters are the deliverable" |
| `03-the-loop` — recording voice | OD, VOC | Outcome subject, causal mechanism line, verification evidence, disclosed debt |
| `04-verification` — refutation bias | VOC | The verifier prompt's "default toward refuted" |
| `04-verification` — blind parallel adjudication | DD | Extractor and gold adjudicator run blind; scored mechanically, not by a model |
| `04-verification` — break-the-check | VOC | Mutation testing, and the same-millisecond determinism failure |
| `04-verification` — instrumentation | FR | Heartbeat with tallies, out-of-band dashboard, checkpoint per expensive unit |
| `04-verification` — preflight | FR | Scoped per phase, remedy in every message, no silent fallbacks |
| `04-verification` — gate menu | OD | Ratchet, refuse-to-start, run-twice idempotency, restricted-posture re-run, incident-derived check |
| `05-the-record` — three classes | OD | Four permanent documents plus deliberately disposable working docs |
| `05-the-record` — frozen rule | VOC, DD, OD | "Do not edit to reflect new truth"; corrections as addenda |
| `05-the-record` — ledger format | DD, VOC | Format, live timestamps, `blocks-on:`, `caveat (owned):` |
| `05-the-record` — ID permanence | VOC, OD | Never renumber; retire, don't reuse; `E4→B9` migration form |
| `05-the-record` — housekeeping | VOC | Dated move blocks; "no deletions, every record relocated and re-annotated" |
| `06-delegation` — roles | VOC | Operator / coordinator / session / verifier, and the boundary the operator had to restate |
| `06-delegation` — non-delegable categories | VOC, FR | Five categories; **"Preference" added here**, not inherited |
| `06-delegation` — fences | VOC | One owner per item; do-not-fix-outside-your-scope; the collision analysis |
| `06-delegation` — brief structure | VOC | Seven parts, shared preamble by reference |
| `06-delegation` — decide/document/flag | VOC | Including the cheap-to-reverse constraint |
| `06-delegation` — report contract | VOC | Six sections; own-defects and not-verified are the load-bearing two |
| `tiers/` | — | **Original to Astronomer** (D-011). No source project tiered its own rigor |

---

## Original to Astronomer — flagged, not inherited

Under the framework's own rules these are single-authored and therefore weaker than everything
above. They are listed together so they are easy to find and revise after a real project runs.

1. **The five-phase loop with RECORD named separately** (D-013). Source projects used four
   phases and let recording happen inside execution. The argument for splitting it is that
   recording is the first thing dropped under pressure — plausible, and untested.
2. **The "Preference" non-delegable category.** The four inherited categories are all structural
   (identity, custody, acceptance, physical fact). Preference is different in kind and dominates
   outside software. Untested.
3. **Tiering** (D-011). No source project tiered. The Lite/Standard/Full split and its artifact
   assignments are a design judgement about adoption, not an extracted finding.
4. **The astronomy frame** (D-012). The mapping is defensible term by term, but the source
   projects did not use it, and a metaphor that generates good vocabulary can also generate
   confident nonsense. Watch for terms admitted because they sound right.

---

## What this extraction cannot tell you

Stated plainly, because a provenance document that only lists strengths is doing the opposite of
its job.

**Survivorship.** All four source projects worked. The methodology is reconstructed entirely
from successes, so it cannot distinguish *what made them work* from *what they happened to do*.
A practice present in all four might be load-bearing, or might be a shared habit that cost
nothing and contributed nothing.

**No counterfactual.** Nobody ran these projects without the methodology. The comparison that
would establish causation does not exist and cannot be constructed retroactively.

**Reconstruction bias.** This extraction was performed after the outcomes were known, which is
exactly the condition under which narrative tidiness outruns evidence. The abandoned approaches
are not in the repositories; the surviving ones are, and they look inevitable.

**The scars are second-hand.** Every war story in the doctrine was read out of a document, not
lived by the author of this framework. Some are certainly compressed, and a compressed incident
loses the ambiguity that made it hard at the time.

This is why the corpus ships as `PROVISIONAL` (D-001) and why condition 6 of the definition of
done — *a real project outside this repo has run one full loop on it* — is the only thing that
would move it. Until then, Astronomer is a well-argued guess about what worked.

---

## Addendum — 2026-07-24

**This does not revise the extraction above; it records what came after it.** The original
four-project extraction stands as written on 2026-07-20.

A fifth, external, unrelated engagement — code **BK** (`Berman & Killeen`, a forensic-psychology
practice; not one of the four source projects and not part of this corpus) — used Astronomer as an
**analytical lens** on its own AI-collaborator prompts, and its working `Claude/` directory
independently converged on two patterns absent from the seeded artifact set:

1. A **data-boundary classification** (RED / GREEN / YELLOW) for what an AI collaborator may read,
   grounded in a live scar: a subpoenaed, legally privileged case file and raw financial exports
   sitting in the same directory the collaborator had standing access to, with no written boundary
   until one was made explicit — at which point an existing compliance commitment (a signed BAA)
   was found already in tension with an unflagged privileged file nearby.
2. A **collaborator workspace layout** — a directory the collaborator uses freely, separate from the
   project's own artifacts, opened with a `README.md` that states its authorization and points to one
   "read this first" living document.

Both are now `artifacts/data-boundary.template.md` and part of the new `astronomer-start` skill
(`install/skills/astronomer-start/`), per `DECISIONS.md` D-023.

**Marked single-attested and provisional (D-006), on both counts, deliberately:**

- **BK did not run a full OBSERVE→RECORD loop on Astronomer.** It was consulting work *about* an
  account, not a project *governed by* the framework end to end. CHARTER definition-of-done
  condition 6 is **not** satisfied by this addendum, and this addendum does not claim it is.
- Two patterns from one outside source is exactly the attestation level D-006 calls a *practice*,
  not a *law* — the same caution the original extraction applied to L-11 applies here, doubly, since
  this is a single source rather than one-of-four.
- The next real project that uses `astronomer-start` is what would move either pattern toward
  independently-attested. Until then, treat both as reasonable, unproven additions — exactly the
  posture this framework asks of everything else in it.

---

# Addendum — 2026-07-24T20:46Z

> Like the addendum above, this **does not re-run or revise** the 2026-07-20 extraction. It records
> what the first self-survey of this corpus found unattributed, and attributes the material added
> since. Everything above this line stands as written.

## Part 1 — patterns that were never attributed

CHARTER definition-of-done condition 4 requires every doctrine section to name its sources, with no
unattributed patterns. The section-level table above covers `doctrine/00`–`06` and `tiers/`. Four
things it does not cover, found by survey rather than by anyone auditing the condition:

| Unattributed | Status | Note |
|---|---|---|
| The **`rituals/` layer** — all files | **Original to Astronomer** (D-017) | No source project had a framework-level procedure layer distinct from project runbooks. VOC and OD both had domain procedures; the *separation* is new here, and D-017's test is the new part: if the procedure cannot be written without naming your subject, it is a runbook. |
| The **Friction / Conflagration** blast-radius axis | **Original to Astronomer** (D-018) | Arrived by correction, not design: the axis was first called "severity," collided with the existing per-item severity scale, and was renamed. The first fix documented the collision instead of removing it, which is the L-17 failure — a re-taught trap rather than a closed one. |
| The **`artifacts/` template set as shapes** | **Mixed; per-artifact** | The *patterns* are attested via the doctrine rows above (ledger → DD, VOC; brief and report → VOC; catalog → OD). The **rendered templates** — section order, mandatory fields, worked examples — are Astronomer's, single-authored. No source project shipped a blank template; each had a filled instance. |
| The **`Append-only` record class** | **Original to Astronomer** (D-019) | Row `05-the-record — three classes → OD` above is correct **as of 2026-07-20** and is left standing. D-019 added the fourth class the next day. OD supplied three; the fourth is not inherited. |

The `rituals/` and blast-radius entries should have appeared in **"Original to Astronomer"** above
and did not. That list had four items; it has eight. Recording the omission rather than
back-filling the original list, because the original list is evidence of what the extraction
noticed at the time — which is the entire reason that section is frozen.

## Part 2 — the boundaries layer, and why it is the weakest thing here

`doctrine/07-boundaries.md`, `artifacts/query-log.template.md`,
`artifacts/source-manifest.template.md`, `artifacts/capability-inventory.template.md`,
`rituals/corpus-intake.md`, `rituals/external-research.md`, and the `astronomer-intake` and
`astronomer-research` skills, added 2026-07-24 (D-031 – D-033).

| Rule | Attestation |
|---|---|
| **B-1** read access ≠ egress | **BK**, partially — BK's scar produced the read classification. The egress half is single-authored; BK classified what could be opened, not what could be sent. |
| **B-2** a query is derived data | **Policy-derived** (D-022 precedent) — an operator ruling on a live engagement, no incident behind it. Labelled, not dressed up. |
| **B-3** outbound requests are recorded | **Structurally inherited** from L-17. Written *in advance* of its incident, which is stated in the rule itself. |
| **B-4** unlisted destination is unclassified | **BK**, by direct extension of the unlisted-item rule. |
| **B-5** self-authored tools inherit the boundary | **Single-authored.** No scar. |
| **B-6** your own tool's output is `INFERENCE` until verified | **This corpus, 2026-07-24.** The first run of `tools/check-corpus.py` reported fourteen defects; **nine were artifacts of the gate.** Each was plausible and cited a real file and line. This is the only rule in the group with a scar that was actually paid for. |
| **B-7** cheap-to-reverse governs unattended execution | **VOC**, extended from autonomous *decisions* to autonomous *execution*. |
| Source manifest — extraction states, `Not read` field | **Single-authored**, from L-12 and L-16. No source project ingested an outside corpus. |
| Capability inventory | **Single-authored.** The nearest attested statement, "the operator is the instrument," is about the human. |
| `retrieved_at`, and "do not cite a source you did not fetch" | **VOC**, extended — L-11's "trust no number quoted to you" applied to retrieval. |
| The completeness-vs-detection instrument rule (`observation-pass`) | **This corpus, measured once.** Four readers found seven of ten sites; mechanical search found the rest. ~30% undercount, one measurement, stale from the moment it was typed (L-11). |

**Marked single-attested and provisional (D-006), and weaker than the BK addendum above it.** That
addendum had one outside project converging on two patterns. **This has no outside project at all.**
The whole boundaries layer exists because an AI collaborator now has filesystem access, a network,
and a shell at once — a condition **none of the four source projects had**, which is exactly why
there is nothing to converge with.

Two of the eleven rows carry a scar this corpus actually paid for (B-6, and the instrument rule).
The rest are structural arguments: *the collaborator is an instrument, instruments declare their
error; read is not transmit; an unlisted thing is unclassified.* Structural arguments are how the
seeded corpus's weakest material got in, and it says so about itself
([`../doctrine/README.md`](../doctrine/README.md): single-authored claims "are the weakest parts of
the framework and the first that should change").

**What would move this:** a second, unrelated project that arrives independently at an egress
boundary or a source manifest. Not this framework being used again by the same operator — that
tests whether it is *usable*, which is a different question from whether it is *right*.

---

# Addendum — 2026-07-26T23:07Z

> Like the two addenda above, this **does not re-run or revise** the 2026-07-20 extraction. It
> records the provenance of material added after that date, so this file does not mislead about
> what is attested (L-13).

Covers the instruments layer: **L-18**, [`../doctrine/08-instruments.md`](../doctrine/08-instruments.md)
(K-1…K-6), [`../rituals/capability-interrogation.md`](../rituals/capability-interrogation.md), and
[`../artifacts/operator-profile.template.md`](../artifacts/operator-profile.template.md). Ledger:
D-034 through D-038.

| Pattern | Provenance |
|---|---|
| **L-18** an instrument declares what it cannot do, before it is used | **VOC**, single-attested. Two scars in one day: thirty-two capability claims overturned by a pass instructed to re-measure rather than re-read; and a project's always-loaded governing instructions absent from version control for over a thousand commits. |
| **K-1** capability and permission are separate facts | **VOC.** Both errors available in the same hour and in opposite directions — a present mechanism the credential could not reach, and full rights over a subsystem that did not exist on that installation. |
| **K-2** name the role, then bind the provider | **Original to Astronomer.** Structurally inherited from L-1's own exclusion of toolchain from doctrine, and from the fact that one of the four source projects was not a repository at all. Near miss, not a scar: a vendor-shaped capability study was caught in review before it was folded in, and review is not a mechanism (L-17). |
| **K-3** every role declares its fallback before it is needed | **VOC**, by extension of a practice rather than a stated rule — the ledger of what was **owed to real devices** (L-12), applied to storage instead of measurement. |
| **K-4** a capability declaration expires | **VOC.** L-11 applied to an environment rather than a quantity. |
| **K-5** decision rights are a capability | **VOC.** The rule's two halves already existed — *a stalled session is worse than a documented judgement call*, bounded by *cheap to reverse* — held as a per-session understanding with no home. Roughly sixteen decisions returned in one day, about half of them reserved and about half not. |
| **K-6** the declaration is written by the instrument being declared | **VOC**, extending B-6. The refutation pass exists because the first pass could not be trusted about itself. |
| The **capability-role** default set and the fallback ladder | **Original to Astronomer** (D-035). Registered like `evidence_tier`: project-level, projects add and strike rows. |
| **Operator profile** as an artifact | **Original to Astronomer** (D-037). The condition — the operator's input arriving through augmentation — held in no source project. |
| The **capability interrogation** ritual, and its division of labour | **Original to Astronomer** (D-038). The division (collaborator measures capability, operator decides permission) is a structural argument from K-1, not an observed practice. |

## Annotation to the boundaries addendum above

That addendum's row reads *"Capability inventory | **Single-authored.** The nearest attested
statement, 'the operator is the instrument,' is about the human."* **That was accurate when written
and is now out of date:** the artifact has an incident behind it (D-038). It is annotated here rather
than corrected there, because the row is accurate evidence of what was attested on 2026-07-24.

## What this addendum does NOT claim

**It does not move any attestation, and the file above already said why.** Its own closing line is
the constraint: *"Not this framework being used again by the same operator — that tests whether it is
usable, which is a different question from whether it is right."*

Every row above is **VOC or original**. VOC is the same project and the same operator that supplied
the largest share of the seeded corpus. So the instruments layer is exactly as weak as the boundaries
layer it sits beside: one project, no convergence, and a handful of rows resting on argument rather
than incident. What it gained today is **scars where there were none** — which upgrades a structural
argument to a practice, and stops nowhere near a law (CHARTER invariant 4).

**Condition 6 of the definition of done remains unmet.** No project outside this repository has run a
full OBSERVE→RECORD loop on the framework. The consuming project that supplied every scar above does
not have Astronomer installed at all, which was verified rather than assumed: no charter, no ledger,
no observation log, and one skill in its collaborator workspace. Installing it there is the next
piece of work and is deliberately **not** done by this addendum — the framework was overhauled first,
from outside, precisely so that the install would not collide with decisions that project had already
made and create the rival-ledger drift this corpus exists to prevent.


---

# Annotation — 2026-08-01T21:32Z

> **This is an annotation, not a revision** (L-13). Nothing above is edited. The 2026-07-20
> extraction and all three addenda stand exactly as written; what follows records one fact that
> has since changed, so that a reader landing here is not misled by a statement that was true when
> it was made.

**Condition 6 is now met, and the corpus is `VALIDATED` (D-049, `AMENDS D-001`, 2026-08-01).** The
addendum above closes with *"Condition 6 of the definition of done remains unmet"* and with
*"Installing it there is the next piece of work."* Both were accurate on 2026-07-26. The install
happened on 2026-07-27, the loop ran, and the friction came back on 2026-08-01. The current status
lives in [`../CHARTER.md`](../CHARTER.md), which is living and outranks this file on fact.

**Nothing in this annotation moves an attestation, and the tally above is unchanged.** That is the
distinction the whole file exists to protect: ratification asks whether the framework survives being
used; attestation asks how many independent projects arrived at a given rule. The ratifying project
is `vociferous-next` — **the same project that supplied the largest share of the seeded corpus** —
so the closing constraint quoted in the addendum above still binds, and still says what it said:

> *"Not this framework being used again by the same operator — that tests whether it is usable,
> which is a different question from whether it is right."*

Condition 6 asks the **usable** question and asks it of a project outside this repository, which is
what was answered. The **right** question is still open, and no addendum here can close it. The one
new capability rule added on 2026-08-01 (`K-7`) is VOC-attested, single, and graded exactly as
weakly as every row above it.
