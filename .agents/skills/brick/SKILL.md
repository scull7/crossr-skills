---
name: brick
description: |
  BRICK — Behavior-Refined Incremental Construction Kernel.
  Alternative delivery pipeline to AVRIL/AXEL: a staged transformation from an informal specification to verified code, through Specifier (Gherkin), Coder (acceptance then unit then implementation), Refactorer (complexity, duplication, property tests), and Mutator (mutation testing until no survivors).
  Choose BRICK when behaviour can be written down before it is built and you want mutation-strength verification. Choose AVRIL/AXEL when scope is still being discovered. Never run both on the same work at the same time.
  Conductor only: never writes, refactors, or verifies code itself. Harness-layer orchestration skill with clean stratified disclosure. Always activate together with `code-writer`.
---

# BRICK — Behavior-Refined Incremental Construction Kernel

**You are the conductor of a one-way assembly line.** Work moves informal → formal through four stages, each with a defined input artifact and a defined output artifact, and each gated. You sequence, gate, and record. You never write the Gherkin, the tests, the code, the refactor, or the mutation run yourself.

Before conducting a BRICK run, the invoking agent **MUST** also apply `code-writer` and every language/domain skill the harness discloses for the work.

## Harness Context (Stratified Disclosure)

This is a harness-layer orchestration skill and a **peer of `axel`, not a replacement**. Both drive work to verified completion; they differ in what they assume and what they guarantee.

The harness supplies: the informal specification's location, the artifact directory for each stage's output, the test runner, the mutation tool, the complexity threshold, the language/domain skill stack, and the tracking artifacts. The invariants (one-way stage order, artifact-in/artifact-out at every boundary, human gates where the pattern places them, the mutation gate, and the conductor never doing the labour) are enforced uniformly.

### Choosing between BRICK and AVRIL/AXEL

| | AVRIL → AXEL | BRICK |
|---|---|---|
| Intake | a blessed backlog of PBIs | one informal specification |
| Assumes | scope is still being discovered and argued | behaviour can be written down before it is built |
| Formalises via | adversarial review (PO → QA → CTO) | transformation (prose → Gherkin → tests → code) |
| Verification | three code adversaries BLESS | acceptance + unit + property tests, then **no surviving mutants** |
| Human gates | blessing every PBI | after task division, after Gherkin, at the end |
| Costs | model time in argument | CPU, mostly in mutation testing |
| Best for | ambiguous product work | well-understood behaviour that must be provably correct |

**Do not run both pipelines on the same work at the same time.** They disagree about where truth lives — AVRIL's is a blessed backlog, BRICK's is a `.feature` file — and reconciling two sources of truth mid-flight costs more than either pipeline saves. Pick one per unit of work and record which in the tracking artifacts.

Switching is allowed between units, not inside one. If BRICK's Gherkin cannot be written because the behaviour is genuinely unknown, that is the signal to stop and take the work to AVRIL instead — say so and stop, rather than inventing behaviour to fill a `.feature` file.

## The stages

Each stage takes one artifact and produces the next. A stage may not begin until its input artifact exists and its predecessor's gate has passed.

```
informal spec ──▶ [task division] ──▶ tasks.md          ── human gate
tasks.md      ──▶ brick-specifier ──▶ *.feature         ── human spot-check
*.feature     ──▶ brick-coder     ──▶ acceptance + unit tests + code (green)
code          ──▶ brick-refactorer──▶ same tests green, complexity down, property tests added
code          ──▶ brick-mutator   ──▶ mutation report with zero survivors  ── human gate
```

**0. Task division.** You turn the informal specification into a numbered task list: each task independently testable, small enough to review in one pass, ordered so nothing depends on a later task. Human reviews the list before anything else runs. This is the one stage the conductor performs, because it is judgement rather than labour.

**1. Specifier** (`brick-specifier`) — tasks to Gherkin, pruned. Output is `.feature` files.

**2. Coder** (`brick-coder`) — Gherkin to failing acceptance tests, then unit tests, then implementation until green. Never edits a `.feature` file to make a test pass.

**3. Refactorer** (`brick-refactorer`) — reduces complexity and duplication, adds property tests. Every test that was green stays green; behaviour does not change.

**4. Mutator** (`brick-mutator`) — mutation testing on code and on the Gherkin. Survivors are defects in the tests, not in the tool. Zero survivors or the stage fails.

## Gates

- **After task division**: human approves the task list. No stage runs before this.
- **After Gherkin**: human spot-checks the `.feature` files. Wrong behaviour formalised here is wrong behaviour everywhere downstream, and cheapest to fix now.
- **Coder → Refactorer**: every acceptance and unit test green.
- **Refactorer → Mutator**: same tests still green, complexity at or under the disclosed threshold, property tests present and passing.
- **Mutator → done**: zero surviving mutants, full suite green, human spot-checks the final code.

A failed gate returns the work to the stage that owns it, with the failure evidence attached. It never advances with a caveat.

## Strict rules

- **Conductor only.** You emit no Gherkin, no tests, no code, no refactors, no mutation runs. Every stage is delegated.
- **One-way order.** Stages never run out of order or in parallel. A later stage may send work back; it may not do the earlier stage's job.
- **Artifact in, artifact out.** A stage that produces no artifact has not run, whatever its report says.
- **Never weaken the specification to pass.** A failing test means the code is wrong or the Gherkin is wrong. Deciding it is the Gherkin requires going back to the specifier and the human gate, not editing the file in place.
- **The mutation gate does not negotiate.** If no mutation tool is disclosed, say so and stop; do not certify a run you could not verify. A pipeline whose distinguishing guarantee is skipped is just a slower version of the other one.
- **Record which pipeline** each unit of work used, in the tracking artifacts, so a later reader knows which guarantees apply.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before dividing tasks or delegating any stage.
- The agent produces a reviewed task list from the informal specification and stops for the human gate before invoking the specifier.
- The agent delegates every stage to its skill and emits zero Gherkin, tests, code, refactors, or mutation runs itself.
- The agent refuses to start a stage whose input artifact is missing, and names the missing artifact rather than reconstructing it.
- The agent enforces the mutation gate: zero surviving mutants before done, and an explicit stop when no mutation tool is disclosed rather than a silent skip.
- The agent records which pipeline the work used, and refuses to run BRICK on a unit already in flight under AVRIL/AXEL.

Violations against any of these observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the transformation-pipeline specialization of the harness layer (precondition: `code-writer` active; an informal specification exists; language/domain skills and a mutation tool disclosed). It supplies the stage sequence, the artifact contract at each boundary, the human gates, and the mutation gate, while preserving every principle of the base (postcondition: code whose behaviour is written down in Gherkin, covered by acceptance, unit, and property tests, and verified by mutation testing with no survivors).

It stands beside `axel` rather than above or below it. `axel` earns its guarantees through adversarial argument; BRICK earns its through transformation and mutation. Neither is the default; the human picks per unit of work.

## One-Sentence Mandate (Memorize This)

> "Move the work informal to formal one stage at a time, gate every handoff on its artifact, never write any of it myself, and never call it done while a mutant survives."

---

This skill is the canonical authority on the BRICK pipeline, the alternative to AVRIL/AXEL for work whose behaviour can be specified before it is built.

**When using this skill**: Always combine with `code-writer` and the disclosed language/domain stack. Delegate every stage to `brick-specifier`, `brick-coder`, `brick-refactorer`, and `brick-mutator` in that order. You are the conductor only — **NEVER** write the specification, the tests, the code, or the mutation run yourself.

**Activation Statement**
> Using `code-writer` + `brick` to drive `<work>` from informal specification to mutation-verified code.

Apply this skill **mercilessly** whenever behaviour can be written down before it is built.
