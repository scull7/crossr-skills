# Split CrossR into four sycamore-hq remotes

**Status:** complete after split-08. Graphs (split-09) are a **separate chain**.
**Human artifact:** [skills-loops-harness-split.html](skills-loops-harness-split.html)
**Charter PR:** [sycamore-hq/crossr-skills#95](https://github.com/sycamore-hq/crossr-skills/pull/95) (merged)
**Pins:** `skills = "v0-last-monolith"`, `loops = "v0"`, harness `v0`

Do not rewrite AVRIL/AXEL/BRICK. Do not add new orchestration skills to `crossr-skills`.

---

## Resume in a later session

1. Work from `sycamore-hq/crossr-skills` `main` (not `feat/ocaml-gan-trio`).
2. Read this file + the HTML. Tracking: `features.json` phase `split-skills-loops-harness` (completed).
3. Split-00..08 done. Next unit is **split-09 (graphs)** — not this chain.
4. Landing Pages is still off. Do not invent a custom domain.

Trigger: “continue the skills/loops/harness split from split-09”.

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
- Consumers: dual-publish one tagged monolith, deprecation pointers, cut, then dogfood.
- BRICK **stages stay in skills**. Conductor `brick` moves.
- `agent-harness` **stays**. `HARNESS-SPEC.md` **moves**.
- `dashboard-prompt` + `chief-of-staff` **move to harness**.
- Graph DSL: **defer**. Conductors stay SKILL.md until dogfood is green.
- Public remotes. No custom domain for landing yet.
- Lockfile: `skills = <tag>`, `loops = <tag>`. Not a third tracker. No git submodules.

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
| split-03 | Copy loops | Clean copy into [crossr-loops](https://github.com/sycamore-hq/crossr-loops). Source SHA `2c0b009`. Tag [`v0`](https://github.com/sycamore-hq/crossr-loops/releases/tag/v0). |
| split-04 | Copy harness | Clean copy into [crossr-harness](https://github.com/sycamore-hq/crossr-harness). `HARNESS-SPEC.md` §12–13 stripped. Source SHA `5f4e3c7`. |
| split-05 | Copy landing | Clean copy of Zola `site/` + mdBook rewritten as links. Source SHA `9ff577e`. |
| split-06 | Dual-publish tag | Skills tag `v0-last-monolith`. Catalog `moved-to` on seven items. Old scripts printed deprecation and still ran. |
| split-07 | Delete from skills | Catalog-only README. N=18. Shims exit 1. Copies gone. Pages workflow removed. |
| split-08 | Dogfood | Bootstrap from harness. Pins `skills = "v0-last-monolith"`, `loops = "v0"`. Harness tagged `v0`. `--process-only` on all three products. Smoke green. |

Local note: original checkout may still be on `feat/ocaml-gan-trio`. Split work used worktree `/Users/nathansculli/src/crossr-skills-split-charter`.

---

## Remaining

### split-09 — graphs (not this chain)

Explicit graph format in `crossr-loops` after dogfood is green. YAML/JSON nodes+edges later. Not Rhai/OpenCode-native on day one.

---

## Stay in crossr-skills (do not copy away)

`code-writer`; rust/ocaml writer+reviewer+tester+architect; `rust-errors`, `rust-axum-backend`, `rust-frontend`, `rust-tui`; `voice-dna`, `unslop`, `diataxis`, `obsidian-cli`; `skill-evaluator` + skill GAN agents; `agent-harness`; `brick-specifier`, `brick-coder`, `brick-refactorer`, `brick-mutator`; `docs/public-skills.json`; `scripts/sync-claude-skills`.

---

## Risks

- Three catalogs + a site. One lockfile. Loops CI against the pinned skills tag. Landing owns no law.
- Pages: last skills deploy is frozen; landing Pages is not enabled. Old user Pages does not redirect.
- Chicken-egg dogfood: resolved. Pins exist; `--process-only` on products; full bootstrap on a fresh dir copies catalog + loops + harness files.

## Unresolved

- Custom domain for `crossr-web-landing`? None yet.
- Landing Pages still off.
