# Safety, performance, and security

SOLE OWNER of partial functions, catch-all handlers, and warning suppressions. Other topics cite, never restate.

## Rules

RS-01  Never `Obj.magic`, `Marshal` of untrusted data, or an unchecked `Array.get` without a proven index.
       check: rg 'Obj\.magic' --glob '*.ml' → 0; rg 'Marshal\.' --glob '*.ml' → review each hit; none on untrusted input

RS-02  `List.hd` / `List.tl` / unchecked `Option.get` / `Result.get_ok` never on production results. Startup and tests only, where failure is a bug.
       check: rg 'List\.hd|List\.tl|Option\.get\b|Result\.get_ok' --glob '*.ml' → review each hit; none outside tests / startup

RS-03  Never `try ... with _ ->` or `match ... with exception _ ->` as a catch-all. Match the specific exception. Keep handlers tight.
       check: rg 'with _ ->|exception _ ->' --glob '*.ml' → review each hit

RS-04  Never add `[@warning]` / `[@ocaml.warning]` suppressions. Fix the warning.
       check: rg '\[@+(ocaml\.)?warning' --glob '*.ml*' → 0

RS-05  Tail-recursive list and loop functions (`List.fold_left`, accumulators) for unbounded data. `[@tailcall]` where tail recursion is the invariant.

RS-06  Persistent data structures by default. Mutable structures only behind abstract interfaces at the action layer.

RS-07  Never store secrets in source.

RS-08  Configuration comes from environment or config modules, never from literals in code.

RS-09  Never log passwords, tokens, or PII.

## How

`Obj.magic` is a hole in the type system with no comment big enough to fill it. `Marshal.from_string` on bytes you did not write is remote code execution wearing a stdlib name.

`List.hd []` raises. `Option.get None` raises. In production code that is a crash the type system was built to prevent; the honest shape is a `match` or `Option.to_result`. In `main` at startup or inside a test, a raise is the bug report you want.

`try ... with _ -> default` hides `Out_of_memory`, `Stack_overflow`, and the typo you will spend a day finding. Name the exception.

A `[@warning "-8"]` on a non-exhaustive match is a catch-all with extra steps. The compiler found a missing case; add it.

A `List.map` over a million-element list is fine; a hand-written non-tail `let rec` over the same list is a stack overflow waiting for production data.

Secrets in git are a breach, not a style miss. Logs that print a bearer token are the same class of bug.
