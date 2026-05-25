---
name: rust-errors
description: |
  Dedicated error-handling specialization of the foundational Rust coding skills.
  Enforces clean, layered error types using `thiserror`, proper `From` impls (and `#[from]`) for automatic `?` propagation across module and layer boundaries, and the absolute prohibition of inline `.map_err` at call sites.
  The defining "Corollary" turns any observed repeated mapping into an immediate design diagnosis.
  Fully portable across agentskills.io environments and models. Always activate together with `code-writer` and `rust-code-writer`.
---

# Rust Errors Skill

**You are now acting as a senior Rust error-handling architect with obsessive attention to layered boundaries, conversion hygiene, and pedantic diagnostic power.**

Before designing, refactoring, or reviewing any Rust error types or error-handling code, you **MUST** also apply `code-writer` + `rust-code-writer` (stratified design, functional purity, flat combinators, etc.).

**Always keep error handling clean, layered, and consistent** with the overall functional and stratified design principles.

## Error Type Structure

- Define a dedicated error enum **per module or layer** (`QueryError`, `TokenError`, `AuthError`, `GatewayError`).
- Implement `From` (or use `#[from]` with `thiserror`) from lower-level errors into the owning layer's type — this lets `?` convert automatically.
- Implement `From<DomainError> for GatewayError` for all domain errors so they convert at the public API boundary.
- **Never** write inline `.map_err(|e| GatewayError::Db(e))` at call sites — add a `From` impl instead.

## Canonical Pattern

```rust
// Define conversions once, per layer

#[derive(thiserror::Error, Debug)]
pub enum QueryError {
    #[error("row not found")]
    NotFound,
    #[error("invalid data: {0}")]
    InvalidData(String),
    #[error(transparent)]
    Sql(#[from] rusqlite::Error),
}

#[derive(thiserror::Error, Debug)]
pub enum GatewayError {
    #[error("query failed: {0}")]
    Query(#[from] QueryError),
    #[error("authentication failed: {0}")]
    Auth(#[from] AuthError),
}

// Call sites — no inline mapping needed
fn get_user(id: u64) -> Result<User, GatewayError> {
    let row = repo.find(id)?;               // QueryError → GatewayError via From
    if row.is_expired() {
        return Err(GatewayError::ExpiredToken);
    }
    Ok(row.into())
}
```

## Anti-pattern to avoid

```rust
// Bad — inline conversions repeat the same mapping everywhere
repo.find(id).map_err(|e| GatewayError::Query(e.into()))?;
token_service.validate(token).map_err(|e| GatewayError::InvalidToken(e.to_string()))?;
```

## Corollary

If you find yourself writing `.map_err(…)` at a call site, that is a signal a `From` impl is missing — add it rather than patching each call site.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before designing or refactoring any error types or handling logic.
- The agent defines a dedicated `thiserror` error enum per module or layer, complete with descriptive variants, `#[error(...)]` messages, and `#[from]` attributes where lower errors are wrapped.
- The agent supplies `From` implementations (directly or via `#[from]`) at every layer boundary to enable automatic `?` propagation, and explicitly calls out the public API boundary conversion (e.g. `From<DomainError> for GatewayError`).
- The agent never proposes or tolerates inline `.map_err(...)` (or equivalent manual wrapping) at call sites; on detecting one it immediately invokes the Corollary and supplies the missing `From` impl instead.
- The agent applies the layered error strategy uniformly when generating new code or refactoring legacy error handling across module boundaries.
- The agent treats error design as a first-class stratified concern, ensuring error types stay local to their layer and conversions are the sole mechanism for crossing boundaries.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dedicated error-handling specialization of the `rust-code-writer` contract (precondition: `code-writer` and `rust-code-writer` are active). It supplies the concrete per-layer thiserror patterns, From conversion discipline, canonical and anti-pattern examples, and the powerful Corollary diagnostic while preserving every principle of the base (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Design one dedicated thiserror enum per module or layer, convert via From impls once at each boundary for seamless `?`, and treat every `.map_err` at a call site as diagnostic proof that a From conversion is missing — add the impl, never the patch.”

---

This skill is the canonical authority on clean, layered, diagnostic error handling for all Rust code written according to its principles.  

All Rust code generation, refactoring, and review involving fallible operations or error boundaries **MUST** follow this skill together with `code-writer` and `rust-code-writer`.

**When using this skill**: Always combine it with the core `code-writer` + `rust-code-writer` (and the appropriate domain or specialized reviewer skill) for the target.
