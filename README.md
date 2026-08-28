# crossr-skills

**Where the Cross meets clean code.**

High-quality agent skills and a battle-tested harness for building reliable, long-running AI coding agents.

> Forged in the Cross. Built for craft.

---

## Live Public Presence

This repository dogfoods its own harness. The public website and documentation were built using the exact process described here.

- **Marketing Site**: [https://scull7.github.io/crossr-skills/](https://scull7.github.io/crossr-skills/)
- **Documentation**: [https://scull7.github.io/crossr-skills/docs/](https://scull7.github.io/crossr-skills/docs/)

---

## What is this?

A curated collection of **Agent Skills** (`.agents/skills/`) plus a complete, self-hosting **harness process** for teams that want their AI agents to ship production-grade code across many sessions.

The skills strictly follow the [agentskills.io](https://agentskills.io) specification. The process layer (stacked PR discipline, multi-tier verification, PETC loop, GAN reviews, HTML as a first-class human artifact, etc.) is defined in [HARNESS-SPEC.md](HARNESS-SPEC.md).

New projects can be bootstrapped in minutes with:

```bash
./scripts/harness-bootstrap /path/to/your-project
```

---

## Quick Start

```bash
git clone https://github.com/scull7/crossr-skills.git
./crossr-skills/scripts/harness-bootstrap /path/to/your-new-project
cd /path/to/your-new-project
just harness-validate
```

This creates a full harness including `AGENTS.md`, `features.json`, `progress.md`, `justfile`, and the canonical `.agents/skills/` directory.

It also installs the OpenCode slash commands `/avril` (planning) and `/axel` (execution) under `.opencode/`. **Restart opencode** to pick them up. Existing `.opencode/` files are never overwritten — the bootstrap reports which ones it kept.

---

## Skills

All skills are designed with the same standards applied to production Rust code: functional purity, stratified design, zero technical debt, and handover-clean artifacts.

Public catalog SSOT: [`docs/public-skills.json`](docs/public-skills.json) (14 skills). Names below must match that file.

| Skill                  | Purpose                                              | Category      |
|------------------------|------------------------------------------------------|---------------|
| `code-writer`          | Core coding philosophy (Grokking Simplicity + SICP) | Foundation    |
| `rust-code-writer`     | Idiomatic, pure, stratified, flat-combinator Rust    | Rust Core     |
| `rust-code-reviewer`   | Ruthless Rust code quality guardian                  | Quality       |
| `rust-code-tester`     | Obsessive test coverage and error-path verification  | Quality       |
| `rust-architect`       | Torvalds-style system-level architecture gatekeeper  | Architecture  |
| `rust-team-lead`       | GAN orchestrator for multi-agent Rust plan execution | Orchestration |
| `avril`                | Planning GAN — blessed PBIs (PO → QA → CTO)          | Orchestration |
| `axel`                 | Execution loop — blessed PBI → PETC + code GAN       | Orchestration |
| `brick`                | BRICK pipeline — informal spec to mutation-verified code | Orchestration |
| `brick-specifier`       | BRICK stage 1 — approved tasks to pruned Gherkin | Orchestration |
| `brick-coder`          | BRICK stage 2 — Gherkin to red tests then green code | Orchestration |
| `orchestrator-prompt`  | Generate stateless AXEL/AVRIL orchestrator prompts per project | Orchestration |
| `dashboard-prompt`     | Wire a proven status dashboard to a project's real trackers | Orchestration |
| `chief-of-staff`       | Portfolio status briefing built from verified project dashboards | Orchestration |
| `rust-axum-backend`    | Clean layered Axum HTTP APIs with policy gates       | Backend       |
| `rust-frontend`        | Leptos + WASM + Polars with anti-slop guidance       | Frontend      |
| `rust-tui`             | ratatui Component + Action + two-phase dispatch      | TUI           |
| `rust-errors`          | Layered thiserror handling (no anyhow)               | Backend       |
| `agent-harness`        | Full harness process (stacked PRs, GAN, HTML-first)  | Harness       |
| `skill-evaluator`      | Audit and remediate agent skills against CrossR standards | Meta     |
| `voice-dna`            | CrossR sharp-human writing voice with full unslop pattern list | Writing       |
| `unslop`               | Voice-agnostic pass that strips AI tells from prose  | Writing       |

**Not in the public catalog:** `obsidian-cli`, `diataxis` (deferred), empty `diataxis-*` stubs — see `out` in `docs/public-skills.json`.

Flagship pipeline: **Intent → AVRIL → Blessed Backlog → AXEL → Done** ([docs](https://scull7.github.io/crossr-skills/docs/pipeline/overview.html)).

See the [full documentation](https://scull7.github.io/crossr-skills/docs/) for pipeline chapters, catalog, and bootstrap.

---

## The Harness

This repo ships with a complete, production-proven harness:

- **HARNESS-SPEC.md** – The canonical process specification
- Stacked, reviewable PRs (< 10 min deep review target)
- Mechanical GAN reviews (Reviewer + Tester + Architect agents)
- `features.json` + `progress.md` for traceable incremental work
- `scripts/harness-bootstrap` – one-command harness installation
- HTML as the primary human-facing artifact format

Everything in this repository (including the public website) was built using this harness.

---

## Core Philosophy

> “Write code that is layered, modular, and built from pure calculations operating on immutable data; isolate all actions; prefer the language’s standard library; use abstraction and higher-order functions to control complexity so that any human reader can understand and safely modify the system.”

This mindset applies to every skill and to the harness itself.

---

## Principles

- **No garbage** — Every skill is reviewed by `rust-code-reviewer`, `rust-code-tester`, and `rust-architect`.
- **Small and focused** — One skill = one clear responsibility.
- **Self-verifying** — Skills contain their own usage rules and activation statements.
- **Dogfooded** — The harness is used to maintain the harness (and its public site).

---

## Contributing

Contributions are welcome, especially improvements to the harness process and new high-quality skills that follow the same standards.

Please read [HARNESS-SPEC.md](HARNESS-SPEC.md) and follow the stacked PR + GAN discipline used in this repository.

---

## License

MIT — use freely, improve boldly, give credit where it’s due.

---

## About

Maintained by **Nathan Sculli** (@scull7)  
Christian • Father • Functionally Obsessed

> “Whatever you do, work at it with all your heart, as working for the Lord.” — Colossians 3:23
