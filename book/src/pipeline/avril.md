# AVRIL — Planning GAN

**AVRIL** = Automated Visionary Review Iteration Loop.

Skill: `avril` · Personas: `planning-architect-agent`, `product-owner-agent`, `qa-architect-agent`, `visionary-cto-agent`

Normative detail: [HARNESS-SPEC.md §12](https://github.com/scull7/crossr-skills/blob/main/HARNESS-SPEC.md).

## Purpose

Turn product/technical intent into a **unanimously blessed** Product Backlog. Planning-only: **does not implement code**. Hands off to [AXEL](axel.md).

## Loop (fixed order)

1. **Generator** — Planning Architect proposes small, vertical-slice PBIs.
2. **Product Owner** — value, scope, ruthless cuts → `BLESS <id>` or `REJECT <id>`.
3. **QA Architect** — testability, AC completeness, failure modes → `BLESS` / `REJECT`.
4. **Visionary CTO** — strategic fit, two-year trajectory (final gate) → `BLESS` / `REJECT`.
5. Any `REJECT` → minimal revise → **full three-adversary chain again** (prior blessings do not carry).
6. When every active PBI has three fresh `BLESS` marks → **Blessed Backlog Summary** → **stop**.

Advancement requires the exact token `BLESS`. Silence or “LGTM” is not enough.

## Activation

> Using `code-writer` + `avril` to run the Automated Visionary Review Iteration Loop on the current intent until every PBI is triple-blessed.

## Board

Prefer [Pinto](https://github.com/moriturus/pinto) when available (`.pinto/`, `pinto list --json`). Otherwise use the portable PBI shape in the `avril` skill (id, title, why, scope_in/out, acceptance_criteria checkboxes, dependencies).

## Toy example

**Intent:** “CLI todo list with tags.”

Example PBIs (illustrative):

1. Add a todo with a single tag (AC: create, list, tag filter).
2. Mark complete / incomplete (AC: status toggle, list filters).
3. Persist to a local file (AC: restart retains data; corrupt file fails loudly).

Each item needs testable checkbox AC and explicit `scope_out`.

## Output

A Blessed Backlog Summary lists ordered ids, cuts, empty open questions, and the blessing log. Then **stop** — do not start coding under AVRIL.

## Size bar and optional owl-sketch

Split PBIs that cannot be reviewed in a short deep-review pass. Optional **owl-sketch** spikes (“draw the owl”) may explore unknown domains, then massage findings into general PBIs — still requiring full PO → QA → CTO `BLESS` before AXEL. Owl output alone never authorizes execution.

Execution-time mega-diffs use AXEL’s optional [decomposition mode](axel.md#optional-mitchell-decomposition-mode) (default off). Contract: [mitchell-decomposition-contract.html](https://github.com/scull7/crossr-skills/blob/main/docs/plans/mitchell-decomposition-contract.html).
