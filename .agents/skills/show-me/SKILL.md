---
name: show-me
description: |
  Explain the current topic with the smallest visual that makes the point:
  pseudocode, call tree, component tree, file tree, Mermaid, a shape-diff
  of those, a copyable target shape, or one focused HTML artifact.
  Use when writing or reviewing a pull request, a plan, or an architecture
  plan; when the user says show me, diagram, sketch, draw this, what
  changes, how does this flow; when a prose explanation is hiding
  ownership, order, or the shape of the diff.
  Not for posting GitHub review threads (github-pr-review) or issuing a
  BLESS/REJECT (architecture, gan-verdict).
---

# Show me

Explain the current topic of conversation visually. Skip the preamble
and keep prose brief. Pick the smallest view that makes the key point
clear.

## When

- Pull request: shape-diff of the call tree, file tree, or component
  tree; sequence of the changed path. Show what moved, not the whole
  system. Do not restate the GitHub diff.
- Plan: proposed file tree, intended call tree, types or signatures,
  short pseudocode of the new path.
- Architecture plan: layer or sequence Mermaid, responsibility file
  tree, module-boundary component tree.
- Anything else: the one form that answers the current question.

You may use one of these, you may use several. It is unlikely you
will use all of them.

## Forms

Logic or an algorithm as pseudocode:

```text
on(save)
  if content is unchanged
    return cached result
  write new content
  return fresh result
```

Runtime control flow as a call tree:

```text
submitForm
  createSession
    persistPrompt
    launchAgent
  navigateToSession
```

UI structure as a component tree, including state and module
boundaries that matter:

```tsx
<SessionPage> (apps/example/src/routes/session.tsx)
  useSessionEvents()
  <SessionToolbar>
    <RunSkillButton> (packages/ui)
```

File responsibility or a broad refactor as a shallow file tree:

```text
src/
├── commands/       # parses user actions
├── sessions/       # owns session state
└── transport/      # sends API requests
```

Component interaction, control flow, or data flow with Mermaid:

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant Daemon
    User->>UI: choose command
    UI->>Daemon: send expanded prompt
    Daemon-->>UI: stream result
```

Use `diff` when the point is what changes and the surrounding shape
already exists. Match the diff shape to the topic.

For a component change:

```diff
 <SessionPage>
   useSessionEvents()
   <SessionToolbar>
+    <RunSkillButton />
   <SessionTimeline>
+    <SkillResultCard />
```

For a file-layout change:

```diff
 src/
 ├── commands/
+│   └── show-me.ts       # expands the slash command
 ├── sessions/
-└── transport.ts
+└── transport/
+    ├── client.ts
+    └── stream.ts
```

For a call-tree or call-stack change:

```diff
 submitForm
   createSession
     persistPrompt
+    expandSkillMention
     launchAgent
-  navigateToSession
+  navigateToSession
+    subscribeToEvents
```

For a state or control-flow change:

```diff
 on(save)
-  write content
+  if content is unchanged
+    return cached result
+  write new content
+  invalidate cache
```

Show the whole block when most of it is new, when omitted context
would hide ownership or order, or when the user needs a copyable
target shape:

```ts
function expandSkill(command: string): string {
  const skillName = command.slice(1)
  return `use the ${skillName} skill`
}
```

## HTML

For a visual UI, layout, state comparison, or concept too dense for
Mermaid, write one focused HTML file — a diagram, an infographic, or
a short slide deck. Match the product's colors, type, spacing, and
components. Use real labels and data. Support desktop and mobile.

House palette when the artifact is for Sycamore / CrossR:

- Well pitch `#171412`
- Plaster page `#F3EEE6`
- Packed mile `#C4A882`
- Split fig `#9E4E36`
- Dust leaf `#6A7348`
- Canopy shade `#2E342C`

Write the file next to the work (`show-me-<slug>.html` or under
`docs/plans/`). Open it with whatever the environment has (`open`,
`xdg-open`, or the harness preview). Do not require Claude-Code
`Bash(open …)`.

## Guidance

Place each visual next to the short text it supports. Keep only the
calls, files, props, states, and boundaries needed to answer the
current question.

This skill presents shape. It does not review, bless, reject, or
open a PR.

Adapted from HumanLayer `show-me` (MIT).
https://github.com/humanlayer/skills
