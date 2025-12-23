# Todo App Example

A complete task management application showing data structures, state management, and user interaction patterns.

## Features

- Add new tasks
- Mark tasks as complete
- Delete completed tasks
- View statistics
- Input validation

## Complete Code

```python
"""
Todo List Application
A complete task management app built with Graphica
"""

import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

# Data storage - list of dictionaries
tasks = []

# === UI Layout ===

# Title
gui.Label(app, "My Todo List", x=210, y=20, size=18)

# Input section
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)

# Display section
gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

# Actions section
gui.Label(app, "Task #:", x=50, y=530, size=11)
task_number = gui.Input(app, x=110, y=530, width=50)

# Statistics
stats_label = gui.Label(app, "No tasks yet", x=50, y=560, size=10)

# === Functions ===

def add_task():
    """Add a new task to the list"""
    task = task_input.get()
    
    # Validate input
    if not task.strip():
        gui.alert("Please enter a task!", "Empty Task")
        return
    
    # Add to task list
    tasks.append({"text": task, "done": False})
    
    # Clear input and update display
    task_input.clear()
    update_display()

def complete_task():
    """Mark a task as complete"""
    num = task_number.get()
    
    # Validate number
    if not num.isdigit():
        gui.alert("Please enter a valid task number", "Invalid Number")
        return
    
    index = int(num) - 1
    
    # Check if task exists
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        task_number.clear()
        update_display()
        gui.alert(f"Task {num} marked as complete!", "Success")
    else:
        gui.alert(f"Task {num} doesn't exist", "Not Found")

def delete_completed():
    """Remove all completed tasks"""
    global tasks
    
    completed_count = sum(1 for task in tasks if task["done"])
    
    if completed_count == 0:
        gui.alert("No completed tasks to delete", "Nothing to Delete")
        return
    
    # Confirm before deleting
    if gui.confirm(f"Delete {completed_count} completed task(s)?", "Confirm Delete"):
        tasks = [task for task in tasks if not task["done"]]
        update_display()
        gui.alert(f"Deleted {completed_count} task(s)", "Deleted")

def update_display():
    """Refresh the task display and statistics"""
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        stats_label.set("No tasks yet")
        return
    
    # Build task list with status icons
    display_text = ""
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        display_text += f"{i}. {status} {task['text']}\n"
    
    task_display.set(display_text)
    
    # Calculate and show statistics
    total = len(tasks)
    completed = sum(1 for task in tasks if task["done"])
    remaining = total - completed
    
    stats_label.set(f"Total: {total} | Completed: {completed} | Remaining: {remaining}")

# === Buttons ===

gui.Button(app, "Add Task", command=add_task, x=230, y=135)
gui.Button(app, "Complete", command=complete_task, x=170, y=527)
gui.Button(app, "Delete Completed", command=delete_completed, x=270, y=527)

# Run the application
app.run()
```

## How It Works

### Data Structure

Tasks are stored as dictionaries in a list:

```python
tasks = [
    {"text": "Buy groceries", "done": False},
    {"text": "Write report", "done": True},
    {"text": "Call dentist", "done": False}
]
```

This structure allows us to:
- Track task text and completion status
- Easily iterate through tasks
- Filter completed vs incomplete tasks

### Adding Tasks

```python
def add_task():
    task = task_input.get()
    
    if not task.strip():  # Validate
        gui.alert("Please enter a task!", "Empty Task")
        return
    
    tasks.append({"text": task, "done": False})  # Add
    task_input.clear()  # Clear input
    update_display()  # Refresh UI
```

Key points:
- **Validation first** - check for empty input
- **Structured data** - consistent format
- **Clear feedback** - user sees the result immediately

### Completing Tasks

```python
def complete_task():
    num = task_number.get()
    
    if not num.isdigit():
        gui.alert("Please enter a valid task number", "Invalid Number")
        return
    
    index = int(num) - 1  # Convert to 0-based index
    
    if 0 <= index < len(tasks):  # Check bounds
        tasks[index]["done"] = True
        update_display()
```

Key points:
- **Input validation** - ensure it's a number
- **Bounds checking** - prevent index errors
- **User-friendly numbering** - display 1-based, store 0-based

### Deleting Completed Tasks

```python
def delete_completed():
    global tasks
    
    completed_count = sum(1 for task in tasks if task["done"])
    
    if completed_count == 0:
        gui.alert("No completed tasks to delete", "Nothing to Delete")
        return
    
    if gui.confirm(f"Delete {completed_count} completed task(s)?", "Confirm Delete"):
        tasks = [task for task in tasks if not task["done"]]
        update_display()
```

Key points:
- **Count first** - know what you're deleting
- **Confirm destructive actions** - always ask
- **List comprehension** - filter efficiently

### Updating the Display

```python
def update_display():
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        stats_label.set("No tasks yet")
        return
    
    # Build display text
    display_text = ""
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        display_text += f"{i}. {status} {task['text']}\n"
    
    task_display.set(display_text)
    
    # Update statistics
    total = len(tasks)
    completed = sum(1 for task in tasks if task["done"])
    remaining = total - completed
    
    stats_label.set(f"Total: {total} | Completed: {completed} | Remaining: {remaining}")
```

Key points:
- **Single source of truth** - one function updates everything
- **Visual feedback** - icons show status
- **Statistics** - provide useful information

## Key Learning Points

### 1. Data Modeling

Using dictionaries for tasks:
```python
# Good structure
{"text": "Task description", "done": False}

# vs just strings
"Task description"  # Can't track completion status
```

### 2. List Operations

Common patterns used:

```python
# Add item
tasks.append(new_task)

# Filter list
active_tasks = [t for t in tasks if not t["done"]]

# Count matching items
completed = sum(1 for t in tasks if t["done"])

# Enumerate with custom start
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task['text']}")
```

### 3. Input Validation

Always validate before using input:

```python
# Check not empty
if not value.strip():
    return

# Check is digit
if not value.isdigit():
    return

# Check in range
if not (0 <= index < len(tasks)):
    return
```

### 4. User Feedback

Multiple ways to provide feedback:

```python
# Success alerts
gui.alert("Task added!", "Success")

# Error alerts
gui.alert("Invalid input", "Error")

# Confirmation dialogs
if gui.confirm("Delete?", "Confirm"):
    # proceed

# Status labels
status.set("Processing...")
```

## Possible Enhancements

### 1. Priority Levels

```python
tasks.append({
    "text": task,
    "done": False,
    "priority": "high"  # high, medium, low
})
```

### 2. Due Dates

```python
from datetime import datetime

tasks.append({
    "text": task,
    "done": False,
    "due_date": datetime(2024, 12, 31)
})
```

### 3. Categories

```python
tasks.append({
    "text": task,
    "done": False,
    "category": "work"  # work, personal, shopping, etc.
})
```

### 4. Save to File

```python
import json

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# At startup
tasks = load_tasks()
```

### 5. Edit Existing Tasks

```python
def edit_task():
    num = task_number.get()
    new_text = task_input.get()
    
    if num.isdigit() and new_text:
        index = int(num) - 1
        if 0 <= index < len(tasks):
            tasks[index]["text"] = new_text
            update_display()
```

### 6. Sort Tasks

```python
def sort_by_status():
    global tasks
    # Incomplete tasks first
    tasks.sort(key=lambda t: t["done"])
    update_display()

def sort_alphabetically():
    global tasks
    tasks.sort(key=lambda t: t["text"].lower())
    update_display()
```

### 7. Search/Filter

```python
search_input = gui.Input(app, x=50, y=540, width=200)

def search_tasks():
    query = search_input.get().lower()
    
    if not query:
        update_display()
        return
    
    matching = [t for t in tasks if query in t["text"].lower()]
    
    # Display only matching tasks
    if matching:
        display_text = ""
        for i, task in enumerate(matching, 1):
            status = "✓" if task["done"] else "○"
            display_text += f"{i}. {status} {task['text']}\n"
        task_display.set(display_text)
    else:
        task_display.set("No matching tasks found")
```

## Design Patterns Used

### Single Responsibility

Each function does one thing:
- `add_task()` - adds tasks
- `complete_task()` - marks complete
- `update_display()` - updates UI
- `delete_completed()` - removes tasks

### DRY (Don't Repeat Yourself)

`update_display()` is called everywhere we change data, rather than duplicating display logic.

### Input Validation Pattern

```python
def process_input():
    # 1. Get input
    value = input_field.get()
    
    # 2. Validate
    if not valid(value):
        show_error()
        return
    
    # 3. Process
    do_something(value)
    
    # 4. Update UI
    update_display()
```

## Common Mistakes to Avoid

### Forgetting to Update Display

```python
# ❌ Bad
def add_task():
    tasks.append({"text": task, "done": False})
    # Forgot to call update_display()

# ✅ Good
def add_task():
    tasks.append({"text": task, "done": False})
    update_display()
```

### Not Validating Input

```python
# ❌ Bad
def complete_task():
    index = int(task_number.get()) - 1
    tasks[index]["done"] = True  # Crashes on invalid input

# ✅ Good
def complete_task():
    num = task_number.get()
    if not num.isdigit():
        return
    index = int(num) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
```

### Forgetting Global Keyword

```python
# ❌ Bad
def delete_completed():
    tasks = [t for t in tasks if not t["done"]]  # Creates local variable

# ✅ Good
def delete_completed():
    global tasks
    tasks = [t for t in tasks if not t["done"]]
```

## See Also

- [Calculator Example](calculator.md) - Button grid and operations
- [Text Editor Example](text-editor.md) - File operations
- [First App Tutorial](../getting-started/first-app.md) - Step-by-step building
- [Event Handling Guide](../guide/events.md) - Understanding event patterns