# AXEL — Execution Loop

**AXEL** = Automated eXecution Loop.

Skill: `axel` · Persona: `axel-conductor-agent`  
Rust inner GAN: `rust-team-lead` (Reviewer → Tester → Architect)

Normative detail: [HARNESS-SPEC.md §13](https://github.com/scull7/crossr-skills/blob/main/HARNESS-SPEC.md).

## Purpose

Drive **only AVRIL-blessed** (or explicitly human-authorized) PBIs through Plan → Execute → Test → Commit until acceptance criteria have evidence and the board is honest.

The conductor **never writes production code** — it sequences Generator + code GAN.

## Intake gate (non-negotiable)

AXEL starts only if one of:

1. AVRIL Blessed Backlog Summary lists the ids, or  
2. Board items carry a blessed marker (e.g. `avril-blessed`), or  
3. Human authorizes a finite PBI id set  

**Unblessed work is refused.** Scope changes return to [AVRIL](avril.md).

## Per-PBI loop

1. **Select** one ready PBI (deps done; prefer `pinto next`).
2. **Plan** — concise; unresolved questions blocking → stop for human.
3. Board → **in-progress**.
4. **Decompose** into small phases (“phase k of n”).
5. Each phase: Generator → **Reviewer → Tester → Architect** (each must `BLESS`) → commit + tracking.
6. **AC evidence** — every checkbox needs recorded evidence; verification matrix green.
7. Board → review → **done** only when AC complete.
8. PBI Completion Record → next or stop.

## Activation

> Using `code-writer` + `axel` (+ disclosed language/domain skills; Rust: `rust-code-writer` + `rust-team-lead` as inner GAN) to execute the next blessed PBI through PETC until AC are evidenced and the board is honest.

## Rust pairing

- **AXEL** owns intake, board, AC evidence, tracking.  
- **`rust-team-lead`** is the preferred inner code GAN for implementation phases.

## Optional: Mitchell decomposition mode

**Default off.** When enabled (“mitchell” / decomposition mode / harness `decomposition_mode`), AXEL measures phase diffs (`git diff --numstat`, added+deleted) against a threshold (default **1500** LOC). Over-threshold work does **not** commit: decompose → massage tasks → execute chunks (recurse). Parallel subagents optional; sequential always OK. Does not bypass intake or code GAN.

Normative contract: [mitchell-decomposition-contract.html](https://github.com/scull7/crossr-skills/blob/main/docs/plans/mitchell-decomposition-contract.html) (issue #43).
