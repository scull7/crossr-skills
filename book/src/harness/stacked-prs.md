# PETC Loop & Stacked PR Discipline

## The PETC Loop

Every session follows the same rhythm:

1. **Plan** — Read `progress.md` + `features.json` + recent git history. Propose the next small task. End the plan with a bulleted list of unresolved questions.
2. **Execute** — Implement using the appropriate skills and strict adherence to project conventions.
3. **Test** — Run the full matrix (`just check`, `just test`, `just clippy`, `just fmt`). Run `rust-code-reviewer`, `rust-code-tester`, and `rust-architect` (or the full GAN team) on the changes.
4. **Commit** — Small, focused diff + update `features.json` + append to `progress.md` + clean git state.

## Stacked PR Discipline

Large features are never delivered in one giant PR.

Instead, they are decomposed into a chain of small, stacked PRs (typically 8–16 for major efforts).

Each PR in the stack must answer:

- **What this PR contains**
- **What the next PR will contain**
- **How this was verified**
- **Risk level and why review is easy**

### Historical Example

The 16-PR `CD-1873` authz chain in ferro-wave is the canonical real-world demonstration of this pattern at scale. A high-risk security subproject was delivered as a series of tiny, extremely reviewable changes with full traceability and multi-tier verification harnesses.

## Why This Matters

- A human reviewer (or agent) can give deep, high-quality feedback in < 10 minutes.
- Progress is visible and motivating.
- Rollback or partial delivery is safe.
- The final merged result is still a clean, coherent feature.

This discipline is non-negotiable for work tracked in this harness.