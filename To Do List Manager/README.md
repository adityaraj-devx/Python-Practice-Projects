# To-Do List Manager

## Overview
A command-line task management application that allows users to add, view, complete, and delete tasks. Task data is stored in a JSON file so it remains available between sessions.

## Features
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON
- Simple menu-driven interface

## Requirements
- Python 3

## Project Files

- `main.py` - Main application
- `todo.json` - Stores task data

## Run

```bash
python main.py
```

## Menu Options

1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit

## Example Task Format

```json
{
  "tasks": [
    {
      "description": "Complete Python project",
      "complete": false
    }
  ]
}
```

## Learning Concepts

This project demonstrates:
- Functions
- Lists and dictionaries
- JSON file handling
- CRUD operations
- Exception handling
- File persistence