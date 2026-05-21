# Introduction

Welcome to the **CrossR Skills** documentation.

This book is the canonical reference for the skills and harness process developed in this repository.

## What is CrossR Skills?

A curated collection of high-quality **Agent Skills** together with a complete, self-hosting **harness** for building reliable, long-running AI coding agents.

The skills follow the official [agentskills.io](https://agentskills.io) specification. The process layer is defined in the [HARNESS-SPEC.md](https://github.com/scull7/crossr-skills/blob/main/HARNESS-SPEC.md) at the root of this repository.

## Why This Exists

Most AI coding agents are stateless. Every new session starts from scratch.

The harness turns those stateless sessions into something far more powerful:

- Persistent state across context resets
- Incremental, verifiable progress
- Extremely reviewable changes (target: < 10 minutes deep review per PR)
- Self-verifying handovers
- Mechanical quality enforcement via the GAN cycle (Generator + Adversary)

This combination has been battle-tested on real production work, including a 16-PR security-critical authorization chain.

## Core Philosophy

The same standards we apply to production Rust code apply here:

- Functional purity and stratified design
- Zero technical debt
- Handover-clean artifacts
- **HTML as a first-class human interface** for plans, reviews, and specifications

## How to Use This Book

- Start with the [Harness Overview](harness/overview.md) to understand the full system.
- The [Skills](../skills/overview.md) section documents the reusable capabilities.
- Follow [Getting Started](getting-started/bootstrap.md) to bootstrap the harness in your own projects.

This book is itself dogfooded — it was built using the same harness and process it describes.