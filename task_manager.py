"""A small command-line task manager that stores tasks in a JSON file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks() -> list[dict[str, object]]:
    """Load saved tasks, returning an empty list on first run."""
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read {DATA_FILE.name}: {exc}") from exc
    if not isinstance(data, list):
        raise RuntimeError(f"{DATA_FILE.name} must contain a JSON list.")
    return data


def save_tasks(tasks: list[dict[str, object]]) -> None:
    """Save tasks as readable UTF-8 JSON."""
    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def add_task(title: str) -> None:
    """Add one task after validating its title."""
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    tasks = load_tasks()
    task_id = max((int(task["id"]) for task in tasks), default=0) + 1
    tasks.append({"id": task_id, "title": title, "done": False})
    save_tasks(tasks)
    print(f"Added task {task_id}: {title}")


def list_tasks() -> None:
    """Print all tasks, or a helpful message when none exist."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python task_manager.py add \"Your task\"")
        return
    for task in tasks:
        marker = "x" if task.get("done") else " "
        print(f"[{marker}] {task['id']}: {task['title']}")


def complete_task(task_id: int) -> None:
    """Mark a task complete by its numeric ID."""
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Completed task {task_id}.")
            return
    raise ValueError(f"Task {task_id} was not found.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a small personal task list.")
    commands = parser.add_subparsers(dest="command", required=True)
    add_parser = commands.add_parser("add", help="add a new task")
    add_parser.add_argument("title", help="task description")
    commands.add_parser("list", help="show all tasks")
    done_parser = commands.add_parser("done", help="mark a task complete")
    done_parser.add_argument("id", type=int, help="numeric task ID")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "add":
            add_task(args.title)
        elif args.command == "list":
            list_tasks()
        elif args.command == "done":
            complete_task(args.id)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
