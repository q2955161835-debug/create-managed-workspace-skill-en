"""Validate a standard managed workspace structure."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_FILES = [
    "AGENTS.md",
    ".gitignore",
    ".env.example",
    "docs/project-map.md",
    "docs/task-index.md",
    "docs/progress.md",
    "tasks/README.md",
]

ROOT_DIRS = ["docs", "skills", "tasks", "output", "try"]
TASK_PATHS = [
    "README.md",
    "docs/project-map.md",
    "docs/progress.md",
    "input",
    "work",
    "output",
    "try",
]


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.exists():
        return [f"Workspace does not exist: {root}"]

    for rel in ROOT_FILES:
        if not (root / rel).is_file():
            errors.append(f"Missing required file: {rel}")
    for rel in ROOT_DIRS:
        if not (root / rel).is_dir():
            errors.append(f"Missing required directory: {rel}")

    agents = root / "AGENTS.md"
    if agents.exists():
        text = agents.read_text(encoding="utf-8", errors="replace")
        for phrase in ["Task Ownership", "skills/", "try/", ".env.example"]:
            if phrase not in text:
                errors.append(f"AGENTS.md missing required rule: {phrase}")

    tasks = root / "tasks"
    if tasks.is_dir():
        for task in sorted(p for p in tasks.iterdir() if p.is_dir()):
            for rel in TASK_PATHS:
                target = task / rel
                if "." in Path(rel).name:
                    if not target.is_file():
                        errors.append(f"{task.name} missing required file: {rel}")
                elif not target.is_dir():
                    errors.append(f"{task.name} missing required directory: {rel}")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Workspace root to validate")
    args = parser.parse_args()

    errors = validate(Path(args.path).resolve())
    if errors:
        for error in errors:
            print(f"FAIL\t{error}")
        sys.exit(1)
    print("OK\tWorkspace structure check passed")


if __name__ == "__main__":
    main()
