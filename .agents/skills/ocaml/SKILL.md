---
name: ocaml
description: |
  OCaml language book. Card routes to situational references. Generator loads How + Rules for the situation; adversaries load the generated RULES.md only.
  Fully portable across agentskills.io environments and models. Always activate together with `code-writer`.
metadata:
  book: "true"
---

# OCaml Book

Load `code-writer` first. This card says which reference applies. It is not the law.

Anti-Pattern Severity / Fines live in `code-writer`. Do not photocopy them here.

## When to load which reference

| Situation | Load |
|---|---|
| `result` values, error variants, exceptions, `Fun.protect` | `references/error-handling.md` |
| JSON / SQL / HTTP / CLI strings → domain types at the adapter | `references/input-parsing.md` |
| Stratified modules, dune layering, pure calculations | `references/layering.md` |
| Combinators, nested `match`, exhaustiveness, parameters | `references/control-flow.md` |
| `let*` / `let**`, `Result.Syntax`, stdlib-version caveats | `references/monads.md` |
| Tests, AAA, `dune runtest`, QCheck, cram | `references/testing.md` |
| `.mli`, abstract `type t`, odoc | `references/api-surface.md` |
| dune gate, ocamlformat, `open`, third-party deps | `references/tooling.md` |
| `Obj.magic`, partial functions, `[@warning]`, tail calls, secrets | `references/safety-performance-and-security.md` |

Generator: this card + the reference for the situation (Rules + How).
Adversaries: `RULES.md` only. Never `references/`.
Test verifier: rules tagged `test` in `RULES.md`.

Contract refs (not topics; extractor skips them): `references/specialization.md`, `references/verification.md`.

## Topic prefixes

Registry: `docs/book-topics.md`. This book shares RE RP RL RF RT RA RC RS with the rust baseline and mints `RM` (monads). It has no RD: OCaml's type surface is the `.mli` and lives under RA.

## One-Sentence Mandate (Memorize This)

> Load the ocaml book with `code-writer`; apply the reference that matches the situation; adversaries read RULES.md only.

**When using this skill**: Always combine it with `code-writer`. Pick the reference that matches the work. Do not load every reference.

**Activation Statement**
> Using `code-writer` + `ocaml` for this OCaml work.
