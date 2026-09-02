---
name: github-pr-fix
description: "Applies open GitHub pull request review feedback to the code: implements the changes, pushes to the PR branch, replies on each thread, and resolves the ones genuinely satisfied. Use whenever the user wants review comments acted on rather than explained — 'fix the PR', 'address/apply/implement the review comments', 'do what the reviewer asked', 'clear my unresolved threads', 'reply on each thread and close them out', 'resolve the ones you fixed' — including when all they give is a PR reference (URL, owner/repo#N, 'pr 58', '#91') plus any intent to change code, push, or clear threads. Also covers `/fix-pr`, re-review passes where a reviewer reopened threads a previous push did not actually fix, clusters of related comments sharing a slug, and threads already satisfied that just need a reply and a resolve. Works on plain human review prose as well as tagged comments. Not for producing new review feedback (use github-pr-review), summarizing a diff, opening a PR, or code changes with no PR review behind them."
metadata:
  author: scull7
  short-description: Implement PR review comments and resolve the threads
---

# Fix PR

Read the open inline review threads on a pull request, apply the ones you are
allowed to touch, push to the PR head, then resolve only the threads whose
outcome a reader could verify on the new HEAD.

Resolving a thread is a claim: it tells the next reviewer *this is handled, you
don't need to read it again*. That claim is only worth anything if it is true
and checkable. An open thread costs a reviewer thirty seconds. A falsely
resolved one costs them the bug. Most of the discipline below is about not
resolving things, for that reason.

The job is not done when you have described a fix in chat. It is done when the
commit is on the PR head branch on the remote, each addressed thread has a
reply, the satisfied threads are resolved, and the working tree is clean.

## Reading the threads

Threads written by `github-pr-review` start with a machine-readable first line:

```
<blocker|should-fix|nit|q> [<cluster-slug>] <one-line problem>

Issue: ...
Why it matters: ...
Suggested fix: ...
Done when: <observable condition>
```

Both bracketed parts are optional. Human reviewers write prose and use neither,
which is the common case — see *Untagged threads* below.

Read every open inline thread before changing anything. Resolved threads are
context, not work: read them so you don't undo a fix someone already agreed to,
then leave them alone. Skip conversation-tab essays; they are not anchored to
code and there is nothing to resolve.

## Severity law

- **blocker** — must fix. Resolve only once `Done when` holds on HEAD.
- **should-fix** — fix unless you have a genuinely better argument. If you do,
  reply with the argument and leave the thread open. Disagreement is a
  conversation for a human to close, not something you can resolve away.
- **nit** — skip, unless the user asked for nits. Don't reply, don't resolve;
  list them in the report so the user can ask for them in a second pass. A nit
  you silently fix is unreviewed code the reviewer never asked for.
- **q** — a question is not a fix. Answer it in a reply if you can answer it
  honestly; change no code and leave it open for the human who asked.

## Untagged threads

Most PRs are reviewed by people who never heard of the severity grammar. Do not
refuse to work on those, and do not invent tags in your reply. Classify by what
the comment is asking for:

- Asks for a specific change → treat as `should-fix`.
- Asks a question, or says "why" / "did you consider" → treat as `q`.
- Praise, or an observation with no ask → ignore, no reply, no resolve.
- Genuinely ambiguous → treat as `q` and ask. Guessing wrong here means writing
  code nobody wanted and then resolving the thread that would have caught it.

State the classification you used in the report so the user can correct you.

## `Done when` is the acceptance test

`Done when` is the condition you have to make true. `Suggested fix` is a hint —
prefer it when it still applies to the code as it stands, but you are not bound
to it if it no longer fits. Satisfy the condition either way.

If a thread has no `Done when`, write the condition you used into your reply
before you resolve, and only resolve if that condition is something the next
reader can check on HEAD. "I made it cleaner" is not checkable. "`parse_port`
now returns `ParseError` on every failure path" is.

Some open threads are already satisfied — the author fixed it in a later commit,
or the reviewer read a stale diff. Write no code. Reply that the condition
already holds, name the commit where it became true, and resolve.

## Clusters

Threads sharing a `[slug]` are one change split across files, not four separate
tasks. The anchor is the structural change; the children are the local edits
that carry it out.

1. Read the anchor first, and the whole cluster, before editing anything.
2. Make the structural change, then the child edits.
3. Resolve nothing in the cluster until the anchor's `Done when` holds.
4. Then resolve the children, then the anchor.
5. If one child can't be finished, leave the entire cluster open and say why in
   the report. A half-applied structural change with three resolved threads is
   the worst possible state to hand back — it looks finished and isn't.

## Workflow

1. Parse `owner`, `repo`, and the number from the URL or `owner/repo#n`.
2. Read the PR body, head branch, and all review threads. Commands and API
   shapes are in [references/github.md](references/github.md). Paginate until
   every thread is in the inventory — a plan built on the first page silently
   drops work.
3. `gh pr checkout <n>`. Work on the PR head branch. Don't invent a side branch;
   the fix has to land where the review is.
4. Inventory the open inline threads: id, severity, cluster, path, `Done when`.
5. Plan in this order — `blocker` clusters, remaining `blocker`s, `should-fix`
   clusters, remaining `should-fix`s. Then stop. No nits, no `q`, nothing
   outside those threads.
6. Apply the changes. No drive-by refactors, no new dependencies, no formatter
   or lockfile churn nobody asked for. Every hunk in the diff should be
   traceable to a thread.
7. Check each touched thread's `Done when` against the working tree. If one
   doesn't hold, it isn't fixed — go back or drop it from the resolve list.
8. Run the repo's checks (below).
9. Commit the review fixes. Push to the PR head branch. If the push is rejected
   because the head moved, `git pull --ff-only` and re-run the checks; if that
   fails too, stop and report. Don't force-push unless the user said to — the
   reviewer's line anchors live on those commits.
10. Reply on each addressed thread, then resolve the ones that earned it.
    Reply shapes are in [references/examples.md](references/examples.md).
11. Clean up, then report.

If there is nothing to do — every open thread is a nit, a `q`, or already
satisfied — that is a valid outcome. Don't manufacture a commit to look busy.

## Running the repo's checks

Run what the repo actually uses, not what you would guess from the file
extensions. Look in this order: `AGENT.md` / `CONTRIBUTING.md` for named
commands, a `Makefile` target (`check`, `lint`, `test`), the CI workflow's
steps, then the ecosystem default. Run the narrowest check that covers your
change first, then widen.

Ecosystem defaults when nothing in the repo says otherwise:

| | |
|---|---|
| Rust | `cargo fmt --check && cargo clippy --all-targets --all-features -- -D warnings && cargo test` |
| Node / TS | the `lint`, `typecheck`, and `test` scripts in `package.json` |
| Python | the configured formatter and linter, then `pytest` |
| Go | `gofmt -l . && go vet ./... && go test ./...` |

You own the failures your change introduced. A check that was already red on the
base commit is not yours to fix in this pass — note it in the report and leave
it. Widening scope to turn an unrelated check green is how a three-line review
fix becomes an unreviewable diff.

If a check can't run at all (toolchain missing, no network), say exactly which
one and why in the report. Don't quietly skip it and let the reply imply it
passed.

## Cleanup

Neither the tree nor the PR should show that an agent thrashed here.

- Working tree clean after the push. No stash, no leftover worktree, no scratch
  files, no `.orig` or `.rej`.
- No debug prints, commented-out code, or TODOs the threads didn't ask for.
- No pending GitHub review left in draft state.
- Delete any temp files or worktrees you created.

## Report

A short table in chat, nothing else. No narrative, no restating the diff.

| Thread | Severity | Cluster | Action | SHA | Resolved |
|---|---|---|---|---|---|

`Action` is one of: `fixed`, `already done`, `skipped nit`, `left open: q`,
`left open: argued`, `left open: blocked`. Follow the table with one line only
if something needs a human: a check you couldn't run, a cluster you left open,
or a classification you're unsure about.

## Do not

- Invent work no thread asked for.
- Re-litigate an accepted ADR or a decision the PR body says is settled.
- "Fix" a `q`.
- Take nits unless asked.
- Resolve a thread whose condition you cannot point at on HEAD.
- Resolve anything before the commit is on the remote PR head.
- Resolve a thread you argued against, or one you only half-fixed.
- Force-push, unless the user told you to.
