# crossr-skills

**Where the Cross meets clean code.**

Curated agent skills for functionally obsessed developers.

Skills that light the way for functionally obsessed agents.  
Stewarding clean, reusable skills for agents who build with purpose.

---

## What is this?

A personal collection of high-quality **Agent Skills** (`.agents/skills/`) built for long-running, reliable AI agents.

The skills follow the official [Agent Skills specification](https://agentskills.io). The accompanying process layer is defined in [HARNESS-SPEC.md](HARNESS-SPEC.md) (stacked PRs, multi-tier verification harnesses, traceability, reviewability, and the PETC loop).

New projects should use `scripts/harness-bootstrap` to get started with the full harness.

Every skill follows the official [Agent Skills specification](https://agentskills.io) and is designed with the same ruthless standards I apply to my Rust code:

- **Functional purity** first
- **Stratified, layered design**
- **Zero technical debt**
- **Handover-clean** and self-verifying

---

## Core Philosophy

> “Write code that is layered, modular, and built from pure calculations operating on immutable data; isolate all actions; prefer the language’s standard library; use abstraction and higher-order functions to control complexity so that any human reader can understand and safely modify the system.”

This same mindset applies to every skill in this repo.

---

## Skills Included

| Skill                  | Purpose                                      | Category    |
|------------------------|----------------------------------------------|-------------|
| `code-writer`          | Core coding philosophy (Grokking Simplicity + SICP) | Foundation |
| `rust-code-writer`     | Idiomatic, pure, stratified Rust             | Rust Core   |
| `rust-code-reviewer`   | Ruthless code quality guardian               | Quality     |
| `rust-code-tester`     | Obsessive test coverage & verification       | Quality     |
| `rust-architect`       | Torvalds-style system-level architecture gatekeeper | Architecture |
| `rust-team-lead`       | GAN orchestrator for reliable multi-agent workflows | Orchestration |
| `rust-axum-backend`    | Axum HTTP APIs with clean layered design     | Backend     |
| `rust-frontend`        | Leptos + WASM + Polars frontends             | Frontend    |
| `rust-errors`          | Clean, layered error handling with `thiserror` | Backend     |
| `agent-harness`        | Persistent scaffolding for long-running agents (Tensorwave Edition) | Harness |

---

## How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/scull7/crossr-skills.git
   ```

2. Copy the skills you need into your project:
   ```bash
   cp -r crossr-skills/.agents/skills/your-project/.agents/skills/
   ```

3. Reference them in your `AGENTS.md` or `CLAUDE.md`.

---

## Principles

- **No garbage.** Every skill is reviewed by `rust-code-reviewer`, `rust-code-tester`, and `rust-architect` before blessing.
- **Small, focused, reusable.** One skill = one clear purpose.
- **Self-verifying.** Every skill includes usage rules.
- **Christian foundation.** Built with excellence as worship — subtle but intentional.

---

## License

MIT — use freely, improve boldly, give credit where it’s due.

---

## About

Maintained by **Nathan Sculli** (@scull7)  
Christian • Father • Functionally Obsessed

> “Whatever you do, work at it with all your heart, as working for the Lord.” — Colossians 3:23
