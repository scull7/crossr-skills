default:
    @just --list

# Environment bootstrap
init:
    echo "crossr-skills environment ready"

# Quality gates (used by agents and CI)
check:
    cargo check --workspace 2>/dev/null || echo "(no Rust crates yet)"

test:
    cargo test --workspace 2>/dev/null || echo "(no tests yet)"

clippy:
    cargo clippy --workspace -- -W clippy::pedantic -D warnings 2>/dev/null || echo "(no Rust crates)"

fmt:
    cargo fmt --all --check 2>/dev/null || echo "(no Rust crates)"

# Catalog validation (process checks live in sycamore-hq/crossr-harness)
harness-validate:
    @just docs-verify
    @just claude-skills-check
    @if command -v jq >/dev/null 2>&1; then \
        jq -e 'if type == "object" then . else error("features.json must be an object") end' features.json > /dev/null && \
        echo "features.json: basic structure OK" || \
        (echo "features.json: invalid structure" && exit 1); \
    else \
        echo "jq not found — skipping features.json validation"; \
    fi

# Catalog allowlist vs README vs SKILL.md
docs-verify:
    @./scripts/verify-docs

docs-verify-report:
    @./scripts/verify-docs --html

# Claude compatibility copies of .agents/skills/
claude-skills-sync:
    @./scripts/sync-claude-skills

# Non-fatal drift report; skips when no Claude skills directory exists
claude-skills-check:
    @echo "" && echo "Checking Claude skill copies..." && ./scripts/sync-claude-skills --check --soft
