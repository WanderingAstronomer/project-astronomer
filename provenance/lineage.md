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
| **FR** | `fractalized-rag` | Retrieval-architecture proof of concept | 986-line authoritative specification written before any code; not a git repository |
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
