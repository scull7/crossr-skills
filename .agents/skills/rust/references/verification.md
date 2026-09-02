# Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the rust book's One-Sentence Mandate before generating or planning any Rust code.
- The agent loads the topic reference that matches the situation, not the whole book, and does not feed How to an adversary.
- The agent defines or extends dedicated thiserror enums per layer, supplies `From` impls, and never uses inline `.map_err` at call sites or `.unwrap()` on production `Result`s.
- The agent replaces primitives, sentinels, and boolean flags with newtypes, `Option<T>`, and exhaustive match, and parses wire values at the edge.
- The agent enforces the tooling checklist (fmt, pedantic clippy `-D warnings`, build, tests, no `dbg!` / `println!`) before calling the change complete.
- The agent identifies `#[allow(clippy::too_many_*)]`, unnecessary ownership transfers, undocumented `unsafe`, and wildcard imports outside tests, and refactors them.

Violations against any of these six during fresh activation mean the book was not followed.
