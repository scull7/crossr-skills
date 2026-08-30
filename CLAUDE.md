# Agent Guidelines for crossr-skills

This repo is the portable skills catalog. Process lives in `sycamore-hq/crossr-harness`. Loops live in `sycamore-hq/crossr-loops`.

## Before writing or reviewing anything

1. Read the relevant skill in `.agents/skills/`
2. Read `AGENTS.md`
3. Follow the stacked PR + <10 minute review discipline

## Core Rules

- All skills live in `.agents/skills/` and follow the official agentskills.io format.
- Claude compatibility files (if present) are generated — do not edit them by hand.
- Every change must be part of a small, reviewable PR in the current stacked chain.
- Do not add orchestration skills (conductors, `orchestrator-prompt`, `dashboard-prompt`, `chief-of-staff`).

See AGENTS.md. Process spec: https://github.com/sycamore-hq/crossr-harness/blob/main/HARNESS-SPEC.md
