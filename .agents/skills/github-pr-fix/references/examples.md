# Reply shapes

Replies are addressed to the next reviewer, who wants to know what changed and
how to check it. Two or three lines. The code is the argument; the reply is the
pointer to it.

## Fixed

```
Done in <sha>.

Done when: no parse path returns String or anyhow for a parse failure.
```

## Fixed, condition restated (thread had no `Done when`)

```
Done in <sha>. Extracted the retry loop into `RetryPolicy::run`.

Checked by: `client.rs` has no remaining inline retry counters.
```

State the condition explicitly here, because you are about to resolve on it and
nobody else wrote it down.

## Already satisfied

```
Already true as of <sha>. No further change.

Done when: this arm returns ParseError.
```

## Declined should-fix

```
Leaving this open.

The suggested enum collapses two failure modes the HTTP layer still needs to
distinguish when mapping to status codes. Prefer keeping the current type until
that mapping exists.
```

Leave it open. Someone with commit authority closes an argument, not you.

## Answering a `q`

```
The budget is 3 because the upstream gateway retries twice itself; more than
that and a single client request can fan out past the rate limit.

No code change.
```

Leave it open. The person who asked decides whether the answer is enough.

## Cluster child

```
Done in <sha> as part of [parse-errors].
```

Resolve children only once the anchor's `Done when` holds, then the anchor.

## Blocked

```
Not done. The change needs `ParseError` to carry the source span, and the span
type is added in #482. Leaving this open until that lands.
```

## Do not write

- "Thanks for the review!" — the thread is a work item, not correspondence.
- A restatement of the reviewer's own comment back at them.
- A second proposed fix. If you fixed it, the diff is the proposal.
- An apology, or a summary of everything else you changed in the PR.
