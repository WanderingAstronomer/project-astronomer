#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify-skill-census.py -- the falsifier for the transcript skill extractor.

PRE-REGISTERED CRITERION (written before the extractor existed, non-negotiable)
------------------------------------------------------------------------------
    Given a synthetic fixture containing exactly 12 known skill spans, the extractor
    must report exactly 12. With 3 of those spans deleted from the fixture, it must
    report exactly 9 AND the output must be specific enough to NAME WHICH THREE ARE
    MISSING. If it reports 12 in both cases, the extractor is reporting rather than
    measuring and nothing downstream may use it.

The second clause is the one with teeth. A span COUNT cannot name three missing spans;
only per-span identity can. An extractor that emits `{"span_count": 9}` and nothing else
fails here on purpose -- it has proved it can subtract, not that it can see.

WHY A FALSIFIER AT ALL
----------------------
L-9: the falsifier is written first. L-12: a check that cannot fail as it matters proves
nothing. The extractor's clean run on real transcripts is unfalsifiable -- nobody knows
the true skill-span count of the real corpus, which is the entire reason the extractor is
being built. So the extractor's clean output MAY NOT BE BELIEVED until it has been
observed going RED against known truth. This script is what makes it go red.

AND THIS SCRIPT IS ITSELF A CHECK, so `--selftest` breaks IT on purpose. It runs the whole
suite twice: once against an honest reference extractor (must go green) and once against a
LIAR that hardcodes the entire correct baseline answer without ever opening the input
(must go red), and once against a COUNTER that measures honestly but emits no per-span
identity (must also go red). A suite that greenlights the liar has no teeth, and
`--selftest` is how that is discovered without waiting for the real tool.

THE SEEDED DEFECTS
------------------
Each runs on a FRESH copy of the fixture; mutations never accumulate (L-10, one variable).

  D1  delete 3 spans: A1 (activated by a Skill call), B1 (straddles a compaction
      boundary), B2 (the FIRST of two same-skill spans in one session)
                                    -> count must be 9, and the 3 must be NAMEABLE
  D2  corrupt attributionSkill      -> must be REPORTED, never silently dropped
  D3  truncate a file mid-record    -> a skipped line, not a crash
  D4  duplicate a session's file    -> must not double-count within a session
  D5  empty root                    -> must report 0. Catches a hardcoded constant.
  D6  strip all attribution in one  -> must report 8. Catches a count keyed on files
      file                             or on Skill tool calls rather than attribution.

B2 rather than an easier third span on purpose: it is one of TWO `astronomer-supervise`
spans, so an extractor whose only per-span identity is the skill NAME, or a positional
index that re-numbers after a deletion, names the wrong survivor and is caught.

D5 and D6 exist because D1 alone can be passed by an extractor that counts the wrong
thing correctly. D1 deletes records; D6 deletes only the ATTRIBUTION while leaving every
record, including the Skill tool calls, in place -- so an extractor that counts
activations instead of attributions survives D1 and dies here.

THE EXTRACTOR CONTRACT
----------------------
Two interfaces are accepted. Stdout forms are tried first, in order:
    python skill-census.py --root DIR --json
    python skill-census.py --json --root DIR
    python skill-census.py DIR --json
    python skill-census.py --input DIR --json
    python skill-census.py --root DIR

If none yields JSON, FILE-OUTPUT mode is tried -- NDJSON spans plus a JSON summary:
    python skill-census.py --root DIR --out spans.ndjson --summary summary.json                            --progress 0
which is what scratchpad/skill-census.py implements. Summary keys are also looked up
inside nested `run` / `totals` blocks.

Stdout must carry ONE JSON object. Leading log noise is tolerated; the last
brace-balanced object in stdout is used. Required and optional keys, with the aliases
this verifier accepts, so a concurrently written tool is not failed on spelling:

    spans / skill_spans / results        REQUIRED. list of span objects.
      .session_id / sessionId / session  REQUIRED on each span.
      .skill / attributionSkill / name   REQUIRED on each span.
      .first_uuid / firstUuid /          A DELETION-STABLE identity is REQUIRED for D1
        start_uuid / uuid                  to be passable -- it is what lets three
      .start_ts / start_timestamp          missing spans be named. Either key works.
                                           A file+record ORDINAL is deliberately not
                                           accepted: ordinals shift when a line is
                                           removed, which is exactly what D1 does.
                                           Identity is compared file-qualified, because
                                           a bare start_ts is not unique across files.
      .file / path / source              optional.
      .record_count / records / n        optional.
      .activation                        optional: "skill_call" | "auto".
      .ends_open                         optional bool.
    span_count / total_spans / count     optional; defaults to len(spans).
    skipped_lines / skipped / errors     REQUIRED for D3. list or int.
    anomalies / malformed                REQUIRED for D2 (or a skipped_lines entry that
                                         names the offending file). list or int.
    null_attribution_records /           optional but checked at baseline if present.
      null_attribution

Semantics are defined in make-skill-fixture.py's CONTRACT block (rules 1-10) and are NOT
negotiable by aliasing. The load-bearing ones: unattributed records are transparent; a
human turn ends a span; a compaction boundary does not; records dedupe by
(sessionId, uuid); an open span at EOF still counts.

Usage:
    python verify-skill-census.py                    # auto-locates ./skill-census.py
    python verify-skill-census.py --extractor PATH
    python verify-skill-census.py --selftest         # prove THIS script can go red
    python verify-skill-census.py --diagnose         # span definition differs; probe anyway

Exit codes:
    0  every seeded defect was caught
    1  a seeded defect slipped through  <-- the extractor has no teeth, do not use it
    2  the extractor failed the baseline (clean fixture != 12), so nothing else is
       meaningful and the defects were not run. `--diagnose` runs them anyway, with
       the absolute count assertions suspended and every relative one still binding;
       a green --diagnose is NOT the criterion being met.
    3  the extractor is not present or emits no parseable JSON. THE END-TO-END RUN IS
       OWED. This is not a pass and must never be reported as one.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
GENERATOR = HERE / "make-skill-fixture.py"
DEFAULT_EXTRACTOR = HERE / "skill-census.py"

INVOCATIONS = [
    ["--root", "{d}", "--json"],
    ["--json", "--root", "{d}"],
    ["{d}", "--json"],
    ["--input", "{d}", "--json"],
    ["--root", "{d}"],
    ["{d}"],
]


# --------------------------------------------------------------------------------------
# running the extractor and normalising whatever it says
# --------------------------------------------------------------------------------------


class ExtractorError(RuntimeError):
    pass


def _last_json_object(text: str):
    """Tolerate log noise around the payload: return the last brace-balanced object."""
    try:
        return json.loads(text)
    except Exception:
        pass
    starts = [m.start() for m in re.finditer(r"\{", text)]
    for i in reversed(starts):
        depth, instr, esc = 0, False, False
        for j in range(i, len(text)):
            ch = text[j]
            if instr:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    instr = False
                continue
            if ch == '"':
                instr = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[i:j + 1])
                    except Exception:
                        break
    raise ExtractorError("no parseable JSON object on stdout")


def _pick(d: dict, *names, default=None):
    """Look for any of `names` at the top level, then inside the conventional nested
    blocks (`run`, `totals`) that a file-writing extractor uses for its summary."""
    for n in names:
        if n in d and d[n] is not None:
            return d[n]
    for block in ("run", "totals", "summary"):
        sub = d.get(block)
        if isinstance(sub, dict):
            for n in names:
                if n in sub and sub[n] is not None:
                    return sub[n]
    return default


def _as_count(v) -> int:
    if v is None:
        return 0
    if isinstance(v, int):
        return v
    if isinstance(v, (list, tuple, dict)):
        return len(v)
    return 0


class Report:
    """Normalised view of one extractor run."""

    def __init__(self, raw: dict, argv: list, stdout: str, stderr: str, rc: int):
        self.raw, self.argv, self.stdout, self.stderr, self.rc = raw, argv, stdout, stderr, rc
        spans = _pick(raw, "spans", "skill_spans", "results", default=None)
        if spans is None or not isinstance(spans, list):
            raise ExtractorError(
                "output has no `spans` list (aliases: skill_spans, results). A bare "
                "count cannot name which spans are missing, which the criterion requires."
            )
        self.spans = []
        for s in spans:
            if not isinstance(s, dict):
                raise ExtractorError("a span entry is not an object")
            self.spans.append({
                "session_id": _pick(s, "session_id", "sessionId", "session"),
                "skill": _pick(s, "skill", "attributionSkill", "name"),
                "first_uuid": _pick(s, "first_uuid", "firstUuid", "start_uuid", "uuid"),
                "start_ts": _pick(s, "start_ts", "start_timestamp", "startTs",
                                  "first_timestamp"),
                "file": _pick(s, "file", "path", "source"),
                "record_count": _pick(s, "record_count", "records", "n"),
                "activation": _pick(s, "activation"),
                "ends_open": _pick(s, "ends_open", "endsOpen", default=False),
            })
        self.count = _pick(raw, "span_count", "total_spans", "count", "spans",
                           default=len(self.spans))
        if isinstance(self.count, list):
            self.count = len(self.count)
        if not isinstance(self.count, int):
            self.count = len(self.spans)
        self.skipped = _pick(raw, "skipped_lines", "skipped", "errors",
                             "lines_skipped_total", "lines_unparseable", default=[])
        self.skipped_n = _as_count(self.skipped)
        self.anomalies = _pick(raw, "anomalies", "malformed", "malformed_attribution",
                               "lines_malformed", default=[])
        self.anomalies_n = _as_count(self.anomalies)
        self.null_attr = _pick(raw, "null_attribution_records", "null_attribution",
                               default=None)

    # -- span identity -------------------------------------------------------------
    # D1 demands the three missing spans be NAMEABLE, so each span needs a key that
    # SURVIVES the deletion of other spans. Three candidates, in descending order of
    # strength:
    #   first_uuid  -- stable under any edit elsewhere in the file.
    #   start_ts    -- equally stable; the fixture gives every record a distinct stamp.
    #   (session, skill, nth) -- DEGRADED. It re-indexes when a same-skill span is
    #                   deleted, so it names the wrong survivor. D1 deletes B2, the
    #                   FIRST of two `astronomer-supervise` spans, precisely so that a
    #                   tool relying on this is caught rather than flattered.
    # A file+ordinal key (e.g. start_record) is deliberately NOT accepted: record
    # ordinals shift the moment a line is removed, which is exactly what D1 does.

    @property
    def identity_kind(self) -> str:
        if self.spans and all(s["first_uuid"] for s in self.spans):
            return "first_uuid"
        if self.spans and all(s["start_ts"] for s in self.spans):
            return "start_ts"
        return "none"

    @property
    def has_identity(self) -> bool:
        return self.identity_kind != "none"

    def identities(self) -> set:
        """File-qualified. A bare start_ts is NOT unique across files -- two sessions
        recorded at the same wall-clock time collide, and the fixture caught exactly
        that collision in this function on its first real run."""
        k = self.identity_kind
        if k == "none":
            return set()
        return {(s["file"] or "", s[k]) for s in self.spans}

    def skill_pairs(self):
        from collections import Counter
        return Counter((s["session_id"], s["skill"]) for s in self.spans)

    def mentions_file(self, name: str) -> bool:
        """Only the DIAGNOSTIC channels count. Searching the whole payload matches a
        per-skill `files` roster and turns D2 into a false fire -- which it did on the
        first real run against skill-census.py."""
        return (name in json.dumps(self.skipped)
                or name in json.dumps(self.anomalies))


def _run_file_mode(extractor: Path, root: Path, timeout: int) -> Report:
    """Some extractors write NDJSON spans + a JSON summary to FILES instead of stdout
    (skill-census.py does). That is a fine interface; only the semantics are fixed. Drive
    it into a scratch dir and rebuild the same normalised Report from the two files."""
    tmp = Path(tempfile.mkdtemp(prefix="skill-census-out-"))
    spans_p, summ_p = tmp / "spans.ndjson", tmp / "summary.json"
    argv = [sys.executable, str(extractor), "--root", str(root),
            "--out", str(spans_p), "--summary", str(summ_p), "--progress", "0"]
    try:
        p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout,
                           env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    except subprocess.TimeoutExpired:
        raise ExtractorError(f"file-output mode timed out after {timeout}s")
    if not spans_p.exists() and not summ_p.exists():
        raise ExtractorError(
            f"file-output mode wrote neither {spans_p.name} nor {summ_p.name} "
            f"(rc={p.returncode}); stderr: {p.stderr.strip()[:300]}")
    spans = []
    if spans_p.exists():
        with io.open(spans_p, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    spans.append(json.loads(line))
    raw = {}
    if summ_p.exists():
        raw = json.loads(summ_p.read_text(encoding="utf-8"))
    raw["spans"] = spans
    # `summary.totals.spans` is the extractor's own count; keep it authoritative so a
    # disagreement between its count and its span list is visible rather than papered
    # over by len(spans).
    return Report(raw, argv, p.stdout, p.stderr, p.returncode)


def run_extractor(extractor: Path, root: Path, timeout: int = 180) -> Report:
    last_err = None
    for form in INVOCATIONS:
        argv = [sys.executable, str(extractor)] + [a.format(d=str(root)) for a in form]
        try:
            p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=timeout,
                               env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        except subprocess.TimeoutExpired:
            last_err = f"timed out after {timeout}s"
            continue
        try:
            raw = _last_json_object(p.stdout)
        except ExtractorError as e:
            last_err = f"{e} (rc={p.returncode})"
            continue
        try:
            return Report(raw, argv, p.stdout, p.stderr, p.returncode)
        except ExtractorError as e:
            raise ExtractorError(f"{e}\n  argv: {' '.join(argv)}")
    try:
        return _run_file_mode(extractor, root, timeout)
    except ExtractorError as e:
        raise ExtractorError(
            f"no stdout form produced JSON (last: {last_err}); file-output mode also "
            f"failed: {e}")


# --------------------------------------------------------------------------------------
# fixture handling and the mutations
# --------------------------------------------------------------------------------------


def build_fixture(dest: Path) -> dict:
    p = subprocess.run([sys.executable, str(GENERATOR), "--out", str(dest), "--quiet"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    if p.returncode != 0:
        raise RuntimeError(f"fixture generator failed:\n{p.stdout}\n{p.stderr}")
    return json.loads((dest / "MANIFEST.json").read_text(encoding="utf-8"))


def _rewrite(path: Path, fn):
    """Map fn over parsed lines. fn returns a dict to keep, or None to delete.
    Unparseable lines are passed through verbatim -- the fixture's corrupt line must
    survive every mutation."""
    out = []
    with io.open(path, encoding="utf-8") as fh:
        raw = fh.read()
    trailing_nl = raw.endswith("\n")
    for line in raw.split("\n"):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except Exception:
            out.append(line)
            continue
        r = fn(rec)
        if r is not None:
            out.append(json.dumps(r, ensure_ascii=False, separators=(",", ":")))
    body = "\n".join(out) + ("\n" if trailing_nl else "")
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body)


def mut_delete_spans(fix: Path, man: dict, span_ids) -> dict:
    targets = {s["span_id"]: s for s in man["spans"] if s["span_id"] in span_ids}
    kill = {u for s in targets.values() for u in s["uuids"]}
    for f in {s["file"] for s in targets.values()}:
        _rewrite(fix / f, lambda r: None if r.get("uuid") in kill else r)
    return targets


def mut_corrupt_attribution(fix: Path, man: dict, span_id: str) -> dict:
    s = next(x for x in man["spans"] if x["span_id"] == span_id)
    kill = set(s["uuids"])

    def f(r):
        if r.get("uuid") in kill and "attributionSkill" in r:
            # A structurally wrong value, not merely an unknown name. Nothing may
            # coerce this into a skill name and carry on.
            r["attributionSkill"] = {"name": s["skill"], "corrupted": True}
        return r

    _rewrite(fix / s["file"], f)
    return s


def mut_truncate(fix: Path, name: str, keep_fraction: float = 0.55) -> int:
    p = fix / name
    data = p.read_bytes()
    cut = int(len(data) * keep_fraction)
    # land mid-record: walk forward off any newline so the last line is half a record
    while cut < len(data) and data[cut:cut + 1] == b"\n":
        cut += 1
    p.write_bytes(data[:cut])
    return cut


def mut_duplicate(fix: Path, name: str, as_name: str) -> None:
    shutil.copyfile(fix / name, fix / as_name)


def mut_strip_attribution(fix: Path, name: str) -> None:
    def f(r):
        r.pop("attributionSkill", None)
        r.pop("attributionPlugin", None)
        return r

    _rewrite(fix / name, f)


# --------------------------------------------------------------------------------------
# the suite
# --------------------------------------------------------------------------------------


class Suite:
    def __init__(self, extractor: Path, workdir: Path, verbose: bool = False,
                 diagnose: bool = False):
        self.extractor, self.workdir, self.verbose = extractor, workdir, verbose
        # diagnose: the extractor disagrees with the fixture's span DEFINITION, so the
        # absolute "must be 12 / must be 9" assertions are not applicable. Every
        # assertion that does not depend on the absolute count still runs and still
        # gives a real verdict -- which is what answers "is it measuring at all?".
        self.diagnose = diagnose
        self.results: list[tuple[str, bool, str]] = []
        self.baseline_count = None
        self.baseline_anomalies = 0
        self.baseline_by_file = {}
        self.baseline_identities = set()
        self.span_identity = {}
        self._i = 0

    def _fresh(self, tag: str):
        self._i += 1
        d = self.workdir / f"{self._i:02d}-{tag}"
        return d, build_fixture(d)

    def _record(self, defect: str, caught: bool, detail: str):
        self.results.append((defect, caught, detail))
        if caught:
            print(f"FIRED   {defect}")
        else:
            print(f"MISSED  {defect}   <-- seeded defect went unnoticed")
        for ln in detail.strip().splitlines():
            print(f"        {ln}")
        print()

    # -- baseline -----------------------------------------------------------------

    def baseline(self) -> bool:
        d, man = self._fresh("baseline")
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            print(f"BASELINE FAILED: {e}")
            return False
        exp = man["expected"]["span_count"]
        self.baseline_count = rep.count
        ok = rep.count == exp and len(rep.spans) == exp
        if self.diagnose and not ok:
            print(f"[DIAG] baseline: clean fixture -> {rep.count} spans "
                  f"(fixture contains {exp}) -- span DEFINITION differs; absolute "
                  f"assertions are suspended, relative ones still bind")
        else:
            print(f"[{'PASS' if ok else 'FAIL'}] baseline: clean fixture -> "
                  f"{rep.count} spans (expected {exp})")
        print(f"        invocation      : {' '.join(rep.argv[1:])}")
        print(f"        per-span identity: "
              f"{'yes' if rep.has_identity else 'NO -- D1 cannot be passed'}")
        print(f"        skipped lines   : {rep.skipped_n} "
              f"(fixture contains {man['expected']['skipped_lines']})")
        if rep.null_attr is not None:
            print(f"        null attribution: {rep.null_attr} "
                  f"(fixture contains {man['expected']['null_attribution_records']})")
        from collections import Counter
        if not ok:
            got = Counter(s["skill"] or "?" for s in rep.spans)
            want_c = Counter(s["skill"] for s in man["spans"])
            print(f"        reported skills : {sorted(got.elements())}")
            print(f"        fixture skills  : {sorted(want_c.elements())}")
            for k in sorted(set(got) | set(want_c)):
                if got[k] != want_c[k]:
                    print(f"        DIFFERS: {k!r} reported {got[k]}x, "
                          f"fixture has {want_c[k]}x")
            if not self.diagnose:
                return False
        # The count being right by luck is worth ruling out: the skills must match too.
        elif Counter(s["skill"] for s in rep.spans) != Counter(
                s["skill"] for s in man["spans"]):
            print("[FAIL] baseline: right COUNT, wrong SKILLS -- that is a coincidence, "
                  "not a measurement")
            print(f"        reported: {sorted(s['skill'] or '?' for s in rep.spans)}")
            print(f"        expected: {sorted(s['skill'] for s in man['spans'])}")
            return False
        self.baseline_identities = rep.identities()
        self.baseline_anomalies = rep.anomalies_n
        from collections import Counter as _C
        self.baseline_by_file = dict(_C(s["file"] for s in rep.spans if s["file"]))
        # Pair each fixture span to whatever identity THIS extractor uses for it, so a
        # later "which three vanished" is asked in the extractor's own vocabulary.
        # Pairing on (session, skill, nth-in-session) is safe HERE and only here: the
        # fixture is intact, so both sides list the same spans in the same order.
        self.span_identity = {}
        if rep.has_identity:
            seen = {}
            key_to_ident = {}
            for s in rep.spans:
                k = (s["session_id"], s["skill"])
                seen[k] = seen.get(k, -1) + 1
                key_to_ident[(k[0], k[1], seen[k])] = (s["file"] or "",
                                                       s[rep.identity_kind])
            seen = {}
            for m in man["spans"]:
                k = (m["session_id"], m["skill"])
                seen[k] = seen.get(k, -1) + 1
                ident = key_to_ident.get((k[0], k[1], seen[k]))
                if ident is not None:
                    self.span_identity[m["span_id"]] = ident
            if len(self.span_identity) != len(man["spans"]):
                msg = (f"paired {len(self.span_identity)}/{len(man['spans'])} fixture "
                       f"spans to extractor spans by (session, skill, occurrence)")
                if not self.diagnose:
                    print(f"[FAIL] baseline: could not pair every fixture span -- {msg}")
                    return False
                print(f"        {msg}")
        print()
        return True

    # -- D1 -----------------------------------------------------------------------

    def d1_delete_three(self):
        name = ("D1 delete 3 spans (A1 skill_call, B1 compaction-straddling, "
                "B2 first of two same-skill spans)")
        d, man = self._fresh("d1")
        targets = mut_delete_spans(d, man, {"A1", "B1", "B2"})
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            return self._record(name, False, f"extractor produced nothing usable: {e}")

        if rep.count == self.baseline_count:
            return self._record(
                name, False,
                f"reported {rep.count} both before and after 3 spans were deleted. "
                f"THIS IS THE PRE-REGISTERED FAILURE: it is reporting, not measuring.")
        # The criterion is "exactly three fewer, and name them" -- RELATIVE to the
        # baseline, not the constant 9. It was written as 9 when the fixture held 12
        # spans; adding the subagent case made the fixture 13 and the constant then
        # failed a CORRECT extractor reporting 10. The assertion is unchanged in
        # substance and must not be loosened further: three deleted means three fewer.
        expect_after = self.baseline_count - 3
        if not self.diagnose and rep.count != expect_after:
            return self._record(name, False,
                                f"reported {rep.count}; the criterion demands exactly {expect_after}")

        # The count is right. Now the harder half: can the three be NAMED?
        if not rep.has_identity:
            return self._record(name, False,
                                "reported 9 but emitted no deletion-stable per-span "
                                "identity (first_uuid or start_ts), so the three "
                                "missing spans cannot be named. A count that can "
                                "subtract is not a measurement.")
        missing = self.baseline_identities - rep.identities()
        want = {self.span_identity[sid] for sid in targets
                if sid in self.span_identity}
        if len(want) != len(targets):
            return self._record(name, False,
                                "could not resolve the deleted spans in the "
                                "extractor's own identity vocabulary")
        if self.diagnose:
            # Relative form: every deleted span MUST have disappeared. Extra churn is
            # allowed here only because a differing span definition legitimately
            # reshapes neighbours (a merged span loses its head and re-forms).
            survived = want & rep.identities()
            if survived:
                return self._record(
                    name, False,
                    f"{len(survived)} of the 3 deleted spans is still being reported: "
                    f"{sorted(survived)}")
            extra = (missing - want)
            return self._record(
                name, True,
                f"{self.baseline_count} -> {rep.count}; all three deleted spans are "
                f"absent:\n  " +
                ", ".join(f"{s['span_id']} ({s['skill']})"
                          for s in sorted(targets.values(), key=lambda x: x["span_id"])) +
                (f"\n  {len(extra)} further span identity/ies also changed, consistent "
                 f"with the differing span definition" if extra else "") +
                "\n  RELATIVE VERDICT ONLY: the absolute '9' is not asserted because the "
                "baseline count is disputed.")
        if missing != want:
            return self._record(
                name, False,
                "reported 9, but the three that vanished are not the three deleted.\n"
                f"  deleted  : {sorted(s['span_id'] for s in targets.values())}\n"
                f"  vanished : {sorted(missing)}\n"
                f"  expected : {sorted(want)}")
        named = ", ".join(f"{s['span_id']} ({s['skill']})"
                          for s in sorted(targets.values(), key=lambda x: x["span_id"]))
        self._record(name, True,
                     f"12 -> 9, and the three absent spans are exactly:\n  {named}")

    # -- D2 -----------------------------------------------------------------------

    def d2_corrupt_attribution(self):
        name = "D2 corrupt the attributionSkill field on one span (A2)"
        d, man = self._fresh("d2")
        s = mut_corrupt_attribution(d, man, "A2")
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            return self._record(name, False, f"crashed or produced nothing: {e}")
        if rep.count == self.baseline_count:
            return self._record(name, False,
                                f"still reported {rep.count} -- it coerced a JSON object "
                                f"into a skill name, or never looked at the value's type")
        # The fixture already contains 2 malformed lines, so "anomalies > 0" is true
        # before the corruption is seeded. The signal is the anomaly level RISING, or
        # the offending FILE being named in a diagnostic channel.
        reported = (rep.anomalies_n > self.baseline_anomalies
                    or rep.mentions_file(s["file"]))
        if not reported:
            return self._record(
                name, False,
                f"reported {rep.count} (the span is gone) but surfaced NOTHING: no "
                f"anomaly above the baseline {self.baseline_anomalies}, no "
                f"skipped-line entry naming {s['file']}. A silent drop is "
                f"the false-success defect class (L-16) -- the census would read clean "
                f"while missing a span.")
        self._record(name, True,
                     f"span count {rep.count} (was {self.baseline_count}) and the "
                     f"malformed record was REPORTED: anomalies "
                     f"{self.baseline_anomalies} -> {rep.anomalies_n}, "
                     f"file named in a diagnostic channel="
                     f"{rep.mentions_file(s['file'])}")

    # -- D3 -----------------------------------------------------------------------

    def d3_truncate(self):
        name = "D3 truncate sessB.jsonl mid-record"
        d, man = self._fresh("d3")
        mut_truncate(d, "sessB.jsonl")
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            return self._record(name, False,
                                f"did not survive a truncated file: {e}\n"
                                f"  a half-written line must be a skipped line, "
                                f"not a crash")
        if rep.rc != 0:
            return self._record(name, False,
                                f"exited {rep.rc} on a truncated file; expected a clean "
                                f"run with the bad line reported")
        if rep.skipped_n < 1:
            return self._record(name, False,
                                "survived but reported ZERO skipped lines -- the "
                                "truncated record vanished without a trace")
        # Ask in the extractor's OWN identity vocabulary, not the fixture's uuids --
        # the two only coincide when the extractor happens to key on uuid.
        untouched = {self.span_identity[s["span_id"]] for s in man["spans"]
                     if s["file"] in {"sessA.jsonl", "sessC.jsonl", "sessD.jsonl"}
                     and s["span_id"] in self.span_identity}
        if rep.has_identity:
            lost = untouched - rep.identities()
            if lost:
                return self._record(name, False,
                                    f"a truncated sessB cost {len(lost)} spans in files "
                                    f"that were never touched: {sorted(lost)}")
        self._record(name, True,
                     f"survived (rc=0), reported {rep.skipped_n} skipped line(s), "
                     f"span count {rep.count}, and all "
                     f"{len(untouched)} spans in untouched files are intact")

    # -- D4 -----------------------------------------------------------------------

    def d4_duplicate(self):
        name = "D4 duplicate a session across two files (sessA.jsonl copied)"
        d, man = self._fresh("d4")
        mut_duplicate(d, "sessA.jsonl", "sessA-backup-copy.jsonl")
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            return self._record(name, False, f"produced nothing usable: {e}")
        if self.baseline_count and rep.count == 2 * self.baseline_count:
            return self._record(name, False,
                                f"reported {rep.count}: every span was counted twice. "
                                "Records must dedupe by (sessionId, uuid) -- otherwise "
                                "any backup copy under the scan root inflates the census.")
        if rep.count != self.baseline_count:
            return self._record(name, False,
                                f"reported {rep.count}; a duplicate file must leave the "
                                f"count at {self.baseline_count}")
        self._record(name, True,
                     f"still {rep.count} with the session present twice on disk -- "
                     f"deduped by "
                     "(sessionId, uuid) as the contract requires\n"
                     "  NOTE: this assertion is 'the count did NOT change', so a "
                     "constant-reporting extractor passes it vacuously. D5 is its "
                     "complement and is what actually rules that out.")

    # -- D5 -----------------------------------------------------------------------

    def d5_empty_root(self):
        name = "D5 empty root (no transcripts at all)"
        d = self.workdir / "05-empty"
        d.mkdir(parents=True, exist_ok=True)
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            return self._record(name, False,
                                f"could not report an empty root: {e}\n"
                                f"  zero input must yield zero spans, not an error and "
                                f"not a constant")
        if rep.count != 0:
            return self._record(name, False,
                                f"reported {rep.count} spans from a directory containing "
                                f"no files. The number is not coming from the input.")
        self._record(name, True, "0 spans from 0 files")

    # -- D6 -----------------------------------------------------------------------

    def d6_strip_attribution(self):
        name = "D6 strip every attributionSkill from sessA (records and Skill calls stay)"
        d, man = self._fresh("d6")
        mut_strip_attribution(d, "sessA.jsonl")
        try:
            rep = run_extractor(self.extractor, d)
        except ExtractorError as e:
            return self._record(name, False, f"produced nothing usable: {e}")
        if rep.count == self.baseline_count:
            return self._record(
                name, False,
                f"reported {rep.count} with sessA's attribution entirely removed. Every "
                "record, "
                "including the Skill tool call, is still there -- so this counts "
                "activations, files or records, NOT attribution. D1 alone would not "
                "have caught this.")
        want_n = self.baseline_count - self.baseline_by_file.get("sessA.jsonl", 4)
        if rep.count != want_n:
            return self._record(name, False,
                                f"reported {rep.count}; the baseline put "
                                f"{self.baseline_by_file.get('sessA.jsonl', 4)} spans in "
                                f"sessA, so {want_n} should remain")
        if rep.has_identity:
            gone = {s["first_uuid"] for s in man["spans"] if s["file"] == "sessA.jsonl"}
            if gone & rep.identities():
                return self._record(name, False,
                                    "reported 8 but some sessA span is still listed")
        self._record(name, True,
                     f"{self.baseline_count} -> {rep.count}; every sessA span is gone "
                     f"even though every record and the Skill tool call remain")

    # -- driver -------------------------------------------------------------------

    def run(self) -> int:
        print(f"extractor : {self.extractor}")
        print(f"fixtures  : {self.workdir}")
        print(f"generator : {GENERATOR}\n")
        if not self.baseline():
            print("The baseline did not hold, so a later red proves nothing about the "
                  "defects. Seeded defects NOT run.")
            return 2
        for fn in (self.d1_delete_three, self.d2_corrupt_attribution, self.d3_truncate,
                   self.d4_duplicate, self.d5_empty_root, self.d6_strip_attribution):
            fn()
        caught = sum(1 for _, ok, _ in self.results if ok)
        total = len(self.results)
        print("-" * 72)
        print(f"{caught}/{total} seeded defects caught")
        if caught == total:
            print("Every seeded defect fired. The extractor has been observed FAILING "
                  "on known-bad input, so its clean result on real transcripts may now "
                  "be believed to the extent this fixture models them.")
            return 0
        print("A seeded defect slipped through. The extractor is REPORTING, not "
              "measuring; nothing downstream may use its output.")
        return 1


# --------------------------------------------------------------------------------------
# --selftest: prove this suite can go red, using stub extractors
# --------------------------------------------------------------------------------------

HONEST = r'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reference implementation of the extractor contract. Written ONLY as an oracle for
verify-skill-census.py --selftest. It is not the deliverable and is not tuned for the
real corpus. Its purpose is to show the contract is satisfiable, so that a red result
from the real extractor is a statement about the real extractor."""
import argparse, io, json, os, sys
from pathlib import Path

def human_turn(rec):
    if rec.get("type") != "user":
        return False
    # A compaction summary is type="user" with STRING content -- indistinguishable from
    # a human turn on shape alone. Without this line every compaction-straddling span
    # splits in two. The fixture caught exactly this bug in this very function on the
    # falsifier's first run; the real extractor is likely to have it too.
    if rec.get("isCompactSummary") or rec.get("isVisibleInTranscriptOnly"):
        return False
    # A SUBAGENT lane has no human in it. Its type="user" records are the harness
    # feeding the agent -- a prompt, a continuation -- and closing a span on them
    # fragments one continuous activation into per-turn slivers. Measured on the real
    # corpus before this line existed: 3,174 of 3,404 spans closed on a "human turn",
    # 3,315 of them in subagent lanes, 967 of them a single record long.
    if rec.get("isSidechain"):
        return False
    c = (rec.get("message") or {}).get("content")
    if isinstance(c, str):
        return True
    if isinstance(c, list):
        return not any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c)
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?")
    ap.add_argument("--root", dest="root_kw")
    ap.add_argument("--input", dest="root_in")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = Path(a.root_kw or a.root_in or a.root or ".")

    spans, skipped, anomalies = [], [], []
    seen, nulls, dups = set(), 0, 0

    for path in sorted(root.glob("*.jsonl")):
        cur = None
        pending = None
        def close(open_end=False):
            nonlocal cur
            if cur:
                cur["ends_open"] = open_end
                spans.append(cur)
                cur = None
        with io.open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception as e:
                    skipped.append({"file": path.name, "line": ln,
                                    "reason": "unparseable JSON: %s" % e})
                    continue
                key = (rec.get("sessionId"), rec.get("uuid"))
                if key[1] is not None:
                    if key in seen:
                        dups += 1
                        continue
                    seen.add(key)

                if human_turn(rec):
                    close(); pending = None
                    continue

                skill = None
                if rec.get("type") == "assistant" and "attributionSkill" in rec:
                    v = rec["attributionSkill"]
                    if v is None or v == "":
                        nulls += 1
                    elif not isinstance(v, str):
                        anomalies.append({"file": path.name, "line": ln,
                                          "reason": "attributionSkill is %s, not a string"
                                                    % type(v).__name__})
                    else:
                        skill = v

                if skill is None:
                    # remember an activating Skill call so activation can be labelled
                    m = rec.get("message") or {}
                    for b in (m.get("content") or []):
                        if isinstance(b, dict) and b.get("type") == "tool_use" \
                                and b.get("name") == "Skill":
                            pending = (b.get("input") or {}).get("skill")
                    continue

                if cur and cur["skill"] == skill:
                    cur["record_count"] += 1
                    cur["last_uuid"] = rec.get("uuid")
                else:
                    close()
                    cur = {"session_id": rec.get("sessionId"), "skill": skill,
                           "file": path.name, "first_uuid": rec.get("uuid"),
                           "last_uuid": rec.get("uuid"), "record_count": 1,
                           "activation": "skill_call" if pending == skill else "auto",
                           "ends_open": False}
                    pending = None
        close(open_end=True)

    out = {"spans": spans, "span_count": len(spans), "skipped_lines": skipped,
           "anomalies": anomalies, "null_attribution_records": nulls,
           "duplicate_records": dups,
           "files_scanned": len(list(root.glob("*.jsonl"))),
           "sessions": len({s["session_id"] for s in spans})}
    sys.stdout.write(json.dumps(out, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    sys.exit(main())
'''

LIAR = r'''#!/usr/bin/env python3
"""A deliberately dishonest extractor: it NEVER OPENS THE INPUT. It hardcodes the
baseline answer -- the right count, the right skills, the right session ids -- so it
sails through the baseline looking flawless. It is the strongest form of the adversary
the criterion was written against: a tool that reports instead of measuring, and whose
report happens to be correct exactly once. If the suite greenlights this, the suite is
decoration."""
import json, sys
A = "aaaaaaaa-1111-4aaa-8aaa-aaaaaaaaaaaa"
B = "bbbbbbbb-2222-4bbb-8bbb-bbbbbbbbbbbb"
C = "cccccccc-3333-4ccc-8ccc-cccccccccccc"
D = "dddddddd-4444-4ddd-8ddd-dddddddddddd"
PAIRS = [(A, "anthropic-skills:astronomer-start"), (A, "astronomer-verify"),
         (A, "engineering:code-review"), (A, "engineering:debug"),
         (B, "deep-research"), (B, "astronomer-supervise"),
         (B, "astronomer-supervise"), (B, "behavioral-audit"),
         (C, "feature-spawn"), (C, "data:analyze"),
         (C, "product-management:write-spec"), (D, "dataviz")]
spans = [{"session_id": s, "skill": k, "first_uuid": "fake-%02d" % i,
          "start_ts": "2026-08-27T09:00:%02d.000Z" % i,
          "file": "sess.jsonl", "record_count": 2, "activation": "auto"}
         for i, (s, k) in enumerate(PAIRS)]
sys.stdout.write(json.dumps({"spans": spans, "span_count": 12, "skipped_lines": [],
                             "anomalies": []}))
'''

COUNTER = r'''#!/usr/bin/env python3
"""Honest arithmetic, no identity. It genuinely reads the input and genuinely gets the
count and the skill names right, so it sails through the baseline and through D1's first
half -- and dies on D1's second half, because a list of skill names cannot say WHICH
three spans vanished when two of the twelve share a name. That is why the criterion has
a second half."""
import argparse, io, json, sys
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("root", nargs="?")
ap.add_argument("--root", dest="rk"); ap.add_argument("--input", dest="ri")
ap.add_argument("--json", action="store_true"); a = ap.parse_args()
root = Path(a.rk or a.ri or a.root or ".")
found = []
for p in sorted(root.glob("*.jsonl")):
    cur = None
    for line in io.open(p, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except Exception: continue
        c = (r.get("message") or {}).get("content")
        if r.get("type") == "user" and not r.get("isCompactSummary") and (
                isinstance(c, str) or (isinstance(c, list) and not any(
                    isinstance(b, dict) and b.get("type") == "tool_result" for b in c))):
            if cur: found.append(cur)
            cur = None; continue
        s = r.get("attributionSkill") if r.get("type") == "assistant" else None
        if not isinstance(s, str) or not s: continue
        if cur != s:
            if cur: found.append(cur)
            cur = s
    if cur: found.append(cur)
sys.stdout.write(json.dumps(
    {"spans": [{"skill": s} for s in found], "span_count": len(found),
     "skipped_lines": [], "anomalies": []}))
'''


def selftest(workdir: Path) -> int:
    stubs = workdir / "stubs"
    stubs.mkdir(parents=True, exist_ok=True)
    # want_green: only exit 0 is acceptance. A refusal at the baseline (2) and a
    # refusal at a seeded defect (1) are both refusals, and which one a bad extractor
    # earns is not the point being proved here.
    cases = [
        ("honest reference extractor", HONEST, True,
         "implements the contract; must go GREEN or the contract is unsatisfiable"),
        ("LIAR: hardcodes the whole baseline answer, never reads input", LIAR, False,
         "must be REFUSED -- this is the pre-registered failure mode"),
        ("COUNTER: correct count and skills, no deletion-stable identity", COUNTER,
         False,
         "must be REFUSED -- a count cannot name which three spans went missing"),
    ]
    overall = 0
    for label, src, want_green, why in cases:
        stub = stubs / (label.split(":")[0].replace(" ", "_") + ".py")
        with io.open(stub, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(src)
        print("=" * 72)
        print(f"SELFTEST  {label}")
        print(f"          expect {'ACCEPT' if want_green else 'REFUSE'} -- {why}")
        print("=" * 72)
        wd = workdir / ("st-" + stub.stem)
        wd.mkdir(parents=True, exist_ok=True)
        rc = Suite(stub, wd).run()
        got_green = rc == 0
        ok = got_green == want_green
        print(f"\n>>> exit {rc} = {'ACCEPTED' if got_green else 'REFUSED'} "
              f"(wanted {'ACCEPT' if want_green else 'REFUSE'}) -- "
              f"{'as expected' if ok else 'WRONG'}\n")
        if not ok:
            overall = 1
    print("=" * 72)
    if overall == 0:
        print("SELFTEST PASSED: this suite goes green on an honest extractor and RED on "
              "both a liar and a count-only extractor. It discriminates.")
    else:
        print("SELFTEST FAILED: this suite does not discriminate and must not be used "
              "to clear the real extractor.")
    return overall


def main() -> int:
    ap = argparse.ArgumentParser(description="falsifier for the transcript skill extractor")
    ap.add_argument("--extractor", default=str(DEFAULT_EXTRACTOR))
    ap.add_argument("--workdir", default=None,
                    help="where fixtures are built (default: a temp dir, kept on failure)")
    ap.add_argument("--selftest", action="store_true",
                    help="break this suite on purpose against stub extractors")
    ap.add_argument("--diagnose", action="store_true",
                    help="the extractor uses a different SPAN DEFINITION and so cannot "
                         "hit 12. Suspend the absolute count assertions and run every "
                         "baseline-relative one, to answer 'is it measuring at all?'. "
                         "A green --diagnose run is NOT a pass against the criterion.")
    a = ap.parse_args()

    if not GENERATOR.exists():
        print(f"missing fixture generator: {GENERATOR}")
        return 3

    keep = a.workdir is not None
    wd = Path(a.workdir) if keep else Path(tempfile.mkdtemp(prefix="verify-skill-census-"))
    wd.mkdir(parents=True, exist_ok=True)
    try:
        if a.selftest:
            return selftest(wd)
        ex = Path(a.extractor)
        if not ex.exists():
            print(f"EXTRACTOR NOT PRESENT: {ex}")
            print()
            print("The end-to-end run is OWED. This is not a pass and must not be")
            print("recorded as one. The fixture and this suite are built and their own")
            print("--selftest demonstrates they discriminate; what has NOT been shown is")
            print("anything about the real extractor, because it does not exist yet.")
            print()
            print("Re-run as:  python verify-skill-census.py --extractor <path>")
            return 3
        rc = Suite(ex, wd, diagnose=a.diagnose).run()
        if a.diagnose:
            print()
            print("DIAGNOSTIC RUN. The pre-registered criterion asserts an absolute")
            print("12 -> 9 and was NOT evaluated here. This run answers only the weaker")
            print("question: does the output move with the input? A --diagnose exit 0")
            print("must never be recorded as the criterion having been met.")
        return rc
    finally:
        if not keep:
            print(f"\n(fixtures were built under {wd})")


if __name__ == "__main__":
    sys.exit(main())
