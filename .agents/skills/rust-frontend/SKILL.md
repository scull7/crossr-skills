---
name: rust-frontend
description: |
  Specialized skill for building Rust-based web frontends using WASM, Leptos, and data processing with Polars.
  Extends `rust-code-writer` with frontend-specific rules for UI, performance, theming, data pipelines, and anti-slop creative design.
  Harness-layer domain skill with clean stratified disclosure. Fully portable across agentskills.io environments and models when paired with a compatible harness. Always activate together with `code-writer` + `rust-code-writer`.
---

# Rust Frontend Skill (WASM / Leptos / Polars)

**This skill extends `rust-code-writer`.**  
You **MUST** apply `code-writer` + `rust-code-writer` first, then layer on these frontend-specific rules.

## Harness Context (Stratified Disclosure)

This is a harness-layer domain skill for Rust WASM frontend development using Leptos and Polars.

The core content below is written in portable language: the rules for keeping all deep computation in Rust (WASM binary or Leptos server functions), using Pico CSS as base with mandatory separate custom complementary CSS/SCSS, supporting adaptive light/dark themes with user toggle, employing modern unique typography and custom fonts, restricting tabular work to the `polars` crate with small-subset discipline, always rebuilding the WASM binary on Rust changes, and the strong anti-"AI slop" mandate for creative, distinctive, hand-crafted interfaces are universal practices that apply in any agentskills.io Rust project using this frontend stack.

These patterns were battle-tested in prior CrossR frontend efforts and serve as the expected baseline for new frontend work in projects whose harness discloses equivalent stack and design constraints. The skill definition itself remains fully portable and harness-agnostic.

When the invoking harness discloses a project using a similar Leptos + WASM + Polars architecture and aesthetic constraints, the following high-signal patterns (refined in that codebase) are recommended realizations:

- **WASM build ritual**: The command `wasm-pack build --target web --out-dir web/pkg` (or the precise equivalent for the project's directory layout and target, as disclosed by the harness).
- **Polars analysis limit**: Never ingest or display more than 10 rows at a time when analyzing or presenting dataframe data — always work with tiny subsets to prevent context overload in agent sessions.
- **Aesthetic character descriptors**: Strict emphasis on hand-crafted character through typography, motion, and atmosphere (as the distinctive signature of CrossR frontend work).

## Core Frontend Mandates

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
  - **Always** rebuild the WASM binary when any Rust code it depends on changes using the command and output directory disclosed by the invoking harness at activation.

## Data Processing (Polars) Rules

- **Always** use the `polars` crate for any tabular data manipulation. Never use other dataframe libraries.
- When working with dataframes:
  - Never print the row count or schema alongside the dataframe (it is redundant).
  - Never ingest or display more than the limit disclosed by the invoking harness at activation when analyzing data — work with subsets to avoid context overload.

## Anti "AI Slop" Guidance

You have a strong tendency to converge on generic, safe, "on-distribution" outputs. This produces what users call "AI slop".

For frontend work:

- Be **creative and distinctive**. Make interfaces that feel deliberately designed for the specific context rather than generic modern web defaults.
- Avoid overused fonts (Inter, Roboto, system sans), clichéd color schemes, and cookie-cutter component patterns.
- Prioritize typography, motion, and atmosphere that give the product character.
- The goal is interfaces that feel hand-crafted and surprising in a good way, not "AI-generated".

Keep the guidance general and principle-based. Do not hard-code specific aesthetic references (e.g. particular OS themes or retro styles) unless the project itself has already chosen them.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before emitting any frontend-specific guidance or recommendations.
- The agent explicitly states that `code-writer` + `rust-code-writer` must be applied first before any WASM, Leptos, Polars, UI, or styling-specific rules or patterns are given.
- The agent delivers exactly the portable Core Frontend Mandates, WASM / Leptos Rules, Data Processing (Polars) Rules, and Anti "AI Slop" Guidance using the original high-value wording with zero additions, omissions, or unrelated refactoring suggestions.
- Any reference to the specific `wasm-pack build --target web --out-dir web/pkg` command string, the "10 rows" Polars limit, or unique non-portable aesthetic character descriptors from the Harness Context appears *only* inside the Harness Context block and is always wrapped in qualified disclosure language ("when the invoking harness discloses a project using a similar ...", "recommended realizations", "battle-tested ... patterns ... serve as the expected baseline for ... projects whose harness discloses equivalent ... constraints").
- The agent never promotes the specific build command, row count limit, or unique aesthetic character descriptors as universal "must" or "always" mandates in the Core Frontend Mandates, WASM / Leptos Rules, Data Processing (Polars) Rules, Anti "AI Slop" Guidance, or any other section outside the Harness Context.
- The agent closes by directing the reader to the combined activation statement and any post-task harness rituals (tests, clippy, reviewer gates, tracking updates) disclosed at activation.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dedicated WASM / Leptos / Polars frontend specialization of the harness layer (precondition: `code-writer` + `rust-code-writer` active). It supplies the practical voice and patterns for deep-computation-in-Rust-only, Pico CSS base + mandatory custom complementary CSS/SCSS, adaptive theming with toggle, distinctive typography with custom fonts, Polars-only tabular with small-subset discipline, WASM rebuild ritual, and the anti-slop creative mandate for hand-crafted interfaces, while preserving every principle of the base skills (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Apply Rust frontend patterns on top of `code-writer` + `rust-code-writer` by keeping all deep computation in Rust (WASM or Leptos server functions), enforcing Pico CSS as base with mandatory custom complementary CSS/SCSS, adaptive light/dark theming with user toggle, distinctive modern typography with custom fonts, Polars-only tabular work with small-subset discipline, always rebuilding WASM on Rust changes, and the anti-slop mandate for creative hand-crafted interfaces — treating all specific command strings, row limits, and aesthetic precedents as qualified, harness-disclosed examples only.”

---

This skill is the canonical authority on clean, stratified Rust WASM / Leptos / Polars frontend development for all work following agentskills.io harness patterns.

All Leptos component, WASM module, frontend UI or styling, or Polars data-pipeline work **MUST** route through this skill (combined with the prerequisites) to guarantee portable, high-signal patterns without harness coupling.

**When using this skill**: Always combine it with the core `code-writer` + `rust-code-writer`. Reference any project-specific realizations (e.g. exact wasm-pack command and flags, Polars row limit, or branding-specific fonts and CSS conventions) only as disclosed by the invoking harness at activation. Apply the deep-Rust computation + anti-slop creative discipline mercilessly.

**Activation Statement**  
> Using `code-writer` + `rust-code-writer` + `rust-frontend` for this frontend task.

Apply this skill **mercilessly** on every Leptos, WASM, Polars, or Rust frontend UI task.
