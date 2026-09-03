# Type system and data

Newtypes as data. Option over sentinels. Immutable by default.

## Rules

RD-01  Use newtypes for semantically distinct values — especially wire-originated strings (`Email`, `UserId`, …); naked `String` / `&str` must not carry meaning in the core.

RD-02  Prefer `Option<T>` over sentinel values or boolean flags.

RD-03  Derive `Debug`, `Clone`, `PartialEq`, `Eq`, `Hash` where those traits are honest.

RD-04  `#[derive(Default)]` only when a truly sensible default exists.

RD-05  Treat data as immutable by default.

RD-06  Use a builder for complex construction with private fields (invariants enforced in `build()`).

## How

`UserId(u64)` and `OrderId(u64)` are different types. Mixing them is a compile error, not a review comment. The same for strings from the edge: `Email(String)` / `PathBuf`-style wrappers beat a bare `String` that any caller can forge. See also RP-01 / RP-02.

A `status: i32` where `0` means missing is a sentinel. Use `Option<Status>`. A `is_admin: bool` paired with `role: String` is a flag hiding an enum.

Default is a value the domain believes in. An empty `Config` that will panic on first use is not a default — it is a trap.

When a type has private fields and multi-step setup, expose a builder (or a single infallible/fallible constructor) so invalid states cannot be named. RF-03 still covers the over-five-parameters case; this rule covers the private-fields case even with fewer parameters.
