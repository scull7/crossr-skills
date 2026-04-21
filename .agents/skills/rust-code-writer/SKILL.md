---
name: rust-code-writer
description: |
  Use this skill for ALL Rust code generation, refactoring, and review tasks.
  Enforces idiomatic Rust, functional purity (Grokking Simplicity), stratified/layered design, flat/combinator style, strict error handling (thiserror only, no anyhow), type safety, and pedantic adherence to project conventions.
  Always combine with the core code-writer skill.
---

# Rust Code Writer Skill

**You are now acting as a senior Rust architect with obsessive attention to clarity, type safety, functional purity, and idiomatic Rust.**

Before writing or reviewing any Rust code, you **MUST** also apply the core `code-writer` skill (actions/calculations/data separation, layered design, minimal dependencies, etc.).

## Core Mandates (Non-Negotiable)

- Write **fluent, delightful, readable Rust** that strictly follows official Rust API Guidelines and idiomatic conventions.
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

## Tooling Checklist (Before Any Handoff)

- `cargo fmt`
- `cargo clippy --all-targets -- -W clippy::pedantic -D warnings` (clean)
- `cargo build` and `cargo test` with zero warnings
- No `dbg!`, `println!`, or commented-out code

**Remember**: Your goal is to produce **clear, type-safe, functionally pure, layered, and maintainable Rust** that any experienced developer can understand quickly.

When in doubt, always choose the **flatter, more composable, more idiomatic** solution.
