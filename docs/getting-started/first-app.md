# Your First App

Let's build a complete todo list application from scratch. This tutorial will teach you everything you need to know about building real Graphica applications.

## What We're Building

A todo list app where users can:
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete completed tasks
- See task statistics

## Step 1: Create the Window

Start with a new file called `todo_app.py`:

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

app.run()
```

Run it to make sure it works: `python todo_app.py`

You should see an empty window. Perfect!

## Step 2: Add the Title

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

# Title at the top
gui.Label(app, "My Todo List", x=210, y=20, size=18)

app.run()
```

## Step 3: Add Input for New Tasks

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

gui.Label(app, "My Todo List", x=210, y=20, size=18)

# Input section
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)

app.run()
```

## Step 4: Add the Display Area

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

gui.Label(app, "My Todo List", x=210, y=20, size=18)

# Input section
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)

# Task display area
gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

app.run()
```

Looking good! Now for the functionality.

## Step 5: Store Tasks

Add a list to store our tasks:

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

# Store tasks here
tasks = []

gui.Label(app, "My Todo List", x=210, y=20, size=18)
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)
gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

app.run()
```

## Step 6: Add Tasks Function

Create a function to add new tasks:

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

tasks = []

gui.Label(app, "My Todo List", x=210, y=20, size=18)
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)
gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

def add_task():
    """Add a new task to the list"""
    task = task_input.get()
    
    # Check if input is not empty
    if task.strip():
        # Add to our list
        tasks.append({"text": task, "done": False})
        
        # Clear the input
        task_input.clear()
        
        # Update the display
        update_display()
    else:
        gui.alert("Please enter a task!", "Empty Task")

def update_display():
    """Refresh the task display"""
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        return
    
    # Build the display text
    display_text = ""
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        display_text += f"{i}. {status} {task['text']}\n"
    
    task_display.set(display_text)

app.run()
```

## Step 7: Add the Add Button

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

tasks = []

gui.Label(app, "My Todo List", x=210, y=20, size=18)
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)

# Add button here
gui.Button(app, "Add Task", command=add_task, x=230, y=135)

gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

def add_task():
    task = task_input.get()
    
    if task.strip():
        tasks.append({"text": task, "done": False})
        task_input.clear()
        update_display()
    else:
        gui.alert("Please enter a task!", "Empty Task")

def update_display():
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        return
    
    display_text = ""
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        display_text += f"{i}. {status} {task['text']}\n"
    
    task_display.set(display_text)

app.run()
```

Try it out! You can now add tasks to your list.

## Step 8: Mark Tasks Complete

Add functionality to complete tasks:

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

tasks = []

gui.Label(app, "My Todo List", x=210, y=20, size=18)
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)
gui.Button(app, "Add Task", command=add_task, x=230, y=135)

gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

# Task number input
gui.Label(app, "Task #:", x=50, y=530, size=11)
task_number = gui.Input(app, x=110, y=530, width=50)

def add_task():
    task = task_input.get()
    
    if task.strip():
        tasks.append({"text": task, "done": False})
        task_input.clear()
        update_display()
    else:
        gui.alert("Please enter a task!", "Empty Task")

def complete_task():
    """Mark a task as complete"""
    num = task_number.get()
    
    if not num.isdigit():
        gui.alert("Please enter a valid task number", "Invalid Number")
        return
    
    index = int(num) - 1
    
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        task_number.clear()
        update_display()
        gui.alert(f"Task {num} marked as complete!", "Success")
    else:
        gui.alert(f"Task {num} doesn't exist", "Not Found")

def update_display():
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        return
    
    display_text = ""
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        display_text += f"{i}. {status} {task['text']}\n"
    
    task_display.set(display_text)

# Add the complete button
gui.Button(app, "Complete", command=complete_task, x=170, y=527)

app.run()
```

## Step 9: Delete Completed Tasks

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

tasks = []

gui.Label(app, "My Todo List", x=210, y=20, size=18)
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)
gui.Button(app, "Add Task", command=add_task, x=230, y=135)

gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

gui.Label(app, "Task #:", x=50, y=530, size=11)
task_number = gui.Input(app, x=110, y=530, width=50)
gui.Button(app, "Complete", command=complete_task, x=170, y=527)

def add_task():
    task = task_input.get()
    
    if task.strip():
        tasks.append({"text": task, "done": False})
        task_input.clear()
        update_display()
    else:
        gui.alert("Please enter a task!", "Empty Task")

def complete_task():
    num = task_number.get()
    
    if not num.isdigit():
        gui.alert("Please enter a valid task number", "Invalid Number")
        return
    
    index = int(num) - 1
    
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
    
    if gui.confirm(f"Delete {completed_count} completed task(s)?", "Confirm Delete"):
        tasks = [task for task in tasks if not task["done"]]
        update_display()
        gui.alert(f"Deleted {completed_count} task(s)", "Deleted")

def update_display():
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        return
    
    display_text = ""
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        display_text += f"{i}. {status} {task['text']}\n"
    
    task_display.set(display_text)

# Add delete button
gui.Button(app, "Delete Completed", command=delete_completed, x=270, y=527)

app.run()
```

## Step 10: Add Statistics

Final touch - show some statistics:

```python
import Graphica as gui

app = gui.Window("Todo List", width=550, height=600)

tasks = []

gui.Label(app, "My Todo List", x=210, y=20, size=18)
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)
gui.Button(app, "Add Task", command=add_task, x=230, y=135)

gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

gui.Label(app, "Task #:", x=50, y=530, size=11)
task_number = gui.Input(app, x=110, y=530, width=50)
gui.Button(app, "Complete", command=complete_task, x=170, y=527)
gui.Button(app, "Delete Completed", command=delete_completed, x=270, y=527)

# Statistics label
stats_label = gui.Label(app, "No tasks yet", x=50, y=560, size=10)

def add_task():
    task = task_input.get()
    
    if task.strip():
        tasks.append({"text": task, "done": False})
        task_input.clear()
        update_display()
    else:
        gui.alert("Please enter a task!", "Empty Task")

def complete_task():
    num = task_number.get()
    
    if not num.isdigit():
        gui.alert("Please enter a valid task number", "Invalid Number")
        return
    
    index = int(num) - 1
    
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        task_number.clear()
        update_display()
        gui.alert(f"Task {num} marked as complete!", "Success")
    else:
        gui.alert(f"Task {num} doesn't exist", "Not Found")

def delete_completed():
    global tasks
    
    completed_count = sum(1 for task in tasks if task["done"])
    
    if completed_count == 0:
        gui.alert("No completed tasks to delete", "Nothing to Delete")
        return
    
    if gui.confirm(f"Delete {completed_count} completed task(s)?", "Confirm Delete"):
        tasks = [task for task in tasks if not task["done"]]
        update_display()
        gui.alert(f"Deleted {completed_count} task(s)", "Deleted")

def update_display():
    """Refresh the display and statistics"""
    if not tasks:
        task_display.set("No tasks yet. Add one above!")
        stats_label.set("No tasks yet")
        return
    
    # Build task list
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

app.run()
```

## Complete Application

Here's the final, complete code:

```python
"""
Todo List Application
A complete task management app built with Graphica
"""

import Graphica as gui

# Create the main window
app = gui.Window("Todo List", width=550, height=600)

# Data storage
tasks = []

# Title
gui.Label(app, "My Todo List", x=210, y=20, size=18)

# Input section
gui.Label(app, "Add a new task:", x=50, y=70, size=12)
task_input = gui.Input(app, x=50, y=95, width=400)
gui.Button(app, "Add Task", command=lambda: add_task(), x=230, y=135)

# Display section
gui.Label(app, "Your tasks:", x=50, y=180, size=12)
task_display = gui.TextArea(app, x=50, y=210, width=450, height=300)

# Actions section
gui.Label(app, "Task #:", x=50, y=530, size=11)
task_number = gui.Input(app, x=110, y=530, width=50)
gui.Button(app, "Complete", command=lambda: complete_task(), x=170, y=527)
gui.Button(app, "Delete Completed", command=lambda: delete_completed(), x=270, y=527)

# Statistics
stats_label = gui.Label(app, "No tasks yet", x=50, y=560, size=10)

def add_task():
    """Add a new task to the list"""
    task = task_input.get()
    
    if task.strip():
        tasks.append({"text": task, "done": False})
        task_input.clear()
        update_display()
    else:
        gui.alert("Please enter a task!", "Empty Task")

def complete_task():
    """Mark a task as complete"""
    num = task_number.get()
    
    if not num.isdigit():
        gui.alert("Please enter a valid task number", "Invalid Number")
        return
    
    index = int(num) - 1
    
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
    
    # Build task list
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

# Run the application
app.run()
```

## What You Learned

Congratulations! You just built a complete, functional application. You learned:

- ✅ Creating windows and layouts
- ✅ Using inputs and text areas
- ✅ Handling button clicks
- ✅ Managing application state
- ✅ Validating user input
- ✅ Updating displays dynamically
- ✅ Using confirmation dialogs
- ✅ Working with lists and data structures

## Next Steps

Now that you've built your first app, try enhancing it:

1. **Save tasks to a file** so they persist between runs
2. **Add due dates** for tasks
3. **Priority levels** (high, medium, low)
4. **Search functionality** to find specific tasks
5. **Edit existing tasks** instead of just adding new ones

## See Also

- [Calculator Example](../examples/calculator.md) - Another complete app
- [Text Editor Example](../examples/text-editor.md) - File operations
- [Best Practices Guide](../guide/best-practices.md) - Write better code