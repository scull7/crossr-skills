# crossr-skills Harness v2 Upgrade — Progress

This file tracks the work to evolve crossr-skills into the canonical base harness, following the exact stacked PR discipline proven in the ferro-wave authz 16-PR chain.

## Completed Phases

### PR 1–8 (COMPLETED)
- HARNESS-SPEC.md + beautiful review HTML
- agent-harness skill v2 (with authz lessons)
- Fines moved upstream into core writers
- Reviewer + Errors enhancements (reviewability, traceability, policy gates)
- rust-axum-backend production patterns
- rust-frontend generic anti-slop guidance
- New standalone rust-tui skill
- harness-bootstrap executable + templates

## Current Phase

### PR 9: Dogfooding the harness on crossr-skills itself
- Adding AGENTS.md, features.json, progress.md, justfile, CLAUDE.md
- Making the repo eat its own dogfood

## Verification Status
- All PRs follow < 10 minute deep review rule
- Content reviewed against approved plan and HARNESS-SPEC.md
- Stacked PR chain maintained on GitHub