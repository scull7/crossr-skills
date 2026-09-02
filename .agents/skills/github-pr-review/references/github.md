# GitHub review protocol

Prefer dedicated GitHub tools when the session has them (a GitHub MCP server:
`pull_request_read`, `pull_request_review_write`, `add_comment_to_pending_review`,
…). Otherwise use `gh`. Don't invent a third path — a hand-rolled `curl` differs
in auth and pagination from everything else here, and the failure modes are
yours alone to debug.

Whichever path you use, the shape is the same: draft all comments locally,
validate, create one review, attach every comment, submit once with the event.

Two id spaces, easy to confuse:

- Thread node ids look like `PRRT_kwDO...`. GraphQL and the MCP resolve /
  unresolve tools use these.
- Comment ids are integers (`databaseId` / REST `id`, the number in a
  `#discussion_r...` anchor). REST edit and reply, and the MCP reply tool, use
  these.
- Review ids are also integers, but a different sequence. A review id passed
  where a comment id belongs fails with a bare 404.

## Contents

- [Read the PR](#read-the-pr)
- [Get the head on disk](#get-the-head-on-disk)
- [Diff and line anchoring](#diff-and-line-anchoring)
- [Existing threads](#existing-threads)
- [Your previous reviews](#your-previous-reviews)
- [Draft file](#draft-file)
- [Post the review — gh](#post-the-review--gh)
- [Post the review — MCP tools](#post-the-review--mcp-tools)
- [Backfill cluster permalinks](#backfill-cluster-permalinks)
- [Re-review operations](#re-review-operations)
- [Recovering from a failed post](#recovering-from-a-failed-post)

## Read the PR

```bash
gh pr view <n> --repo OWNER/REPO \
  --json url,title,body,baseRefName,headRefName,headRefOid,reviewDecision,statusCheckRollup,closingIssuesReferences
gh api user --jq .login     # who you are, for finding your own prior reviews
```

Record `headRefOid` and the base sha. Every comment you post should be against
that head commit (`commit_id` in the review body); if the head moves while you
are drafting, your line numbers may no longer mean what you think, so re-fetch
the diff before posting.

MCP equivalents: `pull_request_read` with `method: "get"` (head/base refs and
shas, `mergeable_state`), `"get_diff"`, `"get_files"`, `"get_commits"`,
`"get_check_runs"` (CI on the head), `"get_reviews"`, `"get_review_comments"`
(threads, paginated with `perPage` / `after`). `get_me` for your login.

MCP tool names vary between server versions. Older servers expose
`create_pending_pull_request_review` / `submit_pending_pull_request_review` /
`delete_pending_pull_request_review` as separate tools; newer ones fold them
into `pull_request_review_write` with a `method` field. Look at what the
session actually has before assuming either.

## Get the head on disk

```bash
gh pr checkout <n>                      # in your own clone
```

Without `gh`, or when the clone is shared with something else that must stay
on its branch:

```bash
git fetch origin <headRefName>
git worktree add /tmp/pr-<n> origin/<headRefName>     # detached, disposable
# ... verify in /tmp/pr-<n> ...
git worktree remove --force /tmp/pr-<n>
```

A worktree gives you the head without touching the checkout you were handed.
Remove it when you are done; a stray worktree pins its branch and confuses the
next `git status`.

## Diff and line anchoring

```bash
gh pr diff <n> --repo OWNER/REPO > /tmp/pr.diff
# or, in a clone with both refs fetched — three dots, from the merge base:
git diff <base-sha>...<headRefOid> > /tmp/pr.diff
```

Use the PR's own base sha (or `gh pr diff`), not a local `main` that may be
behind or ahead. A stale base puts files in the diff that the PR did not
touch, and then the anchor check passes comments GitHub will reject.

A review comment is anchored to a `path` plus a `line` on one `side` of the
diff. The rules GitHub enforces:

- `side: RIGHT` + `line` — a line as it appears in the new file. It must be an
  added or context line inside a hunk. This is what you want almost always.
- `side: LEFT` + `line` — a line in the old file, for commenting on a deletion.
- Multi-line: add `start_line` (and `start_side`, same as `side`). `start_line`
  must be < `line` and both must be inside the same hunk.
- A line the diff doesn't touch (not in any hunk) is rejected with a 422
  `pull_request_review_thread.line must be part of the diff`, and that 422
  fails the **entire** review call. This is the single most common posting
  failure. Validate before posting.
- `position` (offset into the diff) is the legacy API. Don't use it; it is
  fragile across pushes and the MCP tools don't speak it.

`scripts/validate_review.py` parses the diff and checks every comment in the
draft file against these rules, plus the first-line grammar, the event, and the
count cap. Run it before posting; it is much cheaper than a rejected review.

```bash
python <skill-path>/scripts/validate_review.py /tmp/review.json /tmp/pr.diff
# add --self-review when you are the PR author (a zero-finding COMMENT is then valid)
```

## Existing threads

MCP: `pull_request_read` with `method: "get_review_comments"`, `perPage: 100`,
and pass back `pageInfo.endCursor` as `after` while `hasNextPage` is true.
Each thread carries `id` (the `PRRT_...` node id), `isResolved`, `isOutdated`,
`path`, `line`, and its comments with their numeric ids and authors.

`gh`:

```bash
gh api graphql -f query='
query($owner:String!,$repo:String!,$n:Int!,$after:String) {
  repository(owner:$owner, name:$repo) {
    pullRequest(number:$n) {
      reviewThreads(first:100, after:$after) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          isResolved
          isOutdated
          path
          line
          startLine
          comments(first:20) {
            nodes { databaseId body author { login } createdAt url }
          }
        }
      }
    }
  }
}' -F owner=OWNER -F repo=REPO -F n=NUMBER
```

Build the inventory before drafting so the duplicate check has something to
check against, and **fetch it again immediately before you submit**. The gap
between the two is where another reviewer lands.

`isOutdated` means the anchored line moved in a later push, not that the issue
is gone.

Comment bodies read back through some tool paths have `<...>` tokens stripped
and HTML escaped; the text on GitHub is intact. Some MCP servers also append an
attribution footer to every body you post. Neither is reviewer text; ignore
both when reading threads.

## Your previous reviews

MCP: `pull_request_read` with `method: "get_reviews"`; keep the ones whose
`user.login` is you and whose `state` is not `PENDING`.

```bash
gh api repos/OWNER/REPO/pulls/NUMBER/reviews --paginate \
  --jq '.[] | select(.user.login=="YOUR_LOGIN") | {id, state, commit_id, submitted_at}'
```

A non-empty result means re-review mode. Take the `commit_id` of the latest
submitted one as the point to diff from:

```bash
git diff <commit_id>..HEAD                       # in the checked-out tree
gh api repos/OWNER/REPO/compare/<commit_id>...<headRefOid>   # without a tree
```

If `<commit_id>` is no longer an ancestor of HEAD (the branch was rebased or
force-pushed), the incremental diff is meaningless. Fall back to the full diff
and say so in the report; the thread positions will mostly show `isOutdated`.

Replies posted through the REST reply endpoint or the MCP reply tool show up
in this list as extra reviews with an empty body and state `COMMENTED`. They
are shells, not passes; skip them when looking for your last real review.

A review with state `PENDING` in that list is one that was never submitted.
If you created it in this session, delete it before posting a new one (see
[Recovering from a failed post](#recovering-from-a-failed-post)). If you did
not, it belongs to another session on this account that is mid-post; leave it
and wait, or stop and say so.

## Draft file

Write every comment into one JSON file before touching the API. This is the
exact body the REST endpoint takes, so the validated file is what gets posted.

```json
{
  "commit_id": "<headRefOid>",
  "event": "REQUEST_CHANGES",
  "body": "One blocker in the port parser; two should-fix in error mapping.",
  "comments": [
    {
      "path": "src/net/parse.rs",
      "line": 42,
      "side": "RIGHT",
      "body": "blocker Port above 65535 is accepted\n\nIssue: ...\nWhy it matters: bug — ...\nSuggested fix: ...\nDone when: ..."
    },
    {
      "path": "src/net/parse.rs",
      "start_line": 55,
      "line": 61,
      "side": "RIGHT",
      "start_side": "RIGHT",
      "body": "should-fix [parse-errors] ..."
    }
  ]
}
```

`event` is one of `APPROVE`, `REQUEST_CHANGES`, `COMMENT`. Omitting it creates
a *pending* review that nobody can see — fine as a first step, wrong as a
final state. `body` is the review summary: one or two sentences, no findings
(those are all in `comments`). An `APPROVE` may have an empty `comments`
array; a `REQUEST_CHANGES` must have at least one `blocker` in it. When you
are the PR author, GitHub refuses `APPROVE`; a zero-finding self-review is a
`COMMENT` with the same one-sentence body.

## Post the review — gh

One call, everything attached, submitted:

```bash
gh api -X POST repos/OWNER/REPO/pulls/NUMBER/reviews --input /tmp/review.json
```

The response includes the review `id`. If the call fails, nothing was posted
(the endpoint is atomic for this shape) — fix the offending comment and retry
the whole file.

`gh pr review <n> --approve --body "..."` is fine for a zero-finding APPROVE
with no comments. It cannot attach inline comments, so don't reach for it
otherwise.

## Post the review — MCP tools

Same shape in three steps; keep the drafted file as the source of truth so the
comments are identical to what you validated.

1. Create the pending review: `pull_request_review_write` with
   `method: "create"`, no `event`, `commitID: <headRefOid>` (older servers:
   `create_pending_pull_request_review`, `commitId`).
2. `add_comment_to_pending_review` once per comment — `path`, `line`, `side`,
   `body`, `subjectType: "LINE"`, plus `startLine` / `startSide` for a range.
3. Submit: `pull_request_review_write` with `method: "submit_pending"`,
   `event`, `body` (older: `submit_pending_pull_request_review`).

`submit_pending` returns a success string, not the review. To get the review
id and comment permalinks (for the report, or the backfill), call
`pull_request_read` `get_reviews` and `get_review_comments` afterwards.

If step 2 fails on a comment, the pending review is left with the earlier
comments attached. Either fix and continue (the pending review is still
there), or delete it (`method: "delete_pending"`) and start over. Don't submit
a partial batch; the event would be computed from findings that aren't all
there.

`pull_request_review_write` with `method: "create"` **and** an `event` (body,
no inline comments) is the MCP equivalent of `gh pr review` — zero-finding
reviews only.

## Backfill cluster permalinks

Anchor comments list their children as `path:line` at draft time because the
children don't have URLs yet. After the review is posted, with `gh`:

```bash
# comments of the review you just created, with their permalinks
gh api repos/OWNER/REPO/pulls/NUMBER/reviews/REVIEW_ID/comments \
  --jq '.[] | {id, path, line, html_url, first: (.body | split("\n")[0])}'

# rewrite the anchor body with links substituted for path:line
gh api -X PATCH repos/OWNER/REPO/pulls/comments/ANCHOR_COMMENT_ID \
  -f body="$(cat /tmp/anchor-with-links.md)"
```

Match children to the anchor by the `[slug]` in their first line. Editing the
body does not re-notify anyone, so this is safe to do after submit. The MCP
servers seen so far have no tool for editing a review comment; on that path
the `path:line` list stands, and that is fine — the fixer can find a line.

## Re-review operations

Reply on a thread. MCP: `add_reply_to_pull_request_comment` with the numeric
id of the thread's first comment (`commentId`) and `body`. `gh` (GraphQL, takes
the thread id, lands in the thread):

```bash
gh api graphql -f query='
mutation($threadId:ID!,$body:String!) {
  addPullRequestReviewThreadReply(input:{
    pullRequestReviewThreadId:$threadId, body:$body
  }) { comment { id } }
}' -F threadId=PRRT_... -F body='...'
```

The REST / MCP reply creates an implicit one-comment review around the reply.
Two consequences: it fails while you have a pending review open ("one pending
review per pull request"), so do replies before creating the pending review;
and it shows up in `get_reviews` as an empty `COMMENTED` shell, which is
harmless but not a pass.

Unresolve a thread whose `Done when` does not hold on HEAD (reply first, so the
reader knows why it reopened). MCP: `pull_request_review_write` with
`method: "unresolve_thread"` and `threadId: PRRT_...` (or the standalone
`unresolve_review_thread` tool). `gh`:

```bash
gh api graphql -f query='
mutation($threadId:ID!) {
  unresolveReviewThread(input:{threadId:$threadId}) { thread { isResolved } }
}' -F threadId=PRRT_...
```

Resolve one of your own threads that the author's reply or push has satisfied.
MCP: `method: "resolve_thread"` (or `resolve_review_thread`). `gh`:

```bash
gh api graphql -f query='
mutation($threadId:ID!) {
  resolveReviewThread(input:{threadId:$threadId}) { thread { isResolved } }
}' -F threadId=PRRT_...
```

Replies and (un)resolves are per-thread operations outside the new review.
Do them first, then post the new review for the new findings; the review's
event should reflect the thread state after your unresolves.

## Recovering from a failed post

A pending review of yours that was never submitted blocks a new one on some
paths and confuses every reader who can see it in the UI.

```bash
gh api repos/OWNER/REPO/pulls/NUMBER/reviews --jq '.[] | select(.state=="PENDING") | .id'
gh api -X DELETE repos/OWNER/REPO/pulls/NUMBER/reviews/REVIEW_ID
```

MCP: `pull_request_review_write` with `method: "delete_pending"`.

Only pending reviews can be deleted, and only delete one you created in this
session. A submitted review with a wrong event can't be retracted; if you
approved something you shouldn't have, post a follow-up `REQUEST_CHANGES` with
the blocker and say in its body that it supersedes the earlier approval. A
wrong or duplicate comment of your own gets a one-line reply and a resolve.
Don't dismiss reviews — that is an action for a maintainer, not a reviewer
correcting itself.
