# AGENTS.md — Instructions for AI Coding Agents

This file contains the rules, conventions, and workflows that all AI coding agents **must** follow when working in this repository.

**Primary reference:** [HARNESS-SPEC.md](HARNESS-SPEC.md) — the full process, artifacts, and rituals.

---

## Core Behavioral Rules

These rules are non-negotiable and derived from repeated observed failures across many codebases.

1. **Think before acting.** Explicitly state your understanding, assumptions, and any ambiguities. Ask clarifying questions instead of guessing.
2. **Be surgically precise.** Modify *only* the minimal code necessary to complete the requested task. Never refactor unrelated areas "while you're here."
3. **Minimal changes only.** Solve exactly what was asked. Do not add speculative features, future-proofing, or unrelated improvements.
4. **Define success upfront.** Before writing code, state the success criteria. Iterate until they are met. Do not stop early.
5. **Read before writing.** Review relevant files, callers, exports, and context first.
6. **Match existing conventions exactly.** Follow the style, patterns, and decisions already present in the codebase — even if you disagree with them.
7. **Tests must verify real intent.** Write tests that validate the actual business logic or behavior, not just that code exists or runs.
8. **Checkpoint after significant work.** After major steps, summarize what was done, what was verified, what remains, and any open questions.
9. **Fail loud and early.** Surface uncertainty, errors, limitations, or conflicts immediately. Never hide problems or guess.
10. **Respect token budgets and context.** Be concise. Summarize when appropriate. Restart context when needed rather than continuing with degraded performance.
11. **Use HTML for human-facing deliverables.** When producing specs, reports, reviews, dashboards, prototypes, or any artifact primarily for human consumption, prefer a self-contained HTML file (with Tailwind via CDN) over raw Markdown. HTML dramatically improves human comprehension and engagement.
12. **Follow the stacked PR discipline.** All work must be delivered in small, reviewable PRs (< 10 minutes deep review). Use explicit traceability, plan mode, and the PETC loop.

---

## Project Commands

Always use the `justfile` for canonical commands:

- `just init` — Environment bootstrap
- `just check`
- `just test`
- `just clippy`
- `just fmt`
- `just status` — Orchestration status dashboard in the terminal (also available in opencode as `/status`) (completed / in progress / todo)
- `just status-html` — Also write `docs/status-dashboard.html` (the in-harness UI)
- `just harness-validate` — Validate `features.json` + run `docs-verify`, `opencode-verify`, and the Claude skill drift check
- `just claude-skills-sync` — Regenerate the Claude compatibility copies in `~/.claude/skills` from `.agents/skills/`
- `just docs-verify` — Verify documentation alignment with current canonical standards

Run the appropriate commands before declaring work complete.

---

## Project Structure & Key Files

- `HARNESS-SPEC.md` — The authoritative process specification. Read this for how work is done here.
- `.agents/skills/` — All reusable capabilities (agentskills.io format). All skills follow the canonical portable structure with proper Harness Relationship (Stratified) disclosure (see HARNESS-SPEC.md).
- `.agents/agents/` — Reusable agent personas (e.g., reviewer, tester, architect). The permanent `skill-evaluator-agent`, `skill-remediator-agent`, and `skill-reviewer-agent` are used for all skill remediation work. Planning consensus uses AVRIL personas: `planning-architect-agent`, `product-owner-agent`, `qa-architect-agent`, `visionary-cto-agent` (skill: `avril`). Execution uses `axel-conductor-agent` (skill: `axel`) plus the code GAN trio.
- `features.json` + `progress.md` — Machine + human tracking of work (phase → commits → features model).
- `scripts/harness-bootstrap` — Tool to scaffold the full harness in new projects.
- `scripts/sync-skills` — Tool to keep skills in sync across projects.

---

## HTML Output Guidance (Human Interface Layer)

For any deliverable intended for human review — specs, architecture documents, PR summaries, reports, dashboards, prototypes, deployment guides, etc. — **generate a self-contained HTML file** as the primary artifact.

- Use Tailwind CSS via CDN for styling.
- Make it beautiful, scannable, and interactive where helpful.
- This is dramatically more effective than Markdown for human consumption ("the unreasonable effectiveness of HTML").
- You may also produce a Markdown version for git or agent handoff, but HTML is the primary human-facing output.

Example filenames: `architecture-review.html`, `pr-summary.html`, `deploy-guide.html`.

---

## Git & PR Workflow

- Follow the stacked PR pattern described in HARNESS-SPEC.md.
- Every PR must be reviewable in < 10 minutes.
- Use Plan Mode: plans are concise and end with a list of unresolved questions.
- Commit messages and PR titles should reference the relevant feature/phase IDs.

---

## Boundaries & Safety

- **Never** make destructive changes without explicit confirmation.
- **Never** touch unrelated files or systems.
- **Always** run verification commands (`just test`, `just clippy`, etc.) before claiming completion.
- Surface any policy, security, or architectural concern immediately.

---

## Status Dashboard (In-Harness UI)

Every orchestration skill (`avril`, `axel`, `rust-team-lead`, and prompts generated by `orchestrator-prompt`) must keep a live **completed / in progress / todo** view as it works.

- `just status` renders it in the terminal; `just status-html` also writes `docs/status-dashboard.html`.
- Sources are read-only and optional: `features.json` phases/commits, the Pinto board when installed, and the `progress.md` tail. A missing source degrades to empty rather than failing.
- The board wins over `features.json` for headline counts when both are present.
- The file is **generated — never hand-edited**, and is never the source of truth: the board and tracking artifacts are.
- Refresh at every checkpoint the skill lists (board transitions, BLESS marks, AC evidence gate, planning stop). Commit the HTML **only at phase or PBI boundaries** so the diff stays meaningful.

## Claude Skill Copies

`.agents/skills/` is the single source of truth. The Claude compatibility copies under `~/.claude/skills` (or `CLAUDE_SKILLS_DIR`) are **generated, never hand-edited** — see HARNESS-SPEC.md §2.1.

- `just claude-skills-sync` regenerates them; `./scripts/sync-claude-skills --all` installs every repo skill, and named arguments add specific ones.
- Skills in the target that this repo does not own (personal or project-local) are never deleted or modified — they are reported and left alone.
- Replaced files are backed up to a timestamped `skills.backup-*` directory.
- `just harness-validate` reports drift without failing; run the sync to clear it.

## OpenCode Slash Commands (`/avril`, `/axel`)

This repo ships project-scoped OpenCode entrypoints under `.opencode/`:

- **`/avril`** — planning conductor. Bare `/avril` gives a read-only status report (board, blessed set, ready PBIs, blockers). `/avril <free text>` plans, proposes, or runs the PO → QA → CTO blessing loop. It never writes production code.
- **`/status`** — read-only project status. Bare `/status` gives the standing report (completed / in progress / todo, what's next, what looks stalled). `/status <question>` answers from the same dump. The agent has `edit` and `task` denied, so it structurally cannot mutate anything.
- **`/axel`** — execution conductor. Bare `/axel` reports the next ready blessed PBI and **asks for confirmation before executing anything**. `/axel run <id>` drives that PBI through PETC + code GAN. It never writes code itself.
- Both open with a read-only preflight (git, `progress.md`, `features.json`, Pinto board, blessed summaries) that fails soft when a tool or file is missing.
- **Restart opencode** after changing anything under `.opencode/` — config is read at startup and is not hot-reloaded.
- Verify the layer with `just opencode-verify` (or `./scripts/verify-opencode --run-preflight` to also execute the preflight blocks).

## How to Work in This Repo

1. Read the relevant parts of `HARNESS-SPEC.md`.
2. Activate the appropriate skills from `.agents/skills/`.
3. Use Plan Mode for any non-trivial task.
4. Produce HTML for human review artifacts when applicable.
5. Follow the GAN cycle (Reviewer → Tester → Architect) for significant changes using the agents in `.agents/agents/`.
5b. For significant planning / prototype backlog work, run AVRIL (`code-writer` + `avril`) until every PBI is triple-blessed (PO → QA → CTO) before execution.
5b-alt. Alternatively, for work whose behaviour can be written down before it is built, run BRICK (`code-writer` + `brick`): informal spec → tasks → Gherkin → red tests → green code → refactor → mutation gate. See HARNESS-SPEC §4.4 for choosing between the two pipelines. Never run both on the same unit of work.
5c. For executing a blessed backlog, run AXEL (`code-writer` + `axel` + language stack; Rust: inner `rust-team-lead`) — PETC per phase, code GAN BLESS × 3, AC evidence, honest board/tracking.
6. Deliver work in small, stacked, reviewable PRs.
7. Update `features.json` + `progress.md` as you go.

**All agents must follow these rules.** Violations will be called out during review.