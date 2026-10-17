#!/usr/bin/env python3
"""
gate.py - the Maestro routing gate, a Claude Code PreToolUse hook.

It reads the hook payload on stdin and decides whether a session may send a message to
another session, using the group registry (one JSON file per sidebar group). Only two tools
are governed: SendMessage and mcp__ccd_session_mgmt__send_message. Everything else passes
untouched.

Exit 0 with no output = allow. Exit 2 with a reason on stderr = block.
An unexpected error allows the send and appends one line to ~/.maestro/gate-errors.log:
a broken gate must never wedge every session on the machine.

Python 3 standard library only. See README.md next to this file for the rules.
"""

import datetime
import json
import os
import posixpath
import re
import sys
import traceback

GOVERNED_TOOLS = ("SendMessage", "mcp__ccd_session_mgmt__send_message")

AGENT_ID_RE = re.compile(r"^a[0-9a-f]{15,}$")
REF_SUFFIX_RE = re.compile(r"\s*\[[^\[\]]*\]\s*$")
ROLE_TITLE_RE = re.compile(r"^(Maestro|Conductor) \((.+)\)$", re.IGNORECASE)
WORKSPACE_RE = re.compile(r'"workspace"\s*:\s*("(?:[^"\\]|\\.)*")')


# ------------------------------------------------------------------ normalisation

def norm_path(p):
    """Case-folded, forward-slash, no trailing separator. Pure string work: no realpath."""
    p = os.path.expanduser(str(p).strip()).replace("\\", "/")
    p = posixpath.normpath(p)
    if len(p) > 1:
        p = p.rstrip("/") or "/"
    return p.lower()


def path_contains(ws, cwd):
    """True when cwd is ws or lies under it, on a component boundary."""
    if not ws or not cwd:
        return False
    prefix = ws if ws.endswith("/") else ws + "/"
    return cwd == ws or cwd.startswith(prefix)


def norm_id(s):
    s = str(s).strip().lower()
    if s.startswith("local_"):
        s = s[len("local_"):]
    return s


def norm_title(s):
    return " ".join(str(s).split()).lower()


# ------------------------------------------------------------------ registry

def registry_dir():
    d = os.environ.get("MAESTRO_REGISTRY")
    return d if d else os.path.expanduser("~/.maestro/registry")


def _problem(data):
    if not isinstance(data, dict):
        return "not a JSON object"
    for field in ("group", "workspace"):
        if not isinstance(data.get(field), str) or not data.get(field).strip():
            return "missing '%s'" % field
    if not isinstance(data.get("maestro"), dict):
        return "missing 'maestro'"
    return None


def _workspace_of_malformed(data, text):
    if isinstance(data, dict) and isinstance(data.get("workspace"), str) \
            and data["workspace"].strip():
        return norm_path(data["workspace"])
    m = WORKSPACE_RE.search(text or "")
    if m:
        try:
            ws = json.loads(m.group(1))
        except ValueError:
            return None
        if isinstance(ws, str) and ws.strip():
            return norm_path(ws)
    return None


def _entry(group, role, raw, default_title):
    raw = raw if isinstance(raw, dict) else {}
    title = raw.get("title")
    if not isinstance(title, str) or not title.strip():
        title = default_title
    session = raw.get("session")
    hook = raw.get("hook_session")
    return {
        "group": group,
        "role": role,
        "title": title.strip() if isinstance(title, str) else "",
        "session": session if isinstance(session, str) and session.strip() else None,
        "hook_session": hook if isinstance(hook, str) and hook.strip() else None,
    }


def load_registry(directory):
    groups, malformed = [], []
    try:
        names = sorted(os.listdir(directory))
    except OSError:
        return groups, malformed
    for name in names:
        if not name.lower().endswith(".json"):
            continue
        path = os.path.join(directory, name)
        if not os.path.isfile(path):
            continue
        text, data = None, None
        try:
            with open(path, encoding="utf-8-sig") as fh:
                text = fh.read()
            data = json.loads(text)
        except (OSError, ValueError):
            data = None
        problem = _problem(data) if data is not None else "does not parse as JSON"
        if problem:
            malformed.append({"path": path, "problem": problem,
                              "workspace": _workspace_of_malformed(data, text)})
            continue

        g = {
            "name": data["group"].strip(),
            "slug": data.get("slug") if isinstance(data.get("slug"), str) else "",
            "file": path,
            "workspace": norm_path(data["workspace"]),
            "permits": [p for p in (data.get("permits") or []) if isinstance(p, dict)]
            if isinstance(data.get("permits"), list) else [],
        }
        g["maestro"] = _entry(g, "maestro", data["maestro"], "Maestro (%s)" % g["name"])
        conductor = data.get("conductor")
        g["conductor"] = _entry(g, "conductor", conductor, "Conductor (%s)" % g["name"]) \
            if isinstance(conductor, dict) else None
        members = []
        roster = data.get("roster") if isinstance(data.get("roster"), list) else []
        for item in roster:
            if not isinstance(item, dict):
                continue
            role = item.get("role") if isinstance(item.get("role"), str) else "section"
            e = _entry(g, role.strip().lower() or "section", item, "")
            if e["title"] or e["session"]:
                members.append(e)
        g["members"] = members
        groups.append(g)
    return groups, malformed


def all_entries(groups):
    for g in groups:
        yield g["maestro"]
        if g["conductor"] is not None:
            yield g["conductor"]
        for m in g["members"]:
            yield m


# ------------------------------------------------------------------ sender and target

def sender_group(groups, cwd):
    if not cwd:
        return None
    inside = [g for g in groups if path_contains(g["workspace"], cwd)]
    if not inside:
        return None
    return max(inside, key=lambda g: len(g["workspace"]))


def _is_session(entry, sid):
    if entry is None or not sid:
        return False
    want = norm_id(sid)
    for value in (entry.get("hook_session"), entry.get("session")):
        if value and norm_id(value) == want:
            return True
    return False


def sender_role(group, sid):
    if _is_session(group["maestro"], sid):
        return "maestro"
    if _is_session(group["conductor"], sid):
        return "conductor"
    return "member"


def resolve(name, groups):
    entries = list(all_entries(groups))
    want_id = norm_id(name)
    by_session = [e for e in entries if e["session"] and norm_id(e["session"]) == want_id]
    if by_session:
        return by_session
    want = norm_title(name)
    found = [e for e in entries if e["title"] and norm_title(e["title"]) == want]
    m = ROLE_TITLE_RE.match(name.strip())
    if m:
        role, gname = m.group(1).lower(), norm_title(m.group(2))
        for g in groups:
            if norm_title(g["name"]) != gname:
                continue
            e = g["maestro"] if role == "maestro" else g["conductor"]
            if e is not None and not any(e is f for f in found):
                found.append(e)
    return found


# ------------------------------------------------------------------ rules

def has_live_permit(s_group, target, requested):
    wanted = {norm_title(target["title"]), norm_title(requested)}
    ids = {norm_id(target["session"])} if target["session"] else set()
    for p in s_group["permits"]:
        to = p.get("to")
        if not isinstance(to, str) or not to.strip():
            continue
        if not p.get("ended") and (norm_title(to) in wanted or norm_id(to) in ids):
            return True
    return False


def evaluate(s_group, sr, sid, t, requested):
    """Return a block reason (without the MAESTRO GATE prefix) or None to allow."""
    tg, tr, tname = t["group"], t["role"], t["title"] or requested
    if s_group is None:
        if tr == "maestro":
            return None
        return ("%s belongs to group %s; outside sessions may contact only %s."
                % (tname, tg["name"], tg["maestro"]["title"]))

    same_group = s_group is tg
    if same_group:
        if sr == "member" and tr == "maestro" and tg["conductor"] is not None:
            # O-71: a Conductor whose hook_session is missing or stale is read as a member and
            # was silently cut off from its Maestro for a week. Name the field so it self-heals.
            return ("send this to %s; sections don't message the Maestro. If you are %s, "
                    "conductor.hook_session in %s is %s; set it to %s."
                    % (tg["conductor"]["title"], tg["conductor"]["title"], tg["file"],
                       "empty" if not tg["conductor"].get("hook_session") else "stale", sid))
        return None

    if sr == "maestro":
        if tr == "maestro":
            return None
        if has_live_permit(s_group, t, requested):
            return None
        return ("%s may message %s of group %s only under a permit from the operator, "
                "recorded in %s; no live permit there names this session."
                % (s_group["maestro"]["title"], tname, tg["name"], s_group["file"]))

    label = "the conductor" if sr == "conductor" else "a member"
    reason = ("%s of %s may not message outside its group; ask %s to raise an exchange."
              % (label, s_group["name"], s_group["maestro"]["title"]))
    if sr == "member" and tr == "maestro":
        reason += (" If you are %s, set maestro.hook_session in %s to %s."
                   % (s_group["maestro"]["title"], s_group["file"], sid))
    return reason


# ------------------------------------------------------------------ hook entry point

def block(reason):
    sys.stderr.write("MAESTRO GATE: " + reason + "\n")
    sys.stderr.flush()
    return 2


def main():
    raw = sys.stdin.buffer.read().decode("utf-8-sig", errors="replace")
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ValueError("hook payload is not a JSON object")

    tool = payload.get("tool_name")
    if tool not in GOVERNED_TOOLS:
        return 0
    tool_input = payload.get("tool_input") or {}
    name = tool_input.get("to") if tool == "SendMessage" else tool_input.get("session_id")
    if not isinstance(name, str) or not name.strip():
        return 0
    name = REF_SUFFIX_RE.sub("", name).strip()
    if name.lower() == "main" or AGENT_ID_RE.match(name):
        return 0  # in-session subagent plumbing; never governed

    groups, malformed = load_registry(registry_dir())
    cwd = norm_path(payload["cwd"]) if isinstance(payload.get("cwd"), str) \
        and payload["cwd"].strip() else None
    sid = str(payload.get("session_id") or "").strip()

    held = [m for m in malformed if m["workspace"] and path_contains(m["workspace"], cwd)]
    if held:
        return block("the registry file %s is malformed (%s) and this session's folder is "
                     "inside its workspace, so messages are held until that file is fixed."
                     % (held[0]["path"], held[0]["problem"]))

    s_group = sender_group(groups, cwd)
    sr = sender_role(s_group, sid) if s_group is not None else None

    targets = resolve(name, groups)
    if not targets:
        # An unregistered workspace is still another workspace. A governed Conductor or member
        # addressing "Maestro (X)" or "Conductor (X)" for some other X is leaving its group even
        # when X has no registry row yet (found 2026-10-10: a member of AST could reach
        # "Maestro (Vociferous Next)" because VOC had not registered).
        m = ROLE_TITLE_RE.match(name)
        if (m and s_group is not None and sr != "maestro"
                and norm_title(m.group(2)) != norm_title(s_group["name"])):
            label = "the conductor" if sr == "conductor" else "a member"
            return block("%s of %s may not message outside its group; ask %s to raise an exchange."
                         % (label, s_group["name"], s_group["maestro"]["title"]))
        return 0

    reasons = [evaluate(s_group, sr, sid, t, name) for t in targets]
    if len(targets) > 1:
        if any(reasons):
            first = next(r for r in reasons if r)
            where = ", ".join(sorted({t["group"]["name"] for t in targets}))
            return block("%s The name '%s' matches sessions in more than one group (%s); "
                         "address the session by its local_ id instead." % (first, name, where))
        return 0
    if reasons[0]:
        return block(reasons[0])
    return 0


def log_error():
    try:
        directory = os.path.expanduser("~/.maestro")
        os.makedirs(directory, exist_ok=True)
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        tb = traceback.format_exc().strip().replace("\r", "").replace("\n", " | ")
        with open(os.path.join(directory, "gate-errors.log"), "a", encoding="utf-8") as fh:
            fh.write("%s %s\n" % (stamp, tb))
    except Exception:
        pass


if __name__ == "__main__":
    try:
        code = main()
    except SystemExit:
        raise
    except BaseException:
        log_error()
        code = 0
    sys.exit(code)
