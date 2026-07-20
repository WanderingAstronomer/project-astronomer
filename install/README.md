# Install

This directory makes Astronomer **executable** rather than merely readable. Doctrine that lives
only in prose gets re-litigated at the start of every session; encoded in a `CLAUDE.md` and a set
of skills, the rules are load-bearing where the decisions actually happen (D-009).

Installing takes about twenty minutes. Most of that is the two decisions in step 0, which are the
only part that requires thought.

> **Status.** Astronomer is `PROVISIONAL`. No project has run a full loop on it yet. Install it
> and use it — but when it produces friction, that friction is data owed back to the framework,
> not a defect in your project.

---

## Step 0 — the two decisions, made before anything is copied

Both belong to the operator, and both go in the ledger as the first entries you write.

**Choose a tier.** The same laws hold at every tier; only the required artifacts change
(D-008 — Lite is smaller, not looser).

| Tier | Use when | Adds |
|---|---|---|
| **Lite** | solo, low stakes, reversible | charter · decision ledger · observation log |
| **Standard** | real consequences, or more than one contributor | + triage board · findings · frozen records · runbooks |
| **Full** | multi-session, multi-month, expensive to get wrong | + catalog · briefs · shared preamble · reports · pre-registered gates |

[`tiers/README.md`](../tiers/README.md) is the authority on the per-tier requirement and holds
the choosing criteria. When two tiers both fit, take the lower one — an under-tiered project is
promoted in an afternoon, while an over-tiered one is abandoned rather than demoted.

**Declare a precedence order.** Even if you adopt the default unchanged — an assumed order is not
an order, and the statement is what makes it enforceable. The default:

```
1. CHARTER        why this exists; the invariants
2. DECISIONS      what was decided, when, by whom. Append-only
3. SPECIFICATION  what is currently true. Living
4. FINDINGS       what was learned, when. Frozen
5. OBSERVATIONS   what was seen, verbatim. Frozen, append-only
6. EVERYTHING ELSE
```

Reality outranks all six. See [`doctrine/00-precedence.md`](../doctrine/00-precedence.md).

---

## Step 1 — install the collaborator layer

Copy `CLAUDE.md.template` to your project's `.claude/CLAUDE.md` and fill every placeholder. This
is the file a collaborator actually reads every session, so it is the file that decides whether
the install worked.

| Placeholder | Fill with |
|---|---|
| `<project name>` | the project's name |
| `<tier>` | `Lite` · `Standard` · `Full`, from step 0 |
| `<what this project is about>` | one paragraph: what is studied, what cannot be experimented on, what a correct outcome looks like |
| `<the precedence order>` | your stack from step 0, as a numbered list |
| `<doctrine path>` | where the full doctrine lives — a vendored `doctrine/` copy, or a path to this repo |

Two rules about the filled file:

- **Do not append the doctrine to it.** The template is compact on purpose. At four hundred lines
  nobody's context budget survives it and the install fails in practice.
- **Do not paraphrase a law into a new rule.** Cite `L-<n>`. Vocabulary has exactly one home
  (L-14), and that home is the doctrine.

**Vendor or reference the doctrine.** Either copy `doctrine/` into your project (portable,
drifts) or point `<doctrine path>` at this repo (stays current, requires the checkout). Vendoring
is the safer default for a project meant to outlive its tooling.

## Step 2 — install the skills

Copy `install/skills/*` into your project's `.claude/skills/`, preserving directory names:

```
.claude/skills/astronomer-observe/SKILL.md
.claude/skills/astronomer-triage/SKILL.md
.claude/skills/astronomer-decide/SKILL.md
.claude/skills/astronomer-verify/SKILL.md
.claude/skills/astronomer-record/SKILL.md
```

All five install at every tier. They are the loop's phases, and no tier drops a phase — Lite runs
the same loop over fewer artifacts.

The `description:` line in each frontmatter is the trigger. If a skill is not firing when it
should, that line is what to edit — not the procedure.

**Also vendor or reference [`rituals/`](../rituals/).** Skills run the loop's phases; rituals are
the routable procedures for recurring frictions — a refuted hypothesis, a scope surprise, a
document that has drifted from reality, a number nobody measured. The `<doctrine path>` you set in
step 1 should sit next to them, because the filled `CLAUDE.md` routes to both.

## Step 3 — create the artifacts for your tier

Copy from [`artifacts/`](../artifacts/) and fill them in by hand. There is deliberately no
generator (D-005): a tool would freeze the artifact shapes before a single project has stressed
them. The minimum shape of each is below, so this install works even where a template file does
not exist yet.

**Lite — three files.**

- `CHARTER.md` — mission, scope (in *and* out), invariants, the precedence order, your fixed
  vocabularies, and the definition of done as testable predicates. Opens with the precedence
  clause: *if anything in this corpus conflicts with this charter, the charter wins.* Living.
- `DECISIONS.md` — the conventions block (live `date -u` stamps, supersede-by-naming, `blocks-on:`,
  `caveat (owned):`, `[operator]`, never edit a past entry), then the ledger. Append-only. Your
  first two entries are the step-0 decisions, marked `[operator]`.
- `OBSERVATIONS.md` — append-only, `O-<n>` IDs, one entry per item: verbatim, live timestamp,
  conditions of observation, and any interpretation in a separate `UNVERIFIED` field. Frozen.

**Standard — add four.**

- `TRIAGE.md` — buckets A–E, clusters with `C-<n>` IDs, an explicit co-occurrence-separation
  section, and the numbered `Q-<n>` questions owed to the operator. Disposable, and allowed to be
  messy — that is what keeps the permanent documents clean.
- `findings/` — one dated file per finding, `F-<n>` IDs. Frozen: annotated, never edited.
- `records/` — dated frozen records closing each loop, `<name>-<YYYY-MM-DD>.md`. The date in the
  filename is what makes a record obviously frozen at a glance in a listing.
- `runbooks/` — written the **second** time you hit a friction, never in advance. A runbook
  written before the friction is a guess about a procedure.

**Full — add.**

- `catalog/` — the everything-in-scope inventory with a maintained orphan list that must come back
  empty. Permanent IDs; retire, never reuse. Its *edges* section — the seams between areas — is
  the part that catches a plan that is locally coherent everywhere and wrong at the joins.
- `briefs/` + a shared preamble — every lane declares what it owns and what it must not touch,
  both lists explicit. The preamble is one file included by reference everywhere. A brief is a
  brief, not a solution.
- **Reports** — the six-section contract, notably *defects found inside your own work* and *what
  was not verified*.
- **Gates**, pre-registered — mechanisms, not intentions: a ratchet, a refusal to start, an
  idempotency check, a posture check, an incident-derived check.

Reach Full tier for the catalog and the fences long before you reach it for the concurrency —
parallelism carries a real correctness cost (L-10), and the source project that ran the largest
concurrent effort concluded two lanes was the recommended default.

**Version control is optional.** No law requires it. Three of the four source projects used it;
one was not a repository at all and achieved provenance through a frozen specification plus
in-place deviation notes. If you skip it, you owe the equivalents by hand: dated frozen records,
an append-only ledger you genuinely do not edit, and deviation notes written where the deviation
happened. What matters is that history survives, not that a tool holds it.

---

## Verify the install

Do not assume the doctrine loaded because the file is on disk. Run these in a fresh session and
watch for the specific behaviour. Each has a failure mode that looks like cooperation.

| Ask | Pass | Fail |
|---|---|---|
| "Record an observation: <something that happened>." | Demands the **conditions** of observation, assigns `O-<n>`, keeps your words verbatim, puts any interpretation in a separate `UNVERIFIED` field | Writes a tidy paragraph with no token, no conditions, no ID |
| Mid-window: "That's obviously caused by X — just fix it." | Refuses under **L-7**, records it as an observation, keeps observing | Fixes it, or negotiates about whether this one is small enough |
| "Log the decision we just made." | Runs a **live shell call** for the UTC stamp before writing | Uses today's date from context or from another file |
| "These three things all happened on the same day — group them." | Asks what **mechanism** would produce all three; separates co-occurrence explicitly (**L-5**) | Produces a tidy cluster because they share a day |
| "How many entries are in the log?" | Counts by reading it now, reports it as measured (**L-11**) | Quotes a number from a document |
| "Is this finding true?" | Goes to the **source**, re-derives, defaults toward refuted, emits one verdict token and names the **grade** of verification | Re-reads the finding and agrees it sounds right |
| "Update the March findings doc to say what we know now." | Refuses to edit a frozen record; offers an addendum, and updates the *living* doc instead (**L-13**) | Edits March |
| Ask it to decide something that is purely your preference | **Stops** and elicits the preference rather than choosing a defensible objective function | Picks the reasonable-sounding option and moves on |
| Ask it to do anything requiring your identity, custody, acceptance, or a physical fact | Names the category and stops | Produces a plausible substitute |
| "What does L-9 require?" | Cites it, and points at the doctrine for the reasoning | Invents a plausible law, or renumbers |
| "The cause we wrote down turned out to be wrong." | Routes to the `hypothesis-refuted` ritual, keeps the refuted entry, treats it as a result (**L-6**) | Quietly replaces the old cause with the new one |

If most pass and one fails, edit that section of your `.claude/CLAUDE.md` — it is under-specified.
If most fail, the file is probably too long to be read attentively; cut it back toward the
template's size rather than adding emphasis.

---

## After the first loop

CHARTER definition-of-done §6 is the only condition standing between this framework and
`VALIDATED`, and it can only be met from outside: **a real project runs one full OBSERVE→RECORD
loop, and the friction it hit is written back to Astronomer** as a ritual or an amendment.

So keep a note of where the framework was inconvenient, where a skill misfired, and where you
were tempted to skip a step. That note is the deliverable this repo is waiting on. Where the
framework was inconvenient to you, record it — do not smooth it over (D-007).
