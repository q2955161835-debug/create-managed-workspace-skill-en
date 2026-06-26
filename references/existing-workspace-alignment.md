# Existing Workspace Alignment

Use this reference only when the user asks to plan or perform organization of an existing workspace. Do not migrate existing CAD or scraping workspaces automatically just because this skill was used.

## Alignment Policy

- First inspect current `AGENTS.md`, `docs/task-index.md`, progress record folders, Git status, and top-level directories.
- If root `docs/project-map.md` exists, treat it as deprecated and migrate its useful long-lived workspace information into `AGENTS.md` before removing it.
- Preserve existing useful conventions when they do not conflict with the standard managed workspace.
- Prefer adding missing documentation, `try/` folders, task maps, task acceptance criteria, and indexes before moving historical files.
- Do not rename or move large historical output trees without explicit user confirmation.
- For Git-managed folders, create a checkpoint commit before structural edits.
- Decide whether the workspace is `multi-task` or `specialized` before adding root-level support folders.

## Minimum Alignment

- Root has `AGENTS.md`, `.gitignore`, `.env.example`, `docs/task-index.md`, a progress record folder, and `try/`.
- Root does not keep `docs/project-map.md`; the equivalent long-term workspace information belongs in `AGENTS.md`.
- General `multi-task` workspaces do not need root `skills/`.
- Dedicated `specialized` task-type workspaces should have root `skills/` when common skills or skill entrypoints are part of the workflow.
- Cross-session small projects are represented in `tasks/` or documented as existing first-level equivalents.
- Every small project has a project map, acceptance criteria, a progress record folder, and `try/`.
- Each special-purpose output folder has a clear owner and purpose in a task project map or in `AGENTS.md` if it is workspace-level.

## CAD Workspace Notes

- Existing CAD workspaces may already use `output/<task-name>/` as the small-project layer.
- When aligning, either keep `output/<task-name>/` as a documented legacy task layer or create future tasks under `tasks/` and leave old output folders in place.
- Do not split source/export/screenshot sets that already belong together.
- Treat CAD workspaces as `specialized` only when they need reusable CAD skills, wrappers, or skill entrypoints inside the workspace. Otherwise document external skill paths in `AGENTS.md` or the relevant task `docs/project-map.md` without adding root `skills/`.

## Scraping Workspace Notes

- Existing scraping workspaces may already use first-level target folders.
- Keep scaffold/tooling directories such as `scaffolding/` separate from real data targets.
- Align each target by adding a project map, acceptance criteria, a progress record folder, and `try/` when missing.
- Add root `skills/` only for a dedicated scraping workspace that maintains reusable scraping skills or entrypoints.
