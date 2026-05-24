---
name: code-writer
description: |
  Foundational, model- and harness-agnostic coding philosophy skill.
  Establishes the universal, portable principles for writing human-readable, simple, intellectually manageable code: immutable data, pure calculations, isolated actions, stratified layering, and standard-library preference.
  Inspired by Grokking Simplicity and SICP. All code generation, refactoring, and review MUST follow this skill. It is the required base layer for every language-specific or domain-specific skill.
---

# Code Writer Skill

**This is the core coding philosophy skill.**  
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

### Anti-Pattern Severity

Bad patterns carry real cost and are **prevented at generation time**, not merely caught in review:

- Deep nesting, unreadable code, large commits/PRs, "AI slop", or language-specific mechanisms that suppress important static analysis warnings (e.g. lints) are treated as technical debt.

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
- Always show a standard-library solution first. Only suggest an external library or package if truly necessary, with clear justification.

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

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before generating or planning any code.
- The agent explicitly identifies and separates Data, Calculations, and Actions in its reasoning and the structure of generated code.
- Generated code is organized into stratified layers (primitives/data, domain calculations/combinators, action orchestration) with uniform abstraction per layer.
- The agent always offers a standard-library solution first and only proposes third-party dependencies after clear justification plus explicit user approval.
- Every function in output code is short and focused, uses intention-revealing names, and restricts comments to explaining why rather than what the code does.
- The agent detects and refactors away deep nesting, large functions, entangled logic, or low-quality patterns in favor of composition, higher-order functions, and minimalism.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the universal base contract for all code work (precondition: none). Language- or domain-specific skills specialize it by adding concrete rules, idioms, and tooling examples (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Write code that is layered, modular, and built from pure calculations operating on immutable data; isolate all actions; prefer the language’s standard library; use abstraction and higher-order functions to control complexity so that any human reader can understand and safely modify the system.”

---

This skill is the universal foundation for all code written according to its principles.  
All language-specific or domain-specific skills (e.g., your language-specific reviewer skill) **MUST** build upon and never contradict this `code-writer` skill.  

**When using this skill**: Always combine it with the appropriate language-specific or domain reviewer skill for the target language/domain.
