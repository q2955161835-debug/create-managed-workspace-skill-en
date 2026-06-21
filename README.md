# Create Managed Workspace

![Create Managed Workspace cover](assets/cover.png)

Create Managed Workspace is a Codex skill for creating maintainable project workspaces for recurring work. It is designed for tasks that repeat often but change goal each time: CAD modeling, scraping projects, research writing, automation scripts, file conversion, and multi-output project work.

The skill does not generate business logic for one domain. It creates the operating structure around the work: project rules, project maps, task indexes, progress logs, temporary test areas, final output folders, a place for commonly used skills, and a dedicated `try/` folder for every small project.

This is the English edition of the original Chinese skill. The original local installed skill is at:

```text
D:\2Folder\skills\create-managed-workspace
```

The original Chinese open-source repository is:

```text
https://github.com/q2955161835-debug/create-managed-workspace-skill
```

## Why this exists

Many agent tasks are not one-shot answers. They span several sessions, create multiple files, and need to be resumed later. Without a stable workspace structure, teams often run into these problems:

- Final outputs and temporary experiments end up in the same folder.
- The latest deliverable is unclear.
- Long-running work lacks a durable progress record.
- CAD source files, exported models, screenshots, and validation notes lose their relationship.
- Scraping projects repeat the same source collection because there is no task list or dedupe record.
- Useful local skills are rediscovered repeatedly because there is no workspace-level storage point.

This skill turns those conventions into scripts, templates, and validation checks.

## Generated workspace structure

```text
<workspace-root>/
|-- AGENTS.md
|-- .gitignore
|-- .env.example
|-- docs/
|   |-- project-map.md
|   |-- task-index.md
|   `-- progress.md
|-- skills/
|   `-- .gitkeep
|-- tasks/
|   |-- README.md
|   `-- YYYYMMDD-short-task-name/
|       |-- README.md
|       |-- docs/
|       |   |-- project-map.md
|       |   `-- progress.md
|       |-- input/
|       |-- work/
|       |-- output/
|       `-- try/
|-- output/
`-- try/
```

Key conventions:

- `AGENTS.md`: workspace-level operating rules for agents.
- `docs/project-map.md`: long-term workspace map and directory responsibilities.
- `docs/task-index.md`: cross-session task index.
- `docs/progress.md`: concise workspace-level progress summary.
- `skills/`: storage for commonly used workspace-specific skills. It starts empty.
- `tasks/`: small project directories.
- `tasks/.../docs/project-map.md`: long-lived map for one small project.
- `tasks/.../docs/progress.md`: progress record for one small project.
- `tasks/.../try/`: temporary test and debugging area for that small project.
- `output/`: workspace-level or historical deliverables.
- root `try/`: workspace-level one-off tests only.

## Installation

Clone this repository into a location your agent can read:

```powershell
git clone https://github.com/q2955161835-debug/create-managed-workspace-skill-en.git D:\2Folder\skills\create-managed-workspace-en
```

Then register or route the skill according to your local agent setup:

```text
D:\2Folder\skills\create-managed-workspace-en\SKILL.md
```

## Quick start

Create a new workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\new_workspace.py "D:\Projects\MyWorkspace" --name "My Workspace"
```

Use the PowerShell wrapper:

```powershell
D:\2Folder\skills\create-managed-workspace-en\scripts\New-Workspace.ps1 -Path "D:\Projects\MyWorkspace" -Name "My Workspace"
```

Create a task inside an existing managed workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\new_task.py "D:\Projects\MyWorkspace" "CAD bracket model"
```

Validate the workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\validate_workspace.py "D:\Projects\MyWorkspace"
```

Initialize Git and create a baseline commit while creating a new workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\new_workspace.py "D:\Projects\MyWorkspace" --name "My Workspace" --init-git
```

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/new_workspace.py` | Create a standard managed workspace root. |
| `scripts/New-Workspace.ps1` | Windows PowerShell wrapper for `new_workspace.py`. |
| `scripts/new_task.py` | Create a standard small project under `tasks/`. |
| `scripts/validate_workspace.py` | Check whether a workspace and its tasks match the expected structure. |

Scripts do not overwrite existing managed files by default. Use `--overwrite` only when replacement is intended.

## Task type adjustments

### CAD

Use one task directory per CAD job:

- `input/`: drawings, photos, PDFs, measurement references.
- `work/`: parametric source, draft geometry, intermediate checks.
- `output/`: final source, STEP/STL/3MF/GLB/DXF/DWG exports, screenshots, validation notes.
- `try/`: disposable geometry experiments.

If CAD skills live outside the workspace, record their paths in `docs/project-map.md`. Copy them into root `skills/` only when the workspace needs a private version.

### Scraping

Use one task directory per scraping target:

- Put variable confirmation tables and field definitions under task `docs/` or the task root.
- Maintain `docs/task-list.md` when multiple URLs, files, APIs, or channels require dedupe tracking.
- Add `raw-data/`, `raw-files/`, `old-data/`, `clean-data/`, and `reports/` only when needed.
- Document every added folder in the task `docs/project-map.md`.
- Keep temporary fetch probes and parser experiments in task `try/`.

### Research, writing, and automation

- `input/`: prompts, source files, user-provided materials.
- `work/`: drafts, scripts, notebooks, intermediate reports.
- `output/`: final documents, tables, packages, or deliverables.
- `try/`: one-off conversion tests, command probes, temporary validation.

## Existing workspace alignment

This skill can guide organization of existing workspaces, but it does not automatically migrate them. Read:

- `references/existing-workspace-alignment.md`
- `references/task-type-adjustments.md`
- `references/rule-checklist.md`

Recommended alignment strategy:

- Add missing documentation and `try/` folders before moving historical files.
- Preserve useful existing conventions when they do not conflict with the managed workspace structure.
- Do not rename or move large historical output trees without explicit confirmation.
- For Git-managed folders, create a checkpoint commit before structural edits.

## Environment and secret safety

Generated `.env.example` files are placeholders only. Real sensitive configuration belongs in `.env`, and `.env` must be ignored.

Never place real API keys, tokens, cookies, database passwords, or private endpoints in:

- `.env.example`
- README files
- progress records
- copyable chat snippets

## Validation

Validate the skill:

```powershell
python C:\Users\29551\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\2Folder\skills\create-managed-workspace-en
```

Validate a generated workspace:

```powershell
python D:\2Folder\skills\create-managed-workspace-en\scripts\validate_workspace.py "D:\Projects\MyWorkspace"
```

Expected success output:

```text
OK    Workspace structure check passed
```

## Repository layout

```text
.
|-- SKILL.md
|-- README.md
|-- LICENSE
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- cover.png
|   `-- templates/
|-- references/
|   |-- existing-workspace-alignment.md
|   |-- rule-checklist.md
|   `-- task-type-adjustments.md
`-- scripts/
    |-- New-Workspace.ps1
    |-- new_task.py
    |-- new_workspace.py
    `-- validate_workspace.py
```

## License

This project is released under the MIT License. See `LICENSE`.
