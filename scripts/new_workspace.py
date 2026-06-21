"""Create a managed workspace."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


ROOT_DIRS = ["docs", "tasks", "output", "try"]
ROOT_KEEP_DIRS = ["output", "try"]
WORKSPACE_KINDS = ("multi-task", "specialized")


def now_minute() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


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


def maybe_git_init(root: Path) -> None:
    if (root / ".git").exists():
        return
    subprocess.run(["git", "init"], cwd=root, check=True)
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "chore: baseline managed workspace"], cwd=root, check=True)


def workspace_agents(name: str, workspace_kind: str) -> str:
    skills_rule = (
        "- Root `skills/` stores commonly used skills for this specialized task-type workspace. It starts empty.\n"
        if workspace_kind == "specialized"
        else "- General multi-task workspaces do not create root `skills/` by default. Add it only when converting to a specialized task-type workspace.\n"
    )
    return f"""# {name} Workspace Rules

## Task Ownership
- Before starting work that creates files, spans sessions, or leaves multiple artifacts, check `docs/task-index.md` for an existing task.
- If the work belongs to an existing task, continue in that task directory.
- For a new complex task, create `tasks/YYYYMMDD-short-task-name/` and register it in the task index.
- Do not register simple Q&A, one-off searches, or sessions that produce no files.

## Task Directories
- Each task directory contains `README.md`, `docs/project-map.md`, `docs/progress.md`, `input/`, `work/`, `output/`, and `try/`.
- `README.md` records the goal, current status, key decisions, and next step.
- `docs/project-map.md` records long-lived task information, directory responsibilities, entry points, dependencies, and data flow.
- `docs/progress.md` records task-level progress.
- `try/` stores test, debugging, and temporary validation files. Clearing it must not affect formal results.

## Workspace Directories
{skills_rule.rstrip()}
- Root `try/` is only for workspace-level one-off debugging and tests.
- Root `output/` may keep historical deliverables. New task outputs should prefer `tasks/.../output/`.

## Progress Records
- Sessions with task directories record detailed progress in the task `docs/progress.md`.
- Root `docs/progress.md` keeps only a short workspace-level summary: time, task name/path, and core result.
- Before high-risk operations, update progress records and state the rollback plan.

## Environment Ledger
- `.env` is the real ledger for sensitive local configuration, must be ignored by `.gitignore`, and must not be committed.
- `.env.example` is the example ledger and may contain only variable names, placeholder values, examples, and necessary notes.
"""


def create_workspace(root: Path, name: str, overwrite: bool, init_git: bool, workspace_kind: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    root_dirs = list(ROOT_DIRS)
    root_keep_dirs = list(ROOT_KEEP_DIRS)
    if workspace_kind == "specialized":
        root_dirs.append("skills")
        root_keep_dirs.append("skills")

    for folder in root_dirs:
        (root / folder).mkdir(parents=True, exist_ok=True)
    for folder in root_keep_dirs:
        touch_keep(root / folder)

    stamp = now_minute()
    write_file(root / "AGENTS.md", workspace_agents(name, workspace_kind), overwrite)
    write_file(
        root / ".gitignore",
        """.env
.venv/
__pycache__/
*.pyc
.pytest_cache/
try/**
!try/
!try/.gitkeep
tasks/*/try/**
!tasks/*/try/
!tasks/*/try/.gitkeep
""",
        overwrite,
    )
    write_file(
        root / ".env.example",
        """# Environment variable example ledger
# Store variable names, placeholders, and notes only. Never write real secrets, tokens, cookies, database passwords, or private endpoints here.
""",
        overwrite,
    )
    write_file(
        root / "docs" / "project-map.md",
        f"""# Project Map

## Goal
- `{name}` is a managed workspace for cross-session tasks, small projects, artifacts, and rules.

## Directory Responsibilities
- `AGENTS.md`: workspace rules.
- `docs/task-index.md`: cross-session task index.
- `docs/progress.md`: workspace-level progress summary.
- `docs/project-map.md`: long-lived workspace information.
{"- `skills/`: common skills for a specialized task-type workspace; empty at creation time." if workspace_kind == "specialized" else "- General multi-task workspaces do not create `skills/` by default. Add it later only when converting to a specialized task-type workspace."}
- `tasks/`: small project directories.
- `output/`: historical or workspace-level deliverables.
- `try/`: workspace-level test, debugging, and temporary validation files.

## Workspace Kind
- {workspace_kind}

## Environment Ledger
- `.env`: real sensitive local configuration, ignored and never committed.
- `.env.example`: variable names and placeholder notes.

## Created
- {stamp}
""",
        overwrite,
    )
    write_file(
        root / "docs" / "task-index.md",
        """# Task Index

Use this file to answer: which cross-session tasks exist, where they are, what they produced, and what should happen next. Do not register simple Q&A, one-off searches, or sessions that produce no files.

| Task ID | Task Name | Status | Last Session Time | Task Directory | Final Output | Next Step |
| --- | --- | --- | --- | --- | --- | --- |

## Status Values
- `in progress`: work is currently active.
- `needs confirmation`: user input or scope confirmation is required.
- `complete`: the stage goal is complete and outputs are recorded.
- `paused`: work is intentionally paused but context is preserved.
""",
        overwrite,
    )
    write_file(
        root / "docs" / "progress.md",
        f"""# Progress

## {stamp} ~ {stamp}
- Completed: created the standard managed workspace structure.
- Added/modified/generated files and purpose: `AGENTS.md`, `.gitignore`, `.env.example`, `docs/`, {"`skills/`, " if workspace_kind == "specialized" else ""}`tasks/`, `output/`, `try/`.
- Errors: none.
""",
        overwrite,
    )
    write_file(
        root / "tasks" / "README.md",
        """# tasks

Each small project uses `YYYYMMDD-short-task-name/` and contains `README.md`, `docs/project-map.md`, `docs/progress.md`, `input/`, `work/`, `output/`, and `try/`.
""",
        overwrite,
    )
    if init_git:
        maybe_git_init(root)
    return root


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Workspace root path to create")
    parser.add_argument("--name", help="Human-readable workspace name")
    parser.add_argument(
        "--workspace-kind",
        choices=WORKSPACE_KINDS,
        default="multi-task",
        help="multi-task creates no root skills directory; specialized creates root skills directory",
    )
    parser.add_argument(
        "--specialized",
        action="store_true",
        help="Shortcut for --workspace-kind specialized",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing managed files")
    parser.add_argument("--init-git", action="store_true", help="Initialize Git and create a baseline commit if needed")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    name = args.name or root.name
    workspace_kind = "specialized" if args.specialized else args.workspace_kind
    created = create_workspace(root, name, args.overwrite, args.init_git, workspace_kind)
    print(created)


if __name__ == "__main__":
    main()
