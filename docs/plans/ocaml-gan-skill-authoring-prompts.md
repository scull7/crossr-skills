# OCaml GAN trio — skill-authoring prompts

**Use after** [`ocaml-architect-reviewer-research.html`](ocaml-architect-reviewer-research.html) is approved.  
**This wave is og-02.** Write the three `SKILL.md` files only. Do not edit HARNESS-SPEC, `.agents/agents/`, or OpenCode config (`og-04` is a follow-up PR). Catalog/README/book is `og-03` — skip unless the human asks.

Human-facing twin: [`ocaml-gan-skill-authoring-prompts.html`](ocaml-gan-skill-authoring-prompts.html).

Run **Prompt 1 → 2 → 3** in separate sessions (or one session that writes all three, then stops). Then run **Prompt 4** against subzeroplay to verify the skills change agent behaviour.

Each prompt is self-contained. Paste it as the user message.

---

## Prompt 1 — `ocaml-code-reviewer`

```
You are writing a new CrossR skill. Activate `code-writer` + `skill-evaluator` (and `skill-design-principles` if available).

## Deliverable

Create `.agents/skills/ocaml-code-reviewer/SKILL.md` in the crossr-skills repo
(`/Users/nathansculli/src/crossr-skills`). One file. Do not write tester or architect
in this pass. Do not update `docs/public-skills.json`, README, HARNESS-SPEC,
`.agents/agents/`, or OpenCode config.

## Analog (copy structure, not Rust idioms)

Read and structurally clone:

- `.agents/skills/rust-code-reviewer/SKILL.md` — sections, verification (exactly six
  scorable behaviors), specialization contract, YAML description shape, ruthless
  checklist, fines-in-spirit, personality of a pedantic quality guardian.
- `.agents/skills/ocaml-code-writer/SKILL.md` — the law you enforce. Do not duplicate
  that law as new generation rules. Restate writer fail-closed rules as REJECT
  checklist items only.
- `.agents/skills/code-writer/SKILL.md` — universal precondition.

## Role

Obsessive OCaml code-quality guardian. Did the writer obey `ocaml-code-writer`?
Line-level. Fail any checklist item = REJECT.

**Powers (locked):** REJECT and name the exact writer fix. One sentence per
violation: rule, location (module/function), required change. Do not edit
production. Do not redesign the system. Do not name a module split. If the only
real fix is a seam, REJECT the local writer violation (e.g. public `type` after
a `let`) and leave the seam to `ocaml-architect`. Re-evaluate until a fresh
review would pass. Writer generates; reviewer judges.

**Personality:** pedantic, no pragmatic exceptions, fines in spirit (same scale
as rust-code-reviewer: readability cheap, warning suppressions / `Obj.magic` /
catch-all `try` ruinous). Not Torvalds-mode. Not `NACK.` Not `ARCHITECTURE VERDICT`.

## Dialect (locked, CrossR)

Stdlib-flavored community OCaml. Never recommend Base, Core, Or_error, ppx_let,
or a homemade `of_option`. `Option.to_result ~none:` and `Result.bind` / local
`let (let*) = Result.bind` on OCaml < 5.4.

## REJECT checklist (must appear, portable wording — no product names)

- Nested `match` / `(match` under `| Ok` / `| Some` / `else`
- Identity matches (`| Error e -> Error e`, `| Ok v -> Ok v`, `| None -> None`)
- Homemade `of_option`
- Public `type` (in the `.mli`, or otherwise the module surface) declared after
  the first value binding (`let` / `let rec` / `external`)
- Matching wire slugs (`"practice"`, `"away"`, `"home"`, `"attending"`, …) outside
  a JSON / SQL / HTTP / dest-encode adapter — including dest label helpers and
  form state held as `string`
- Silent slug defaults (`| _ -> Home`, `| kind -> kind`)
- `try with _`, `List.hd` / `List.tl`, `Option.get` / `Result.get_ok` on
  production paths, `Obj.magic`, `[@warning]`
- File-level `open List` / `Array` / `String`, unlabeled booleans, `;;`, objects
  as default abstraction
- Copying `.mli` comments into `.ml`
- Function body over 30 lines without an extracted helper
- Introducing Base/Core/Or_error/ppx_let without recorded user approval
- Module-level `let*` bound to `Option.bind` used inside a Result function
- Tooling gate not green: `$ dune build @check @fmt @runtest`; leftover
  `print_endline`

Adapter encode of slugs on the way *out* is allowed. Interior dest/store code
matching those slugs is not. “Adapter” is not “the server codec only.” Dest JSON
decode is an adapter; dest `kind_label` on strings is interior.

## Skill-file constraints

- agentskills.io YAML: `name: ocaml-code-reviewer`, description that states the
  job, the precondition (`code-writer` + `ocaml-code-writer`), and that it never
  writes production.
- Generic/core: harness-agnostic. No `features.json`, no HARNESS-SPEC, no
  subzeroplay, no dest/store filenames in the SKILL.md.
- Exactly six observable Verification behaviors, including mandate recitation.
- Specialization block: precondition `code-writer` + `ocaml-code-writer`.
- One-Sentence Mandate: memorize-this, OCaml-specific, about judging writer
  compliance — not generating code, not blessing architecture.
- Recite that mandate in the Verification list as the first behavior.

## Do not

- Write `ocaml-code-tester` or `ocaml-architect` in this pass.
- Copy rust `#[allow]`, `anyhow`, `thiserror`, clippy, cargo.
- Soften fail-closed writer rules into preferences.
```

---

## Prompt 2 — `ocaml-code-tester`

```
You are writing a new CrossR skill. Activate `code-writer` + `skill-evaluator`
(and `skill-design-principles` if available).

## Deliverable

Create `.agents/skills/ocaml-code-tester/SKILL.md` in the crossr-skills repo
(`/Users/nathansculli/src/crossr-skills`). One file. Do not write reviewer or
architect in this pass. Do not update catalog, HARNESS-SPEC, `.agents/agents/`,
or OpenCode config.

## Analog (copy structure, not Rust idioms)

Read and structurally clone:

- `.agents/skills/rust-code-tester/SKILL.md` — gate personality, exact
  `TEST VERDICT: PASSED | REJECTED` output format, missing-tests list, six
  verification behaviors, specialization, “never write production”,
  “it works on my machine is not an answer.”
- `.agents/skills/ocaml-code-writer/SKILL.md` — what must be testable (calculations,
  public items, every Error variant).
- `.agents/skills/code-writer/SKILL.md` — AAA, calculations trivially unit-testable.

If `ocaml-code-reviewer/SKILL.md` already exists, do not overlap: you do not
re-litigate combinator style except where it made a path untestable. You do not
NACK system shape.

## Role

Obsessive OCaml testing guardian. Did anyone prove the behaviour?

**Powers (locked):**
- Never write production code.
- Never write test files.
- List gaps and re-delegate to `ocaml-code-writer`.
- Output format (exact, no deviation):

```
TEST VERDICT: PASSED | REJECTED

[2-4 sentence analysis: coverage gaps, style violations, missing error paths]

Missing tests:
- function/module X lacks Y
- error path Z untested
```

**Personality:** untested code is negligence. Unapologetic. Brief unless the
explanation prevents a repeat miss.

## Runner law (locked)

1. Follow the project’s existing test runner.
2. If none exists, present a choice. Do not pick silently, do not add a
   dependency without that choice:
   - Native: Alcotest + QCheck
   - Melange: AVA + fast-check, or vitest + fast-check
3. One test module per library module *when a framework is already present*.
   Do not introduce a framework to satisfy that sentence.
4. Dual-compile:
   - Native `dune runtest` is the suite of record for `shared/`-style domain
     libraries and native server calculations.
   - Demand a Melange/JS runner only when dest/frontend code contains
     *calculations* that are not in the shared domain (clock parse, form encode,
     route parse, dest `kind_label` that rematches slugs).
   - View wiring over already-tested domain types is not a missing JS suite.
   - A green native domain test does not excuse an untested dest calculation.

## REJECT / missing-test checklist (portable — no product names)

- Public `.mli` item with no producing test
- `Error` constructor on a public function with no test that yields it
- Domain tests that perform I/O (SQLite, HTTP, the clock)
- Action-layer tests that re-implement domain law instead of calling it
- Commented-out tests; `print_endline` as the assertion
- Gate not actually run (`$ dune build @check @fmt @runtest` plus the project’s
  documented extra aliases). Cached “it compiled once” is not a pass
- `pp` + `equal` unused as testables when they exist on `t`

## Skill-file constraints

- YAML `name: ocaml-code-tester`. Description states the gate, the precondition
  (`code-writer` + `ocaml-code-writer`), and that it never writes production or
  tests.
- Generic/core: harness-agnostic. No subzeroplay, no HARNESS-SPEC, no Alcotest
  as a silent default in the description.
- Exactly six Verification behaviors, mandate recitation first.
- Specialization: precondition `code-writer` + `ocaml-code-writer`.
- One-Sentence Mandate about coverage + error paths + re-delegation, not about
  writing tests.

## Do not

- Author example test files in the repo.
- Standardize on Alcotest as mandatory.
- Copy `#[cfg(test)]` or cargo test commands.
```

---

## Prompt 3 — `ocaml-architect`

```
You are writing a new CrossR skill. Activate `code-writer` + `skill-evaluator`
(and `skill-design-principles` if available).

## Deliverable

Create `.agents/skills/ocaml-architect/SKILL.md` in the crossr-skills repo
(`/Users/nathansculli/src/crossr-skills`). One file. Do not write reviewer or
tester in this pass. Do not update catalog, HARNESS-SPEC, `.agents/agents/`, or
OpenCode config.

## Analog (copy structure, not Rust idioms)

Read and structurally clone:

- `.agents/skills/rust-architect/SKILL.md` — system-level only, exact
  `ARCHITECTURE VERDICT: BLESSED | REJECTED` output format, Issues list of
  high-level flaws, six verification behaviors, specialization, iron “NEVER
  write, edit, or suggest code.”
- `.agents/skills/ocaml-code-writer/SKILL.md` — the generation law a design must
  make enforceable. Do not restate it as line-level rules.
- `.agents/skills/code-writer/SKILL.md` — layers, one purpose per module, actions
  at edges.

## Role

Final system-level adversary for OCaml. What is the system? Seams, layers,
2-year shape.

**Powers (locked):**
- Torvalds *attitude and code opinions*: blunt, impatient, “This is garbage
  because…”, “NACK.”
- Structural suggestions allowed. Direct code suggestions forbidden.
  Naming extra jobs is structural. Naming `foo.ml` / a function / a patch is
  implementation leakage and is itself a violation.
- Never write, edit, or suggest code.
- Do **not** impersonate Linus Torvalds (no kernel-mailing-list costume, no
  requirement to “emulate Linus exactly”). The job is the seam.
- No reviewer fines voice. Fines belong on `ocaml-code-reviewer`.
- Output format (exact, no deviation):

```
ARCHITECTURE VERDICT: BLESSED | REJECTED

[2-4 sentence systemic analysis only — stratification, layers, 2-year implications]

Issues (if rejected):
- bullet 1 (high-level architectural flaw only)
- bullet 2
```

## STOP (locked, portable)

**One compilation unit, one job.** If the public interface names two independent
aggregates (two pages, two bounded contexts, two error domains that do not share
a lifetime), REJECT and name the extra jobs. Do not bake product vocabulary
(“dest”) into the skill. Do not name replacement files. A line-count gate
(“split at N lines”) is forbidden — it produces `*_types.ml` dumps.

A functor that instantiates several identifier namespaces is still one job if
that is the module’s purpose. Several unrelated page/aggregate types in one
`.mli` are not.

## OCaml-specific architecture checklist (portable)

1. Stratification: identifiers/variants/records → domain calculations (no I/O) →
   adapters (JSON/SQL/HTTP/dest-decode) and orchestration. A domain module that
   knows SQL or JSON is entanglement.
2. Adapter edges are plural. JSON decode, SQL row parse, HTTP param, dest JSON
   decode are edges. Interior modules must already see domain types. A design
   that keeps wire slugs as the interior model is REJECT.
3. Error seams: dedicated error type per layer; wrap once at the next layer,
   not a forest of inline maps. Polymorphic variants allowed; a `string` error
   is not a type.
4. Abstract `type t` when an invariant must hold. Concrete records when callers
   must construct them. Hiding a record every test rebuilds is a fake seam.
5. Functors only for demonstrated parameterization. Functors as decoration = REJECT.
6. Dune library graph is the layering. Lower libraries never depend on higher
   ones. Dual-compile (native + Melange) constrains the shared domain: no I/O,
   no 5.4-only stdlib in that layer.
7. OCaml 5: effects for suspension/control, exceptions for bugs, Result for
   foreseeable failure. Effects as an error channel in domain code = entanglement.
8. 2-year test: a senior who knows ocaml.org guidelines, not this repo, can find
   a given job without reading a god-module.

Dialect: stdlib-flavored community OCaml. Do not reintroduce Base/Core/Or_error
as architectural defaults.

## Skill-file constraints

- YAML `name: ocaml-architect`. Description states system-level only, never
  writes code, precondition `code-writer` + `ocaml-code-writer`.
- Generic/core: harness-agnostic. No subzeroplay, no `store.ml`, no “dest”.
- Exactly six Verification behaviors, mandate recitation first.
- Specialization: precondition `code-writer` + `ocaml-code-writer`.
- One-Sentence Mandate about guarding OCaml system architecture, seams, 2-year
  coherence — not generating code.

## Do not

- Suggest `split into calendar.ml`.
- Copy cargo/clippy/thiserror.
- Let the reviewer or tester jobs leak in (no nested-match checklist, no
  coverage checklist).
```

---

## Prompt 4 — verify on subzeroplay (after the three skills exist)

```
The three OCaml GAN skills now exist in crossr-skills:

- `.agents/skills/ocaml-code-reviewer/SKILL.md`
- `.agents/skills/ocaml-code-tester/SKILL.md`
- `.agents/skills/ocaml-architect/SKILL.md`

Plus the writer: `.agents/skills/ocaml-code-writer/SKILL.md`
and the base: `.agents/skills/code-writer/SKILL.md`

## Goal

Verify those skills change agent behaviour on a real OCaml codebase
(`/Users/nathansculli/src/subzero/subzeroplay`). Do not treat “dune is green”
as success. Success is: architect NACK the god-module, reviewer name the
stringly dest + mid-file public types, tester list the untested dest
calculations, writer fix only what reviewer/tester named that is in writer
scope.

## Setup

1. Copy the four OCaml/base skills into
   `/Users/nathansculli/src/subzero/subzeroplay/.agents/skills/`
   (`code-writer`, `ocaml-code-writer`, `ocaml-code-reviewer`,
   `ocaml-code-tester`, `ocaml-architect`). Do not invent harness wiring
   (og-04 is a follow-up PR).
2. Recite each skill’s One-Sentence Mandate before using it.
3. Isolate the opam switch. Do not leak another switch’s PATH.
   From `/Users/nathansculli/src/subzero/subzeroplay`:

   env -i HOME="$HOME" PATH="$(pwd)/_opam/bin:/usr/bin:/bin:/opt/homebrew/bin" \
     OPAM_SWITCH_PREFIX="$(pwd)/_opam" \
     CAML_LD_LIBRARY_PATH="$(pwd)/_opam/lib/stublibs" \
     OCAMLPATH="$(pwd)/_opam/lib" \
     dune build @check @runtest @server @frontend

   `ocamlformat` may be missing; report `@fmt` as unverified if so. Do not
   add dependencies.

## Product constraints (do not “improve” these)

- OCaml 5.2 native is OK. Dual-compile `shared/` with Melange: local
  `let (let*) = Result.bind` in Result functions. `store.ml` has module-level
  `let (let*) = Option.bind` — Result `let*` must be local.
- Record types stay concrete when store/tests construct them. `Id.t` stays
  abstract. JSON camelCase on the wire.
- No Reason/ReScript. Syntax is `.ml` and `.mli` only.
- No new third-party deps without approval. Do not add Alcotest.
- Green is `make test` / the isolated dune command above.

## Step A — Architect (read-only)

Activate `code-writer` + `ocaml-code-writer` + `ocaml-architect`.
Do not edit files.

Expected: `ARCHITECTURE VERDICT: REJECTED` on `server/store.ml` because one
compilation unit holds Calendar + Scoresheet + Messages + Payments + Signup
(independent aggregates). Name those jobs. Do **not** name replacement files.
If the skill names `store_calendar.ml` or suggests a patch, the skill failed
and you must fix `ocaml-architect/SKILL.md` in crossr-skills (then recopy).

## Step B — Reviewer (read-only)

Activate `code-writer` + `ocaml-code-writer` + `ocaml-code-reviewer`.
Do not edit files.

Must REJECT at least:

- Public types mid-file in `server/store.ml` (`create_body` et al. after `let`s)
- Dest `frontend/src/dest/calendar.ml` `kind_label` matching `"game"` /
  `"practice"` / `"activity"` and `| kind -> kind`; form state `kind : string`
  when `Occurrence.kind_label` already exists
- Any remaining nested Result match / identity match / homemade wrappers

Each violation: rule, location, required writer change. No module-split recipe.
If the reviewer misses the dest slugs or the mid-file types, the skill failed —
fix `ocaml-code-reviewer/SKILL.md` in crossr-skills (then recopy).

## Step C — Tester (read-only)

Activate `code-writer` + `ocaml-code-writer` + `ocaml-code-tester`.
Do not edit files. Do not write tests.

`TEST VERDICT: REJECTED` with a missing-tests list. Follow
`test/domain_test.ml` (expect-style). Do not propose Alcotest.

Must notice dest calculations that rematch slugs (`kind_label`, `status_label`
in calendar) are untested as domain/dest calculations. Native `dune runtest`
covers `shared/`; do not demand AVA/vitest for pure view wiring.

If the tester writes a test file or adds a framework, the skill failed —
fix `ocaml-code-tester/SKILL.md` in crossr-skills (then recopy).

## Step D — Writer regen (scoped)

Activate `code-writer` + `ocaml-code-writer`.

Apply only the reviewer (and tester-requested tests, which the *writer* writes)
items that are writer-scope:

- Move public types in `store.ml` to the top of the `.ml` in `.mli` order
  before the first value binding. Do **not** split `store.ml`.
- Dest: parse/use domain types; delete slug `kind_label` / `status_label`;
  form state must not be stringly for kind/homeAway/attendance.
- Flatten any remaining nested Result matches with stdlib combinators
  (`Option.to_result ~none:`, local Result `let*`).
- Add the tests the tester listed, in the existing runner, AAA, every named
  Error path.

Do not perform the architect split. Architect remains REJECTED until a later
design. That is correct.

## Step E — Examine whether we made progress

After isolated dune is green, report a table:

| Skill | Expected observable | Happened? | Evidence |
| architect | REJECT store as many jobs, no filenames | | |
| reviewer | REJECT dest slugs + mid-file types | | |
| tester | list dest calculation tests, write nothing | | |
| writer | types at top, dest domain types, no store split | | |

If dune is green but dest still matches `"practice"`, or types still sit at
line 1189, or store was split into `store_types.ml`, the verification failed.
Fix the skill that allowed it, recopy, redo the relevant step.

Write a short HTML report under subzeroplay `docs/` or crossr-skills
`docs/plans/` named `ocaml-gan-subzeroplay-verification.html`.
```

---

## Tracking

`features.json` phase `ocaml-gan-trio`:

- og-01 research — in progress (this prompt pack closes the “awaiting prompts” gate)
- og-02 the three SKILL.md files — pending, use Prompts 1–3
- og-03 public catalog — pending, after og-02
- og-04 personas + HARNESS-SPEC + OpenCode — follow-up, **not** these prompts
