---
record_class: living
precedence: 6
confidence: UNVERIFIED
owns: []
verified_by: nothing yet — this is a brief, not a built thing
last_verified: never
---

<!-- owns: was [scope-resolution, scope-namespacing, upward-promotion] until 2026-08-19.
     A superseded document cannot own a vocabulary: L-14 gives a vocabulary exactly one
     home, and this file declared supersession in prose while still claiming three keys the
     superseding brief also claimed. The gate caught it. The keys now live only in
     design/distribution-and-scope.md. -->


> **SUPERSEDED 2026-08-19 by `design/distribution-and-scope.md`.** This file covered nesting
> only, and its §5.3 contradicts the distribution design on where `doctrine/` is installed.
> Kept for the reasoning, not for execution. **Do not work from this file.**

# BRIEF — `nested-scopes` — Astronomer instances that know where they sit

> **Status: design brief. Nothing here is built.** Every mechanism described is a proposal, and the
> measurements in §3 are the only load-bearing facts. Written 2026-08-19 against
> `project-astronomer @ 3fed7fc` and `vociferous-next @ b4b10332`.

---

## 1. Read this first

Astronomer today assumes **one instance, one project, flat**. The operator needs it to nest: an
install at `~/work/` that spans everything, another at `~/work/clients/acme/`, another at
`~/work/clients/acme/projects/rebrand/` — each maintaining itself, each knowing where it sits, with
changes rippling *upward* rarely and *downward* automatically.

**Six decisions, committed:**

1. **A scope is discovered by walking up**, exactly like `.git`. Every instance carries
   `.astronomer/scope.toml` declaring its identity; the chain from cwd to root *is* the scope path.
2. **Every scope owns a namespace prefix, and bare IDs always mean the local scope.** This is the
   single highest-risk part of the whole feature and §4 explains why.
3. **Doctrine is installed once at the root and inherited**, never duplicated per level.
4. **The 90/8/2 split is not implemented as a quota.** It is implemented as *write at the smallest
   scope where the claim is true*, and 90/8/2 becomes a calibration signal you can measure.
5. **Upward is explicit promotion; downward is automatic inheritance.** An ancestor change never
   rewrites a descendant — it raises a staleness flag the descendant resolves. That is the
   difference between a ripple and a domino.
6. **Depth is not capped at three.** It is capped by a context budget that can be measured, plus a
   rule that deletes scopes which do not earn their existence. See §5.6.

---

## 2. Why this scope exists

The operator's framing: *"We don't want one Astronomer instance accounting for absolutely everything
all the time because that becomes too big to handle."*

That is correct and it is already the framework's own position. `tiers/README.md` says a framework
demanding a full apparatus for a small effort **"gets abandoned in week three and takes its laws with
it."** A single root instance spanning all work would be exactly that failure at a larger radius:
one charter trying to constrain a rebrand and a tax filing, one ledger where a decision about
`acme`'s brand voice sits beside a decision about a Python dependency.

Nesting is how the framework scales *outward* the way tiers already let it scale *down*.

---

## 3. Verified current state

Measured by me, this window. These are the numbers the design rests on.

| Fact | Value | Why it matters |
|---|---|---|
| `vociferous-next/CLAUDE.md` | **35,454 bytes / 463 lines** | The per-level rendering cost. Three naive levels ≈ 106 KB before any work begins. This is the real depth limit. |
| Full doctrine corpus | **123,520 bytes** | Duplicating it per level is unaffordable and unnecessary — hence decision 3. |
| Tiers already exist | Lite / Standard / Full | Sizing is a *solved* axis. Scope must not reinvent it. |
| Namespace collisions already bite at **two** namespaces | `D-` vs `AST-D-`, `O-` vs `AST-O-`, `I-` vs `K-` | `vociferous-next/CLAUDE.md` devotes a paragraph to this hazard and cites `AST-O-48` — a second project making the same error. Three scopes make it worse, not linearly. |

### UNVERIFIED — hypotheses, not facts

- **That Claude Code loads `CLAUDE.md` from ancestor directories.** If it does, discovery is partly
  free and §5.1 can lean on it. If it does not, the resolver must compose renderings itself. **This
  must be measured before implementation** — it changes the shape of §5.7.
- That ~30 instances would actually nest. The operator describes one hierarchy; whether the other
  instances fall into it or stay flat is unknown, and the design must tolerate both.

---

## 4. What makes this harder than it looks

**The namespace problem is the whole feature's risk, concentrated.**

`vociferous-next` already carries this scar at two namespaces:

> A bare `D-NNN` resolves to **this project's spine only**. Astronomer's own ledger is cited
> `AST-D-NNN`. […] Write the prefix even when context makes it obvious — it stops being obvious the
> moment the sentence is quoted somewhere else.

And it records what the failure costs: an ID renumber swept the spine and two records, but issue
bodies kept citing old numbers **which now resolved to different rulings** — one issue cited them
seven times, and a session obeying it would have drafted a charter amendment against the wrong one.

With three scopes there are four namespaces in play (root, client, project, plus `AST-`). A bare
`D-012` written at project scope and later quoted in a client-level document **silently changes
meaning**. Nothing catches it, because both resolve.

**Everything else in this brief is mechanism. This is the part that must be made impossible rather
than discouraged.**

Two lesser traps:

- **Precedence has no single direction.** An outer scope binds inner ones on constraints; an inner
  scope wins on specifics. A design that picks one direction globally will be wrong half the time.
  §5.5 resolves this.
- **Context budget compounds silently.** Each level's rendering is loaded before work starts. Naive
  composition makes depth expensive in exactly the resource sessions are shortest on.

---

## 5. The design

### 5.1 Discovery and self-identification

Every instance carries `.astronomer/scope.toml`:

```toml
id     = "ACME"                 # namespace prefix — unique among ancestors, enforced
name   = "Acme Corp"
role   = "client"               # free text; conventional: root | domain | client | project
tier   = "standard"             # orthogonal to scope — see 5.7
root   = false                  # exactly one instance in a chain sets true
```

Resolution walks up from cwd collecting every `.astronomer/scope.toml` until it finds `root = true`
or hits the filesystem root. The ordered chain **is** the scope path:

```
WRK  ~/work                              root,   tier=lite
 └ ACME  ~/work/clients/acme             client, tier=standard
    └ REBRAND  ~/work/clients/acme/projects/rebrand   project, tier=full
```

`astro whoami` prints exactly that, and it is the self-identification the operator asked for. A
session opening `rebrand/` learns in one command that it is a project inside a client inside work.

**If a directory has no install but an ancestor does**, it resolves to the nearest ancestor and says
so rather than failing. Opening `~/work/clients/acme/notes/` is a session at `ACME` scope.

### 5.2 Namespaces — the rule that must be mechanical

**Bare IDs always mean the local scope. Ancestors are always cited with their prefix.**

| Written at | Bare `D-012` means | A client decision is cited | Astronomer's own |
|---|---|---|---|
| `REBRAND` | `REBRAND-D-012` | `ACME-D-004` | `AST-D-051` |
| `ACME` | `ACME-D-012` | `WRK-D-001` | `AST-D-051` |

Three enforcement points, and none of them is a convention:

1. **The installer refuses a prefix already used by any ancestor.** Collision is impossible to
   create, not merely discouraged.
2. **`astro check-citations` resolves every `<PREFIX>-D-NNN` in scope-owned documents** and fails on
   any prefix not in the chain. This is the analogue of the existing `check_issue_citations.py` gate
   and should be modelled on it.
3. **Promotion rewrites bare IDs.** When a record moves from `REBRAND` to `ACME`, every bare `D-`
   inside it is rewritten to `REBRAND-D-` *before* it lands upward — because at the new scope, bare
   no longer means what it meant. **This is the step most likely to be forgotten and it is the step
   that produces silent wrong-resolution.**

### 5.3 What is scoped, and what is not

| Artifact | Where it lives | Why |
|---|---|---|
| `doctrine/`, `rituals/`, `artifacts/` | **Root only.** Inherited by every descendant | The shared vocabulary. `L-14`: vocabulary has one home. Duplicating 123 KB per level buys nothing and invites drift |
| `CHARTER.md` | **Every scope** | A client's "never do this" must bind their projects |
| `DECISIONS.md` (spine) | **Every scope** | Rulings have natural altitude |
| `OBSERVATIONS.md` | **Every scope** | Mostly local; occasionally promoted |
| `CAPABILITY-INVENTORY.md` | **Root only** | It measures the *machine*. One machine, one inventory |
| `OPERATOR-PROFILE.md` | **Root only** | One operator |
| `DATA-BOUNDARY.md` | **Every scope** | The boundary genuinely narrows inward — a project sees less than the work root |
| `CLAUDE.md` | **Every scope**, composed by reference | See 5.7 |

### 5.4 Write routing — replacing 90/8/2 with a test

The operator's 90/8/2 is an accurate *prediction*, but a percentage cannot be executed. Convert it
to the question `L-4` already asks — **every claim carries scope**:

> **Write the record at the smallest scope where the claim is true.**

- True only of this project → local.
- True of every project for this client → client.
- True of all work → root.

The distribution then *falls out* rather than being enforced, and 90/8/2 becomes something better
than a quota: **a calibration signal.** `astro scope-stats` reports the actual split, and a project
writing 40 % upward is evidence that either the scopes are drawn wrong or someone is generalising
from one instance — which is `L-4`'s `ASSERTED-UNIVERSAL` failure, now visible as a number.

**Do not implement percentages. Implement the test, then measure against the prediction.**

### 5.5 Precedence — inner may narrow, never relax

The direction is not uniform, and this is the rule that resolves it:

> **An inner scope may NARROW an outer constraint. It may never RELAX one.**

- `ACME` says *"no client data leaves the tenant."* `REBRAND` may add *"and no screenshots either."*
  It may not carve an exception.
- `WRK` says *"every deliverable carries provenance."* A project cannot opt out.
- On **specifics** — build commands, file layout, this project's own vocabulary — the inner scope
  simply wins, because the outer has no opinion.

`astro check-scope` should flag an inner charter clause that contradicts rather than narrows an
outer one. That check is worth building early; it is the one place where nesting can silently break
a promise made at a higher level.

### 5.6 Ripple, not domino

**Downward is automatic. Upward is explicit. Neither rewrites anything.**

- **Inheritance (down):** a session at `REBRAND` reads `WRK` and `ACME` charters, ledgers and
  boundaries as ancestors. Automatic, every session, no action.
- **Promotion (up):** `astro promote --to ACME OBS-014`. The record moves, bare IDs are rewritten
  (5.2), and a stub remains at the origin pointing upward so the local citation still resolves.
- **Aftershock:** when an ancestor record changes, descendants are **not** edited. Each descendant's
  next `astro status` reports `ancestor changed: ACME-D-004 (charter) — affects 2 local records`.
  The descendant decides.

That last property is what makes it aftershocks rather than dominoes: **the shock is a notification,
and it stops at whoever is willing to act on it.** A root-level charter amendment cannot silently
rewrite thirty projects.

### 5.7 Depth — budget-limited, not number-limited

Do not hard-cap at three. Cap it three ways that each mean something:

1. **Mechanically unlimited.** Walk-up costs one `stat` per level.
2. **Budget-limited, and this is the real one.** `CLAUDE.md` measures **35 KB** in a Full-tier
   project. Naive composition of three levels is ~106 KB of context before work starts. So
   composition must be **by reference, not by copy**: an inner `CLAUDE.md` carries a pointer to its
   ancestors plus *only its own deltas*. Ancestors are read on demand, not pasted. Depth cost
   becomes sublinear, and `astro render --budget` should refuse to emit a rendering over a declared
   ceiling.
3. **Earn-your-existence rule.** A scope must hold **at least one record that could not live at its
   parent or its child**. `astro scope-stats` reports empty scopes; an empty scope is deleted, not
   kept for symmetry.

**Recommendation: three is the natural depth; warn at four; refuse past six.** Four is legitimate
(`work → domain → client → project`). Past six the earn-your-existence rule will almost always be
failing somewhere, and the refusal is cheaper than the audit.

### 5.8 Tier and scope are orthogonal — say so loudly

`tiers/README.md` already fixes the laws and varies only the artifacts. Nesting inherits that
unchanged, with one consequence worth stating because the intuition runs the wrong way:

**Outer scopes are usually LOWER tier than inner ones.** A work root is plausibly **Lite** — charter,
ledger, observation log, nothing more. A single client project may well be **Full**. The root spans
more and demands less; the project spans less and demands more.

Without this stated, someone will build a Full apparatus at `~/work/` and abandon the whole thing in
week three, which is the exact failure `tiers/README.md` was written to prevent.

---

## 6. Scope

### IN

1. `.astronomer/scope.toml`, the resolver, and `astro whoami`.
2. Namespace prefixes with installer-enforced uniqueness and a citation checker.
3. Per-scope charter / ledger / observations; root-only doctrine, capability inventory, operator
   profile.
4. `astro promote`, the origin stub, and bare-ID rewriting on promotion.
5. Staleness reporting for ancestor changes.
6. Reference-based `CLAUDE.md` composition with a budget ceiling.
7. `astro scope-stats` reporting the actual write distribution.

### OUT

1. **Any automatic upward write.** Promotion is always a human act.
2. **Any automatic rewrite of a descendant.** Aftershocks notify; they do not edit.
3. Cross-scope *merging* of ledgers into one view. Ancestors are read in place, cited by prefix.
4. Multi-machine or multi-operator scope trees. `CAPABILITY-INVENTORY` and `OPERATOR-PROFILE` are
   root-only precisely because that case is out.
5. Retrofitting the existing ~30 flat instances into a hierarchy. A flat instance is simply a chain
   of length one and must keep working untouched.

---

## 7. Acceptance criteria

Each is written so it can fail.

1. **`astro whoami`** in a three-level tree prints the chain, each scope's id, role and tier, and
   names which scope owns the cwd.
2. **The installer refuses** a `scope.toml` whose `id` matches any ancestor's, and says which
   ancestor holds it.
3. **`astro check-citations` fails** on a document citing a prefix not in its chain. Demonstrate it
   failing against a deliberately-bad fixture *before* trusting a clean result — the checker
   discipline this framework already paid for twice.
4. **Promotion rewrites bare IDs.** Promote a record containing a bare `D-007` from `REBRAND` to
   `ACME`; assert the landed record reads `REBRAND-D-007` and that a stub remains at the origin.
5. **An ancestor charter change edits no descendant file.** Assert byte-identical descendants, and
   assert `astro status` reports the staleness.
6. **A flat instance still works.** Run every command in a chain of length one; nothing errors and
   nothing asks for a parent.
7. **Budget ceiling holds.** Compose a three-level rendering and assert it is materially smaller
   than the 106 KB naive concatenation. If it is not, 5.7's composition-by-reference has failed and
   depth is unaffordable.
8. **`astro check-scope` flags** an inner charter clause that relaxes rather than narrows an outer
   constraint.

---

## 8. What I could not determine

- **Whether Claude Code loads `CLAUDE.md` from ancestor directories.** The single most
  design-relevant unknown. *Settles it:* create a two-level fixture and observe what a session
  actually reads. Do this **first** — it decides whether §5.7 leans on the runtime or implements
  composition itself.
- **Whether the ~30 existing instances want to nest at all.** The operator describes one hierarchy.
  If most stay flat, the earn-your-existence rule matters more than the resolver.
- **What a scope should do about `reference/` corpora.** `K-7` says a shared index has finite signal
  and adding to it can subtract. A client-scope vendor corpus inherited by every project could be
  exactly that failure. Not designed here.
- **Whether `DATA-BOUNDARY` genuinely narrows inward** in practice, or whether the filesystem reach
  is identical at every level and the per-scope copy is ceremony. Worth measuring on the operator's
  real tree before building it per-scope.
- **Nothing in this brief has been built or tested.** Every mechanism is a proposal; the only
  verified content is §3.

---

## Return

A pull request against `project-astronomer` implementing §6 IN, with §7's eight criteria
demonstrated — each shown failing before it is shown passing. If §8's first unknown resolves against
the design, **stop and re-brief rather than working around it**; composition strategy is not a detail
that can be patched later.
