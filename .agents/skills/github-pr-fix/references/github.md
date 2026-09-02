# GitHub thread protocol

Prefer dedicated GitHub tools when the session has them (`pull_request_read` /
`get_review_comments`, reply, `resolve_thread`). Otherwise use `gh`. Don't
invent a third path — a hand-rolled `curl` against the API will differ in auth
and pagination from everything else here.

Two id spaces, easy to confuse:

- Thread node ids look like `PRRT_kwDO...`. GraphQL uses these.
- Comment ids are integers (`databaseId`). REST replies use these.

Passing one where the other belongs fails with an unhelpful error, so check
which you're holding before the call.

## Checkout and head state

```bash
gh pr checkout <number>
gh pr view <number> --json url,title,headRefName,headRefOid,reviewDecision,body
```

Record `headRefOid` before you start. Comparing it again before you push tells
you whether the head moved under you.

## List threads

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
          comments(first:20) {
            nodes { databaseId body author { login } createdAt }
          }
        }
      }
    }
  }
}' -F owner=OWNER -F repo=REPO -F n=NUMBER
```

When `hasNextPage` is true, pass `endCursor` back as `-F after=...` and keep
going until every thread is in the inventory.

`isOutdated` means the line moved, not that the issue is gone. Read the thread
and locate the code at its new position rather than skipping it.

## Reply

GraphQL, preferred — takes the thread id, so the reply lands on the thread
rather than starting a new one:

```bash
gh api graphql -f query='
mutation($threadId:ID!,$body:String!) {
  addPullRequestReviewThreadReply(input:{
    pullRequestReviewThreadId:$threadId,
    body:$body
  }) { comment { id } }
}' -F threadId=PRRT_... -F body='...'
```

REST fallback — takes the first comment's numeric `databaseId`:

```bash
gh api -X POST repos/OWNER/REPO/pulls/NUMBER/comments/COMMENT_ID/replies \
  -f body='...'
```

## Resolve

Only after the fix commit is on the remote PR head. Resolving first and pushing
second leaves a window where the thread claims something the branch doesn't
show, and if the push then fails the claim is simply false.

```bash
gh api graphql -f query='
mutation($threadId:ID!) {
  resolveReviewThread(input:{threadId:$threadId}) {
    thread { isResolved }
  }
}' -F threadId=PRRT_...
```

If a `resolve_thread` tool is available, use it with the same `PRRT_...` id.

Reply on a thread before resolving it. A thread that goes from open to resolved
with no reply tells the reviewer nothing about what happened.

Never resolve a skipped nit, a `q`, or a `should-fix` you argued against.
