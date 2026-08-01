---
record_class: living
precedence: 3
confidence: CONFIRMED
owns:
  - the-artifact-set
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Artifacts

> **Doc class:** living. Rewritten to match the artifact set as it stands. The history of what
> changed lives in [`../DECISIONS.md`](../DECISIONS.md), not here.

The doctrine states what must be true. These are the document shapes that make it true in
practice — extracted from four projects that arrived at them independently, not designed here.
Every template is meant to be copied whole. The `<angle-bracket>` slots are the parts that
change; everything outside them is structure that has already earned its place, and deleting a
section because it looks like ceremony is how a project rediscovers why it was there.

Three things to understand before the table.

**Class is not a filing convention — it is a rule about who may change the file, and when.**
[`../doctrine/05-the-record.md`](../doctrine/05-the-record.md) recognizes four classes and one
rule each: *living* is rewritten freely to match current reality, *frozen* is annotated but
never edited, *append-only* is frozen at the entry and living at the file, *disposable* is
permitted to be messy and is deliberately not a deliverable. The
most common way a record fails is not an error inside a file. It is a file whose class nobody
declared — so it gets updated, frozen, and thrown away at different times by different people,
and none of them are wrong.

**Two artifacts are append-only, and that is its own class rather than a flavour of another
one.** The decision ledger and the observation log grow forever but no entry in them is ever
edited. Neither *living* nor *frozen* describes that: *frozen* implies the file is closed,
*living* implies entries may be revised, and both readings are wrong (D-019). The class applies
to the **entry**, not the file — an entry is fixed the moment it is written, and corrections
arrive as new entries that name the old one. Growth is not editing. Say this out loud in your own
charter, because the first person who "tidies up" a ledger entry will believe they are
maintaining a living document.

**Templates are written for where they land, not for where they live.** A template's links resolve
from the **project root** it is copied to. So: framework references (`doctrine/`, `rituals/`,
`tiers/`) are bare backticked paths and never markdown links, because the framework path varies per
install; project references (`CHARTER.md`, `DECISIONS.md`) stay links, because those resolve at the
destination; and a `../` in a template link is always wrong, because after the copy it points
outside the project at whatever happens to be there. The corpus previously used both conventions at
once — `charter.template.md` linking `DECISIONS.md` correctly for a project root while its
neighbours linked `../doctrine/…` correctly for `artifacts/`. Both could not be right.
[`../tools/check-corpus.py`](../tools/check-corpus.py) now enforces this.

**Tier changes which artifacts are required. It never relaxes a law** (CHARTER invariant 6,
D-008). A Lite project still separates observation from intervention (L-7) and still types its
claims (L-3). It simply does not maintain a catalog while doing so.

**These artifacts are the project layer. They do not restate the framework layer.** Doctrine and
[rituals](../rituals/README.md) ship with Astronomer and are domain-neutral; your charter,
ledger, and runbooks are yours and are domain-specific (D-016). Where a template needs a shared
vocabulary — the confidence tokens, most importantly — it **points at doctrine rather than
copying it** (L-14, AMENDS D-015). Resist the urge to inline those definitions "for
convenience": the seeded framework shipped three different memberships of the confidence
vocabulary within hours of writing the law against exactly that, and it was caught by review
rather than by any mechanism.

---

## The catalog

| Artifact | Class | Purpose | Required at | Template |
|---|---|---|---|---|
| **Charter** | living | Declares why the project exists, what is in and out, the invariants, the precedence order, and the vocabularies. The top of the authority stack — the document that makes a contradiction *detectable* (L-1). | **Lite** | [`charter.template.md`](charter.template.md) |
| **Decision ledger** | append-only | What was decided, when, by whom, and why. Supersession by name (L-2). The cheapest artifact in the framework and the highest-value one. | **Lite** | [`decisions.template.md`](decisions.template.md) |
| **Observation log** | append-only | What was seen, verbatim, with the conditions that limited the seeing. Interpretation lives in its own labelled field so it can never be mistaken for the observation (L-3). | **Lite** | [`observation-log.template.md`](observation-log.template.md) |
| **Data boundary** | living | Names what the collaborator may read, may never read, and must ask about — RED / GREEN / YELLOW, each item named specifically with its reason. Not a tier gate: required whenever filesystem access reaches beyond the project's own work product, from Lite upward. | **Lite, conditional** | [`data-boundary.template.md`](data-boundary.template.md) |
| **Source manifest** | append-only | Per document taken in from outside: ID, format, what was extractable, and **what specifically could not be read**. A failed extraction does not look like a failure — a scanned PDF returns a page count, no error, and almost no text (L-12, L-16). Gated on a condition: required whenever the project takes in material it did not author. | **Lite, conditional** | [`source-manifest.template.md`](source-manifest.template.md) |
| **Query log** | append-only | Every outbound request — what was asked, verbatim, to what destination, derived from what. A query carries information out even when it copies nothing (B-2). Gated on a condition: required whenever a data boundary exists and any outbound channel is permitted. | **Lite, conditional** | [`query-log.template.md`](query-log.template.md) |
| **Capability inventory** | living | The roles the project needs and what actually provides each, with **capability and permission in separate columns** (K-1), a fallback ladder per role (K-3), the decision-rights band (K-5), and where the collaborator is systematically wrong. Every other instrument in the framework declares its own error; this applies the rule to the one doing most of the observing (L-18). Gated on a condition: required whenever something other than the operator is doing the observing. | **Lite, conditional** | [`capability-inventory.template.md`](capability-inventory.template.md) |
| **Operator profile** | living | The human twin of the capability inventory. What reshapes the operator's intent before the collaborator sees it, the shape of what actually arrives, the asymmetry between what they can produce and what they can review, and where their reporting is thin — with direction, so it can be subtracted. `06-delegation.md` established that the operator is the instrument and never gave that instrument a place to declare its error; this is that place. Gated on a condition: required whenever the operator's input arrives through augmentation rather than directly. | **Lite, conditional** | [`operator-profile.template.md`](operator-profile.template.md) |
| **Triage board** | disposable | Sorts observations by **epistemic state**, groups them into clusters with one hypothesised cause each, and ends in a list of decisions owed to the human. Blunt, opinionated, revised violently — that is its function. | **Standard** | [`triage-board.template.md`](triage-board.template.md) |
| **Findings** | frozen | What was concluded, at the time it was concluded, with the method and evidence tier per finding. Verdict first. Corrections arrive as addenda (L-13). | **Standard** | [`findings.template.md`](findings.template.md) |
| **Frozen record** | frozen | The point-in-time record of one run, pass, or intervention: metadata, metrics against the pre-registered gate (L-9), failure modes, owned caveats, and what a human must still check. | **Standard** | [`frozen-record.template.md`](frozen-record.template.md) |
| **Runbook** | living | When / Do / Record. The response to a recurring situation in **your subject**, written down once so it stops being re-improvised. If the procedure can be written without naming your subject it is a framework [ritual](../rituals/README.md), not a runbook (D-017). | **Standard** | [`runbook.template.md`](runbook.template.md) |
| **Catalog** | living | The everything-in-scope inventory. Every item assigned to exactly one row, with an orphan list that must come back empty, and an `edges` ledger for the seams between areas. | **Full** | [`catalog.template.md`](catalog.template.md) |
| **Brief** | disposable → frozen on execution | A self-contained work order for someone who cannot ask you a question. Symptoms, verified facts, labelled hypotheses, fences, acceptance criteria — never a solution. | **Full** | [`brief.template.md`](brief.template.md) |
| **Shared preamble** | living | The rules common to every piece of work, included by reference into every brief and identical everywhere on purpose. Each rule carries the failure that produced it (D-003). | **Full** | [`shared-preamble.template.md`](shared-preamble.template.md) |
| **Report** | frozen | The six-section return contract. Opens with a baseline-versus-final table measured by the reporter and never quoted (L-11). Sections 4 and 6 are what make it evidence rather than a pitch. | **Full** | [`report.template.md`](report.template.md) |

"Required at" means *required from this tier upward*. **Fifteen artifacts, in two groups.**

**Eleven are gated on tier:** Lite requires three (charter, ledger, observation log), Standard adds
four, Full adds four more.

**Four are gated on a condition, not on tier** — the data boundary, the source manifest, the query
log, and the capability inventory. Each states its own condition, and each is required from **Lite**
upward once that condition holds. The reason they are not tiered is that the conditions have nothing
to do with stakes: a one-person Lite project sitting next to a client's raw files, taking in
documents it did not author, needs all four more than a Full-tier project working on a clean
repository of its own making needs any of them. Tiering them would have made the cheapest projects
the least protected, which is exactly backwards. See
[`../tiers/README.md`](../tiers/README.md) — and note that choosing a tier is itself a decision and
goes in the ledger.

---

## Lifecycle

| Artifact | Created | Updated | Frozen / closed | Retired |
|---|---|---|---|---|
| Charter | Day one, before the first observation | Whenever reality diverges from it, by explicit ledger entry — never silently | Never | Only when the project ends; kept, banner-marked |
| Decision ledger | Day one, with the tier choice as its first entry | Every decision, at the moment it is made, with a live UTC stamp | Per entry, on write | Never |
| Observation log | At the opening of the first observation window | Every entry, during the pass — never written up afterward | Per entry on write; the whole window closes with an `INTAKE CLOSED` marker | Never |
| Data boundary | Before the first file is opened, when the condition applies | The moment access changes, by explicit statement — never by the collaborator noticing a new file and assuming a tier for it | Never | When the collaborator's access to the wider directory ends |
| Source manifest | Before the first outside document is read | Per document, during intake | Per entry on write; a re-extraction is a new entry naming the old | Never |
| Query log | Alongside the data boundary, before the first outbound request | At the moment of each request — never afterward | Per entry on write | Never; a pruned query log cannot answer the one question it exists for |
| Capability inventory | Before the first observation window, as part of `capability-interrogation` inside `starting-a-project` | Whenever the environment changes — and re-dated every time (K-4) | Never | When the collaborator stops working on the project |
| Operator profile | Alongside the capability inventory, in the same sitting — the two halves of one question | When the operator's tooling, capacity or condition changes — and re-dated every time | Never; a stale profile about a person is a live risk | When the collaborator stops working with that operator |
| Triage board | Immediately after `INTAKE CLOSED` | Continuously and destructively while triage runs | On exit: every item bucketed, clustered or explicitly standalone | Superseded by the next pass; kept if it carried load, discarded if it did not |
| Findings | At the end of RESOLVE, when there is something concluded | Never edited. Addenda only, dated, appended below | On publication | Never — an outdated finding is evidence about what you knew |
| Frozen record | At the end of one run, pass, or intervention | Never edited. Addenda only | On write | Never |
| Runbook | The second time you improvise the same response | Freely, to match what actually works now | Never | When the situation it covers has been gated out of existence; banner, do not delete |
| Catalog | At the start of Full-tier work, before scoping | Continuously; rows change status, IDs never change | Never | Rows retire with a `deprecated` status; IDs are never reused |
| Brief | Before an executor starts, by the coordinator | Not after handoff. A changed brief mid-flight is a new brief | On execution — banner it `EXECUTED <date>` | Never; it is the only surviving statement of what you *intended* |
| Shared preamble | When the second parallel workstream is created | Whenever a run produces a new rule — with its war story attached | Never | Never |
| Report | On return of delegated work | Never edited by the coordinator. Disputes go in the ledger | On submission | Never |

Four transitions do the damage, and they are worth naming.

**Disposable → frozen, by accident.** A triage board that starts getting cited outside the pass
that produced it has stopped being disposable, whatever the directory says. The test from
[`../doctrine/05-the-record.md`](../doctrine/05-the-record.md) is blunt: *if you would be upset
to lose it, it is not disposable.* Promote it deliberately, or you will eventually lose a
load-bearing document that everyone assumed was scratch.

**Executed plan → deleted.** The instinct to delete a finished brief is strong and wrong. Banner
it instead:

> **EXECUTED `<YYYY-MM-DD>` — kept as a reusable template. Re-baseline before re-running.**

The plan is the only surviving statement of what you intended, which is exactly what you need
when the outcome disappoints and you are trying to work out whether the plan failed or the
execution did.

**Frozen → quietly corrected.** All three source projects that formalized this hit the same
failure: a record that is silently updated becomes a record that appears to have been right all
along, which destroys its value as evidence of what you knew and when. Corrections are addenda,
below the original, dated, and they say plainly that they do not revise what is above them.

**Retirement → deletion.** Nothing is deleted. Records are relocated and re-annotated, and the
move itself is recorded in a dated housekeeping block: what moved, where, and why. An
undocumented reorganization is indistinguishable from data loss six months later.

---

## Choosing what you need

Start at the tier the *consequences* justify, not the one your ambition justifies. Three
artifacts — a charter, a ledger, an observation log — are enough to run the whole loop on
something reversible and solo, and they are the three that a project which abandons the
framework in week three still turns out to have needed. Add the Standard four when a wrong
conclusion would cost real money, real time, or somebody else's trust: triage and findings exist
because at that point you need to be able to reconstruct *why* you concluded something, and a
runbook exists because at that point the same situation has started recurring. Add the Full four
only when the work is genuinely parallel or genuinely large — a catalog earns its cost when
scope ambiguity is the binding constraint, and briefs, preambles, and reports earn theirs when
work is being handed to someone who cannot ask you a question. Every one of the Full artifacts
is overhead on a project of one, and a framework that demands them of a personal log is a
framework that gets abandoned before it ever proves anything (D-011). Write the tier choice in
the ledger with the reason, so that the day you find yourself wanting the next tier up, you can
see what you assumed when you chose this one.
