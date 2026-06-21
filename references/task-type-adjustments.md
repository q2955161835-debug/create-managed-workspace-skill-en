# Task Type Adjustments

Use the standard workspace and task structure first. Add task-specific folders only when the task needs them, then document each folder in the task `docs/project-map.md`.

## CAD

- Keep each CAD task inside `tasks/YYYYMMDD-short-task-name/`.
- Put reference drawings, photos, PDFs, and measurement input in `input/`.
- Put CAD source scripts, intermediate models, and draft geometry checks in `work/`.
- Put final source, STEP/STL/3MF/GLB/DXF/DWG exports, screenshots, and verification notes in `output/`.
- Use the task `try/` for disposable geometry experiments.
- Store commonly used CAD skills in root `skills/` only when they are workspace-specific copies; otherwise record external paths in the task or root `docs/project-map.md`.

## Scraping

- Keep each scraping target inside `tasks/YYYYMMDD-short-task-name/`.
- Add `raw-data/`, `raw-files/`, `old-data/`, `clean-data/`, `evidence-screenshots/`, and `reports/` only when needed.
- Put variable confirmation tables and field definitions under the task `docs/` or task root.
- Maintain `docs/task-list.md` when multiple URLs, files, APIs, or source channels need dedupe tracking.
- Keep raw structured crawl outputs in `raw-data/` and downloaded files or snapshots in `raw-files/`.
- Put temporary fetch tests and parser experiments in the task `try/`.

## Research, Writing, and Automation

- Put source files and prompts in `input/`.
- Put drafts, scripts, notebooks, and intermediate reports in `work/`.
- Put final deliverables in `output/`.
- Put throwaway probes, one-off conversion tests, and temporary scripts in `try/`.
