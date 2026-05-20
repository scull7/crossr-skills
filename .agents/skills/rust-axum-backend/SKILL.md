---
name: rust-axum-backend
description: |
  Specialized skill for building Rust HTTP APIs and web servers using Axum.
  Extends `rust-code-writer` with Axum-specific patterns, layered design, error handling, and middleware usage.
  Use this skill whenever building or modifying backend HTTP servers.
---

# Rust Axum Backend Skill

**This skill extends `rust-code-writer`.**  
You **MUST** apply `code-writer` + `rust-code-writer` first, then layer on these Axum-specific rules.

## Core Axum Backend Rules

- **Handler Signature**: Return `Result<Response, AppError>` (or equivalent project error type) from route handlers to enable centralized error handling.
- **Layered Extractors**: Use proper layered extractors (`State`, `Json`, `Path`, `Query`, etc.). Never rely on global mutable state.
- **Shared State**: Use properly typed shared state structs (usually via `State<AppState>`). All state must be `Send + Sync + Clone` where required.
- **Middleware**: Apply `tower` middleware for:
  - Tracing / logging
  - Timeouts
  - Compression (`tower-http::compression`)
  - CORS (when needed)
  - Security headers
- **CPU-bound Work**: Offload any blocking or heavy CPU work to `tokio::task::spawn_blocking`.
- **Error Handling**: Use the project's layered error strategy. Route handlers should return the application-level error type.

## Recommended Patterns

- Keep handlers thin: extract data → call service layer → convert to response.
- Business logic belongs in services/repositories (pure calculations where possible).
- Use `axum::response::IntoResponse` for custom error responses.
- Prefer structured JSON errors over plain text.

## Production Patterns from Ferro-Wave Event Gateway

When building real Axum services at scale (see waveq-event-gateway):

- **Thin transport crates**: The `*-http` crate should contain *only* handlers, extractors, and middleware. All domain logic, authz, validation, and error types live in a `*-core` crate.
- **AppError newtype + exhaustive mapping**: Wrap the domain error and implement `IntoResponse` with a match that produces structured JSON. Never leak internal details on 5xx errors. Map policy denials to distinct status codes.
- **Layered custom extractors**: Use `FromRequestParts` + `FromRef<AppState>` for things like `AuthedPrincipal`. Perform the security gate (e.g. CN-hostname binding) early, before any DB access.
- **test-utils feature**: Expose test helpers from core under a `test-utils` feature so integration test crates can construct realistic state without leaking test code into production.
- **router() + serve()**: Expose `pub fn router(state: AppState) -> Router` and `pub async fn serve(...)`. Document the route table in the module docs.
- **Feature-gated transports**: In the server binary crate, use optional dependencies + `#[cfg(feature = "rest")]` / `#[cfg(feature = "grpc")]` with a `compile_error!` if neither is enabled.

These patterns were battle-tested in the ferro-wave gateway and are now the expected baseline for new Axum work.

## When to Use This Skill

Use `rust-axum-backend` whenever the task involves:
- Creating or modifying Axum routes
- Building HTTP handlers
- Adding middleware
- Designing `AppState` or shared application state
- Implementing backend APIs

**Activation**: When the user asks for backend, HTTP, API, or Axum-related work, explicitly say:

> Using `code-writer` + `rust-code-writer` + `rust-axum-backend` for this Axum backend task.

---

**Always prioritize functional purity, stratified design, and flat code** from `rust-code-writer` even when building web servers.
