---
name: gan-verdict
description: |
  Verdict and report-envelope protocol for every CrossR GAN gate.
  Owned by neither conductor nor adversary; referenced by both, redefinable by neither. The conductor may specify what it wants to hear, never what counts as approval.
---

# GAN Verdict Protocol

1. Verdict tokens: exactly `BLESS` or `REJECT`. Silence, hedge, or "LGTM" is not approval.
2. One verdict per delegation.
3. The verdict names its gate: `<gate>: BLESS | REJECT` (e.g. `architecture: BLESS`).
4. `REJECT` must cite concrete blockers.
5. Report envelope — field schema (all fields optional; the conductor selects which apply and fills the values at delegation time):
   - phase id
   - "k of n"
   - AC ids claimed
   - findings shape (one-liners | prose)
   - max length
   - `file:line` citations
6. Adding an envelope field means changing this file — never a conductor card.
