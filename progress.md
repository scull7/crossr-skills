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

## Verification & Completion (Post-Merge)

The full stacked PR chain (PRs #1–#10) has been merged.

### Post-merge verification performed
- All mandatory artifacts present (HARNESS-SPEC.md, AGENTS.md, features.json, progress.md, justfile, CLAUDE.md, rust-tui skill, bootstrap script + templates)
- `scripts/harness-bootstrap` tested successfully in clean environments
- Minor bugs in the bootstrap script fixed during verification (heredoc + chmod issues)
- features.json updated to mark the entire "harness-v2" effort as completed

## Final Status
**Harness v2 + GAN Mechanization is complete.**

The repository is now self-hosting its own process, including mechanical GAN agent definitions and improved tooling.

All future work on crossr-skills (and consuming projects) should follow the rules in HARNESS-SPEC.md.

The mechanization effort (GAN agent definitions + hardening) was delivered via a second stacked PR chain (`gan/01` through `gan/05`).

## Skill Remediation (2026 Dogfood of the Harness on Its Own Skills)

**Phase initiated via Setup PR.**

- Added permanent skill GAN agents (`.agents/agents/skill-evaluator-agent.md`, `skill-remediator-agent.md`, `skill-reviewer-agent.md`) modeled exactly on the rust-* trio.
- Added `"skill-remediation"` phase + 13 traceable commits (setup + sr/01–sr/12) to `features.json`.
- All work follows the approved plan (see session plan.md for full PETC + stratified harness-agnosticism policy + hybrid simulation verification rubric).
- Explicit human approval gate required after Setup PR merges before sr/01 begins.
- Each subsequent PR will contain: one skill (or self-remediation), its remediation-report.html, minimal impacted docs, features/progress updates, full GAN + hybrid simulation evidence, and `just harness-validate` PASS.

**Current status:** Setup PR in preparation. 12 individual skill PRs to follow after gate.