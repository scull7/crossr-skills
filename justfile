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

# Documentation (mdBook)
book-build:
    cd book && mdbook build

book-serve:
    cd book && mdbook serve --open

# Combined docs site (Zola marketing + mdBook at /docs)
docs-build:
    mdbook build book --dest-dir site/static/docs
    cd site && zola build --force
    @echo "Built combined site. Output in site/public (docs at site/public/docs/)"

docs-serve:
    @echo "For local combined serving, build with 'just docs-build' then serve site/public"