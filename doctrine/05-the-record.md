# 05 — The Record

A project's record is not its output. It is the thing that makes the output trustworthy, and it
fails in a specific, predictable way: not by containing errors, but by containing documents whose
**class** is ambiguous — so nobody knows whether a given file is supposed to be updated, frozen,
or thrown away, and all three happen to it at different times.

Astronomer recognizes three classes and one rule per class.

---

## The three classes

| Class | Rule | Examples |
|---|---|---|
| **Living** | Rewritten freely to match current reality. States what *is*, never how it got that way. | charter, specification, catalog, runbooks, [rituals](../rituals/) |
| **Frozen** | Point-in-time. **Annotated, never edited.** Corrections are addenda. | observations, findings, audits, build records, session reports |
| **Append-only** | **Frozen at the entry, living at the file.** An entry is fixed the moment it is written; the file grows forever. | decision ledgers, observation logs |
| **Disposable** | High-churn working docs. Deliberately not deliverables. | triage boards, analysis passes, punch lists |

**Append-only is its own class, and needs to be** (D-019). The two most-written artifacts in the
framework — the ledger and the observation log — are neither living nor frozen, and forcing them
into either produces a wrong reading. *Frozen* implies the file is closed; *living* implies
entries may be revised. Both are false. The class applies to the **entry**, not the file.

**Living documents state current truth, not history.** The single most common corruption is a
specification that accretes a change-log — "updated 2026-03-14 to reflect…" — until reading it
requires reconstructing a timeline. The commit history and the decision ledger hold history.
VOC's settlement pass phrased the ruling as: **"Strip to current reality, not history. Specs
state what IS; the commit tree holds the change-log."**

**Frozen documents are annotated, never corrected.** All three projects that formalized this hit
the same failure: a research document quietly updated becomes a document that appears to have
been right all along, which destroys its value as evidence of what you knew and when. OD's
addendum block states the mechanism exactly — the addition "does not re-run or revise" the
frozen record, it "only notes what shipped afterward so this document does not mislead about the
live system."

When a frozen record and a living one conflict, **the living one wins on fact and the frozen one
stands on the historical record.** Both statements are true and neither file changes.

**Disposable documents are permitted to be messy — and that is their function.** OD deliberately
excluded its triage and performance-analysis docs from version control. Because nobody outside
would read them, they could be blunt, opinionated, addressed to the owner, and revised
violently. The four permanent documents were written for a stranger. **Giving yourself a
sanctioned place to write badly is what keeps the permanent documents clean** — without it, the
mess ends up in the specification.

A caution that goes with it: a disposable document that starts carrying load must be promoted to
frozen or living. If you would be upset to lose it, it is not disposable, whatever the directory
says.

---

## Ledgers

The single highest-value artifact in the framework, and the cheapest. Two source projects
arrived at a near-identical format.

**Entry form:**

```
[<live UTC>] D-<n>: **<the decision>** — <why>
```

**Rules:**

- **Live timestamps only.** `date -u`, read at the moment of writing. Never an ambient or
  injected date — both projects state this explicitly, because injected dates drift and a ledger
  ordered by drifting timestamps cannot be resolved.
- **Append-only.** Never edit an entry. Amend with a new timestamped `AMENDS D-<n>:` line.
- **Supersede by naming** (L-2). Recency alone does not win.
- **`blocks-on:`** — a decision resting on unproven evidence carries this tag and stays open.
- **`caveat (owned):`** — state the weakness yourself. DD's best entry names the control run
  that was *not* performed and says who chose to skip it and why. An owned caveat is a durable
  asset; an unstated one is a landmine with your fingerprints on it.
- **Mark who decided.** Where a human made the call rather than a collaborator, say so. The
  boundary is recorded, not assumed.

The entry that a ledger exists for looks like this — a real one, compressed:

> **The gate was mis-calibrated and is demoted to a monitored metric.** The original threshold
> was lifted from a same-sample ceiling that no model reaches on held-out data, so holding
> anything to it was a gate artifact, not a quality signal. — *human's call.* Frozen numbers:
> [pointer]. `caveat (owned):` the cleanest control was not run; momentum was chosen over the
> extra run, knowingly.

Numbers, the comparison condition, the reasoning about why the *gate* rather than the subject
was wrong, explicit human ownership, an owned caveat naming what was skipped, and a pointer to
the frozen record. That is roughly ninety seconds of writing, and it is the difference between a
project that can be resumed and one that has to be re-derived.

---

## Identifiers

**IDs are permanent addresses. Never renumber. Retire, never reuse.**

An ID that gets reused breaks every historical reference to it silently — the reference still
resolves, to the wrong thing, which is worse than a dangling pointer. VOC's rule: "IDs are
stable and permanent — never renumber; retire with a `deprecated` status."

A workable scheme, adapted from the source projects:

| Prefix | Means | Lives in |
|---|---|---|
| `D-<n>` | decision | the ledger |
| `O-<n>` | observation | the observation log |
| `C-<n>` | cluster (a shared root cause) | the triage board |
| `Q-<n>` | open question owed to a human | triage board / standard |
| `F-<n>` | finding | findings |

Bare references resolve to the **local** ledger only. Cross-project references are namespaced
(`VOC-D-4`). An item that splits keeps its ID and gains a suffix (`O-14a`, `O-14b`) rather than
being renumbered. An item that migrates between buckets **keeps both addresses** — OD wrote
`E4→B9` as a heading, which preserves every earlier reference while recording the movement.

---

## Status vocabularies

Fixed, small, and defined in one place (L-14). Choose once per project and put them in the
charter.

- **Confidence:** defined once, in
  [`02-epistemics.md`](02-epistemics.md#confidence-tokens). Not restated here — that is the
  point of L-14, and this file restated it once already (see `AMENDS D-015`).
- **Severity:** `stop` · `major` · `minor` · `question` — where `question` means *needs a human
  decision*, which is a disposition and not a magnitude
- **Effort:** wall-clock bands, not points. OD defined them inline: *S = minutes, M = an
  hour-ish, L = multi-hour or needs design care.* Falsifiable, unlike a 5.
- **Change size:** `minimal` · `medium` · `large`, declared before starting. Re-classing upward
  is expected; silently exceeding the class is not.
- **Doc status:** `living` · `frozen` · `disposable`, stated at the top of the file.

---

## Naming

- **Numbered slugs for ordered corpora:** `01-charter.md`, `04-verification.md`. Numbers are
  *slots* — when a document is retired, the slot's history is recorded and the number may be
  refilled by something unrelated. It is a position, not a meaning.
- **Date-suffixed for frozen records:** `audit-2026-07-20.md`. The date in the filename is what
  makes a frozen record obviously frozen at a glance in a directory listing.
- **Underscore-prefix for shared includes:** `_SHARED-PREAMBLE.md` sorts to the top, where a file
  every other file depends on belongs.

---

## Housekeeping is a ritual, and it is recorded

When documents are moved, retired, or reorganized, the move is **recorded in a dated block** —
what moved, where, and why. VOC's docs index carries a run of these, and its own summary of the
retirement rule is: **"No deletions; every record was relocated and re-annotated, never
trimmed."**

Spent one-time documents — an executed plan, a used prompt — get a banner rather than a delete:

> **EXECUTED 2026-07-20 — kept as a reusable template. Re-baseline before re-running.**

The instinct to delete a completed plan is strong and wrong. The plan is the only surviving
statement of what you *intended*, which is what you need when the outcome disappoints and you
are trying to work out whether the plan or the execution failed.
