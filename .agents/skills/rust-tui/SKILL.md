---
name: rust-tui
description: |
  Specialized skill for building production-grade terminal UIs in Rust using ratatui.
  Extends `rust-code-writer` with ratatui-specific patterns for the unidirectional Component + Action + centralized dispatch architecture, pure `handle_key` translator (no mutation), two-phase update contract, offloading long-running work via mpsc, pure calculation layers, and exhaustive TestBackend + dispatch testing.
  Harness-layer domain skill with clean stratified disclosure. Fully portable across agentskills.io environments and models when paired with a compatible harness. Always activate together with `code-writer` + `rust-code-writer`.
---

# Rust TUI Skill (ratatui + Unidirectional Architecture)

**This skill extends `rust-code-writer`.**  
You **MUST** apply `code-writer` + `rust-code-writer` first, then layer on these TUI-specific rules.

## Harness Context (Stratified Disclosure)

This is a harness-layer domain skill for ratatui TUI development in Rust.

The core content below is written in portable language: the rules for the unidirectional Component + Action + centralized dispatch architecture, pure `handle_key` as a translator from key events to Actions (no mutation), the two-phase update contract (`handle_key` then `update`), `render` receiving read-only state plus focused flag, offloading all long-running work, maintaining a pure calculation layer, and exhaustive testing via `TestBackend` and dispatch unit tests are universal ratatui idioms that apply in any agentskills.io Rust project using ratatui for terminal UIs.

The concrete `Component` trait definition and references to the architecture refined across multiple phases of ferro-wg are isolated here under qualified disclosure only. When the invoking harness discloses a project using a similar ratatui unidirectional architecture, the following high-signal patterns (refined in that codebase) are recommended realizations:

```rust
pub trait Component {
    fn handle_key(&mut self, key: KeyEvent, state: &AppState) -> Option<Action>;
    fn update(&mut self, action: &Action, state: &AppState);
    fn render(&mut self, frame: &mut Frame, area: Rect, focused: bool, state: &AppState);
}
```

This architecture has shipped multiple complex, reliable TUIs with zero production panics and exceptional reviewability. These patterns were battle-tested in ferro-wg and serve as the expected baseline for new ratatui TUI work in projects whose harness discloses equivalent architectural constraints. The skill definition itself remains fully portable and harness-agnostic.

## Core TUI Architecture (Portable)

All serious ratatui applications follow the unidirectional architecture:

### Component + Action + Centralized Dispatch

- `handle_key` is a **pure translator** (key + read-only `&AppState` → `Option<Action>`). No mutation.
- `update` is the **broadcast notification** phase. Components may only mutate their own local widget state (e.g. `TableState`).
- `render` always receives `&AppState` (read-only) + a `focused` flag.

This is the two-phase update contract. It is the Rust equivalent of Elm/Redux for the terminal.

### Action Enum — The Only Way State Changes

All mutations flow through a single exhaustive `Action` enum.

`AppState` contains a single `dispatch(&mut self, action: &Action)` method that is the **sole source of truth** for state changes.

Components never mutate `AppState` directly.

### Offload Everything

Long-running work (daemon IPC, file I/O, benchmarks, network) is always spawned as a background task. Results come back as `Action`s via an `mpsc` channel.

The main event loop stays responsive and pure.

### Pure Calculation Layer

Formatting, data shaping, filtering, health calculations, etc. live in pure modules (e.g. `benchmark.rs`, `ux.rs`) that take immutable data and return values. No side effects.

### Testing Idioms

- Exhaustive unit tests on `AppState::dispatch` for every `Action` variant and edge case.
- `TestBackend` snapshot tests for every component at 80×24 (and other key sizes).
- Component tests for `handle_key` → `Action` and `update` side-effects on local state.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before emitting any TUI-specific guidance or recommendations.
- The agent explicitly states that `code-writer` + `rust-code-writer` must be applied first before any ratatui, Component, Action, AppState, or TUI-specific rules or patterns are given.
- The agent delivers exactly the portable Core TUI Architecture (Component + Action + centralized dispatch, pure handle_key translator, offload everything, pure calculation layer, Testing Idioms) using the original high-value wording with zero additions, omissions, or unrelated refactoring suggestions.
- Any reference to ferro-wg or the concrete `Component` trait definition appears *only* inside the Harness Context block and is always wrapped in qualified disclosure language ("battle-tested in ferro-wg", "When the invoking harness discloses a project using a similar ratatui unidirectional architecture", "high-signal patterns (refined in that codebase) are recommended realizations", "projects whose harness discloses equivalent architectural constraints").
- The agent never promotes ferro-wg patterns or the concrete trait as universal "must" mandates or "the architecture" in the Core TUI Architecture, or any other section outside the Harness Context.
- The agent closes by directing the reader to the combined activation statement and any post-task harness rituals (tests, clippy, reviewer gates, tracking updates) disclosed at activation.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dedicated ratatui TUI specialization of the harness layer (precondition: `code-writer` + `rust-code-writer` active). It supplies the practical voice and patterns for the unidirectional Component + Action + centralized dispatch architecture, pure `handle_key` translator (no mutation), two-phase update contract, offloading long-running work via mpsc, pure calculation layers, and exhaustive TestBackend + dispatch testing, while preserving every principle of the base skills (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Apply ratatui TUI patterns on top of `code-writer` + `rust-code-writer` by building as a pure unidirectional data flow: Components emit Actions via a pure `handle_key` translator, a single `AppState::dispatch` owns all mutation, side effects are offloaded, calculations stay pure, and every component is exhaustively testable with `TestBackend` — treating all ferro-wg-derived concrete trait shapes and architecture details as qualified, harness-disclosed examples only.”

---

This skill is the canonical authority on clean, stratified ratatui TUI development for all work following agentskills.io harness patterns.

All ratatui component, Action, AppState, event loop, or terminal UI architecture work **MUST** route through this skill (combined with the prerequisites) to guarantee portable, high-signal patterns without harness coupling.

**When using this skill**: Always combine it with the core `code-writer` + `rust-code-writer`. Reference any project-specific realizations (e.g. exact `Component` trait signature, dispatch implementation, or ferro-wg patterns) only as disclosed by the invoking harness at activation. Apply the unidirectional pure-translator + exhaustive-test discipline mercilessly.

**Activation Statement**  
> Using `code-writer` + `rust-code-writer` + `rust-tui` for this terminal UI task.

Apply this skill **mercilessly** on every ratatui TUI, Component, Action, or terminal UI task.
