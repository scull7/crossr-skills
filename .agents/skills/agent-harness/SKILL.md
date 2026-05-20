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

# Agent Harness Skill (Tensorwave Edition) — v2

**This skill extends `code-writer` + `rust-code-writer`.**
You **MUST** apply the core coding philosophy first, then layer on these
harness-specific rules for any Tensorwave project.

**Primary reference:** Read and follow [HARNESS-SPEC.md](/HARNESS-SPEC.md) (the formal, executable specification). This skill is the practical implementation guide.

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

> Every project must have the items below. See HARNESS-SPEC.md for the full, normative definition.

### 1. Canonical Skills Location (Strict agentskills.io)

All reusable skills live in `.agents/skills/<name>/SKILL.md` and follow the official specification exactly.

**Claude compatibility is optional and generated.**  
A `generate-claude-compat` step (provided by the harness bootstrap) produces `.claude/skills/` and distilled `.claude/commands/` from the canonical `.agents/` sources. Never maintain duplicate copies by hand.

### 2. `init.sh` / `justfile`

One-command environment bootstrap and the exact build/test/clippy matrices used in CI and CLAUDE.md. Agents always use these.

### 3. `features.json` (phase/commits/features model)

Production shape proven on large work (ferro-wg and the 16-PR authz chain):

```json
{
  "phase7": {
    "status": "in_progress",
    "commits": [
      { "id": "c3", "title": "Help overlay", "status": "completed",
        "features": ["help_overlay_component", "help_overlay_tests"] }
    ]
  }
}
```

A JSON Schema + validation step is part of the harness.

### 4. `progress.md`

Commit-narrative human log ending with a "Verification Status" block (tooling + adversary reviews).

### 5. Git + Session Ritual

Clean commits + the mandatory start-of-session commands (see HARNESS-SPEC.md).

### 6. `AGENTS.md` (project root)

Contains skill references + the Plan Mode contract + link to this spec.

---

## Stacked PR Decomposition + Multi-Tier Verification Harnesses

The 16-PR `CD-1873-add-authz-subproject` chain in ferro-wave is the canonical real-world example of this harness at scale.

**Key patterns to internalize and enforce:**

- Decompose large or high-risk features into 8–16 small, stacked, reviewable PRs.
- Each PR must have an explicit "What this PR contains / Next PR / Verification" summary and a risk note.
- Use stable traceability IDs (tw-xxx, ADR-0002, Phase N, CD-1873, etc.) in PR titles, code comments, test names, and features.json.
- Build **literal verification harnesses** at multiple tiers:
  - Tier-1: in-process + parity snapshot tests (legacy equivalence)
  - Tier-2: real packaging (deb, Docker, Helm) + VM / k8s substrate tests
- Enforce **policy / security gates before any effectful or data-access work** (the mTLS CN-hostname binding check that runs before the Mongo lookup is the model).
- Add "reviewability comments" liberally so a human or agent can understand intent in < 2 minutes.
- Decouple documentation (beautiful single-file static deploy guide + its own CI) so docs never block code.

Document which of these patterns your project is using in its `AGENTS.md` or a `docs/HARNESS.md`.

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

1. **Plan** — Read `progress.md` + `features.json` + `git log` → propose next task + plan.
2. **Execute** — Implement using appropriate skills + reference to HARNESS-SPEC.md.
3. **Test** — Full matrix + `rust-code-reviewer` + `rust-code-tester` + `rust-architect`.
4. **Commit** — Small, reviewable diff + update artifacts + append to `progress.md`.

---

## Session Start Ritual (v2)

Every agent **must** run (at minimum):

```bash
git status && git log --oneline -10
cat progress.md | tail -n 30
# Updated jq for phase/commits shape (see HARNESS-SPEC.md)
./init.sh || just init
cargo check && cargo test --quiet
```

Then consult `features.json` for the next pending granular feature and the current phase/commit.

---

## Error Recovery & Self-Critique

- Agents must self-verify before marking work complete.
- Use `rust-code-reviewer` ruthlessly on every code change.
- Git is the safety net — **never** force-push; always commit.
- If state is broken → run `./init.sh` + revert to last good commit.

---

## Activation Statement (v2)

> Using `code-writer` + `rust-code-writer` + `agent-harness` +
> [relevant domain skills] + reference to HARNESS-SPEC.md for this task.

When bootstrapping a new project:

1. Run the `harness-bootstrap` executable (or equivalent) from the templates.
2. It creates the initial harness (AGENTS.md, features.json with schema, justfile, .agents/ guidance, Claude generator step, etc.).
3. Commit the empty harness.
4. All future work is tracked and executed inside the harness defined in HARNESS-SPEC.md.

---

## How to Include This Skill

1. Save this file to `.agents/skills/agent-harness/SKILL.md`.
2. Update your root `AGENTS.md` (Core Skills section) with a link to `HARNESS-SPEC.md`.
3. Run the harness bootstrap when starting a new project.

---

## One-Sentence Mandate

> Build harnesses that make long-running agents **reliable**, **incremental**, **self-verifying**, and **handover-clean** using persistent artifacts, concise planning, strict agentskills.io compliance, and the stacked multi-tier verification patterns proven on large security-critical work.