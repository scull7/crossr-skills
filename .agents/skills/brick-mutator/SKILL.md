---
name: brick-mutator
description: |
  BRICK stage 4 and the pipeline's hard gate. Runs mutation testing over the code and over the Gherkin, and treats every surviving mutant as a defect in the tests.
  A surviving mutant is proof that some change to the system breaks nothing observable — which means a test is missing or asserts nothing. Survivors are killed by strengthening tests, never by deleting the mutant or loosening the run.
  Refuses to certify when no mutation tool is disclosed, rather than skipping the gate. Harness-layer BRICK stage skill with clean stratified disclosure. Always activate together with `code-writer` and the disclosed language skills.
---

# BRICK Mutator

**A surviving mutant is a hole in the tests, and it is your job to prove it or kill it.** Mutation testing changes the code on purpose and asks whether anything notices. If nothing does, the suite is weaker than its coverage number claims.

Before running the gate, the invoking agent **MUST** also apply `code-writer` and every language/domain skill the harness discloses.

## Harness Context (Stratified Disclosure)

This is stage 4 of the `brick` pipeline, and the gate that distinguishes it from AVRIL/AXEL. Input is refactored code with a green suite; output is a mutation report with zero survivors.

The mutation tool is a harness parameter — `cargo-mutants` for Rust, `mutmut` or `cosmic-ray` for Python, Stryker for JavaScript and C#, `pitest` for the JVM. **If the harness discloses no mutation tool, say so and stop.** Do not substitute coverage, do not hand-roll mutants, and do not certify the stage. BRICK's whole claim over the other pipeline is this gate; skipping it silently turns BRICK into a slower AXEL with extra ceremony.

Mutation runs are CPU-expensive and are usually the pipeline's bottleneck. That is a known cost of choosing BRICK, not a reason to weaken the run.

## What you do

**1. Mutate the code.** Run the disclosed tool over the changed code. Every mutant that survives is a place where the implementation could be wrong and no test would notice.

**2. Mutate the Gherkin.** Alter the scenarios — change a value, negate an outcome, drop a `Then` — and confirm the acceptance tests fail. An acceptance test that passes against a mutated scenario is not testing that scenario. This catches the failure the code-level run cannot see: tests wired to the implementation rather than the specification.

**3. Kill every survivor by strengthening a test.** For each survivor: name the mutant, explain what it proves is untested, then add or tighten a test so it dies. Re-run to confirm.

**4. Run the full suite.** Green, with the strengthened tests included.

**5. Report.** Mutants generated, killed, survived, and what each survivor taught you. The report is the stage's artifact; a verdict without it has not happened.

## Boundaries

- **Never delete or exclude a mutant to pass.** Exclusion lists are for mutants that are provably equivalent — semantically identical to the original — and each exclusion carries a written reason. "This one is hard to kill" is not a reason.
- **Never weaken the run.** Reducing the mutation set, lowering the threshold, or scoping to easy files inverts the gate. If the run is too slow, say so and let the human decide the scope; do not decide it quietly.
- **Kill survivors with tests, never by changing the code.** Rewriting implementation so a mutant cannot be generated hides the gap instead of closing it.
- **Never edit a `.feature` file** to make a Gherkin mutant die. Same rule as every stage since the specifier.
- **Zero survivors or the gate fails.** There is no partial pass. Report the count and stop; the conductor routes the work back.
- **Equivalent mutants are a claim you must defend.** Show why the mutation cannot change observable behaviour. Unproven equivalence is a survivor.

## Failure modes

| Situation | What to do |
|---|---|
| No mutation tool disclosed | Stop. Report that the gate cannot run. Do not substitute coverage — high coverage with surviving mutants is exactly the condition this stage exists to detect. |
| The run exceeds the time budget | Report the budget and the scope, and ask. Narrowing scope is a human decision, and a narrowed run must be labelled as such in the report. |
| A survivor looks equivalent | Prove it or kill it. Write down why no observable behaviour changes; if the argument is shaky, treat it as a real survivor. |
| A Gherkin mutant does not fail its acceptance test | This is the most serious finding available here: the test is wired to the implementation, not the specification. Report it prominently. |
| Killing a survivor requires new behaviour | Stop. The gap is in the specification, not the tests, and that goes back to `brick-specifier` through the human gate. |
| The tool reports a crash rather than a mutant result | Fix the harness before interpreting anything. A crashed run is not a clean run. |

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before running any mutation.
- The agent stops and reports when no mutation tool is disclosed, and never substitutes coverage or a hand-rolled approximation for the gate.
- The agent mutates both the code and the Gherkin, and reports the two runs separately.
- The agent kills every survivor by adding or tightening a test, never by editing the implementation, deleting the mutant, or narrowing the run.
- The agent defends any equivalent-mutant claim with a written argument, and treats unproven equivalence as a live survivor.
- The agent emits a mutation report — generated, killed, survived, and what each survivor taught — and refuses to certify the stage with a non-zero survivor count.

Violations against any of these observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the verification gate of the `brick` pipeline (precondition: `code-writer` and the disclosed language skills active; refactored code with a green suite; a disclosed mutation tool). It supplies the code and Gherkin mutation runs, the kill-by-test rule, the equivalent-mutant burden of proof, and the refusal to certify without a tool, while preserving every principle of the base (postcondition: zero surviving mutants, a green full suite, and a report explaining what each survivor revealed).

This is what BRICK offers that adversarial review cannot: an adversary that is mechanical, exhaustive within its operator set, and indifferent to how convincing the code looks.

## One-Sentence Mandate (Memorize This)

> "Change the code on purpose and find out what nothing notices; kill every survivor with a better test, never a smaller run, and never certify a gate I could not actually run."

---

This skill is the canonical authority on the verification gate of the BRICK pipeline.

**When using this skill**: Always combine with `code-writer` and the disclosed language stack. Mutate code, mutate Gherkin, kill survivors with tests, report everything. You strengthen the tests — **NEVER** the mutant set, the scope, or the code.

Apply this skill **mercilessly** on every BRICK verification gate.
