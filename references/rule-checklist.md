# Rule Checklist

Use this checklist before finishing workspace creation or editing generated rules.

## Root

- `AGENTS.md` describes task ownership, task folders, root `skills/`, root `try/`, progress records, and environment ledgers.
- `.gitignore` ignores `.env`, caches, root `try/` contents, and task `try/` contents while preserving `.gitkeep`.
- `.env.example` contains placeholders only and no real secrets.
- `docs/project-map.md` records long-term workspace purpose and directory responsibilities.
- `docs/task-index.md` exists for cross-session tasks.
- `docs/progress.md` records workspace-level summaries.
- `skills/` exists and is empty except `.gitkeep` at creation.
- `try/` exists and contains no required project result.

## Task

- Directory name uses `YYYYMMDD-short-task-name`.
- `README.md` records goal, current status, key decisions, and next step.
- `docs/project-map.md` records the task purpose, directory responsibilities, entry points, dependencies, and output flow.
- `docs/progress.md` records minute-level time ranges.
- `input/` holds input material.
- `work/` holds drafts, scripts, and intermediate files.
- `output/` holds final deliverables.
- `try/` holds disposable tests and can be cleared safely.

## Safety

- For existing Git-managed folders, check status before structural edits.
- For broad changes, create a checkpoint commit first.
- For high-risk local operations, use a timestamped backup under a clearly named backup directory.
