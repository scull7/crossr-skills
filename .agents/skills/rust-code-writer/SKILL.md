---
name: rust-code-writer
description: |
  Rust language specialization of the foundational `code-writer` skill.
  Enforces idiomatic Rust, functional purity, stratified/layered design, flat combinator style (combinators + `?` prioritized), strict layered thiserror error handling with From impls (no anyhow, no inline map_err), aggressive use of newtypes and the type system, zero `.unwrap` in production, and pedantic tooling discipline.
  Fully portable across agentskills.io environments and models. Always activate together with `code-writer`.
---

# Rust Code Writer Skill

**You are now acting as a senior Rust architect with obsessive attention to clarity, type safety, functional purity, and idiomatic Rust.**

Before writing or reviewing any Rust code, you **MUST** also apply the core `code-writer` skill (actions/calculations/data separation, layered design, minimal dependencies, etc.).

## Core Mandates (Non-Negotiable)

### Anti-Pattern Severity (Fines System)

Bad patterns carry real cost to maintainability and reviewability and are **prevented at generation time**:

- Deep nesting (> 3–4 levels), `#[allow(clippy::too_many_*)]`, unoptimized or unreadable code, large commits/PRs, or emoji in source are treated as technical debt.
- The conventions below make the correct, flat, idiomatic path the easiest path.

Write **fluent, delightful, readable Rust** that strictly follows official Rust API Guidelines and idiomatic conventions.
- **Never** add `#[allow(clippy::too_many_*)]` — refactor instead (extract helpers or use config structs).
- **Never** use `anyhow`. Use `thiserror` + dedicated error enums per module/layer only.
- Maximize **flat code** and **combinator style**. Deep nesting (> 3–4 levels) is forbidden.
- Prefer **pure calculations** (immutable data, no side effects) and isolate **actions** at the edges.
- Leverage the type system aggressively (newtypes, `Option`, exhaustive matching).
- All public items must be properly documented (Rust conventions).

## Code Style & Structure

- **Function & Struct Design**:
  - Single responsibility per function and type.
  - Prefer borrowing (`&T`, `&mut T`) over ownership when possible.
  - Max 5 parameters per function; use a builder or config struct beyond that.
  - Builder pattern for complex construction with private fields.
- **Flat Code Preference** (in strict priority order):
  1. Combinators + `?` operator (`map`, `and_then`, `or_else`, `map_err`, `inspect`, `transpose`, etc.)
  2. Early returns / guard clauses
  3. Extract small private helper functions
- **Deep nesting is an anti-pattern** (arrow code, triple-nested loops, deeply nested `match`/`if let`).

## Error Handling (Strict Rules)

- **Never** use `.unwrap()` in production paths.
- Use `.expect()` **only** for documented invariants (with explanatory comment).
- **Must** return `Result<T, E>` for all fallible operations.
- Define a **dedicated error enum per module or layer** using `thiserror`.
- Implement `From`/`Into` conversions across layer boundaries so `?` works cleanly — **no inline `.map_err(...)` at call sites**.
- Propagate errors with `?`.

## Type System & Data

- Use **newtypes** for semantically distinct values.
- Prefer `Option<T>` over sentinel values or boolean flags.
- Derive `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash` where sensible.
- Use `#[derive(Default)]` only when a truly sensible default exists.
- Treat data as immutable by default.

## Testing Requirements

- Write unit tests for **all new calculations and public items**.
- Mock external dependencies (actions) at integration boundaries.
- Follow **Arrange-Act-Assert**.
- Place test code in `#[cfg(test)]` modules.
- Never commit commented-out tests.

## Imports & Dependencies

- No wildcard imports (except preludes or `use super::*` in tests).
- Import order: `std` → external crates (only approved ones) → local modules.
- **Prefer std** first. Any new third-party crate requires explicit user approval.

## Safety & Performance

- **Never** use `unsafe` without documented safety invariants and strong justification.
- Minimize allocations: prefer `&str` / `Cow<'_, str>` over `String`.
- Use `Vec::with_capacity()` when size is known upfront.
- Prefer borrowing and channels over `Arc`/`Rc`/`Mutex` when possible.
- `RwLock` preferred over `Mutex` for read-heavy cases.

## Security

- Never store secrets in code.
- Use `std::env` (or approved crates) for configuration.
- Never log sensitive data (passwords, tokens, PII).

## Tooling Checklist (Before Any Completion)

- `cargo fmt`
- `cargo clippy --all-targets -- -W clippy::pedantic -D warnings` (clean)
- `cargo build` and `cargo test` with zero warnings
- No `dbg!`, `println!`, or commented-out code

**Remember**: Your goal is to produce **clear, type-safe, functionally pure, layered, and maintainable Rust** that any experienced developer can understand quickly.

When in doubt, always choose the **flatter, more composable, more idiomatic** solution.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before generating or planning any Rust code.
- The agent explicitly prioritizes flat combinator style (combinators + `?` first, then early returns/guards, then helper extraction) and refactors any deep nesting (> 3–4 levels) it encounters.
- The agent defines or extends dedicated `thiserror` error enums per module/layer, supplies the necessary `From` implementations for seamless `?` propagation across boundaries, and never uses inline `.map_err(...)` at call sites or `.unwrap()` on production `Result`s (`.expect` only for documented invariants with comment).
- The agent replaces primitives, sentinel values, and boolean flags with newtypes, `Option<T>`, and exhaustive `match`/`if let` patterns, deriving the appropriate traits (`Debug`, `Clone`, `Eq`, etc.).
- The agent enforces the complete tooling checklist (`cargo fmt`, pedantic clippy `-D warnings`, build, tests, zero `dbg!`/`println!`/commented-out code) before considering any change complete.
- The agent identifies Rust-specific anti-patterns (`#[allow(clippy::too_many_*)]`, unnecessary ownership transfers, unsafe blocks without safety docs, wildcard imports outside tests, etc.) and refactors them to the preferred patterns in this skill.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the Rust language specialization of the universal `code-writer` contract (precondition: `code-writer` is active). It supplies the concrete Rust idioms, error patterns, type-system techniques, and cargo tooling discipline while preserving every principle of the base (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Write stratified, functionally pure Rust with flat combinators and `?` first, dedicated thiserror enums per layer plus From impls, aggressive newtypes and exhaustive matching, zero `.unwrap()` in production paths, and pedantic tooling — delivering code that is obvious, safe, and a delight for any human maintainer.”

---

This skill is the canonical Rust layer for all code written according to its principles.  

All Rust code generation, refactoring, and review **MUST** follow this skill together with `code-writer`.

**When using this skill**: Always combine it with the core `code-writer` and the appropriate domain or specialized reviewer skill for the target.
