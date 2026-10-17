#!/usr/bin/env python3
"""
verify_gate_mutations.py - proves test_gate.py can fail.

A test suite that passes says nothing until it has been seen to fail against a broken gate.
This copies gate.py into a temp directory, seeds one defect at a time by exact string
replacement, and runs test_gate.py against each mutant (via MAESTRO_GATE_PATH). Every
mutant must make at least one test fail.

The verifier itself fails when:
  - the unmutated gate does not pass the suite (a red baseline would "catch" everything);
  - a replacement target is not found exactly once in gate.py (an edit to the gate that
    moves the target must not let a mutant silently become a no-op);
  - any mutant survives (the suite passes against it).

Usage:  python install/maestro/verify_gate_mutations.py
Exit:   0 baseline green and every mutant caught · 1 otherwise
"""

import os
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(HERE, "gate.py")
TESTS = os.path.join(HERE, "test_gate.py")

# (name, target string in gate.py, replacement)
MUTANTS = [
    ("conductor hook_session hint dropped (O-71)",
     '"conductor.hook_session in %s is %s; set it to %s."',
     '"(hint removed %s %s %s)."'),
    ("unregistered workspaces not governed (pattern rule dropped)",
     '        if (m and s_group is not None and sr != "maestro"\n',
     '        if (False and m and s_group is not None and sr != "maestro"\n'),
    ("cross-group check disabled (everyone treated as same group)",
     "    same_group = s_group is tg\n",
     "    same_group = True\n"),
    ("prefix-boundary check dropped (voc contains vocab)",
     'prefix = ws if ws.endswith("/") else ws + "/"',
     "prefix = ws"),
    ("permit 'ended' ignored",
     'if not p.get("ended") and (',
     "if ("),
    ("ungoverned sender allowed everywhere",
     '    if s_group is None:\n        if tr == "maestro":',
     "    if s_group is None:\n        if True:"),
    ("nested workspaces: shallowest wins instead of deepest",
     'return max(inside, key=lambda g: len(g["workspace"]))',
     'return min(inside, key=lambda g: len(g["workspace"]))'),
    ("paths compared case-sensitively",
     "    return p.lower()\n",
     "    return p\n"),
    ("title collision blocks only when every match blocks",
     "        if any(reasons):",
     "        if all(reasons):"),
    ("ref suffix not stripped",
     'name = REF_SUFFIX_RE.sub("", name).strip()',
     "name = name.strip()"),
    ("'Maestro|Conductor (Group)' pattern resolution removed",
     "    m = ROLE_TITLE_RE.match(name.strip())\n",
     "    m = None\n"),
    ("mcp send_message not governed",
     'GOVERNED_TOOLS = ("SendMessage", "mcp__ccd_session_mgmt__send_message")',
     'GOVERNED_TOOLS = ("SendMessage",)'),
    ("Solo exemption dropped (sections blocked from Maestro with no conductor)",
     ' and tg["conductor"] is not None:',
     ":"),
    ("sections-to-Maestro rule removed",
     'if sr == "member" and tr == "maestro" and tg["conductor"]',
     'if False and tg["conductor"]'),
    ("Maestro-to-Maestro cross-group allowance removed",
     '        if tr == "maestro":\n            return None\n        if has_live_permit',
     "        if has_live_permit"),
    ("unexpected exceptions crash instead of allowing",
     "    except BaseException:\n        log_error()\n        code = 0\n",
     "    except BaseException:\n        raise\n"),
    ("malformed registry files ignored",
     "    if held:\n",
     "    if False:\n"),
    ("local_ prefix not normalised in session ids",
     '    if s.startswith("local_"):\n',
     "    if False:\n"),
    ("hook_session self-heal hint dropped",
     '    if sr == "member" and tr == "maestro":\n        reason +=',
     "    if False:\n        reason +="),
    ("subagent ids and 'main' governed like titles",
     'if name.lower() == "main" or AGENT_ID_RE.match(name):',
     "if False:"),
]


def run_suite(gate_path):
    env = dict(os.environ)
    env["MAESTRO_GATE_PATH"] = gate_path
    proc = subprocess.run([sys.executable, TESTS, "-f"], stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, env=env, timeout=600)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def first_failure(output):
    for line in output.splitlines():
        if line.startswith(("FAIL:", "ERROR:")):
            return line
    return "(no FAIL/ERROR line found)"


def main():
    with open(GATE, encoding="utf-8") as fh:
        source = fh.read()

    problems = []
    code, out = run_suite(GATE)
    if code != 0:
        print("BASELINE RED: the unmutated gate fails the suite; nothing below means anything.")
        print(out)
        return 1
    print("baseline: unmutated gate passes the suite")

    work = tempfile.mkdtemp(prefix="maestro-gate-mutants-")
    jobs = []
    try:
        for i, (name, target, repl) in enumerate(MUTANTS, 1):
            count = source.count(target)
            if count != 1:
                problems.append("mutant %d (%s): target found %d times, expected 1"
                                % (i, name, count))
                continue
            d = os.path.join(work, "m%02d" % i)
            os.makedirs(d)
            path = os.path.join(d, "gate.py")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(source.replace(target, repl))
            jobs.append((i, name, path))

        with ThreadPoolExecutor(max_workers=min(8, os.cpu_count() or 4)) as pool:
            results = list(pool.map(lambda j: (j, run_suite(j[2])), jobs))
    finally:
        shutil.rmtree(work, ignore_errors=True)

    caught = 0
    for (i, name, _), (code, out) in results:
        if code != 0:
            caught += 1
            print("  caught   %2d  %s\n                %s" % (i, name, first_failure(out)))
        else:
            problems.append("mutant %d (%s): SURVIVED, the suite passed against it"
                            % (i, name))
            print("  SURVIVED %2d  %s" % (i, name))

    print("\n%d of %d mutants caught" % (caught, len(MUTANTS)))
    for p in problems:
        print("VERIFIER FAILURE: " + p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
