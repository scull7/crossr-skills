---
name: dashboard-prompt
description: |
  Generates a project-tailored status dashboard for any project: the tracker config that makes the dashboard read that project's real sources correctly, plus the machine-facing refresh contract the working agent follows.
  Detects the project's actual trackers and status vocabulary, proves the classification against live data before emitting anything, and fills `assets/dashboard-contract-template.md` with verified facts.
  Use when a project needs a status view and its tracker is not already covered, or when an existing dashboard reports counts that contradict the board.
  Harness-layer generator skill with clean stratified disclosure. Always activate together with `code-writer`.
---

# Dashboard Prompt Generator

**You are wiring a status view to a project's real sources, not inventing one.** Your deliverables are a tracker config, a refresh contract, and evidence that the two agree with what the board actually says. You do not run the project's work, move its tickets, or edit its trackers.

Before generating, the invoking agent **MUST** also apply `code-writer`.

## Harness Context (Stratified Disclosure)

This is a harness-layer generator skill. It produces artifacts for a dashboard generator that renders **completed / in progress / todo** from a project's own tracking sources.

The reference implementation is `scripts/status-dashboard` with an optional `dashboard.config.json`, but the skill is not bound to it: the concrete generator command, config path, and source names are parameters disclosed by the invoking harness. What is fixed is the contract — sources are read-only, the view never becomes the record, classification is proven against live data rather than assumed, and a dashboard that cannot be refreshed is declared stale rather than left to rot.

The output is read by the working agent, not by a human. Write it as instructions, not as documentation.

## The failure this exists to prevent

A dashboard whose status vocabulary does not match its tracker's classifies every unfamiliar word as todo. It reports `0 in progress` during active work, without erroring. Nobody notices, because a confident dashboard looks the same as a correct one.

So the central job of this skill is not writing prose. It is **proving the mapping against live data before shipping it.**

## Inputs

| Input | Source (in priority order) | If absent |
|-------|----------------------------|-----------|
| `PROJECT_NAME`, `REPO` | human → git root | unresolved question |
| Board | `pinto`, `gh project`, `jira`, `linear`, or any CLI emitting JSON | record "none"; features/tracking file becomes the only source |
| Tracking file | `features.json` or the project's equivalent | record "none" |
| Narrative log | `progress.md` or equivalent | record "none" |
| Status vocabulary | **the literal strings the board emits**, collected from live output | ask; never assume the defaults fit |
| `REFRESH`, `PUBLISH` | justfile / scripts | install the reference generator, or state the project has none |
| Checkpoints | the project's real state transitions (board moves, review gates, merges) | derive from its workflow; never ship the generic list |
| Commit boundary | project convention for committing generated files | phase or ticket boundary |

## Procedure (Exact Flow)

1. **Inventory the trackers.** Find every source that knows about work state. Run each read command yourself and look at the output. Do not infer a tracker's shape from its name.
2. **Collect the literal status vocabulary.** Extract the distinct status strings the board and tracking file actually emit, with counts. This is a fact-finding step with a command behind it, not a guess.
3. **Map each observed string** to done, active, or todo. Every string gets a decision. An unmapped string silently becomes todo, so an unreviewed vocabulary is an unfinished job.
4. **Write the config** (`dashboard.config.json` or the harness's equivalent): status map, board command as an argv list, items path, field names, source filenames. Omit any key whose default already fits.
5. **Prove it.** Run the generator with the config and compare its counts against the board's own totals for the same states. They must match. If they do not, the mapping is wrong — fix it and run again. Record the comparison; it is the evidence for this work.
6. **Fill the contract** from `assets/dashboard-contract-template.md`: resolve every `{{…}}`, derive checkpoints from the project's real transitions, and record any vocabulary gotcha you hit in step 3.
7. **Verify mechanically:** the contract has zero `{{` remaining; every source line names a real command or says "none"; the checkpoint list is project-specific; the proof from step 5 is attached.
8. **Close** with `## Unresolved questions` (may be empty) and the counts the dashboard currently reports.

## Examples

A project whose board is GitHub Projects and whose tracking file uses its own words.

Step 2 collected the literal strings, with counts, by running the board command:

```
gh project item-list 42 --format json
  'Todo'        x7
  'In Review'   x2
  'Done'        x11
  'Icebox'      x3
```

Every string gets a decision. `Icebox` is not in flight and not finished, so it stays
todo by omission, and that omission is deliberate rather than accidental:

```json
{
  "status_map": {
    "done":   ["Done", "Released"],
    "active": ["In Review", "In Progress"]
  },
  "board": {
    "command": ["gh", "project", "item-list", "42", "--format", "json"],
    "items_path": "items",
    "fields": { "id": "id", "title": "content.title", "status": "status" }
  }
}
```

Step 5 is what makes it shippable:

```
board says:      Done=11   not-Done=12
dashboard says:  ✔ completed 11   ▶ in progress 2   ○ todo 10
reconciles: 11 == 11, and 2 + 10 == 12
```

The contract then names those commands and that vocabulary, so the working agent
never has to rediscover them.

A project with no board at all is a valid outcome, not a failure: record `Board: none`,
let the tracking file carry the counts, and say so in the contract rather than
inventing a source.

## Boundaries

- **Generate and prove only.** Never move a ticket, edit a tracker, or change project state to make the dashboard look better.
- **No invented sources.** Every command in the config was run and produced the output you say it did.
- **Never ship an unproven mapping.** Step 5 is not optional. A config that has not been compared against live board totals is a guess with a filename.
- **The view never becomes the record.** If the dashboard and the board disagree, report it; do not reconcile it by editing either.
- **Fail loud.** No board, an ambiguous vocabulary, or counts that will not reconcile go in the unresolved list, not smoothed over.
- **Idempotent.** Re-running on an unchanged project reproduces the same config and contract, and re-running after the tracker changes updates them in place. Never append a second config or leave a stale one beside a new one.
- **The config names a program that will be executed.** It is data, not a script: the board command is an argv list run without a shell, so it cannot carry shell syntax. It still names an executable, so treat the config with the same trust as a build file, keep it in the repo, and never point it at a command taking input from outside the project.

## Failure modes

| Situation | What to do |
|---|---|
| No machine-readable source of work state | Record `Board: none`, say the project has no dashboard-able state yet, and stop. Do not create a tracker to fill the gap. |
| Board command exists but returns no JSON | Report the raw output. A tracker that cannot be parsed is an unresolved question, not a reason to fall back to defaults. |
| A status string's meaning is genuinely ambiguous (`Blocked`, `On Hold`) | Ask. Blocked-as-active and blocked-as-todo are both defensible, and the choice changes what the dashboard tells people. |
| Counts will not reconcile after fixing the map | Stop and report both numbers. An unreconciled dashboard is the failure this skill exists to prevent; do not ship it with a caveat. |
| The project already has a working config | Verify it still reconciles, and say so. Rewriting a correct config is churn. |

## Verification

In a fresh activation the following six behaviors are directly observable and scorable:

- The agent recites the One-Sentence Mandate verbatim before touching any project file.
- The agent runs each candidate source command and shows its real output before writing any config, rather than inferring shape from the tracker's name.
- The agent lists the distinct status strings the project actually emits, with counts, and assigns every one of them to done, active, or todo.
- The agent runs the generator with the config and shows the count comparison against the board's own totals; a mismatch is fixed and re-run, never explained away.
- The emitted contract contains zero `{{` sequences, names only commands that were executed, and carries checkpoints tied to that project's real state transitions rather than the template's generic list.
- The agent changes no project state: no ticket moves, no tracker edits, no commits beyond the config, the contract, and the generator it installed.

Violations against any of these observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.

## Specialization

This skill is the dashboard-wiring specialization of the harness layer (precondition: `code-writer` active; a project with at least one machine-readable source of work state). It supplies the tracker inventory, the vocabulary-mapping discipline, the prove-against-live-data gate, and the machine-facing contract template, while preserving every principle of the base (postcondition: a config whose counts provably match the board, and a contract the working agent can follow without further explanation).

It composes with the orchestration skills rather than replacing them. `avril`, `axel`, and `rust-team-lead` already know *when* to refresh a dashboard; this skill makes sure the thing they refresh is telling the truth about that project.

It carries no dashboard-refresh duty of its own, for the same reason `orchestrator-prompt` does not: both are generators that finish in one pass rather than conductors running work over time. The duty belongs in what they emit, and here that is the contract itself.

## One-Sentence Mandate (Memorize This)

> "Wire the dashboard to the project's real sources, prove the counts against the board before shipping, and never let a view claim something the record does not."

---

This skill is the canonical authority on tailoring a status dashboard to a project's own trackers.

**When using this skill**: Always combine with `code-writer`. Inventory first, map second, prove third, write fourth. You are wiring and verifying — **NEVER** running the project's work or editing its trackers.

**Activation Statement**
> Using `code-writer` + `dashboard-prompt` to wire a proven status dashboard and refresh contract for `<project>`.

Apply this skill **mercilessly** whenever a dashboard's numbers must be trusted.
