# OCaml architect + reviewer — research context

**Status:** grill locked · prompts issued · 2026-08-29  
**Primary human artifact:** [`ocaml-architect-reviewer-research.html`](ocaml-architect-reviewer-research.html)  
**This file:** agent handoff. Do not generate skills or prompts until the HTML is approved.

This file is evidence + an ownership map. It is not a SKILL.md, not a prompt, and not a split of `store.ml`.

Grill locked. Skill-authoring prompts: [`ocaml-gan-skill-authoring-prompts.html`](ocaml-gan-skill-authoring-prompts.html).

---

## 1. What to build

Rust already has a three-gate code GAN: writer → reviewer → tester → architect. OCaml has only the writer. This wave adds the three quality/architecture gates, not a team-lead.

| Rust | OCaml analog | Job |
|------|----------------|-----|
| `code-writer` | `code-writer` | Universal base. Shared. |
| `rust-code-writer` | `ocaml-code-writer` | Exists. Generation law. Do not duplicate it. |
| `rust-code-reviewer` | `ocaml-code-reviewer` | Pedantic line-level reject of writer violations. |
| `rust-code-tester` | `ocaml-code-tester` | Coverage + exhaustive error-path gate. Never writes production. |
| `rust-architect` | `ocaml-architect` | System-level NACK. Never writes or suggests code. |

Names follow the Rust pattern: `ocaml-architect` (not `ocaml-code-architect`), `ocaml-code-reviewer` (the `code-` marks the quality guardian). Activate with `code-writer` + `ocaml-code-writer`.

---

## 2. Ownership split

The writer already failed closed on combinators, nested match, stringly types, and public types at the top of the `.ml`. Architect and reviewer exist because the writer still scoped past two classes of defect: a god-module, and dest code matching wire slugs. Those classes belong to different skills.

### Writer

How the next function is written. Local, syntactic, scorable.

- Combinators → match → helper
- No nested Result/Option match
- No identity match, no homemade `of_option`
- Public types before first `let`
- Parse wire strings at the adapter
- Dedicated `result` errors, local `let*` on < 5.4
- Function ≤ 30 lines

### Reviewer

Did the writer obey the writer? Line-level. Reject and demand the exact fix.

- Every writer fail-closed rule as REJECT
- Dest matching `"practice"` is a writer violation the reviewer must not miss
- `create_body` after a `let` is REJECT, not “later”
- May name the offending function. May not redesign the system.
- Mirrors `rust-code-reviewer`: checklist + fines, not Torvalds-mode

### Tester

Did anyone prove the behaviour? Coverage and error paths. Never writes production code.

- Unit tests for every calculation and public item
- Arrange-Act-Assert. Every `Error` variant has a producing test
- Gate: `dune build @check @fmt @runtest` (and the project’s documented extra aliases, e.g. `@server @frontend`)
- Mock actions at edges only. Domain tests stay pure
- Delegate production fixes to `ocaml-code-writer`. Re-delegate on any gap
- Mirrors `rust-code-tester`: `TEST VERDICT: PASSED | REJECTED`, “it works on my machine is not an answer”
- Does not NACK system shape (architect) and does not re-litigate combinator style except where it made a path untestable

### Architect

What the system is. Seams, layers, 2-year shape. Never writes, edits, or suggests code.

- `store.ml` holding Calendar + Scoresheet + Messages + Payments + Signup is one unit doing five jobs
- A `.mli` exporting more than one dest/page/aggregate is a STOP, not a split recipe
- Layer direction: `shared/` → codec → server / dest. Dest does not own domain law
- Abstract vs concrete `type t` is a seam decision
- Functors, dune library graph, Melange dual-compile of `shared/`
- Output: `BLESSED | REJECTED` only. “Split into X.ml” is implementation leakage

A line-count gate (“split at 400 lines”) is not architecture. It produces `store_types.ml`. The architect names the *flaw* (one compilation unit, five dests). The writer, after a new design is blessed, performs the split along those dests.

---

## 3. Rust analog contracts to copy structurally

Copy shape and gates. Do not copy Rust idioms or Torvalds-onto-OCaml without a decision (see §10).

Canonical sources in this repo:

- `.agents/skills/rust-architect/SKILL.md`
- `.agents/skills/rust-code-reviewer/SKILL.md`
- `.agents/skills/rust-code-tester/SKILL.md`
- `.agents/skills/ocaml-code-writer/SKILL.md` (precondition writer; do not duplicate)
- `HARNESS-SPEC.md` §6 (verification gates) and §11 (GAN personas)

### `rust-architect`

- Precondition: `code-writer` + language writer
- Never writes, edits, or suggests code. Implementation leakage is itself a violation
- Verdict: `ARCHITECTURE VERDICT: BLESSED | REJECTED` plus 2–4 sentences and an Issues list of high-level flaws only
- Checklist: layers, call graph, actions at edges, 2-year obviousness, compliance with base skills
- Personality: blunt, “This is garbage because…”, “NACK.”
- Six scorable verification behaviors including mandate recitation

### `rust-code-reviewer`

- Precondition: `code-writer` + language writer
- Obsessive enforcement of the writer’s rules. Fail any checklist item = reject
- May demand exact fixes / refactor violating code. Must not open a new design
- Fines in spirit ($100 readability, $100,000 for warning suppressions)
- Does not replace the tester (coverage) or the architect (seams)

### `rust-code-tester`

- Precondition: `code-writer` + language writer
- Never writes, edits, or suggests production code. Delegates all implementation to the writer
- 100% coverage on calculations and public items. Every error path exercised
- Strict Arrange-Act-Assert. Pure deterministic tests. Mock actions at edges only
- Verdict: `TEST VERDICT: PASSED | REJECTED` plus missing-tests list
- Personality: untested code is negligence. “It works on my machine is not an answer.”
- Six scorable verification behaviors including mandate recitation

---

## 4. What `ocaml-code-writer` already owns

Reviewer enforces these. Architect assumes them and rejects designs that make them unenforceable. Do not restate them as new law in the new skills except as REJECT checklist items (reviewer) or “design must make these enforceable” (architect).

- `.mli` first, abstract `type t` when invariants must hold
- Public types at top of `.ml`, `.mli` order, before first value binding
- Stdlib combinators before match before helper extract — fail-closed
- Nested match under `| Ok` / `| Some` / `else` is a violation
- Identity matches are a violation. No homemade `of_option`
- `Option.to_result ~none:`, `Result.bind` / local `let*` on < 5.4
- Wire strings die at the JSON/SQL/HTTP adapter. Invalid slugs are errors, not `| _ -> Home`
- Dedicated error variant per module/layer as `result`. No exceptions as control flow
- No `Obj.magic`, `List.hd`/`List.tl`, catch-all `try`, `[@warning]`
- No objects by default. No file-level `open List`. No `Util` modules
- odoc `[f x] is ...` on the interface only
- Gate: `dune build @check @fmt @runtest`
- Stdlib-first. Base/Core/Or_error require explicit approval — already decided against for CrossR
- Function body ≤ 30 lines

---

## 5. Trusted OCaml corpus

Ranked during the writer research. CrossR dialect is **stdlib-flavored community OCaml**, not Jane Street Base/Core. Architect and reviewer must not reintroduce Or_error, ppx_let, or Core as defaults.

| Source | Trust | Take for architect / reviewer |
|--------|-------|-------------------------------|
| [ocaml.org programming guidelines](https://ocaml.org/docs/guidelines) | Canonical | Interface-first, stdlib naming, `|>` data last, no objects by default, physical equality almost never. |
| [ocaml.org error handling](https://ocaml.org/docs/error-handling) | Canonical | Result for foreseeable failure; exceptions for bugs / omnipresent failure. Dedicated error types. Architect: error types wrap at one seam, not in every handler. |
| [RWO error-handling chapter](https://dev.realworldocaml.org/error-handling.html) | High (dialect-aware) | Result vs exception split. Ignore Jane Street Or_error / sexp Error.t as CrossR default. |
| [Jane Street ppx_js_style](https://ocaml.org/p/ppx_js_style/latest) | High, picky | Annotated ignores, `.mli` comments are odoc or `(*_ *)`. Do not import dated-deprecation or Core. |
| [Dune style / AGENTS.md](https://discuss.ocaml.org/t/dunes-style-guide/10802) | High | Module naming, small units, dune as the build law. Architect cares about library graph, not fmt. |
| [ocaml/ocaml CONTRIBUTING](https://github.com/ocaml/ocaml/blob/trunk/CONTRIBUTING.md) | High, compiler-specific | Exhaustive match, no warning suppressions. Skip compiler-runtime special cases. |
| lindig/ocaml-style, OCamlverse docs, Xen XAPI | Supporting | Interface comments, no Util modules, named layers. XAPI is a large-system existence proof of `.mli` discipline. |
| CS3110 / UPenn / JHU course notes | Teaching | Use only as examples of exhaustive match and module signatures. Not production law. |

Production-grade OCaml *agent skill* corpus found in the original research: [avsm/ocaml-claude-marketplace](https://github.com/avsm/ocaml-claude-marketplace) only. skills.sh hits were low-install and mostly unrelated. Do not fork that marketplace into CrossR; steal structure (dune gate, `.mli`-first) where it already matches the writer.

---

## 6. Evidence from subzeroplay

The writer regen flattened the Result pyramids and parsed create/rsvp/add bodies at `session_json`. Isolated `dune build @check @runtest @server @frontend` went green. Two leftovers were then classified:

### Architect exhibit — `server/store.ml` ~2287 lines

Not “too many lines.” Calendar, Scoresheet, Messages, Payments, and Signup share one compilation unit. Types for those dests are declared mid-file because the unit is several modules hiding in one file. Moving every type to line 1 without a seam is still a god-module.

Writer rule (now fail-closed): public types before first `let`. Architect rule (proposed): a `.mli` that exports more than one dest/page/aggregate is REJECT. No file names in the verdict.

### Reviewer exhibit — dest `calendar.ml` matching slugs

```ocaml
let kind_label = function
  | "game" -> "Game"
  | "practice" -> "Practice"
  | "activity" -> "Activity"
  | kind -> kind
```

`Occurrence.kind_label` already exists. Form state is still `kind : string`. `| kind -> kind` is the silent default the writer forbids as `| _ -> Home`. Encoding slugs on the way *out* is the adapter. Matching them for labels is interior dest code.

The writer already forbids this. The reviewer exists so an agent cannot “read adapter as server-only” and ship it.

### Other regen constraints the new skills must not forget

- OCaml 5.2 native stdlib has no `Result.Syntax` (Melange does); dual-compile `shared/` forces local `let (let*) = Result.bind`
- Record types in this product stay concrete because store/tests construct them; hide only clearly internal helpers
- `Id.t` stays abstract
- JSON is camelCase on the wire
- No new third-party deps without approval
- Module-level `let (let*) = Option.bind` in `store.ml` means Result `let*` must be local inside Result functions

---

## 7. Proposed architect concerns (system-level only)

These become the OCaml-specific checklist. Still no code, no file-split recipe.

1. **One job per compilation unit.** If the interface names two dests, two pages, or two aggregates, the unit is doing two jobs. REJECT. Do not name the replacement files.
2. **Stratification.** Lowest: identifiers, variants, records. Middle: domain calculations in `shared/` (no I/O). Highest: SQL/HTTP/JSON adapters and dest orchestration. A domain module that knows SQL or JSON is entanglement.
3. **Adapter edges are plural.** JSON decode, SQL row parse, HTTP param, dest JSON decode are all edges. Interior dests and the store must already see domain types. Architect rejects a design that keeps slugs as the dest’s model.
4. **Error seams.** Each layer has its own error type. Conversion happens once at the call into the next layer, not as a forest of inline maps in handlers. Polymorphic variants are allowed; a grab-bag `string` error is not a type.
5. **Abstract vs concrete.** Abstract `type t` when an invariant must hold (`Id.t`). Concrete records when store/tests/dests must construct them. Hiding a record “for cleanliness” that every test rebuilds is a fake seam.
6. **Functors** only for demonstrated parameterization (the Id functor is the existence proof). Functors as decoration = REJECT.
7. **Dune library graph** is the layering. `shared/` must not depend on `server/` or dests. Dual-compile (native + Melange) is a constraint on the domain layer: no I/O, no 5.4-only stdlib in `shared/`.
8. **Effects vs exceptions vs Result** (OCaml 5): effects for suspension/control, exceptions for bugs, Result for foreseeable failure. An effects-based error channel in domain code is entanglement.
9. **2-year test.** A new senior who knows ocaml.org guidelines, not this repo, can find the Team dest without reading 2k lines of store.

---

## 8. Proposed reviewer concerns (line-level)

These are the writer rules restated as REJECT items, plus the dest-adapter reading the writer missed.

- Any `(match` under `| Ok` / `| Some` / `else`
- `| Error e -> Error e` and friends; homemade `of_option`
- Public `type` after a `let`
- Matching `"practice"` / `"away"` / `"home"` / `"attending"` outside a JSON, SQL, HTTP, or dest-encode adapter — including dest label helpers and form state
- Silent slug defaults (`| _ -> Home`, `| kind -> kind`)
- `try with _`, `List.hd`, `Option.get` on production paths, `Obj.magic`, `[@warning]`
- File-level `open List`, unlabeled booleans, `;;`, objects as default abstraction
- Copying `.mli` comments into `.ml`
- Function body over 30 lines without an extracted helper
- Introducing Base/Core/Or_error/ppx_let without recorded approval
- Using module-level `let*` bound to `Option.bind` inside a Result function (the subzeroplay store trap)
- Tooling: `dune build @check @fmt @runtest` not green, leftover `print_endline`

Reviewer personality mirrors the Rust guardian (pedantic, fines, no pragmatic exceptions). It does not NACK system shape. If the only fix is a module split, the reviewer REJECTS the local violation (types mid-file) and leaves the seam to the architect.

---

## 8b. Proposed tester concerns

OCaml-specific translation of `rust-code-tester`. Still never writes production.

- Every new calculation and public `.mli` item has a producing test
- Every `Error` constructor on a public function has a test that yields it
- Arrange-Act-Assert. No commented-out tests. No `print_endline` in tests as the assertion
- Domain tests (`shared/`) are pure: no SQLite, no HTTP, no the clock
- Action-layer tests (store, app) mock or use a fixture DB at the edge; they do not re-implement domain law
- Dual-compile: native `dune runtest` is the suite of record. Melange dests are not exempt from tests of their calculations; absence of a JS test runner is REJECT for dest *calculations*, not for DOM wiring
- Follow the project’s existing runner (subzeroplay: `test/domain_test.ml` expect-style) rather than adding Alcotest/QCheck without approval
- `pp` + `equal` as testables when those exist on `t`
- Gate must actually have been run. Cached “it compiled once” is not a pass
- On failure: re-delegate to `ocaml-code-writer`. Tester does not patch production to make a test green, and does not edit Gherkin/product behaviour to hide a gap

---

## 9. Out of scope this wave

- `ocaml-team-lead` — orchestration analog of `rust-team-lead`.
- A Melange/dest domain skill analogous to `rust-frontend`. Dest slug bugs are reviewer/writer; dest architecture is architect. A separate frontend skill is a later specialization.
- Rewriting `ocaml-code-writer` again, except if generation of the new skills finds a contradiction.
- Performing the `store.ml` split or the calendar dest regen. Those are product work, not skill work.

---

## 10. Unresolved questions (approve or answer)

1. Names `ocaml-architect`, `ocaml-code-reviewer`, `ocaml-code-tester` — **keep** (decided).
2. Architect persona — **decided:** Torvalds attitude and code opinions; structural suggestions allowed, never direct code. Blunt, impatient, `ARCHITECTURE VERDICT: BLESSED | REJECTED`. Never writes or suggests code; implementation leakage is a violation. Do not impersonate Torvalds. No reviewer fines voice on this skill.
3. Architect STOP — **decided:** one compilation unit, one job. If the public interface names two independent aggregates, REJECT and name the extra jobs. Do not bake “dest” into the skill. Do not name replacement files.
4. Reviewer powers — **decided:** REJECT and name the exact writer fix (rule, location, required change). Do not edit production. Fines stay on this skill. Writer generates; reviewer judges.
5. Tester runner — **decided:** follow the project’s existing runner. If none exists, present a choice (do not pick silently): Alcotest + QCheck for native; AVA + fast-check or vitest + fast-check for Melange. No new framework without that choice.
5b. Dual-compile suite of record — **decided:** native `dune runtest` covers `shared/` and native server calculations. Demand a Melange runner only when dest code contains calculations not in `shared/`. View wiring over already-tested domain types is not a missing JS suite. A native domain pass does not excuse an untested dest calculation (e.g. rematching `"practice"`).
5c. Tester writes tests — **decided:** no. List gaps and re-delegate to `ocaml-code-writer`. Tester never writes production or test files.
6. Harness wiring — **decided:** follow-up PR (`og-04` in `features.json`). This wave is the three `SKILL.md` files plus the public catalog. Personas under `.agents/agents/`, HARNESS-SPEC §6/§11, and OpenCode GAN wiring wait until the skills exist.
