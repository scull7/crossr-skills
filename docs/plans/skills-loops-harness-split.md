# Split CrossR into four sycamore-hq remotes

**Status:** paused after split-04. Resume at **split-05: copy landing**.
**Human artifact:** [skills-loops-harness-split.html](skills-loops-harness-split.html)
**Charter PR:** [sycamore-hq/crossr-skills#95](https://github.com/sycamore-hq/crossr-skills/pull/95) (merged)

Do not rewrite AVRIL/AXEL/BRICK while moving them. Do not add new orchestration skills to `crossr-skills`.

---

## Resume in a later session

1. Work from `sycamore-hq/crossr-skills` `main` (not `feat/ocaml-gan-trio`).
2. Read this file + the HTML. Tracking: `features.json` phase `split-skills-loops-harness`.
3. Next unit of work is **split-05** only. One stacked PR, <10 min review.
4. Copy into `sycamore-hq/crossr-web-landing` (Zola `site/`, mdBook `book/` rewritten as **links**). No SKILL.md. No spec of record. Leave copies in skills until dual-publish.

Trigger: “continue the skills/loops/harness split from split-05”.

---

## Locked decisions

- Org: **sycamore-hq**. `scull7/crossr-skills` already transferred.
- Remotes:
  - `sycamore-hq/crossr-skills` — portable catalog
  - `sycamore-hq/crossr-loops` — AVRIL / AXEL / BRICK / rust-team-lead
  - `sycamore-hq/crossr-harness` — spec, bootstrap, dashboard
  - `sycamore-hq/crossr-web-landing` — public front door
- Deps (acyclic): `harness → loops → skills`. Landing links; owns no law.
- New remotes: **clean copy** + `MIGRATION.md` with source SHAs. Skills keeps full history.
- Consumers: **dual-publish one tagged monolith**, deprecation pointers, then cut.
- BRICK **stages stay in skills**. Conductor `brick` moves.
- `agent-harness` **stays**. `HARNESS-SPEC.md` **moves**.
- `dashboard-prompt` + `chief-of-staff` **move to harness**.
- Graph DSL: **defer**. Conductors stay SKILL.md until dogfood is green.
- Public remotes. No custom domain for landing yet.

---

## Why

One repo sold a catalog and a process runtime. Catalog must load in Claude/Cursor/Grok without buying CrossR process. Process must compose catalog skills as nodes without owning their text.

After the split, HARNESS-SPEC §12–13 defining AVRIL/AXEL is a spec bug. Loop law → loops. Artifact/ritual law → harness. Skill law → SKILL.md.

---

## Done

| ID | What | Evidence |
|----|------|----------|
| split-00 | Transfer `scull7/crossr-skills` → `sycamore-hq/crossr-skills` | git 301s old URL. Pages live at https://sycamore-hq.github.io/crossr-skills/ . `scull7.github.io/crossr-skills/` is 404. |
| split-01 | Charter freeze + classification | #95 merged. README freeze. HTML plan. |
| split-02 | Empty remotes | [loops](https://github.com/sycamore-hq/crossr-loops), [harness](https://github.com/sycamore-hq/crossr-harness), [landing](https://github.com/sycamore-hq/crossr-web-landing) — MIT + not-ready README. |
| split-03 | Copy loops | Clean copy of conductors + loop personas + `/avril` `/axel` bodies + pipeline chapters into [crossr-loops](https://github.com/sycamore-hq/crossr-loops). Source SHA `2c0b00976928c275e07c7ebc43b4b0e0f400b2ba`. Skills keeps copies. |
| split-04 | Copy harness | Clean copy into [crossr-harness](https://github.com/sycamore-hq/crossr-harness). `HARNESS-SPEC.md` §12–13 stripped. Source SHA `5f4e3c7d97dae62de437821b78e149ac0d8be3fa`. Skills keeps copies. |

Local note: original checkout may still be on `feat/ocaml-gan-trio`. Split work used worktree `/Users/nathansculli/src/crossr-skills-split-charter`.

---

## Remaining stacked PRs

### split-03 — copy loops (DONE)

Clean copy into `crossr-loops`. Skills **keeps** the files until split-07. Catalog later gets `moved-to` on dual-publish, not in this PR.

**Skills (directories):**

- `.agents/skills/avril/`
- `.agents/skills/axel/`
- `.agents/skills/brick/` (conductor only — not `brick-specifier|coder|refactorer|mutator`)
- `.agents/skills/rust-team-lead/`
- `.agents/skills/orchestrator-prompt/`

**Personas:**

- `.agents/agents/planning-architect-agent.md`
- `.agents/agents/product-owner-agent.md`
- `.agents/agents/qa-architect-agent.md`
- `.agents/agents/visionary-cto-agent.md`
- `.agents/agents/axel-conductor-agent.md`
- `.agents/agents/rust-reviewer-agent.md`
- `.agents/agents/rust-tester-agent.md`
- `.agents/agents/rust-architect-agent.md`
- `.agents/agents/brick-specifier-agent.md`
- `.agents/agents/brick-coder-agent.md`
- `.agents/agents/brick-refactorer-agent.md`
- `.agents/agents/brick-mutator-agent.md`

**OpenCode prompt bodies** (loops owns content; harness bootstrap will install):

- `templates/harness/opencode/agent/avril.md`
- `templates/harness/opencode/agent/axel.md`
- `templates/harness/opencode/command/avril.md`
- `templates/harness/opencode/command/axel.md`

**Pipeline law:** `book/src/pipeline/{overview,avril,axel,brick}.md`

Also: `MIGRATION.md` naming the skills SHA copied from. Loops README replaces not-ready charter.

Stay in skills: `skill-evaluator-agent`, `skill-remediator-agent`, `skill-reviewer-agent`.

### split-04 — copy harness (DONE)

Clean copy into `crossr-harness`.

- `HARNESS-SPEC.md` — **strip §12–13 loop law** on copy. Replace with: loops supplied by `crossr-loops`; harness discloses board, tracking, ritual, dashboard command.
- `scripts/harness-bootstrap`
- `scripts/status-dashboard`
- `scripts/sync-skills` (later grows lockfile: `skills = <tag>`, `loops = <tag>`)
- `scripts/verify-docs`, `scripts/verify-opencode`
- `templates/harness/` minus loop prompt bodies (those come from loops at bootstrap)
- OpenCode `/status` (`templates/harness/opencode/agent/status.md`, `command/status.md`, `opencode.jsonc` skeleton)
- `.agents/skills/dashboard-prompt/`
- `.agents/skills/chief-of-staff/`
- `features.schema.json`
- `test/harness-bootstrap-smoke.sh`
- `just` recipes for `status` / `status-html` (as docs, not this repo’s justfile forever)

Lockfile shape (do not invent a third tracker):

```
skills = <tag>
loops  = <tag>
```

Bootstrap copies: skills → `.agents/skills/`; loop conductors+personas → skills + `.agents/agents/`; harness templates → project files. Never overwrite existing `.opencode/`. No git submodules.

### split-05 — copy landing (NEXT)

Clean copy into `crossr-web-landing`: Zola `site/`, mdBook `book/` rewritten as **links** (catalog → skills, pipeline → loops, bootstrap → harness). No SKILL.md. No spec of record.

Product READMEs link to the landing remote.

### split-06 — dual-publish tag

Tag skills `vN-last-monolith` (still contains everything). Old `sync-skills` / `harness-bootstrap` print “use sycamore-hq/crossr-harness”. Catalog marks moved items with `moved-to`.

### split-07 — delete from skills

Remove moved artifacts from the catalog repo. Catalog-only README. Shim or remove old scripts.

### split-08 — dogfood

Bootstrap all three product repos from harness. First loops/harness commits may stay manual until tags exist; after tags, all three consume published harness.

### split-09 — graphs (not this chain)

Explicit graph format in `crossr-loops` after dogfood is green. YAML/JSON nodes+edges later. Not Rhai/OpenCode-native on day one.

---

## Stay in crossr-skills (do not copy away)

`code-writer`; rust/ocaml writer+reviewer+tester+architect; `rust-errors`, `rust-axum-backend`, `rust-frontend`, `rust-tui`; `voice-dna`, `unslop`, `diataxis`, `obsidian-cli`; `skill-evaluator` + skill GAN agents; `agent-harness`; `brick-specifier`, `brick-coder`, `brick-refactorer`, `brick-mutator`; `docs/public-skills.json`; `scripts/sync-claude-skills`.

---

## Risks

- Three catalogs + a site. One lockfile. Loops CI against the pinned skills tag. Landing owns no law.
- Spec drift if HARNESS-SPEC still defines AVRIL on copy day. Strip on split-04.
- Pages: new URL works; old user Pages does not redirect.
- Chicken-egg dogfood until first tags.

## Unresolved

- Custom domain for `crossr-web-landing`? None yet.
- Dual-publish tag name (`vN-last-monolith` is a placeholder).
