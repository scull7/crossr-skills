# Comment shapes

The reader of each comment is someone who will fix it without asking you a
follow-up question. Evidence in the Issue line, consequence in the Why line, a
concrete edit in the Suggested fix, and a condition they can check in Done when.

## blocker, with a suggestion block

Anchored on the single line the fix replaces.

````
blocker Port above 65535 is accepted

Issue: `parse_port` only checks `s.parse::<u32>()` succeeded; `parse_port("70000")` returns `Ok(70000)` (confirmed with `cargo test port_range` after adding the case).
Why it matters: bug — `Listener::bind` later truncates to u16 and binds port 4464 silently.
Suggested fix:
```suggestion
    let port = s.parse::<u16>().map_err(|_| ParseError::Range(s.to_owned()))?;
```
Done when: `parse_port("70000")` returns `Err(ParseError::Range(_))` and a test asserts it.
````

## should-fix, prose fix, multi-line anchor

Anchored on the range of lines the fix touches (`start_line`..`line`).

```
should-fix Retry loop re-reads the whole body on each attempt

Issue: `body` is a `Read`, so the second iteration of this loop sends an empty request; the retry can never succeed. `client.rs:88` is the only caller and passes a `File`.
Why it matters: bug — every retried upload fails with a 400 from the server instead of the transient error it was retrying.
Suggested fix: take `body: impl Read + Seek` and `seek(SeekFrom::Start(0))` at the top of the loop, or read it into a `Vec<u8>` once before the loop.
Done when: a test with a failing-then-succeeding mock transport sees the full body on the second attempt.
```

## nit

Short. The fixer will skip it unless asked, so it does not need the same
weight of evidence — but it still needs a concrete edit.

```
nit `HashMap` here is iterated in order-dependent tests

Issue: `render_summary` iterates `counts` and the snapshot test in `summary_test.rs:40` compares the output string.
Why it matters: maintainability — the test will flake when the hasher changes.
Suggested fix: use `BTreeMap`, or sort the keys before rendering.
Done when: `render_summary` output is deterministic across runs.
```

## q

A real question, not a softened should-fix. Say what you would have needed to
verify it.

```
q Is the 3-attempt retry budget shared with the gateway's own retries?

Issue: This adds 3 retries on top of whatever the gateway does; I could not find the gateway config in this repo to confirm whether it retries too.
Why it matters: perf — if both retry, one client request can fan out 9× under load.
Suggested fix: none until answered; if the gateway retries, drop this to 1.
Done when: answered in this thread.
```

## Cluster anchor

Posted on the entry point of the structural change. Carries the design and the
child list. `path:line` entries become permalinks after the backfill pass.

```
should-fix [parse-errors] Parse failures are stringly typed across the config module

Issue: Four new parse paths in this PR return `Err(String)` (listed below). Callers in `main.rs:52` match on the string content to decide exit codes.
Why it matters: maintainability — string matching on error text is already wrong for one path (`"invalid port"` vs `"port out of range"`), and each new parse function makes it worse.
Suggested fix: add `enum ParseError { Range(String), Syntax(String), Missing(&'static str) }` with `thiserror`, return it from every path below, and match on the variant in `main.rs`.
Done when: no function in `src/config/` returns `Result<_, String>`, and `main.rs` matches on `ParseError` variants.

Children:
- src/config/port.rs:42
- src/config/addr.rs:17
- src/config/duration.rs:30
- src/main.rs:52
```

## Cluster child

Local edit only. The design is in the anchor.

```
should-fix [parse-errors] Return `ParseError::Range` here

Issue: This is one of the `Err(String)` paths from the [parse-errors] anchor on `src/config/mod.rs`.
Why it matters: see anchor.
Suggested fix: `.map_err(|_| ParseError::Range(s.to_owned()))`.
Done when: this function's error type is `ParseError`.
```

## Review body

One or two sentences, no findings. Findings are in the threads.

```
One blocker in port parsing; the parse-errors cluster is a should-fix across four files. Ran `cargo test` on head — green apart from the case I added for the blocker.
```

Zero-finding approve:

```
Read the diff and ran `cargo clippy` and `cargo test` on 9f3c1a2; the new retry path is covered by `retry_test.rs`. No findings.
```

## Re-review: resolved thread whose condition does not hold

Reply on the existing thread, then unresolve it. Do not open a new thread.

```
Not yet — `parse_port("70000")` still returns `Ok(70000)` on 2b7e9d0; the new `u16` parse is only on the IPv6 branch. Reopening.

Done when: `parse_port("70000")` returns `Err(ParseError::Range(_))` on both branches.
```

## Re-review: author argued, you agree

```
Agreed — the HTTP layer needs both variants distinguishable. Resolving.
```

## Re-review: author argued, you don't

One reply with the specific point, then leave it for a human.

```
The mapping in `http.rs:112` only distinguishes them by string prefix today, which is the thing this thread is about. Leaving open for a maintainer to decide; not blocking on it.
```

## Re-review: outdated thread that the push fixed

```
Fixed in 562ee87 — the copy is now checked and the run exits 1 with `✗ copy failed: <name>`. Resolving.
```

## Re-review: resolved thread, not fixed, and your original claim was too strong

Say both things in one reply; the thread keeps the history.

```
Line 110 still keys on `-f "$dest/SKILL.md"`, so a target dir with only a stray file is overlaid on the first sync and `--check` reports drift. Correction to my note: a second sync does converge, so this is one spurious drift report, not permanent — nit, not should-fix. Reopening at that level.

Done when: `sync <name>` on a pre-existing dir without `SKILL.md` takes the replace path and the following `--check` is clean.
```

## Own thread that turned out to be a duplicate

```
Duplicate of the thread above on the same lines (opened a minute before mine). Resolving this one; that one stands.
```

## Do not write

- "Consider maybe possibly…" — say the finding or don't.
- "Looks good!" as a comment. Approval is the review event, not a thread.
- A comment whose Done when is "this is addressed".
- Two findings in one thread joined by "also".
- A blocker whose Issue line has no evidence you can point at.
- A summary of the PR in the review body. The author wrote the PR.
