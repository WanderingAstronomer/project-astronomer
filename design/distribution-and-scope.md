---
record_class: living
precedence: 6
confidence: UNVERIFIED
owns:
  - distribution-mechanism
  - scope-resolution
  - scope-namespacing
  - upward-promotion
  - core-hosting
  - upstream-contribution
supersedes: design/nested-scopes.md
verified_by: tools/fleet-census.py (fleet facts) + two-level runtime fixture (§0.2); the mechanisms remain unbuilt
last_verified: 2026-08-19
---

# BRIEF — `distribution-and-scope` — Astronomer as an installable, updatable, nestable framework

> **This brief supersedes `design/nested-scopes.md`**, which covered only nesting and contained a
> direct contradiction with the distribution design (see §4.1). Do not work from that file.
>
> **Status: design brief. Nothing here is built.** Every mechanism is a proposal.
>
> **§3's measurements were re-run on 2026-08-19 and four of them were wrong. §0 is the
> correction and it is the first thing to read.** Where §0 and a later section disagree, §0 wins;
> the later sections have been corrected in place and each correction says so.

---

## 0. CORRECTION — what was re-measured, and what it refutes

This section was added `2026-08-19T22:11Z` after the brief's own instruction was followed:
*"run the normalised comparison across all 30 before step 1"* and *"build a two-level fixture and
observe what a session actually reads. **Do this first.**"*

Both were done. The instrument is [`tools/fleet-census.py`](../tools/fleet-census.py), verified by
[`tools/verify-census.py`](../tools/verify-census.py), which seeds three defects — LF normalisation
removed, history lookup removed, worktree detection disabled — and confirms each is caught. **The
clean census result is reported only because the census was first observed failing.**

### 0.1 The fleet is a third of the stated size, and its drift is a ninth

| Claim in §3 | Measured 2026-08-19 | Verdict |
|---|---|---|
| "~30 project instances" | **9 install points, 7 distinct projects** | `REFUTED` |
| Instances are independent | **`<worktree-A>` and `<worktree-B>` are git worktrees of `vociferous-next`** — one project, three checkouts | `REFUTED` |
| "Genuine drift, entire surface: 3 files" | **9 files, which fold to 4 distinct artifacts in 2 of 7 projects** | `CORRECTED` |
| "45 of 47 shared docs identical" | **387 of 444 managed files match HEAD exactly** | `CONFIRMED in spirit` |
| `install/retrieval-setup.md` drifted, 20 lines | **4 of 5 instances are byte-identical to HEAD.** The 20 lines are an **uncommitted change in upstream's own working tree** | `REFUTED` |
| `skills/astronomer-start` drifted, 2 lines | **Stale, not drifted** — it matches upstream `4a33900e`; upstream later added `K-7` | `RECLASSIFIED` |
| 2 orphaned capabilities | **4.** The fourth is `<instance-D>`' `astronomer-intake` "Step 2a", operator-approved under `<instance-D> D-029` | `CORRECTED` |

**The defect underneath all of it is one defect, and it is a design defect, not a counting error.**
§5.3's lockfile classifies a managed file two ways — **clean** or **drifted**. That split cannot
tell *an old release* from *a local edit*. Measured: of the 57 managed files that do not match
HEAD, **48 are clean older releases** — byte-identical, after LF normalisation, to a commit that
upstream actually shipped. `<instance-C>` alone holds 45 of them and **has edited nothing**.

Under §5.4 as written, `astro update` refuses to touch a drifted file. So adopting the installer in
`<instance-C>` would refuse 45 files, write 45 `.incoming` files, and hand the operator 45
decisions **that are all the same decision**. That is §4.2's stated failure — *"the operator learns
to ignore the one signal the system exists to produce"* — arriving by a second route the brief did
not check. **The classification must be three-way**, and the census already implements it:

> `current` (matches HEAD) · `stale` (matches an earlier upstream commit — safe to overwrite, and
> the census names which) · `drifted` (matches no version upstream ever shipped — never overwrite).

Consequence for §8: **migration is smaller than the brief hoped and differently shaped.** Not "3
files across ~30 instances" but **4 artifacts across 2 projects**, with 48 files updating
mechanically and silently once staleness is distinguishable from drift.

### 0.2 The two runtime unknowns are settled — and they refute D4 and D5

§11 called these "the two highest-value unknowns" and said to settle them with a fixture before
implementing. A two-level fixture was built and a real `claude` session run inside it, twice, with
the git repository root moved between runs. Ancestor and descendant each carried a distinct
`CLAUDE.md` token and a distinctly-named skill.

| Fixture | Ancestor `CLAUDE.md` loaded? | Ancestor skill available? |
|---|---|---|
| Repo root **above** the working dir (ancestor inside the repo) | **yes** | **yes** — the skill ran and returned its token |
| Repo root **at** the working dir (ancestor outside the repo) | **yes** | **no** — the probe returned `NOSKILL` |

Falsified in both directions: the skill was invoked by name, and the negative case returned the
sentinel rather than merely omitting the skill from a list.

**Neither of the two branches §7.1 anticipated is what happens. The measured answer is a third one:**

| Mechanism | Walks up from the working directory | Stops at |
|---|---|---|
| `CLAUDE.md` / `CLAUDE.local.md` | yes — **loaded in full, at launch**, concatenated root-first | the **filesystem root**; it crosses repository boundaries |
| `.claude/skills/` | yes | the **repository root**; it does **not** cross |

Three consequences, each fatal to something the brief committed to:

- **D4 is `REFUTED` as stated.** Its axis — path-resolved docs versus runtime-resolved skills — 
  predicts skills must install at *every* scope. They must not. Inside one repository, skills
  resolve from ancestors, so a scope chain within a repo needs **one** skills install, at the repo
  root.
- **D5 is `REFUTED` as stated.** The hosting unit is not the *chain*. **It is the repository.** A
  chain that crosses a repo boundary needs one skills host **per repository** it spans. The
  measured fleet is exactly this shape: `<instance-D>` is one repo containing `<nested-dir>/`, so one
  skills install serves both; `DevSlop/` is not a repo and each project beneath it is, so the seven
  projects there need seven.
- **§6.7's composition-by-reference is not achievable, and the budget problem is worse than
  stated.** Ancestor `CLAUDE.md` files are loaded **in full at launch** by the runtime. There is no
  on-demand path to opt into and `astro render --budget` cannot prevent it, because the runtime does
  the loading, not `astro`. Depth cost is **linear and unavoidable**. See the corrected §6.7.

**Per this brief's own Return clause, that is a stop-and-re-brief condition, and this section is the
re-brief.** Part A (distribution, flat) does not depend on any of it and survives; Part B's
organising principle does not.

### 0.3 What is now recommended

1. **Part A still ships first (D11 stands, and is strengthened).** It is unaffected by §0.2 and
   needs one change: the three-way classification of §0.1.
2. **Part B must be re-drawn around the repository boundary**, not the chain. `scope.toml` and the
   namespace enforcement of §6.2 are unaffected and remain correct.
3. **Nothing should be written to any instance until the four drifted artifacts are harvested.**
   §8's ordering — harvest before install — was right, and the harvest list is longer than it knew.
4. **`astro` remains barred by the CHARTER.** "Out of scope: tooling that generates or validates
   projects" (`D-005`). `D-005` sunsets on condition 6, which was met on `2026-08-01` — so the bar
   is revisitable, but revisiting it is an operator decision recorded in `DECISIONS.md`, not
   something a brief may assume. **Building `astro` is blocked on that entry.** The census is not:
   it measures and writes nothing, in the same class as `check-corpus.py`.

---

## 1. Read this first

Two problems, one system.

**Problem A — distribution.** Astronomer lives in **9 install points across 7 projects**, maintained
by hand (measured §0.1; the first draft said ~30). Every
update means touching each project. This does not scale.

**Problem B — scope.** A single flat instance cannot span `work → clients → client → projects →
project`. One charter cannot usefully constrain both a rebrand and a tax filing.

They are the same system because the thing being distributed is the thing being scoped.

### The decisions, committed

| # | Decision |
|---|---|
| **D1** | **A vendoring installer (`astro`)**, driven by a manifest in the central repo and a lockfile per instance. Not a submodule, not a subtree, not a package. §5.2 |
| **D2** | **Paths do not move.** Ownership is declared by manifest and enforced by lockfile hashes, not by directory nesting. §5.1 |
| **D3** | **Hashes are computed on LF-normalised content.** Without this every Windows instance reports total drift forever. §4.2 |
| ~~**D4**~~ | ~~*Core splits by how it is read: path-resolved docs install once per chain; runtime-resolved skills install at every scope.*~~ **`REFUTED` 2026-08-19 by fixture (§0.2).** Skills *do* resolve from ancestors, bounded by the repository root. Replaced by **D4′**. |
| **D4′** | **Core splits by *what bounds its lookup*.** Both docs and skills resolve upward; they stop at different places. `CLAUDE.md` stops at the filesystem root, `.claude/skills/` at the **repository root**. §7.1 |
| ~~**D5**~~ | ~~*One "core host" per chain.*~~ **`REFUTED` 2026-08-19 (§0.2).** The chain is the wrong unit. Replaced by **D5′**. |
| **D5′** | **One skills host per *repository* the chain spans; one docs host per chain.** A flat instance is a chain of length one inside one repository, so the flat case remains a special case of the nested one. §7.1 |
| **D6** | **Scopes self-identify by walking up**, exactly like `.git`. §6.1 |
| **D7** | **Bare IDs always mean the local scope**; ancestors are always cited with a prefix, enforced by the installer and a checker. §6.2 |
| **D8** | **90/8/2 is not a quota.** It becomes *write at the smallest scope where the claim is true*, and 90/8/2 becomes a measurable calibration signal. §6.4 |
| **D9** | **Upward is explicit, downward is automatic, neither rewrites anything.** Aftershocks notify; they never edit. §6.6 |
| **D10** | **Two distinct verbs**, because the earlier draft overloaded one word: `astro contribute` sends work *outward* to the central repo; `astro raise` moves a record *upward* a scope level. §7.2 |
| **D11** | **Distribution ships first (v1.0); scope ships second (v1.1).** All but one existing install point is flat — `<instance-D>` is the exception and it nests inside a single repository — and the flat path must be proven before nesting is added. §8 |
| **D12** | **Managed files classify three ways, not two: `current` / `stale` / `drifted`.** A two-way split reports 48 measured files as local edits when their projects have edited nothing. §0.1 |
| **D13** | **Worktrees are folded into their repository before the fleet is counted or written to.** Three checkouts of one project are one project, and an installer that writes to all three writes to one git index. §0.1 |

---

## 2. Why this scope exists

The operator's framing on scope: *"We don't want one Astronomer instance accounting for absolutely
everything all the time because that becomes too big to handle."*

That is the framework's own position, already written down. `tiers/README.md` says a framework
demanding a full apparatus for a small effort **"gets abandoned in week three and takes its laws with
it."** A single root instance spanning all work is that failure at a larger radius.

Nesting scales the framework *outward* the way tiers already scale it *down*.

On distribution, the current mechanism is `install/README.md` — a careful six-step manual procedure
(Step 0a adoption, Step 0 decisions, Step 1 collaborator layer, Step 2 skills, Step 3 artifacts,
Step 4 retrieval, Step 5 role bounds). It is good, and it is a **creation** procedure with no update
path. `astro` automates those steps and adds the half that is missing.

---

## 3. Verified current state

> **This section was measured against one instance and extrapolated. It has been re-measured
> across the whole fleet — see §0.1 for what changed.** The table below is the corrected one.
> Reproduce it with `python tools/fleet-census.py`.

| Fact | Value | Consequence |
|---|---|---|
| Install points carrying `astronomer-*` skills | **9** | Not ~30. The hand-maintenance cost is a third of the stated one |
| Distinct projects, worktrees folded | **7** | `<worktree-A>` and `<worktree-B>` are worktrees of `vociferous-next` |
| Managed files matching upstream `HEAD` | **387 of 444** | The fleet has *not* diverged |
| Managed files **stale** — clean earlier releases | **48** | Mechanical updates. 45 are `<instance-C>`, which has edited nothing (D12) |
| Managed files **genuinely drifted or novel** | **9**, folding to **4 distinct artifacts in 2 of 7 projects** | The entire human-decision surface |
| The 4 artifacts | `rituals/deliberation-thread.md` (novel) · `rituals/README.md` (edit) · `skills/astronomer-supervise/` (novel) · `<instance-D>`' `skills/astronomer-intake` "Step 2a" (novel, `<instance-D> D-029`) | The harvest list, one longer than §8 knew |
| CRLF is real but not universal | **3 of 9** install points carry CRLF; 161 files identical only after normalisation | D3 stands and is load-bearing for exactly those three |
| Vendored-tree layouts found in the wild | **5** — `docs/astronomer/` full · `docs/astronomer/` partial (no `install/`) · `astronomer/` at repo root · `<nested-dir>/astronomer/` nested · skills-only, no tree | The installer cannot assume a `dst`; it must discover or be told |
| Upstream `HEAD` | `3fed7fc`, **2026-08-01** | Upstream ships 8 skills; two projects run 9 |
| Upstream working tree | **dirty** — `install/retrieval-setup.md` has 20 uncommitted lines | The "instance drift" §3 originally reported in that file was this |
| `vociferous-next/CLAUDE.md` | **35,454 bytes / 463 lines** | Per-level cost, and §0.2 makes it unavoidable per level |
| Citations to `docs/astronomer/<subdir>/` in one instance | **24 files** | Paths must not move (D2) |
| Tiers | Lite / Standard / Full | Sizing is solved; scope must not reinvent it |

### Settled since the first draft

- **Claude Code loads `CLAUDE.md` from ancestor directories** — in full, at launch, across
  repository boundaries. `CONFIRMED` by fixture, §0.2.
- **Claude Code resolves `.claude/skills/` from ancestor directories** — bounded by the repository
  root. `CONFIRMED` by fixture, falsified both ways, §0.2. **This refutes D4 and D5.**
- **Whether the other instances resemble this one.** They do not, uniformly: one is 45 files behind,
  one holds an unharvested operator-approved capability, and five layouts exist. Measured, not
  inferred.

### Still UNVERIFIED

- Whether the 7 projects want to nest at all. The operator describes one hierarchy; `<instance-D>`
  is the only measured two-level structure and it arrived without a design.
- Whether `<instance-E>` (skills, no vendored tree) is a deliberate configuration or an incomplete
  install. It is clean either way, which is why the census cannot tell.

---

## 4. What makes this harder than it looks

### 4.1 The two earlier drafts contradicted each other

The distribution plan installs `doctrine/`, `rituals/`, `artifacts/` into **every** instance. The
nesting brief installs them at the **root only**, inherited. In a three-level tree, either
`rebrand/docs/astronomer/doctrine/` exists or it does not — and the answer changes what the lockfile
manages, what `astro status` checks, and whether a project can be updated independently.

**§7.1 resolves this**, and the resolution is not a compromise: the two drafts were splitting on the
wrong axis.

### 4.2 CRLF will destroy the drift signal if unhandled

A raw-byte comparison reported 46 of 47 files drifted when 45 were byte-identical. Ship that and
every Windows instance reports total drift permanently, and the operator learns to ignore the one
signal the system exists to produce. **This is not a detail. It is D3.**

### 4.3 The namespace problem is the scope feature's risk, concentrated

`vociferous-next/CLAUDE.md` already carries the scar at *two* namespaces:

> A bare `D-NNN` resolves to **this project's spine only**. […] Write the prefix even when context
> makes it obvious — it stops being obvious the moment the sentence is quoted somewhere else.

And what the failure cost: an ID renumber swept the spine and two records, but issue bodies kept
citing old numbers **which now resolved to different rulings** — one issue cited them seven times.

Three scopes means four namespaces including `AST-`. A bare `D-012` written at project scope and
quoted at client scope **silently changes meaning**, because both resolve. Everything else here is
mechanism; this must be made *impossible*, not discouraged.

### 4.4 Precedence has no single direction

An outer scope binds inner ones on constraints; an inner scope wins on specifics. A design that
picks one direction globally is wrong half the time. §6.5.

### 4.5 Astronomer must land at two roots

`docs/astronomer/**` and `.claude/skills/astronomer-*`. One source, two destinations. This single
fact is what rules out submodules and subtrees (§5.2) — and it is also the seam that D4 turns from a
problem into the organising principle.

---

## 5. Part A — Distribution (ships as v1.0)

### 5.1 Ownership roles, and why paths do not move

Moving core under `docs/astronomer/core/` would make ownership visible in the path. Rejected: **24
files in one instance cite `docs/astronomer/<subdir>/` paths**, so roughly 700 across the fleet, many
in frozen records that must not be rewritten. A path migration converts a distribution upgrade into a
corpus-wide edit.

Ownership is instead declared and **checkable**, which is stronger than a directory convention a
human can violate silently.

| Role | Owner | On update | Contents |
|---|---|---|---|
| **Core** | Central repo | Overwritten when clean; **never** when drifted | `doctrine/`, `rituals/`, `artifacts/`, `tiers/`, `tools/`, `provenance/lineage.md`, `astronomer-*` skills |
| **Local** | The instance | Never touched | `CAPABILITY-INVENTORY.md`, `DATA-BOUNDARY.md`, `OPERATOR-PROFILE.md`, `OBSERVATIONS.md`, `reference/`, the project's own charter and spine, project-only skills |
| **Rendered** | Generated | Regenerated; staleness reported, never forced | `CLAUDE.md` |

**Why the split falls there.** Core is the shared vocabulary — `L-14` says vocabulary has one home,
and if two instances hold different texts of `01-laws.md` then a citation to `L-9` stops resolving to
the same thing. Local is everything that measures *this* instance; shipping a central
`CAPABILITY-INVENTORY.md` would be shipping a false measurement. **Rendered is the role most plans
miss and it is the entire methodology dimension** — `CLAUDE.md` already declares itself "a rendering,
not a source" and states that a rendering is regenerated when its source changes, never edited in
place. Nothing enforces that today.

### 5.2 The mechanism, and the four rejections

**`astro`: a single-file, stdlib-only Python installer, distributed by the central repo, self-updating.**

- **git submodule — rejected.** A submodule owns exactly one directory; Astronomer lands at two
  (§4.5). Worse, `.claude/skills/` must *also* hold instance-only skills — measured here:
  `behavioral-audit`, `feature-spawn` — and a submodule cannot host foreign siblings. It also
  assumes every instance is a git repo; the lineage records `<instance-F>` as "not a git
  repository".
- **git subtree — rejected.** Same single-prefix limit, plus it rewrites instance history and has no
  per-file drift policy — so it cannot satisfy the actual requirement, which is *preserve local
  customisation while updating everything else*.
- **npm / pip package — rejected.** Installs into `node_modules` / `site-packages`, not
  `.claude/skills/` where the runtime must find it, so a post-install copy is needed anyway — the
  vendoring installer in costume. It also forces a language runtime onto non-software instances; the
  lineage records `data-dating` as a non-software research study, and that instance is the only
  evidence the framework generalises beyond code.
- **GitHub template repo — rejected.** Solves creation, not update. Approximately the current state.

### 5.3 Manifest (central) and lockfile (per instance)

```toml
# manifest.toml
schema = 2

[[group]]
name = "doctrine"
src  = "core/doctrine/"
dst  = "docs/astronomer/doctrine/"
policy = "managed"
hosting = "chain"        # installed once per chain — see 7.1

[[group]]
name = "skills"
src  = "core/skills/"
dst  = ".claude/skills/"
policy = "managed"
hosting = "scope"        # installed at EVERY scope — see 7.1
prefix_only = "astronomer-"   # never touches sibling dirs

[[group]]
name = "scaffold"
src  = "templates/"
dst  = "docs/astronomer/"
policy = "once"          # written if absent, never updated

[[group]]
name = "claude-md"
src  = "templates/CLAUDE.md.tmpl"
dst  = "CLAUDE.md"
policy = "rendered"
```

Four policies carry the design: `managed` (shared core), `once` (scaffold then let go), `rendered`
(the methodology dimension), and the `hosting` axis added by D4.

```json
// .astronomer/manifest.lock
{
  "version": "v1.4.0",
  "resolved": "a1f9c3e…",
  "normalisation": "lf",
  "core_host": "self",          // or a relative path to the hosting ancestor
  "files": {
    "docs/astronomer/doctrine/01-laws.md": { "sha256": "9c2e…", "policy": "managed" }
  }
}
```

The lockfile makes the central requirement mechanical: every managed file is classifiable at any
moment as **clean** (hash matches), **drifted** (local edit), or **stale** (upstream moved).

### 5.4 Command surface

| Command | Does |
|---|---|
| `astro status` | Classify every managed file. Non-zero exit on drift, so CI can gate |
| `astro update` | Overwrite **clean** files only. Drifted files are never touched — the incoming version lands as `<file>.incoming` and is reported |
| `astro diff <path>` | Local vs incoming for a drifted file |
| `astro contribute <path>` | **Outward.** Package a local improvement as a patch + provenance, open a PR against the central repo |
| `astro render` | Regenerate `CLAUDE.md`; report staleness without forcing |
| `astro pin v1.3.0` / `astro rollback` | Version control per instance |
| `astro whoami` | Print the scope chain *(v1.1)* |
| `astro raise <record> --to ACME` | **Upward.** Move a record a scope level *(v1.1)* |

### 5.5 Why scale stays flat

**No per-instance state lives centrally.** The central repo does not know which projects exist; each
instance carries its own lockfile and pulls when it chooses. A 10th or 100th instance is one
`astro install` and changes nothing centrally. Fan-out is a loop:

```bash
for d in ~/Documents/DevSlop/*/; do
  [ -f "$d/.astronomer/manifest.lock" ] || continue
  astro --root "$d" update --report-only-drift
done
```

Clean instances update silently; drifted ones report and are left alone. **Operator attention is
spent only where a human decision exists** — measured today, 3 files rather than 30 projects.

### 5.6 Versioning and rollback

Semver, with tiers defined by *what breaks in an instance*, because most of what ships is prose.

| Bump | Means | Examples |
|---|---|---|
| **MAJOR** | A citation stops resolving, or a rule changes meaning | A law renumbered or repealed; a ritual renamed; a path moved; a skill's trigger contract changed |
| **MINOR** | New capability, nothing existing changes meaning | A new ritual; a new skill; `astronomer-supervise` arriving |
| **PATCH** | Correction leaving every citation valid | A typo; a clarified sentence; a corrected `file:line` |

**A renumbered law is always MAJOR.** This framework has already paid for the alternative (§4.3).

Three postures per instance: **floating** (`astro update` takes latest), **pinned**
(`astro pin v1.3.0` — correct for a project mid-audit, where a doctrine change would move the ground
under an in-flight investigation), **held at minor** (`astro pin v1.3` — patches yes, features no).

**Rollback is reinstallation, not reversal.** `astro rollback` reinstalls the previous version's
exact hashes. Because managed files are overwritten only when clean, rollback **cannot** destroy
local work — a drifted file was never in the installer's hands. That property is what makes rollback
safe to run without thinking, which is the only kind anyone uses under pressure.

**`CLAUDE.md` staleness is reported, never auto-applied.** Re-rendering it is a content decision: it
is the file every session reads first, and this framework has a recorded scar where a stale
prohibition in it cost an entire session, because it was obeyed over a ledger that had already
granted the authority.

---

## 6. Part B — Scope (ships as v1.1)

### 6.1 Discovery and self-identification

```toml
# .astronomer/scope.toml
id     = "ACME"          # namespace prefix — unique among ancestors, enforced
name   = "Acme Corp"
role   = "client"        # conventional: root | domain | client | project
tier   = "standard"      # orthogonal to scope — see 6.8
root   = false           # exactly one instance per chain sets true
```

Resolution walks up from cwd collecting `scope.toml` files until `root = true` or the filesystem
root. The ordered chain **is** the scope path:

```
WRK  ~/work                                          root,   tier=lite
 └ ACME  ~/work/clients/acme                         client, tier=standard
    └ REBRAND  ~/work/clients/acme/projects/rebrand  project, tier=full
```

`astro whoami` prints that chain. A directory with no install but an ancestor that has one **resolves
to the nearest ancestor and says so** rather than failing.

### 6.2 Namespaces — mechanical, not conventional

**Bare IDs always mean the local scope. Ancestors are always cited with their prefix.**

| Written at | Bare `D-012` means | Client decision cited as | Astronomer's own |
|---|---|---|---|
| `REBRAND` | `REBRAND-D-012` | `ACME-D-004` | `AST-D-051` |
| `ACME` | `ACME-D-012` | `WRK-D-001` | `AST-D-051` |

Three enforcement points, none a convention:

1. **The installer refuses a prefix already used by any ancestor**, naming which one holds it.
2. **`astro check-citations`** resolves every `<PREFIX>-D-NNN` in scope-owned documents and fails on
   any prefix outside the chain. Model it on the existing `check_issue_citations.py`.
3. **`astro raise` rewrites bare IDs before the record lands upward** — at the new scope, bare no
   longer means what it meant. **This is the step most likely to be forgotten and the one that
   produces silent wrong-resolution.**

### 6.3 What is scoped

| Artifact | Where | Why |
|---|---|---|
| `doctrine/`, `rituals/`, `artifacts/`, `tiers/`, `tools/` | **Core host only** (§7.1) | Shared vocabulary; `L-14` |
| `astronomer-*` skills | **Every scope** (§7.1) | Runtime-resolved, not path-resolved |
| `CHARTER.md` | Every scope | A client's "never do this" binds their projects |
| `DECISIONS.md` | Every scope | Rulings have natural altitude |
| `OBSERVATIONS.md` | Every scope | Mostly local; occasionally raised |
| `CAPABILITY-INVENTORY.md` | **Root only** | It measures the *machine*. One machine |
| `OPERATOR-PROFILE.md` | **Root only** | One operator |
| `DATA-BOUNDARY.md` | Every scope | The boundary genuinely narrows inward |
| `CLAUDE.md` | Every scope, composed by reference | §6.7 |

### 6.4 Write routing — the test that replaces 90/8/2

A percentage cannot be executed. `L-4` already asks the right question — every claim carries scope:

> **Write the record at the smallest scope where the claim is true.**

True only of this project → local. True of every project for this client → client. True of all work →
root.

The distribution then *falls out* instead of being enforced, and 90/8/2 becomes better than a quota:
a **calibration signal**. `astro scope-stats` reports the actual split, and a project writing 40 %
upward is evidence that either the scopes are drawn wrong or someone is generalising from one
instance — `L-4`'s `ASSERTED-UNIVERSAL` failure, now visible as a number.

### 6.5 Precedence — inner may narrow, never relax

> **An inner scope may NARROW an outer constraint. It may never RELAX one.**

`ACME` says *"no client data leaves the tenant"*; `REBRAND` may add *"and no screenshots"*. It may not
carve an exception. On **specifics** — build commands, layout, local vocabulary — the inner scope
simply wins, because the outer has no opinion.

`astro check-scope` flags an inner charter clause that contradicts rather than narrows. Build it
early; it is the one place nesting can silently break a promise made higher up.

### 6.6 Ripple, not domino

- **Inheritance (down)** — automatic, every session. A session at `REBRAND` reads `WRK` and `ACME`
  charters, ledgers and boundaries as ancestors.
- **Raising (up)** — explicit. `astro raise OBS-014 --to ACME` moves the record, rewrites bare IDs,
  and leaves a stub at the origin so local citations still resolve.
- **Aftershock** — when an ancestor changes, descendants are **not** edited. The next `astro status`
  reports `ancestor changed: ACME-D-004 (charter) — affects 2 local records`. The descendant decides.

**The shock is a notification, and it stops at whoever is willing to act on it.** A root charter
amendment cannot silently rewrite thirty projects.

### 6.7 Depth — budget-limited, not number-limited

1. **Mechanically unlimited** — one `stat` per level.
2. **Budget-limited, the real constraint — and the constraint is harder than this brief first
   claimed.** `CLAUDE.md` is 35 KB here; three levels ≈ 106 KB before work starts.

   > **`REFUTED 2026-08-19` (§0.2).** This item read: *"Composition must be by reference, not by
   > copy: an inner `CLAUDE.md` carries a pointer to its ancestors plus only its own deltas;
   > ancestors are read on demand. Depth cost becomes sublinear."* **Ancestors are not read on
   > demand.** Measured: the runtime walks up from the working directory and loads every ancestor
   > `CLAUDE.md` **in full, at launch**, concatenated root-first, across repository boundaries.
   > There is no by-reference mode to opt into, and `astro render --budget` cannot refuse what the
   > runtime has already loaded. **Depth cost is linear and unavoidable.**

   What survives, restated so it can be executed:

   - **The ceiling is on the chain, not the file.** A budget check must sum every ancestor
     `CLAUDE.md` from the filesystem root down and compare *that* to the ceiling. A per-file check
     passes three times and still ships 106 KB.
   - **An inner `CLAUDE.md` must carry its deltas and nothing else** — no restatement of ancestor
     content, no pointers to it. The runtime has already supplied it, so a summary is duplication
     paid for twice, and a *stale* summary is worse: it contradicts the ancestor it copied.
   - **The only real lever is authored size**, plus the runtime's own `claudeMdExcludes`, which
     drops named ancestor files by glob. That setting is the escape hatch for a chain whose root is
     shared with unrelated work — which is exactly `~/Documents` in the measured fleet.
   - **The 106 KB figure is now a floor to design against, not a worst case to engineer away.**
3. **Earn-your-existence.** A scope must hold ≥1 record that could not live at its parent or child.
   `astro scope-stats` reports empty scopes; an empty scope is deleted, not kept for symmetry.

**Three is the natural depth; warn at four; refuse past six.** Four is legitimate
(`work → domain → client → project`). Past six the earn-your-existence rule is almost certainly
failing somewhere, and refusal is cheaper than the audit.

### 6.8 Tier and scope are orthogonal, and the intuition runs backwards

`tiers/README.md` fixes the laws and varies only the artifacts. Nesting inherits that unchanged, with
one consequence that must be stated because people assume the opposite:

**Outer scopes are usually LOWER tier than inner ones.** A work root is plausibly **Lite** — charter,
ledger, observation log, nothing more. A single client project may be **Full**. The root spans more
and demands less.

Unstated, someone builds a Full apparatus at `~/work/` and abandons the whole thing in week three —
exactly the failure `tiers/README.md` exists to prevent.

---

## 7. Where Part A and Part B meet

### 7.1 The core-host rule — resolving §4.1

> **`REFUTED 2026-08-19` and rewritten.** The original split core on *how a file is reached* —
> path-citation versus runtime — and concluded that docs install once per chain while skills install
> at every scope. The fixture in §0.2 refutes it: **both** resolve upward. The section closed by
> naming the branch that would collapse it, and that is the branch that happened. What follows is
> the corrected rule; the original reasoning is preserved in the paragraph above.

Both docs and skills are reached by walking up from the working directory. They differ in **where
the walk stops**, and that — not path-versus-runtime — is the axis:

| | Found by walking up | The walk stops at | Therefore installed |
|---|---|---|---|
| `doctrine/`, `rituals/`, `artifacts/`, `tiers/`, `tools/` | path citation, from a `CLAUDE.md` that is itself loaded from ancestors | the **filesystem root** — no boundary | **once per chain** |
| `astronomer-*` skills | the runtime's own discovery | the **repository root** | **once per repository the chain spans** |

> **A chain has one docs host. It has one skills host *per repository it spans*. A flat instance is a
> chain of length one inside one repository, so both rules collapse to "install here" and the flat
> case remains a special case of the nested one.**

That last property is what lets D11 ship distribution first without designing nesting into a corner,
and it survives the refutation intact.

Four consequences:

- **Version skew on docs is impossible** — one copy per chain. Skew on *skills* is possible **only
  across repository boundaries**, and is therefore bounded and enumerable: `astro status` reports one
  skills version per repository in the chain.
- **The scope tree and the repository tree are different trees, and the design must hold both.**
  Nothing forces a scope boundary to coincide with a repository boundary, and in the measured fleet
  they mostly do not: `<instance-D>` is one repository spanning two scopes, while the seven projects
  under `DevSlop/` are seven repositories at one scope each.
- **A descendant's lockfile lists only what it hosts**, plus a pointer to its docs host — and, when
  it is the first scope inside a new repository, its own skills.
- **`docs/astronomer/` in a descendant contains only local artifacts** (charter, ledger, observations,
  boundary). Doctrine is cited across the chain by path.

**The open question this replaces the old one with:** a scope chain whose descendant sits in its own
repository gets ancestor `CLAUDE.md` but *not* ancestor skills — so the always-loaded file will cite
rituals the session cannot invoke. Whether that is tolerable, or whether such a descendant must carry
its own skills copy, is **not settled here** and is the first thing Part B has to decide.

### 7.2 Two verbs, deliberately different words

The earlier draft used `promote` for both directions. They are different operations and sharing a
name would produce exactly the class of confusion §4.3 is about.

| Verb | Direction | Destination | Frequency |
|---|---|---|---|
| `astro contribute` | **Outward** | The central GitHub repo, as a PR | Rare; this is how `deliberation-thread` and `astronomer-supervise` go home |
| `astro raise` | **Upward** | The parent scope, in the same tree | Uncommon; the 8 % and 2 % of D8 |

A record can be both: raised to the client scope, and later contributed upstream if it turns out to
be doctrine rather than client policy.

### 7.3 What happens to `install/README.md`

`astro install` automates its Steps 1–3 and 5. **It is not deleted.** It becomes the manual fallback
and the explanation of *what* is being installed and why — the reasoning `astro` executes but does
not contain. Step 0/0a (the decisions before anything is copied) and Step 4 (retrieval) stay manual,
because both are operator judgement rather than file movement.

---

## 8. Migration

Sequenced deliberately. **Harvest precedes installation** — installing first would overwrite the two
orphaned capabilities with an upstream that never learned them.

### Phase 1 — v1.0, distribution only, flat

1. **Harvest the orphans upstream.** `rituals/deliberation-thread.md`,
   `skills/astronomer-supervise/`, the `rituals/README.md` row, the 2-line `astronomer-start` change.
   Review `install/retrieval-setup.md`'s 20 changed lines by hand — the one drift large enough to be
   a real divergence rather than an addition.
2. **Restructure upstream** into `core/` + `templates/`. Invisible to instances, because the manifest
   maps `src → dst`. This is the decoupling the manifest buys.
3. **Write `manifest.toml` and `bin/astro`; tag `v1.0.0`** — defined as *the union of upstream and
   every capability any instance had invented*, so no instance loses ground by adopting.
4. **GATE — pilot on `vociferous-next`.** Require: every managed file **clean**; the 3 known drifts
   reported and **not** overwritten; `behavioral-audit` and `feature-spawn` untouched; suite
   unchanged. `L-8`, and the roll-out does not pass a NO-GO.
5. **Waves of 3, then 10, then the rest.** The wave of three must include `data-dating`
   (non-software) and `<instance-F>` (not a git repo) — the shapes most likely to break assumptions
   the pilot could not test.
6. **Add `astro status` to CI** wherever CI exists.

### Phase 2 — v1.1, scope

7. **Measure the two UNVERIFIED runtime questions** (§3). They decide §7.1.
8. **Implement `scope.toml`, the resolver, `astro whoami`**, and the namespace enforcement of §6.2 —
   *before* any promotion machinery, because the checker must exist before records start moving.
9. **Implement `astro raise`, staleness reporting, `astro scope-stats`.**
10. **Build one real three-level tree** on the operator's actual work directory and run for a week
    before converting anything else.

---

## 9. Scope

### IN

1. `astro` — install, status, update, diff, contribute, render, pin, rollback.
2. Manifest, per-instance lockfile, LF-normalised hashing, the three ownership roles,
   and the three-way `current`/`stale`/`drifted` classification of D12.
3. `scope.toml`, the resolver, `whoami`, namespace enforcement, `check-citations`, `check-scope`.
4. `astro raise`, origin stubs, bare-ID rewriting, staleness reporting, `scope-stats`.
5. Reference-based `CLAUDE.md` composition with a budget ceiling.

### OUT

1. **Any automatic upward write**, and **any automatic rewrite of a descendant.**
2. Cross-scope *merging* of ledgers into one view. Ancestors are read in place, cited by prefix.
3. Multi-machine or multi-operator scope trees — hence root-only `CAPABILITY-INVENTORY` and
   `OPERATOR-PROFILE`.
4. Retrofitting the flat instances into a hierarchy. A flat instance is a chain of length one and
   must keep working untouched.
5. Deleting `install/README.md`.

---

## 10. Acceptance criteria

Each written so it can fail. Demonstrate every checker **failing against a known-bad fixture before
its clean result is believed** — the discipline this framework has already paid for twice.

**Distribution**

1. `astro status` on a fresh install reports **every** managed file clean, on Windows and on Linux.
   *(This is the D3 test. If Windows reports drift, normalisation is broken.)* **Already
   demonstrated** for the classifier: `tools/verify-census.py` seeds the un-normalised hash and
   confirms the CRLF check goes red.
2. `astro update` against a locally-edited managed file **does not modify it**, writes
   `<file>.incoming`, and reports it.
3. `astro update` never touches `.claude/skills/behavioral-audit/` or `feature-spawn/`.
4. `astro rollback` restores the previous version's hashes and leaves drifted files untouched.
5. A non-git instance installs and updates successfully.
   **Note (2026-08-19):** every measured install point is now inside a git repository, but two
   (`<instance-E>`, `Presentations/The Engineer's Dilemma`) are not, and the lineage records
   `<instance-F>` as not a repository. The criterion stands. It also acquires a second edge:
   staleness detection (D12) is defined against *upstream's* history, not the instance's, so a
   non-git **instance** is fine while a non-git **upstream** would disable D12 entirely.
5a. **`astro status` in `<instance-C>` reports 45 files `stale`, not `drifted`, and names the
   upstream commit they match.** This is the D12 test and it is the one that decides whether
   adoption is mechanical or a 45-decision interview. *Already demonstrated by
   `tools/fleet-census.py`; it is restated here because `astro` must not regress it.*
5b. **`astro status` reports `<worktree-A>`, `<worktree-B>` and `vociferous-next` as one project with
   three checkouts, and `astro update` refuses to write to a worktree without an explicit flag.**
   This is the D13 test. Three checkouts share one git index; writing to all three is one project
   being written to three times.
5c. **`astro install` refuses to guess a destination** in an instance whose vendored tree is not at
   `docs/astronomer/`, and names the layouts it found. Five layouts are measured (§3); a wrong
   guess installs a second corpus beside the first.

**Scope**

6. `astro whoami` in a three-level tree prints the chain with each scope's id, role and tier, and
   names which scope owns the cwd.
7. The installer **refuses** a `scope.toml` whose `id` matches any ancestor's, naming the holder.
8. `astro check-citations` **fails** on a document citing a prefix outside its chain.
9. `astro raise` on a record containing a bare `D-007` lands it reading `REBRAND-D-007` upward and
   leaves a resolving stub at the origin.
10. An ancestor charter change leaves every descendant file **byte-identical**, and `astro status`
    reports the staleness.
11. A flat instance runs every command with no parent present and never asks for one.
12. ~~*A composed three-level rendering is materially smaller than the 106 KB naive
    concatenation.*~~ **`WITHDRAWN 2026-08-19` — this criterion cannot be satisfied and could
    never have been.** It presumes composition-by-reference, which §0.2 measured as unavailable:
    the runtime concatenates every ancestor `CLAUDE.md` in full at launch, so the "naive
    concatenation" *is* what a session receives no matter what `astro render` emits. Replaced by:

    **12′.** `astro render --budget` sums every ancestor `CLAUDE.md` **from the filesystem root
    down to the working directory** and fails when the total exceeds the ceiling. It must be shown
    failing on a three-level fixture that passes a per-file check — a per-file ceiling passes three
    times and still ships 106 KB.

    **12″.** A rendered inner `CLAUDE.md` **restates no ancestor content**, verified by a check
    that fails when a heading from an ancestor appears in a descendant's rendering.
13. `astro check-scope` flags an inner charter clause that relaxes rather than narrows an outer one.
14. **A descendant in its own repository reports the skills it cannot reach.** Given a scope chain
    crossing a repository boundary, `astro status` names every `astronomer-*` skill available at the
    ancestor and absent at the descendant. §7.1 leaves the remedy open; the criterion is that the
    gap is *visible*, because the always-loaded `CLAUDE.md` will cite rituals the session cannot
    invoke and nothing else would surface that.

---

## 11. What I could not determine

### Settled on 2026-08-19 — struck through, kept for the reasoning

- ~~**Whether Claude Code loads `CLAUDE.md`, or resolves `.claude/skills/`, from ancestor
  directories.**~~ **Settled by fixture (§0.2).** Both do; they stop in different places. It
  resolved *against* the design, and this document was re-briefed rather than patched.
- ~~**Whether the other 29 instances resemble this one.**~~ **Settled by census (§0.1).** There are
  not 29 others — there are 6 other projects, and they do not resemble it uniformly.
- ~~**The content of `install/retrieval-setup.md`'s 20 changed lines.**~~ **Read.** They are the
  `PROMOTED 2026-08-04` block recording `COAW-D-041`, and they are an **uncommitted upstream
  change**, not instance drift. Four of five instances match `HEAD` exactly.

### Still open

- **Whether upstream's `tools/` should be distributed.** Now five files, and the question sharpens:
  `fleet-census.py` is upstream-only by construction — it reads upstream's git history to date a
  stale file, so it cannot run from inside an instance that lacks that history. `tools/` is
  therefore not one group. Some of it is shippable and some is not.
- **How non-git instances fetch.** Most likely a tarball of the tag; specified as required, not
  designed.
- **Whether a descendant in its own repository must carry its own skills copy** (§7.1). The new
  first question for Part B, created by settling the old one.
- **Whether `DATA-BOUNDARY` genuinely narrows inward**, or whether filesystem reach is identical at
  every level and the per-scope copy is ceremony. Measure on the operator's real tree first.
- **Whether `reference/` corpora should be inheritable.** `K-7` says a shared index has finite signal
  and adding to it can subtract; a client-scope vendor corpus inherited by every project could be
  exactly that failure. Not designed here.
- **Whether `<instance-E>`'s skills-without-a-tree is deliberate.** The census cannot tell, because
  it is clean either way.
- **Whether the CHARTER's bar on tooling is lifted.** `D-005` sunsets on condition 6, met
  `2026-08-01`. Until an entry in `DECISIONS.md` says so, `astro` is out of scope and this brief
  cannot authorise itself. **Operator decision.**
- **The mechanisms in this brief are still not built.** §0's measurements and
  `tools/fleet-census.py` are the only verified content; §3 is now measured rather than
  extrapolated, and everything from §5 onward remains a proposal.

---

## Return

> **The original Return said: *"If §11's first unknown resolves against the design, stop and
> re-brief."* It resolved against the design. This document is the re-brief, and the instruction was
> followed rather than worked around.** What follows replaces the original ask.

**Done, and in this repository now:**

- `tools/fleet-census.py` — the three-way classifier, and the instrument behind every number in §0.
- `tools/verify-census.py` — three seeded defects, each confirmed caught. The census was observed
  failing before its clean result was used.
- §0, and the corrections it forced through §3, §5.1, §6.7, §7.1, §9, §10 and §11.

**Blocked, and on whom:**

- **`astro` itself is blocked on the operator**, not on design. `D-005` and CHARTER "Out of scope"
  bar a CLI; `D-005`'s own sunset condition has been met, so the bar is revisitable — but only by a
  dated entry in `DECISIONS.md`. A brief cannot lift a charter bar by proposing work that violates
  it.

**Next, in order, once that entry exists:**

1. **Harvest the four artifacts** (§3), including the one this brief did not know about. Harvest
   still precedes installation, and now precedes it by a longer list.
2. **Build Part A with D12 and D13 in it from the start.** §10's criteria 1–5c.
3. **Re-draw Part B around the repository boundary** (§7.1), starting with the question §7.1 now
   leaves open.

Phase 1 still merges before Phase 2 begins. **Nothing should be written to any instance until step
1 is done** — `<instance-D>` holds an operator-approved capability that exists in exactly one place
on this machine.
