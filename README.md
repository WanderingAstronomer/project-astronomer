# Project Astronomer

**A framework for doing rigorous work on subjects you cannot run experiments on.**

Astronomer is the extracted, generalized methodology behind four working projects — a
transcription platform, a civic mapping service, a retrieval-architecture proof of concept,
and a personal research study. None of them shared a domain. All four independently
converged on the same operating discipline. This repository is that discipline, named,
written down, and made installable.

---

## What it is

Astronomer is three things, in this order:

1. **A doctrine** — a small set of laws about evidence, sequence, and honesty that hold
   regardless of what you are working on. This is the part that matters. ([`doctrine/`](doctrine/))
2. **An artifact set** — the specific document shapes those laws imply: a decision ledger,
   an observation log, a triage board, a frozen record, a work brief. Proven templates, not
   suggestions. ([`artifacts/`](artifacts/))
3. **An installable layer** — a `CLAUDE.md` and a set of skills that teach an AI collaborator
   the doctrine, so the rules are enforced in the working session rather than remembered
   in a document nobody rereads. ([`install/`](install/))

It is deliberately **domain-agnostic**. The first project built on it is a physical-health
project, which is the real test: if the framework only works on software, it was never a
framework — it was a habit with good PR.

## Why "Astronomer"

The name is load-bearing, not decorative.

An astronomer studies a subject they cannot touch. They cannot run a controlled trial on a
star. They cannot isolate a variable, hold the rest constant, and re-run the universe. Every
conclusion they reach is an inference drawn from uncontrolled observation, through an
imperfect instrument, about an object that was already in the past by the time the light
arrived. And yet astronomy is not soft. It is one of the most quantitatively rigorous
sciences we have.

It got there by building a discipline specifically for that predicament:

| Astronomy | Astronomer the framework |
|---|---|
| You observe; you cannot experiment | The core epistemic problem this framework solves |
| **Seeing** — the atmospheric conditions limiting a given night's resolution | Every observation records the conditions that limit it |
| The **observation log** — timestamped, raw, never rewritten | The intake ledger: verbatim first, interpretation second, append-only |
| **Catalogs** (Messier, NGC) — exhaustive, permanently numbered | The everything-in-scope catalog; IDs are permanent, retired but never reused |
| **Ephemeris** — the prediction published *before* the night | Pre-registered acceptance criteria, written before you look |
| **Magnitude** — a calibrated, shared scale | Fixed severity and confidence vocabularies |
| **Light-travel time** — you are always looking at the past | Lagging indicators: today's reading reports months of input |
| **Instrument error** — known, published, subtracted | Measure your own baseline; trust no number quoted to you |
| **Unresolved** — a real, respectable category | Name what you cannot resolve instead of inventing it |

This is exactly the predicament of every project in the lineage. You cannot A/B test your own
body against a control body. You cannot run a production system twice under identical
conditions. You cannot interview a corpus. In all of them, the work is *rigorous inference
from uncontrolled observation* — and that is the thing astronomy is best at in the world.

So the framework is not "software methodology applied to health." It is the methodology that
was always underneath, which happened to be discovered while writing software.

## The shape of the work

Every Astronomer project runs the same loop. The loop is the framework.

```
OBSERVE   Record what happened. Verbatim, timestamped, read-only.
          Change nothing. Not even the obvious things.
              ↓
TRIAGE    Bucket by what you KNOW, not by how much it hurts.
          Group by shared root cause. Co-occurrence is not shared cause.
              ↓
RESOLVE   Prove the cause. Cite the evidence. Refute your own first guess.
          Do not act from the hypothesis.
              ↓
ACT       Smallest reversible change that addresses the proven cause.
          One variable at a time, or the result is unattributable.
              ↓
RECORD    Freeze what happened. Update what is true.
          Keep the wrong calls visible.
```

The most commonly skipped step is the boundary between OBSERVE and TRIAGE. It is also the
one that costs the most when skipped, because a fix applied during observation destroys the
evidence for every observation after it.

## Start here

| If you want to… | Read |
|---|---|
| Understand the rules | [`doctrine/01-laws.md`](doctrine/01-laws.md) — start here, it is short |
| Understand *why* those rules | [`doctrine/02-epistemics.md`](doctrine/02-epistemics.md) |
| Know how heavy this is going to be | [`tiers/README.md`](tiers/README.md) |
| Start a project on it | [`install/README.md`](install/README.md) |
| See the receipts | [`provenance/lineage.md`](provenance/lineage.md) |
| Know what governs this repo itself | [`CHARTER.md`](CHARTER.md) |

## Tiers

Astronomer scales down. The same laws hold at every tier; only the required artifacts change.
A personal journal should not need a coverage map and seven fenced work lanes — and a
framework that demands one is a framework that gets abandoned in week three.

- **Lite** — 3 artifacts. A charter, a decision ledger, an observation log. Solo, low stakes,
  reversible.
- **Standard** — adds triage, findings, and frozen records. Anything with real consequences
  or more than one contributor.
- **Full** — adds the catalog, fenced parallel lanes, briefs and reports, and mechanical gates.
  Multi-session, multi-month, expensive to get wrong.

See [`tiers/README.md`](tiers/README.md). Choosing a tier is itself a decision, and it goes
in the ledger.

## This repo runs on itself

Astronomer has its own [`CHARTER.md`](CHARTER.md) and its own [`DECISIONS.md`](DECISIONS.md),
maintained under its own rules. That is not a cute flourish — it is the only honest way to
find out whether the framework survives contact with a real project. Where it has been
inconvenient, that is recorded rather than smoothed over.

## Status

**Seeded 2026-07-20.** The doctrine, artifact set, tier definitions, and install layer are
written. No project has been built on it yet. The first will be a physical-health project in a
separate repository — kept separate deliberately, so the framework has to generalize rather
than quietly grow health-shaped assumptions.

Until a real project has run a full loop on it, every claim in here is a **hypothesis about
what worked**, reconstructed from four projects that were not trying to produce a framework at
the time. Treated under this framework's own rules, that makes this corpus `PROVISIONAL`.
