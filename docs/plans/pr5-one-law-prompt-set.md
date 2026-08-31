# PR 5 prompt set v2 — One ruleset per book, progressively disclosed

Plan: `crossr-skills/docs/plans/gan-layer-separation-plan.md` §4 PR 5 / §3.4, plus the parked
items recorded under §4 PR 5 ("Parked here from PR 1a review" and "Parked here from PR 3a / 3b
review"). Preconditions: PR 4 fully landed (skills#110, harness#6); pins are skills
`v1-gan-layers` / loops `v1-cards` everywhere.

## What changed from v1 of this prompt set

| v1 | v2 | Why |
|---|---|---|
| OCaml parked | **OCaml included** (own PR) | One book cannot prove the infrastructure is language-agnostic; hardcoding survives a single-book PR undetected. Elm / TypeScript / JavaScript targets already exist in crossr-using repos. |
| `generate` node → `rust` | **Graph fully neutral**; book disclosed per project | `axel/references/harness-parameters.md` already owns the language stack ("disclose at session start"). The graph naming a language is a second authority for the same fact — the dual-mandate bug (decision #3) reborn. |
| `rust/references/RULES.md` | **`<book>/RULES.md`** | The v1 path put the extractor's output inside its own input glob. Also makes `references/` = generator-only / How-bearing and `RULES.md` = adversary-facing, structurally. |
| 6 topics | **8 topics, per-book sets** | The v1 six left Safety, Security and Code Style homeless *in Rust too*; OCaml additionally orphans monad pipelines and pattern matching. The projection contract is universal; the topic list is per-book. |
| Absorb + delete in one PR | **Additive first, delete last** | Book creation is additive: no window, no dangling name, no coordinated tag. All breakage collapses into the retarget PRs. |
| 6 PRs | **7 PRs**, each smaller | v1's 5a alone was larger than any PR here. |

**Stack (seven PRs):**

```
5a  skills   book infrastructure + rust/ book                     ADDITIVE — deletes nothing
5b  skills   ocaml/ book                                          ADDITIVE — genericity test
5c  skills   gate cards, architecture CP2, domain retargets,
             delete the three absorbed writers
             → cut skills tag v1-one-law on the 5c merge commit
5d  loops    pin; neutral code-gan.json + requires.book; schema +
             verifier; personas; harness-parameters Language stack
             → cut loops tag v1-one-law-consumers on the merge commit
5e  harness  HARNESS-SPEC §6; lockfile books; smoke; dead site gate
5f  skills   loops pin bump + just regen-agents + plan record closing PR 5
5g  landing  (rider, any time after 5c) drop rust-team-lead + the four retired names
```

Tag names are placeholders — pick your own, cut them where the stack says, never re-point a cut tag.

---

## Decisions settled BEFORE dispatch

1. **OCaml is in** (reverses the "park OCaml" recommendation). `ocaml-code-writer` (19,551 B) is
   absorbed in 5b. Rationale: the infrastructure must be language-agnostic for Elm / TS / JS, and
   generality is unfalsifiable with a single book. Second consequence: OCaml gains adversaries for
   the first time (§2.4 `ocaml reviewer ✗ tester ✗ architect ✗`) the moment the gate cards go
   language-neutral in 5c. §7 row 5 is amended in 5f — it is unsatisfiable as written either way.
2. **The graph carries no language.** `code-gan.json`'s `generate` node retargets to `code-writer`,
   not to a book. The book is disclosed per project (`lockfile.toml` `books = [...]`, read at
   pre-flight step 4), and the graph declares `requires.book: true` so "runs without a disclosed
   book" is a mechanical failure rather than prose. Retargeting `generate` to `rust` would pin one
   book inside a shared graph and force `code-gan-<lang>.json` forks with identical topology —
   which is the duplication PR 3 deleted `rust-team-lead` to kill.
3. **The Rules projection is `<book>/RULES.md`** — one generated file per book, committed,
   drift-gated, ids fully qualified. Not under `references/`: that directory is the extractor's
   input, and keeping it How-only makes "the reviewer never sees How" a path rule.
4. **The projection contract is universal; the topic set is per book.** Every reference file carries
   `## Rules` + `## How`; ids are append-only; `RULES.md` is generated. *Which* topics a book has is
   the book's business — JS has no `.mli`, Elm has no `unsafe`. The extractor collects `## Rules`
   blocks from whatever files exist and never hardcodes a topic list.
5. **Staged duplication is allowed and time-boxed.** 5a/5b create books while `rust-code-writer`,
   `rust-errors` and `ocaml-code-writer` still exist. During that window the **old path stays
   authoritative** — `harness-parameters.md` still discloses the Rust triple, so the books are inert
   staging, not a second live law. Superseded skills are frozen (no edits) and carry a deprecation
   marker. Deletion happens in 5c.

---

## Shared guardrails (paste into every brief verbatim)

```
GUARDRAILS (crossr v2 review standard — violations get the PR rejected):
- Read docs/plans/gan-layer-separation-plan.md (the law; §3.4 and §4 PR 5 govern this
  work) and AGENTS.md in the repo you are editing, before writing anything.
- Enumerate EVERY protected-law edit in the PR body, one numbered item each, with the
  exact before/after phrasing. Undisclosed law edits are an automatic REJECT (#107
  precedent).
- No intermediate delta skills (no rust-review, rust-testing) — shape B, decision #2.
- NO BOOK NAME may appear in graphs/, in a gate card (code-review, testing), or in a
  role persona. The book is disclosed per project, never hardcoded. A language-specific
  domain skill (rust-axum-backend, rust-tui, rust-frontend) MAY name its own book —
  that is its subject, not a default. Paste the proving grep in the PR body.
- Never hand-write generated output: graphs/index.html only via verify-graphs --html;
  .opencode/agent/ only via the harness generator; <book>/RULES.md only via
  scripts/extract-rules. Every generator must be idempotent — run it twice, git status
  clean, no timestamps.
- A skill carrying a DEPRECATED marker is frozen: never edit it. Changes go to the book
  that supersedes it.
- Byte tables in the PR body are measured (wc -c on the tree), never estimated.
- Run the repo's validations yourself before opening the PR and paste the results:
  skills: just harness-validate (docs-verify + claude-skills-check + rules-check +
          features.json)
  loops:  just graphs-verify / verify-protocol / verify-skill-refs
  harness: ./test/harness-bootstrap-smoke.sh
- Do not touch progress.md / MIGRATION history, gan-verdict (tokens are final — §4 PR 5
  parked note), or anything outside the declared file list. Scope creep is a REJECT.
- Tags are immutable once cut. Merge order is the stack order. The PR body carries the
  stack line (what merges before, what tag is cut, what comes next).
- The Tester is starved, never deleted. The testing gate card must exist and load.
```

---

## Brief 5a — skills: book infrastructure + the `rust` book (additive)

```
You are implementing crossr v2 PR 5a in sycamore-hq/crossr-skills.

[paste GUARDRAILS]

GOAL — §3.4: one ruleset per language, one location, progressively disclosed, two
projections per topic. This PR builds the book INFRASTRUCTURE and the first book. It
is ADDITIVE: it deletes no skill, renames nothing, and breaks no consumer. The old
Rust path stays authoritative until 5d moves the disclosure. Say that in the PR body —
a reviewer will otherwise read the duplication as the regression this plan exists to cure.

THE PROJECTION CONTRACT (universal; every book obeys it, now and for Elm/TS/JS):
- Every reference file carries exactly two sections:
  ## Rules  — normative, checkable. Each rule <=3 lines. A `check:` command line where
              mechanically checkable. Tag `test` on rules the test verifier owns.
  ## How    — examples, patterns, reasoning. Adversaries must NEVER load this.
- Rule ids: bare `<TOPIC>-nn` in the source file, emitted fully qualified as
  `<book>/<TOPIC>-nn` in the generated projection. Append-only from birth: superseded,
  never renumbered (§3.7 logic applies to rule ids).
- Topic prefix baseline (shared across books so a prefix names a topic regardless of
  language): RE error-handling, RP input-parsing, RL layering, RF control-flow,
  RT testing, RA api-surface, RC tooling, RS safety-and-security.
- The topic SET is per book. Do not hardcode this list anywhere in the tooling.

CREATE .agents/skills/rust/:
- SKILL.md — a ~2 KB card in the style of the PR-4 conductor cards (see crossr-loops
  .agents/skills/axel/SKILL.md at tag v1-cards, 5,989 B, for the shape): which reference
  applies to which situation, nothing else. No persona. A one-sentence contract-summary
  mandate is allowed per the 8920866 foundation-mandate decision; keep it to one sentence.
- references/error-handling.md      RE  — absorbs rust-errors/SKILL.md (5,470 B)
- references/input-parsing.md       RP  — parse-don't-validate, newtypes at the edge
- references/layering.md            RL  — stratification, actions/calculations/data
- references/control-flow.md        RF  — combinator style, nesting depth, exhaustive match
- references/testing.md             RT  — AAA, error paths, cfg(test); rules tagged `test`
- references/api-surface.md         RA  — pub items, docs, semver
- references/tooling.md             RC  — fmt, clippy pedantic, deny lists, approved crates
- references/safety-and-security.md RS  — unwrap/unsafe/overflow, input trust, secrets

  control-flow and safety-and-security are new relative to the plan's six-file sketch.
  The sketch left rust-code-writer's "Code Style & Structure", "Safety & Performance" and
  "Security" sections with no home. Note the addition in the PR body as a disclosed
  refinement of §3.4, not a silent expansion.

SOURCE MATERIAL (measured on main) — COPY, DO NOT DELETE. Deletion is 5c:
- rust-code-writer/SKILL.md      7,674 B
- rust-errors/SKILL.md           5,470 B
- the Rust-specific bodies of rust-code-reviewer (5,059 B) and rust-code-tester
  (5,083 B) — roughly the ~2-3 KB that is actually Rust per §2.3.
Do NOT restate code-writer's Anti-Pattern Severity / Fines System in any reference.
It was deliberately upstreamed (features.json: harness-v2 pr3 "Fines upstream into
code-writer") and BOTH rust-code-writer and ocaml-code-writer photocopy it — that is
the §2.7 photocopy, twice. Cite `code-writer` in one line instead. Same rule for the
Non-Negotiable Core Principles.

CREATE scripts/extract-rules:
- BOOK-GENERIC. Iterates every .agents/skills/*/references/*.md that contains a
  `## Rules` block; emits one .agents/skills/<book>/RULES.md per book. The output path
  is deliberately OUTSIDE references/ so the extractor never ingests its own output.
  Do not hardcode `rust`, and do not hardcode the topic list.
- GENERATED marker at the top of each RULES.md naming this script. Topic headers, rule
  ids fully qualified (`rust/RE-01`), `check:` lines and tags carried through.
- --check mode diffs against the committed file, exits non-zero on drift.
- Fail LOUD on any malformed Rules block (missing id, duplicate id within a book, no
  `## Rules` section in a reference, a rule over 3 lines). Learn from
  scripts/regen-agents (the justfile-strip guard): silent skips manufacture the drift
  this script exists to prevent.
- Deterministic (no timestamps) and idempotent: second run byte-identical.
- justfile: `rules-sync` + `rules-check`; add rules-check to harness-validate.

DEPRECATION MARKERS (rust-code-writer, rust-errors) — one block at the top of each
SKILL.md: superseded-by path, the PR that deletes it (5c), and its measured byte count
at absorb time. The byte count is a drift detector: if it changes during the staging
window, the absorb was no longer a move.

CATALOG BOOKKEEPING:
- docs/public-skills.json: ADD `rust` (category "Rust Book"). Add
  "status": "superseded-by: rust" to the rust-code-writer and rust-errors entries.
  Do not remove them yet. README table must match by name (verify-docs compares names).
  NOTE: verify-docs enforces allowlist -> disk and README == allowlist, but has NO
  reverse check — a skill directory absent from the allowlist passes silently. So an
  unlisted book would leave the catalog carrying an undocumented skill for the whole
  window. List it.
- Grep the catalog for `rust-errors` and `rust-code-writer`; list every referrer in the
  PR body and state that all of them remain correct until 5c (the old path is still the
  live one). Nothing is dangling in this PR — that is the point of the ordering.

VALIDATE: just harness-validate PASS including the new rules-check;
./scripts/extract-rules twice -> git status clean; --check red/green demonstrated (edit
a rule, show it fail, revert, show it pass). wc -c table: rust/SKILL.md (~2 KB target),
each reference, RULES.md.

PR BODY: stack line (5a -> 5b -> 5c, tag v1-one-law on 5c); "ADDITIVE — deletes
nothing, old path authoritative until 5d"; the two added topics disclosed; every
protected-law edit enumerated; the staging-window discipline (frozen skills, markers).
```

---

## Brief 5b — skills: the `ocaml` book (additive; the genericity test)

```
You are implementing crossr v2 PR 5b in sycamore-hq/crossr-skills, stacked on 5a
(the projection contract, the extractor and the rust/ book exist).

[paste GUARDRAILS]

GOAL: a second book. This PR is the test of whether 5a's infrastructure is actually
language-agnostic — the property the whole book model rests on for Elm, TypeScript and
JavaScript, which are already in play in crossr-using repos.

HARD ACCEPTANCE CONDITION:
  This PR touches ZERO lines of scripts/extract-rules and ZERO lines of the justfile
  rules-* targets. If you find you need to change either, STOP and report it — 5a
  hardcoded something and the fix belongs in a 5a follow-up, not here. State the
  zero-line result in the PR body with `git diff --stat`.

CREATE .agents/skills/ocaml/ absorbing ocaml-code-writer/SKILL.md (19,551 B — the
largest file in the catalog). Same contract, same prefixes, ids `ocaml/<TOPIC>-nn`.
Its topic set is OCaml's, not Rust's. From the source headings, expect:
- error-handling      RE  — Result errors, fail-closed combinators
- input-parsing       RP  — wire strings parsed to domain types at the edge
- layering            RL  — Modules & Layering, .ml/.mli stratification
- control-flow        RF  — `let*` = Result / `let**` = Option monad discipline,
                            no nested match, combinators then match then helpers
- testing             RT  — rules tagged `test`
- api-surface         RA  — .mli-first, abstract `type t`, documentation
- tooling             RC  — dune build @check @fmt @runtest, ocamlformat pinning,
                            imports & dependencies
- safety-and-security RS  — no Obj.magic / List.hd / catch-all try, no [@warning]
                            suppressions
Distribute "OCaml-Specific Anti-Patterns" into the topic each belongs to. Do NOT create
an anti-patterns grab-bag reference — a bag with no topic has no reviewer projection.
Do NOT restate code-writer's Fines System (see 5a).

DEPRECATION MARKER on ocaml-code-writer (superseded-by ocaml, deleted in 5c, measured
19,551 B). Do not delete it here.

CATALOG BOOKKEEPING: add `ocaml` (category "OCaml Book") to docs/public-skills.json +
README; mark the ocaml-code-writer entry "status": "superseded-by: ocaml".

VALIDATE: just harness-validate PASS; rules-check now covers BOTH books; extractor twice
-> clean; wc -c table for ocaml/SKILL.md, each reference, RULES.md.

PR BODY: the zero-line extractor result (headline — it is what this PR proves); stack
line; topic-set differences from the rust book and why each is a language fact rather
than a contract violation.
```

---

## Brief 5c — skills: gate cards, architecture CP2, domain retargets, deletions

```
You are implementing crossr v2 PR 5c in sycamore-hq/crossr-skills, stacked on 5b
(both books exist; the three writers are staged for deletion and frozen).

[paste GUARDRAILS]

GOAL: the adversary skills become thin, LANGUAGE-NEUTRAL gate cards named for the
activity (decision #1); every writer-stack reference retargets; the superseded writers
are deleted. After this PR the catalog has ONE writer skill (code-writer) plus N books,
and the tag v1-one-law is cut on the merge commit.

RENAMES (git mv, keep history):
- rust-code-reviewer (5,059 B) -> code-review. Strip to the gate card: what this gate
  verifies, its inputs, the gan-verdict response contract line. Target <=2 KB (§7 row 5).
  INPUTS MUST BE BOOK-AGNOSTIC: "the diff, the brief, and the disclosed book's RULES.md".
  Never `rust/RULES.md` — a gate card naming a book is the monoculture bug one layer up.
  The card must also state that adversaries load RULES.md ONLY, never <book>/references/
  (§3.4: a reviewer fed How suggests implementations).
  The ~2 KB of real Rust law (thiserror / no anyhow / no unwrap / pedantic clippy /
  approved crates) was copied into the rust book in 5a — DELETE it here and prove nothing
  was lost: map every deleted section to its book reference file + rule ids in the PR body.
  Delete the "Non-Negotiable Core Principles" restatement outright (§2.7 photocopy).
- rust-code-tester (5,083 B) -> testing. Same treatment. The tester's Rust delta lives in
  rust/references/testing.md tagged `test`; the card says "rules tagged `test` in the
  disclosed book's RULES.md".
- The verdict gate names in gan-verdict and the response contracts are ALREADY
  code-review: / testing: / architecture: (PR 1a decision) — verify with grep, change
  nothing there.

ARCHITECTURE (protected law — one disclosed edit; architecture/SKILL.md is 4,791 B):
- Core Principle 2, "Violates the principles of `code-writer` + `rust-code-writer` (and
  their specializations)" -> "Violates `code-writer` or the disclosed book's Rules
  projection". Zero other checklist edits (1a's zero-checklist-edits discipline). This
  is the parked 1a item — cite it.

DOMAIN SKILL RETARGETS (measured): rust-axum-backend 7,728 B, rust-tui 7,986 B,
rust-frontend 9,005 B, brick-coder 7,210 B.
- Every "activate together with `code-writer` + `rust-code-writer`" and every "extends
  rust-code-writer" locus -> `code-writer` + the `rust` book. rust-axum-backend alone has
  ~8 loci (frontmatter, MUST-apply, verification scorable, Specialization, mandate,
  activation statement) — enumerate every one, per file, in the PR body.
- These skills MAY name the `rust` book: a Rust domain skill's subject is Rust. That is
  not the hardcoding the guardrail forbids; gate cards and graphs are.
- Domain skills stay separate skills (§8 open q. 4) — do NOT absorb them.

DELETIONS (the staging window closes here):
- .agents/skills/rust-code-writer/, rust-errors/, ocaml-code-writer/ and their Claude
  compatibility copies (via scripts/sync-claude-skills, never by hand).
- docs/public-skills.json: drop all three entries; drop the "status" markers from 5a/5b;
  rust-code-reviewer -> code-review, rust-code-tester -> testing. README table to match.

ACCEPTANCE GREPS, paste results in the body:
  grep -rn 'rust-code-writer\|rust-errors\|ocaml-code-writer\|rust-code-reviewer\|rust-code-tester' \
    .agents/skills/ .opencode/ README.md AGENTS.md docs/public-skills.json
  -> zero hits. History files (progress.md, features.json titles, docs/plans/) are
  excluded by construction — do not edit them.
  grep -rn 'rust\|ocaml' .agents/skills/code-review/ .agents/skills/testing/
  -> zero hits. This is the language-neutrality proof for the gate cards.

VALIDATE: just harness-validate PASS (rules-check still green — deleting the writers must
not disturb either book). wc -c table: code-review, testing (both <=2 KB), architecture
(4,791 B ± the CP2 line).

PR BODY: mapping table old law -> book file + rule ids, line by line; every protected-law
edit enumerated (architecture CP2, both gate-card strips, each domain locus); stack line
(merge after 5b, cut tag v1-one-law here); the named consumers that break until 5d
(loops graphs + personas at the v1-gan-layers pin — the pin insulates them; nothing breaks
until the pin moves, which is what the tags are for).
```

---

## Brief 5d — loops: neutral graph, disclosure mechanism, personas

```
You are implementing crossr v2 PR 5d in sycamore-hq/crossr-loops.
Precondition: skills tag v1-one-law exists (verify with git ls-remote; state the peeled
SHA in the PR body).

[paste GUARDRAILS]

GOAL: the loop stops naming a language. The graph carries topology; the book is disclosed
per project. This is the decision-#2 half of PR 5.

- lockfile.toml: skills = "v1-one-law" (the loops self-pin line: leave as is).

- graphs/code-gan.json (the 3a park, recorded in the plan):
    generate  node uses.skill: rust-code-writer   -> code-writer
    reviewer  node uses.skill: rust-code-reviewer -> code-review
    tester    node uses.skill: rust-code-tester   -> testing
    architect node: unchanged
    requires.skills: ["code-writer", "code-review", "testing", "architecture"]
    requires.book: true        <-- NEW
  Topology unchanged. NO book name appears in this file. graphs/index.html regenerated
  via ./scripts/verify-graphs --html only.

- graphs/schema.json: `requires` currently has "additionalProperties": false, so
  `requires.book` MUST be added to the schema in this PR or the graph fails validation.
  Add it as {"type": "boolean", "description": "Runs only against a disclosed language
  book; the graph never names one."}.

- scripts/verify-skill-refs — two additions, each a separate commit with its own test
  output:
  1. If a graph declares requires.book: true, FAIL if any uses.skill or requires.skills
     entry resolves to a book skill (a catalog skill directory containing RULES.md).
     This is the mechanical gate that stops the monoculture growing back; it is the only
     thing that will catch a future `generate -> rust` retarget.
  2. Resolve persona Required Skills lines against the catalog. Today verify-skill-refs
     checks graphs only — nothing mechanical catches a stale persona requirement, which
     is why this brief has to enumerate them by hand below.

- PERSONAS (.agents/agents/) — two classes of edit, enumerate each:
  1. Required Skills retargets: reviewer-agent requires rust-code-reviewer -> code-review;
     tester-agent requires rust-code-tester -> testing. Also brick-coder-agent,
     brick-mutator-agent and brick-refactorer-agent, which name the dying writer
     (`brick` itself stays parked per §8 q. 3 — its personas still break without this).
  2. Voice de-Rust (the 2a parked gap): reviewer-agent "Obsessive, ruthless Rust Code
     Quality Guardian" -> drop "Rust"; tester-agent "Obsessive Rust Testing Guardian" ->
     drop "Rust"; sweep architect-agent and both conductor personas. The personas are
     language-neutral roles over a language-specific book; the voice must match the
     architecture now.

- .agents/skills/axel/references/harness-parameters.md §"Language stack (stratified)" —
  THE DISCLOSURE AUTHORITY, and the file v1 of this prompt set never named. Its "Rust
  (default when the repo is Rust / harness says so)" block hardcodes the whole dying
  triple plus rust-errors and the domain skills. Rewrite it book-driven:
    - The harness discloses `books` (from the consumer repo's lockfile.toml) at session
      start.
    - Generator loads: code-writer + <book> (card + the references for the situation) +
      domain skills.
    - Adversaries load: the gate card + <book>/RULES.md. Never <book>/references/.
    - Test verifier: rules tagged `test` in that same RULES.md.
    - No book disclosed -> stop and ask the human (this preserves the existing fail-loud
      rule at axel/SKILL.md:101, now with something mechanical behind it).
  axel/SKILL.md:29 pre-flight step 4 ("State language stack + adversary chain") stays —
  it is now satisfiable from the lockfile instead of from vibes.

- REPO-WIDE SWEEP. v1 of this prompt set told the agent to grep book/src/pipeline/*.md,
  README.md and templates/harness/opencode/command/*.md. Measured: NONE of those contain
  a single hit. The actual referrers of the four dying names are:
      graphs/code-gan.json                                 (above)
      .agents/agents/reviewer-agent.md, tester-agent.md    (above)
      .agents/agents/brick-coder-agent.md, brick-mutator-agent.md,
        brick-refactorer-agent.md                          (above)
      .agents/skills/axel/references/harness-parameters.md (above)
      AGENTS.md                                            (retarget)
      graphs/index.html                                    (generated — regenerate)
      progress.md                                          (history — do not touch)
  Re-run the grep yourself repo-wide (exclude .git, progress.md, MIGRATION) and paste it;
  do not trust this list to still be complete.
  While in the book: the stale scull7/crossr-skills HARNESS-SPEC links (axel.md, avril.md)
  are parked review debt — fix them to
  sycamore-hq/crossr-harness/blob/main/HARNESS-SPEC.md in this pass.

VALIDATE: graphs-verify, verify-protocol and verify-skill-refs all PASS with
CROSSR_SKILLS_PATH pointed at a v1-one-law checkout; paste the output, including a
demonstration that the new requires.book rule fails when you temporarily point a node at
a book. Cut tag v1-one-law-consumers on the merge commit (stack line in the body).
```

---

## Brief 5e — harness: spec, the `books` declaration, smoke, dead site gate

```
You are implementing crossr v2 PR 5e in sycamore-hq/crossr-harness.
Precondition: tags v1-one-law (skills) and v1-one-law-consumers (loops) exist — verify
and state peeled SHAs.

[paste GUARDRAILS]

- lockfile.toml + lockfile.toml.example: skills = "v1-one-law",
  loops = "v1-one-law-consumers". Example comment updated.

- NEW: the per-project book declaration. Add to lockfile.toml.example, with a comment:
      books = ["rust"]     # disclosed language books; ["ocaml"], ["rust","ts"], ...
  This is what makes "load the book when necessary, and necessary is project-dependent"
  mechanical instead of prose. It is a DISCLOSURE filter, not a copy filter:
  scripts/harness-bootstrap copy_skill_dirs copies every skill directory unconditionally
  and that stays true. Document the distinction in HARNESS-SPEC.md so nobody later
  "optimizes" bootstrap into partial copies.

- HARNESS-SPEC.md §6 (the 3b park, recorded in the plan): gate 2 rust-code-reviewer ->
  code-review, gate 3 rust-code-tester -> testing. Gate 4 is already architecture. Sweep
  the whole spec for the five dead names (the four above plus ocaml-code-writer);
  enumerate every edit. Add the book/disclosure model to the spec's GAN section.

- Harness skills (chief-of-staff, dashboard-prompt) + scripts: grep the five dead names,
  retarget any live hit (3b precedent: one-word-class drops, enumerated).

- scripts/verify-docs: the site block is dead code here (guarded on a site/ directory this
  repo does not have — established in the 3b review) and its must-list still requires
  rust-team-lead. Either delete the site block outright (recommended — the site lives in
  crossr-web-landing, which owns its own copy checks) or fix the must-list to the current
  featured set. State which and why. This is the harness half of the "move the allowlist
  and the landing copy together" plan item — cite it; 5g is the landing half.

- test/harness-bootstrap-smoke.sh: pins updated. Add assertions that a fresh target has
  .agents/skills/rust/, .agents/skills/ocaml/, .agents/skills/code-review/ and
  .agents/skills/testing/ — and, more importantly, that it has NO rust-code-writer/,
  rust-errors/, ocaml-code-writer/, rust-code-reviewer/ or rust-code-tester/. The ABSENCE
  assertions are the ones that matter: presence-of-books would have passed during the
  5a/5b staging window too and proved nothing.
  Also assert each book ships a committed RULES.md (bootstrap copies files and never runs
  generators, so an uncommitted projection means consumers get nothing).
  Conductor window unchanged: axel 5,989 + gan-verdict 1,132 = 7,121. Books are
  subagent-side and must NOT appear in the conductor window — assert that too.

VALIDATE: ./test/harness-bootstrap-smoke.sh PASS end-to-end, paste the tail.
```

---

## Brief 5f — skills: closer + plan record

```
You are implementing crossr v2 PR 5f in sycamore-hq/crossr-skills.
Precondition: 5a-5e merged; loops tag v1-one-law-consumers exists.

[paste GUARDRAILS]

- lockfile.toml: loops = "v1-one-law-consumers".
- Deleted/stale check first, then just regen-agents (personas changed in 5d — the
  regenerated .opencode/agent/ files pick up the de-Rusted voice and retargeted required
  skills). Second run: git status clean. No orphan-persona warnings — if 5d's edits left
  stale copies anywhere, delete and rerun.

- PLAN RECORD (docs/plans/gan-layer-separation-plan.md AND its hand-maintained HTML twin
  docs/plans/gan-layer-separation-plan.html — there is no generator for the twin; both
  must be edited and must agree):
  - Mark PR 5 landed with all seven PR links and both tags.
  - §7 row 5, replace the unsatisfiable "one writer skill remains (code-writer)" with:
      "One universal writer skill (code-writer) plus one book per language. Zero
       <lang>-code-writer skills remain — rust-code-writer, rust-errors and
       ocaml-code-writer absorbed. Rules projections generated per book and drift-gated;
       gate cards <=2 KB and book-agnostic; the code-gan graph names no language."
    Record the measured results: N rules per book with stable ids, gate-card bytes,
    reviewer load set (gate card + RULES.md) against the pre-PR reviewer skill at 5,059 B.
  - §2.4 monoculture table: rust and ocaml now both have writer + reviewer + tester +
    architect coverage. That table was the plan's original diagnosis; update it.
  - §8: close open question 3's sibling reasoning where it was applied to OCaml, and
    record the reversal honestly — the pre-dispatch recommendation was to park OCaml; it
    was overruled because a single book cannot demonstrate that the infrastructure is
    language-agnostic, which is the property Elm / TypeScript / JavaScript targets depend
    on. Record 5b's zero-line extractor diff as the evidence that it does.
  - Add the decisions this stack settled that the plan did not previously contain:
    the projection contract vs. per-book topic sets; <book>/RULES.md placement;
    requires.book; the lockfile `books` declaration.
  - Discharge the parked items this stack closed: architecture CP2 (1a), code-gan.json
    (3a), HARNESS-SPEC §6 (3b), persona voice (2a), the harness half of the featured-set
    item (5e). Mark the landing half (5g) as the only remaining piece if it has not
    merged yet.
  - Acceptance condition 1 status note: with the book split and the neutral graph, an
    Elm/Melange run loads code-writer + the axel card + the universal gate cards and does
    not halt; what remains before it can be demonstrated live is an `elm` book and
    books = ["elm"] in that repo's lockfile. State it plainly — the condition is not yet
    demonstrated, only unblocked.
- progress.md + features.json entries per house style.
- VALIDATE: just harness-validate PASS (including rules-check).
```

---

## Brief 5g — web-landing rider (any time after 5c)

```
You are implementing the crossr v2 landing fix in sycamore-hq/crossr-web-landing.
Recorded debt: gan-layer-separation-plan §4 PR 3 landed block ("move the allowlist and
the landing copy together").

- site/templates/index.html:222 — the crossr-loops card says "AVRIL, AXEL, BRICK
  conductor, rust-team-lead. ...". Drop rust-team-lead; if the card lists what loops
  ships, the current truth is "AVRIL, AXEL, BRICK conductor, code-gan graph".
- Sweep the site for the names retired by PR 5 (rust-code-writer, rust-errors,
  ocaml-code-writer, rust-code-reviewer, rust-code-tester) and rust-team-lead; retarget
  or drop each. Where the site describes the catalog, the current truth is
  "code-writer + language books (rust, ocaml) + activity gates (code-review, testing,
  architecture)".
- Do not add new claims. The site links out and owns no law.
- State in the PR body that this is the landing half of the plan item whose harness half
  was 5e (cite both).
```

---

## Review gauntlet (what I will check when each PR comes back)

- **5a**: extractor run twice, byte-identical; --check demonstrated red AND green; every
  rule id unique and <=3 lines; no code-writer / Fines photocopy in any reference; RULES.md
  outside references/; nothing deleted; deprecation markers carry measured bytes; the two
  added topics disclosed as a §3.4 refinement, not slipped in.
- **5b**: `git diff --stat` proves zero lines of scripts/extract-rules — this is the PR's
  entire point; OCaml topic set justified per-topic; no anti-patterns grab-bag; ids
  namespaced `ocaml/`.
- **5c**: mapping table verified line by line against the books; gate cards <=2 KB measured
  AND grep-clean of 'rust'/'ocaml'; CP2 the only architecture edit; all three writers gone
  including Claude copies; acceptance greps re-run in front of me.
- **5d**: code-gan.json names no language; requires.book in schema AND enforced by
  verify-skill-refs, with the failure demonstrated; persona Required Skills greps; voice
  grep for 'Rust' in .agents/agents/; harness-parameters.md Language stack actually
  rewritten (the file v1 forgot); repo-wide grep pasted, not the hand-listed subset.
- **5e**: smoke run locally with the ABSENCE assertions failing on a pre-5c tree; conductor
  window still 7,121; books present with committed RULES.md; verify-docs decision argued;
  the disclosure-vs-copy distinction documented in the spec.
- **5f**: double regen clean; plan twins consistent; §7 row 5 and §2.4 both updated; every
  park discharged or re-parked with a home; the OCaml reversal recorded with its evidence.
- **Throughout**: no delta skills, no hand-copied Rules, no book name in a graph / gate card
  / persona, tags cut where the stack says.
