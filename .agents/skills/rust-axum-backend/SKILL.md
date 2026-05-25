---
name: rust-axum-backend
description: |
  Specialized skill for building Rust HTTP APIs and web servers using Axum.
  Extends `rust-code-writer` with Axum-specific patterns, layered design, error handling, and middleware usage.
  Harness-layer domain skill with clean stratified disclosure. Fully portable across agentskills.io environments and models when paired with a compatible harness. Always activate together with `code-writer` + `rust-code-writer`.
---

# Rust Axum Backend Skill

**This skill extends `rust-code-writer`.**  
You **MUST** apply `code-writer` + `rust-code-writer` first, then layer on these Axum-specific rules.

## Harness Context (Stratified Disclosure)

This is a harness-layer domain skill for Axum HTTP backend development in Rust.

The core content below is written in portable language: the rules for handler signatures, layered extractors, shared state, middleware application, offloading CPU work, error handling with `IntoResponse`, and keeping handlers thin are universal Axum best practices that apply in any agentskills.io Rust project using Axum.

The battle-tested production patterns from the ferro-wave event gateway are isolated here under qualified disclosure only. When the invoking harness discloses a project using a similar multi-crate Axum architecture, the following high-signal patterns (refined in that codebase) are recommended realizations:
- **Thin transport crates**: The `*-http` crate should contain *only* handlers, extractors, and middleware. All domain logic, authz, validation, and error types live in a `*-core` crate.
- **AppError newtype + exhaustive mapping**: Wrap the domain error and implement `IntoResponse` with a match that produces structured JSON. Never leak internal details on 5xx errors. Map policy denials to distinct status codes.
- **Layered custom extractors**: Use `FromRequestParts` + `FromRef<AppState>` for things like `AuthedPrincipal`. Perform the security gate (e.g. CN-hostname binding) early, before any DB access.
- **test-utils feature**: Expose test helpers from core under a `test-utils` feature so integration test crates can construct realistic state without leaking test code into production.
- **router() + serve()**: Expose `pub fn router(state: AppState) -> Router` and `pub async fn serve(...)`. Document the route table in the module docs.
- **Feature-gated transports**: In the server binary crate, use optional dependencies + `#[cfg(feature = "rest")]` / `#[cfg(feature = "grpc")]` with a `compile_error!` if neither is enabled.

These patterns were battle-tested in the ferro-wave gateway and serve as the expected baseline for new Axum work in projects whose harness discloses equivalent architectural constraints. The skill definition itself remains fully portable and harness-agnostic.

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
- **Error Handling**: Use a centralized layered error strategy (returning the application-level error type from handlers).

## Recommended Patterns

- Keep handlers thin: extract data → call service layer → convert to response.
- Business logic belongs in services/repositories (pure calculations where possible).
- Use `axum::response::IntoResponse` for custom error responses.
- Prefer structured JSON errors over plain text.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before emitting any Axum-specific guidance or recommendations.
- The agent explicitly states that `code-writer` + `rust-code-writer` must be applied first before any Axum-specific rules or patterns are given.
- The agent delivers exactly the portable Core Axum Backend Rules and Recommended Patterns (thin handlers, layered extractors, `State<AppState>`, `spawn_blocking`, `AppError` + `IntoResponse`, tower middleware) using the original high-value wording with zero additions, omissions, or unrelated refactoring suggestions.
- Any reference to ferro-wave, event-gateway, or the six specific production patterns appears *only* inside the Harness Context block and is always wrapped in qualified disclosure language ("battle-tested production patterns from the ferro-wave event gateway", "When the invoking harness discloses a project using a similar multi-crate Axum architecture", "high-signal patterns (refined in that codebase) are recommended realizations", "projects whose harness discloses equivalent architectural constraints").
- The agent never promotes ferro-wave patterns as universal "expected baseline" or "must" mandates in the Core Rules, Recommended Patterns, or any other section outside the Harness Context.
- The agent closes by directing the reader to the combined activation statement and any post-task harness rituals (tests, clippy, reviewer gates, tracking updates) disclosed at activation.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dedicated Axum backend specialization of the harness layer (precondition: `code-writer` + `rust-code-writer` active). It supplies the practical voice and patterns for thin handlers, layered extractors and `State<AppState>`, centralized error handling via `AppError` + `IntoResponse`, tower middleware composition, CPU isolation with `spawn_blocking`, and the strict separation of portable Axum rules from harness-disclosed project realizations (including qualified ferro-wave examples), while preserving every principle of the base skills (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Apply Axum backend patterns on top of `code-writer` + `rust-code-writer` by keeping handlers thin, using layered extractors and `State<AppState>`, centralizing errors with `AppError` + `IntoResponse`, composing tower middleware, and offloading CPU work to `spawn_blocking` — treating all ferro-wave-derived production patterns as qualified, harness-disclosed examples only.”

---

This skill is the canonical authority on clean, stratified Axum HTTP backend development for all work following agentskills.io harness patterns.

All Axum route, handler, middleware, `AppState`, or backend API work **MUST** route through this skill (combined with the prerequisites) to guarantee portable, high-signal patterns without harness coupling.

**When using this skill**: Always combine it with the core `code-writer` + `rust-code-writer`. Reference any project-specific realizations (e.g. exact `AppError` shape, crate boundaries, or mandatory patterns) only as disclosed by the invoking harness at activation. Apply the thin-handler + stratified-error discipline mercilessly.

**Activation Statement**  
> Using `code-writer` + `rust-code-writer` + `rust-axum-backend` for this Axum backend task.

Apply this skill **mercilessly** on every Axum backend, HTTP API, or server task.
