#!/usr/bin/env bash
# Idempotent Cloud Agent install. Runs from the repository root after checkout.
set -euo pipefail

export PATH="/usr/local/cargo/bin:/usr/local/bin:${HOME}/.cargo/bin:${PATH}"

for cmd in just python3 jq git; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "crossr-skills install: $cmd is not on PATH" >&2
    exit 1
  fi
done

just init
