# BRICK — the alternative pipeline

BRICK is the second delivery pipeline in this harness. It stands beside AVRIL/AXEL rather than replacing it, and the human picks one per unit of work.

**B**ehavior-**R**efined **I**ncremental **C**onstruction **K**ernel: a staged transformation from an informal specification to code verified by mutation testing.

## When to choose it

| | AVRIL → AXEL | BRICK |
|---|---|---|
| Intake | a blessed backlog of PBIs | one informal specification |
| Assumes | scope is still being discovered | behaviour can be written down first |
| Formalises via | adversarial review | transformation |
| Verification | three code adversaries BLESS | tests, then no surviving mutants |
| Costs | model time in argument | CPU, mostly mutation testing |

Choose AVRIL/AXEL when you are still arguing about what to build. Choose BRICK when you already know, and correctness must be provable.

## The stages

```
informal spec ──▶ [task division] ──▶ tasks.md      ── human gate
tasks.md      ──▶ brick-specifier ──▶ *.feature     ── human spot-check
*.feature     ──▶ brick-coder     ──▶ tests + code (green)
code          ──▶ brick-refactorer──▶ complexity down, property tests
code          ──▶ brick-mutator   ──▶ zero survivors ── human gate
```

Task division is the one stage the conductor performs itself, because it is judgement rather than labour. Every other stage is delegated to its skill, and every boundary carries an artifact: a stage that produced nothing has not run.

## The rules that make it work

**The Gherkin is the specification of record.** From `brick-specifier` onward, no stage may edit a `.feature` file. Changing behaviour means returning to the specifier through the human gate. Editing Gherkin to make a test pass inverts the pipeline.

**Red before green.** `brick-coder` proves every test fails — on its assertion, not on a wiring error — before making it pass. A test that has never been red is an assertion nobody verified.

**Never edit a test to make a refactor pass.** `brick-refactorer` reverts instead. A red test after a refactor means the refactor changed behaviour, and editing the test destroys the evidence that it was safe.

**Zero surviving mutants.** `brick-mutator` mutates both the code and the Gherkin. A survivor is a hole in the tests, killed by strengthening a test — never by narrowing the run. If no mutation tool is available, BRICK stops rather than certifying an unverified run.

## Do not run both pipelines on the same work

AVRIL's source of truth is a blessed backlog; BRICK's is a `.feature` file. Reconciling two sources of truth mid-flight costs more than either pipeline saves. Switch between units of work, never inside one, and record which pipeline a unit used so a later reader knows which guarantees apply.

If the Gherkin cannot be written because the behaviour is genuinely unknown, that is the signal to stop and take the work to AVRIL — not to invent behaviour to fill a `.feature` file.

## Related

- [AVRIL](avril.md) · [AXEL](axel.md) · [Pipeline overview](overview.md)
- HARNESS-SPEC §4.4 documents the choice.
