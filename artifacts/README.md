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
[`../doctrine/05-the-record.md`](../doctrine/05-the-record.md) recognizes three classes and one
rule each: *living* is rewritten freely to match current reality, *frozen* is annotated but
never edited, *disposable* is permitted to be messy and is deliberately not a deliverable. The
most common way a record fails is not an error inside a file. It is a file whose class nobody
declared — so it gets updated, frozen, and thrown away at different times by different people,
and none of them are wrong.

**Two artifacts are append-only, which is neither cleanly living nor cleanly frozen.** The
decision ledger and the observation log grow forever but no entry in them is ever edited. The
governing rule is the frozen one — an entry is fixed the moment it is written, and corrections
arrive as new entries that name the old one — so they are classed **frozen (append-only)**.
Growth is not editing. Say this out loud in your own charter, because the first person who
"tidies up" a ledger entry will believe they are maintaining a living document.

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
| **Decision ledger** | frozen (append-only) | What was decided, when, by whom, and why. Supersession by name (L-2). The cheapest artifact in the framework and the highest-value one. | **Lite** | [`decisions.template.md`](decisions.template.md) |
| **Observation log** | frozen (append-only) | What was seen, verbatim, with the conditions that limited the seeing. Interpretation lives in its own labelled field so it can never be mistaken for the observation (L-3). | **Lite** | [`observation-log.template.md`](observation-log.template.md) |
| **Triage board** | disposable | Sorts observations by **epistemic state**, groups them into clusters with one hypothesised cause each, and ends in a list of decisions owed to the human. Blunt, opinionated, revised violently — that is its function. | **Standard** | [`triage-board.template.md`](triage-board.template.md) |
| **Findings** | frozen | What was concluded, at the time it was concluded, with the method and evidence tier per finding. Verdict first. Corrections arrive as addenda (L-13). | **Standard** | [`findings.template.md`](findings.template.md) |
| **Frozen record** | frozen | The point-in-time record of one run, pass, or intervention: metadata, metrics against the pre-registered gate (L-9), failure modes, owned caveats, and what a human must still check. | **Standard** | [`frozen-record.template.md`](frozen-record.template.md) |
| **Runbook** | living | When / Do / Record. The response to a recurring situation in **your subject**, written down once so it stops being re-improvised. If the procedure can be written without naming your subject it is a framework [ritual](../rituals/README.md), not a runbook (D-017). | **Standard** | [`runbook.template.md`](runbook.template.md) |
| **Catalog** | living | The everything-in-scope inventory. Every item assigned to exactly one row, with an orphan list that must come back empty, and an `edges` ledger for the seams between areas. | **Full** | [`catalog.template.md`](catalog.template.md) |
| **Brief** | disposable → frozen on execution | A self-contained work order for someone who cannot ask you a question. Symptoms, verified facts, labelled hypotheses, fences, acceptance criteria — never a solution. | **Full** | [`brief.template.md`](brief.template.md) |
| **Shared preamble** | living | The rules common to every piece of work, included by reference into every brief and identical everywhere on purpose. Each rule carries the failure that produced it (D-003). | **Full** | [`shared-preamble.template.md`](shared-preamble.template.md) |
| **Report** | frozen | The six-section return contract. Opens with a baseline-versus-final table measured by the reporter and never quoted (L-11). Sections 4 and 6 are what make it evidence rather than a pitch. | **Full** | [`report.template.md`](report.template.md) |

"Required at" means *required from this tier upward*. Full requires all eleven; Standard
requires seven; Lite requires three. See [`../tiers/README.md`](../tiers/README.md) — and note
that choosing a tier is itself a decision and goes in the ledger.

---

## Lifecycle

| Artifact | Created | Updated | Frozen / closed | Retired |
|---|---|---|---|---|
| Charter | Day one, before the first observation | Whenever reality diverges from it, by explicit ledger entry — never silently | Never | Only when the project ends; kept, banner-marked |
| Decision ledger | Day one, with the tier choice as its first entry | Every decision, at the moment it is made, with a live UTC stamp | Per entry, on write | Never |
| Observation log | At the opening of the first observation window | Every entry, during the pass — never written up afterward | Per entry on write; the whole window closes with an `INTAKE CLOSED` marker | Never |
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
