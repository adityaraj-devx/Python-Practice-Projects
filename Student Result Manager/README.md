# Student Result Manager

## Overview
Student Result Manager is a simple command-line application that allows users to store and manage student records. Users can add students, view all students, and check individual student results. Data is stored in a JSON file for persistence.

## Features
- Add new students and their marks
- View all registered students
- Search for a student's result by name
- Store data in a JSON file
- Simple menu-driven interface

## Requirements
- Python 3

## Project Structure

```text
Student Result Manager/
│
├── main.py
├── rsm.json
└── README.md
```

## Run

```bash
python main.py
```

## Menu Options

```text
1. View Students
2. Add Student
3. Check Result
4. Exit
```

## Example

### Add Student

```text
Enter the name of the student: Piyush
Enter the marks of the student: 80

Student added.
```

### Check Result

```text
Enter the name of the student: Piyush

Name - Piyush | Marks - 80
```

## Data Format

Student records are stored in JSON format:

```json
{
    "students": [
        {
            "Name": "Piyush",
            "marks": "80"
        },
        {
            "Name": "Aditya",
            "marks": "95"
        }
    ]
}
```

## Learning Concepts

This project demonstrates:

- Functions
- Lists and dictionaries
- JSON file handling
- Data persistence
- Searching records
- Exception handling
- Menu-driven applications