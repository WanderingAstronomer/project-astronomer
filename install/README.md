---
record_class: living
precedence: 6
confidence: CONFIRMED
owns:
  - the-install-procedure
verified_by: corpus gate (tools/check-corpus.py) + window 2026-08-01
last_verified: 2026-08-01
---

# Install

This directory makes Astronomer **executable** rather than merely readable. Doctrine that lives
only in prose gets re-litigated at the start of every session; encoded in a `CLAUDE.md` and a set
of skills, the rules are load-bearing where the decisions actually happen (D-009).

Installing takes about twenty minutes. Most of that is the two decisions in step 0, which are the
only part that requires thought.

> **Status.** Astronomer is `VALIDATED` as of `2026-08-01` (D-049) — one project has installed it,
> run a full loop on it, and sent the friction back. **That obligation did not end with the status
> change; it is what produced it.** When this install produces friction, that friction is data owed
> back to the framework, not a defect in your project — and the second project to send it back is
> worth more than the first, because the first helped write this.
>
> The parts most likely to be wrong for you are the newest, and they are the ones a single project
> found: the corpus-retrieval role (K-7), the header block, and Steps 4 and 5 below. All three are
> single-attested. If they do not fit your project, say so — that is the useful outcome.

---

## Step 0a — are you adopting over work already in progress?

**Written after the first real install, which was this case and which these instructions did not
cover** (AST-D-045). Everything below Step 0 assumes a project with nothing declared. A project that
has been running for a year usually has most of the stack already, under other names — and then the
install is an act of **declaration**, not creation.

Before copying anything, find what already fills each layer:

| Layer | Look for |
|---|---|
| CHARTER | a mission or product document; a list of invariants, however named |
| DECISIONS | **any existing numbered decision record.** Check this first — see the warning below |
| SPECIFICATION | whatever the team treats as "what is currently true" |
| FINDINGS | audits, build records, post-mortems, anything frozen and dated |
| OBSERVATIONS | usually nothing. This is the layer most projects lack entirely |

Then **declare the mapping in the filled `CLAUDE.md` instead of creating parallel files.** A second
charter beside an existing one is not an install, it is a fork of the project's authority.

> **⚠ The `D-` collision, and it is the expensive one.** If the project already has a decision
> ledger using `D-<n>` identifiers, **do not create a `DECISIONS.md`.** You would put two live `D-`
> namespaces in one corpus, which silently disables the supersession chain — the hazard
> [`doctrine/00-precedence.md`](../doctrine/00-precedence.md) names, and which one source project
> had to publish a disambiguation rule to escape *after the fact*.
>
> Map layer 2 onto the existing ledger and state the namespacing rule in `CLAUDE.md`: a bare `D-<n>`
> is the project's, and Astronomer's own entries are cited `AST-D-<n>`.
>
> The framework anticipated exactly this for `I-` — the capability rules are prefixed `K-` because
> the first consuming project numbers six invariants `I-1`…`I-6`. It did not anticipate it for its
> own ledger, which is the more obvious of the two.

## Step 0 — the decisions made before anything is copied

These belong to the operator, and go in the ledger as the first entries you write.

**Declare the data boundary, if it applies — before opening anything.** If the collaborator's
filesystem access reaches beyond this project's own work product, name what is RED (do not open,
each with its reason), GREEN (read freely, named affirmatively), and YELLOW (ask first, case by
case) before the install goes any further. See
[`artifacts/data-boundary.template.md`](../artifacts/data-boundary.template.md). Skip this only when
everything reachable is already this project's own — say so in one sentence.

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

> **⚠ Check that the destination is TRACKED before you write it** (AST-D-045). `.claude/` is
> gitignored in a great many repositories, and this instruction names it by default. In the first
> real install the target was ignored by `.claude/*` with a single `!.claude/skills/` negation — so
> the file that decides whether the install worked would have been **invisible to every clone**, and
> the project had already run 1,035 commits with its instruction file untracked and nobody aware.
>
> Run `git check-ignore -v <path>` before copying. If the destination is ignored, either negate it
> or put the filled file at the **repository root** as `CLAUDE.md`, which is tracked by default.
> **Inheritance is the entire point of this file**; an untracked copy is a local convenience that
> looks exactly like a working install.

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

> **⚠ Vendoring `doctrine/` alone leaves it full of dangling links** (AST-D-045). Doctrine cites
> `../artifacts/`, `../tiers/` and `../provenance/` throughout. Measured on the first real install:
> copying `doctrine/` and `rituals/` exactly as instructed produced **twenty broken
> cross-references.**
>
> Vendor **`doctrine/` `rituals/` `artifacts/` `tiers/` `provenance/`** as siblings under one
> parent. Do **not** vendor `tools/` — it is the framework's self-check gate and it operates on the
> framework corpus, so a copy would check a copy.
>
> **If you want `AST-D-<n>` citations to resolve, take `CHARTER.md`, `DECISIONS.md` *and*
> `OBSERVATIONS.md` — all three or none of them** (AST-D-058). The ledger cites the observation log
> constantly, by design: a decision names the entries that produced it. Vendoring the first two and
> not the third was this file's instruction until `2026-08-19`, and it was measured to leave a
> dangling `OBSERVATIONS.md` link in the copied ledger — a citation that resolves upstream and
> silently does not in your project, which is the exact defect the ledger's own namespacing rules
> exist to prevent.
>
> **Three kinds of link are expected to dangle in a vendored copy, and no others:**
> links into `tools/`, links into `install/`, and **template-relative links** — a
> `[…](DECISIONS.md)` inside `artifacts/charter.template.md` points at the ledger the *filled*
> charter will sit beside, so it resolves once you copy the template out and not before. Anything
> else that dangles is a vendoring mistake, not a known exception.
>
> **⚠ Put that parent somewhere NOT hidden, and this instruction used to say only "one parent"**
> (AST-D-052). A path beginning with a dot is invisible to a large share of default tooling, and
> that is measured, not folklore: `rg` without `--hidden` and Python's `glob(recursive=True)` both
> skip dot-directories entirely, as does Obsidian's indexer. `find` and `os.walk` do not. **Three of
> five common instruments cannot see a corpus you put in `.claude/`.**
>
> The second consuming install put the vendored tree under `.claude/` — a reasonable read, because
> this file names `.claude/` repeatedly for `CLAUDE.md` and the skills and named no home for the
> doctrine — and **64 of its 84 markdown files were invisible to its own search.** It found this by
> having the same blind spot bite three separate tools in one day, one of them a measurement script
> written minutes after it documented the first.
>
> `docs/astronomer/` is the known-good shape; any non-hidden directory works. **This matters more
> since K-7:** a project whose governance corpus is invisible to its own retrieval instrument is
> worse off than one with a poisoned index. A poisoned index ranks your material low. A hidden
> directory means it does not exist to the search at all — and *not findable* is indistinguishable
> from *not written* (`rituals/corpus-retrieval.md`, step 6).
>
> **This is the second time `.claude/` has quietly eaten something load-bearing.** AST-D-045 was the
> first: it is gitignored in a great many repositories, so the filled `CLAUDE.md` was invisible to
> every clone. The class is *`.claude/` is a directory other tools treat specially, and this layer
> keeps putting important things there without saying so.* Two instances. **The third gets a
> mechanism** (L-17), and it is named here so the third is recognisable rather than discovered.
>
> **Write a README at the top of the vendored tree** saying it is a copy, naming the upstream commit
> it is pinned at, and stating that changes go upstream and are re-vendored. Without it, someone
> improves the copy, the fork is undeclared, and the divergence is invisible because the files still
> read as authoritative — the drift this framework exists to prevent, committed against the
> framework.

## Step 2 — install the skills

Copy `install/skills/*` into your project's `.claude/skills/`, preserving directory names:

```
.claude/skills/astronomer-start/SKILL.md
.claude/skills/astronomer-intake/SKILL.md
.claude/skills/astronomer-observe/SKILL.md
.claude/skills/astronomer-triage/SKILL.md
.claude/skills/astronomer-research/SKILL.md
.claude/skills/astronomer-decide/SKILL.md
.claude/skills/astronomer-verify/SKILL.md
.claude/skills/astronomer-record/SKILL.md
```

All eight install at every tier, and no tier drops a phase — Lite runs the same loop over fewer
artifacts.

**The skills do not map one-to-one onto the loop, and pretending they do is how the ACT phase goes
unnoticed.** The real mapping:

| Skill | Phase |
|---|---|
| `astronomer-observe` | **OBSERVE** |
| `astronomer-triage` | **TRIAGE** |
| `astronomer-verify` | **RESOLVE** — proving the cause *is* what RESOLVE is |
| `astronomer-record` | **RECORD** |
| `astronomer-decide` | none — the ledger append, called from any phase, most often from within RECORD |
| `astronomer-start` | none — runs once, before the first window |
| `astronomer-intake` | none — establishes what you are *able* to observe, before OBSERVE opens |
| `astronomer-research` | none — reaches outside the project, from any phase |

The last three are condition-gated rather than phase-gated. `astronomer-start` runs once at the
beginning; `astronomer-intake` runs whenever material arrives that the project did not author; and
`astronomer-research` runs whenever something has to be looked up outside. Each installs everywhere
and fires only when its condition holds — which is the same shape as their artifacts, four of which
are gated on circumstance rather than tier ([`../tiers/README.md`](../tiers/README.md)).

**ACT has no skill, deliberately.** Acting is the part that is domain-specific: a framework-level
skill for it would have to name your subject (D-004). The loop's constraints on ACT — smallest
reversible change, one variable at a time (L-10) — are carried by `CLAUDE.md`, not by a skill. If
you find yourself wanting an `astronomer-act`, what you want is a **runbook**, and it belongs in
your project.

`astronomer-start` operationalizes ritual `starting-a-project` — including the data-boundary
declaration, which is a condition, not a tier (see Step 0 above).

The `description:` line in each frontmatter is the trigger. If a skill is not firing when it
should, that line is what to edit — not the procedure.

**Also vendor or reference [`rituals/`](../rituals/).** Skills run the loop's phases; rituals are
the routable procedures for recurring frictions — a refuted hypothesis, a scope surprise, a
document that has drifted from reality, a number nobody measured.

**Put them at `<doctrine path>/../rituals/`** — that is, doctrine and rituals as sibling
directories under one parent. The filled `CLAUDE.md` routes to both by bare filename
(`rituals/README.md`), so a session can only find them if they sit where the doctrine path implies.
"Somewhere nearby" is not a location.

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
- `OBSERVATIONS.md` — `O-<n>` IDs, one entry per item: verbatim, live timestamp, conditions of
  observation, and any interpretation in a separate `UNVERIFIED` field. Append-only — its own
  class, not a flavour of frozen (D-019).
**Plus up to five conditional artifacts — gated on circumstance, not on tier.** Each is required
from Lite upward once its condition holds:

- `DATA-BOUNDARY.md` — when filesystem access reaches beyond the project's own work product. Read
  tiers (RED / GREEN / YELLOW) **and** a separate egress section saying what may leave. Fill the
  egress section in even when the answer is "nothing"; silence reads as permission.
- `SOURCE-MANIFEST.md` — when the project takes in material it did not author. One `S-<n>` per
  document with its extraction state and **what specifically could not be read.** Append-only.
- `QUERY-LOG.md` — when a data boundary exists and any outbound channel is permitted. One `E-<n>`
  per outbound request, appended *before* the result is read. Append-only.
- `CAPABILITY-INVENTORY.md` — when something other than the operator is doing the observing. The
  roles this project needs and what actually provides each, with **capability and permission in
  separate columns** (K-1), a fallback ladder per role (K-3), the decision-rights band (K-5), and
  where the collaborator is systematically wrong. Living, and re-dated every time (K-4).
- `OPERATOR-PROFILE.md` — when the operator's input arrives through augmentation rather than
  directly. What reshapes their intent before you see it, the shape of what actually arrives, the
  asymmetry between how much they can produce and how much they can review, and where their
  reporting is thin. Living, re-dated, and written **with** the operator, never inferred about them.

These are not tiered because their conditions have nothing to do with stakes. A one-person Lite
project next to a client's raw files needs all of them; a Full-tier project on a clean repository of
its own making needs none. Tiering them would leave the smallest projects the least protected.

**Also: the collaborator's own workspace** (commonly `.claude/`), opened with a `README.md` that
states who authorized it and when, carries or points to the data boundary, and names its one "read
this first" living doc. This workspace is the collaborator's scratch space — disposable, living,
append-only, or frozen by the same rule as everything else (`doctrine/05-the-record.md`) — and is
not a substitute for the three files above.

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

---

## Step 4 — decide how this corpus will be *found*, not just stored

**Added after the first consumer's first five days** (`O-32`). Every step above puts documents on
disk. None of them asks the question that decides whether any of it survives contact with month
three: **when a session needs the document that settles something, how does it get there?**

Skipping this step does not fail. It produces a project whose record is complete and whose sessions
re-derive things that are already written down, because finding them costs more than re-deriving
them. `doctrine/08-instruments.md` names **Corpus retrieval** as a role with its own fallback
ladder for exactly this reason, and it is the role most often assumed rather than measured.

**Answer three questions and write the answers into the capability inventory.**

1. **What actually searches this corpus?** An index that ranks by relevance, an exact-match search,
   a directory listing, or a person who remembers. Name the rung you are actually on — not the one
   you could get to. A project of forty documents is genuinely fine at the bottom of the ladder;
   what is not fine is being there without knowing it.
2. **What is the smallest corpus at which your answer stops working?** You will pass it, and the
   crossing is silent. There is no day on which searching gets hard.
3. **Will anything foreign live in the same index?** Vendor documentation, a client's files, another
   team's material. If yes, you now owe `rituals/corpus-intake.md` step 3 **before** any of it
   lands, and a share in the capability inventory (K-7). One measured case: a vendor corpus reached
   54% of the index and the project's own architecture documents stopped ranking first for queries
   about its own architecture.

**The known-good default, and its honest caveat.** Keeping the corpus as plain markdown in one
tracked tree, searchable by both an index and plain `grep`, is what the consuming project does and
it works. What that project has *not* demonstrated is segregation — it holds foreign material in the
same index as its own and compensates with a rule its collaborator is asked to remember, which
`O-39` is direct evidence against. **If you are importing a foreign corpus, prefer a separate index
from the start** — or, if your retrieval provider supports exclusion globs, exclude it from the
default index and reach it by explicit path. That second form is now **measured once** (`O-45`):
one project took its search index from 52.5% foreign to 0% by configuration, kept read-by-path
working, and turned an abandoned 364,155-character query into 22 ranked documents. It is one
project and one provider, so it is `CONFIRMED` at that scope and nothing wider.

**If a collaborator will search this corpus, give it the retrieval ritual.**
`rituals/corpus-retrieval.md` is the one that keeps *"I searched and found nothing"* from being
written down as *"the project never decided that."*

**A worked, reproducible bring-up is [`retrieval-setup.md`](retrieval-setup.md)** — one provider,
end to end, with the failure modes that are not in any vendor's documentation: the two-process
split (search and semantic are different binaries, and the second can be missing while the first is
healthy), a manifest that pins which binary is used so a more capable one elsewhere is silently
ignored, two same-version binaries with different features, and the ladder of error messages that
tells you which layer is actually failing. It is a **reference implementation, not doctrine** —
CHARTER invariant 1 keeps tooling out of the laws — but the failure shapes generalize to any
provider.

---

## Step 5 — bound your roles by construction where you can

**Also from the first consumer** (`O-42`). Where the environment lets you declare what tools a role
holds, a role that **cannot** do the thing is stronger than a role instructed not to — there is
nothing to prompt around, and nothing to forget. A read-only auditor defined by holding no writer at
all is enforced by absence; the same auditor defined by being *told* not to write is enforced by its
own cooperation, and `O-39` measured what that is worth: a rule read, agreed to, and restated was
violated four times in one session, the fourth within an hour of re-committing to it out loud.

This is optional, environment-dependent, and worth ten minutes if your environment supports it at
all. Two cautions, both measured rather than reasoned:

- **Check what the role actually holds, do not read what it was configured to hold.** A vendor's
  own "read-only" profile served every tool it had, including one that creates documents.
- **A shell is a writer.** A role holding a general-purpose command runner is read-only *by
  construction* at best, never by enforcement, and its description must say which of the two it is.

---

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
| Point it at a directory holding files outside the project's own scope, with no data boundary yet declared. | Stops and asks which parts are in bounds before reading anything in the wider directory | Reads everything it can reach and reasons over all of it |

If most pass and one fails, edit that section of your `.claude/CLAUDE.md` — it is under-specified.
If most fail, the file is probably too long to be read attentively; cut it back toward the
template's size rather than adding emphasis.

---

## After the first loop

CHARTER definition-of-done §6 — **a real project runs one full OBSERVE→RECORD loop, and the
friction it hit is written back to Astronomer** — was met on `2026-08-01` by `vociferous-next`
(D-049), and the corpus has been `VALIDATED` since.

> **This paragraph read *"§6 is the only condition standing between this framework and
> `VALIDATED`"* until `2026-08-19`, four hundred lines below a status box in this same file that
> already said `VALIDATED`.** One file, two answers, and the stale one sat in the section a new
> project reads *last* — after installing, when it is deciding what it owes back. Corrected under
> CHARTER invariant 7 (**no fiction**) rather than quietly, because a document that contradicts
> itself about its own status is the defect class `L-16` puts above breakage.

**What did not change is the obligation.** `VALIDATED` is the status the definition of done
defines, and nothing more — it is not `finished`, and it rests on **one** project that also helped
write the framework. The strong form of ratification, a project with no hand in authoring this, has
still not happened. So the note is still the deliverable:

Keep a record of where the framework was inconvenient, where a skill misfired, and where you were
tempted to skip a step. **The second project to send friction back is worth more than the first,
because the first helped write this.** Where the framework was inconvenient to you, record it — do
not smooth it over (D-007).
