#!/usr/bin/env python3
"""Validate a drafted PR review against the PR diff before posting it.

Usage: validate_review.py REVIEW_JSON PR_DIFF [--max-comments N] [--self-review]

Checks, per comment:
  - first line matches  <blocker|should-fix|nit|q> [<slug>] <problem>
  - body has Issue / Why it matters / Suggested fix / Done when lines
    (nits may omit Why it matters; questions may omit Suggested fix)
  - path appears in the diff
  - line (and start_line) is a commentable line on the given side
  - start_line < line, same hunk

And per review:
  - event matches the severities present (with --self-review, a zero-finding
    COMMENT is accepted because the PR author cannot APPROVE)
  - comment count within the cap
  - no two comments on the same path/line with the same first line

Exit code 0 when clean, 1 when any problem is found. Problems go to stderr.
Stdlib only.
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

FIRST_LINE = re.compile(r"^(blocker|should-fix|nit|q)(?:\s+\[([a-z0-9][a-z0-9-]*)\])?\s+\S.*$")
REQUIRED = ("Issue:", "Done when:")
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


@dataclass
class FileLines:
    right: set[int] = field(default_factory=set)
    left: set[int] = field(default_factory=set)
    # hunk id per line so multi-line ranges can be checked for same-hunk
    right_hunk: dict[int, int] = field(default_factory=dict)
    left_hunk: dict[int, int] = field(default_factory=dict)


def parse_diff(text: str) -> dict[str, FileLines]:
    files: dict[str, FileLines] = {}
    cur: FileLines | None = None
    old = new = 0
    hunk_id = 0
    for raw in text.splitlines():
        if raw.startswith("+++ "):
            name = raw[4:].strip()
            if name.startswith("b/"):
                name = name[2:]
            cur = files.setdefault(name, FileLines()) if name != "/dev/null" else None
            continue
        if raw.startswith("--- ") or raw.startswith("diff ") or raw.startswith("index "):
            continue
        m = HUNK.match(raw)
        if m:
            old, new = int(m.group(1)), int(m.group(3))
            hunk_id += 1
            continue
        if cur is None or not raw:
            continue
        tag, _ = raw[0], raw[1:]
        if tag == "\\":
            continue
        if tag == "+":
            cur.right.add(new); cur.right_hunk[new] = hunk_id; new += 1
        elif tag == "-":
            cur.left.add(old); cur.left_hunk[old] = hunk_id; old += 1
        elif tag == " ":
            cur.right.add(new); cur.right_hunk[new] = hunk_id
            cur.left.add(old); cur.left_hunk[old] = hunk_id
            new += 1; old += 1
    return files


def check_comment(i: int, c: dict, files: dict[str, FileLines], problems: list[str]) -> str | None:
    tag = f"comment[{i}] {c.get('path')}:{c.get('line')}"
    body = c.get("body", "")
    first = body.split("\n", 1)[0]
    m = FIRST_LINE.match(first)
    if not m:
        problems.append(f"{tag}: first line does not match grammar: {first!r}")
        severity = None
    else:
        severity = m.group(1)
    missing = [k for k in REQUIRED if k not in body]
    if severity != "nit" and "Why it matters:" not in body:
        missing.append("Why it matters:")
    if severity != "q" and "Suggested fix:" not in body:
        missing.append("Suggested fix:")
    if missing:
        problems.append(f"{tag}: body missing {', '.join(missing)}")

    path = c.get("path")
    fl = files.get(path)
    if fl is None:
        problems.append(f"{tag}: path not in diff")
        return severity
    side = c.get("side", "RIGHT")
    lines, hunks = (fl.right, fl.right_hunk) if side == "RIGHT" else (fl.left, fl.left_hunk)
    line = c.get("line")
    if not isinstance(line, int) or line not in lines:
        problems.append(f"{tag}: line {line} is not a commentable {side} line in the diff")
        return severity
    start = c.get("start_line")
    if start is not None:
        if not isinstance(start, int) or start not in lines:
            problems.append(f"{tag}: start_line {start} is not a commentable {side} line")
        elif start >= line:
            problems.append(f"{tag}: start_line {start} must be < line {line}")
        elif hunks.get(start) != hunks.get(line):
            problems.append(f"{tag}: start_line {start} and line {line} are in different hunks")
    return severity


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    max_comments = 15
    self_review = "--self-review" in argv
    if "--max-comments" in argv:
        max_comments = int(argv[argv.index("--max-comments") + 1])
    review = json.loads(Path(argv[1]).read_text())
    files = parse_diff(Path(argv[2]).read_text())
    problems: list[str] = []

    comments = review.get("comments", [])
    severities = []
    seen: set[tuple] = set()
    for i, c in enumerate(comments):
        sev = check_comment(i, c, files, problems)
        if sev:
            severities.append(sev)
        key = (c.get("path"), c.get("line"), c.get("body", "").split("\n", 1)[0])
        if key in seen:
            problems.append(f"comment[{i}]: duplicate of an earlier comment on the same line")
        seen.add(key)

    if len(comments) > max_comments:
        problems.append(f"{len(comments)} comments exceeds cap of {max_comments}; drop nits or cluster")

    event = review.get("event")
    if event not in ("APPROVE", "REQUEST_CHANGES", "COMMENT"):
        problems.append(f"event {event!r} is not APPROVE / REQUEST_CHANGES / COMMENT (omitting it leaves the review pending)")
    elif "blocker" in severities and event != "REQUEST_CHANGES":
        problems.append(f"a blocker is present but event is {event}; must be REQUEST_CHANGES")
    elif "blocker" not in severities and event == "REQUEST_CHANGES":
        problems.append("event is REQUEST_CHANGES but no comment is a blocker")
    elif comments and event == "APPROVE" and any(s in ("blocker", "should-fix") for s in severities):
        problems.append("event is APPROVE but should-fix/blocker comments are present")
    if not comments and event != "APPROVE" and not (self_review and event == "COMMENT"):
        problems.append(f"no comments but event is {event}; a zero-finding review is an APPROVE (or COMMENT with --self-review)")
    if self_review and event == "APPROVE":
        problems.append("event is APPROVE but --self-review is set; GitHub rejects an approval from the PR author, use COMMENT")
    if not review.get("body", "").strip():
        problems.append("review body is empty; one sentence summarising what was checked")

    for p in problems:
        print(p, file=sys.stderr)
    counts = {s: severities.count(s) for s in ("blocker", "should-fix", "nit", "q") if s in severities}
    print(f"{len(comments)} comments {counts} event={event} -> {'OK' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
