# CATALOG — `<project name>`

> **Doc class:** living. Rows change status; **IDs never change.** Retire with a `deprecated`
> status — never renumber, never reuse. A reused ID breaks every historical reference to it
> silently: the reference still resolves, to the wrong thing, which is strictly worse than a
> dangling pointer because nothing announces it.

The everything-in-scope inventory. Its purpose is not documentation — it is **coverage**. A
catalog exists so that "we have looked at all of it" becomes a claim someone can check, and so
that the thing nobody owns becomes visible before it becomes the thing nobody fixed.

**Required at:** **Full** — and deliberately not a law. An exhaustive inventory with an empty
orphan list is powerful and it is expensive, and demanding one of a small project is how you get a
project that never starts. Build this when scope ambiguity is the binding constraint — when
people are asking "is that ours?" more than once a week — and not before.

---

## Rows

| ID | Name | Type | Responsibility | Depends-on / Used-by | Status | Notes |
|---|---|---|---|---|---|---|
| `<PFX-001>` | `<name>` | `<type>` | `<what it is responsible for, in one clause — the reason it exists, not a description of it>` | **dep:** `<ids>` · **used-by:** `<ids>` | `<active / partial / deprecated / planned / unknown>` | `<…>` |
| `<PFX-002>` | `<name>` | `<type>` | `<…>` | **dep:** `<ids>` · **used-by:** `<ids>` | `<…>` | `<…>` |

### The columns, and what each one is for

**`ID`** — a permanent address, prefixed by area. Assign it once and never move it. An item that
splits keeps its ID and gains suffixes (`PFX-014a`, `PFX-014b`); an item that merges into another
is marked `deprecated` with a pointer, and stays in the table.

**`Type`** — from a fixed, small vocabulary declared in the charter (L-14). Whatever your
categories are, define them once, here or there, and render everywhere else from that definition.
Types invented per-row are how a catalog becomes a list.

**`Responsibility`** — one clause, stating what the item is *for*. This column does the real work
and it is the one that gets filled in lazily. Two failures show up here immediately, and nowhere
else: an item whose responsibility cannot be stated in one clause is probably two items, and two
items with the same responsibility means one of them is unowned, unmaintained, or both — and
nobody knows which.

**`Depends-on / Used-by`** — both directions. Recording only dependencies gives you a graph you
can walk one way, and every question you actually want to ask — *what breaks if I change this*,
*what is safe to retire* — is the other way.

**`Status`** — including `unknown`, which is mandatory and load-bearing. An item nobody can
account for is a finding, not a gap in the table. Marking it `unknown` puts it in the coverage
summary where it will be looked at; leaving the cell blank puts it nowhere.

**`Notes`** — where an item's oddity goes. If the note is longer than the row, the item needs its
own record and this cell becomes a pointer.

---

## Completeness guarantee

This is what separates a catalog from an inventory, and it is the entire reason to build one.

> **Every item within the declared scope is assigned to exactly one row. Not zero — an item with
> no row is invisible to every pass that uses this catalog as its map. Not two — an item with two
> rows has two owners, which in practice means none, and the failure surfaces only when both
> assume the other handled it.**
>
> **The orphan list must come back empty.** Not "mostly empty," not "empty except for the
> obvious ones." Empty. A non-empty orphan list is the catalog's single output signal, and
> tolerating entries in it converts the guarantee into a gesture.

**Declared scope:** `<the boundary, stated precisely enough that "inside or outside?" is
answerable without a judgement call. Everything inside gets a row. Everything outside is listed in
the exclusions below — with a reason, because an unexplained exclusion is re-litigated by whoever
did not hear the argument.>`

**Exclusions:**

- `<what is out of scope>` — `<why>` (`<D-n>`)

### Orphan list

`<Items found within the declared scope that have no row. This list is worked to empty and then
kept, empty, with a date — because "empty" and "never run" look identical in a document, and only
one of them is reassuring.>`

**Last swept:** `<live UTC>` · **Orphans:** `<n>` — `<must be 0>`

| Item | Found where | Why it had no row | Disposition |
|---|---|---|---|
| `<…>` | `<…>` | `<…>` | `<assigned PFX-<n> / declared out of scope, D-<n>>` |

### Duplicate-assignment list

`<Items assigned to more than one row. Same rule: worked to empty, then kept empty with a date.>`

**Last swept:** `<live UTC>` · **Duplicates:** `<n>` — `<must be 0>`

---

## Coverage summary

Recomputed at each sweep and kept as a block, so that coverage is a number someone can dispute
rather than an impression.

```
CATALOG COVERAGE — <live UTC>

  Items in declared scope        <n>
  Rows                           <n>
  Assigned                       <n> / <n>   (<pct>%)     MUST be 100%
  Orphans                        <n>                      MUST be 0
  Duplicate assignments          <n>                      MUST be 0

  By status
    active                       <n>
    partial                      <n>
    planned                      <n>
    deprecated                   <n>
    unknown                      <n>                      <-- the number that matters

  Edges (see below)              <n> recorded / <n> reviewed
  Areas with no owner            <n>                      MUST be 0
```

**`unknown` is the number to read first.** A catalog reporting 100% assignment with a healthy
`unknown` count is telling you something honest and useful: the map is complete, and some of the
territory is unexplored. A catalog with `unknown: 0` on its first sweep is not complete — it is
optimistic, and it has quietly rounded every uncertain item to the nearest comfortable status.
Report thin coverage as thin: a cell with two items appears in the table with a two next to it,
never omitted, because omission reads as *no signal* while a visible small number reads as *not
yet enough*.

---

## Edges

> **In the source project, the edges ledger was called "the most important artifact in the
> catalog."**

The rows tell you what exists. **The edges tell you where it breaks.** Every real failure of the
merge-cleanly-but-wrong class lives at a seam between two areas that were each internally correct
— which means it lives in a place that no row-level review will ever look at, because every row it
touches is fine.

An edge is any place where two areas meet and neither wholly owns the meeting: a handoff, a shared
value, a format agreed between two parties, a boundary where one side's assumption is the other
side's obligation, a translation between two vocabularies.

| Edge ID | Between | What crosses | Contract | Owner | Verified at | Status |
|---|---|---|---|---|---|---|
| `<E-001>` | `<PFX-003>` ↔ `<PFX-017>` | `<what actually passes across — data, control, authority, an assumption>` | `<what each side promises the other, stated so it could be violated>` | `<who owns the seam itself — not either side>` | `<where the contract is actually checked, or NOWHERE>` | `<…>` |

### The four columns that do the work

**`What crosses`** — be specific, and include the things that are not obviously "things." An
*assumption* crossing an edge is the most dangerous cargo there is, because neither side has
written it down and both are relying on it.

**`Contract`** — stated so it could be violated. "They agree on the format" is not a contract;
"`<A>` guarantees `<X>` is never empty and `<B>` may assume it" is. If the contract cannot be
stated in a way that could be broken, there is no contract at the seam — only a coincidence that
has held so far.

**`Owner`** — the seam has its own owner, and it is not "both sides." An edge owned by both sides
is owned by neither: each will assume the other is checking, and the assumption is symmetrical,
which is why it survives so long.

**`Verified at`** — where the contract is actually checked, or the honest word **NOWHERE**. An
edge with `NOWHERE` in this column is not a gap in the catalog; it is a finding, and it belongs in
the triage board. Most edges start life as `NOWHERE`, and writing it down is the whole exercise —
the contract that everyone believes is enforced somewhere, and is not, is the one that fails.

### Unowned areas

`<Rows whose Responsibility is real and whose owner is nobody. Must be empty. An unowned area is
not a staffing problem — it is an area where every observation will be nobody's to act on, which
means the observations stop being recorded.>`

**Count:** `<n>` — `<must be 0>`

---

## Sweep ritual

The catalog is only trustworthy at the moment it was last swept, and a swept date is what
distinguishes a live map from a historical one.

1. Enumerate everything in the declared scope, **from the subject itself** — not from this file.
   Cataloguing from the catalog reproduces last quarter's understanding with a fresh date on it,
   which is worse than not sweeping, because it launders a stale document into a current one.
2. Diff against the rows. Anything present and unrowed goes to the orphan list; anything rowed and
   absent gets `deprecated`, **not deleted**.
3. Work the orphan list to empty. Every entry ends as an assignment or a scoped exclusion with a
   decision ID.
4. Re-walk the edges. Ask of each: *is this contract still what both sides believe?* Edges rot
   quietly, because nothing on either side changes when the shared assumption does.
5. Recompute the coverage block. Stamp it with a live UTC reading.
6. Record the sweep in the ledger — including what moved, what was retired, and why. An
   unrecorded reorganization is indistinguishable from data loss six months later.

**Last full sweep:** `<live UTC>` · **By:** `<who>` · **Method:** `<how enumeration was done, and
what that method could not have seen>`

---

## Worked example

*Fragment from the catalog of a small volunteer monitoring study. Domain is illustrative only.*

| ID | Name | Type | Responsibility | Depends-on / Used-by | Status | Notes |
|---|---|---|---|---|---|---|
| `SITE-002` | Lower ford | site | The downstream sampling point; carries the study's only continuous series | **dep:** `INST-004`, `PROC-001` · **used-by:** `DATA-001`, `FIND-003` | active | Access is via private land; permission renews annually |
| `INST-004` | Turbidity tube | instrument | Turns a water sample into a number a volunteer can read without training | **used-by:** `SITE-002`, `SITE-005` | active | Reads in 5-unit steps; cannot resolve changes smaller than that, and three findings currently rest on differences of 5 |
| `PROC-001` | Sampling protocol | procedure | Fixes the conditions so readings are comparable across dates and people | **dep:** `D-007` · **used-by:** all sites | active | Amended 2026-06-14; readings before that date carry a known weekday artifact |
| `SITE-007` | Upstream control | site | *(was: the paired control for catchment-wide change)* | **used-by:** `FIND-001` (pre-2026-05-28 only) | `deprecated` | Access withdrawn; see `D-008`. **Row retained** — `FIND-001` still cites it and always will |
| `DATA-003` | Volunteer field sheets | record | The verbatim capture, before anything is transcribed | **used-by:** `DATA-001` | `unknown` | Nobody can currently say where the 2025 sheets are. Not a blank cell — a finding |

| Edge ID | Between | What crosses | Contract | Owner | Verified at | Status |
|---|---|---|---|---|---|---|
| `E-002` | `DATA-003` ↔ `DATA-001` | Transcription from paper field sheets into the spreadsheet | Every sheet is transcribed exactly once, and a sheet with an unreadable field becomes a blank cell — **never an inferred value** | `<name>` | **NOWHERE** | open — raised as a triage item |
| `E-005` | `INST-004` ↔ `PROC-001` | The assumption that all volunteers read the tube at the same fill height | The protocol specifies the height; the instrument has no mark at it | `<name>` | **NOWHERE** | open — an unwritten assumption crossing a seam, which is exactly the cargo this ledger exists to catch |

`E-005` is the row worth studying. Both sides are individually correct: the protocol says what to
do, and the instrument does what it does. Nothing is broken in either. The failure lives entirely
in the space between them, it has been silently degrading every reading in the series, and no
review of either item alone would ever have surfaced it.
