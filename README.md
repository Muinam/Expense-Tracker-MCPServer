# Expense Tracker MCP Server

A FastMCP server that exposes expense-tracking tools backed by a local SQLite database.

## What It Does

Runs an MCP server (`FastMCP`) named **"Expense Tracker"** that stores and queries expenses in `expence_tracker.db`, auto-created on startup.

### Tools

| Tool | Description |
|---|---|
| `add_expense(date, amount, category, subcategory="", note="")` | Inserts a new expense row, returns `{status, id}` |
| `list_expenses(start_date, end_date)` | Returns all expenses in an inclusive date range |
| `summarize(start_date, end_date, category=None)` | Returns total amount grouped by category, optionally filtered to one category |

### Resource

- `expense://categories` — serves the contents of `categories.json` (read fresh on every request, so edits don't require a restart)

## Requirements

```bash
pip install fastmcp
```

Place a `categories.json` file next to the script (referenced by `categories()` but not created automatically).

## Running

```bash
python main.py
```

Starts an HTTP MCP server on `0.0.0.0:8000`.