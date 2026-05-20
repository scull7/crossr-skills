---
name: rust-tui
description: |
  Specialized skill for building production-grade terminal UIs in Rust using ratatui.
  Codifies the unidirectional, highly testable Component + Action + centralized dispatch
  architecture proven in large-scale TUI projects. Use this whenever building or
  refactoring ratatui-based applications.
---

# Rust TUI Skill (ratatui + Unidirectional Architecture)

**This skill extends `code-writer` + `rust-code-writer`.**  
You **MUST** combine them before applying these TUI-specific rules.

## Core Architecture (Non-Negotiable)

All serious ratatui applications in this ecosystem follow the architecture refined across multiple phases of ferro-wg:

### The Component Trait

```rust
pub trait Component {
    fn handle_key(&mut self, key: KeyEvent, state: &AppState) -> Option<Action>;
    fn update(&mut self, action: &Action, state: &AppState);
    fn render(&mut self, frame: &mut Frame, area: Rect, focused: bool, state: &AppState);
}
```

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

## When to Activate This Skill

Use `rust-tui` when the task involves:
- Building or refactoring a ratatui TUI
- Adding new tabs, modals, or components
- Working with `AppState`, `Action`, or the event loop
- Improving test coverage or architecture of an existing TUI

**Activation Statement**:
> Using `code-writer` + `rust-code-writer` + `rust-tui` for this terminal UI task.

## One-Sentence Mandate

> Build terminal UIs as a pure unidirectional data flow: Components emit Actions, a single `AppState::dispatch` owns all mutation, side effects are offloaded, and every component is exhaustively testable with `TestBackend`.

This architecture has shipped multiple complex, reliable TUIs with zero production panics and exceptional reviewability. Follow it.