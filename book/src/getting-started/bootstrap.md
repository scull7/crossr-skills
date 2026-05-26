# Bootstrapping a New Project

The fastest way to adopt the full harness in a new project is the `harness-bootstrap` script.

## One Command

```bash
git clone https://github.com/scull7/crossr-skills.git
./crossr-skills/scripts/harness-bootstrap /path/to/your-new-project
```

## What Gets Created

The bootstrap emits a complete, ready-to-commit harness:

- `AGENTS.md` (with Plan Mode and skill references)
- `features.json` + `features.schema.json`
- `progress.md`
- `justfile` with the standard targets
- `.agents/skills/` (copy of the skills you choose)
- `.gitignore` entries for generated artifacts
- `CLAUDE.md` (optional, generated)
- A `harness-validate` target

After running the script, you should immediately commit the new harness as the foundation of the project.

## After Bootstrapping

Run:

```bash
just harness-validate
just init
```

`just harness-validate` now also runs `just docs-verify` to ensure documentation stays aligned with the current canonical standards.

Then begin your first piece of work using the PETC loop.

The bootstrap script itself is part of the harness and is maintained using the same process it enables.