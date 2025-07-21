# Task Manager CLI

A lightweight and simple command-line tool to help you manage your daily tasks.  
All data is stored locally in a `tasks.json` file — no internet or cloud needed!

## Features

- Add, update, and delete tasks.
- List all tasks or filter by status (`todo`, `done`, `in-progress`).
- Mark tasks as (`todo`, `done`, `in-progress`).
- Local JSON storage (no external dependencies).

## Requirements

- Python 3.8 or higher  
- No external libraries required

## How to Run

In your terminal, navigate to the project folder and run:

```bash
python main.py
```

## 🛠Usage

After starting the app, you can use the following commands:

### Add a Task

```bash
add 'Study Python'
```
**Output:**
```
'Study Python' added successfully (ID: 1)
```

### Update a Task

```bash
update 1 'Study C++'
```
**Output:**
```
'Study Python' changed successfully to 'Study C++'
```

### Delete a Task

```bash
delete 1
```
**Output:**
```
'Study C++' deleted successfully.
```

### Mark a Task as Done

```bash
mark 1 done
```
**Output:**
```
'Study Python' status changed from 'Todo' to 'Done'
```

### 📋 List Tasks

```bash
list
```
**Output:**
```
All tasks
```

```bash
list done
```
**Output:**
```
Tasks marked as 'Done'
```

```bash
list todo
```
**Output:**
```
Tasks still marked as 'Todo'
```

```bash
s
```
**Output:**
```
Saves the progress
```

```bash
q
```
**Output:**
```
Quits the program
```

## 👤 Author

Created by jamnihil-py
Feel free to fork, suggest changes, or submit issues.