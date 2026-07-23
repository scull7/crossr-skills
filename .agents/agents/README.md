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

## AVRIL → AXEL Pipeline

```
Intent → AVRIL (planning GAN) → Blessed Backlog → AXEL (execution loop) → Done
```

### AVRIL Agents (Planning GAN)

**AVRIL** = Automated Visionary Review Iteration Loop (skill: `avril`).

Planning-only consensus on Product Backlog Items. Stops at a blessed backlog; does not implement code.

| Persona | File | AVRIL role |
|---------|------|------------|
| Planning Architect | `planning-architect-agent.md` | Generator — proposes/revises PBIs |
| Product Owner | `product-owner-agent.md` | Adversary 1 — value & scope |
| QA Architect | `qa-architect-agent.md` | Adversary 2 — testability & AC |
| Visionary CTO | `visionary-cto-agent.md` | Adversary 3 — strategy & trajectory (final gate) |

#### Recommended AVRIL invocation order

1. **Generator**: `planning-architect-agent` proposes PBIs (Pinto preferred when disclosed).
2. For each PBI, in order:
   1. `product-owner-agent`
   2. `qa-architect-agent`
   3. `visionary-cto-agent`
3. Any `REJECT` → generator revises → full three-adversary chain again for that item.
4. Item is done only when all three emit explicit `BLESS <id>`.
5. Orchestrator (`avril`) emits Blessed Backlog Summary and **stops**.

> "Run AVRIL using `code-writer` + `avril` and the agents in `.agents/agents/` on this intent."

### AXEL Agents (Execution Loop)

**AXEL** = Automated eXecution Loop (skill: `axel`).

Drives AVRIL-blessed PBIs through PETC + code GAN. Never writes code itself.

| Persona | File | AXEL role |
|---------|------|-----------|
| AXEL Conductor | `axel-conductor-agent.md` | Orchestrator — intake, board, PETC, AC evidence, tracking |
| Reviewer / Tester / Architect | `rust-*-agent.md` (or harness equivalents) | Code GAN adversaries per phase |

#### Recommended AXEL invocation order

1. **Intake**: Blessed Backlog Summary, `avril-blessed` marker, or explicit human PBI ids.
2. **Select** one ready PBI (`pinto next` when available).
3. **Plan** (concise + unresolved questions).
4. Board → in-progress; decompose into small phases.
5. Each phase: Generator (Rust: often `rust-team-lead`) → Reviewer → Tester → Architect (`BLESS` × 3) → commit + track.
6. **AC evidence** + verification matrix green → board review/done.
7. PBI Completion Record; next PBI or stop.

> "Run AXEL using `code-writer` + `axel` (+ language stack) and `axel-conductor-agent` on the blessed backlog."

**Scope changes mid-execution return to AVRIL.** AXEL does not re-bless product intent.

## Skill Remediation GAN Agents

- `skill-evaluator-agent.md` — Scores and proposes remediated SKILL.md files.
- `skill-remediator-agent.md` — Applies remediation under evaluator/reviewer pressure.
- `skill-reviewer-agent.md` — Final pedantic gate on skill quality.

## Usage

**Code change review:**

> "Run the full GAN review using the agents in `.agents/agents/` on this change."

**Backlog planning:**

> "Run AVRIL using `code-writer` + `avril` …"

**Blessed backlog execution:**

> "Run AXEL using `code-writer` + `axel` …"
