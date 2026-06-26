# Create Managed Workspace

![Create Managed Workspace cover](assets/cover.png)

Create Managed Workspace is an agent-oriented Skill for Codex, Claude Code, opencode, and similar coding agents. It is designed to create maintainable project workspaces for recurring work that changes goals each time: CAD modeling, scraping projects, research writing, automation scripts, file conversion, and multi-output projects.

It does not generate domain-specific business logic. Instead, it builds the operating structure around the work: `AGENTS.md` rules, task indexes, progress logs, task project maps, task acceptance criteria, temporary test areas, final output folders, and a dedicated `try/` folder for each small project. Only specialized task-type workspaces get a root place for reusable skills.

This is the English edition of the original Chinese skill:

```text
https://github.com/q2955161835-debug/create-managed-workspace-skill
```

## Why this exists

Many agent tasks are not one-shot interactions. They span sessions, create multiple files, and must be resumed later. Without a stable workspace structure, common problems include:

- Mixing experimental files and final deliverables.
- Unclear latest output.
- Missing long-term progress tracking.
- CAD sources, exports, screenshots, and validation notes becoming disconnected.
- Repeated scraping due to missing task-level tracking.
- Loss of reusable local skills in dedicated task-type workspaces due to lack of storage conventions.

This skill encodes these conventions into scripts, templates, and validation rules.

## Generated workspace structure

By default, new workspaces use `multi-task` mode, do not include root `skills/`, and no longer create root `docs/project-map.md`. Root long-lived workspace information belongs in `AGENTS.md`.

```text
<workspace-root>/
|-- AGENTS.md
|-- .gitignore
|-- .env.example
|-- docs/
|   |-- task-index.md
|   `-- progress/
|       `-- YYYY-M-D.md
|-- tasks/
|   |-- README.md
|   `-- YYYYMMDD-short-task-name/
|       |-- README.md
|       |-- docs/
|       |   |-- project-map.md
|       |   |-- acceptance-criteria.md
|       |   `-- progress/
|       |       `-- YYYY-M-D.md
|       |-- input/
|       |-- work/
|       |-- output/
|       `-- try/
|-- output/
`-- try/
```

A `specialized` task-type workspace additionally gets:

```text
<workspace-root>/
`-- skills/
    `-- .gitkeep
```

## Key conventions

- `AGENTS.md` defines workspace rules, workspace purpose, directory responsibilities, task registration, output placement, environment ledgers, and agent operating constraints.
- Root `docs/project-map.md` is deprecated and no longer generated; migrate old root project-map content into `AGENTS.md`.
- `docs/task-index.md` tracks cross-session tasks.
- `docs/progress/YYYY-M-D.md` stores workspace-level progress by record completion date.
- `skills/` exists only for specialized task-type workspaces and stores reusable skills, wrappers, or external skill entrypoints.
- `tasks/` stores small project units.
- Each task keeps `docs/project-map.md` for long-lived task structure.
- Each task keeps `docs/acceptance-criteria.md` for functional, interaction, test, manual acceptance, result, and final conclusion checks.
- Each task has its own `try/` sandbox.

## Installation

Clone into your agent-accessible skills directory:

```powershell
git clone https://github.com/q2955161835-debug/create-managed-workspace-skill-en.git D:\2Folder\skills\create-managed-workspace-en
```

## Quick start

Create a workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\new_workspace.py "D:\Projects\MyWorkspace" --name "My Workspace"
```

Create a specialized task-type workspace with root `skills/`:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\new_workspace.py "D:\Projects\CadWorkspace" --name "CAD Workspace" --workspace-kind specialized
```

Create a task:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\new_task.py "D:\Projects\MyWorkspace" "CAD bracket model"
```

Validate:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\validate_workspace.py "D:\Projects\MyWorkspace"
```

Validate a specialized task-type workspace explicitly:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\validate_workspace.py "D:\Projects\CadWorkspace" --workspace-kind specialized
```

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/new_workspace.py` | Creates a managed workspace root; default multi-task mode creates no `skills/` and no root `docs/project-map.md`; specialized mode creates `skills/`. |
| `scripts/New-Workspace.ps1` | Windows PowerShell wrapper for `new_workspace.py`. |
| `scripts/new_task.py` | Creates a standard small project under `tasks/`, including `docs/project-map.md` and `docs/acceptance-criteria.md`. |
| `scripts/validate_workspace.py` | Checks the workspace root and task folders, and reports deprecated root `docs/project-map.md` files. |

Scripts do not overwrite existing files unless `--overwrite` is passed.

## Task types

### CAD

- `input/`: reference drawings, photos, PDFs, and dimensions.
- `work/`: parametric modeling sources, drafts, and temporary check scripts.
- `output/`: final sources, STEP/STL/3MF/GLB/DXF/DWG exports, screenshots, and verification notes.
- `docs/acceptance-criteria.md`: export checks, geometry checks, screenshot/manual review, and final conclusion.
- `try/`: disposable geometry experiments.

### Scraping

- Put variable confirmation tables and field definitions under task `docs/` or the task root.
- Maintain `docs/task-list.md` for multi-source dedupe tracking when needed.
- Add `raw-data/`, `raw-files/`, `old-data/`, `clean-data/`, `evidence-screenshots/`, and `reports/` only when needed.
- Document new folders in task `docs/project-map.md`.
- Record source coverage, dedupe checks, output file checks, and manual review in `docs/acceptance-criteria.md`.
- Put fetch tests, parser experiments, and one-off probes in task `try/`.

### Research / automation

- `input/`: prompts, materials, references, and user-provided files.
- `work/`: drafts, scripts, notebooks, and intermediate reports.
- `output/`: final documents, tables, script packages, or deliverables.
- `docs/acceptance-criteria.md`: repeatable commands, manual review criteria, output file checks, and final conclusion.
- `try/`: disposable conversion tests, command probes, and temporary validation.

## Existing workspace alignment

This skill does not automatically migrate existing workspaces. Use references for safe alignment planning:

- `references/existing-workspace-alignment.md`
- `references/task-type-adjustments.md`
- `references/rule-checklist.md`

Recommended strategy:

- Add missing documentation and `try/` folders before moving historical files.
- If root `docs/project-map.md` exists, migrate useful content into `AGENTS.md`, then remove the deprecated file.
- Do not split already well-organized historical output trees.
- Create a checkpoint commit before large structural edits in Git-managed folders.
- Confirm before renaming directories, bulk-moving files, or deleting historical outputs.

## Safety

No secrets should be stored in README, `AGENTS.md`, docs, acceptance criteria, or progress records. Use `.env` for sensitive values, keep it ignored, and maintain `.env.example` with placeholders only.

## Validation

Validate a generated workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\validate_workspace.py "D:\Projects\MyWorkspace"
```

Successful output:

```text
OK    Workspace structure check passed
```

## License

MIT License
