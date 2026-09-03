# Tooling

One gate. Pinned formatter. Stdlib first. `open` hygiene.

## Rules

RC-01  The completion gate is `dune build @check @fmt @runtest`. It is clean before any change is done.
       check: dune build @check @fmt @runtest; on a project without `.ocamlformat`, the RC-03 gate `dune build @check @runtest`

RC-02  Zero warnings, warnings as errors. Fix the warning: exhaustive match, rename the unused binding.

RC-03  OCamlFormat is applied with `version` pinned in `.ocamlformat` when the project is formatted (`ocamlformat` installed and `.ocamlformat` present). When it is not, the gate is `dune build @check @runtest`, formatting is hand-consistent with the file's existing style, and the missing formatter is named in the completion report — never silently skipped, never installed without approval.

RC-04  No `print_endline` / `Printf` debugging leftovers and no commented-out code in production paths.
       check: rg 'print_endline|Printf\.printf' --glob '*.ml' → review each hit

RC-05  No `;;` in source files. It is for the toplevel only.
       check: rg ';;' --glob '*.ml' → 0

RC-06  Prefer the standard library. Any third-party dependency (Base / Core, containers, lwt, eio, fmt, alcotest) needs explicit user approval.

RC-07  A library already in the project is used; a second one for the same job is not added.

RC-08  Prefer `Re` over `Str` and `Fmt` over `Printf` for structured output, only after approval when they are not already dependencies. Stdlib `Format` is always allowed.

RC-09  No file-level `open` of `List` / `Array` / `String` (silent `map` / `length` clashes). Use qualified names, aliases, `let open M in`, or `M.(...)`. Exception: `Format` — open it if you use it, so `Stdlib` print and `Format` print never mix.
       check: rg '^open (List|Array|String)$' --glob '*.ml' → 0

## How

The gate is a completion condition, not a suggestion. `@check` type-checks everything including tests; `@fmt` fails on any formatting diff; `@runtest` runs the suite.

A project without `.ocamlformat` gets the two-target gate and a sentence in the report saying so. Installing a formatter into someone's project is a dependency decision, and dependency decisions are the user's.

`open List` at the top of a file turns `map` into `List.map` for every reader who did not scroll up. `let open List in` inside one function is fine — the scope is visible.

A new opam dependency is a thing the next human has to trust and build. Ask first.
