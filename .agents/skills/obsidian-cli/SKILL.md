---
name: obsidian-cli
version: 1.1.0
tags: [obsidian, cli, vault, markdown, productivity, plugin-dev]
description: High-value guidance for using Obsidian CLI v1.12+ to interact with vaults. Focuses on smart usage, common workflows, error handling, and best practices rather than exhaustive command lists. Use for vault ops, note management, tasks, properties, plugin/theme dev. Prioritizes token efficiency and AI-first patterns. Requires Obsidian running.
---

# Obsidian CLI Skill

Use the `obsidian` CLI to interact with a **running Obsidian instance**. It excels at quick reads/writes, searches, and dev tasks but is not always the best tool for complex edits.

**Always run `obsidian help` or `obsidian <command> --help` first** for the latest.

Full docs: https://help.obsidian.md/cli

## When to Use CLI vs. Direct File/Markdown Edits
- **Use CLI**: Quick mutations (append, property set), searches, daily notes, tasks/tags, plugin reloads, dev debugging.
- **Use direct Markdown/Canvas edits** (compose with obsidian-markdown skill): Complex restructuring, large content generation, Canvas/Bases heavy work, or when avoiding shell quoting issues.
- **Fallback**: Direct `cat`/`echo` or file tools for massive vaults or when CLI has permission/sync conflicts.

**Decision Tree**:
- Small/quick change? → CLI (e.g., `property:set`, `append`).
- Semantic search + reasoning? → CLI `search` + parse output.
- Big rewrite or AI-generated content? → Direct edit skill.
- Plugin/theme dev? → CLI dev commands.

## Syntax & Targeting Basics
**Parameters**: `key=value` (quote spaces).
**Flags**: Boolean (no value), e.g., `silent overwrite`.
**Multiline**: Use `
`, `	`.

**File targeting**:
- `file=<name>` (wikilink-style, no extension/path needed).
- `path=<exact/path/from/vault.md>`.

**Vault targeting**: Defaults to focused vault. Prefix: `vault="Vault Name"`.

**Useful globals**: `--copy` (clipboard), `silent` (no open), `total` (counts), `limit=N`.

## Core Workflows (Token-Efficient Examples)
```bash
# Read / quick inspect
obsidian read file="My Note" --copy

# Create / append
obsidian create name="New Note" content="# Header\nContent" template="Daily" silent
obsidian append file="My Note" content="- [ ] New task\n"

# Properties & tasks
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo

# Search
obsidian search query="keyword" limit=20
```

**Common Chains** (Daily note + tasks + properties):
1. `obsidian daily:append content="- [ ] Task"`
2. `obsidian property:set ...`
3. Parse output in LLM prompt for follow-up.

## Querying Vault State
- `search`, `tags`, `backlinks`, `list`, `daily:*`.
- **Tip**: Use `total` for counts on large vaults to avoid token bloat.

## Safe Mutations
Prefer `create`, `append`, `property:*` over full overwrites. Always use `silent` when scripting.

## Plugin & Theme Development
**Dev cycle**:
1. Edit code.
2. `obsidian plugin:reload id=my-plugin`
3. `obsidian dev:errors`
4. `obsidian dev:screenshot` or `dev:dom`
5. `obsidian dev:console level=error`
6. `obsidian eval code="..."` for JS inspection.

Additional: `dev:css`, `dev:mobile`.

## Error Handling & Gotchas
- **Vault not found/focused**: Specify `vault=`.
- **Permission / sync conflicts**: Use `silent`; check mobile sync separately. Large vaults → fallback to file ops.
- **CLI version mismatch**: Run `obsidian version`; ensure >=1.12.
- **Quoting/shell issues** (cross-agent): Escape carefully; test in target CLI (Claude vs. Gemini shell handling differs).
- **Output parsing**: LLM tip — ask for structured JSON summary when possible (`--copy` + parse).
- **Network/sync errors**: Retry or check Obsidian status; avoid during active mobile sync.
- **No output / hangs**: Add `limit=`; large results bloat tokens.

**Anti-patterns**:
- Don't overuse for complex workflows → compose skills.
- Avoid full `read` on huge notes without limits.
- Never expose sensitive vault data without user confirmation (properties/history may contain PII).

## Security & Privacy
Obsidian vaults often hold sensitive info. 
- Default to minimal commands.
- Review outputs before sharing.
- Avoid `history`, full `properties`, or `eval` on untrusted code unless necessary.
- Agent guideline: Ask user before commands that read many files or export data.

## Performance & Scale
- **Large vaults** (1k+ notes): Use targeted `search`/`file=`, avoid broad lists. Fallback to direct filesystem for bulk.
- Search limits: Always set `limit=`.
- Mobile edges: CLI primarily desktop-focused; test sync.

## Cross-Agent & LLM Tips
- **Shell differences**: Gemini/Claude may need different quoting. Test commands.
- **Parsing**: Instruct LLM: "Parse CLI output as JSON if possible" or "Summarize key findings."
- **Tool restrictions**: Some agents limit shell; prefer composable skills.
- **Validator**: Test in target environment with sample vault (edge cases: conflicts, large files, disabled plugins).

## Testing Notes
- Verified against `obsidian help` (v1.12.x).
- Simulated agent workflows, error scenarios, large vault mocks.
- Cross-agent: Tested basic compatibility in Claude Code / similar.

**Recommendation**: Keep SKILL.md lean. Move exhaustive command reference to `reference/commands.md` in a follow-up PR if volume grows. This version prioritizes intelligence over completeness.