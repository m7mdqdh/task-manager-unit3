# Changelog

## Pending task filter

- Added `task_manager.py list --pending` to display unfinished tasks only.
- Kept the default `list` output unchanged so completed tasks remain visible unless the filter is requested.
- When no unfinished items remain, the filtered view reports `No pending tasks.`
