#!/usr/bin/env python3
"""
check-corpus.py — the corpus self-check gate.

WHY THIS EXISTS (the incident is the description; see rituals/recurring-defect.md):

  Twice, a vocabulary in this corpus shipped with more than one membership.

  First: AMENDS D-015. The confidence vocabulary went out with THREE different memberships
  — four tokens in one table, five in the ledger, six in another table — within hours of
  writing L-14, the law that says a vocabulary has exactly one home. Two reviewers found it
  independently. The amendment closed with: "Under L-17 a third recurrence demands a gate
  rather than a third correction ... Not built. next: build it if the drift recurs."

  Second: D-019 promoted `append-only` to a record class in its own right. Ten sites across
  the corpus went on enumerating three classes for four days. One of them, the
  astronomer-start skill, did not merely omit the fourth class — it instructed the reader
  "do not invent a fourth," which would have put a new project's ledger in the wrong class
  on day one.

  That is the recurrence. This is the gate. Per L-17, the fix for a defect CLASS is a
  mechanism, not a third hand-fix: every hand-fix in the source corpus drifted back.

  The guard is intentional. Fix the cause; do not switch off the check.

THE CHECKS (this header is itself the drift class it guards -- it read "FOUR CHECKS" while
listing four, for as long as there were four, and then stopped being true. tools/ is exempt
from the counted-prose check, so nothing but a reader catches it.)

  1. vocabularies — every registered token set has one home containing every member, and
     every tight enumeration of it anywhere in the corpus carries the full membership.
  2. install manifest — the skill directories on disk match both places that list them.
     Nothing else detects an omission, and adding a skill requires lockstep edits in three
     files.
  3. links — every relative markdown link resolves from the file it appears in, including
     its #anchor.
  4. attestation — every law carries a grade, the grade matches the number of independent
     source projects behind it, and anything below `settled` states what would raise it.
     Checks 1-3 ask whether the documents agree with each other. This one asks whether the
     corpus meets the promotion standard it published for itself, and it was added because
     they disagreed: the charter defined one source and three, twelve of eighteen laws sat
     at two, and the counts lived only in a frozen file that cannot carry a correction.
  5. header blocks — every living and append-only file carries the block from
     05-the-record.md; record_class and confidence come from the registry; CONFIRMED obliges
     verified_by and last_verified; no two documents claim the same owns: key.
  6. ID collisions — no D- or O- address is allocated twice, an AMENDS names a decision that
     exists, and the entry pattern still matches something (a check that has gone blind
     reports zero collisions, which reads exactly like a clean corpus).
  7. template carries — rules that bite at SESSION time live in the always-loaded file, not
     only in install/README.md, which is read once and never again (D-044).

WHAT THIS CANNOT CATCH — stated, not hidden:
  - A vocabulary that is not in tools/vocabularies.json. Adding a token set to the corpus
    without registering it here is invisible to this gate.
  - Drift stated in prose rather than as a tight list ("the three classes are ...").
  - Vocabularies marked check_enumerations:false in the registry, each with its reason.
  - Whether a source project listed in provenance/attestation.json ACTUALLY arrived at the
    rule independently. That judgement was made once, by a reader who could see all four
    corpora, and is not re-derivable here. A wrongly-credited source passes silently.
  Run with --verbose to print every exemption taken. Silence is not coverage.

Usage:  python tools/check-corpus.py [--verbose]
Exit:   0 all checks pass · 1 one or more failures
"""

import json
import re
import sys
from pathlib import Path

# The corpus is UTF-8 throughout; Windows consoles frequently are not. Report in ASCII and
# force a UTF-8 stream so a snippet quoted out of a doctrine file cannot crash the gate.
# A check that dies on its own output is worse than no check: it fails loudly for the wrong
# reason and teaches you to ignore it.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "tools" / "vocabularies.json"

VERBOSE = "--verbose" in sys.argv or "-v" in sys.argv

failures: list[str] = []
exemptions: list[str] = []


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts:
            continue
        yield p


def fail(msg: str) -> None:
    failures.append(msg)


def exempt(msg: str) -> None:
    exemptions.append(msg)


# ---------------------------------------------------------------- check 1

BOUND_L = r"(?<![A-Za-z0-9_-])"
BOUND_R = r"(?![A-Za-z0-9_-])"
# Members may be wrapped in backticks and/or bold/italic markers.
WRAP = r"[`*_]{0,3}"
# A separator is a LIST separator only. Prose between two members means it is a sentence,
# not an enumeration, and this gate deliberately does not police sentences. The trailing
# (?:or |and )? catches natural-language lists: "a, b, c, or d".
SEP = r"\s*[·|,/]\s*(?:or |and )?"

NUMWORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}


def as_int(word: str):
    w = word.lower()
    return NUMWORDS.get(w, int(w) if w.isdigit() else None)


# A run must carry at least this many members before it counts as an enumeration.
# Two members side by side is a COMPARISON ("the Operator / Coordinator boundary",
# "frozen, append-only"); three or more is a LIST. Every real drift this gate was built
# for was 3-of-4, 4-of-6, or 5-of-6 — never 2. Set to 2 and the output is almost entirely
# prose pairs, which is how a check gets ignored and then switched off.
MIN_RUN = 3


def check_vocabularies(registry: dict) -> None:
    for vocab in registry["vocabularies"]:
        name = vocab["name"]
        members = vocab["members"]
        home = vocab["home"]
        cased = vocab.get("case_sensitive", True)
        flags = 0 if cased else re.IGNORECASE

        # -- 1a. the home file must contain every member
        if vocab.get("check_home", True):
            home_path = ROOT / home
            if not home_path.exists():
                fail(f"[vocab:{name}] declared home does not exist: {home}")
                continue
            text = home_path.read_text(encoding="utf-8", errors="replace")
            missing = [
                m for m in members
                if not re.search(BOUND_L + re.escape(m) + BOUND_R, text, flags)
            ]
            if missing:
                fail(
                    f"[vocab:{name}] home {home} is missing member(s): "
                    f"{', '.join(missing)}"
                )
        else:
            exempt(
                f"[vocab:{name}] home-membership NOT checked — "
                f"{vocab.get('unchecked_reason', 'no reason given')}"
            )

        # -- 1a-bis. counted prose: "recognizes three classes" when there are four.
        # This is the gap that let the D-019 drift survive: doctrine/05-the-record.md said
        # "Astronomer recognizes three classes" in a sentence, directly above a table
        # listing four, and no list-shaped check could see it. A sentence that counts a
        # vocabulary is asserting its membership just as firmly as a list is.
        for noun in vocab.get("count_nouns", []):
            expected = len(members)
            # (?<![.\d]) — a section number is not a count. Without it "### 5.1 Ownership
            # classes" matched on the "1" of "5.1" and the gate reported prose counting one
            # record_class. doctrine/00-precedence.md: a gate producing a false positive is a
            # defect in the gate, and "the guard is intentional" does not licence a wrong
            # guard. Digit-word counts ("three") are unaffected; only a digit glued to a
            # preceding period or digit is excluded.
            count_re = re.compile(
                r"(?<![.\d])\b(" + "|".join(NUMWORDS) + r"|\d{1,2})\s+"
                r"(?:[A-Za-z][A-Za-z-]*\s+){0,2}?" + re.escape(noun) + r"\b",
                re.IGNORECASE,
            )
            for path in md_files():
                r = rel(path)
                if r in {e["file"] for e in vocab.get("exempt_files", [])}:
                    continue
                if r.startswith("tools/"):
                    continue  # the gate's own prose describes the defect it checks for
                text = path.read_text(encoding="utf-8", errors="replace")
                for match in count_re.finditer(text):
                    n = as_int(match.group(1))
                    if n is None or n == expected:
                        continue
                    line_no = text.count("\n", 0, match.start()) + 1
                    fail(
                        f"[vocab:{name}] {r}:{line_no} prose counts {n} "
                        f"'{noun}', registry has {expected}\n"
                        f"    -> {' '.join(match.group(0).split())}"
                    )

        # -- 1b. every tight enumeration anywhere must carry the full membership
        if not vocab.get("check_enumerations", True):
            exempt(
                f"[vocab:{name}] enumerations NOT checked - "
                f"{vocab.get('unchecked_reason', 'no reason given')}"
            )
            continue

        if len(members) < MIN_RUN:
            exempt(
                f"[vocab:{name}] enumerations NOT checked - only {len(members)} members, "
                f"below the {MIN_RUN}-member threshold that separates a list from a "
                f"comparison. Membership consistency here is a manual review item."
            )
            continue

        alt = "|".join(re.escape(m) for m in sorted(members, key=len, reverse=True))
        tok = f"{WRAP}(?:{alt}){WRAP}"
        run_re = re.compile(BOUND_L + tok + f"(?:{SEP}{tok})+", flags)
        member_re = re.compile(BOUND_L + f"(?:{alt})" + BOUND_R, flags)

        allowed = {a["file"]: a["reason"] for a in vocab.get("allowed_subsets", [])}
        exempt_files = {e["file"]: e["reason"] for e in vocab.get("exempt_files", [])}

        for path in md_files():
            r = rel(path)
            if r == "tools/vocabularies.json":
                continue
            if r in exempt_files:
                exempt(f"[vocab:{name}] {r} exempt — {exempt_files[r]}")
                continue

            text = path.read_text(encoding="utf-8", errors="replace")
            for match in run_re.finditer(text):
                found_raw = member_re.findall(match.group(0))
                found = {f if cased else f.lower() for f in found_raw}
                full = {m if cased else m.lower() for m in members}
                if found == full or len(found) < MIN_RUN:
                    continue
                line_no = text.count("\n", 0, match.start()) + 1
                if r in allowed:
                    exempt(
                        f"[vocab:{name}] {r}:{line_no} subset allowed — {allowed[r]}"
                    )
                    continue
                missing = sorted(full - found)
                snippet = " ".join(match.group(0).split())[:70]
                fail(
                    f"[vocab:{name}] {r}:{line_no} enumerates "
                    f"{len(found)}/{len(full)}, missing: {', '.join(missing)}\n"
                    f"    -> {snippet}"
                )


# ---------------------------------------------------------------- check 2

def check_install_manifest() -> None:
    skills_dir = ROOT / "install" / "skills"
    if not skills_dir.is_dir():
        fail("[manifest] install/skills/ does not exist")
        return

    on_disk = {
        d.name for d in skills_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    }
    no_skill_md = {
        d.name for d in skills_dir.iterdir()
        if d.is_dir() and not (d / "SKILL.md").exists()
    }
    for d in sorted(no_skill_md):
        fail(f"[manifest] install/skills/{d}/ has no SKILL.md")

    readme = ROOT / "install" / "README.md"
    in_readme = set(
        re.findall(r"\.claude/skills/([a-z0-9-]+)/SKILL\.md",
                   readme.read_text(encoding="utf-8", errors="replace"))
    )

    template = ROOT / "install" / "CLAUDE.md.template"
    in_template = set(
        re.findall(r"`(astronomer-[a-z0-9-]+)`",
                   template.read_text(encoding="utf-8", errors="replace"))
    )

    for label, listed in (("install/README.md", in_readme),
                          ("install/CLAUDE.md.template", in_template)):
        for missing in sorted(on_disk - listed):
            fail(f"[manifest] skill '{missing}' exists on disk but is not listed in {label}")
        for phantom in sorted(listed - on_disk):
            fail(f"[manifest] {label} lists skill '{phantom}' which does not exist on disk")


# ---------------------------------------------------------------- check 4

def check_attestation(registry: dict) -> None:
    """Every law carries a grade, and the grade matches the evidence behind it.

    This is the first check in this corpus that polices an EPISTEMIC claim rather than a
    string. The others ask whether the documents agree with each other; this one asks whether
    the corpus meets the promotion standard it published for itself.

    It exists because they disagreed. CHARTER invariant 4 defined one source as a practice and
    three as a law, twelve of the eighteen laws sat at two, and nothing anywhere named that
    grade or noticed it was missing (D-039). The counts themselves lived only in a FROZEN file
    (L-13), which cannot carry a new law or a correction, so there was no live home to check
    against at all until provenance/attestation.json.

    The sunset assertion is the load-bearing one. Six sites in this corpus said "provisional"
    with no expiry and no forcing function, so provisional material accumulated permanently and
    nothing was ever going to review it. Requiring `would_attest` on anything below `settled`
    is what converts that from a good intention into a mechanism (L-17).
    """
    path = ROOT / "provenance" / "attestation.json"
    if not path.exists():
        fail("[attestation] provenance/attestation.json does not exist")
        return

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"[attestation] provenance/attestation.json is not valid JSON: {exc}")
        return

    bands = data.get("grade_bands", {})
    if not bands:
        fail("[attestation] no grade_bands declared - nothing to check a grade against")
        return

    # The review event is stated once, at the top, and every sunset points at it (L-14). A
    # per-law copy would be twelve identical strings, i.e. twelve places for it to drift.
    if not str(data.get("review_event", "")).strip():
        fail("[attestation] review_event is empty - every sunset points at it, so a blank "
             "one makes every would_attest unreviewable")

    entries = data.get("laws", [])
    by_id = {e.get("id"): e for e in entries}

    for e in entries:
        if list(by_id).count(e.get("id")) > 1:
            fail(f"[attestation] duplicate entry for {e.get('id')}")

    # -- 4a. the registry and the law vocabulary must describe the same set.
    law_vocab = next(
        (v for v in registry["vocabularies"] if v["name"] == "law"), None
    )
    if law_vocab is None:
        fail("[attestation] no 'law' vocabulary in the registry to check against")
        return
    laws = set(law_vocab["members"])

    for missing in sorted(laws - set(by_id)):
        fail(f"[attestation] {missing} is a law but has no attestation entry - "
             f"a law with no grade is a claim with no stated evidence (L-18)")
    for phantom in sorted(set(by_id) - laws):
        fail(f"[attestation] entry for {phantom}, which is not in the law vocabulary")

    # -- 4b. count matches the sources listed, and the grade matches the count.
    for law_id in sorted(laws & set(by_id), key=lambda s: int(s.split("-")[1])):
        e = by_id[law_id]
        sources = e.get("sources", [])
        count = e.get("count")
        grade = e.get("grade")

        if len(set(sources)) != len(sources):
            fail(f"[attestation] {law_id} lists a source twice: {sources}")

        if count != len(sources):
            fail(f"[attestation] {law_id} claims count {count} but lists "
                 f"{len(sources)} source(s): {sources}")
            continue

        if grade not in bands:
            fail(f"[attestation] {law_id} has grade '{grade}', which is not a declared band "
                 f"({', '.join(bands)})")
            continue

        low, high = bands[grade]
        if not low <= count <= high:
            expected = [g for g, (lo, hi) in bands.items() if lo <= count <= hi]
            fail(f"[attestation] {law_id} is graded '{grade}' on {count} source(s); "
                 f"band is {low}-{high}. Correct grade: "
                 f"{expected[0] if expected else 'none - count is outside every band'}")
            continue

        # -- 4c. the sunset. Anything not settled owes what would raise it.
        if grade != "settled" and not str(e.get("would_attest", "")).strip():
            fail(f"[attestation] {law_id} is graded '{grade}' with no 'would_attest' - "
                 f"a provisional rule with no stated path out of provisional never leaves it")


# ---------------------------------------------------------------- check 3

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
CODE_SPAN_RE = re.compile(r"`[^`]*`")


def strip_quoted_links(line: str) -> str:
    """Blank out inline code spans that contain a whole markdown link.

    A link inside backticks is being QUOTED, not followed - tools/README.md discusses a
    broken template link by showing it. Documenting a defect must not trip the check for
    that defect, or the only way to describe a problem is to reproduce it.

    Only spans containing '](' are removed. The common form [`file.md`](file.md) puts
    backticks inside the link LABEL, and that span holds no link of its own, so it survives
    and the link is still checked.
    """
    return CODE_SPAN_RE.sub(lambda m: "" if "](" in m.group(0) else m.group(0), line)


def slug(heading: str) -> str:
    h = re.sub(r"[`*_]", "", heading).strip().lower()
    h = re.sub(r"[^a-z0-9 \-]", "", h)
    return re.sub(r"\s+", "-", h)


_anchor_cache: dict[Path, set[str]] = {}


def anchors_of(path: Path) -> set[str]:
    if path not in _anchor_cache:
        text = path.read_text(encoding="utf-8", errors="replace")
        _anchor_cache[path] = {slug(h) for h in HEADING_RE.findall(text)}
    return _anchor_cache[path]


def check_links() -> None:
    for path in md_files():
        # Templates are written to be COPIED, so their links are resolved from where the
        # copy LANDS - a project root - not from artifacts/ where the master sits.
        #
        # The convention, and it is the whole reason this is not simply exempted:
        #   - references to FRAMEWORK files (doctrine/, rituals/, tiers/) are bare backticked
        #     paths, never markdown links, because the framework path varies per install
        #     (install/README.md fills a <doctrine path> placeholder).
        #   - references to PROJECT files (CHARTER.md, DECISIONS.md, OBSERVATIONS.md) stay
        #     markdown links, root-relative, because they resolve at the destination.
        #   - a '../' in a template link is always wrong: after the copy it points outside
        #     the project, at whatever happens to be there.
        is_template = path.name.endswith(".template.md")
        base = ROOT if is_template else path.parent

        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            for target in LINK_RE.findall(strip_quoted_links(line)):
                if re.match(r"^(https?:|mailto:|tel:)", target):
                    continue
                if "<" in target or ">" in target:
                    continue  # unfilled template placeholder
                file_part, _, anchor = target.partition("#")

                if not file_part:
                    if anchor and anchor not in anchors_of(path):
                        fail(f"[link] {rel(path)}:{line_no} anchor #{anchor} "
                             f"not found in this file")
                    continue

                if is_template and file_part.startswith("../"):
                    fail(f"[link] {rel(path)}:{line_no} template link escapes the project "
                         f"root -> {target}\n"
                         f"    Templates are copied to a project. Reference framework files "
                         f"by bare backticked path, not by link.")
                    continue

                dest = (base / file_part).resolve()
                if not dest.exists():
                    fail(f"[link] {rel(path)}:{line_no} broken -> {target}")
                    continue
                if anchor and dest.suffix == ".md":
                    if anchor not in anchors_of(dest):
                        fail(f"[link] {rel(path)}:{line_no} anchor #{anchor} "
                             f"not found in {file_part}")


# ---------------------------------------------------------------- main

# ---------------------------------------------------------------- check 6

# Files that legitimately carry no header block, each for a stated reason. Silence is not a
# reason -- an unexplained omission here is indistinguishable from a file nobody got to.
HEADER_EXEMPT = {
    "provenance/lineage.md":
        "FROZEN (L-13). Retrofitting a header onto a frozen record is an edit to it. "
        "doctrine/05-the-record.md states this exemption; do not 'fix' it.",
    "install/CLAUDE.md.template":
        "Copied to a consuming project's root as CLAUDE.md. Whether that file carries a "
        "header block is the consuming project's call, not this repo's.",
}

# The eight skills carry harness-required frontmatter (name/description) and are validated by
# check_install_manifest instead. Adding record_class to them risks skill registration, which
# is a live capability -- the gate does not trade a working instrument for a tidier schema.
HEADER_SKIP_GLOBS = ("install/skills/",)

HEADER_REQUIRED = ("record_class", "precedence", "confidence", "owns")
PLACEHOLDER = re.compile(r"^<.*>$")


def parse_header(text: str):
    """Return the raw frontmatter block as a dict of str -> str|list, or None if absent.

    Deliberately a line reader and not a YAML parser: the gate must run with no third-party
    dependency, and the block is fixed-shape by doctrine. A file whose header needs a real
    YAML parser has already left the shape this checks.
    """
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    body = text[3:end]
    out, key = {}, None
    for line in body.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and key:
            out.setdefault(key, [])
            if isinstance(out[key], list):
                out[key].append(line[4:].strip())
            continue
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key, val = key.strip(), val.strip()
            out[key] = val if val else []
    return out


def check_header_blocks(registry: dict) -> None:
    """Every living/append-only markdown file declares its class, rank and confidence.

    WHY THIS EXISTS. The framework spent its whole life stating a document's class in prose --
    `> **Doc status:** living.` -- which is readable and not queryable. The first consuming
    project independently rendered six of these vocabularies as frontmatter across 703 of its
    750 documents before anything here described a schema (O-33), and separately produced the
    case this check is really aimed at: a document whose `precedence: 6` sat machine-readable
    in its own header while it was quoted as authority against a precedence-2 ruling (O-37).

    WHAT IT CANNOT DO. It cannot tell you a header is TRUE. `last_verified` is a date someone
    typed; `owns:` is a claim, not a proof. It checks shape, membership, and one implication
    (CONFIRMED obliges a citation and a date) -- which is the mechanically checkable subset,
    exactly as the docstring at the top of this file says of the whole gate.
    """
    classes = next(v for v in registry["vocabularies"] if v["name"] == "record_class")["members"]
    tokens = next(v for v in registry["vocabularies"] if v["name"] == "confidence")["members"]
    owners: dict[str, str] = {}

    for path in md_files():
        r = rel(path)
        if any(r.startswith(g) for g in HEADER_SKIP_GLOBS):
            continue
        if r in HEADER_EXEMPT:
            exempt(f"[header:{r}] no header block -- {HEADER_EXEMPT[r]}")
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        head = parse_header(text)
        if head is None:
            fail(f"[header] {r} has no header block (doctrine/05-the-record.md)")
            continue

        for field in HEADER_REQUIRED:
            if field not in head:
                fail(f"[header] {r} header is missing required field '{field}'")

        klass = head.get("record_class", "")
        if isinstance(klass, str) and klass and not PLACEHOLDER.match(klass):
            if klass not in classes:
                fail(f"[header] {r} record_class '{klass}' is not in the record_class "
                     f"vocabulary ({', '.join(classes)})")

        prec = head.get("precedence", "")
        if isinstance(prec, str) and prec and not PLACEHOLDER.match(prec):
            if not prec.isdigit() or not 1 <= int(prec) <= 6:
                fail(f"[header] {r} precedence '{prec}' is not a layer number 1-6")

        conf = head.get("confidence", "")
        if isinstance(conf, str) and conf and not PLACEHOLDER.match(conf):
            if conf not in tokens:
                fail(f"[header] {r} confidence '{conf}' is not a confidence token")
            elif conf == "CONFIRMED":
                # 02-epistemics.md: CONFIRMED means independently re-derived -- CITE WHERE.
                for owed in ("verified_by", "last_verified"):
                    v = head.get(owed, "")
                    if not v or (isinstance(v, str) and PLACEHOLDER.match(v)):
                        fail(f"[header] {r} claims confidence: CONFIRMED but has no "
                             f"'{owed}'. The token means re-derived from the source; "
                             f"without a citation and a date it is UNVERIFIED.")

        # L-14, made mechanical: a fact has exactly one home, and now says so out loud.
        for key in head.get("owns", []) or []:
            if PLACEHOLDER.match(key) or key.startswith("<"):
                continue
            if key in owners:
                fail(f"[header] L-14: '{key}' is claimed by both {owners[key]} and {r}. "
                     f"A vocabulary has exactly one home.")
            else:
                owners[key] = r

    # Every registered vocabulary's declared home should claim it in owns:. This is the
    # registry and the corpus checking each other rather than the corpus checking itself.
    for vocab in registry["vocabularies"]:
        home, name = vocab["home"], vocab["name"]
        if home in HEADER_EXEMPT or any(home.startswith(g) for g in HEADER_SKIP_GLOBS):
            continue
        claimed = owners.get(name)
        if claimed is None:
            fail(f"[header] vocabulary '{name}' declares its home as {home}, but no "
                 f"document claims it in owns:")
        elif claimed != home:
            fail(f"[header] vocabulary '{name}' declares its home as {home}, but "
                 f"{claimed} claims it in owns:")


# ---------------------------------------------------------------- check 7

# (file, human label, regex whose group(1) is the ID, how the ID is written)
ID_SOURCES = [
    ("DECISIONS.md", "ledger entry",
     re.compile(r"^`\[[^\]]*\]\s*(D-\d+):", re.M), "D-NNN"),
    ("OBSERVATIONS.md", "observation",
     re.compile(r"^###\s+`(O-\d+)`", re.M), "O-N"),
]

# An amendment carries the number it amends and does NOT consume a new one (DECISIONS.md,
# Conventions). A naive port of this check flagged all three of them as collisions on the
# first run, which is the shape a gate fails in when it is copied instead of adapted.
AMENDS_RX = re.compile(r"^`\[[^\]]*\]\s*AMENDS\s+(D-\d+):", re.M)


def check_id_collisions() -> None:
    """One address, one entry. Never renumber, never reuse (05-the-record.md, hard rule 11).

    WHY THIS IS HERE AND NOT ONLY IN A CONSUMING PROJECT. This framework mandates the exact
    structure that collides: append-only files, permanent IDs, gaps never closed, and a next
    ID that is "one more than the highest I can see." Read by two branches that cannot see
    each other, that produces two valid-looking files and one silent collision at merge. The
    consuming project hit it four times on a single identifier (O-38). DECISIONS.md and
    OBSERVATIONS.md have the identical exposure and had no check at all.

    WHAT IT CANNOT DO (L-18). It sees one working tree. It catches a collision at the moment
    a merge resolution is wrong -- which is where the damage would otherwise be committed --
    and it CANNOT predict a collision between two branches that have not met. Nothing local
    can, and claiming otherwise would be the false-capability defect it exists to catch.
    """
    for relpath, label, rx, form in ID_SOURCES:
        path = ROOT / relpath
        if not path.exists():
            fail(f"[id] {relpath} does not exist")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        matches = list(rx.finditer(text))

        # A regex that stops matching must fail loudly rather than pass vacuously. This is
        # the check most likely to rot silently: the entry form changes, nothing matches,
        # and a gate reporting "0 collisions" is indistinguishable from one that is blind.
        if not matches:
            fail(f"[id] {relpath}: found no {label} IDs at all. The '{form}' entry form "
                 f"changed, or this check is now blind. Fix the pattern, do not delete it.")
            continue

        seen: dict[str, list[int]] = {}
        for m in matches:
            line = text[:m.start()].count("\n") + 1
            seen.setdefault(m.group(1), []).append(line)

        for ident, lines in sorted(seen.items()):
            if len(lines) > 1:
                fail(f"[id] {relpath}: {label} '{ident}' is allocated {len(lines)} times "
                     f"(lines {', '.join(map(str, lines))}). An ID is a permanent address. "
                     f"The entry already in the record keeps '{ident}'; the one that never "
                     f"entered it is numbered FORWARD. That is numbering, not renumbering.")

        # The inverse, which the consuming project's version does not check: an amendment
        # pointing at a decision that was never made. Same class of damage, opposite sign --
        # a dangling amendment resolves to nothing rather than to the wrong thing.
        if relpath == "DECISIONS.md":
            allocated = set(seen)
            for m in AMENDS_RX.finditer(text):
                if m.group(1) not in allocated:
                    line = text[:m.start()].count("\n") + 1
                    fail(f"[id] {relpath}:{line} amends '{m.group(1)}', which was never "
                         f"allocated. An amendment carries the number it amends; if that "
                         f"number does not exist the amendment has no subject.")


# ---------------------------------------------------------------- check 8

# Rules that are LOAD-BEARING AT SESSION TIME must live in the always-loaded file, not only in
# install/README.md. The README is read once, during an install, by someone who then never opens
# it again; CLAUDE.md.template is what a collaborator actually has in front of it every session.
#
# THIS IS D-044's FINDING, RECURRING. That entry moved the instruments material into the install
# layer because "doctrine a session never reads is not in force" -- and the SAME defect was sitting
# two files away the whole time, on the namespacing rule, unnoticed until a consuming project's
# session wrote a bare `D-044` next to an `AST-D-049` and could not have known better.
#
# Each row is (regex, human name, the incident). A row with no incident does not belong here --
# this list is for rules that have already been missed, not for everything anyone considers
# important. Adding one because it seems wise is how a compact template stops being compact,
# which install/README.md names as the way the install fails in practice.
TEMPLATE_MUST_CARRY = [
    (r"AST-D-",
     "the AST- ledger namespacing rule",
     "Third instance of the namespace class. (1) A source project ran two live `D-` namespaces "
     "and had to publish a disambiguation rule after the fact -- the scar 00-precedence.md "
     "cites. (2) install/README.md then instructed the first real install to create a rival "
     "`DECISIONS.md`, caught only by refusing it (D-045b). (3) 2026-08-01, a consuming project's "
     "session wrote a bare `D-044` one paragraph after citing `AST-D-049`; the convention existed "
     "in install/README.md and was absent from the file that session actually reads."),
]


def check_template_carries() -> None:
    """The always-loaded file carries the rules that bite at session time.

    WHAT THIS CANNOT DO. It checks that the STRING is present, not that the rule is stated well,
    and certainly not that a session then follows it -- O-39 measured a rule read, agreed to and
    restated out loud being violated four times in one session. This raises the floor from
    "absent" to "present." That is the whole claim.
    """
    template = ROOT / "install" / "CLAUDE.md.template"
    if not template.exists():
        fail("[template] install/CLAUDE.md.template does not exist")
        return
    text = template.read_text(encoding="utf-8", errors="replace")
    for pattern, name, incident in TEMPLATE_MUST_CARRY:
        if not re.search(pattern, text):
            fail(f"[template] install/CLAUDE.md.template does not carry {name}. "
                 f"A rule that lives only in install/README.md is read once and never again "
                 f"(D-044). Incident: {incident}")

    # The mirror image: the README must not be the ONLY home either way round. If the README
    # dropped the rule while the template kept it, an installer following the README would not
    # know to fill it in -- the same gap, pointing the other direction.
    readme = ROOT / "install" / "README.md"
    if readme.exists():
        rtext = readme.read_text(encoding="utf-8", errors="replace")
        for pattern, name, _ in TEMPLATE_MUST_CARRY:
            if not re.search(pattern, rtext):
                fail(f"[template] install/README.md no longer explains {name}, which "
                     f"install/CLAUDE.md.template carries. The installer is told to fill in a "
                     f"rule nothing explains.")


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    check_vocabularies(registry)
    check_install_manifest()
    check_links()
    check_attestation(registry)
    check_header_blocks(registry)
    check_id_collisions()
    check_template_carries()

    if VERBOSE and exemptions:
        print(f"EXEMPTIONS TAKEN ({len(exemptions)}) - every one is a place this gate "
              f"does not look:\n")
        for e in exemptions:
            print(f"  - {e}")
        print()

    if failures:
        print(f"CORPUS CHECK FAILED - {len(failures)} problem(s):\n")
        for f in failures:
            print(f"  [FAIL] {f}")
        print("\nThe guard is intentional. Fix the cause, do not disable the check.")
        if not VERBOSE:
            print("Run with --verbose to see what the gate deliberately does not check.")
        return 1

    print("CORPUS CHECK PASSED - vocabularies, install manifest, links, and attestation "
          "all consistent.")
    if not VERBOSE:
        print(f"({len(exemptions)} exemptions taken; run with --verbose to see them.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
