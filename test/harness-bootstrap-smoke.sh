#!/usr/bin/env bash
# Basic smoke test for harness-bootstrap

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOOTSTRAP="$SCRIPT_DIR/scripts/harness-bootstrap"

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

echo "Testing fresh bootstrap..."
"$BOOTSTRAP" "$TMPDIR" > /dev/null

if [ -f "$TMPDIR/AGENTS.md" ] && [ -f "$TMPDIR/features.json" ] && [ -f "$TMPDIR/justfile" ]; then
    echo "✓ Fresh bootstrap created expected files"
else
    echo "✗ Fresh bootstrap failed"
    exit 1
fi

echo "Testing idempotency (no --force)..."
"$BOOTSTRAP" "$TMPDIR" > /dev/null 2>&1 || true

echo "Testing --force overwrite..."
"$BOOTSTRAP" --force "$TMPDIR" > /dev/null

echo "✓ All smoke tests passed"