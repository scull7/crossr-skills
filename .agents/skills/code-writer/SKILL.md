---
name: code-writer
description: |
  Core code writing skill for the entire project. 
  Enforces the project's permanent coding philosophy inspired by Grokking Simplicity and SICP.
  All code generation, refactoring, and reviews MUST follow this skill.
  This is the foundational skill that all other language-specific skills build upon.
---

# Code Writer Skill

**This is the project's core coding philosophy skill.**  
All agents generating or modifying code **MUST** follow this skill at all times.

## Purpose

Produce code that is:
- Primarily written **for humans to read**.
- As simple as possible while solving the problem.
- Built to control intellectual complexity through abstraction, modularity, and functional thinking.

Inspired by *Grokking Simplicity* (Eric Normand) and *Structure and Interpretation of Computer Programs* (SICP).

## Core Mindset (Always Apply)

1. **Programs are for people first, machines second.**
2. **Distinguish three kinds of things** in every codebase:
   - **Data** – Immutable facts and values.
   - **Calculations** – Pure, deterministic functions with no side effects.
   - **Actions** – Anything involving time, external state, I/O, mutation, or non-determinism.
3. **Stratified / Layered Design** – Organize code into clear layers of abstraction.
4. **Control complexity by pulling things apart** – Never add entanglement.

## Mandatory Rules

### Actions, Calculations & Data
- Prefer calculations. Push logic into pure functions.
- Isolate actions at the edges of the system. Never mix actions with calculations.
- Treat data as immutable by default.
- Explicitly separate actions vs calculations when writing or reviewing code.

### Abstraction & Modularity
- Use procedural and data abstraction relentlessly.
- Every module and function must have a single, clear purpose.
- Prefer small, focused, reusable modules.
- Use higher-order functions and composition liberally (`map`, `filter`, `reduce`, function composition, etc.).

### Third-Party Dependencies
- **Prefer the language’s standard library first**.
- Adding any third-party dependency **requires explicit user approval**.
- Always show a standard-library solution first. Only suggest a crate/library if truly necessary, with clear justification.

### Stratified Design & Layering
- Code must be organized in layers:
  - Lowest: primitives and data
  - Middle: domain-specific calculations and combinators
  - Highest: orchestration of actions and top-level logic
- Functions at the same layer must use the same level of abstraction.
- Keep the call graph clear and understandable.

### Functional Style (Default)
- Favor pure functional style.
- Use immutable data structures and explicit state when needed.
- Avoid hidden side effects inside calculations.

### Clarity & Readability
- Use meaningful, intention-revealing names.
- Keep functions short and focused (< 20–30 lines preferred).
- Write code that can be understood at a high level without reading every detail.
- Comments explain *why*, not *what*.

## Practical Rules
- Apply these principles in a language-agnostic way (adapt to Rust, TypeScript, Python, etc.).
- Incremental adoption is allowed — refactor one calculation at a time.
- Calculations must be trivially unit-testable.
- Prefer explicit error handling over exceptions when possible.

## One-Sentence Mandate (Memorize This)

> “Write code that is layered, modular, and built from pure calculations operating on immutable data; isolate all actions; prefer the language’s standard library; use abstraction and higher-order functions to control complexity so that any human reader can understand and safely modify the system.”

---

This skill is the **foundation** for all code in the project.  
All language-specific skills (including `rust-code-reviewer`) **MUST** build upon and never contradict this `code-writer` skill.

**When using this skill**: Always combine it with the appropriate language-specific reviewer (e.g., `rust-code-reviewer` for Rust code).
