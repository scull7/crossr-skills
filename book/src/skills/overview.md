# Skills Overview

All reusable capabilities live under `.agents/skills/` and follow the official [agentskills.io](https://agentskills.io) specification.

## Canonical structure

All skills in this repository follow the **canonical portable structure** and the **Harness Relationship (Stratified)** principle. Generic/core skills are fully harness-agnostic. Harness-layer and domain skills include a `## Harness Context (Stratified Disclosure)` block. The `skill-evaluator` skill is the authority for this standard.

The **public catalog** is the machine-readable allowlist in [`docs/public-skills.json`](https://github.com/scull7/crossr-skills/blob/main/docs/public-skills.json). Deep skill law lives in each skill’s `SKILL.md` in the repo — this book does **not** duplicate per-skill pages.

## Public catalog

| Skill | Purpose | Category | Activate with |
|-------|---------|----------|---------------|
| `code-writer` | Core coding philosophy (Grokking Simplicity + SICP) | Foundation | always with other skills |
| `rust-code-writer` | Idiomatic, pure, stratified, flat-combinator Rust | Rust Core | `code-writer` + this |
| `rust-code-reviewer` | Ruthless Rust code quality guardian | Quality | code GAN |
| `rust-code-tester` | Obsessive test coverage and error-path verification | Quality | code GAN |
| `rust-architect` | Torvalds-style system-level architecture gatekeeper | Architecture | code GAN final gate |
| `rust-team-lead` | GAN orchestrator for multi-agent Rust plan execution | Orchestration | AXEL inner GAN on Rust |
| `avril` | Planning GAN — blessed PBIs (PO → QA → CTO) | Orchestration | `code-writer` + `avril` |
| `axel` | Execution loop — blessed PBI → PETC + code GAN | Orchestration | `code-writer` + `axel` (+ stack) |
| `brick` | BRICK pipeline — informal spec to mutation-verified code | Orchestration | `code-writer` + `brick` |
| `brick-specifier` | BRICK stage 1 — approved tasks to pruned Gherkin | Orchestration | BRICK stage |
| `orchestrator-prompt` | Generate stateless AXEL/AVRIL orchestrator prompts per project | Orchestration | `code-writer` + `orchestrator-prompt` |
| `dashboard-prompt` | Wire a proven status dashboard to a project's real trackers | Orchestration | `code-writer` + `dashboard-prompt` |
| `chief-of-staff` | Portfolio status briefing built from verified project dashboards | Orchestration | `code-writer` + `chief-of-staff` |
| `rust-axum-backend` | Clean layered Axum HTTP APIs with policy gates | Backend | + `rust-code-writer` |
| `rust-frontend` | Leptos + WASM + Polars with anti-slop guidance | Frontend | + `rust-code-writer` |
| `rust-tui` | ratatui Component + Action + two-phase dispatch | TUI | + `rust-code-writer` |
| `rust-errors` | Layered thiserror handling (no anyhow) | Backend | + `rust-code-writer` |
| `agent-harness` | Full harness process (stacked PRs, GAN, HTML-first) | Harness | long-running sessions |
| `skill-evaluator` | Audit and remediate agent skills | Meta | skill remediation GAN |
| `voice-dna` | CrossR sharp-human writing voice with full unslop pattern list | Writing | human-facing artifacts |
| `unslop` | Voice-agnostic pass that strips AI tells from prose | Writing | any human-facing draft |

**N = 14** public skills. Items in `out` in `public-skills.json` (e.g. `obsidian-cli`, empty diataxis stubs) are **not** marketed.

## Pipeline skills

Orchestration pair: **`avril`** (plan) → **`axel`** (execute). See [Pipeline Overview](../pipeline/overview.md).

## Claude compatibility

Claude compatibility is **generated**, never hand-maintained. Canonical source: `.agents/skills/`.
