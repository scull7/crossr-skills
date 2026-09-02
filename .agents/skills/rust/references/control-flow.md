# Control flow

Flat combinators first. Nesting is a smell.

## Rules

RF-01  Prefer combinators + `?`, then early returns / guards, then small private helpers.

RF-02  Nesting deeper than 3–4 levels is forbidden.

RF-03  Max 5 parameters per function; use a builder or config struct beyond that.

RF-04  Prefer borrowing (`&T`, `&mut T`) over ownership when either works.

RF-05  Match exhaustively. A `_` arm that hides a real case is a defect.

RF-06  Single responsibility per function and type.

## How

Priority is strict:

1. `map` / `and_then` / `or_else` / `inspect` / `transpose` + `?`
2. Guard clauses that return early
3. A helper with a name that states the case

Arrow code, triple-nested loops, and `match` inside `if let` inside `for` fail this topic. Extract until the happy path reads left-to-right.

`map_err` in a combinator chain that *defines* a conversion is not the call-site `.map_err` that error-handling forbids. If you are wrapping at the use site, you want a `From` impl instead.
