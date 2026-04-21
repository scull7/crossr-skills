---
name: agent-harness
description: |
  Specialized skill for designing and bootstrapping **effective harnesses** for
  long-running AI agents in Tensorwave software projects.
  Combines Anthropic's long-running agent scaffolding, AIHero's
  Plan-Execute-Test-Commit loop, and Revfactory Harness patterns.
  Use this skill whenever you need agents to maintain state, make incremental
  progress, and leave production-ready code across multiple sessions.
---

# Agent Harness Skill (Tensorwave Edition)

**This skill extends `code-writer` + `rust-code-writer`.**
You **MUST** apply the core coding philosophy first, then layer on these
harness-specific rules for any Tensorwave project (Rust backends, Leptos
frontends, Axum APIs, Polars pipelines, GPU orchestration, etc.).

## Purpose

A **harness** is the persistent scaffolding that turns stateless AI sessions
into reliable, multi-session agents. It guarantees:

- State continuity across context resets
- Incremental, verifiable progress (one small task per session)
- Clean, merge-ready handovers
- Self-critique and automated verification

Inspired by:

- [Anthropic – Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [AIHero – AGENTS.md for plans agents actually read](https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read)
- [Revfactory Harness – meta-skill for agent teams & skill generation](https://github.com/revfactory/harness)

---

## Core Harness Artifacts

> Create all five in every Tensorwave project.

### 1. `init.sh`

One-command environment bootstrap (start servers, DB, WASM build, GPU env
vars, etc.). Agents **always** run `./init.sh` at session start.

### 2. `features.json` (or `tasks.json`)

Structured, machine-readable task list. Example entry:

```json
{
  "id": "tw-42",
  "category": "backend",
  "description": "Implement Axum health-check endpoint with GPU metrics",
  "steps": ["..."],
  "status": "pending",
  "verified": false,
  "notes": ""
}
```

Agents update `status` **only** after running tests + self-critique.

### 3. `progress.md`

Human-readable session log. Agents append:

- What they did
- Decisions made
- Any unresolved questions

### 4. Git

Every session ends with a clean, descriptive commit. Agents must run
`git status` and `git log --oneline -10` at session start.

### 5. `AGENTS.md` (project root)

Project-specific rules — see the **Plan Mode** section below.

---

## `AGENTS.md` — Plan Mode (AIHero Pattern)

````markdown
## Plan Mode (Agents must follow this exactly)

- Make every plan extremely concise. Sacrifice grammar for scannability.
- At the end of each plan, give a bulleted list of unresolved questions (if any).
- Always follow the Plan → Execute → Test → Commit loop.
- Never skip planning. Never jump straight to code.
```

### Plan → Execute → Test → Commit Loop

Repeat every session:

1. **Plan** — Read `progress.md` + `features.json` + `git log` → propose next
   task + plan.
2. **Execute** — Implement using appropriate skills (e.g. `rust-axum-backend`).
3. **Test** — Unit tests, integration tests, E2E (Puppeteer-style if frontend),
   `cargo test`, `cargo clippy -- -D warnings`.
4. **Commit** — `git commit -m "TW-42: ..."` + update `features.json` + append
   to `progress.md`.

---

## Agent Team Design Patterns (Revfactory-inspired)

Choose **one pattern per project** and document it in the harness README.

| Pattern               | When to use              | Example for Tensorwave                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------- |
| Pipeline              | Sequential stages        | Analyze → Design → Rust Backend → Frontend → QA              |
| Supervisor + Specialists | Dynamic delegation    | Supervisor delegates to `rust-backend-agent`, `leptos-agent`, `gpu-bench-agent` |
| Producer-Reviewer     | High-quality generation  | Code producer → `rust-code-reviewer`                         |
| Hierarchical          | Deeply nested tasks      | Top-level feature → sub-tasks                                 |

Agents and skills are generated into `.agents/agents/` and `.agents/skills/`
using **progressive disclosure** (keep context small).

---

## Session Start Ritual

Every agent **must** run the following at the start of each session:

```bash
pwd
cat progress.md | tail -n 50
git log --oneline -10
cat features.json | jq '.[] | select(.status=="pending") | .id' | head -5
./init.sh

# Run basic smoke tests
cargo check && cargo test --quiet
```

Only then pick the next pending feature.

---

## Error Recovery & Self-Critique

- Agents must self-verify before marking `"verified": true`.
- Use `rust-code-reviewer` ruthlessly on every code change.
- Git is the safety net — **never** force-push; always commit.
- If state is broken → run `./init.sh` + revert to last good commit.

---

## Activation Statement

> Using `code-writer` + `rust-code-writer` + `agent-harness` +
> [relevant domain skills, e.g. `rust-axum-backend`, `rust-frontend`,
> `rust-errors`] for this Tensorwave harness task.

When bootstrapping a new Tensorwave project:

1. Say the activation statement above.
2. Ask the agent to create the five core artifacts.
3. Commit the empty harness.
4. From then on, every new session begins with:
   **"Continue harness work on next feature."**

---

## How to Include This Skill

1. Save this file to `.agents/skills/agent-harness/SKILL.md`.
2. Update your root `AGENTS.md` (Core Skills section):

   ```markdown
   - **`agent-harness`**
     Specialized skill for effective long-running agent harnesses in
     Tensorwave projects.
   ```

3. _(Optional but recommended)_ Create a template `AGENTS.md` in new project
   roots using the **Plan Mode** section above.

---

## One-Sentence Mandate

> Build harnesses that make long-running agents **reliable**, **incremental**,
> **self-verifying**, and **handover-clean** using persistent artifacts, concise
> planning, and our existing skill system.
