# Layering

One level of abstraction per function. Actions at the edges.

## Rules

RL-01  Every function operates at one consistent level of abstraction.

RL-02  Calculations are pure. Actions sit at the edges. Data is immutable.

RL-03  Higher layers compose lower ones. The call graph must be obvious.

RL-04  An error type stays in its layer. Crossing a boundary is a `From` conversion, not a mix-in.

## How

A handler that parses, queries SQL, and formats HTML is three layers pretending to be one. Split it.

Calculations take data and return data. They do not touch the clock, the disk, or a socket. Actions do, and they call calculations — never the other way around.

`code-writer` already owns this split. This topic is the Rust shape of it: structs and enums as data, `fn` without `&mut` / I/O as calculation, adapters as action.
