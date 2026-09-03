# Error handling

Foreseeable failures are data. Exceptions are for bugs. Partial accessors and catch-all handlers are RS's; this topic does not restate them.

## Rules

RE-01  Every foreseeable fallible operation (I/O, parse, validation, missing key) returns `('a, error) result`. Exceptions are for programming errors and omnipresent failures, never control flow.

RE-02  Each module or layer defines a dedicated `type error = ...` exposed through its `.mli`; a large module with several independent fallible operations defines one per operation family (`signup_error`, `create_team_error`).

RE-03  Wrap into the caller's error type at one layer seam. Never scatter inline conversions across call sites.

RE-04  Compose with stdlib combinators, not nested `match`: `Option.to_result ~none:err` to enter `result`, then `Result.map` / `Result.map_error` / `Result.bind`. Reimplementing one the stdlib has (a homemade `of_option`) is a violation.

RE-05  `assert` documents a true invariant. `assert false` is never a stub — only a proven-dead branch.

RE-06  Resource cleanup goes through `Fun.protect ~finally` or a `with_*` wrapper built on it. Cleanup that runs only on the success path is a defect.

RE-07  `find_*` returns `'a option` (may not exist); `get_*` returns a value that must exist. `_opt` / `_exn` pairs only when wrapping an exception-raising function.

RE-08  Never swallow an error with `|> ignore` or `| Error _ -> Ok ()` without a comment. Ignored expressions are type-annotated: `ignore (expr : t)` or `let (_ : t) = expr`.
       check: rg '\|> ignore\b|Error _ -> Ok \(\)' --glob '*.ml' → review each hit

RE-09  OCaml 5 effects are for suspension and control; exceptions are for errors. Handle effects at I/O sources, never inside parsers.

## How

One error variant per layer, wrapped once at the seam:

```ocaml
(* store.mli *)
type error = Not_found | Sql of string
val find_user : id:Id.User.t -> (User.t, error) result

(* service.ml *)
type error = Store of Store.error | Forbidden

let get_user ~id =
  Store.find_user ~id |> Result.map_error (fun e -> Store e)
```

Bad — the same wrap, pasted at every call site, and a nested match doing what `Result.map_error` already does:

```ocaml
match Store.find_user ~id with
| Ok u -> Ok u
| Error e -> Error (Store e)
```

Entering `result` from an option is `Option.to_result ~none:Not_found`, never a hand-rolled helper. Chaining is `let*` (see `monads.md`).

Files and sockets close in `~finally`. If the happy path closes the handle and the error path does not, the error path leaks.
