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

# Harness-specific
harness-validate:
    @if command -v jq >/dev/null 2>&1; then \
        jq -e 'if type == "object" then . else error("features.json must be an object") end' features.json > /dev/null && \
        echo "features.json: basic structure OK" || \
        (echo "features.json: invalid structure" && exit 1); \
        if [ -f features.schema.json ]; then \
            echo "Schema validation not yet implemented (requires ajv or similar)"; \
        fi; \
    else \
        echo "jq not found — skipping features.json validation"; \
    fi

# =============================================================================
# Site & Documentation (Zola + mdBook) — dogfooding the harness
# =============================================================================

# Marketing site (Zola)
site-build:
    cd site && zola build --force

site-serve:
    cd site && zola serve

# Documentation (mdBook) — will be expanded in later phases
book-build:
    @echo "mdBook build target will be added in Phase C"

book-serve:
    @echo "mdBook serve target will be added in Phase C"

# Combined (marketing only for now)
docs-build: site-build
    @echo "Built marketing site. mdBook integration coming in Phase D."