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
   Claude compatibility (`.claude/skills/` and `.claude/commands/`) is **optional** and produced by a generator script — never hand-maintained duplicates. In this repository that generator is `scripts/sync-claude-skills` (`just claude-skills-sync`); `just harness-validate` reports drift between the canonical skills and the generated copies.

2. **Harness Relationship (Stratified) for Skills**  
   Skills are classified as generic/core (fully harness-agnostic) or harness-layer/domain (with a clean `## Harness Context (Stratified Disclosure)` block that isolates concrete artifact names, commands, and project examples as parameters supplied by the invoking harness). The canonical portable structure (YAML frontmatter, Verification with 6 observable behaviors, Specialization, One-Sentence Mandate, clean footer) is required for all skills. The `skill-evaluator` skill (and its permanent GAN personas) is the authority. This principle was proven and locked in during the 2026 skill-remediation campaign on this repository.

3. **Incremental & Reviewable by Design**  
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

## 4.5 HTML as the Primary Human-Facing Artifact Format

For any artifact whose primary audience is a human — specifications, architecture reviews, PR summaries, reports, dashboards, prototypes, deployment guides, etc. — **generate a self-contained HTML file** as the main deliverable.

**Rationale (The Unreasonable Effectiveness of HTML)**:
- Humans read, understand, and engage with well-designed HTML far more effectively than raw Markdown.
- Modern models produce exceptionally high-quality, single-file HTML (Tailwind via CDN + SVG/light JS) with very little prompting.
- This dramatically improves the quality of human-in-the-loop feedback in the harness.

**Guidelines**:
- Output a single `.html` file (fully self-contained, no local dependencies).
- Use Tailwind CSS via CDN for rapid, clean styling.
- Make the document scannable, visually rich, and interactive where it adds value.
- You may also produce a Markdown version for git or agent handoff, but treat the HTML as the primary human artifact.
- Name files descriptively (e.g., `architecture-review.html`, `pr-42-summary.html`).

This pattern is now a first-class recommendation in the harness.

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

## 11. Agent Definitions (GAN Mechanization)

As of the 2026 GAN mechanization effort, reusable agent personas live in `.agents/agents/`.

The canonical trio for quality enforcement is:
- `rust-reviewer-agent`
- `rust-tester-agent`
- `rust-architect-agent`

Projects are encouraged to run the full GAN sequence (Reviewer → Tester → Architect) on significant changes. See `.agents/agents/README.md` for the recommended invocation pattern.

## 12. AVRIL — Planning GAN (Automated Visionary Review Iteration Loop)

Before execution (PETC / code GAN), significant greenfield or prototype work SHOULD run **AVRIL** — the planning Generator-Adversary Network defined by the `avril` skill.

**Loop (non-negotiable order):**

1. **Generator** — `planning-architect-agent` proposes Product Backlog Items (PBIs).
2. **Adversaries** (each item, every cycle):
   1. `product-owner-agent` — value, scope, user outcomes
   2. `qa-architect-agent` — testability, acceptance criteria, failure modes
   3. `visionary-cto-agent` — strategic fit, two-year trajectory (final gate)
3. Any `REJECT` returns to the Generator for a minimal revise; material edits invalidate prior blessings.
4. An item is complete only when all three adversaries emit explicit `BLESS <id>`.
5. Orchestrator emits a Blessed Backlog Summary and **stops**. Implementation is owned by **AXEL** (§13).

**Board backend (stratified):** Prefer [Pinto](https://github.com/moriturus/pinto) when the project discloses a `.pinto/` board and the `pinto` CLI is available. Otherwise persist the portable PBI shape defined in the `avril` skill. Concrete commands and paths are harness parameters, not hard-wired universals.

**Activation:**

> Using `code-writer` + `avril` to run the Automated Visionary Review Iteration Loop on the current intent until every PBI is triple-blessed.

AVRIL is planning-only. It does not replace the code GAN (Reviewer → Tester → Architect) during implementation.

**Planning size / optional owl-sketch:** Generators MUST split PBIs that cannot be reviewed in under ~10 minutes deep review. An optional bounded “draw the owl” planning spike may explore seams, but its output is not executable authorization — massaged PBIs still require triple `BLESS`. Execution-time oversize diffs are handled by AXEL’s optional **decomposition mode** (§13), not by skipping AVRIL. Contract: `docs/plans/mitchell-decomposition-contract.html` (issue #43).

## 13. AXEL — Execution Loop (Automated eXecution Loop)

After AVRIL (or equivalent human authorization of a finite PBI set), significant implementation SHOULD run **AXEL** — the execution orchestrator defined by the `axel` skill.

**End-to-end pipeline:**

```
Intent → AVRIL (plan GAN) → Blessed Backlog → AXEL (PETC + code GAN) → Done PBIs
```

**Loop (per blessed PBI):**

1. **Intake gate** — Refuse work unless AVRIL-blessed, board-marked blessed, or explicitly human-authorized.
2. **Select** — One ready PBI (dependencies complete; prefer `pinto next` when available).
3. **Plan** — Concise PETC plan; unresolved questions blocking → stop for human.
4. **Board** — `in-progress` while executing.
5. **Decompose** — Smallest semantic phases; state “phase k of n”.
6. **Code GAN** (each phase, fixed order):
   1. Generator (`code-writer` + language/domain; Rust often via `rust-team-lead`)
   2. Reviewer → Tester → Architect — each must emit explicit `BLESS`
   3. On `REJECT`: minimal fix + full re-chain
   4. Commit + update tracking (PBI id in message/artifacts)
7. **AC evidence gate** — Every acceptance criterion needs recorded evidence; harness verification matrix green.
8. **Board** — `review` then `done` only when AC are complete (incomplete AC is a hard stop).
9. Emit PBI Completion Record; advance or stop.

**Board backend:** Same stratified Pinto-preferred rules as AVRIL. AXEL keeps board status honest; it does not invent scope (scope changes return to AVRIL).

**Rust pairing:** On Rust codebases, AXEL owns backlog/board/AC/tracking; `rust-team-lead` is the preferred **inner** code GAN for implementation phases. AXEL still enforces intake, AC evidence, and done criteria.

**Activation:**

> Using `code-writer` + `axel` (+ disclosed language/domain skills; Rust: `rust-code-writer` + `rust-team-lead` as inner GAN) to execute the next blessed PBI through PETC until AC are evidenced and the board is honest.

AXEL conductors never write, edit, or review code themselves. Persona: `axel-conductor-agent`.

**Optional Mitchell decomposition mode (default off):** When the human or harness enables decomposition mode (`decomposition_mode` / “mitchell” / “draw the owl”), AXEL measures each phase diff with `git diff --numstat` (LOC = added + deleted; default threshold **1500**, overridable via `decomposition_loc_threshold`). Over-threshold work **must not commit**; the conductor decomposes and massages tasks, executes reviewable chunks (sequential fallback required if parallel subagents are unavailable), and may run a bounded re-owl only without bypassing intake or code GAN BLESS. When mode is off, AXEL behavior is unchanged. Full contract: `docs/plans/mitchell-decomposition-contract.html` (issue #43). Skill: `axel`.

---

**Whatever you do, work at it with all your heart, as working for the Lord.** — Colossians 3:23

This harness exists so that we can ship excellent, reliable software without burning out our agents or ourselves. Use it with discipline and joy.