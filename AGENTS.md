## Plan Mode

- Make every plan extremely concise. Sacrifice grammar for scannability.
- At the end of each plan, give a bulleted list of unresolved questions.
- Always follow the Plan → Execute → Test → Commit loop defined in HARNESS-SPEC.md.

## Skills

This project uses the official Agent Skills format from crossr-skills.

Core Skills (all located in `.agents/skills/`):

- **`code-writer`** — Foundational coding philosophy (Grokking Simplicity + SICP)
- **`rust-code-writer`** — Idiomatic, pure, stratified Rust
- **`rust-code-reviewer`** — Ruthless code quality guardian
- **`rust-code-tester`** — Obsessive test coverage & verification
- **`rust-architect`** — Torvalds-style architecture gatekeeper
- **`rust-team-lead`** — GAN orchestrator
- **`agent-harness`** — Persistent scaffolding for long-running agents (this spec)
- **`rust-axum-backend`**, **`rust-frontend`**, **`rust-errors`**, **`rust-tui`** — Domain skills

**All agents and contributors must follow the skills referenced above.**

See [HARNESS-SPEC.md](HARNESS-SPEC.md) for the complete process, artifacts, rituals, and stacked PR expectations.