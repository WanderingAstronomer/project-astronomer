#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-census.py -- census of skill activations across Claude Code .jsonl transcripts.

WHAT IT ANSWERS
    Which skills fired, when, in which project, under which entrypoint, and what
    happened inside each span.

READ-ONLY, AND WHY THAT MATTERS TO D-005
    This instrument READS transcripts and WRITES only its own two output files at
    paths the caller names.  It never touches a project, a corpus, or a repository.
    D-005 bars a scaffolding CLI -- tooling that GENERATES or VALIDATES projects and
    thereby freezes the artifact set before a project has stressed it.  A measuring
    instrument is not that, which is the same argument fleet-census.py and
    check-corpus.py both carry, and tools/README.md states the read/write line twice.

    It is also the instrument L-11 asks for.  Every skill-usage number in this corpus
    was, until now, quoted rather than measured.

THE DECISIVE FIELD  (MEASURED 2026-08-28 against 3,286 files / 1.63 GB)
    'attributionSkill' is a TOP-LEVEL string, present ONLY on records whose
    top-level type is 'assistant'.  9,980 top-level occurrences corpus-wide;
    49 further substring hits are nested inside message text (transcripts that
    quote transcripts) and are correctly excluded by the escaping rule below.
    It marks a CONTIGUOUS SPAN over every assistant record produced while the
    skill was active.

TWO STRUCTURAL FACTS THIS TOOL IS BUILT ON  (both measured, see --selftest)

  1. LANES.  6,587 of 9,980 attributed records carry isSidechain=true and a
     top-level 'agentId' (attributionAgent='workflow-subagent').  Workflow
     subagents get their own transcript files, but agentId is still the correct
     span-segmentation key: without it, two agents sharing a file would fuse
     into one bogus span.  Contiguity is therefore evaluated PER LANE, where
     lane = agentId, or '__main__' for the main conversation.

  2. ESCAPING MAKES SUBSTRING GATES SOUND.  A record quoted inside another
     record's message text is JSON-escaped, so it reads \\"role\\":\\"assistant\\".
     The raw probe '"role":"assistant"' cannot match that.  Every cheap
     substring gate here is therefore a real structural test, not a heuristic.
     Corollary used for field extraction: the harness serialises top-level
     scalars AFTER the 'message' blob, so rfind() of a '"key":"' pattern lands
     on the top-level value.  --selftest proves this against full json.loads.

ACTIVATION, AND THE 367-OF-450 MYSTERY
    Counting 'Skill' TOOL CALLS undercounts spans ~6x.  A prior pass found that
    of 450 spans only 78 had a Skill tool_use within the preceding 15 records,
    6 had a slash command, and 367 had NEITHER.  This tool widens the lookback
    from a fixed 15 records to the START OF THE TURN (turns are delimited by
    'promptId', which is carried on user records) and reports BOTH windows, so
    the delta is measured rather than asserted.

    It also classifies activation, because width was never the real problem:
      tool-call               Skill tool_use naming this skill, in-lane, before the span
      slash-command           <command-name>/skill</command-name> in the lookback
      inherited-subagent      sidechain lane with no Skill tool_use anywhere in it --
                              the skill was inherited from the parent workflow, so no
                              lookback of ANY width can find an activation record
      resumed-after-compaction  a compact summary precedes the span, no other signal
      auto-trigger            main lane, turn start reached, no activation signal
      span-at-file-head       the file opens mid-span (resumed session); unknowable
      unknown                 anything left

STREAMING
    One pass, one line at a time, bounded memory.  Nothing is slurped.  Every
    line meets a cheap substring gate before json.loads; only gate-matched lines
    are parsed.  Per-file state is a handful of dicts; spans are written as they
    close and never accumulate.

ENCODING
    Reads utf-8/errors='replace'.  Writes utf-8 explicitly.  Prints ASCII only,
    because this interpreter's stdout is cp1252.

CLI
    --root      transcript root                 (default: ~/.claude/projects)
    --out       spans NDJSON                    (default: ./skill-spans.ndjson)
    --summary   summary JSON                    (default: ./skill-summary.json)
    --limit N   pilot: scan only the first N files
    --roster    file of known skill names, one per line, '#' comments ok.
                If omitted the roster is DERIVED from the 'skill_listing'
                attachments in the transcripts themselves -- the set of skills
                the harness actually offered the model, which is the honest
                denominator for a NEVER-FIRED list.
    --selftest N  cross-check the fast field extractor against json.loads on
                the first N gate-matched records and report mismatches.
    --progress N  print a progress line every N files (default 500).

Pure stdlib.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict, deque

# ---------------------------------------------------------------------------
# Cheap substring gates.  Sound because of the JSON-escaping property above.
# ---------------------------------------------------------------------------

G_ATTR_SKILL = '"attributionSkill"'
G_ASSISTANT = '"role":"assistant"'
G_TYPE_ASSISTANT = '"type":"assistant"'
G_SKILL_TOOL = '"name":"Skill"'
G_COMMAND = '<command-name>'
G_COMPACT = 'isCompactSummary'
G_ROSTER = '"skill_listing"'
G_PROMPTID = '"promptId"'
G_SKILL_BODY = 'Base directory for this skill:'
G_LAUNCHING = 'Launching skill:'

MAIN_LANE = '__main__'
FIXED_WINDOW = 15          # the prior pass's lookback, reproduced for comparison
TOOLUSE_MEMORY = 512       # bounded per-lane history of Skill tool_use events

_RE_CMD = re.compile(r'<command-name>/([^<\s]+)</command-name>')


G_TYPE_USER = '"type":"user"'
G_TOOL_RESULT = '"toolUseResult"'
G_IS_META = '"isMeta"'
G_SIDECHAIN_TRUE = '"isSidechain":true'


def is_user_turn(raw):
    """True only for a record a PERSON produced, in the main conversation.

    FOUR record kinds are `type: "user"` and are not a person: a tool result
    (`toolUseResult`), a compaction summary (`isCompactSummary`), harness meta
    (`isMeta`), and ANY record in a subagent lane (`isSidechain: true`) -- a
    subagent's "user" turns are the harness feeding it, not somebody speaking.

    The sidechain clause is the expensive one to have got wrong, and the fixture
    could not have caught it: it contains no sidechain records at all.  Measured on
    the real corpus without it, 3,174 of 3,404 spans closed on a "human turn" and
    3,315 of those were subagent lanes -- fragmenting single continuous activations
    into 967 one-record slivers.  A rule verified only against a fixture that cannot
    express the failing case is verified at the wrong altitude (L-12).

    Substring tests over the raw line, not a parse: this runs on every line of a
    1.6 GB corpus and must stay cheap.
    """
    if G_TYPE_USER not in raw:
        return False
    if G_TOOL_RESULT in raw or G_COMPACT in raw or G_IS_META in raw:
        return False
    if G_SIDECHAIN_TRUE in raw:
        return False
    return True


def tail_str(raw, key):
    """Extract a TOP-LEVEL string field without parsing the record.

    rfind() is deliberate: the harness serialises top-level scalars after the
    'message' blob, so the last occurrence is the top-level one.  Bails to None
    on any backslash in the value rather than guessing at an escape sequence.
    Proven against json.loads by --selftest.
    """
    pat = '"' + key + '":"'
    i = raw.rfind(pat)
    if i < 0:
        return None
    j = i + len(pat)
    k = raw.find('"', j)
    if k < 0:
        return None
    v = raw[j:k]
    if '\\' in v:
        return None
    return v


def iter_files(root, limit=None):
    """Yield transcript paths in a stable order.  Subagent transcripts are
    nested under <project>/<session>/subagents/..., so this walks recursively
    and derives the project from the first path component under root."""
    n = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for fn in sorted(filenames):
            if not fn.endswith('.jsonl'):
                continue
            yield os.path.join(dirpath, fn)
            n += 1
            if limit is not None and n >= limit:
                return


def project_of(root, path):
    rel = os.path.relpath(path, root)
    parts = rel.replace('\\', '/').split('/')
    return parts[0] if parts else '?'


def norm_skill(name):
    """'ns:skill' and 'skill' should compare equal for activation matching."""
    if not name:
        return ''
    return name.split(':')[-1].strip().lower()


class Span(object):
    __slots__ = ('skill', 'lane', 'agent', 'project', 'session', 'path', 'rel',
                 'start_ord', 'end_ord', 'start_ts', 'end_ts', 'records',
                 'entrypoint', 'version', 'cwd', 'git_branch', 'plugin',
                 'tools', 'mcp_servers', 'sidechain', 'act', 'act15',
                 'act_detail', 'turn_start_ord', 'text_records', 'thinking_records',
                 'closed_by')

    def __init__(self):
        self.tools = Counter()
        self.mcp_servers = Counter()
        self.records = 0
        self.text_records = 0
        self.thinking_records = 0
        self.end_ord = None
        self.end_ts = None
        self.plugin = None
        # Why the span ended.  Recorded rather than inferred, because 'human-turn'
        # and 'attribution-ended' are the same shape in the output and answer
        # different questions about whether a skill was abandoned or completed.
        self.closed_by = 'attribution-ended'

    def to_json(self):
        return {
            'skill': self.skill,
            'project': self.project,
            'session_id': self.session,
            'file': self.rel,
            'lane': self.lane,
            'is_sidechain': self.sidechain,
            'agent': self.agent,
            'start_ts': self.start_ts,
            'end_ts': self.end_ts,
            'start_record': self.start_ord,
            'end_record': self.end_ord,
            'record_count': self.records,
            'assistant_text_records': self.text_records,
            'thinking_records': self.thinking_records,
            'entrypoint': self.entrypoint,
            'harness_version': self.version,
            'cwd': self.cwd,
            'git_branch': self.git_branch,
            'plugin': self.plugin,
            'activation': self.act,
            'activation_window15': self.act15,
            'activation_detail': self.act_detail,
            'turn_start_record': self.turn_start_ord,
            'closed_by': self.closed_by,
            'tools': dict(self.tools),
            'mcp_servers': dict(self.mcp_servers),
        }


class Census(object):

    def __init__(self, root, selftest=0):
        self.root = root
        self.selftest_budget = selftest
        self.selftest_checked = 0
        self.selftest_mismatch = []

        # counters
        self.files_scanned = 0
        self.files_with_spans = 0
        self.lines_read = 0
        self.lines_gated = 0
        self.lines_parsed = 0
        self.lines_bad = 0          # gate-matched but json.loads raised
        self.lines_blank = 0        # empty / whitespace only
        self.lines_malformed = 0    # non-blank and not a '{...}' record: truncated or garbage
        self.decode_replacements = 0  # U+FFFD introduced by errors='replace' -- encoding damage
        self.files_failed = []
        self.bytes_read = 0

        self.assistant_records = 0
        self.assistant_by_entrypoint = Counter()
        self.assistant_by_project = Counter()
        self.attributed_records = 0

        # Anomaly counters.  Every one of these exists because the falsifier caught
        # the condition being handled SILENTLY, which is the false-success class:
        # a census that reads clean while missing a span is worse than one that fails.
        self.null_attr_records = 0       # key present, value null/empty -> TRANSPARENT (rule 6)
        self.nonstring_attr_records = 0  # key present, value not a string -> anomaly, reported
        self.duplicate_records = 0       # (sessionId, uuid) seen before -> a duplicated file in the root
        self.turn_closes = 0             # spans closed by a human turn -- NORMAL, not an anomaly
        self._seen_records = set()       # (sessionId, uuid) for parsed assistant records

        # Anomalies are emitted as a LIST of concrete records, each NAMING its file --
        # not as a dict of counters.  A consumer counting len() of a counter dict gets
        # the number of counter names, which never changes however many anomalies
        # occur; that is precisely how a silent drop stays silent.  Capped so a corrupt
        # corpus cannot exhaust memory, with the true total carried alongside.
        self.anomaly_records = []
        self.anomaly_total = 0

        self.spans = 0
        self.per_skill = defaultdict(lambda: {
            'spans': 0, 'records': 0, 'files': set(), 'projects': Counter(),
            'entrypoints': Counter(), 'activation': Counter(),
            'activation_window15': Counter(), 'tools': Counter(),
            'versions': Counter(), 'first_ts': None, 'last_ts': None,
            'sidechain_spans': 0,
        })
        self.per_project = defaultdict(lambda: {
            'spans': 0, 'records': 0, 'skills': Counter(), 'files_with_spans': set()})
        self.per_entrypoint = defaultdict(lambda: {'spans': 0, 'records': 0})
        self.activation_totals = Counter()
        self.activation15_totals = Counter()
        self.roster_seen = {}        # skill name -> first description line
        self.roster_projects = defaultdict(set)

    # -- roster ------------------------------------------------------------

    def absorb_roster(self, rec, project):
        att = rec.get('attachment') or {}
        content = att.get('content')
        if not isinstance(content, str):
            return
        for line in content.split('\n'):
            line = line.strip()
            if not line.startswith('- '):
                continue
            body = line[2:].strip()
            if not body:
                continue
            if ':' in body:
                name, desc = body.split(':', 1)
                # plugin skills are 'ns:name[: description]'
                if desc and not desc.startswith(' ') and ':' in desc:
                    ns_name = name + ':' + desc.split(':', 1)[0]
                    if ' ' not in ns_name:
                        name, desc = ns_name, desc.split(':', 1)[1]
                elif desc and not desc.startswith(' ') and ' ' not in desc:
                    name, desc = name + ':' + desc, ''
                name = name.strip()
                desc = desc.strip()
            else:
                name, desc = body, ''
            if not name or ' ' in name:
                continue
            if name not in self.roster_seen:
                self.roster_seen[name] = desc[:200]
            self.roster_projects[name].add(project)

    # -- span bookkeeping --------------------------------------------------

    ANOMALY_CAP = 2000

    def note_anomaly(self, kind, rel, rec, detail=None):
        """Record one anomaly, NAMING the file. Always counted; stored up to a cap."""
        self.anomaly_total += 1
        if len(self.anomaly_records) < self.ANOMALY_CAP:
            self.anomaly_records.append({
                'kind': kind,
                'file': rel,
                'uuid': (rec or {}).get('uuid'),
                'session_id': (rec or {}).get('sessionId'),
                'detail': detail,
            })

    def close_span(self, span, out_fh):
        agg = self.per_skill[span.skill]
        agg['spans'] += 1
        agg['records'] += span.records
        agg['files'].add(span.rel)
        agg['projects'][span.project] += 1
        agg['entrypoints'][span.entrypoint or '?'] += 1
        agg['activation'][span.act] += 1
        agg['activation_window15'][span.act15] += 1
        agg['tools'].update(span.tools)
        if span.version:
            agg['versions'][span.version] += 1
        if span.sidechain:
            agg['sidechain_spans'] += 1
        if span.start_ts and (agg['first_ts'] is None or span.start_ts < agg['first_ts']):
            agg['first_ts'] = span.start_ts
        if span.end_ts and (agg['last_ts'] is None or span.end_ts > agg['last_ts']):
            agg['last_ts'] = span.end_ts

        p = self.per_project[span.project]
        p['spans'] += 1
        p['records'] += span.records
        p['skills'][span.skill] += 1
        p['files_with_spans'].add(span.rel)

        e = self.per_entrypoint[span.entrypoint or '?']
        e['spans'] += 1
        e['records'] += span.records

        self.activation_totals[span.act] += 1
        self.activation15_totals[span.act15] += 1
        self.spans += 1

        out_fh.write(json.dumps(span.to_json(), ensure_ascii=False))
        out_fh.write('\n')

    # -- the pass ----------------------------------------------------------

    def scan_file(self, path, out_fh):
        project = project_of(self.root, path)
        rel = os.path.relpath(path, self.root).replace('\\', '/')
        self.files_scanned += 1
        try:
            self.bytes_read += os.path.getsize(path)
        except OSError:
            pass

        open_spans = {}                       # lane -> Span
        lane_skill_tools = defaultdict(lambda: deque(maxlen=TOOLUSE_MEMORY))
        lane_has_skill_tool = defaultdict(bool)
        lane_slash = defaultdict(lambda: deque(maxlen=64))
        lane_compact = {}                     # lane -> ordinal of last compact marker
        lane_body_inject = defaultdict(lambda: deque(maxlen=64))
        lane_first_ord = {}
        turn_start = 0
        cur_prompt = None
        ordinal = -1
        opened_any = False

        try:
            fh = io.open(path, 'r', encoding='utf-8', errors='replace')
        except OSError:
            self.lines_bad += 1
            return
        with fh:
            for raw in fh:
                ordinal += 1
                self.lines_read += 1

                # ---- structural health, checked on EVERY line ---------------
                # This must be able to FIRE, so it does not depend on the gate:
                # a truncated or garbage line never matches a gate substring and
                # would otherwise be silently invisible.  Every legitimate record
                # is exactly one JSON object on one line.
                stripped = raw.strip()
                if not stripped:
                    self.lines_blank += 1
                    continue
                if stripped[0] != '{' or stripped[-1] != '}':
                    self.lines_malformed += 1
                    continue
                if '�' in raw:
                    self.decode_replacements += 1

                is_assistant = G_ASSISTANT in raw
                has_attr = G_ATTR_SKILL in raw and is_assistant
                is_skilltool = G_SKILL_TOOL in raw
                is_cmd = G_COMMAND in raw
                is_compact = G_COMPACT in raw
                is_roster = G_ROSTER in raw
                is_body = (G_SKILL_BODY in raw) or (G_LAUNCHING in raw)
                has_prompt = G_PROMPTID in raw

                # ---- turn boundary (promptId lives on user records) --------
                if has_prompt:
                    pid = tail_str(raw, 'promptId')
                    if pid and pid != cur_prompt:
                        cur_prompt = pid
                        turn_start = ordinal

                # RULE 5: a HUMAN TURN closes every open span.  Two uses of one skill
                # with a person speaking in between are two firings, not one -- the
                # audit asks "how often was this skill reached for", and a new ask is
                # a new reach.  Without this the extractor merges them and UNDERCOUNTS
                # (the fixture caught it on astronomer-supervise B2/B3).
                #
                # A human turn is defined STRUCTURALLY, not by a promptId change, and
                # that distinction is the whole difficulty.  Three kinds of record are
                # `type: "user"` and carry a promptId while being nothing to do with a
                # person: a TOOL RESULT (carries toolUseResult), a COMPACTION SUMMARY
                # (isCompactSummary), and harness META records (isMeta).  Closing on
                # any of those splits a span that should be whole -- measured on the
                # fixture, it split anthropic-skills:astronomer-start at a tool result
                # and deep-research at a compaction boundary, turning 12 spans into 14.
                # ...and it closes ONLY main-lane spans.  A person speaking in the main
                # conversation says nothing about whether a subagent running in parallel
                # is still inside its skill.
                if is_user_turn(raw):
                    for _lane, _sp in list(open_spans.items()):
                        if _lane != MAIN_LANE:
                            continue
                        _sp.closed_by = 'human-turn'
                        self.close_span(_sp, out_fh)
                        self.turn_closes += 1
                        del open_spans[_lane]

                # ---- fast lane/type extraction for assistant records -------
                lane = None
                if is_assistant:
                    # Confirm the top-level type.  This MUST NOT use tail_str():
                    # rfind() assumes top-level scalars serialise after 'message',
                    # which holds for most records but NOT all -- measured, 66 of
                    # 68,770 sampled assistant records end with a content block
                    # whose own "type" is serialised last, and rfind returned
                    # 'text'.  That silently DROPS a genuine assistant record.
                    # A plain substring test is exact instead: no message content
                    # block is ever typed "assistant" (blocks are text / thinking /
                    # tool_use / tool_result / image / document), message.type is
                    # "message", and a quoted record nested in text would be
                    # backslash-escaped and cannot match.
                    if G_TYPE_ASSISTANT not in raw:
                        is_assistant = False
                        has_attr = False
                    else:
                        agent = tail_str(raw, 'agentId')
                        lane = agent or MAIN_LANE
                        if lane not in lane_first_ord:
                            lane_first_ord[lane] = ordinal
                        self.assistant_records += 1
                        ep = tail_str(raw, 'entrypoint') or '?'
                        self.assistant_by_entrypoint[ep] += 1
                        self.assistant_by_project[project] += 1

                gated = has_attr or is_skilltool or is_cmd or is_compact or is_roster or is_body
                if gated:
                    self.lines_gated += 1

                rec = None
                if gated:
                    try:
                        rec = json.loads(raw)
                        self.lines_parsed += 1
                    except Exception:
                        self.lines_bad += 1
                        rec = None

                # ---- roster harvest ---------------------------------------
                if rec is not None and is_roster:
                    try:
                        self.absorb_roster(rec, project)
                    except Exception:
                        pass

                # ---- activation signals -----------------------------------
                if rec is not None and (is_skilltool or is_cmd or is_compact or is_body):
                    sig_lane = rec.get('agentId') or MAIN_LANE
                    if is_skilltool:
                        for blk in _content_blocks(rec):
                            if blk.get('type') == 'tool_use' and blk.get('name') == 'Skill':
                                inp = blk.get('input') or {}
                                nm = inp.get('skill') if isinstance(inp, dict) else None
                                lane_skill_tools[sig_lane].append((ordinal, nm))
                                lane_has_skill_tool[sig_lane] = True
                    if is_cmd:
                        txt = _flat_text(rec)
                        for m in _RE_CMD.finditer(txt):
                            lane_slash[sig_lane].append((ordinal, m.group(1)))
                    if is_compact:
                        lane_compact[sig_lane] = ordinal
                    if is_body:
                        lane_body_inject[sig_lane].append(ordinal)

                # ---- span open / extend / close ---------------------------
                if not is_assistant:
                    continue

                # ---- duplicate suppression --------------------------------
                # A session present in TWO files under the scan root was counted
                # twice (falsifier D4).  That is not hypothetical here: this machine
                # now holds a D: backup of ~/.claude/projects, so any scan rooted
                # above both copies would double every span.  Identity is
                # (sessionId, uuid) -- uuid is unique per record within a session.
                if rec is not None:
                    _sid = rec.get('sessionId')
                    _uid = rec.get('uuid')
                    if _sid is not None and _uid is not None:
                        _key = (_sid, _uid)
                        if _key in self._seen_records:
                            self.duplicate_records += 1
                            self.note_anomaly('duplicate-record', rel, rec)
                            continue
                        self._seen_records.add(_key)

                # ---- attribution --------------------------------------------
                # THREE distinct states, and collapsing them is what the falsifier
                # caught.  Key ABSENT means the skill is no longer active and the
                # span closes.  Key PRESENT with a usable string extends or opens.
                # Key PRESENT but null/empty/non-string is TRANSPARENT (rule 6): it
                # neither closes nor extends, and it is COUNTED -- never dropped in
                # silence, which is how a span used to get split in two.
                skill = None
                transparent = False
                if has_attr:
                    if rec is not None:
                        s = rec.get('attributionSkill')
                        if isinstance(s, str) and s:
                            skill = s
                        elif s is None or s == '':
                            transparent = True
                            self.null_attr_records += 1
                            self.note_anomaly('null-attribution', rel, rec)
                        else:
                            transparent = True
                            self.nonstring_attr_records += 1
                            self.note_anomaly(
                                'nonstring-attribution', rel, rec,
                                'value is %s, not a string' % type(s).__name__)
                    else:
                        s = tail_str(raw, 'attributionSkill')
                        if s:
                            skill = s
                        else:
                            transparent = True
                            self.null_attr_records += 1
                            self.note_anomaly('null-attribution-unparsed', rel, None)

                cur = open_spans.get(lane)
                if transparent:
                    # Do not close, do not extend, do not count as attributed.
                    continue
                if cur is not None and (skill is None or skill != cur.skill):
                    cur.closed_by = 'attribution-ended' if skill is None else 'skill-changed'
                    self.close_span(cur, out_fh)
                    del open_spans[lane]
                    cur = None

                if skill is None:
                    continue

                self.attributed_records += 1

                if cur is None:
                    cur = Span()
                    cur.skill = skill
                    cur.lane = lane
                    cur.project = project
                    cur.rel = rel
                    cur.path = path
                    cur.start_ord = ordinal
                    cur.turn_start_ord = turn_start
                    cur.sidechain = bool(rec.get('isSidechain')) if rec else (lane != MAIN_LANE)
                    cur.agent = (rec or {}).get('attributionAgent')
                    cur.session = (rec or {}).get('sessionId')
                    cur.entrypoint = (rec or {}).get('entrypoint')
                    cur.version = (rec or {}).get('version')
                    cur.cwd = (rec or {}).get('cwd')
                    cur.git_branch = (rec or {}).get('gitBranch')
                    cur.plugin = (rec or {}).get('attributionPlugin')
                    cur.start_ts = (rec or {}).get('timestamp')
                    act, act15, detail = self._classify(
                        skill, lane, ordinal, turn_start,
                        lane_skill_tools, lane_has_skill_tool, lane_slash,
                        lane_compact, lane_body_inject, lane_first_ord)
                    cur.act, cur.act15, cur.act_detail = act, act15, detail
                    open_spans[lane] = cur
                    opened_any = True

                cur.records += 1
                cur.end_ord = ordinal
                if rec is not None:
                    ts = rec.get('timestamp')
                    if ts:
                        cur.end_ts = ts
                    for blk in _content_blocks(rec):
                        bt = blk.get('type')
                        if bt == 'tool_use':
                            nm = blk.get('name') or '?'
                            cur.tools[nm] += 1
                            if nm.startswith('mcp__'):
                                parts = nm.split('__')
                                if len(parts) > 1:
                                    cur.mcp_servers[parts[1]] += 1
                        elif bt == 'text':
                            cur.text_records += 1
                        elif bt == 'thinking':
                            cur.thinking_records += 1
                    if self.selftest_budget and self.selftest_checked < self.selftest_budget:
                        self._selftest(raw, rec, rel, ordinal)

        # file ended -- close every still-open span (files CAN end mid-span)
        for lane, sp in list(open_spans.items()):
            self.close_span(sp, out_fh)
        if opened_any:
            self.files_with_spans += 1

    # -- activation classifier --------------------------------------------

    def _classify(self, skill, lane, ordinal, turn_start,
                  lane_skill_tools, lane_has_skill_tool, lane_slash,
                  lane_compact, lane_body_inject, lane_first_ord):
        """Return (activation_turn_window, activation_fixed15_window, detail).

        The two windows differ only in how far back the search runs:
          window15   -- the prior pass's fixed 15-record lookback
          turn       -- back to the start of the current promptId turn, or to
                        the lane's first record for a sidechain lane
        """
        want = norm_skill(skill)
        sidechain = lane != MAIN_LANE
        lane_start = lane_first_ord.get(lane, 0)
        turn_lo = lane_start if sidechain else min(turn_start, ordinal)
        fixed_lo = ordinal - FIXED_WINDOW
        detail = {'lane_start': lane_start, 'turn_lo': turn_lo,
                  'fixed_lo': fixed_lo, 'sidechain': sidechain}

        tool_hit = tool_hit15 = None
        for (o, nm) in reversed(lane_skill_tools[lane]):
            if o >= ordinal:
                continue
            match = (nm is None) or (norm_skill(nm) == want)
            if o >= turn_lo and match and tool_hit is None:
                tool_hit = (o, nm)
            if o >= fixed_lo and match and tool_hit15 is None:
                tool_hit15 = (o, nm)
            if o < turn_lo and o < fixed_lo:
                break

        slash_hit = slash_hit15 = None
        for (o, nm) in reversed(lane_slash[lane]):
            if o >= ordinal:
                continue
            match = norm_skill(nm) == want
            if o >= turn_lo and match and slash_hit is None:
                slash_hit = (o, nm)
            if o >= fixed_lo and match and slash_hit15 is None:
                slash_hit15 = (o, nm)

        comp = lane_compact.get(lane)
        comp_in_turn = comp is not None and turn_lo <= comp < ordinal
        comp_in_15 = comp is not None and fixed_lo <= comp < ordinal

        body = None
        for o in reversed(lane_body_inject[lane]):
            if o < ordinal:
                body = o
                break
        body_in_turn = body is not None and body >= turn_lo

        at_head = ordinal - lane_start <= 2

        def decide(tool, slash, comp_flag, body_flag):
            if tool is not None:
                return 'tool-call'
            if slash is not None:
                return 'slash-command'
            if sidechain and not lane_has_skill_tool[lane]:
                return 'inherited-subagent'
            if comp_flag:
                return 'resumed-after-compaction'
            if body_flag:
                return 'unknown'          # skill body injected, activation record lost
            if at_head:
                return 'span-at-file-head'
            return 'auto-trigger'

        act = decide(tool_hit, slash_hit, comp_in_turn, body_in_turn)
        act15 = decide(tool_hit15, slash_hit15, comp_in_15,
                       body is not None and body >= fixed_lo)

        if tool_hit:
            detail['tool_use_at'] = tool_hit[0]
            detail['tool_use_distance'] = ordinal - tool_hit[0]
            detail['tool_use_name'] = tool_hit[1]
        if slash_hit:
            detail['slash_at'] = slash_hit[0]
            detail['slash_name'] = slash_hit[1]
        if comp is not None:
            detail['compact_at'] = comp
        if body is not None:
            detail['skill_body_at'] = body
        return act, act15, detail

    # -- selftest ----------------------------------------------------------

    def _selftest(self, raw, rec, rel, ordinal):
        self.selftest_checked += 1
        # 'type' is deliberately absent: the census no longer reads it through
        # tail_str (see the G_TYPE_ASSISTANT note above).  These are exactly the
        # fields tail_str still drives.
        if (G_TYPE_ASSISTANT in raw) != (rec.get('type') == 'assistant'):
            if len(self.selftest_mismatch) < 40:
                self.selftest_mismatch.append(
                    {'file': rel, 'record': ordinal, 'key': '<assistant gate>',
                     'fast': G_TYPE_ASSISTANT in raw,
                     'slow': rec.get('type') == 'assistant'})
        for key in ('entrypoint', 'sessionId', 'version',
                    'attributionSkill', 'agentId', 'promptId'):
            fast = tail_str(raw, key)
            slow = rec.get(key)
            if not isinstance(slow, str):
                slow = None
            if fast != slow:
                if len(self.selftest_mismatch) < 40:
                    self.selftest_mismatch.append(
                        {'file': rel, 'record': ordinal, 'key': key,
                         'fast': fast, 'slow': slow})

    # -- summary -----------------------------------------------------------

    def summary(self, roster_override, elapsed, out_path, summary_path):
        fired = set(self.per_skill.keys())
        fired_norm = set(norm_skill(s) for s in fired)

        if roster_override is not None:
            roster = dict((r, '') for r in roster_override)
            roster_source = 'supplied file'
        else:
            roster = dict(self.roster_seen)
            roster_source = 'derived from skill_listing attachments in the corpus'

        never = []
        for name in sorted(roster):
            if name in fired or norm_skill(name) in fired_norm:
                continue
            never.append({'skill': name,
                          'offered_in_projects': len(self.roster_projects.get(name, ())),
                          'description': (roster.get(name) or '')[:140]})

        fired_not_in_roster = sorted(s for s in fired
                                     if s not in roster and norm_skill(s) not in
                                     set(norm_skill(r) for r in roster))

        per_skill = {}
        for k, v in self.per_skill.items():
            per_skill[k] = {
                'spans': v['spans'],
                'attributed_records': v['records'],
                'sidechain_spans': v['sidechain_spans'],
                'main_spans': v['spans'] - v['sidechain_spans'],
                'files': len(v['files']),
                'projects': dict(v['projects']),
                'entrypoints': dict(v['entrypoints']),
                'activation': dict(v['activation']),
                'activation_window15': dict(v['activation_window15']),
                'harness_versions': dict(v['versions']),
                'first_ts': v['first_ts'],
                'last_ts': v['last_ts'],
                'top_tools': dict(v['tools'].most_common(15)),
            }

        per_entrypoint = {}
        for ep, cnt in self.assistant_by_entrypoint.items():
            spans = self.per_entrypoint.get(ep, {}).get('spans', 0)
            recs = self.per_entrypoint.get(ep, {}).get('records', 0)
            per_entrypoint[ep] = {
                'assistant_records': cnt,
                'spans': spans,
                'attributed_records': recs,
                'spans_per_1000_assistant_records': round(1000.0 * spans / cnt, 3) if cnt else None,
                'attributed_share_pct': round(100.0 * recs / cnt, 3) if cnt else None,
            }
        for ep, v in self.per_entrypoint.items():
            if ep not in per_entrypoint:
                per_entrypoint[ep] = {
                    'assistant_records': 0, 'spans': v['spans'],
                    'attributed_records': v['records'],
                    'spans_per_1000_assistant_records': None,
                    'attributed_share_pct': None}

        per_project = {}
        for k, v in self.per_project.items():
            per_project[k] = {
                'spans': v['spans'],
                'attributed_records': v['records'],
                'files_with_spans': len(v['files_with_spans']),
                'assistant_records': self.assistant_by_project.get(k, 0),
                'spans_per_1000_assistant_records': (
                    round(1000.0 * v['spans'] / self.assistant_by_project[k], 3)
                    if self.assistant_by_project.get(k) else None),
                'skills': dict(v['skills']),
            }

        try:
            out_size = os.path.getsize(out_path)
        except OSError:
            out_size = None

        return {
            'generated_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            'root': self.root,
            'run': {
                'wall_clock_s': round(elapsed, 3),
                'files_scanned': self.files_scanned,
                'files_with_spans': self.files_with_spans,
                'bytes_read': self.bytes_read,
                'lines_read': self.lines_read,
                'lines_gated': self.lines_gated,
                'lines_parsed': self.lines_parsed,
                'lines_unparseable': self.lines_bad,
                'lines_blank': self.lines_blank,
                'lines_malformed': self.lines_malformed,
                'lines_skipped_total': self.lines_bad + self.lines_blank + self.lines_malformed,
                'lines_with_decode_replacement': self.decode_replacements,
                'files_failed': self.files_failed,
                'gate_selectivity_pct': round(100.0 * self.lines_gated / self.lines_read, 3) if self.lines_read else None,
                'lines_per_s': round(self.lines_read / elapsed, 1) if elapsed else None,
                'output_bytes': out_size,
                'spans_ndjson': out_path,
                'summary_json': summary_path,
            },
            'totals': {
                'spans': self.spans,
                'assistant_records': self.assistant_records,
                'attributed_records': self.attributed_records,
                'attributed_share_pct': round(100.0 * self.attributed_records / self.assistant_records, 3) if self.assistant_records else None,
                'distinct_skills_fired': len(self.per_skill),
                'roster_size': len(roster),
                'roster_source': roster_source,
            },
            # A LIST, each entry naming its file. Reported always, including empty.
            'anomalies': self.anomaly_records,
            'anomaly_counts': {
                'total': self.anomaly_total,
                'listed': len(self.anomaly_records),
                'capped_at': self.ANOMALY_CAP,
                'null_or_empty_attribution_records': self.null_attr_records,
                'nonstring_attribution_records': self.nonstring_attr_records,
                'duplicate_records_suppressed': self.duplicate_records,
            },
            # NOT an anomaly -- a span ending because a person spoke is the normal
            # case under rule 5, and filing it beside real defects would drown them.
            'spans_closed_by_human_turn': self.turn_closes,
            'activation_turn_window': dict(self.activation_totals),
            'activation_fixed15_window': dict(self.activation15_totals),
            'per_skill': per_skill,
            'per_project': per_project,
            'per_entrypoint': per_entrypoint,
            'never_fired': never,
            'fired_but_not_in_roster': fired_not_in_roster,
            'selftest': {
                'records_checked': self.selftest_checked,
                'mismatches': len(self.selftest_mismatch),
                'examples': self.selftest_mismatch[:10],
            },
        }


def _content_blocks(rec):
    m = rec.get('message')
    if not isinstance(m, dict):
        return ()
    c = m.get('content')
    if not isinstance(c, list):
        return ()
    return [b for b in c if isinstance(b, dict)]


def _flat_text(rec):
    m = rec.get('message')
    if not isinstance(m, dict):
        return ''
    c = m.get('content')
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        out = []
        for b in c:
            if isinstance(b, dict) and isinstance(b.get('text'), str):
                out.append(b['text'])
        return '\n'.join(out)
    return ''


def load_roster(path):
    names = []
    with io.open(path, 'r', encoding='utf-8', errors='replace') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            names.append(line.split()[0].rstrip(':'))
    return names


def main(argv=None):
    default_root = os.path.join(os.path.expanduser('~'), '.claude', 'projects')
    ap = argparse.ArgumentParser(description='Census of skill spans in Claude Code transcripts.')
    ap.add_argument('--root', default=default_root)
    ap.add_argument('--out', default='skill-spans.ndjson')
    ap.add_argument('--summary', default='skill-summary.json')
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--roster', default=None)
    ap.add_argument('--selftest', type=int, default=0)
    ap.add_argument('--progress', type=int, default=500)
    args = ap.parse_args(argv)

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        sys.stderr.write('root not a directory: %s\n' % root)
        return 2

    roster_override = load_roster(args.roster) if args.roster else None

    census = Census(root, selftest=args.selftest)
    t0 = time.time()
    with io.open(args.out, 'w', encoding='utf-8', newline='\n') as out_fh:
        for i, path in enumerate(iter_files(root, args.limit), 1):
            try:
                census.scan_file(path, out_fh)
            except Exception as exc:          # never let one bad file kill the pass
                census.files_failed.append(
                    {'file': os.path.relpath(path, root).replace('\\', '/'),
                     'error': repr(exc)[:200]})
                sys.stderr.write('file failed: %s: %r\n' %
                                 (os.path.relpath(path, root), exc))
            if args.progress and i % args.progress == 0:
                sys.stdout.write('  ... %d files, %d lines, %d spans, %.1fs\n'
                                 % (i, census.lines_read, census.spans, time.time() - t0))
                sys.stdout.flush()
    elapsed = time.time() - t0

    summ = census.summary(roster_override, elapsed, os.path.abspath(args.out),
                          os.path.abspath(args.summary))
    with io.open(args.summary, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(summ, indent=2, ensure_ascii=False, sort_keys=False))
        fh.write('\n')

    r = summ['run']
    t = summ['totals']
    # ASCII only: this interpreter's stdout is cp1252.
    print('wall clock       %.2f s' % r['wall_clock_s'])
    print('files scanned    %d  (with spans: %d)' % (r['files_scanned'], r['files_with_spans']))
    print('bytes read       %d' % r['bytes_read'])
    print('lines read       %d' % r['lines_read'])
    print('lines gated      %d  (%.1f%% of lines)' % (r['lines_gated'], r['gate_selectivity_pct'] or 0.0))
    print('lines parsed     %d' % r['lines_parsed'])
    print('lines skipped    %d  (unparseable %d, malformed/truncated %d, blank %d)'
          % (r['lines_skipped_total'], r['lines_unparseable'],
             r['lines_malformed'], r['lines_blank']))
    print('decode damage    %d lines carried a replacement char' % r['lines_with_decode_replacement'])
    print('files failed     %d' % len(r['files_failed']))
    print('assistant recs   %d' % t['assistant_records'])
    print('attributed recs  %d  (%.2f%%)' % (t['attributed_records'], t['attributed_share_pct'] or 0.0))
    print('spans            %d  across %d distinct skills' % (t['spans'], t['distinct_skills_fired']))
    print('output bytes     %s' % r['output_bytes'])
    print('')
    print('activation, lookback = START OF TURN:')
    for k, v in sorted(summ['activation_turn_window'].items(), key=lambda kv: -kv[1]):
        print('   %-26s %d' % (k, v))
    print('activation, lookback = 15 records (prior method):')
    for k, v in sorted(summ['activation_fixed15_window'].items(), key=lambda kv: -kv[1]):
        print('   %-26s %d' % (k, v))
    print('')
    print('never fired (of roster %d, source: %s): %d'
          % (t['roster_size'], t['roster_source'], len(summ['never_fired'])))
    if summ['selftest']['records_checked']:
        print('selftest: %d records cross-checked, %d field mismatches'
              % (summ['selftest']['records_checked'], summ['selftest']['mismatches']))
    print('')
    print('spans   -> %s' % r['spans_ndjson'])
    print('summary -> %s' % r['summary_json'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
