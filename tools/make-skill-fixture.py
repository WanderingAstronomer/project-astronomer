#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make-skill-fixture.py -- synthetic .jsonl transcripts with a KNOWN skill-span count.

WHY THIS EXISTS
---------------
The transcript extractor (scratchpad/skill-census.py) is going to produce a number.
A number produced by a program that has only ever been run on real data, where nobody
knows the true answer, is a REPORT, not a MEASUREMENT. This fixture is the known-truth
target: it contains exactly 12 skill spans, it says which 12, and it contains the
awkward shapes on purpose so that an extractor which merely pattern-matches the easy
case is caught here rather than downstream.

FIDELITY -- what was measured, not guessed
------------------------------------------
Every record shape below was read out of real transcripts under
C:/Users/drew/.claude/projects/ on 2026-08-28. Specifically MEASURED:

  * `attributionSkill` appears ONLY on records of type "assistant". Sampled 4,564 lines
    across 40 files: 46 attributed records, all type=assistant, all str-valued.
    A further 3 large vociferous-next transcripts: 116 attributed records, all assistant.
  * `attributionSkill` sits at the TOP LEVEL of the record, beside `attributionPlugin`,
    NOT inside `message`.
  * The `Skill` tool_use that activates a skill is itself UNATTRIBUTED. In
    coaw/b31b8ff5 the Skill call is line 13 and the first attributed record is line 19.
    An extractor that counts Skill tool calls is therefore counting a different thing.
  * Skill names appear both plugin-qualified ("anthropic-skills:astronomer-start") and
    bare ("astronomer-supervise", "deep-research").
  * Attributed runs are interleaved with UNATTRIBUTED records -- user/tool_result,
    attachment, last-prompt, custom-title, ai-title -- so "consecutive" cannot mean
    "adjacent lines".
  * A compaction boundary is type="system", subtype="compact_boundary", parentUuid=null,
    with `logicalParentUuid` and `compactMetadata`; it is followed by a type="user"
    record carrying isCompactSummary=true and isVisibleInTranscriptOnly=true.
  * `promptId` is present on essentially ALL user records (176/176 in coaw/b31b8ff5), so
    it does NOT distinguish a human turn from a tool result. The discriminator is the
    content shape: a human turn has string content, or a list with no tool_result block
    (measured: 170 tool_result vs 6 human turns in that file).

NOT observed in the real corpus, and therefore SYNTHETIC hazards -- stated so nobody
mistakes them for field data:

  * attributionSkill present but null or "". Zero instances found corpus-wide.
  * A skill span straddling a compaction boundary. 5 files contain both a span and a
    boundary; in 0 of them does the same skill appear on both sides. The fixture asserts
    a CHOSEN answer here (see CONTRACT rule 4), it does not report a fact.
  * The same session written to two files. Checked: no case-differing project dirs on
    this machine. It remains a live hazard for any extractor pointed at a root that also
    contains a backup or rescue copy, which is why the verifier seeds it.

THE CONTRACT THE FIXTURE ENFORCES
---------------------------------
1. A SPAN is a maximal run of attributed records sharing one `attributionSkill` value.
2. Unattributed records are TRANSPARENT: they do not end a span. (Forced by the real
   data -- user/tool_result records sit inside every real span.)
3. A DIFFERENT attributed skill ends the current span and opens a new one, even with no
   record in between.
4. A compaction boundary is TRANSPARENT. Same skill either side == ONE span.
   This is a CHOICE, not an observation. It is pinned here so that an extractor which
   chooses differently disagrees LOUDLY instead of quietly.
5. A HUMAN TURN ends any open span. Human turn == type "user" whose message.content is a
   string, or is a list containing no tool_result block. Without this rule two separate
   uses of one skill in one session collapse into one span.
6. attributionSkill that is null or "" counts as UNATTRIBUTED (transparent, rule 2) and
   must be COUNTED and REPORTED, never silently discarded.
7. A span needs at least one ATTRIBUTED record. A Skill tool call with no attributed
   record after it is an activation that did nothing -- it is not a span.
8. A span still open when the file ends IS a span (`ends_open`).
9. Records are deduplicated by (sessionId, uuid). The same session appearing in two
   files must not double-count.
10. An unparseable line is SKIPPED AND REPORTED. Never fatal, never invisible.

Usage:
    python make-skill-fixture.py [--out DIR] [--quiet]

Writes DIR/*.jsonl and DIR/MANIFEST.json. Default DIR is
<scratchpad>/skill-census-fixture. Exits 0 on success.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRATCH = Path(__file__).resolve().parent
DEFAULT_OUT = SCRATCH / "skill-census-fixture"

VERSION = "2.1.229"
MODEL = "claude-opus-5"
CWD = r"C:\Users\drew\Documents\DevSlop\fixture-project"


# --------------------------------------------------------------------------------------
# record construction -- shapes copied from real transcripts, payloads shortened
# --------------------------------------------------------------------------------------


class Session:
    """Builds one .jsonl file's worth of records with a valid parentUuid chain."""

    def __init__(self, session_id: str, filename: str, branch: str = "main",
                 clock_offset_s: int = 0, sidechain: bool = False,
                 agent_id: str | None = None) -> None:
        self.session_id = session_id
        self.filename = filename
        self.branch = branch
        # A SUBAGENT lane. Its `type: "user"` records are the harness feeding the
        # agent, not a person speaking, so they must NOT close a skill span. The
        # fixture had no sidechain records at all until 2026-08-28, which meant the
        # rule governing 3,315 of the real corpus's spans was untestable here.
        self.sidechain = sidechain
        self.agent_id = agent_id
        self.records: list[object] = []  # dicts, or raw str for deliberately bad lines
        self.prev_uuid: str | None = None
        self._n = 0
        # Each session starts at its own hour. Without this every session's Nth record
        # shares a timestamp with every other session's Nth record, and any consumer
        # that identifies a span by start_ts silently confuses two files. The falsifier
        # hit that collision on its first real run against the extractor.
        self._t = clock_offset_s

    # -- helpers ------------------------------------------------------------------

    def _uuid(self, tag: str) -> str:
        """Deterministic, human-readable, uuid-shaped. Readability beats realism here:
        when the verifier prints a missing span the operator can see WHICH one."""
        self._n += 1
        stem = f"{self.session_id[:8]}-{tag}"[:18].replace(" ", "-")
        return f"{stem:-<18}-{self._n:04d}-{self.session_id[:12]}"

    def _ts(self) -> str:
        self._t += 7
        m, s = divmod(self._t, 60)
        h, m = divmod(m, 60)
        return f"2026-08-27T{9 + h:02d}:{m:02d}:{s:02d}.000Z"

    def _env(self, uuid: str, parent: str | None) -> dict:
        env_agent = {"agentId": self.agent_id} if self.agent_id else {}
        return {
            **env_agent,
            "parentUuid": parent,
            "isSidechain": self.sidechain,
            "uuid": uuid,
            "timestamp": self._ts(),
            "userType": "external",
            "entrypoint": "claude-desktop",
            "cwd": CWD,
            "sessionId": self.session_id,
            "version": VERSION,
            "gitBranch": self.branch,
        }

    def _emit(self, rec: dict) -> str:
        self.records.append(rec)
        self.prev_uuid = rec["uuid"]
        return rec["uuid"]

    @staticmethod
    def _usage() -> dict:
        return {
            "input_tokens": 2,
            "cache_creation_input_tokens": 1200,
            "cache_read_input_tokens": 41000,
            "output_tokens": 310,
            "service_tier": "standard",
            "speed": "standard",
        }

    # -- record kinds -------------------------------------------------------------

    def human(self, text: str) -> str:
        """A real human turn. String content -- the measured discriminator."""
        uuid = self._uuid("human")
        rec = self._env(uuid, self.prev_uuid)
        rec.update({
            "promptId": self._uuid("prompt"),
            "type": "user",
            "message": {"role": "user", "content": text},
        })
        return self._emit(rec)

    def assistant(self, blocks: list, skill=None, plugin=None, tag: str = "asst") -> str:
        uuid = self._uuid(tag)
        rec = self._env(uuid, self.prev_uuid)
        rec.update({
            "message": {
                "model": MODEL,
                "id": "msg_" + uuid.replace("-", "")[:24],
                "type": "message",
                "role": "assistant",
                "content": blocks,
                "stop_reason": "tool_use",
                "stop_sequence": None,
                "usage": self._usage(),
            },
            "requestId": "req_" + uuid.replace("-", "")[:24],
            "type": "assistant",
            "effort": "high",
        })
        # attributionSkill sits at TOP level, beside attributionPlugin. Measured.
        # `skill` may legitimately be None (no key at all), or the sentinel objects
        # NULL_SKILL / EMPTY_SKILL which write the key with a null/"" value.
        if skill is NULL_SKILL:
            rec["attributionSkill"] = None
        elif skill is EMPTY_SKILL:
            rec["attributionSkill"] = ""
        elif skill is not None:
            rec["attributionSkill"] = skill
            rec["attributionPlugin"] = plugin if plugin else skill.split(":")[0]
        # Key order in real files puts attribution before type; JSON objects are
        # unordered by spec and json.loads is order-blind, so this is cosmetic only.
        return self._emit(rec)

    def text(self, s: str, skill=None, plugin=None) -> str:
        return self.assistant([{"type": "text", "text": s}], skill, plugin)

    def thinking(self, skill=None, plugin=None) -> str:
        return self.assistant(
            [{"type": "thinking", "thinking": "...", "signature": "sig"}], skill, plugin
        )

    def tool_use(self, name: str, inp: dict, skill=None, plugin=None) -> tuple[str, str]:
        tid = "toolu_" + self._uuid("tu").replace("-", "")[:20]
        uuid = self.assistant(
            [{"type": "tool_use", "id": tid, "name": name, "input": inp,
              "caller": {"type": "direct"}}],
            skill, plugin,
        )
        return uuid, tid

    def tool_result(self, tid: str, content: str = "ok") -> str:
        """Unattributed by construction -- matches every real tool_result seen."""
        uuid = self._uuid("tres")
        rec = self._env(uuid, self.prev_uuid)
        rec.update({
            "promptId": self._uuid("prompt"),
            "type": "user",
            "message": {
                "role": "user",
                "content": [{"type": "tool_result", "tool_use_id": tid,
                             "content": content}],
            },
            "toolUseResult": content,
            "sourceToolAssistantUUID": self.prev_uuid,
        })
        return self._emit(rec)

    def skill_call(self, skill: str, args: str = "") -> str:
        """The activating Skill tool_use. UNATTRIBUTED in real transcripts -- the trap
        for any extractor that counts activations instead of attributions."""
        _, tid = self.tool_use("Skill", {"skill": skill, "args": args})
        self.tool_result(tid, f"Launching skill: {skill}...")
        return tid

    def attachment(self) -> str:
        uuid = self._uuid("att")
        rec = self._env(uuid, self.prev_uuid)
        rec.update({"type": "attachment",
                    "attachment": {"type": "new_directory", "path": CWD}})
        return self._emit(rec)

    def noise(self) -> None:
        """last-prompt / custom-title / ai-title triples appear constantly in real
        transcripts and carry no message at all. An extractor that assumes every
        record has `message` trips here."""
        for t, extra in (
            ("last-prompt", {"lastPrompt": "…", "leafUuid": self.prev_uuid}),
            ("custom-title", {"customTitle": "fixture session"}),
            ("ai-title", {"title": "fixture session"}),
        ):
            uuid = self._uuid("meta")
            rec = self._env(uuid, self.prev_uuid)
            rec.update({"type": t})
            rec.update(extra)
            self.records.append(rec)  # deliberately does NOT advance prev_uuid

    def compact_boundary(self) -> None:
        """Exact shape measured in Photopipe/60247efe line 1815-1816."""
        tail = self.prev_uuid
        uuid = self._uuid("cbound")
        self.records.append({
            "parentUuid": None,
            "logicalParentUuid": tail,
            "isSidechain": False,
            "type": "system",
            "subtype": "compact_boundary",
            "content": "Conversation compacted",
            "isMeta": False,
            "timestamp": self._ts(),
            "uuid": uuid,
            "level": "info",
            "compactMetadata": {
                "trigger": "auto",
                "preTokens": 998579,
                "durationMs": 132801,
                "preservedSegment": {"headUuid": tail, "anchorUuid": tail,
                                     "tailUuid": tail},
            },
            "sessionId": self.session_id,
        })
        suuid = self._uuid("csumm")
        rec = self._env(suuid, uuid)
        rec.update({
            "promptId": self._uuid("prompt"),
            "type": "user",
            "isVisibleInTranscriptOnly": True,
            "isCompactSummary": True,
            "message": {"role": "user",
                        "content": "This session is being continued from a previous "
                                   "conversation that ran out of context. Summary: …"},
        })
        self._emit(rec)

    def raw(self, s: str) -> None:
        """A deliberately unparseable line."""
        self.records.append(s)

    # -- output -------------------------------------------------------------------

    def write(self, out: Path, truncate_tail: bool = False) -> None:
        parts = []
        for r in self.records:
            parts.append(r if isinstance(r, str)
                         else json.dumps(r, ensure_ascii=False, separators=(",", ":")))
        body = "\n".join(parts)
        if truncate_tail:
            # A file cut mid-write: last line is a complete record chopped in half,
            # with NO trailing newline. This is what a killed process leaves behind.
            body += "\n" + parts[-1][: max(40, len(parts[-1]) // 2)]
        else:
            body += "\n"
        # newline="\n" -- writing text on Windows without this doubles CR into CRCRLF.
        with io.open(out / self.filename, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(body)


class _Sentinel:
    def __init__(self, name): self.name = name
    def __repr__(self): return self.name


NULL_SKILL = _Sentinel("NULL_SKILL")
EMPTY_SKILL = _Sentinel("EMPTY_SKILL")


# --------------------------------------------------------------------------------------
# the fixture itself: exactly 12 spans
# --------------------------------------------------------------------------------------


def build(out: Path) -> dict:
    spans: list[dict] = []
    expected_skipped: list[dict] = []

    def span(sid, sess, skill, uuids, activation, ends_open=False,
             straddles=False, note=""):
        spans.append({
            "span_id": sid,
            "session_id": sess.session_id,
            "file": sess.filename,
            "skill": skill,
            "uuids": uuids,
            "first_uuid": uuids[0],
            "last_uuid": uuids[-1],
            "record_count": len(uuids),
            "activation": activation,
            "ends_open": ends_open,
            "straddles_compaction": straddles,
            "note": note,
        })

    # ---- sessA: activation shapes, and two different skills back to back ----------
    A = Session("aaaaaaaa-1111-4aaa-8aaa-aaaaaaaaaaaa", "sessA.jsonl",
                clock_offset_s=0)
    A.human("Set the project up please.")
    A.noise()
    A.thinking()                       # pre-skill, unattributed
    A.skill_call("anthropic-skills:astronomer-start", "stand up the project")

    sk = "anthropic-skills:astronomer-start"
    u = [A.thinking(sk, "anthropic-skills")]
    _, t = A.tool_use("Bash", {"command": "ls"}, sk, "anthropic-skills")
    u.append(_); A.tool_result(t)      # transparent record INSIDE the span
    A.noise()                          # more transparent records
    u.append(A.text("Charter drafted.", sk, "anthropic-skills"))
    span("A1", A, sk, u, "skill_call",
         note="activated by an explicit Skill tool call; the Skill record itself is "
              "unattributed and must not be counted")

    # A2: auto-trigger. No Skill tool call anywhere -- attribution simply begins.
    A.human("Is that actually true?")
    sk = "astronomer-verify"
    u = [A.thinking(sk, None)]
    u.append(A.text("Re-derived from source.", sk, None))
    span("A2", A, sk, u, "auto",
         note="no preceding Skill call; an extractor keyed on activation misses this")

    # A3 / A4: two different skills with NO record between them.
    A.human("Now review the diff.")
    sk3 = "engineering:code-review"
    u3 = [A.thinking(sk3, "engineering"), A.text("Two findings.", sk3, "engineering")]
    sk4 = "engineering:debug"
    u4 = [A.thinking(sk4, "engineering"), A.text("Reproduced.", sk4, "engineering")]
    span("A3", A, sk3, u3, "auto", note="adjacent to A4 with no separator")
    span("A4", A, sk4, u4, "auto",
         note="a different skill on the very next line must open a new span")

    # ---- sessB: compaction, null attribution, same skill twice, a corrupt line ----
    B = Session("bbbbbbbb-2222-4bbb-8bbb-bbbbbbbbbbbb", "sessB.jsonl", branch="feat/x",
                clock_offset_s=3600)
    B.human("Research the landscape.")
    B.skill_call("deep-research", "competitors")
    sk = "deep-research"
    u = [B.thinking(sk, None), B.text("Six sources.", sk, None)]
    B.compact_boundary()               # CONTRACT rule 4: transparent
    u += [B.thinking(sk, None), B.text("Continuing the sweep.", sk, None)]
    span("B1", B, sk, u, "skill_call", straddles=True,
         note="interrupted by a compaction boundary and resumed on the same skill; "
              "ONE span by contract rule 4")

    # B2: a null attributionSkill and an empty-string one sit inside this span.
    B.human("How is the night run doing?")
    sk = "astronomer-supervise"
    u = [B.thinking(sk, None)]
    B.assistant([{"type": "text", "text": "…"}], NULL_SKILL)    # key present, null
    u.append(B.text("Loop is alive.", sk, None))
    B.assistant([{"type": "text", "text": "…"}], EMPTY_SKILL)   # key present, ""
    u.append(B.text("But not progressing.", sk, None))
    span("B2", B, sk, u, "auto",
         note="contains two records whose attributionSkill is present but null/empty; "
              "those are transparent AND must be reported, not dropped in silence")
    expected_null_attribution = 2

    # A corrupt line in a transparent region -- cannot affect any span boundary,
    # which keeps this one variable (L-10).
    B.raw('{"type":"assistant","uuid":"truncated-mid-object","message":{"role":')
    expected_skipped.append({"file": "sessB.jsonl", "reason": "unparseable JSON"})

    # B3: the SAME skill again after a human turn. Contract rule 5 -- a second span.
    B.human("Check it again in ten minutes.")
    sk = "astronomer-supervise"
    u = [B.thinking(sk, None), B.text("Still alive, still stuck.", sk, None)]
    span("B3", B, sk, u, "auto",
         note="same skill as B2; a human turn separates them, so 2 spans not 1. "
              "An extractor that groups by skill-per-session reports 1 here")

    # B4: an ordinary span, so the corrupt line is not the last thing in the file.
    B.human("File it.")
    sk = "behavioral-audit"
    u = [B.thinking(sk, None), B.text("Issue opened.", sk, None)]
    span("B4", B, sk, u, "auto")

    # ---- sessC: ends mid-span ----------------------------------------------------
    C = Session("cccccccc-3333-4ccc-8ccc-cccccccccccc", "sessC.jsonl",
                clock_offset_s=7200)
    C.human("Spawn the feature.")
    C.skill_call("feature-spawn", "")
    sk = "feature-spawn"
    u = [C.thinking(sk, None), C.text("Brief written.", sk, None)]
    span("C1", C, sk, u, "skill_call")

    C.human("Look at the numbers.")
    sk = "data:analyze"
    u = [C.thinking(sk, "data"), C.text("Median is 4.", sk, "data")]
    span("C2", C, sk, u, "auto")

    C.human("Write the spec.")
    sk = "product-management:write-spec"
    u = [C.thinking(sk, "product-management"),
         C.text("Goals and non-goals…", sk, "product-management")]
    span("C3", C, sk, u, "auto", ends_open=True,
         note="the file simply ends here. An open span is still a span (rule 8)")

    # ---- sessD: a file whose final record is physically truncated ----------------
    D = Session("dddddddd-4444-4ddd-8ddd-dddddddddddd", "sessD.jsonl",
                clock_offset_s=10800)
    D.human("Chart it.")
    sk = "dataviz"
    u = [D.thinking(sk, None), D.text("Palette chosen.", sk, None),
         D.text("Legend placed.", sk, None)]
    span("D1", D, sk, u, "auto")
    D.human("thanks")   # this final record is the one the writer chops in half
    expected_skipped.append({"file": "sessD.jsonl", "reason": "truncated final line"})

    # ---- sessE: control. No skills at all. -------------------------------------
    E = Session("eeeeeeee-5555-4eee-8eee-eeeeeeeeeeee", "sessE.jsonl",
                clock_offset_s=14400)
    E.human("Just a chat.")
    E.thinking()
    _, t = E.tool_use("Bash", {"command": "echo hi"})
    E.tool_result(t)
    E.text("Done.")
    E.noise()

    # ---- sessF: a SUBAGENT lane whose user records must NOT close the span -------
    # This case exists because the fixture could not previously express it, and the
    # rule it tests governs 3,315 of the real corpus's 3,404 spans. A subagent's
    # `type: "user"` records are the harness feeding it -- prompts and continuations
    # -- not a person taking a new turn. Treating them as human turns fragmented one
    # continuous activation into per-turn slivers (967 one-record spans, measured).
    # ONE span of four records. Without the sidechain guard the extractor reports THREE.
    F = Session("ffffffff-6666-4fff-8fff-ffffffffffff", "sessF.jsonl",
                clock_offset_s=18000, sidechain=True, agent_id="agent-alpha")
    F.human("Investigate the retry path.")
    sk = "engineering:debug"
    u = [F.thinking(sk, None), F.text("Reading the handler.", sk, None)]
    F.human("continue")
    u.append(F.text("Found the bug.", sk, None))
    F.human("continue")
    u.append(F.text("Proposed a fix.", sk, None))
    span("F1", F, sk, u, "auto",
         note="subagent lane: two sidechain 'user' records sit INSIDE this span and "
              "must be transparent. An extractor closing on any type:user record "
              "reports 3 spans here instead of 1.")

    out.mkdir(parents=True, exist_ok=True)
    for s in (A, B, C, E, F):
        s.write(out)
    D.write(out, truncate_tail=True)

    manifest = {
        "generator": "make-skill-fixture.py",
        "fixture_dir": str(out),
        "contract_version": 1,
        "expected": {
            "span_count": len(spans),
            "files": 6,
            "sessions": 6,
            "skipped_lines": len(expected_skipped),
            "null_attribution_records": expected_null_attribution,
        },
        "expected_skipped_detail": expected_skipped,
        "spans": spans,
        "distinct_skills": sorted({s["skill"] for s in spans}),
    }
    with io.open(out / "MANIFEST.json", "w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    return manifest


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    out = Path(a.out)
    if out.exists():
        shutil.rmtree(out)
    m = build(out)

    if m["expected"]["span_count"] != 13:
        print(f"FIXTURE BUG: built {m["expected"]["span_count"]} spans, wanted 13")
        return 1

    if not a.quiet:
        print(f"fixture written to {out}")
        print(f"  files            : {m['expected']['files']} .jsonl + MANIFEST.json")
        print(f"  spans            : {m['expected']['span_count']}")
        print(f"  skipped lines    : {m['expected']['skipped_lines']} (expected)")
        print(f"  null attribution : {m['expected']['null_attribution_records']}")
        print()
        for s in m["spans"]:
            flag = ("open " if s["ends_open"] else "     ") + \
                   ("compact" if s["straddles_compaction"] else "       ")
            print(f"  {s['span_id']:3} {s['file']:13} {s['activation']:10} {flag} "
                  f"{s['skill']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
