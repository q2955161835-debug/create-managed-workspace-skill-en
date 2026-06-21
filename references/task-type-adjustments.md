# Task Type Adjustments

Use the standard workspace and task structure first. Add task-specific folders only when the task needs them, then document each folder in the task `docs/project-map.md`.

## Workspace Kind

- Use `multi-task` for general workspaces that contain many unrelated projects. Do not create or require root `skills/`.
- Use `specialized` for a dedicated task-type workspace such as CAD, scraping, automation, or research when common skills, wrappers, or skill entrypoints should live with the workspace. Only this kind gets root `skills/`.
- If a specialized workspace uses external skills instead of copied skills, root `skills/` may contain junctions, wrappers, README files, or `.gitkeep`; document the real external paths in root `docs/project-map.md`.

## CAD

- Keep each CAD task inside `tasks/YYYYMMDD-short-task-name/`.
- Put reference drawings, photos, PDFs, and measurement input in `input/`.
- Put CAD source scripts, intermediate models, and draft geometry checks in `work/`.
- Put final source, STEP/STL/3MF/GLB/DXF/DWG exports, screenshots, and verification notes in `output/`.
- Use the task `try/` for disposable geometry experiments.
- Use root `skills/` only when the CAD workspace is a specialized task-type workspace. Store workspace-specific copies, wrappers, or junction entrypoints there; otherwise record external paths in the task or root `docs/project-map.md`.

## Scraping

- Keep each scraping target inside `tasks/YYYYMMDD-short-task-name/`.
- Add `raw-data/`, `raw-files/`, `old-data/`, `clean-data/`, `evidence-screenshots/`, and `reports/` only when needed.
- Put variable confirmation tables and field definitions under the task `docs/` or task root.
- Maintain `docs/task-list.md` when multiple URLs, files, APIs, or source channels need dedupe tracking.
- Keep raw structured crawl outputs in `raw-data/` and downloaded files or snapshots in `raw-files/`.
- Put temporary fetch tests and parser experiments in the task `try/`.
- Use root `skills/` only for a specialized scraping workspace with reusable crawlers, extraction skills, or documented entrypoints. General multi-task workspaces that happen to include scraping tasks should not add root `skills/`.

## Research, Writing, and Automation

- Put source files and prompts in `input/`.
- Put drafts, scripts, notebooks, and intermediate reports in `work/`.
- Put final deliverables in `output/`.
- Put throwaway probes, one-off conversion tests, and temporary scripts in `try/`.
