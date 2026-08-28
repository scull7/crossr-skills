---
description: Project status — completed / in progress / todo from the board and tracking artifacts, plus answers to questions about where the work stands
agent: status
---

## Dashboard (read-only)

!`./scripts/status-dashboard 2>/dev/null || python3 scripts/status-dashboard 2>/dev/null || echo "(no scripts/status-dashboard in this project — report from the board and tracking artifacts below instead)"`

Open items on the board:
!`command -v pinto >/dev/null 2>&1 && pinto list --json 2>/dev/null | python3 -c 'import json,sys;d=json.load(sys.stdin);rows=[t for t in (d if isinstance(d,list) else d.get("tasks",[])) if t.get("status")!="done"];print("\n".join("{} [{}] {}".format(t.get("id"),t.get("status"),t.get("title")) for t in rows) or "board clear (no open items)")' || echo "(pinto not on PATH)"`

Recent commits:
!`git log --oneline -8 2>/dev/null || echo "(no git repository)"`

---

Answer this request from the dump above:

$ARGUMENTS

**If the request is empty**, give the standing report: the headline counts, what is in
progress right now, what is ready to pick up next, and anything that looks stalled or
contradictory. Keep it short — a human is scanning it, not studying it.

Routing hints (free English always works):

- `next` → what is ready to start, and what blocks the rest
- `blocked` / `stalled` → items in progress with no recent commit touching them
- `<id>` → everything the sources say about that one item
- `html` → run `./scripts/status-dashboard --html` and report where it wrote
- `help` → list these routes and stop

Hard rules: read-only — no edits, no board writes, no commits. Never invent a status
or a number that is not in the dump. If a source is missing, name it and report what
the others show. Planning is `/avril`; execution is `/axel`.
