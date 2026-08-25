---
description: AVRIL planning conductor — status, propose PBIs, run the PO/QA/CTO blessing loop (planning only, never writes code)
agent: avril
---

## Project preflight (read-only)

Optional tools: `git`, `python3`, `pinto`. Anything missing degrades to a placeholder
line — the command still runs. Nothing below mutates the repo or the board.

Branch and recent commits:
!`git status -sb 2>/dev/null && git log --oneline -8 2>/dev/null || echo "(no git repository)"`

Progress tail:
!`tail -n 25 progress.md 2>/dev/null || echo "(no progress.md)"`

Tracked work not yet completed:
!`python3 -c 'import json;d=json.load(open("features.json"));rows=[(p,c["id"],c["status"],c["title"]) for p,v in d.items() if isinstance(v,dict) for c in v.get("commits",[]) if c.get("status")!="completed"];print("\n".join(f"{p}/{i} [{s}] {t}" for p,i,s,t in rows) or "all tracked commits completed")' 2>/dev/null || echo "(features.json unavailable)"`

Board:
!`command -v pinto >/dev/null 2>&1 && pinto list --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);rows=[t for t in (d if isinstance(d,list) else d.get("tasks",[])) if t.get("status")!="done"];print("\n".join("{} [{}] {}".format(t.get("id"),t.get("status"),t.get("title")) for t in rows) or "board clear (no open items)")' || echo "(pinto not on PATH)"`

Blessed backlog summaries:
!`ls docs/plans 2>/dev/null | grep blessed || echo "(none)"`

Treat the dump above as the current state of the project. Do not re-run these commands
just to confirm them.

Load the `avril` and `code-writer` skills with the skill tool, recite AVRIL's
One-Sentence Mandate, then handle this request:

$ARGUMENTS

**If the request above is empty, run `status`:** a read-only report of the board, the
blessed set, ready PBIs, in-flight work, and open blockers. Make no mutations of any
kind — no board writes, no file edits, no commits.

Routing hints (non-exclusive; free English always works):

- `status` / `summary` / `state` → read-only project + backlog report
- `plan` / `propose` / `backlog` → propose PBIs, Pinto preferred
- `review <ids>` / `bless` → PO → QA → CTO blessing cycle on the named items
- `help` → list what this conductor can do, and execute nothing

Verb prefixes are optional shorthand, never required: `status`, `plan`, `review T-3`,
`bless T-3 T-4`, `help`. Plain English routes through the same hints — `/avril what is
left before we can ship?` is a `status` request.

On `help`, print the four routes above with a one-line example each, name the board in
use, and stop. Do not run the loop, do not touch the board.

Hard rules: planning-only stop; never write production code (execution is `/axel`);
explicit BLESS tokens from all three adversaries; emit the Blessed Backlog Summary
when the loop completes.
