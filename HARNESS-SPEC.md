# HARNESS-SPEC.md

**The official specification for long-running, reliable AI agent harnesses in Nathan Sculli / Tensorwave projects.**

Version: 2.0 (Approved)  
Status: Canonical source of truth for all projects

---

## 1. Purpose

A **harness** is the persistent scaffolding that turns stateless AI coding sessions into reliable, multi-session, self-verifying agents that ship production-grade code with clean handovers.

This specification defines the minimum artifacts, rituals, processes, and patterns that every project must adopt so that:

- Work is incremental and reviewable (< 10 minutes deep review per PR)
- State survives context resets
- Large features can be decomposed safely (see the 16-PR authz chain precedent)
- Claude, Grok, Cursor, and other agentskills.io-compatible tools can all participate
- Security-sensitive and complex work follows the same discipline as simple tasks

Crossr-skills (`.agents/skills/`) are the reusable capability layer. This spec is the **process and artifact layer** that makes those capabilities effective over time.

---

## 2. Core Principles

1. **Strict agentskills.io Compliance**  
   All skills live under `.agents/skills/<name>/SKILL.md` and follow the official specification exactly (YAML frontmatter with `name` + `description`, Markdown body, progressive disclosure).  
   Claude compatibility (`.claude/skills/` and `.claude/commands/`) is **optional** and produced by a generator script — never hand-maintained duplicates.

2. **Incremental & Reviewable by Design**  
   Every unit of work must be reviewable in under 10 minutes. Large features are decomposed into stacked, small PRs with explicit traceability.

3. **Multi-Tier Verification Harnesses**  
   "Harness" is not just meta — we literally build verification harnesses at multiple tiers (in-process, parity snapshots, real substrate VM/k8s, etc.).

4. **Traceability & Reviewability**  
   Every significant piece of work carries stable IDs (tw-xxx, ADR-0002, Phase N, CD-1873, etc.) in code comments, tests, PR titles, and progress tracking.

5. **Policy Gates Before Effects**  
   Security and correctness gates (especially mTLS CN-hostname binding, authz checks, etc.) must be enforced *before* any database lookup or side-effecting operation.

6. **Self-Verifying Handovers**  
   No session ends without tests, clippy, reviewer/tester/architect sign-off (GAN), and clean git state + updated artifacts.

---

## 3. Mandatory Artifacts (Every Project)

### 3.1 `AGENTS.md` (or `CLAUDE.md` / `AGENT.md`)

Project-specific rules file. Must contain:

- Reference to the skills in `.agents/skills/` (with activation examples)
- The **Plan Mode** contract:
  - Plans must be extremely concise
  - Every plan ends with a bulleted list of unresolved questions
- Link to this `HARNESS-SPEC.md`

### 3.2 `features.json`

Machine-readable work tracking. Real production shape (proven on ferro-wg and the 16-PR authz chain):

```json
{
  "phase7": {
    "status": "in_progress",
    "commits": [
      {
        "id": "commit3",
        "title": "Help overlay component",
        "status": "completed",
        "features": ["help_overlay_component", "help_overlay_tests", "keybindings_constant"]
      }
    ]
  },
  "review_remediation": { ... }
}
```

**Requirements**:
- Phases or major workstreams as top-level keys
- Each commit has stable `id`, human `title`, `status`, and array of granular `features` (these become the atomic units of traceability)
- A companion JSON Schema (`features.schema.json`) + validation step in the bootstrap/ritual

### 3.3 `progress.md`

Human-readable, commit-narrative log. Structure:

```markdown
# Phase 7: UX Polish — Implementation Progress

## Completed Phases

### Commit 3: Help overlay component (COMPLETED)
- ...
- All tests pass, clippy clean, no warnings

## Verification Status
- Tooling checks: PASSED
- Adversary reviews: PASSED (reviewer + tester + architect)
```

Append after every commit. Never rewrite history.

### 3.4 `justfile` (or `init.sh` + `Makefile`)

Canonical one-command entry points for the exact build/test/clippy matrices that appear in `CLAUDE.md` and CI. Agents always run the justfile targets.

### 3.5 Git Hygiene + Session Ritual

At the start of every session the agent **must** execute (at minimum):

```bash
git status
git log --oneline -10
cat progress.md | tail -n 30
# jq for pending work in the new features.json shape
./init.sh || just init
cargo check && cargo test --quiet
```

### 3.6 `.agents/skills/` (Canonical)

All reusable skills live here in strict `agentskills.io` format. This directory is the single source of truth.

---

## 4. Strongly Recommended Artifacts

- `CLAUDE.md` (root + per-workspace) with exact cargo matrices, platform notes, and "format first" rules
- `docs/phase-*.md` or `docs/IMPLEMENTATION_*.md` for larger bodies of work
- `.github/workflows/ci.yml` that mirrors the exact checks in CLAUDE.md
- `rust-toolchain.toml` + `install.sh`
- `tests/` crates or harnesses at multiple tiers (the authz pattern)
- `deploy-guide/` or equivalent beautiful, self-contained operator documentation (can be a single-file static webapp)

---

## 5. The PETC Loop + Stacked PR Discipline

**P**lan → **E**xecute → **T**est → **C**ommit

- Plan is written first, is concise, and ends with unresolved questions.
- Every commit is a small, reviewable unit.
- Large features (see CD-1873 authz) are decomposed into 10–16 stacked PRs, each with explicit "this / next / verification".
- Traceability IDs appear in code, tests, PR titles, and features.json.

---

## 6. Verification Gates (Non-Negotiable)

Before a commit is considered done:

1. Self-critique + full test matrix + clippy (pedantic) + fmt
2. `rust-code-reviewer` ruthless pass
3. `rust-code-tester` coverage + exhaustive error path pass
4. `rust-architect` (or `rust-team-lead` GAN) architectural sign-off

Only after all four layers pass is the commit + artifacts updated.

---

## 7. Claude & Other Tool Compatibility

- The canonical skills are always in `.agents/skills/`.
- A `generate-claude-compat` (or equivalent) step in the bootstrap/harness script can derive:
  - `.claude/skills/<name>/SKILL.md` (full copy or symlink)
  - `.claude/commands/rust-*.md` (distilled, slash-command friendly versions)
- Projects may commit the generated files or gitignore them. The generator is the source of truth for keeping them in sync.

---

## 8. Bootstrap & Adoption

Every new project runs (or the human runs):

```bash
harness-bootstrap .          # or the equivalent script
```

This produces a minimal but complete starting harness (AGENTS.md, features.json with phase 0 + schema reference, justfile, progress.md stub, .agents/skills/ guidance, and the Claude generator).

After the first commit of the empty harness, all future work is tracked inside it.

---

## 9. Special Patterns Proven at Scale (Authz Chain)

- **Stacked small PRs** for high-risk security work
- **Literal "verification harnesses"** at multiple fidelity levels
- **Policy gate before any effect** (mTLS CN-hostname check before Mongo lookup)
- **Distinct error semantics** for policy denials vs operational failures
- **Reviewability comments** and ticket linkage in almost every changed file
- **Decoupled documentation PR** so docs never block code

These patterns are now part of the expected discipline for any comparably large or sensitive feature.

---

## 10. Versioning & Evolution

This spec lives at the root of crossr-skills as `HARNESS-SPEC.md`.  
Changes are proposed via the same harness process the spec itself defines (features.json entries, small reviewable PRs, full verification gates).

---

**Whatever you do, work at it with all your heart, as working for the Lord.** — Colossians 3:23

This harness exists so that we can ship excellent, reliable software without burning out our agents or ourselves. Use it with discipline and joy.