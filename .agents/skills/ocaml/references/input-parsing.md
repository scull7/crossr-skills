# Input parsing

Stringly types die at the edge. The core never matches on a wire string.

## Rules

RP-01  JSON, SQL, HTTP, CLI, and other wire strings become domain types (`Occurrence.kind`, `Id.Facility.t`, `attendance`) in the adapter. Interior code never matches on `"practice"` / `"away"` / `"home"`.
       check: rg '\| *"[a-z_-]+" *->' --glob '*.ml' → every hit is in an adapter module

RP-02  An invalid wire value is an `Error`, not a silent default. `| _ -> Home` at the parse edge is forbidden.

RP-03  A naked `string` from the wire does not cross into the core. The core receives a domain value or nothing.

## How

The adapter owns the vocabulary of the wire and returns `result`:

```ocaml
(* occurrence_json.ml — adapter *)
let kind_of_string = function
  | "practice" -> Ok Occurrence.Practice
  | "game" -> Ok Occurrence.Game
  | other -> Error (`Unknown_kind other)
```

The core signature is `Occurrence.kind -> ...`, never `string -> ...`. A default arm in that parser turns a data error into a wrong schedule.

Once past the edge, dispatch is an exhaustive `match` on the variant (control-flow topic). If the core needs a `match` on a string literal, the adapter is missing a constructor.
