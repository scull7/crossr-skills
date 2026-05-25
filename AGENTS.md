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
- `just harness-validate` — Validate `features.json` against the schema

Run the appropriate commands before declaring work complete.

---

## Project Structure & Key Files

- `HARNESS-SPEC.md` — The authoritative process specification. Read this for how work is done here.
- `.agents/skills/` — All reusable capabilities (agentskills.io format). All skills follow the canonical portable structure with proper Harness Relationship (Stratified) disclosure (see HARNESS-SPEC.md).
- `.agents/agents/` — Reusable agent personas (e.g., reviewer, tester, architect). The permanent `skill-evaluator-agent`, `skill-remediator-agent`, and `skill-reviewer-agent` are used for all skill remediation work.
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

## How to Work in This Repo

1. Read the relevant parts of `HARNESS-SPEC.md`.
2. Activate the appropriate skills from `.agents/skills/`.
3. Use Plan Mode for any non-trivial task.
4. Produce HTML for human review artifacts when applicable.
5. Follow the GAN cycle (Reviewer → Tester → Architect) for significant changes using the agents in `.agents/agents/`.
6. Deliver work in small, stacked, reviewable PRs.
7. Update `features.json` + `progress.md` as you go.

**All agents must follow these rules.** Violations will be called out during review.