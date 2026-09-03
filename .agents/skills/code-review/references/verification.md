# Verification

In a fresh activation the following behaviors are directly observable and scorable:

- The agent applies the Non-Negotiable Core Principles and the complete Ruthless Review Checklist item-by-item to the input code, explicitly naming each violation found (e.g., "violates #3 Functional Purity", "checklist item Error Handling: inline map_err present").
- The agent verifies the code against the disclosed book Rules projection when one exists and flags any gaps.
- The agent requires that all violations be resolved with minimal, exact fixes (no unrelated refactors) and re-evaluates until the code would pass a fresh review under this skill.
- The agent emits its verdict per the `gan-verdict` contract; the review output's own structure and language exemplify the desired qualities: clear layers, intention-revealing, no fluff, pedantic but high-signal.

Violations against any of these observable criteria during fresh activation indicate the skill was not followed and must be corrected before the work can be considered complete.
