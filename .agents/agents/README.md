# Agent Definitions

This directory contains reusable agent personas that encode the project's review and quality processes.

## Core GAN Agents (Code Execution)

- `rust-reviewer-agent.md` — Applies the full `rust-code-reviewer` checklist with extreme pedantry.
- `rust-tester-agent.md` — Enforces testing standards from `rust-code-tester`.
- `rust-architect-agent.md` — Performs high-level architectural review.

### Recommended code GAN invocation order

When reviewing a change, the following sequence is strongly preferred:

1. **Reviewer** (`rust-reviewer-agent`)
2. **Tester** (`rust-tester-agent`)
3. **Architect** (`rust-architect-agent`)

This order (Reviewer → Tester → Architect) mirrors the successful pattern used during the development of the v2 harness itself.

## AVRIL Agents (Planning GAN)

**AVRIL** = Automated Visionary Review Iteration Loop (skill: `avril`).

Planning-only consensus on Product Backlog Items. Stops at a blessed backlog; does not implement code.

| Persona | File | AVRIL role |
|---------|------|------------|
| Planning Architect | `planning-architect-agent.md` | Generator — proposes/revises PBIs |
| Product Owner | `product-owner-agent.md` | Adversary 1 — value & scope |
| QA Architect | `qa-architect-agent.md` | Adversary 2 — testability & AC |
| Visionary CTO | `visionary-cto-agent.md` | Adversary 3 — strategy & trajectory (final gate) |

### Recommended AVRIL invocation order

1. **Generator**: `planning-architect-agent` proposes PBIs (Pinto preferred when disclosed).
2. For each PBI, in order:
   1. `product-owner-agent`
   2. `qa-architect-agent`
   3. `visionary-cto-agent`
3. Any `REJECT` → generator revises → full three-adversary chain again for that item.
4. Item is done only when all three emit explicit `BLESS <id>`.
5. Orchestrator (`avril`) emits Blessed Backlog Summary and **stops** (execution bridge is a follow-up skill).

Tell an agent:

> "Run AVRIL using `code-writer` + `avril` and the agents in `.agents/agents/` on this intent."

## Skill Remediation GAN Agents

- `skill-evaluator-agent.md` — Scores and proposes remediated SKILL.md files.
- `skill-remediator-agent.md` — Applies remediation under evaluator/reviewer pressure.
- `skill-reviewer-agent.md` — Final pedantic gate on skill quality.

## Usage

Tell an agent:

> "Run the full GAN review using the agents in `.agents/agents/` on this change."

The agent should activate the three code definitions in sequence and produce a consolidated report.

For backlog planning, use the AVRIL sequence above instead of the code trio.
