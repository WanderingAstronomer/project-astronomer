---
name: astronomer-start
description: Stand up a new Astronomer project, or adopt the framework over work already in progress — use when nothing has been declared yet (no charter, no ledger, no precedence order), when the operator asks to start, scaffold, or structure a new project, or before the collaborator is given standing filesystem access to a shared directory that holds anything beyond the project's own work product.
---

# Starting a project

Purpose: get the declarations made before any work happens, so the first surprise has somewhere
to land. This operationalizes ritual `starting-a-project` and runs once, before the loop's first
`astronomer-observe` window opens.

Run the steps in order. Steps 1 and 2 come first because everything after them assumes an answer
to "what may I even look at."

## Step 1 — declare the data boundary, before opening anything

If the collaborator's filesystem access reaches beyond this project's own work product — a shared
drive, a client's raw files, another team's directory — stop here first.

1. Ask the operator, explicitly, what is out of bounds. Do not infer it from folder names.
2. Write `data-boundary.template.md` at the top of the collaborator's own workspace (Step 2), filled
   with three named tiers: **RED** (do not open, each item with its one-clause reason) ·
   **GREEN** (read freely, named affirmatively — not "everything else") · **YELLOW** (ask first,
   case by case).
3. **Declare what may leave, separately from what may be read** (doctrine `07-boundaries.md`).
   Permission to read is not permission to transmit. Fill this in even when the answer is
   "nothing" — an unstated egress boundary reads as an unrestricted one.
4. **A query is derived data.** Anything built *from* restricted material carries information out
   even with no copied string in it: *"how do mid-size regional practices handle intake backlogs"*
   copies nothing and discloses sector, scale, and problem at once. State the approved abstract
   vocabulary, and open a query log if any outbound channel is permitted at all.
5. An unlisted item is unclassified, not GREEN. Stop and ask rather than guessing a tier by analogy.
   The same holds for an unlisted destination.

Skip this step only when everything reachable is already this project's own — say so, in one
sentence, rather than leaving the question unanswered.

## Step 2 — declare the collaborator's own workspace

Before the first observation, name where the collaborator's own working files live — separate from
the project's own artifacts (charter, ledger, observations), which belong to the project, not to
the collaborator's process of working on it.

1. Create the workspace directory (commonly `.claude/` or a name the operator prefers) and open it
   with a `README.md` that states: who authorized it and when, the data boundary from Step 1 (or a
   pointer to it), and a one-line index of what the workspace holds.
2. Organize by the same four record classes as everything else in the framework (doctrine
   `05-the-record.md`) — use these, do not invent a fifth:
   - **Disposable** — scratch analysis, drafts, working notes. Freest to write, least load-bearing.
   - **Living** — a synthesized state-of-play doc the operator (or a fresh session) reads first.
     Name it in the README so it never has to be rediscovered.
   - **Frozen** — dated, point-in-time analysis worth keeping as-is once written.
   - **Append-only** — a running work log, if the workspace keeps one. Frozen at the entry, living
     at the file (D-019); it is a class in its own right and not a flavour of frozen.
3. Point to the living state-of-play doc from the README with one line: *"read this first."* A
   workspace with no declared entry point gets read in a different order by every session, which
   is the same failure L-1 exists to prevent, one level down.

This workspace is the collaborator's, to use freely within the boundary declared in Step 1 — but it
is not a replacement for the project's own artifacts (Step 7 below), and nothing in it substitutes
for the charter, the ledger, or the observation log.

## Step 3 — declare your own capabilities and known error

If anything other than the operator is doing the observing — and if you are running this skill, that
is you — write the capability inventory before the first window opens.

Every other instrument in this framework declares what it cannot detect. The observation log
requires it per window; the frozen record requires it per run. The collaborator is the only
instrument that has been exempt, and it is the one doing most of the looking.

1. **Measure the environment, do not assume it** (L-11). What is installed, at what version, in what
   shell. A capability list carried over from a previous session is a stale number, and it will be
   wrong in the direction of claiming too much.
2. **State what you can read, by format** — and specifically whether a scanned document can be
   extracted at all. That one fails silently.
3. **State what you may execute and where you may write** (doctrine `07-boundaries.md`, B-5). A
   script is a reader with no memory of what it was allowed to read.
4. **Name your known error with a direction**, not as modesty. *"Roughly a 30% undercount on
   completeness questions"* can be subtracted; *"may be incomplete"* cannot.
5. **List the instrument debt** — what this environment cannot determine at all, so it is owed
   rather than guessed (L-12, L-16).

Then, before trusting any tool you build yourself: its output is `INFERENCE` until the tool has been
broken on purpose and seen to notice (B-6). This framework's own vocabulary gate reported fourteen
defects on its first run and nine were artifacts of the gate.

## Step 4 — choose a tier

Lite, Standard, or Full (framework `tiers/README.md`). Choose on stakes and reversibility, not
ambition — when two tiers both fit, take the lower one. This is itself the first entry in the
ledger you are about to open (Step 8): log it as `D-001` with the reasoning.

Note which of the four **condition-gated** artifacts apply, independently of tier: the data boundary
(Step 1), the query log (Step 1), the capability inventory (Step 3), and the source manifest —
required from Lite upward whenever the project takes in material it did not author. If material has
already been handed over, run `astronomer-intake` before the first observation window.

## Step 5 — write the charter

Mission; scope IN and scope OUT; the invariants that must not be violated; a definition of done
written as testable predicates, not aspirations.

## Step 6 — declare the precedence order

Inside the charter, explicitly — even adopting the default stack unchanged (doctrine
`00-precedence.md`). An assumed order is not an order (L-1).

## Step 7 — choose the vocabularies, fix the scrutiny gate, name what cannot be delegated

Three declarations, each with one home (L-14), each named in the charter:

- **Vocabularies** — confidence, severity, effort, change size, doc status. Every later artifact
  renders from here rather than restating it.
- **The scrutiny gate** — which claim types earn expensive verification and which never qualify for
  promotion, decided now rather than per-item later (doctrine `02-epistemics.md`).
- **The non-delegable categories** — identity and authority, custody, acceptance, physical fact,
  preference (doctrine `06-delegation.md`), in writing, before any work starts (L-15).

## Step 8 — open the ledger and the observation log

1. Open the decision ledger. Append every decision made in Steps 1–7 as separate, live-stamped
   entries, `[operator]` where the human made the call rather than the collaborator.
2. Open the observation log, empty, with its ID scheme (`O-<n>`) and its **conditions** fields
   declared up front. Fields added later cannot be back-filled onto entries already taken.

## Step 9 — declare the first OBSERVE window, then stop planning

State what is being observed, over what period, and what event closes it. Then go look — do not
begin ACT-phase work before that window closes (L-7). If something obviously needs fixing on day
one, it is an observation.

## Forbidden

- Skipping Step 1 because the project "seems" self-contained. Check; do not assume.
- Leaving the egress boundary blank because nothing currently leaves. Write "nothing leaves this
  machine" — silence is read as permission by the next session.
- Writing "no known limitations" in the capability inventory. That is an absence of an inventory,
  and it is the single most likely sentence in it to be false.
- Writing the collaborator's workspace and the project's artifacts as one undifferentiated pile —
  the workspace is disposable/living/append-only/frozen scratch space; the charter and ledger are
  the record.
- Choosing a tier by ambition rather than by stakes and reversibility.
- Beginning ACT-phase work, or fixing anything noticed along the way, before the first observation
  window has closed.

## Record

`CHARTER` (mission, scope, invariants, precedence, vocabularies, definition of done) ·
`DECISIONS` (the tier choice, the precedence adoption, the vocabulary set, the scrutiny gate, the
non-delegable list, and the data-boundary declaration, as separate numbered entries) ·
`OBSERVATIONS` (the log, opened and empty, first window declared) · `DATA BOUNDARY` (read tiers
*and* the egress section) · `CAPABILITY INVENTORY` (dated, with known error stated directionally) ·
`QUERY LOG` (opened and empty, if any outbound channel is permitted) · the collaborator's own
workspace `README.md`, pointing to its living state-of-play doc.

Also update the skill's own trigger conditions if the operator's answers changed them — a boundary
that turns out to reach further than expected is a decision, live-stamped, not a quiet correction.
