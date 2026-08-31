# Agent Definitions

This directory holds the **skill GAN** personas (owned here) plus runtime copies of
loop personas pulled from the `loops` pin by `harness-bootstrap`. Do not hand-edit
the copied files — refresh them by re-running bootstrap after a pin move.

Code GAN, AVRIL/AXEL, and BRICK conductor personas are authored in
[`sycamore-hq/crossr-loops`](https://github.com/sycamore-hq/crossr-loops).

## Skill Remediation GAN Agents

- `skill-evaluator-agent.md` — Scores and proposes remediated SKILL.md files.
- `skill-remediator-agent.md` — Applies remediation under evaluator/reviewer pressure.
- `skill-reviewer-agent.md` — Final pedantic gate on skill quality.

## Usage

**Skill change review:**

> "Run the skill GAN using the agents in `.agents/agents/` on this SKILL.md."

**Code change review / AVRIL / AXEL:** use the personas in `crossr-loops`.
