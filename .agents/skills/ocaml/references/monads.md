# Monads

One symbol, one meaning, codebase-wide. `let*` is Result. `let**` is Option.

## Rules

RM-01  `let*` is always `Result.bind`; `let**` is always `Option.bind`. Neither symbol is bound to anything else in any file of the codebase.
       check: rg 'let \( *let\* *\) *=' --glob '*.ml' → every hit is `Result.bind`

RM-02  Both operators are declared at the top of the module that needs them (OCaml < 5.4): `let (let*) = Result.bind` and `let (let**) = Option.bind`.

RM-03  On OCaml 5.4+ `open Result.Syntax` may supply `let*`, but a codebase that already declares the operators keeps them. Never `Result.Syntax` in one file and a declared `let*` in another.

RM-04  Never shadow one symbol with the other monad inside a function. A local `let (let*) = Option.bind` in a Result module is forbidden — use `let**`.

RM-05  A boolean guard enters the pipeline as `let* () = if cond then Ok () else Error err in`, not as `if cond then Error err else match ...`.

RM-06  On OCaml ≤ 5.3 and current Melange stdlibs `Option.bind` takes the option first: write `Option.bind x f`. `x |> Option.bind f` does not typecheck.

RM-07  Constructors are not first-class: `Option.map Some_ctor` is illegal. Write the lambda.

RM-08  A combinator missing from the target stdlib falls back to the flat-code order (early match → helper), never to a homemade wrapper or a custom `let*` module.

## How

```ocaml
let ( let* ) = Result.bind
let ( let** ) = Option.bind

let signup ~email ~invite =
  let* email = Email.of_string email in
  let* invite = Invite.find invite |> Option.to_result ~none:No_invite in
  let* () = if Invite.is_live invite then Ok () else Error Invite_expired in
  Ok (Account.v ~email ~invite)

let display_name profile =
  let** first = Profile.first_name profile in
  let** last = Profile.last_name profile in
  Some (first ^ " " ^ last)
```

A reader who sees `let*` anywhere in the codebase knows it is `Result.bind` without opening the module header. That certainty is the whole rule. Re-binding `let*` to `Option.bind` in one file breaks it everywhere.

Option pipelines that need to become a `result` do so once, with `Option.to_result ~none:`, then continue under `let*`. Mixing the two operators in one function is fine; mixing their meanings is not.
