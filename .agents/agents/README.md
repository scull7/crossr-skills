# Agent Definitions

This directory contains reusable agent personas that encode the project's review and quality processes.

## Core GAN Agents

- `rust-reviewer-agent.md` — Applies the full `rust-code-reviewer` checklist with extreme pedantry.
- `rust-tester-agent.md` — Enforces testing standards from `rust-code-tester`.
- `rust-architect-agent.md` — Performs high-level architectural review.

## Recommended GAN Invocation Order

When reviewing a change, the following sequence is strongly preferred:

1. **Reviewer** (`rust-reviewer-agent`)
2. **Tester** (`rust-tester-agent`)
3. **Architect** (`rust-architect-agent`)

This order (Reviewer → Tester → Architect) mirrors the successful pattern used during the development of the v2 harness itself.

## Usage

Tell an agent:

> "Run the full GAN review using the agents in `.agents/agents/` on this change."

The agent should activate the three definitions in sequence and produce a consolidated report.