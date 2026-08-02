---
record_class: living
precedence: 6
confidence: CONFIRMED
owns:
  - retrieval-provider-setup
verified_by: measured end-to-end on one machine 2026-08-01/02; every figure re-derived, and the one step that was NOT reached is marked
last_verified: 2026-08-02
---

# Standing up a corpus-retrieval provider

**This is a reference implementation, not doctrine.** It names a vendor, a binary, and a port, none
of which the framework requires. CHARTER invariant 1 keeps doctrine free of tooling; the *role* is
`Corpus retrieval` and lives in [`../doctrine/08-instruments.md`](../doctrine/08-instruments.md)
(K-7), the *procedure* for using it is
[`../rituals/corpus-retrieval.md`](../rituals/corpus-retrieval.md), and this file is one worked
example of filling the role. Any provider that ranks, matches and lists will do. Read it for the
**shape and the failure modes**, which generalize; substitute your own provider freely.

**Why it exists.** The first two projects to fill this role both got it wrong, in different ways,
and neither failure was visible from inside a session. One indexed a corpus that was 52.5% vendor
documentation and watched its own architecture documents rank below vendor navigation links. The
other put its corpus somewhere the indexer cannot see and got a search engine over a quarter of its
files. A third failure — mine — took a component's error message at face value for four hours.
None of that is discoverable by reading a vendor's README.

---

## 0. Before anything: where the corpus lives

**Not under a dotted path.** Measured 2026-08-02 on a three-file fixture, two files under
`.claude/`, one under `notes/`: the indexer reported `notes=1`. It skips dot-directories, and so do
`rg` without `--hidden` and Python's `glob(recursive=True)`. Only `os.walk` and `find` see through.

That is **four of six instruments blind**, and the one that matters most is the retrieval provider
itself — so a project that puts its governance corpus in `.claude/` and then stands up search gets
an index over everything *except* its governance corpus. Worse than no index, because an empty
result from a real search engine reads as an answer.

`docs/` is the known-good shape. Any non-hidden directory works. See `AST-D-052`.

---

## 1. The architecture, which is two processes and not one

This is the part no documentation states plainly and the part that cost the most time:

| Component | Does | Fails as |
|---|---|---|
| **MCP server** (`obsidian-mcp`) | serves the vault: BM25 full-text, regex, frontmatter/tag queries, wikilink graph, note read/write | a tool error, immediately visible |
| **Semantic daemon** (`obsidian-semanticd`) | embeddings and semantic search **only** | an error *relayed through* the MCP server, which makes it look like an MCP fault |

The MCP server **delegates** semantic queries to the daemon over a named pipe. Everything else it
does itself. So:

- **Full-text, regex, structural navigation work with the MCP server alone.** That is rungs 2 and 3
  of the ladder in `08-instruments.md`, and it is most of the value.
- **Semantic search — the top rung — requires the daemon, separately, and can be missing while
  everything else is healthy.**

A `manifest.json` in the daemon's home directory **pins the daemon's binary path and SHA-256**. The
MCP server bootstraps whatever that manifest names. **A more capable binary sitting elsewhere on the
same machine will not be used**, and nothing reports this.

---

## 2. Bring up the search server

```bash
obsidian-mcp serve --http --port 37842 /path/to/your/corpus
```

Four things that are not obvious and were each measured:

- **The vault root IS the directory you pass.** A file at `docs/spec/00-spine.md` is
  `spec/00-spine.md` to every tool. Sessions strip and re-add that prefix in both directions; check
  the path you were handed before concluding a file is missing.
- **`serve` daemonizes but keeps stdout attached.** Calling it directly blocks your shell forever —
  measured, a shell invocation hung until killed at two minutes while the server came up fine.
  Detach it (`Start-Process`, `nohup`, `&` with output redirected).
- **The `restart` subcommand's graceful stop can fail** and then gives up *without* starting a new
  server: *"This process can only be terminated forcefully"*, then *"port still in use"*. Stop by
  force first, then `serve`. Doing it in that order is what makes a launch script idempotent.
- **One server per corpus, one port each.** A second corpus needs a second port and its own client
  config.

### Exclusions — the K-7 control

```bash
OBSIDIAN_EXCLUDE_PATHS='research/providers/**' obsidian-mcp serve --http --port 37842 /path/to/corpus
```

Globs are **vault-relative** (no leading `docs/`). This is the mechanism that keeps an imported
corpus out of the default query surface while leaving it reachable by explicit path — segregation,
not deletion. Measured on one corpus: indexed notes 752 → 358, foreign share of search 52.5% → 0%,
and a query that had returned 364,155 characters and been abandoned returned 22 ranked documents.
`note_read` into the excluded tree still works.

**Read `../rituals/corpus-intake.md` step 3 before importing anything**, and add the new path to
this variable in the same commit.

### Wire the client

```json
{ "mcpServers": { "obsidian": { "type": "http", "url": "http://127.0.0.1:37842/mcp" } } }
```

Project-scoped, three lines. **The binary is installed once per machine; reaching it is per
project.** A session that searches a connector registry and finds nothing has measured the wrong
thing — this is a local process, not a hosted connector. That mistake was made once, and it
produced a report saying the capability was unavailable when it was one config file away.

---

## 3. Semantic search — the ladder of errors, which is the real documentation

Semantic is the one rung that needs the second process **and** an embedding source. Its errors are
precise and each names a different layer. **Read the error rather than concluding the feature is
absent** — that is the mistake this section exists to prevent.

| Error text | Means | Do |
|---|---|---|
| `daemon binary compiled without embeddings feature` | the daemon the manifest points at was built **without** embeddings | you may have a second, larger binary elsewhere. Compare sizes, not versions |
| `vault not ready; call ensure_vault first` | daemon is capable; the vault has no embedding index yet | proceed — this is progress, not a fault |
| `local embedding backend not compiled` | this build cannot embed **locally**; the API path remains | supply an API endpoint, or obtain a build with the local feature |
| `API key required: set OBSIDIAN_EMBEDDING_API_KEY or OPENAI_API_KEY` | everything is wired; it needs a **credential** | **operator's call — see below** |

**Two same-version binaries can differ in features, and the version string will not tell you.**
Measured: two `obsidian-semanticd 2.3.2` binaries on one machine, 9.9 MB and 12.8 MB. The smaller
lacked embeddings; the manifest pinned the smaller; the larger sat unused in a package directory.
**Size and behaviour are the tell. The version is not.**

The embedding source is either a local model (`OBSIDIAN_EMBEDDING_PROVIDER=local`, needs a build
with that feature and a model cache) or any OpenAI-compatible endpoint
(`OBSIDIAN_EMBEDDING_API_BASE`, which does **not** have to be OpenAI — a local inference server on
`localhost` works and keeps the corpus off the network).

> **Where this document stops, and it stops honestly.** The credential is **custody** — non-delegable
> under [`../doctrine/06-delegation.md`](../doctrine/06-delegation.md). This procedure was measured
> up to and including the `API key required` state and **no further**: nobody supplied a key, so
> **semantic search has not been observed working by the author of this file.** Steps 0–2 are
> `CONFIRMED` end-to-end. Step 3 is `CONFIRMED` as a diagnosis and `UNVERIFIED` as a completion.
> A future session that supplies a credential and sees it work should promote that here and say so.

---

## 4. Verify — and do not accept a process starting as proof

Three checks, in order of what they can actually catch:

1. **The index size, from the server's own log.** It prints `index built notes=N` on startup.
   Compare `N` to a count you take yourself with `find` or `os.walk` — **not** with `rg` or
   `glob`, which share the blind spot you are testing for. A large gap means exclusions are wider
   than you think, or your corpus is somewhere the indexer cannot see.
2. **`vault_info`.** `excluded_notes` should be non-zero if you set exclusions, and the pattern list
   should echo back what you passed. A silently-ignored glob shows up here and nowhere else.
3. **A query you know the answer to.** Search for something the project certainly wrote. If your own
   material does not come back first, you have a K-7 problem regardless of what the counts say.

**Exercise the off switch too.** If your launcher has a flag to disable exclusions, run it once and
confirm the count changes. A documented flag nobody has run is a hypothesis about a flag.

---

## 5. What this provider cannot do, measured

- **`search_metadata` returns full note bodies, not paths.** A corpus-wide frontmatter query is
  therefore unusable: measured at **882,655 characters** for one field on a 362-note index. The one
  query that could navigate a corpus *by precedence* is the one you cannot run. Use `grep` over
  frontmatter instead.
- **Dot-directories are invisible** (§0).
- **Exclusion cannot fix volume that is genuinely yours.** On one corpus a regex search fell 54%
  after excluding a vendor tree and was *still* unusable, because the residual was the project's own
  notes. A foreign-share problem and a large-own-corpus problem present identically — both are "the
  search returned more than anyone will read" — and only the first is fixable this way.

---

## 6. Make it durable

There is no autostart, and that is the right default — nothing should launch a background service on
an operator's machine unasked. So the bring-up must be **one command, in the repository, that a
session can run without deciding anything**. A worked example is the launch script in the first
consuming project; the shape that matters is: force-stop what is on the port, start detached, then
**read the index count back out of the log and print it**. Do not report success from the fact that
a process started (L-16).

Re-run it after a reboot. Record the provider, the exclusions and the foreign share in the
capability inventory ([`../artifacts/capability-inventory.template.md`](../artifacts/capability-inventory.template.md)),
and re-date it when any of them move (K-4).
