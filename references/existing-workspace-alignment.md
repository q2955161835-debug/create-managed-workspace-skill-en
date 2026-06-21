# Existing Workspace Alignment

Use this reference only when the user asks to plan or perform organization of an existing workspace. Do not migrate existing CAD or scraping workspaces automatically just because this skill was used.

## Alignment Policy

- First inspect current `AGENTS.md`, project maps, progress records, Git status, and top-level directories.
- Preserve existing useful conventions when they do not conflict with the standard managed workspace.
- Prefer adding missing documentation, `try/` folders, task maps, and indexes before moving historical files.
- Do not rename or move large historical output trees without explicit user confirmation.
- For Git-managed folders, create a checkpoint commit before structural edits.

## Minimum Alignment

- Root has `AGENTS.md`, `.gitignore`, `.env.example`, project map, progress record, `skills/`, and `try/`.
- Cross-session small projects are represented in `tasks/` or documented as existing first-level equivalents.
- Every small project has a project map, a progress record, and `try/`.
- Each special-purpose output folder has a clear owner and purpose in a project map.

## CAD Workspace Notes

- Existing CAD workspaces may already use `output/<task-name>/` as the small-project layer.
- When aligning, either keep `output/<task-name>/` as a documented legacy task layer or create future tasks under `tasks/` and leave old output folders in place.
- Do not split source/export/screenshot sets that already belong together.

## Scraping Workspace Notes

- Existing scraping workspaces may already use first-level target folders.
- Keep scaffold/tooling directories such as `scaffolding/` separate from real data targets.
- Align each target by adding a project map, a progress record, and `try/` when missing.
