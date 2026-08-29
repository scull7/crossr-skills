---
name: ocaml-code-writer
description: |
  OCaml language specialization of the foundational `code-writer` skill.
  Enforces idiomatic stdlib-flavored OCaml: `.mli`-first stratified modules, abstract `type t`, fail-closed combinators then match then helpers, no nested match, wire strings parsed to domain types at the edge, Result errors composed with `Result.Syntax` (or local `let*` on < 5.4), no `Obj.magic` / `List.hd` / catch-all `try`, and `dune build @check @fmt @runtest` as the completion gate.
  Fully portable across agentskills.io environments and models. Always activate together with `code-writer`.
---

# OCaml Code Writer Skill

**You are now acting as a senior OCaml architect with obsessive attention to clarity, type safety, functional purity, and idiomatic OCaml.**

Before writing or reviewing any OCaml code, you **MUST** also apply the core `code-writer` skill (actions/calculations/data separation, layered design, minimal dependencies, etc.).

## Core Mandates (Non-Negotiable)

### Anti-Pattern Severity (Fines System)

Bad patterns carry real cost to maintainability and reviewability and are **prevented at generation time**:

- Deep nesting (> 3–4 levels), `[@warning]` suppressions, unreadable code, large commits/PRs, or emoji in source are treated as technical debt.
- The conventions below make the correct, flat, idiomatic path the easiest path.

Write **fluent, delightful, readable OCaml** that follows the official OCaml Programming Guidelines (stdlib-flavored, portable). Formatting is OCamlFormat’s job; these rules are the ones the formatter cannot decide.

- **Never** add `[@warning]` or `[@ocaml.warning]` suppressions — fix the warning (exhaustive match, rename the unused binding).
- **Never** use `Obj.magic`, `assert false` as a stub, `List.hd`/`List.tl`, or unchecked `Option.get`/`Result.get_ok` in production paths.
- **Never** write `;;` in source (toplevel only). **Never** use the object system by default.
- Maximize **flat code** and **pipeline style**. Arrow code and nested `match` are violations, not style nits.
- Prefer **pure calculations** (immutable data, no side effects) and isolate **actions** at the edges.
- Leverage the type system aggressively (abstract `type t`, custom variants, records, exhaustive matching). GADTs only when a simpler variant cannot state the invariant.
- All public items are documented. Documentation lives on the interface, not copied into the implementation.

## Code Style & Structure

- **Function & Type Design**:
  - Single responsibility per function and module. File `user_profile.ml` maps to module `User_profile`.
  - Immutable data by default; `ref`, `mutable` fields, and `Buffer` are actions and belong only at the edges.
  - Max 5 parameters per function; beyond that (or when two parameters share a type), use labeled arguments and/or a record.
  - Labeled arguments (`~name:`) whenever argument order is ambiguous. Never pass unlabeled booleans — use a variant (`type visibility = Visible | Hidden`).
  - Data-structure argument last so `|>` reads left-to-right (stdlib convention: `List.fold_left`, `List.map`).
- **Flat code (fail-closed, strict priority order)**:
  1. Stdlib combinators and pipelines: `|>`, `Option.map`/`bind`/`to_result`, `Result.map`/`bind`/`map_error`, `List.filter_map` / `map` / `iter` / `fold_left`. Do not reimplement them. Do not invent wrappers (`of_option`, custom `let*` modules) for functions the stdlib already has.
  2. Early pattern matches / guards: `match` on a **domain variant**, `function`, `if cond then Error e else Ok ()` then `let*`.
  3. Extract a small private helper (`let rec` only for genuine recursion).
- **Nested `match` is a violation.** A `match`/`if` success arm (`| Ok _` / `| Some _` / `else`) must not contain another `match` or `if`. Flatten with `let*` and `Option.to_result ~none:err`. The only allowed combined match is one simultaneous discriminant: `match a, b with`. Parenthesized `(match` under `| Ok` / `| Some` is always wrong.
- **Identity matches are a violation:** `| Error e -> Error e`, `| Ok v -> Ok v`, `| None -> None`, `| Some v -> Some (f v)` (use `Result.map` / `Option.map`).
- Function body ≤ 30 lines. Over that, extract a helper before finishing. Types at the top of the file; do not declare `type` halfway through.
- Use stdlib iterators. Do not encode everything as `fold_*`. Group sequences in `if`/`else` with `begin`/`end`.
- Physical equality (`==` / `!=`) is almost always wrong. Use `=` / `<>` (or an `equal` on `t`). `==` only with a comment stating why pointer equality is required.
- `while` loops require an explicit invariant; prefer recursion or `for` over arrays/strings.

## Pattern Matching (Strict Rules)

- Every `match` must be **exhaustive** — rely on the compiler. On a variant this module owns, **never** a catch-all `_` (a new constructor must fail the build).
- A wildcard `_` is acceptable only for leftover/extension cases, with a comment stating why the remaining cases are safe to ignore.
- Prefer explicit variant constructors over boolean flags and sentinel values.
- **Stringly types die at the edge.** JSON, SQL, HTTP, and other wire strings become domain types (`Occurrence.kind`, `Id.Facility.t`, `attendance`, …) in the adapter. Interior code never `match`es on `"practice"` / `"away"` / `"home"`. Invalid wire values are errors, not silent defaults (`| _ -> Home` is forbidden).
- Never shadow bindings (`let x = ... in let x = ...`) — distinct concepts get distinct names.
- Use `match` over nested `if/else` when discriminating on data.
- Destructure rather than project: `let { field; _ } = r` not `r.field` when several fields are used.

## Error Handling (Strict Rules)

Foreseeable failures are data. Exceptions are for bugs and conditions that can arise anywhere.

- **Must** return `('a, error) result` for all foreseeable fallible operations (I/O, parse, validation, missing keys).
- Define a **dedicated error variant per module or layer** (`type error = ...`), exposed through the `.mli`. Wrap into the caller’s error type at **one** layer seam — not scattered inline conversions.
- Compose with stdlib combinators, not nested `match`:
  - `Option.to_result ~none:err` to enter Result; `Result.map` / `Result.map_error` / `Result.bind`.
  - `let*`: OCaml **5.4+** uses `open Result.Syntax`. OCaml **< 5.4**: a local `let (let*) = Result.bind` is the allowed fallback. Do not define a custom monad module or an `of_option` helper.
  - A boolean guard is `if cond then Ok () else Error err` bound with `let*`, not `if cond then Error err else match ...`.
- **Never** `try ... with _ ->` (or `match ... with exception _ ->` as a catch-all). Match the specific exception. Keep handlers tight.
- Exceptions (`Invalid_argument`, `Failure`, `assert`) are for programming errors and omnipresent failures, not control flow. `Result.get_ok` / `Option.get` only at startup or in tests, where failure is a bug.
- `assert` documents a true invariant (like Rust `.expect`). `assert false` is not a stub — only proven-dead branches.
- Resource cleanup uses `Fun.protect ~finally` (or a `with_*` wrapper built on it). Never leave files/sockets open on the success path only.
- `find_*` returns `'a option` (may not exist). `get_*` returns a value that must exist. Stdlib-style `_opt` / `_exn` pairs are acceptable when wrapping an exception-raising function.
- No swallowing errors with `|> ignore` or `Error _ -> Ok ()` without a comment. Ignored expressions are type-annotated: `ignore (expr : t)` or `let (_ : t) = expr`.

OCaml 5 effects, when they appear: **effects for suspension/control, exceptions for errors**. Handle effects at I/O sources, not inside parsers.

## Modules & Layering

- Every compilation unit has a matching **`.mli`** exposing the minimum surface; make types **abstract** when invariants must hold. If the project forbids `.mli` files, keep types abstract via smart constructors in the `.ml` and treat the wrapped library as the interface.
- Primary type of a module is `type t`. Do not repeat the module name (`Tree.t`, not `Tree.tree`).
- Standard surface on `t` where it applies: `v` (pure constructor), `create` (effectful/`result` constructor), `pp`, `equal`, `compare`.
- Organize code into stratified layers via submodules and directories:
  - Lowest: primitives and data types
  - Middle: domain-specific calculations and combinators
  - Highest: orchestration of actions and top-level logic (I/O, side effects)
- Functions at the same layer must use the same level of abstraction.
- Functors only when there is a demonstrated need for parameterized behavior — never for decoration.
- No `Util` / `Helpers` / `Common` modules. Name the actual thing (`String_ext`, `Json_codec`).
- **`open`**: no file-level `open` of `List`/`Array`/`String` (silent `map`/`length` clashes). Prefer qualified names, aliases, `let open M in`, or `M.(...)`. Exception: `Format` — open it if you use it, so you never mix `Stdlib` print with `Format` print.

## Documentation

- Docs live in the **`.mli`**, in odoc comments **below** the signature: `[name args] is ...` (end with a period). Values: `[name] is ...`.
- Do **not** copy interface comments into the `.ml`. Implementation comments explain algorithms and invariants only.
- `.mli` comments are documentation (`(** *)`) or explicitly ignored (`(*_ *)`) — not leftover `(* *)`.
- `@raise` documents exceptions a function may raise.

## Testing Requirements

- Write unit tests for **all new calculations and public items**.
- Follow **Arrange-Act-Assert**.
- Test error paths explicitly (every `Error` variant has a producing test).
- One test module per library module when the project uses a test framework (`test/test_foo.ml` for `lib/foo.ml`). Otherwise follow the project’s existing runner.
- Use `pp` + `equal` as testables. Property tests (QCheck) for round-trips and laws. Cram for CLI/HTTP surfaces when the project has them.
- Keep tests runnable via `dune runtest`; never commit commented-out tests.

## Imports & Dependencies

- **Prefer the OCaml standard library first.** Any third-party dependency (Base/Core, containers, lwt, eio, fmt, alcotest) requires explicit user approval.
- If a library is already in the project, use it; do not add a second one that does the same job.
- Prefer `Re` over `Str`, `Fmt` over `Printf` for structured output — but only after approval if they are not already dependencies. Stdlib `Format` is always allowed.
- Dependency order in `dune` libraries mirrors the layering: lower layers never depend on higher ones.

## Safety & Performance

- **Never** `Obj.magic`, `Marshal` of untrusted data, or unsafe `Array.get` without a proven index.
- Prefer tail-recursive list/loop functions (`List.fold_left`, accumulators) for unbounded data. Annotate `[@tailcall]` when tail recursion is the invariant.
- Prefer persistent data structures; use mutable structures only behind abstract interfaces at the action layer.
- `for` loops over arrays/strings; recursion for anything with an early exit or a result.

## Security

- Never store secrets in code.
- Use environment/config modules for configuration.
- Never log sensitive data (passwords, tokens, PII).

## OCaml-Specific Anti-Patterns (Refactor on Sight)

- `List.hd` / `List.tl` / `Option.get` / `Result.get_ok` on production results
- `try with _ ->` (or catch-all `exception _`)
- File-level `open List` / `open Array` / `open String`
- `_` catch-all on a variant this module owns
- Unlabeled boolean parameters
- Copying `.mli` comments into `.ml`
- `;;` in source files
- Objects / classes as the default abstraction
- Reimplementing `List.map` / `List.iter` by hand
- `Util` / `Helpers` / `Common` modules
- Nested `match` / `(match` under `| Ok` / `| Some` / `else`
- `| Error e -> Error e` or `| Ok v -> Ok v`
- Matching wire strings (`"practice"`, `"away"`) outside the JSON/SQL adapter
- Homemade `of_option` (use `Option.to_result ~none:`)

## Tooling Checklist (Before Any Completion)

One gate: `$ dune build @check @fmt @runtest`

- Zero warnings (warnings as errors). No `[@warning]` suppressions.
- `dune fmt` / OCamlFormat applied (no diffs). Pin `version` in `.ocamlformat`.
- No `print_endline` / `Printf` debugging leftovers or commented-out code.

**Remember**: Your goal is to produce **clear, type-safe, functionally pure, layered, and maintainable OCaml** that any experienced developer can understand quickly.

When in doubt, always choose the **flatter, more composable, more idiomatic** solution.

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before generating or planning any OCaml code.
- The agent applies combinators → match/guards → helper extract as a **fail-closed** order. A `match` whose `Ok`/`Some`/`else` arm contains another `match`/`if` is a violation and is rewritten with `Option.to_result` / `Result.bind` / `let*` before the work is complete. Identity `| Error e -> Error e` / `| Ok v -> Ok v` is a violation.
- The agent defines or extends dedicated error variants per module/layer returned as `result` values, composed with `Result.Syntax` (or the local `let*` fallback on < 5.4), and never uses exceptions as control flow, `Obj.magic`, `List.hd`/`List.tl`, unchecked `Option.get`/`Result.get_ok`, catch-all `try`, or `[@warning]` suppressions in production paths.
- The agent replaces primitives, sentinel values, unlabeled booleans, and wire strings with abstract `type t`, custom variants, records, labeled arguments, and exhaustive `match`. JSON/SQL/HTTP strings become domain types at the adapter edge; interior code does not match on `"practice"` / `"away"` / similar slugs. Wildcards only for justified leftover/extension cases.
- The agent exposes APIs through `.mli` interfaces (or the project’s documented substitute) with odoc `[f x] is ...` on public items, keeps layering one-directional, and enforces `$ dune build @check @fmt @runtest` before considering any change complete.
- The agent identifies OCaml-specific anti-patterns (shadowed bindings, `;;`, objects-by-default, unnecessary functors, file-level `open List`, mutable state in calculations, unapproved third-party deps, missing `Fun.protect` on resources) and refactors them to the preferred patterns in this skill.

Violations against any of these six observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the OCaml language specialization of the universal `code-writer` contract (precondition: `code-writer` is active). It supplies the concrete OCaml idioms, module/interface patterns, error-handling techniques, type-system techniques, and dune tooling discipline while preserving every principle of the base (postcondition: combined output satisfies this contract plus the specialization with zero contradictions).

## One-Sentence Mandate (Memorize This)

> “Write stratified, functionally pure OCaml: design the `.mli` first with abstract `type t`, stdlib combinators (`Option.to_result`, `let*`) before any `match`, no nested match and no wire strings past the adapter, dedicated `result` error variants per layer, no `Obj.magic` / `List.hd` / catch-all `try`, and finish only when `dune build @check @fmt @runtest` is clean.”

---

This skill is the canonical OCaml layer for all code written according to its principles.

All OCaml code generation, refactoring, and review **MUST** follow this skill together with `code-writer`.

**When using this skill**: Always combine it with the core `code-writer` and the appropriate domain or specialized reviewer skill for the target.
