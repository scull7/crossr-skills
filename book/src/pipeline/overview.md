# Pipeline Overview

CrossR’s flagship product story is a two-stage loop:

```
Intent → AVRIL (plan GAN) → Blessed Backlog → AXEL (PETC + code GAN) → Done
```

Most AI coding fails at the seam between “sounds good” and “shipped.” This pipeline makes that seam explicit.

## Stages

| Stage | Owner | What happens |
|-------|--------|----------------|
| **Intent** | Human | PRD, conversation, prototype notes, ADR set |
| **AVRIL** | Planning GAN | Architect proposes PBIs; PO → QA → CTO must each `BLESS` |
| **Blessed Backlog** | Board (Pinto preferred) | Finite authorized set — planning **stops** here |
| **AXEL** | Execution loop | Only blessed work; PETC + code GAN; AC evidence |
| **Done** | Board + tracking | Honest status; AC checked; commits linked |

## Hard rules

1. **Planning stop** — AVRIL does not implement code. When every PBI is triple-blessed, emit a Blessed Backlog Summary and stop.
2. **Intake gate** — AXEL refuses unblessed work unless the human explicitly authorizes a finite id set.
3. **Scope changes** mid-execution return to AVRIL — AXEL does not re-bless product intent.
4. **Canon** lives in [HARNESS-SPEC.md](https://github.com/scull7/crossr-skills/blob/main/HARNESS-SPEC.md) §12–13. This book is a thin progressive lens, not a second law.

## Next

- [AVRIL — Planning GAN](avril.md)
- [BRICK — the alternative pipeline](brick.md) — transformation and mutation testing instead of adversarial review
- [AXEL — Execution Loop](axel.md)
- [First session prompts](../getting-started/bootstrap.md#first-session-avril--axel)

In OpenCode, the pair is one keystroke away: `/avril` for planning (bare `/avril` is a read-only status report) and `/axel` for execution (bare `/axel` reports the next blessed PBI and asks before running). Restart opencode after installing them.
