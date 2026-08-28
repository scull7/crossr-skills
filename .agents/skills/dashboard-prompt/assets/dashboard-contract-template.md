{{PROJECT_NAME}} — STATUS DASHBOARD CONTRACT (in-harness UI)

You are the agent doing the work in this project. This file tells you how to keep
its status view honest while you work. It is machine-facing: it assumes you already
know the project, and it never explains what a dashboard is.

PARAMETERS (resolved for this project)
  PROJECT_NAME     = {{PROJECT_NAME}}
  REPO             = {{ABSOLUTE_REPO_PATH}}
  REFRESH          = {{terminal command, e.g. `just status`}}
  PUBLISH          = {{HTML command, e.g. `just status-html`}}
  DASHBOARD_FILE   = {{path PUBLISH writes, e.g. docs/status-dashboard.html}}
  CONFIG           = {{dashboard.config.json, or "none — defaults apply"}}
  SOURCES          = see SOURCES below
  CHECKPOINTS      = see CHECKPOINTS below

SOURCES OF TRUTH (read-only; the dashboard renders these, it never replaces them)
  Board          : {{command + what it returns, or "none"}}
  Tracking file  : {{features.json or equivalent, or "none"}}
  Narrative log  : {{progress.md or equivalent, or "none"}}
  Status words   : done   = {{project's done words}}
                   active = {{project's in-flight words}}
                   everything else counts as todo
  If a source is missing, the dashboard degrades to what remains. That is expected.
  Say which source is absent rather than filling the gap with a guess.

CHECKPOINTS (refresh at each; never batch them to the end)
{{- checkpoint 1, tied to a real state change in this project}}
{{- checkpoint 2}}
{{- checkpoint 3}}
  The rule behind the list: refresh immediately after the underlying state changes,
  because the window between the change and the refresh is the window in which the
  dashboard is lying.

RULES
  - Generated, never hand-written. Run REFRESH or PUBLISH. Do not hand-author
    DASHBOARD_FILE, and do not edit it to say something the sources do not.
  - The dashboard is a view, not a record. When it disagrees with the board, the
    board wins and the disagreement is itself a finding worth reporting.
  - Never show work as complete before its completion evidence exists.
  - A stale dashboard is worse than none. If you cannot refresh it, say so in the
    same place you record progress, and say why.
  - Commit DASHBOARD_FILE only at {{commit boundary for this project}}, not on
    every refresh, so the diff stays meaningful.
  - Report counts you read, never counts you expect. If REFRESH shows zeros where
    you believed there was work, that is a defect in the sources or the config —
    investigate it, do not narrate around it.

WHEN THE NUMBERS LOOK WRONG
  A dashboard reporting "0 in progress" during active work usually means the status
  vocabulary does not match the tracker's. Check CONFIG's status words against the
  literal strings the board emits before concluding the work is untracked.
  {{project-specific gotcha, or "No known mismatches."}}

FIRST ACTION
  Run REFRESH now and state the current counts before doing anything else. That is
  your baseline, and every later claim of progress is measured against it.
