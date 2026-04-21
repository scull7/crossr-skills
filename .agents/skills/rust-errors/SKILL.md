---
name: rust-errors
description: |
  Specialized skill for error handling patterns in Rust.
  Teaches how to design clean, layered error types using thiserror, proper From impls, and avoiding inline map_err.
  Use this skill whenever designing error types or handling errors across module/layer boundaries.
---

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

## Activation Statement
 > Using `code-writer` + `rust-code-writer` + `rust-errors` for error handling in this module.
