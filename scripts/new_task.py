"""Create a standard task folder inside a managed workspace."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


TASK_DIRS = ["docs", "input", "work", "output", "try"]
KEEP_DIRS = ["input", "work", "output", "try"]


def now_minute() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today() -> str:
    return datetime.now().strftime("%Y%m%d")


def slugify(name: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "-", name.strip())
    cleaned = re.sub(r"\s+", "-", cleaned)
    cleaned = cleaned.strip(".-")
    if not cleaned:
        raise ValueError("Task name cannot be empty after sanitizing")
    return cleaned


def write_file(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def touch_keep(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    keep = path / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")


def create_task(workspace: Path, name: str, task_id: str | None, overwrite: bool) -> Path:
    root = workspace.resolve()
    if not (root / "tasks").exists():
        raise FileNotFoundError(f"Missing tasks directory: {root / 'tasks'}")

    slug = slugify(name)
    final_id = task_id or f"{today()}-{slug}"
    task = root / "tasks" / final_id
    task.mkdir(parents=True, exist_ok=True)
    for folder in TASK_DIRS:
        (task / folder).mkdir(parents=True, exist_ok=True)
    for folder in KEEP_DIRS:
        touch_keep(task / folder)

    stamp = now_minute()
    write_file(
        task / "README.md",
        f"""# {name}

## Goal
- To be filled.

## Current Status
- Needs confirmation.

## Key Decisions
- To be filled.

## Next Step
- To be filled.
""",
        overwrite,
    )
    write_file(
        task / "docs" / "project-map.md",
        f"""# Project Map

## Task Goal
- To be filled: goal, scope, and deliverables for `{name}`.

## Directory Responsibilities
- `README.md`: goal, current status, key decisions, and next step.
- `docs/project-map.md`: long-lived task information.
- `docs/progress.md`: task-level progress.
- `input/`: input materials.
- `work/`: intermediate files, drafts, and scripts.
- `output/`: final deliverables.
- `try/`: test, debugging, and temporary validation files; safe to clean.

## Created
- {stamp}
""",
        overwrite,
    )
    write_file(
        task / "docs" / "progress.md",
        f"""# Progress

## {stamp} ~ {stamp}
- Completed: created the task directory skeleton.
- Added/modified/generated files and purpose: `README.md`, `docs/project-map.md`, `docs/progress.md`, `input/`, `work/`, `output/`, `try/`.
- Errors: none.
""",
        overwrite,
    )
    return task


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", help="Managed workspace root")
    parser.add_argument("name", help="Task display name")
    parser.add_argument("--task-id", help="Explicit task directory name")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing managed files")
    args = parser.parse_args()

    task = create_task(Path(args.workspace), args.name, args.task_id, args.overwrite)
    print(task)


if __name__ == "__main__":
    main()
