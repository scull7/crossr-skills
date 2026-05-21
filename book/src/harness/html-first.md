# HTML as the Primary Human Interface

For any artifact whose primary audience is a human — specifications, architecture reviews, PR summaries, progress reports, dashboards, deployment guides, etc. — **generate a self-contained HTML file** as the main deliverable.

## Rationale

Markdown is excellent for agents and git.

HTML (especially beautiful, self-contained Tailwind-via-CDN single-file HTML) is dramatically more effective for human comprehension and engagement.

This is sometimes called "the unreasonable effectiveness of HTML."

Modern models are exceptionally good at producing high-quality, scannable, visually rich single-file HTML with almost no extra prompting.

## Guidelines

- Output a single `.html` file.
- Use Tailwind CSS via CDN (`https://cdn.tailwindcss.com`).
- Make the document scannable with clear sections, cards, status pills, and good typography.
- You may still produce a Markdown version for git history and agent handoff.
- Treat the HTML as the **primary** human-facing artifact.

## Examples in This Repository

- `docs/plans/harness-improvement-plan.html`
- The marketing site you are currently reading (`site/`) was built with the same philosophy.

This rule is now a first-class part of the harness and is enforced in `AGENTS.md`.