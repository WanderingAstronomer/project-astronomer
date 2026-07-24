# tools — the corpus self-check

> **Doc class:** living.

```bash
python tools/check-corpus.py            # run the gate
python tools/check-corpus.py --verbose  # also print every exemption it took
python tools/verify-gate.py             # break the corpus on purpose, confirm the gate fires
```

Exit `0` clean, `1` on any failure.

---

## Why this exists

**The gate's description is its incident report** (`rituals/recurring-defect.md`). This one has two
incidents, four days apart, and the second is what built it.

**First — `AMENDS D-015`.** The confidence vocabulary shipped with *three different memberships*:
four tokens in the claim-fields table, five in the ledger, six in the token table. This happened
within hours of writing L-14, the law that says a vocabulary has exactly one home. Two reviewers
found it independently, neither having seen the other's report. The amendment closed with a
prediction and a condition:

> `caveat (owned):` this was found by review, not by a mechanism. Under L-17 a third recurrence
> demands a gate rather than a third correction — a check that every vocabulary in the corpus has
> exactly one enumeration. **Not built.** `next:` build it if the drift recurs.

**Second — D-019.** `append-only` was promoted to a record class in its own right. **Ten sites went
on enumerating three classes for four days.** The worst of them was
`install/skills/astronomer-start/SKILL.md`, which did not merely omit the fourth class — it
instructed the reader *"do not invent a fourth."* A project following that skill would have filed
its ledger and its observation log under a class doctrine explicitly calls the wrong reading, on
day one, while believing it was following the framework.

That is the recurrence the amendment named. Per L-17, the response to a defect *class* is a
mechanism, not a third hand-fix — the source corpus's own record of hand-fixing this class is
*"every hand-fix drifted back."*

There is a second lesson in the numbers. The pass that found the D-019 drift was four independent
readers, told exactly what to look for, and it reported **seven** sites. Direct `grep` during the
repair found **three more, in files those readers had read** (`OBSERVATIONS.md`, `O-19` and
`O-20`). Careful reading under-reports on exhaustive-enumeration questions. That is not a criticism
of the readers; it is the reason this file is a script.

---

## What it checks

| Check | What must hold | What it caught |
|---|---|---|
| **vocabulary lists** | Every token set in `vocabularies.json` has a home containing all its members, and every tight enumeration of it anywhere carries the full membership | The D-019 drift, and two further sites during its own bring-up |
| **counted prose** | A sentence that counts a vocabulary — *"recognizes four classes"*, *"the seventeen laws"* — matches the registry | The sentence form is how the D-019 drift survived: `doctrine/05-the-record.md` said *"three classes"* directly above a table listing four |
| **install manifest** | The skill directories on disk match both lists that name them — `install/README.md` and `install/CLAUDE.md.template` | Adding a skill needs lockstep edits in three files; nothing else detects an omission, and a framework-side rename leaves installed projects routing to a dead name |
| **links** | Every relative markdown link resolves, `#anchor` included | Five broken `../../doctrine/…` links in the newest skill, resolving to a directory that has never existed |
| **template links** | A `*.template.md` link resolves from the **project root** it will be copied to, and never contains `../` | Templates were linking to two different base locations at once; both could not be right |

**The template-link convention**, since the gate now enforces it:

- References to **framework** files (`doctrine/`, `rituals/`, `tiers/`) are bare backticked paths,
  never markdown links. The framework path varies per install — `install/README.md` fills a
  `<doctrine path>` placeholder — so a link written in `artifacts/` cannot survive the copy.
- References to **project** files (`CHARTER.md`, `DECISIONS.md`, `OBSERVATIONS.md`) stay markdown
  links, root-relative, because those resolve where the template lands.
- A `../` in a template link is always wrong. After the copy it points outside the project, at
  whatever happens to be there.

The same rule already applied to the skills, for the same reason, and was the fix for the five
broken links in `astronomer-start`.

**A run is an enumeration only at three or more members.** Two members side by side is a
comparison — *"the Operator / Coordinator boundary"*, *"findings are frozen, append-only"* — and
treating those as lists produced almost entirely false positives on the first run. Every real drift
this gate was built for was 3-of-4, 4-of-6, or 5-of-6. Never 2. A check whose output is mostly
noise gets ignored, and then switched off.

---

## What it cannot catch

Stated here rather than discovered later. `--verbose` prints every exemption on every run, because
a gate that is silent about where it does not look reads as coverage it does not have.

- **A vocabulary nobody registered.** Adding a token set to the corpus without adding it to
  `vocabularies.json` is invisible. **This is the largest hole and there is no cheap fix for it.**
- **Prose that asserts a membership without counting it.** The counted-prose check catches
  *"three classes"*; it cannot catch *"living, frozen and disposable are the record classes"*
  written as a sentence rather than a list. Narrower than it was, not closed.
- **`effort` (`S`/`M`/`L`)** — wholly unchecked. Single-letter members cannot be told from ordinary
  prose by any pattern.
- **`verification_grade`** — unchecked. The corpus renders it two ways, as bold single words and as
  full phrases, and until one is canonical there is no pattern that does not produce false
  positives. Resolving this is a real cleanup, not a config change.
- **`blast_radius`** — two members, below the three-member threshold. Manual review item.
- **`non_delegable`, `id_prefix`, and `law`** — home membership and counted prose are checked;
  enumerations are not, for reasons recorded per-vocabulary in the registry.
- **Anything in an exempt file.** `DECISIONS.md`, `OBSERVATIONS.md`, and `provenance/lineage.md`
  are append-only or frozen, and they quote defective and historical text on purpose — an
  observation log that cannot quote what it saw is not a log. Each exemption names the file and the
  reason.

---

## Files

- **`check-corpus.py`** — the gate.
- **`vocabularies.json`** — the registry. L-14 applied to the framework's own vocabularies: every
  shared token set listed once, with its declared home, its exemptions, and a stated reason for
  each thing left unchecked.
- **`verify-gate.py`** — seeds one real defect per check, asserts the gate fails with the expected
  signature, and restores the file in a `finally` block. `04-verification.md` requires a check be
  observed *failing* before it is trusted: a gate that has only ever been seen passing may be
  passing because it is broken, which is L-16's defect class — reporting a success it has not
  achieved.

Run `verify-gate.py` after any change to the gate itself. A check you have modified and not
re-broken is a check you are trusting on faith.

---

## The rule for the guards

From `rituals/recurring-defect.md`, and it is not negotiable:

> **The guard is intentional — fix the cause, don't disable it.**

If this gate fails, the corpus is wrong. If the gate is wrong, fix the gate and re-run
`verify-gate.py` — do not add an exemption to make a failure go away. Every exemption in
`vocabularies.json` carries a reason, and a reason that amounts to *"this was inconvenient"* is how
the ratchet slips.

**This gate is not automated.** No hook, no CI. D-005 bars tooling that generates or validates
*projects*; a self-check on this repository is not that, but wiring it to run unattended moves in
that direction, and the decision to do so should be a ledger entry rather than a side effect.
