# Task Manager - Feature branch merge exercise

A beginner-friendly Python command-line app for keeping a small personal task list. Tasks are saved in `tasks.json` beside the program.

## Requirements

- Python 3.10 or later
- No third-party packages

## Run it

Open this folder in PyCharm, then use its Run configuration or the built-in terminal:

```bash
python task_manager.py add "Finish Unit 3 homework"
python task_manager.py list
python task_manager.py list --pending
python task_manager.py done 1
```

Use `list --pending` to show unfinished tasks only. Run `python task_manager.py --help` to see all commands. Task titles must not be blank, and completing an unknown task ID displays an error.

## Project files

- `task_manager.py` - command-line interface, input validation, and JSON persistence
- `tasks.json` - created automatically after the first task is added
