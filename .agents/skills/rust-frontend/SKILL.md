---
name: rust-frontend
description: |
  Specialized skill for building Rust-based web frontends using WASM, Leptos, and data processing with Polars.
  Extends `rust-code-writer` with frontend-specific rules for UI, performance, theming, and data pipelines.
  Use this skill whenever working on WASM, Leptos components, or Polars data processing.
---

# Rust Frontend Skill (WASM / Leptos / Polars)

**This skill extends `rust-code-writer`.**  
You **MUST** apply `code-writer` + `rust-code-writer` first, then apply these frontend-specific rules.

## Core Mandates

- All **deep computation** must happen in Rust (either in the WASM binary or Leptos server functions). **Never** offload computation to JavaScript.
- Prioritize performance, simplicity, and excellent human interface design.

## WASM / Leptos Rules

- **UI Styling**:
  - Use **Pico CSS** as the base.
  - **Never** use jQuery, React, Vue, Svelte, or any other JS component framework.
  - **Never** use Pico CSS defaults as-is.
  - Always create a separate custom CSS/SCSS file that complements the app’s semantics and branding.
- **Theming**:
  - Support adaptive light/dark themes by default.
  - Include a user-controlled theme toggle.
- **Typography**:
  - Use modern, unique typography.
  - Always include custom fonts (Google Fonts allowed) for headings and body text.
- **Build Process**:
  - **Always** rebuild the WASM binary when any Rust code it depends on changes using this command:
    
    `wasm-pack build --target web --out-dir web/pkg`

## Data Processing (Polars) Rules

- **Always** use the `polars` crate for any tabular data manipulation. Never use other dataframe libraries.
- When working with dataframes:
  - Never print the row count or schema alongside the dataframe (it is redundant).
  - Never ingest or display more than 10 rows at a time when analyzing data — work with subsets to avoid context overload.

## When to Activate This Skill

Use `rust-frontend` when the task involves:
- Building or modifying Leptos components
- Creating WASM modules
- Implementing frontend UI or styling
- Working with data processing pipelines using Polars

**Activation Statement** (use at the start of relevant responses):

> Using `code-writer` + `rust-code-writer` + `rust-frontend` for this frontend task.

---

**Always maintain functional purity, stratified design, and flat code** from `rust-code-writer` even when building frontend components and data pipelines.
