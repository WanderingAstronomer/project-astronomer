# CAPABILITY INVENTORY — `<collaborator>` — `<YYYY-MM-DD>`

> **Doc class:** living. Rewritten whenever the environment changes, and **re-dated every time**. A
> capability inventory with no date is a claim about an environment that may no longer exist.

**Required at:** **Lite, conditional** — gated on a condition, not a tier: required whenever
something other than the operator is doing the observing. A solo human project does not need one; a
project where an AI collaborator reads the sources, runs the searches, and drafts the findings needs
it before the first window opens.

Every instrument in this framework declares what it cannot detect. The observation log requires it
per window; the frozen record requires it per run. **This artifact applies the same rule to the
collaborator itself**, which is otherwise the only instrument in the corpus exempt from it — and the
one doing most of the observing.

## Why this exists

`doctrine/06-delegation.md` says *"the operator is the instrument"* and that the instrument has
known error. There has never been a parallel statement for a collaborator, so its limits were
discovered per-task, by hitting them, usually mid-window.

The framework's ritual for stale measurements (`rituals/instrument-drift.md`) is entirely
retrospective — every entry point begins *after* you have relied on a bad number. This is the
forward half: state the limits **before** the work, where they cost a paragraph, rather than after,
where they cost the pass.

**This is single-authored and provisional (D-006).** No source project ran an AI collaborator with
standing access, so nothing here is attested by independent convergence. It is a structural argument
— the collaborator is an instrument, instruments declare their error — not a scar. Treat it as a
hypothesis about what is worth declaring, and amend it from what actually bites.

## What to state

### 1. Environment, as measured — not as assumed

`<Operating system, shell, working directory, what is installed and at what version.>`

**Measured now, by me, never quoted** (L-11) — including from this template. A capability list
copied from a previous session is exactly the stale number L-11 is about, and it will be wrong in
the direction of claiming too much.

### 2. What can be read, and in what formats

| Format | Can read | Notes |
|---|---|---|
| `<plain text / markdown>` | `<yes>` | |
| `<PDF, text layer>` | `<yes / no / with what tool>` | |
| `<PDF, scanned images>` | `<no without OCR — and is OCR available?>` | the silent-failure case; see the source manifest |
| `<office documents, spreadsheets>` | `<>` | hidden sheets, tracked changes, comments? |
| `<images, audio, video>` | `<>` | |
| `<archives, mailbox exports>` | `<>` | attachments extracted, or dropped? |

### 3. What can be executed, and where it may write

`<Whether the collaborator may write and run its own tooling; what it may read; which paths it may
write to; whether it may reach the network>` — this is the authorization required by B-5,
`doctrine/07-boundaries.md`, and it belongs here or in the data boundary, once, not in both.

### 4. Network reach

`<What outbound channels exist at all, before the question of what is permitted.>` Capability and
permission are different facts and both are needed: a channel that exists but is forbidden is a
boundary item; a channel that is permitted but does not exist is a plan that will fail quietly.

### 5. Known error — the load-bearing section

`<Where this collaborator is systematically wrong, in a direction you can name.>` Not modesty
boilerplate. A usable entry names the bias and its direction, so it can be subtracted:

> **Completeness questions are under-reported.** Asked "where does X appear," careful reading
> returns a list that looks finished and is not. Measured once on this corpus: four readers, told
> exactly what to look for, found seven of ten sites — a ~30% undercount, in the direction that
> feels complete. Use a mechanical search as the instrument and reading as the interpreter for any
> question of the form "everywhere" (`rituals/observation-pass.md`).

> **Its own tooling reads as authoritative.** Output from a script the collaborator wrote is
> `INFERENCE` until the script has been broken on purpose and seen to notice (B-6). First run of
> this project's own vocabulary gate reported fourteen defects; nine were artifacts of the gate.

### 6. Instrument debt — what cannot be measured here at all

`<Things this environment cannot determine, listed so they are owed rather than guessed.>` The
model is a source project that shipped with a written ledger of what was owed to real devices,
rather than letting a weaker verification stand in silently (L-12). An honest wall beats an
optimistic one (L-16).

## Forbidden

- Copying this file forward from a previous session without re-measuring. That is the stale-number
  failure L-11 exists for, committed against yourself.
- Writing "no known limitations" in section 5. That is not an inventory, it is an absence of one —
  and it is the single most likely sentence in this whole artifact to be false.
- Discovering a capability limit mid-window and continuing without recording it. It is an
  observation (L-7); log it, and amend this file when the window closes.
- Confusing capability with permission. What the collaborator *can* reach and what it *may* reach
  are different questions with different owners; permission lives in the data boundary.

## Lifecycle

Written before the first observation window, as part of `starting-a-project`. Rewritten and re-dated
whenever the environment changes — a new tool, a lost one, a different machine. Never frozen: a
stale capability inventory is a live risk, not a historical record. When a limit turns out to be
wrong, that correction goes in the decision ledger, because it means work done under the old
assumption may need re-checking.
