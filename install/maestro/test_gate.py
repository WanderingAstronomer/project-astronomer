#!/usr/bin/env python3
"""
test_gate.py - black-box tests for gate.py, the Maestro routing gate.

Every test writes a fixture registry into a fresh temp directory and runs the gate as a
subprocess, exactly as Claude Code would: JSON on stdin, MAESTRO_REGISTRY in the
environment, verdict read from the exit code and stderr.

The gate under test is MAESTRO_GATE_PATH if set (verify_gate_mutations.py uses this to
point the suite at seeded mutants), else gate.py next to this file.

Usage:  python install/maestro/test_gate.py [-v] [-f]
"""

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.environ.get("MAESTRO_GATE_PATH") or os.path.join(HERE, "gate.py")

ROOT = "C:\\Users\\drew\\Documents\\DevSlop"

# ----------------------------------------------------------------- fixture registry

VOC = {
    "group": "Vociferous Next",
    "slug": "VOC",
    "size": "Orchestra",
    "workspace": ROOT + "\\voc",
    "maestro": {"title": "Maestro (Vociferous Next)", "session": "local_3719027b-aaaa",
                "hook_session": "8c6cf821-aaaa"},
    "conductor": {"title": "Conductor (Vociferous Next)", "session": "local_f7154940-aaaa",
                  "hook_session": "c0nd0001-aaaa"},
    "roster": [
        {"title": "Landing & Review", "session": "local_a44ff87d-aaaa", "role": "lander"},
        {"title": "Section A", "session": "local_5ec7a000-aaaa", "role": "section"},
        {"title": "Cloud Relay", "session": "local_0e3a0000-aaaa", "role": "oneway"},
    ],
    "permits": [],
    "updated": "2026-10-10T00:00Z",
    "some_future_field": {"ignored": True},
}

HEALTH = {
    "group": "Health",
    "slug": "HEALTH",
    "size": "Chamber",
    "workspace": "C:/Users/drew/Documents/DevSlop/health/",
    "maestro": {"title": "Maestro (Health)", "session": "local_4ea17000-bbbb",
                "hook_session": "4ea1h00k-bbbb"},
    # Deliberately non-standard title: "Conductor (Health)" must still resolve by pattern.
    "conductor": {"title": "Health Conductor", "session": "local_4ea1c000-bbbb",
                  "hook_session": "4ea1ch00-bbbb"},
    "roster": [
        {"title": "Landing & Review", "session": "local_4ea11a00-bbbb", "role": "lander"},
        {"title": "Intake", "session": "local_17a4e000-bbbb", "role": "section"},
    ],
    "permits": [],
}

SOLO = {
    "group": "Solo Proj",
    "slug": "SOLO",
    "size": "Solo",
    "workspace": ROOT + "\\solo\\",
    "maestro": {"title": "Maestro (Solo Proj)", "session": "local_5010a000-cccc",
                "hook_session": None},
    "conductor": None,
    "roster": [{"title": "Worker", "session": "local_w0000000-cccc", "role": "section"}],
}

VOCAB = {
    "group": "Vocab",
    "slug": "VOCAB",
    "size": "Chamber",
    "workspace": ROOT + "\\vocab",
    "maestro": {"title": "Maestro (Vocab)", "session": "local_v0cab000-dddd",
                "hook_session": "v0cabh00-dddd"},
    "conductor": {"title": "Conductor (Vocab)", "session": "local_v0cabc00-dddd",
                  "hook_session": None},
    "roster": [],
}

INNER = {
    "group": "Inner",
    "slug": "INNER",
    "size": "Chamber",
    "workspace": ROOT + "\\voc\\inner",
    "maestro": {"title": "Maestro (Inner)", "session": "local_1aa00000-eeee",
                "hook_session": "1aah0000-eeee"},
    "conductor": {"title": "Conductor (Inner)", "session": "local_1aac0000-eeee",
                  "hook_session": None},
    "roster": [{"title": "Inner Section", "session": "local_1aa50000-eeee",
                "role": "section"}],
}

BASE = {"VOC": VOC, "HEALTH": HEALTH, "SOLO": SOLO, "VOCAB": VOCAB, "INNER": INNER}

# Sender identities (cwd, hook session_id).
OUTSIDE = (ROOT + "\\elsewhere\\proj", "0u751de0-ffff")
VOC_MEMBER = (ROOT + "\\voc\\v2\\frontend", "5ec7h00k-aaaa")
VOC_CONDUCTOR = (ROOT + "\\voc", "c0nd0001-aaaa")
VOC_MAESTRO = (ROOT + "\\voc", "8c6cf821-aaaa")
HEALTH_MEMBER = ("C:\\Users\\drew\\Documents\\DevSlop\\health\\api", "17a4h00k-bbbb")
SOLO_MEMBER = (ROOT + "\\solo\\src", "w0rkh00k-cccc")


class GateCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="maestro-gate-test-")
        self.reg = os.path.join(self.tmp, "registry")
        self.home = os.path.join(self.tmp, "home")
        os.makedirs(self.reg)
        os.makedirs(self.home)
        self.groups = copy.deepcopy(BASE)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    # -- helpers

    def write(self, groups=None):
        for slug, data in (groups if groups is not None else self.groups).items():
            with open(os.path.join(self.reg, slug + ".json"), "w", encoding="utf-8") as fh:
                json.dump(data, fh)

    def path_of(self, slug):
        return os.path.join(self.reg, slug + ".json")

    def run_gate(self, payload=None, raw=None, write=True):
        if write:
            self.write()
        env = dict(os.environ)
        env["MAESTRO_REGISTRY"] = self.reg
        env["USERPROFILE"] = self.home
        env["HOME"] = self.home
        env["PYTHONIOENCODING"] = "utf-8"
        data = raw if raw is not None else json.dumps(payload)
        proc = subprocess.run([sys.executable, GATE], input=data.encode("utf-8"),
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env,
                              timeout=60)
        return proc.returncode, proc.stderr.decode("utf-8", "replace"), \
            proc.stdout.decode("utf-8", "replace")

    def send(self, sender, to, tool="SendMessage", **extra):
        cwd, sid = sender
        tool_input = {"to": to, "message": "hi"} if tool == "SendMessage" \
            else {"session_id": to, "message": "hi"}
        payload = {"session_id": sid, "transcript_path": "x.jsonl", "cwd": cwd,
                   "hook_event_name": "PreToolUse", "tool_name": tool,
                   "tool_input": tool_input}
        payload.update(extra)
        return self.run_gate(payload)

    def mcp(self, sender, session_id):
        return self.send(sender, session_id, tool="mcp__ccd_session_mgmt__send_message")

    def assertAllowed(self, result):
        code, err, out = result
        self.assertEqual(code, 0, "expected allow, got block: %s" % err)
        self.assertEqual(err, "", "allow must be silent on stderr")
        self.assertEqual(out, "", "allow must be silent on stdout")
        # A crash also exits 0 (fail open), so an allow only counts if nothing was logged.
        # Without this, a defect that raises looks exactly like a correct allow.
        log = os.path.join(self.home, ".maestro", "gate-errors.log")
        if os.path.exists(log):
            with open(log, encoding="utf-8") as fh:
                self.fail("allow came from the crash path, not a rule: " + fh.read())

    def assertBlocked(self, result, *fragments):
        code, err, _ = result
        self.assertEqual(code, 2, "expected block (exit 2), got %s; stderr=%r" % (code, err))
        self.assertTrue(err.startswith("MAESTRO GATE:"), err)
        for f in fragments:
            self.assertIn(f, err)
        return err


# ----------------------------------------------------------------- tool filtering

class ToolFiltering(GateCase):
    def test_non_message_tool_ignored(self):
        payload = {"session_id": VOC_MEMBER[1], "cwd": VOC_MEMBER[0],
                   "hook_event_name": "PreToolUse", "tool_name": "Bash",
                   "tool_input": {"to": "Maestro (Health)", "command": "ls"}}
        self.assertAllowed(self.run_gate(payload))

    def test_main_allowed(self):
        self.assertAllowed(self.send(VOC_MEMBER, "main"))

    def test_subagent_id_allowed(self):
        self.assertAllowed(self.send(VOC_MEMBER, "a8e39355c84eae9b7"))

    def test_missing_target_allowed(self):
        self.assertAllowed(self.send(VOC_MEMBER, ""))

    def test_mcp_tool_is_governed(self):
        self.assertBlocked(self.mcp(VOC_MEMBER, "Maestro (Vociferous Next)"),
                           "Conductor (Vociferous Next)")


# ----------------------------------------------------------------- name handling

class NameHandling(GateCase):
    def test_ref_suffix_stripped_blocks(self):
        self.assertBlocked(self.send(VOC_MEMBER, "Maestro (Vociferous Next) [4711e6]"),
                           "send this to Conductor (Vociferous Next)")

    def test_ref_suffix_stripped_allows(self):
        self.assertAllowed(self.send(VOC_MEMBER, "Conductor [4711e6]"))
        self.assertAllowed(self.send(VOC_MEMBER, "Conductor (Vociferous Next) [4711e6]"))

    def test_title_match_is_case_insensitive_and_trimmed(self):
        self.assertBlocked(self.send(VOC_MEMBER, "  maestro (vociferous next)  "),
                           "sections don't message the Maestro")

    def test_unresolved_teammate_allowed(self):
        self.assertAllowed(self.send(VOC_MEMBER, "some-teammate"))

    def test_pattern_conductor_resolves_when_title_missing(self):
        # Health's conductor is titled "Health Conductor"; the pattern still finds it.
        err = self.assertBlocked(self.send(VOC_MEMBER, "Conductor (Health)"),
                                 "may not message outside its group")
        self.assertIn("Maestro (Vociferous Next)", err)

    def test_pattern_resolution_case_insensitive(self):
        self.assertBlocked(self.send(OUTSIDE, "conductor (HEALTH)"),
                           "outside sessions may contact only Maestro (Health)")

    def test_pattern_for_unregistered_group_allowed(self):
        # Superseded 2026-10-10: a governed member addressing an unregistered workspace is now
        # blocked (UnregisteredWorkspace). Only a Maestro or an ungoverned sender gets through.
        self.assertAllowed(self.send(VOC_MAESTRO, "Conductor (Nobody Here)"))

    def test_pattern_conductor_at_solo_is_unresolved(self):
        self.assertAllowed(self.send(OUTSIDE, "Conductor (Solo Proj)"))

    def test_title_collision_across_groups_blocks(self):
        # Landing & Review exists in VOC (allowed, same group) and Health (cross-group).
        self.assertBlocked(self.send(VOC_MEMBER, "Landing & Review"),
                           "more than one group", "local_ id")

    def test_collision_resolved_by_local_id(self):
        self.assertAllowed(self.mcp(VOC_MEMBER, "local_a44ff87d-aaaa"))
        self.assertBlocked(self.mcp(VOC_MEMBER, "local_4ea11a00-bbbb"),
                           "may not message outside its group")


# ----------------------------------------------------------------- ungoverned senders

class Ungoverned(GateCase):
    def test_ungoverned_to_ungoverned_allowed(self):
        self.assertAllowed(self.send(OUTSIDE, "My Other Session"))

    def test_ungoverned_to_maestro_allowed(self):
        self.assertAllowed(self.send(OUTSIDE, "Maestro (Vociferous Next)"))
        self.assertAllowed(self.mcp(OUTSIDE, "local_4ea17000-bbbb"))

    def test_ungoverned_to_conductor_blocked(self):
        self.assertBlocked(self.send(OUTSIDE, "Conductor (Vociferous Next)"),
                           "belongs to group Vociferous Next",
                           "outside sessions may contact only Maestro (Vociferous Next)")

    def test_ungoverned_to_member_blocked(self):
        self.assertBlocked(self.send(OUTSIDE, "Intake"), "belongs to group Health")

    def test_no_cwd_is_ungoverned(self):
        payload = {"session_id": "x", "hook_event_name": "PreToolUse",
                   "tool_name": "SendMessage", "tool_input": {"to": "Section A"}}
        self.assertBlocked(self.run_gate(payload), "outside sessions may contact only")

    def test_missing_registry_dir_allows_everything(self):
        shutil.rmtree(self.reg)
        payload = {"session_id": OUTSIDE[1], "cwd": OUTSIDE[0], "tool_name": "SendMessage",
                   "tool_input": {"to": "Conductor (Vociferous Next)"}}
        self.assertAllowed(self.run_gate(payload, write=False))


# ----------------------------------------------------------------- same group

class SameGroup(GateCase):
    def test_section_to_conductor_allowed(self):
        self.assertAllowed(self.send(VOC_MEMBER, "Conductor (Vociferous Next)"))

    def test_section_to_section_allowed(self):
        self.assertAllowed(self.send(VOC_MEMBER, "Section A"))

    def test_section_to_maestro_blocked_when_conductor_exists(self):
        self.assertBlocked(self.send(VOC_MEMBER, "Maestro (Vociferous Next)"),
                           "send this to Conductor (Vociferous Next)",
                           "sections don't message the Maestro")

    def test_conductor_to_maestro_allowed(self):
        self.assertAllowed(self.send(VOC_CONDUCTOR, "Maestro (Vociferous Next)"))

    def test_maestro_to_member_allowed(self):
        self.assertAllowed(self.send(VOC_MAESTRO, "Section A"))

    def test_solo_member_to_maestro_allowed(self):
        self.assertAllowed(self.send(SOLO_MEMBER, "Maestro (Solo Proj)"))

    def test_conductor_identified_by_session_without_prefix(self):
        # hook session id equals conductor.session with local_ stripped, upper-cased.
        # A member would be blocked here; the conductor is not.
        self.assertAllowed(self.send((VOC_CONDUCTOR[0], "F7154940-AAAA"),
                                     "Maestro (Vociferous Next)"))


# ----------------------------------------------------------------- cross group

class UnregisteredWorkspace(GateCase):
    """A workspace with no registry row is still another workspace (found 2026-10-10)."""

    def test_member_to_unregistered_maestro_blocked(self):
        self.assertBlocked(self.send(VOC_MEMBER, "Maestro (Nowhere Yet)"),
                           "may not message outside its group")

    def test_conductor_to_unregistered_conductor_blocked(self):
        self.assertBlocked(self.send(VOC_CONDUCTOR, "Conductor (Nowhere Yet)"),
                           "the conductor of Vociferous Next")

    def test_maestro_to_unregistered_maestro_allowed(self):
        self.assertAllowed(self.send(VOC_MAESTRO, "Maestro (Nowhere Yet)"))

    def test_ungoverned_to_unregistered_allowed(self):
        self.assertAllowed(self.send(OUTSIDE, "Conductor (Nowhere Yet)"))

    def test_member_to_own_group_pattern_not_blocked_by_this_rule(self):
        self.assertAllowed(self.send(VOC_MEMBER, "Conductor (Vociferous Next)"))


class CrossGroup(GateCase):
    def test_maestro_to_maestro_allowed(self):
        self.assertAllowed(self.send(VOC_MAESTRO, "Maestro (Health)"))
        self.assertAllowed(self.mcp(VOC_MAESTRO, "local_4ea17000-bbbb"))

    def test_maestro_to_other_conductor_blocked_without_permit(self):
        self.assertBlocked(self.send(VOC_MAESTRO, "Conductor (Health)"),
                           "permit from the operator", self.path_of("VOC"))

    def test_maestro_to_other_conductor_allowed_with_permit(self):
        self.groups["VOC"]["permits"] = [{"id": "P-1", "to": "conductor (health)",
                                          "topic": "x", "granted": "2026-10-10T06:00Z",
                                          "ends": "when X-4 closes"}]
        self.assertAllowed(self.send(VOC_MAESTRO, "Conductor (Health)"))

    def test_permit_by_target_title_reaches_by_session_id(self):
        self.groups["VOC"]["permits"] = [{"id": "P-2", "to": "Intake", "ended": False}]
        self.assertAllowed(self.mcp(VOC_MAESTRO, "local_17a4e000-bbbb"))

    def test_permit_by_session_id(self):
        self.groups["VOC"]["permits"] = [{"id": "P-3", "to": "local_17a4e000-bbbb",
                                          "ended": None}]
        self.assertAllowed(self.send(VOC_MAESTRO, "Intake"))

    def test_permit_for_other_target_does_not_cover(self):
        self.groups["VOC"]["permits"] = [{"id": "P-4", "to": "Intake"}]
        self.assertBlocked(self.send(VOC_MAESTRO, "Conductor (Health)"), "permit")

    def test_permit_ended_blocks(self):
        self.groups["VOC"]["permits"] = [{"id": "P-5", "to": "Conductor (Health)",
                                          "ended": True}]
        self.assertBlocked(self.send(VOC_MAESTRO, "Conductor (Health)"),
                           "permit from the operator")

    def test_permit_in_target_file_does_not_count(self):
        self.groups["HEALTH"]["permits"] = [{"id": "P-6", "to": "Health Conductor"}]
        self.assertBlocked(self.send(VOC_MAESTRO, "Health Conductor"), "permit")

    def test_conductor_to_other_maestro_blocked(self):
        err = self.assertBlocked(self.send(VOC_CONDUCTOR, "Maestro (Health)"),
                                 "the conductor of Vociferous Next",
                                 "may not message outside its group",
                                 "ask Maestro (Vociferous Next) to raise an exchange")
        self.assertNotIn("hook_session", err)

    def test_member_to_other_maestro_blocked_with_hint(self):
        self.assertBlocked(self.send(VOC_MEMBER, "Maestro (Health)"),
                           "a member of Vociferous Next", "may not message outside its group",
                           "set maestro.hook_session in", self.path_of("VOC"), VOC_MEMBER[1])

    def test_member_to_other_member_blocked_without_hint(self):
        err = self.assertBlocked(self.send(HEALTH_MEMBER, "Section A"),
                                 "a member of Health may not message outside its group")
        self.assertNotIn("hook_session", err)

    def test_maestro_identified_via_prefixed_hook_session(self):
        self.groups["VOC"]["maestro"]["hook_session"] = "LOCAL_8C6CF821-AAAA"
        self.assertAllowed(self.send(VOC_MAESTRO, "Maestro (Health)"))

    def test_maestro_identified_via_session_field(self):
        self.groups["VOC"]["maestro"]["hook_session"] = None
        self.assertAllowed(self.send((VOC_MAESTRO[0], "3719027b-aaaa"), "Maestro (Health)"))

    def test_stale_hook_session_falls_to_member(self):
        self.assertBlocked(self.send((VOC_MAESTRO[0], "new-session-after-restart"),
                                     "Maestro (Health)"),
                           "set maestro.hook_session", "new-session-after-restart")


# ----------------------------------------------------------------- paths

class Paths(GateCase):
    def test_nested_workspace_deepest_wins(self):
        inner = (ROOT + "\\voc\\inner\\pkg", "1aa5h000-eeee")
        self.assertBlocked(self.send(inner, "Conductor (Vociferous Next)"),
                           "a member of Inner may not message outside its group")
        self.assertAllowed(self.send(inner, "Conductor (Inner)"))

    def test_prefix_boundary_unregistered_sibling(self):
        sibling = (ROOT + "\\vocother\\proj", "s1b00000")
        self.assertBlocked(self.send(sibling, "Conductor (Vociferous Next)"),
                           "outside sessions may contact only")

    def test_prefix_boundary_vocab_vs_voc(self):
        vocab = (ROOT + "\\vocab\\x", "v0cab5ec")
        self.assertBlocked(self.send(vocab, "Section A"),
                           "a member of Vocab may not message outside its group")
        self.assertAllowed(self.send(vocab, "Conductor (Vocab)"))

    def test_path_case_insensitive(self):
        shouting = ("c:\\USERS\\Drew\\documents\\DEVSLOP\\VOC\\Sub", "x")
        self.assertAllowed(self.send(shouting, "Conductor (Vociferous Next)"))
        self.assertBlocked(self.send(shouting, "Maestro (Vociferous Next)"),
                           "send this to Conductor")

    def test_forward_slashes_and_trailing_separator(self):
        fwd = ("C:/Users/drew/Documents/DevSlop/voc/", "x")
        self.assertBlocked(self.send(fwd, "Maestro (Vociferous Next)"),
                           "send this to Conductor")
        health_root = ("C:\\Users\\drew\\Documents\\DevSlop\\health", "x")
        self.assertAllowed(self.send(health_root, "Health Conductor"))


# ----------------------------------------------------------------- registry robustness

class RegistryRobustness(GateCase):
    def test_non_json_files_ignored(self):
        with open(os.path.join(self.reg, "notes.txt"), "w") as fh:
            fh.write("{ not json")
        with open(os.path.join(self.reg, "VOC.json.bak"), "w") as fh:
            fh.write("{ not json")
        self.assertAllowed(self.send(VOC_MEMBER, "Conductor (Vociferous Next)"))

    def test_malformed_with_workspace_blocks_sender_inside(self):
        bad = {"group": "Broken", "workspace": ROOT + "\\broken"}  # no maestro
        self.groups["BROKEN"] = bad
        self.assertBlocked(self.send((ROOT + "\\broken\\x", "s"), "anyone at all"),
                           "malformed", self.path_of("BROKEN"))

    def test_malformed_unparseable_workspace_recovered(self):
        self.write()
        with open(self.path_of("TORN"), "w", encoding="utf-8") as fh:
            fh.write('{"group": "Torn", "workspace": "C:\\\\Users\\\\drew\\\\Documents'
                     '\\\\DevSlop\\\\torn", "maestro": {"title": ')
        payload = {"session_id": "s", "cwd": ROOT + "\\torn\\sub",
                   "tool_name": "SendMessage", "tool_input": {"to": "x"}}
        self.assertBlocked(self.run_gate(payload, write=False), "malformed",
                           self.path_of("TORN"))

    def test_malformed_does_not_block_unrelated_sender(self):
        self.groups["BROKEN"] = {"group": "Broken", "workspace": ROOT + "\\broken"}
        self.assertAllowed(self.send(VOC_MEMBER, "Conductor (Vociferous Next)"))

    def test_malformed_without_workspace_allows_silently(self):
        self.write()
        with open(self.path_of("JUNK"), "w") as fh:
            fh.write("this is not json at all")
        payload = {"session_id": OUTSIDE[1], "cwd": OUTSIDE[0],
                   "tool_name": "SendMessage", "tool_input": {"to": "whoever"}}
        self.assertAllowed(self.run_gate(payload, write=False))
        # The well-formed groups are still enforced.
        payload["tool_input"]["to"] = "Conductor (Vociferous Next)"
        self.assertBlocked(self.run_gate(payload, write=False), "outside sessions")

    def test_malformed_sender_may_still_reach_main(self):
        self.groups["BROKEN"] = {"group": "Broken", "workspace": ROOT + "\\broken"}
        self.assertAllowed(self.send((ROOT + "\\broken", "s"), "main"))

    def test_unknown_fields_ignored(self):
        self.groups["VOC"]["roster"].append({"title": "Extra", "role": "outlier",
                                             "colour": "teal", "session": None})
        self.assertAllowed(self.send(VOC_MEMBER, "Extra"))
        self.assertBlocked(self.send(OUTSIDE, "Extra"), "belongs to group Vociferous Next")


# ----------------------------------------------------------------- never crash

class NeverCrash(GateCase):
    def test_stdin_not_json_allows_and_logs(self):
        code, err, out = self.run_gate(raw="this is { not json")
        self.assertEqual((code, err, out), (0, "", ""))
        log = os.path.join(self.home, ".maestro", "gate-errors.log")
        self.assertTrue(os.path.isfile(log), "expected an error log line")
        with open(log, encoding="utf-8") as fh:
            self.assertIn("JSONDecodeError", fh.read())

    def test_payload_not_an_object_allows(self):
        self.assertEqual(self.run_gate(raw="[1, 2, 3]")[:2], (0, ""))

    def test_tool_input_wrong_shape_allows(self):
        payload = {"session_id": "s", "cwd": VOC_MEMBER[0], "tool_name": "SendMessage",
                   "tool_input": "Maestro (Vociferous Next)"}
        self.assertEqual(self.run_gate(payload)[:2], (0, ""))


if __name__ == "__main__":
    unittest.main()
