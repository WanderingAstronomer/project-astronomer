---
record_class: living
precedence: 6
confidence: UNVERIFIED
owns:
  - maestro-routing-gate
verified_by: install/maestro/test_gate.py + verify_gate_mutations.py, run 2026-10-10T06:25Z
last_verified: 2026-10-10
---

# The Maestro routing gate

`gate.py` is a Claude Code `PreToolUse` hook. It holds the workspace boundary of the Maestro system
mechanically, so that the routing rules are enforced by the harness rather than by instruction alone.
It reads the group registry, works out which group the sending session belongs to and which session it
is addressing, and blocks the sends the routing rules forbid.

It is **not installed**. Nothing in this directory touches any `settings.json`. Installing it is the
operator's call, using the snippet below.

Python 3 standard library only. Works with Windows backslash paths and forward slashes alike.

## What it governs

Only two tools:

- `SendMessage`: the target is `tool_input.to`, a name that may carry a ` [ref]` suffix
  (`Conductor [4711e6]`), or `main`, or a subagent id (`a8e39355c84eae9b7`), or a teammate name.
- `mcp__ccd_session_mgmt__send_message`: the target is `tool_input.session_id`, a `local_...` id,
  a short name, or `parent`.

Every other tool exits 0 silently. To block, the gate prints one reason starting `MAESTRO GATE:` to
stderr and exits 2, which Claude Code shows to the model. To allow, it exits 0 with no output.

**It fails open.** Any unexpected error (stdin that is not JSON, a payload of the wrong shape, a bug)
allows the send and appends one line to `%USERPROFILE%\.maestro\gate-errors.log`. A gate that crashes
closed would wedge every session on the machine. The cost is that a defect which raises looks like an
allow, so the tests treat an allow as valid only when nothing was logged.

## The registry

Directory: `MAESTRO_REGISTRY` if set, else `~/.maestro/registry` (`%USERPROFILE%\.maestro\registry`).
One `<slug>.json` per group. Files not ending in `.json` are ignored. Unknown fields are ignored.

```json
{
  "group": "Vociferous Next",
  "slug": "VOC",
  "size": "Orchestra",
  "workspace": "C:\\Users\\drew\\Documents\\DevSlop\\vociferous",
  "maestro":   {"title": "Maestro (Vociferous Next)",   "session": "local_3719027b-...", "hook_session": "8c6cf821-..."},
  "conductor": {"title": "Conductor (Vociferous Next)", "session": "local_f7154940-...", "hook_session": null},
  "roster": [ {"title": "Landing & Review", "session": "local_a44ff87d-...", "role": "lander"} ],
  "permits": [ {"id": "P-1", "to": "Conductor (Health)", "topic": "...", "operator_words": "...",
                "granted": "2026-10-10T06:00Z", "ends": "when X-4 closes"} ],
  "updated": "..."
}
```

- `size` is Solo, Chamber or Orchestra. `conductor` is `null` at Solo.
- Roster roles are section, outlier, lander or oneway. The gate treats them all as members.
- `session` is the desktop's `local_...` id. `hook_session` is the `session_id` Claude Code puts in
  the hook payload, which is how the gate knows the Maestro or Conductor is the one sending.
- A permit is live unless it carries `"ended": true` (any truthy value). The free-text `ends` field
  is for people; the gate does not read it. To close a permit, set `ended`.

## How it identifies the sender

- **Group.** The registered workspace that contains the payload's `cwd`. Comparison is
  case-insensitive, slash-normalised, trailing-separator-insensitive, and on path-component
  boundaries, so `C:\a\voc` does not contain `C:\a\vocab`. With nested workspaces the deepest wins.
  No match means the sender is **ungoverned**. The match is pure string work; symlinks and junctions
  are not resolved.
- **Role.** `maestro` if the hook `session_id` equals `maestro.hook_session`, or equals
  `maestro.session` with `local_` stripped (case-insensitive, `local_` optional on either side).
  The same test against the conductor gives `conductor`. Anything else is `member`.

## How it resolves the target

1. Strip a trailing ` [xxxx]` ref suffix.
2. `main` and subagent ids (`^a[0-9a-f]{15,}$`) are in-session plumbing: always allowed.
3. Match against every group's session ids (`local_...`, case-insensitive), then against every
   maestro, conductor and roster title (case-insensitive, trimmed).
4. A name shaped `Maestro (<Group>)` or `Conductor (<Group>)` whose group is registered resolves to
   that group's Maestro or Conductor even if the stored title differs.
5. A name that resolves to nothing is not governed and is allowed.
6. A name that resolves to several sessions (the same title in two groups) is checked against each.
   If any would be blocked, the send is blocked and the reason says to address the session by its
   `local_` id.

## The edge rules

Sender group S (or none), sender role, target group T, target role.

| Sender | Target | Verdict |
|---|---|---|
| ungoverned | any Maestro | allowed |
| ungoverned | a Conductor or member of T | blocked: outside sessions may contact only Maestro (T) |
| inside S | anyone in S | allowed, except the next row |
| member of S | Maestro (S), when S has a Conductor | blocked: send it to Conductor (S) |
| Maestro (S) | Maestro (T) | allowed |
| Maestro (S) | a Conductor or member of T | allowed only with a live permit in S's own registry file whose `to` is the target's title or session id |
| Conductor or member of S | anyone in T | blocked: ask Maestro (S) to raise an exchange |
| Conductor or member of S | a title shaped `Maestro (X)` or `Conductor (X)` for any X other than S, **registered or not** | blocked, same reason. An unregistered workspace is still another workspace (added 2026-10-10, after a dry run against the live registry let an AST member reach the then-unregistered `Maestro (Vociferous Next)`) |

When a member of S is blocked from reaching another group's Maestro, the reason adds the self-heal
hint: *if you are Maestro (S), set `maestro.hook_session` in the S file to this session id*. That is
the path for a Maestro whose hook session id changed after a restart and which the gate therefore no
longer recognises.

## Malformed registry files

A file that does not parse, or lacks `group`, `workspace` or `maestro`, is malformed. The rule chosen:

- If its workspace can be determined (from the parsed object, or failing that by pulling the
  `"workspace": "..."` string out of the unparsed text), every send from a sender whose `cwd` is
  inside that workspace is blocked, and the reason names the malformed file. This applies even when a
  deeper, well-formed workspace also contains the sender: the broken file could be the one that
  governs it.
- Sends to `main` and to subagent ids are still allowed, because the gate never governs them.
- If the workspace cannot be determined, the file is skipped silently. Unrelated traffic is not
  blocked, and the well-formed files are still enforced.

The trade: a torn write by a Maestro freezes its own group's messaging until the file is fixed, which
is noticeable and local. It never freezes the whole machine.

## Install

Add this to the user settings, `~/.claude/settings.json`, merging with any `hooks` already there:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "SendMessage|mcp__ccd_session_mgmt__send_message",
        "hooks": [
          {
            "type": "command",
            "command": "python \"C:/Users/drew/Documents/DevSlop/project-astronomer/install/maestro/gate.py\""
          }
        ]
      }
    ]
  }
}
```

Then fill in `hook_session` for each Maestro and Conductor: the value is the `session_id` field of
the hook payload, which differs from the desktop's `local_...` id. Until it is filled in, the gate
can still recognise a session whose hook id equals its `local_` id with the prefix removed; otherwise
it treats the session as a member.

## Verifying it

```
python install/maestro/test_gate.py
python install/maestro/verify_gate_mutations.py
```

`test_gate.py` builds fixture registries in temp directories and runs `gate.py` as a subprocess,
exactly as Claude Code would. Set `MAESTRO_GATE_PATH` to test a different copy of the gate.

`verify_gate_mutations.py` seeds one defect at a time into a copy of the gate (cross-group check
disabled, prefix boundary dropped, permit `ended` ignored, ungoverned sender allowed everywhere, and
more) and requires the suite to fail against every one. It also fails if the unmutated gate does not
pass, or if a mutation's target string is not found exactly once in `gate.py`, so an edit that moves
the code cannot quietly turn a mutant into a no-op. After any edit to `gate.py`, run both.

## What it does not catch

- **Everything in the registry is forgeable.** Any session that can write files can write itself a
  permit, set its own id as `maestro.hook_session`, or move a workspace. The gate enforces the
  registry; it does not authenticate it. The rule that only a group's Maestro writes its file is held
  by instruction, not by this gate.
- **Roster staleness lets unlisted titles through.** A session missing from every roster resolves to
  nothing and is allowed, unless its name has the `Maestro (<Group>)` or `Conductor (<Group>)` shape.
  A renamed session is ungoverned as a target until its row is updated.
- **The hook session id may change after a restart.** A Maestro or Conductor whose id no longer
  matches is treated as a member, and is blocked from cross-group sends until its file is updated.
  The block reason carries the new id to make that fix one edit.
- **The sender is judged by `cwd`.** A session started outside its group's folder is ungoverned, and
  one that changes directory changes group.
- **It is untested whether the hook fires for these tools on every surface.** The suite proves the
  script's decisions given a payload. It does not prove that the desktop app, Remote Control or cloud
  sessions invoke `PreToolUse` hooks for `SendMessage` and `mcp__ccd_session_mgmt__send_message`.
  Observe a real block on each surface before relying on it there.
- **It fails open.** A crash allows the send. Check `gate-errors.log` now and then.
