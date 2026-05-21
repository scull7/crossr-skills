# Skills Overview

All reusable capabilities in this repository live under `.agents/skills/` and strictly follow the official [agentskills.io](https://agentskills.io) specification.

## The agentskills.io Format

Each skill is a single file:

```
.agents/skills/<name>/SKILL.md
```

With YAML frontmatter containing at minimum:

```yaml
---
name: skill-name
description: |
  One or two sentence description of what this skill does and when to use it.
---
```

The rest of the file contains the detailed guidance, rules, anti-patterns, and activation statements.

## Claude Compatibility

**Claude compatibility is generated, never hand-maintained.**

The canonical source is always the `.agents/skills/` directory.

When a project wants Claude support, it runs the generator (provided by `scripts/harness-bootstrap` or `scripts/sync-skills`) to produce the optional `.claude/skills/` and `.claude/commands/` copies.

This keeps cross-project reuse clean and ensures the official specification is the single source of truth.

## Current Skills

See the individual skill documents linked from the table of contents for details. The skills are grouped into:

- Core writing skills (`code-writer`, `rust-code-writer`)
- Quality & architecture skills (`rust-code-reviewer`, `rust-code-tester`, `rust-architect`)
- Domain skills (`rust-axum-backend`, `rust-frontend`, `rust-tui`, `rust-errors`)
- Meta skills (`agent-harness`)

All skills are designed to be combined. The typical activation pattern is:

> Using `code-writer` + `rust-code-writer` + `rust-axum-backend` + `agent-harness` for this task.