---
name: orchestrator-prompt
description: |
  Generates a ready-to-paste ORCHESTRATOR AGENT prompt (stateless AXEL builder / AVRIL verifier / ACCEPTANCE persona loop over opencode runners) for any given project.
  Fills the canonical template in `assets/orchestrator-prompt-template.md` from the project's repo, harness artifacts, and plan; leaves no `{{placeholder}}` behind; ends with unresolved questions instead of inventing facts.
  Use whenever a human wants "an orchestrator prompt for <project>". The output is a prompt for a frontier-model orchestrator — this skill never runs the loop itself.
  Harness-layer generator skill with clean stratified disclosure. Fully portable across agentskills.io environments and models. Always activate together with `code-writer`.
---

# Orchestrator Prompt Generator

**You are a prompt author, not an orchestrator.** Your only deliverable is one self-contained orchestrator prompt for the named project, produced by filling `assets/orchestrator-prompt-template.md` with facts you have verified from the project. You do not dispatch runners, edit ledgers, or execute the loop.

Before generating, the invoking agent **MUST** also apply `code-writer`.

## Harness Context (Stratified Disclosure)

This is a harness-layer generator skill. The template it fills describes a three-persona loop — **AXEL** (stateless builder), **AVRIL** (stateless verifier), **ACCEPTANCE** (adversarial end-user on the judge model) — driven by a frontier-model orchestrator over `opencode run --pure` sessions.

Naming note: the *runner* personas AXEL/AVRIL in the generated prompt are stateless labor roles. They are distinct from the `axel` (execution conductor) and `avril` (planning GAN) skills in this catalog; the generated orchestrator plays the conductor role the `axel` skill describes, and its PLAN is typically an AVRIL-blessed backlog.

Concrete values — repo path, default branch, plan/ledger paths, CI gate, runner/judge model ids, opencode binary, escalation owner, project invariants, acceptance persona — are parameters disclosed by the invoking harness (root rules file, HARNESS-SPEC or equivalent, justfile, plan documents, Pinto/backlog state) or supplied by the human. The invariants of this skill (verbatim template body, every placeholder resolved or explicitly listed as unresolved, invariants and acceptance persona derived from the project rather than generic, no runner execution) are enforced uniformly.

## Inputs

| Input | Source (in priority order) | Default if absent |
|-------|----------------------------|-------------------|
| `PROJECT_NAME`, `REPO` | human request → git root | unresolved question |
| `DEFAULT_BRANCH` | `git symbolic-ref refs/remotes/origin/HEAD` → local branch | `main` |
| `PLAN` | human → `docs/plans/*` / backlog summary / `features.json` phase | unresolved question |
| `LEDGER` | human → existing ledger | `docs/<project>-ledger.md` (state that it does not yet exist) |
| `CI_GATE` | justfile / CI workflow / rules file | unresolved question |
| `RUNNER_MODEL`, `JUDGE_MODEL`, `MODEL_POOL` | human → `.opencode/` config → `opencode models` | template MODEL POOL (Kimi K3, GLM 5.2, DeepSeek, Ox Alpha Free); cheapest `go`-covered for runners, strongest for judge; ids flagged if unresolved |
| `OPENCODE_BIN` | human → `which opencode` | `~/.opencode/bin/opencode` |
| `BRIEF_DIR`, `RUN_DIR` | human | `/tmp/<project>/briefs`, `/tmp/<project>/runs` |
| `INVARIANTS` | rules file, HARNESS-SPEC, skills in play, plan | **never generic** — derive ≥3 project-specific ones or ask |
| `ACCEPTANCE` persona | plan's real end user, runbooks, demos | **never generic** — describe concretely or ask |
| `ESCALATE_TO` | human → git user | unresolved question |
| Off-limits resources, DoD | plan | unresolved question |

## Procedure (Exact Flow)

1. **Read** `assets/orchestrator-prompt-template.md` in full. It is the verbatim body; do not paraphrase, reorder, or drop sections.
2. **Gather** every input from the table above using the project's actual artifacts. Read before writing: rules file, harness spec, justfile/CI, plan, existing ledger, coding-standard skills in play.
3. **Keep** the TOKEN EFFICIENCY block and its `go`-subscription preference verbatim; only substitute concrete model ids and a project-specific tiering note if the human supplies one.
4. **Derive** project-specific INVARIANTS (from the rules file, spec policy gates, and plan constraints) and a concrete ACCEPTANCE persona (from who actually consumes the plan's deliverable). Keep the two fixed invariants ("Never fake", "Never weaken") verbatim.
5. **Fill** every `{{…}}`. A value you cannot verify is not guessed; write `TODO(<question>)` in place and add the question to the unresolved list.
6. **Write** the result to the path the human names (default `docs/orchestrator-prompt.md`; HTML twin optional per harness HTML-first guidance) and echo it.
7. **Verify** mechanically: `grep -c '{{' <output>` must be `0`; every PARAMETERS line has a value; INVARIANTS has ≥3 project lines plus the two fixed ones; ACCEPTANCE names a concrete user, traits, sub-personas, and approval rule; DoD and off-limits list come from PLAN.
8. **Close** with `## Unresolved questions` (may be empty) — never with an offer to start the loop.

## Boundaries

- **Generate only.** Never run the opencode probe, dispatch a runner, create the ledger, or modify the plan.
- **Verbatim body.** Edits are confined to placeholder slots and the two blocks the template marks EDIT FOR THE PROJECT. The TOKEN EFFICIENCY default (sub-agents via opencode, MODEL POOL, `go` subscription first) is never weakened.
- **No invented facts.** Model ids, paths, commands, and owners come from artifacts or the human.
- **Single deliverable.** One prompt file per invocation; regenerating overwrites it idempotently.
- **Fail loud.** Missing plan, ambiguous CI gate, or a DoD that conflicts with a derived invariant is surfaced in the unresolved list, not smoothed over.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before reading any project artifact.
- The agent reads the template asset and the project's rules file, spec, plan, and CI entrypoint before emitting any output.
- The generated prompt contains zero `{{` sequences; every unresolvable slot is a `TODO(...)` mirrored in the unresolved-questions list.
- The INVARIANTS block contains at least three invariants traceable to named project artifacts plus the two fixed invariants verbatim.
- The ACCEPTANCE persona names a concrete real user of the plan's deliverable with enacted traits, sub-personas, and the approval rule — not the template's bracketed examples.
- The agent performs no orchestration action (no probe, no runner launch, no ledger or plan edit) and ends with an unresolved-questions section.

Violations against any of these observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dedicated orchestrator-prompt generation specialization of the harness layer (precondition: `code-writer` active; a target project with a rules file, CI entrypoint, and plan available or disclosed). It supplies the verbatim orchestrator template, the input-sourcing table, derivation rules for project-specific invariants and acceptance persona, the mechanical placeholder check, and the generate-only boundary, while preserving every principle of the base (postcondition: a single self-contained prompt file with no placeholders and an explicit unresolved-questions list).

## One-Sentence Mandate (Memorize This)

> "Fill the orchestrator template for this project from verified artifacts, leave no placeholder or invented fact, make invariants and the acceptance persona project-specific, and never run the loop yourself."

---

This skill is the canonical authority on producing orchestrator prompts for stateless AXEL/AVRIL runner loops in agentskills.io harnesses.

**When using this skill**: Always combine with `code-writer`. Read first, derive second, fill third, verify fourth. You are the author only — **NEVER** the orchestrator.

**Activation Statement**
> Using `code-writer` + `orchestrator-prompt` to generate a self-contained orchestrator prompt for `<project>` from its harness artifacts and plan.

Apply this skill **mercilessly** on every "write me an orchestrator prompt" request.
