---
record_class: living
precedence: 6
confidence: PROVISIONAL
owns:
  - ast-orchestration
verified_by: founded from install/FOUNDING.md (D-067)
last_verified: 2026-10-10
---

# How project-astronomer is organised

Workspace: `C:\Users\drew\Documents\DevSlop\project-astronomer`. Size: **Solo** (D-067). Tier: undeclared
(D-067). Slug: `AST`. Rules come from `doctrine/06-delegation.md`. This file may narrow them and never
widen them.

```
Operator → Maestro (project-astronomer) ◀─ exchanges ─▶ other workspaces' Maestros
```

## Existing records (adoption, FOUNDING Part 4 §8)

| What | Where |
|---|---|
| Ledger | `DECISIONS.md` |
| Observation log | `OBSERVATIONS.md` |
| Charter | `CHARTER.md` |
| Exchange log | `.maestro/EXCHANGES.md` |
| Page | The Maestro System, https://claude.ai/artifact/BRzL6v3KMCukq263B1Vi2g (source `install/maestro/maestro-system-page.html`) |

## Edges this workspace removes from the standard table

None.

## Delegation: what the Maestro may rule on without the operator

Small agreed wording or behaviour questions, and fixes that keep the corpus gate green, logged as
"Maestro's call". These are always the operator's:

- laws, the charter, and new artifact templates (`doctrine/00-precedence.md`);
- money, accounts and anything public;
- writes to the operator's data or anyone else's;
- settings and hooks;
- anything a safety check stopped;
- anything the operator ruled on personally.

## Data boundary

Answers may quote the corpus. Nothing that passes through from another workspace leaves this one, and
no source client is named beyond what the corpus already publishes.
