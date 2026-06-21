# Create Managed Workspace

![Create Managed Workspace cover](assets/cover.png)

Create Managed Workspace is an agent-oriented Skill for Codex, Claude Code, opencode, and similar coding agents. It is designed to create maintainable project workspaces for recurring work that changes goals each time: CAD modeling, scraping projects, research writing, automation scripts, file conversion, and multi-output projects.

It does not generate domain-specific business logic. Instead, it builds the operating structure around the work: rules, project maps, task indexes, progress logs, temporary test areas, final output folders, and a dedicated `try/` folder for each small project. Only specialized task-type workspaces get a root place for reusable skills.

This is the English edition of the original Chinese skill:

```
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

By default, new workspaces use `multi-task` mode and do not include root `skills/`:

```text
<workspace-root>/
|-- AGENTS.md
|-- .gitignore
|-- .env.example
|-- docs/
|   |-- project-map.md
|   |-- task-index.md
|   `-- progress.md
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

A `specialized` task-type workspace additionally gets:

```text
<workspace-root>/
`-- skills/
    `-- .gitkeep
```

## Key conventions

- AGENTS.md defines agent operating rules.
- docs/project-map.md defines long-term structure.
- docs/task-index.md tracks cross-session tasks.
- docs/progress.md stores workspace-level progress.
- skills/ exists only for specialized task-type workspaces and stores reusable skills, wrappers, or external skill entrypoints.
- tasks/ stores small project units.
- Each task has its own docs and try/ sandbox.

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

## Task types

### CAD
- input: references
- work: intermediate models
- output: final exports and validation
- try: disposable experiments

### Scraping
- structured per-task data directories as needed
- maintain task-level documentation for sources and fields

### Research / automation
- input → work → output → try workflow

## Existing workspace alignment

This skill does not automatically migrate existing workspaces.
Use references for safe alignment planning.

## Safety

No secrets should be stored in README or docs.
Use .env for sensitive values.

## License

MIT License
