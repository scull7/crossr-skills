# Type system and data

Newtypes as data. Option over sentinels. Immutable by default.

## Rules

RD-01  Use newtypes for semantically distinct values.

RD-02  Prefer `Option<T>` over sentinel values or boolean flags.

RD-03  Derive `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash` where those traits are honest.

RD-04  `#[derive(Default)]` only when a truly sensible default exists.

RD-05  Treat data as immutable by default.

## How

`UserId(u64)` and `OrderId(u64)` are different types. Mixing them is a compile error, not a review comment.

A `status: i32` where `0` means missing is a sentinel. Use `Option<Status>`. A `is_admin: bool` paired with `role: String` is a flag hiding an enum.

Default is a value the domain believes in. An empty `Config` that will panic on first use is not a default — it is a trap.
