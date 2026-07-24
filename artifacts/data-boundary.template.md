# DATA BOUNDARY — `<project name>`

> **Doc class:** living. Rewritten whenever what the collaborator may access changes — never
> silently (L-1). **Deploy at the top of the collaborator's own workspace** (e.g.
> `.claude/README.md` or `Claude/README.md`) — this is the first thing read in every session,
> before any task begins.

Every non-delegable category in `doctrine/06-delegation.md` names
work a collaborator must not *do*. This artifact names what a collaborator must not *see* — a
different failure mode, and one the four original source projects did not need to formalize
because none of them ran an AI collaborator with standing filesystem access next to material the
collaborator had no business reading.

**Required at:** **Lite, conditional** — gated on the condition below, not on tier.

**Required when:** the collaborator's filesystem access includes anything beyond the project's own
de-identified work product — a shared drive, a client's raw files, another team's directory, a
mailbox export. Required from **Lite** upward under that condition; skip it only when everything
reachable is already yours to read. This is a condition, not a tier gate — a one-person Lite
project with a subpoenaed case file two folders over needs this artifact more than a Full-tier
project with a clean, single-purpose repository.

## The scar

A live engagement authorized an AI collaborator to work inside a shared project directory that
also held a client's legally privileged, subpoenaed custody file and raw financial exports. Nothing
in the authorization said which parts of the directory the collaborator could read — so the
question "is this file in scope" had no answer faster than asking, every time, for every file. The
same engagement's own compliance commitments (a signed BAA, anonymized test data only) were already
in tension with an unrelated privileged case file sitting in the same repository, unflagged,
discovered only when someone finally wrote the boundary down and checked. **Writing the boundary
down is what turned an ambient risk into a visible, checkable one.**

## The three tiers

| Tier | Meaning | Collaborator may |
|---|---|---|
| **RED** | Out of bounds, no exceptions without explicit override | Not open, not summarize, not quote — even in service of a task that seems to need it |
| **GREEN** | The project's own work product, or material already de-identified | Read freely and reason over |
| **YELLOW** | Real, useful, but carries content that needs a case-by-case call | Ask first, every time — this tier is not a standing grant |

A file's tier is a fact about the file, not about the current task. A RED file does not turn GREEN
because today's request would be easier if it did.

## What must be stated, not implied

- **Who authorized access, and when** — an assumed boundary is not a boundary (L-1); state it as a
  dated fact the same way a precedence order is stated.
- **Every RED item, named specifically** — a path, a folder, a file pattern. "Use judgment" is not
  a tier.
- **The reason per RED item**, in one clause — this is the item's scar, and it is what lets the
  collaborator recognize the same danger arriving under a different name (a "custody file" and a
  "subpoena export" and a "minor's records" are one category, not three).
- **What GREEN actually covers** — named affirmatively, not left as "everything else." A boundary
  defined only by its exclusions gets tested against files nobody thought to list.
## What may leave — a separate boundary, stated separately

Read access is not transmission rights (B-1, `doctrine/07-boundaries.md`). The tiers above say what
may be **opened**. This section says what may **leave**, and it is filled in even when the answer is
"nothing," because an unstated egress boundary reads as an unrestricted one.

| Channel | Permitted | Constraint |
|---|---|---|
| `<web search / external service / message / upload / API>` | `<yes / no / ask first>` | `<what may be included, and in what form>` |

**A query is derived data (B-2).** Anything built *from* restricted material carries information
out even with no copied string in it — `<"how do mid-size regional practices handle intake
backlogs" copies nothing and discloses sector, scale, and problem in one line>`. A boundary written
only in terms of copying — do not quote, do not paste, do not attach — reads as complete and does
not cover this at all.

- **What may appear in an outbound request:** `<the approved abstract vocabulary — the terms general
  enough that the question would be asked by someone who had never seen the material>`
- **What may never:** `<names, identifiers, distinctive phrasings, figures, dates, any detail whose
  presence in the question implies the asker has seen the source>`
- **Where the record goes:** `<path to the query log>` — every outbound request is recorded (B-3).
  The failure mode here is silent and cannot be withdrawn, so the log is the only thing that makes a
  violation findable afterward.
- **An unlisted channel is unclassified, not permitted** (B-4). Same rule as an unlisted file.

`<If a question cannot be asked in the approved abstract form, it does not go out — it becomes a
question for the human who owns the material.>`

## Forbidden

- Inferring a tier for an unlisted item by analogy. An unlisted item is unclassified, not GREEN —
  stop and ask (this is the same posture as an unscoped claim under L-4: treated as suspect, not
  trusted, until stated).
- Downgrading a RED item for a single task because the alternative is inconvenient. If the
  boundary is wrong, fix the boundary in writing; do not route around it once.
- Reclassifying quietly. A boundary change is a decision — log it, live-stamped, the same as any
  other (L-2).
- Treating "I may read it" as "I may ask about it." That inference is the one B-1 exists to break,
  and it is invisible because nothing fails when you make it.
- Leaving the egress section empty because nothing is currently permitted to leave. Write
  *"nothing leaves this machine"* and the boundary exists; leave it blank and the next session
  infers a permission from silence.

## Lifecycle

Created before the first file is opened — this artifact is read *before* `starting-a-project`'s
other steps, not after. Updated the moment access changes, by explicit statement, never by the
collaborator noticing a new file exists and assuming a tier for it. Never frozen; a stale boundary
is a live risk, not a historical record.
