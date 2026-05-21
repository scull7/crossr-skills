# The Harness — Overview

A **harness** is the persistent scaffolding that turns stateless AI coding sessions into reliable, multi-session agents that ship production-grade code with clean handovers.

## The Problem

Without a harness, agents suffer from:

- Context loss on every new session
- Inconsistent processes across projects
- Unreviewable giant diffs
- No mechanical self-critique
- Poor handoff quality between sessions or between human + agent

## The Solution

The CrossR harness provides a minimal but powerful set of artifacts, rituals, and processes that any project can adopt.

It is deliberately lightweight so that it can be bootstrapped into a new project in minutes, yet powerful enough to support 16+ PR security and infrastructure efforts.

## Key Components

| Component              | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `HARNESS-SPEC.md`      | The single source of truth for the process                              |
| `.agents/skills/`      | Canonical, reusable skills following the agentskills.io spec            |
| `AGENTS.md`            | Project-specific rules + Plan Mode contract                             |
| `features.json`        | Machine-readable tracking of work (phase → commits → atomic features)   |
| `progress.md`          | Human-readable narrative log of what was done and verified              |
| `justfile`             | Canonical entry points for build, test, validation, and site commands   |
| Stacked PR Discipline  | Every large body of work broken into tiny, reviewable PRs               |
| GAN Verification       | Mechanical Generator → Reviewer/Tester/Architect adversary loop         |
| HTML-First Artifacts   | Self-contained Tailwind HTML as the primary human-facing deliverable    |

## Design Goals

- **Incremental** — Never more than one small task per session
- **Reviewable** — Every PR should be deeply reviewable in under 10 minutes
- **Self-verifying** — Agents must run the full verification loop before declaring work complete
- **Self-hosting** — The harness is used to maintain the harness itself (as you are seeing right now)
- **Rust-dogfooded** — Where tools are needed, we prefer high-quality Rust tools (Zola, mdBook, etc.)

The rest of this section expands on each of these ideas.