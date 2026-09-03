# Testing

AAA. Every `Error` variant has a producing test. `dune runtest` is the gate.

## Rules

RT-01  Unit tests cover every new calculation and public item.
       tag: test

RT-02  Tests follow Arrange-Act-Assert.
       tag: test

RT-03  Error paths are tested explicitly: every `Error` variant has a test that produces it.
       tag: test

RT-04  One test module per library module (`test/test_foo.ml` for `lib/foo.ml`) when the project uses a test framework; otherwise the project's existing runner.
       tag: test

RT-05  `pp` + `equal` are the testables. Property tests (QCheck) for round-trips and laws. Cram for CLI / HTTP surfaces when the project has them.
       tag: test

RT-06  Tests run via `dune runtest`. Never commit a commented-out test.
       tag: test
       check: dune runtest

## How

A calculation without a test is an unverified claim. A public item without a test is an unpublished contract.

An error variant nobody can produce in a test is either dead or untested. Either way, write the test or delete the constructor.

Actions are mocked at the boundary. Calculations are called with data. If a test needs a clock, the clock is an action the caller injects, not `Unix.gettimeofday ()` inside the function under test.

`Result.get_ok` and `Option.get` are acceptable inside tests, where a failure is a bug in the test.
