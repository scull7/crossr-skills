---
name: "github-pr-review"
description: "Reviews GitHub pull requests with structured inline comments. Use when the user asks to review a PR, provides a PR link for review, or asks for code review feedback on a pull request."
---

# PR Review

Review the PR provided by the user.

## Context gathering
Read the PR body, linked issue, the diff, existing review threads, and
CONTEXT.md / docs/adr/ if they exist. Review changed lines and lines
directly impacted by the change. Not the rest of the repo.

## Output
- ALL feedback is an inline comment on a specific line or range. No
  conversation-tab essays.
- Each comment is atomic: one issue, one fix. An implementing agent should
  be able to address it and mark it resolved on its own.
- Comment shape:
  `<blocker|should-fix|nit|q> [<cluster>] <one-line problem>`

  Issue: <what's wrong, 1-2 sentences>
  Why it matters: <bug | security | compat | perf | maintainability>
  Suggested fix: <concrete change; use a GitHub suggestion block when the
  edit is local>
  Done when: <observable condition>
- Severity:
  - blocker: wrong, unsafe, contract break, or contradicts an ADR. Must fix.
  - should-fix: real defect or design miss. Fix unless you have a better
    argument.
  - nit: optional, including "fine now, risky later." Implementation agent
    skips nits unless asked. Never block on a nit.
  - q: question. Do not change code until a human answers.

## Architectural / cross-cutting
- Pick a short cluster slug (`parse-errors`, `authz-layer`).
- Post one anchor comment on the most relevant entry point (the main
  changed file, type, or function).
- Post related comments on their specific lines with the same slug.
- Anchor lists children as `path:line` (backfill permalinks if the API
  returns them). Children point at the slug and state only the local edit.
  Do not paste the whole design into every child.

## Scope, in this order
1. Correctness and bugs (logic, edge cases, races)
2. Security (validation, injection, auth, secrets)
3. API / contract changes and backward compatibility
4. Error handling and observability
5. Performance, only where it plausibly matters
6. Readability and maintainability
7. Test coverage for changed behavior

## Rules
- Don't restate the diff. Don't post praise-only comments. Every comment
  must be actionable.
- Don't re-litigate accepted ADRs. Don't comment on fmt/clippy/linter
  noise, lockfiles, generated files, or style the tools already own.
- Don't duplicate an open thread on the same line for the same issue. On a
  re-review, only flag new defects or "resolved" threads that were not
  actually fixed.
- If you are guessing, do not post. If you find zero issues, say so and
  submit APPROVE. Do not invent nits.
- Any `blocker` → REQUEST_CHANGES. Zero issues → APPROVE with one sentence.
  Otherwise COMMENT.
- Cap: more than 15 comments means drop the nits and collapse the rest.