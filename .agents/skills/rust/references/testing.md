# Testing

AAA. Error paths. Tests live under `cfg(test)`.

## Rules

RT-01  Unit tests cover every new calculation and public item.
       tag: test

RT-02  Tests follow Arrange-Act-Assert.
       tag: test

RT-03  Test code lives in `#[cfg(test)]` modules.
       tag: test

RT-04  Every error path is exercised. Happy path is not enough.
       tag: test

RT-05  Never commit commented-out tests.
       tag: test

RT-06  Mock actions at integration edges. Never mock calculations.
       tag: test

RT-07  `cargo test --workspace` is clean before the change is done.
       tag: test
       check: cargo test --workspace

## How

A calculation without a test is an unverified claim. A public item without a test is an unpublished contract.

Actions are mocked at the boundary. Calculations are called with data. If a test needs a clock, the clock is an action you inject — not a `SystemTime::now()` inside the function under test.

`cargo test --workspace` is the gate. "It passed on my machine" is not a verdict.
