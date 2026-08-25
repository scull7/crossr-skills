# Bootstrapping a New Project

The fastest way to adopt the full harness in a new project is the `harness-bootstrap` script.

## One command

```bash
git clone https://github.com/scull7/crossr-skills.git
./crossr-skills/scripts/harness-bootstrap /path/to/your-new-project
```

## What gets created

- `AGENTS.md` (Plan Mode and skill references)
- `features.json` + `features.schema.json`
- `progress.md`
- `justfile` with standard targets
- `.agents/skills/` (skills you choose)
- `harness-validate` (includes `docs-verify`)

Commit the empty harness immediately, then work inside it.

## After bootstrapping

```bash
just harness-validate
just init
```

Then run the flagship pipeline: **AVRIL** (plan) → **AXEL** (execute). See [Pipeline Overview](../pipeline/overview.md).

## First session (AVRIL → AXEL)

Paste these after bootstrap (adjust intent). Prefer a Pinto board (`pinto init`) when available.

### 1. Plan with AVRIL

```text
Using code-writer + avril to run the Automated Visionary Review Iteration Loop
on this intent until every PBI is triple-blessed:

INTENT: <one paragraph of what you want to ship>

Propose small vertical-slice PBIs with testable acceptance criteria and scope_out.
Run Product Owner → QA Architect → Visionary CTO until each item has explicit BLESS.
Emit a Blessed Backlog Summary and stop — do not implement code.
```

**Expected artifacts:** PBI set (Pinto or portable shape), triple-`BLESS` log, Blessed Backlog Summary. Planning **stops** here.

### 2. Execute with AXEL

```text
Using code-writer + axel (+ rust-code-writer + rust-team-lead if this is Rust)
to execute the next blessed PBI through PETC until AC are evidenced and the board is honest.

Intake: only PBIs from the Blessed Backlog Summary / avril-blessed marker.
For each phase: Generator → Reviewer → Tester → Architect BLESS, then commit + track.
Record AC evidence before moving to done. Conductor does not write production code.
```

**Expected artifacts:** small commits with PBI ids, green verification matrix, AC checkboxes evidenced, board status honest.

## Slash commands

`harness-bootstrap` also installs `.opencode/` so the pair is one keystroke away:

- `/avril` — planning conductor. Bare `/avril` is a read-only status report.
- `/axel` — execution conductor. Bare `/axel` reports the next blessed PBI and asks before running anything.

**Restart opencode** after bootstrap; config is read at startup. Re-running the bootstrap never overwrites `.opencode/` files you have customized — it lists what it kept. Verify the layer with `just opencode-verify`.

## Related

- [AVRIL](../pipeline/avril.md) · [AXEL](../pipeline/axel.md) · [Skills catalog](../skills/overview.md)
