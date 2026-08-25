---
description: AXEL execution conductor — run the next blessed PBI through PETC + code GAN, report status or AC evidence (conductor only)
agent: axel
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

Load the `axel` and `code-writer` skills (plus the disclosed language/domain stack)
with the skill tool, recite AXEL's One-Sentence Mandate, then handle this request:

$ARGUMENTS

**If the request above is empty, do NOT start executing.** Report the next ready
blessed PBI — id, title, acceptance criteria, dependencies — or explain why the intake
gate fails, then **ask the user to confirm** before any execution begins.

Routing hints (non-exclusive; free English always works):

- `status` / `next` → current board state and the next ready blessed PBI
- `run <id>` → execute that PBI through Plan-Execute-Test-Commit with the code GAN
- `evidence <id>` → show recorded AC evidence and verification output for that PBI
- `help` → list what this conductor can do, and execute nothing

Verb prefixes are optional shorthand, never required: `status`, `next`, `run T-3`,
`evidence T-3`, `help`. Plain English routes through the same hints — `/axel pick up
the next blessed ticket` is a `run` request, and still needs confirmation first.

On `help`, print the four routes above with a one-line example each, name the board in
use, and stop. Do not select work, do not move the board.

Decomposition mode is **off by default**. If the user asks for it in `$ARGUMENTS`
(e.g. "with decomposition"), pass that through to the `axel` skill, which owns the
threshold and the decompose loop; contract:
`docs/plans/mitchell-decomposition-contract.html`. Never enable it on your own.

Hard rules: intake gate (AVRIL-blessed work only — planning is `/avril`); conductor
never writes or reviews code; Reviewer → Tester → Architect BLESS before every commit;
every acceptance criterion evidenced before done; no PR unless explicitly asked.
