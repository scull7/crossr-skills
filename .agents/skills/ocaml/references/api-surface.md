# API surface

`.mli` first. Abstract `type t`. Docs on the interface.

## Rules

RA-01  Every compilation unit has a matching `.mli` exposing the minimum surface. If the project forbids `.mli` files, types stay abstract via smart constructors in the `.ml` and the wrapped library is the interface.

RA-02  Make types abstract when invariants must hold. The primary type of a module is `type t` — `Tree.t`, not `Tree.tree`.

RA-03  Standard surface on `t` where it applies: `v` (pure constructor), `create` (effectful or `result` constructor), `pp`, `equal`, `compare`.

RA-04  Public types are declared at the top of the `.ml`, in `.mli` order, before the first value binding (`let` / `let rec` / `external`). A private type used by one helper may sit immediately above that helper. Mutually recursive types stay together.

RA-05  GADTs only when a simpler variant cannot state the invariant. Never the object system by default.

RA-06  Every public item is documented in the `.mli`, in odoc comments below the signature: `[name args] is ...`, ending with a period. `@raise` documents every exception a function may raise.

RA-07  Interface comments are never copied into the `.ml`. Implementation comments explain algorithms and invariants only.

RA-08  `.mli` comments are documentation (`(** *)`) or explicitly ignored (`(*_ *)`), never leftover `(* *)`.
       check: rg '^\(\*[^*_]' --glob '*.mli' → 0

## How

Design the `.mli` first. It is the contract; the `.ml` is one implementation of it.

```ocaml
(*_ team.mli *)
type t
(** A team with at least one member. *)

val v : name:string -> members:Member.t list -> t option
(** [v ~name ~members] is the team, or [None] when [members] is empty. *)

val pp : Format.formatter -> t -> unit
(** [pp fmt t] prints [t]. *)

val equal : t -> t -> bool
(** [equal a b] is [true] when [a] and [b] are the same team. *)
```

An abstract `t` with a smart constructor means an invalid team cannot be named anywhere in the program. A public record means every caller can.

A public type declared after a `let` is a violation on sight: move it to the top, in `.mli` order, before finishing.
