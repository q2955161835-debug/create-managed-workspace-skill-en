# Rule Checklist

Use this checklist before finishing workspace creation or editing generated rules.

## Root

- `AGENTS.md` describes task ownership, task folders, workspace kind, root `try/`, progress records, and environment ledgers.
- `.gitignore` ignores `.env`, caches, root `try/` contents, and task `try/` contents while preserving `.gitkeep`.
- `.env.example` contains placeholders only and no real secrets.
- `docs/project-map.md` records long-term workspace purpose and directory responsibilities.
- `docs/task-index.md` exists for cross-session tasks.
- `docs/progress/YYYY-M-D.md` records workspace-level summaries, one file per record completion date.
- For `multi-task` workspaces, root `skills/` is absent by default.
- For `specialized` task-type workspaces, root `skills/` exists and is empty except `.gitkeep` at creation unless the user asked for skill entrypoints.
- `try/` exists and contains no required project result.

## Task

- Directory name uses `YYYYMMDD-short-task-name`.
- `README.md` records goal, current status, key decisions, and next step.
- `docs/project-map.md` records the task purpose, directory responsibilities, entry points, dependencies, and output flow.
- `docs/progress/YYYY-M-D.md` records minute-level time ranges.
- `input/` holds input material.
- `work/` holds drafts, scripts, and intermediate files.
- `output/` holds final deliverables.
- `try/` holds disposable tests and can be cleared safely.

## Safety

- For existing Git-managed folders, check status before structural edits.
- For broad changes, create a checkpoint commit first.
- For high-risk local operations, use a timestamped backup under a clearly named backup directory.
