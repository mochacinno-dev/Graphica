# Utilities

Graphica provides two utility functions for displaying dialog boxes: `alert()` for showing messages and `confirm()` for asking yes/no questions.

## alert()

Display an informational message to the user in a popup dialog.

```python
gui.alert(message, title="Alert")
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | str | Required | The message to display |
| `title` | str | "Alert" | The dialog window title |

### Returns

Nothing. The function blocks until the user closes the dialog.

### Examples

```python
import Graphica as gui

# Simple alert
gui.alert("Hello, World!")

# Alert with custom title
gui.alert("File saved successfully!", "Success")

# Multi-line alert
gui.alert("Error occurred:\nFile not found\nPlease try again", "Error")
```

## confirm()

Ask the user a yes/no question and get their response.

```python
result = gui.confirm(message, title="Confirm")
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | str | Required | The question to ask |
| `title` | str | "Confirm" | The dialog window title |

### Returns

- `bool`: `True` if the user clicked "Yes", `False` if they clicked "No"

### Examples

```python
import Graphica as gui

# Simple confirmation
if gui.confirm("Are you sure?"):
    print("User confirmed")
else:
    print("User cancelled")

# Confirmation with custom title
if gui.confirm("Delete this file?", "Confirm Delete"):
    # Delete the file
    pass
```

## Complete Examples

### Success Message

```python
import Graphica as gui

app = gui.Window("Save Example", width=400, height=200)

def save_file():
    # Simulate saving
    gui.alert("Your file has been saved successfully!", "Success")

gui.Button(app, "Save", command=save_file, x=150, y=80)

app.run()
```

### Error Handling

```python
import Graphica as gui

app = gui.Window("Error Example", width=400, height=250)

age_input = gui.Input(app, x=50, y=50, width=300)

def validate_age():
    age_str = age_input.get()
    
    if not age_str:
        gui.alert("Please enter your age", "Missing Input")
        return
    
    if not age_str.isdigit():
        gui.alert("Age must be a number", "Invalid Input")
        return
    
    age = int(age_str)
    if age < 0:
        gui.alert("Age cannot be negative", "Invalid Age")
    elif age < 18:
        gui.alert("You must be 18 or older", "Age Restriction")
    else:
        gui.alert(f"Welcome! You are {age} years old.", "Valid")

gui.Label(app, "Enter your age:", x=50, y=20)
gui.Button(app, "Validate", command=validate_age, x=150, y=90)

app.run()
```

### Delete Confirmation

```python
import Graphica as gui

app = gui.Window("Delete Example", width=400, height=200)

items = ["Document.txt", "Image.png", "Data.csv"]

def delete_item():
    if gui.confirm("Are you sure you want to delete this item?\nThis action cannot be undone.", "Confirm Delete"):
        gui.alert("Item deleted successfully", "Deleted")
    else:
        gui.alert("Delete cancelled", "Cancelled")

gui.Button(app, "Delete", command=delete_item, x=150, y=80)

app.run()
```

### Exit Confirmation

```python
import Graphica as gui

app = gui.Window("Exit Confirmation", width=400, height=200)

def try_exit():
    if gui.confirm("Are you sure you want to exit?", "Exit Application"):
        app.close()
    else:
        gui.alert("Exit cancelled", "Info")

gui.Button(app, "Exit", command=try_exit, x=160, y=80)

app.run()
```

### Form Submission

```python
import Graphica as gui

app = gui.Window("Submission Example", width=450, height=350)

gui.Label(app, "Feedback Form", x=160, y=20, size=16)

gui.Label(app, "Your Name:", x=50, y=70)
name = gui.Input(app, x=50, y=95, width=350)

gui.Label(app, "Feedback:", x=50, y=135)
feedback = gui.TextArea(app, x=50, y=160, width=350, height=100)

def submit_form():
    name_val = name.get()
    feedback_val = feedback.get().strip()
    
    if not name_val or not feedback_val:
        gui.alert("Please fill in all fields", "Incomplete Form")
        return
    
    if gui.confirm(f"Submit feedback as {name_val}?", "Confirm Submission"):
        gui.alert("Thank you for your feedback!", "Success")
        name.clear()
        feedback.clear()

gui.Button(app, "Submit", command=submit_form, x=175, y=280)

app.run()
```

### Multi-step Process

```python
import Graphica as gui

app = gui.Window("Wizard Example", width=450, height=250)

step = 1
status = gui.Label(app, "Step 1 of 3", x=180, y=50, size=14)

def next_step():
    global step
    
    if step == 1:
        gui.alert("Preparing files...", "Step 1")
        step = 2
        status.set("Step 2 of 3")
    elif step == 2:
        gui.alert("Processing data...", "Step 2")
        step = 3
        status.set("Step 3 of 3")
    elif step == 3:
        if gui.confirm("Complete the process?", "Final Step"):
            gui.alert("Process completed successfully!", "Done")
            step = 1
            status.set("Step 1 of 3")

gui.Button(app, "Next", command=next_step, x=185, y=100)

app.run()
```

### Information Display

```python
import Graphica as gui

app = gui.Window("Information", width=400, height=200)

def show_help():
    help_text = """
How to use this application:

1. Enter your data in the fields
2. Click Submit to process
3. View the results

For more help, visit our website.
"""
    gui.alert(help_text, "Help")

def show_about():
    about_text = """
My Application v1.0

Created with Graphica
© 2024 Your Name

All rights reserved.
"""
    gui.alert(about_text, "About")

gui.Button(app, "Help", command=show_help, x=100, y=80)
gui.Button(app, "About", command=show_about, x=200, y=80)

app.run()
```

### Validation Chain

```python
import Graphica as gui

app = gui.Window("Registration", width=450, height=350)

gui.Label(app, "Create Account", x=160, y=20, size=16)

gui.Label(app, "Username:", x=50, y=70)
username = gui.Input(app, x=50, y=95, width=350)

gui.Label(app, "Password:", x=50, y=135)
password = gui.Input(app, x=50, y=160, width=350)

gui.Label(app, "Confirm Password:", x=50, y=200)
confirm_pass = gui.Input(app, x=50, y=225, width=350)

def register():
    user = username.get()
    pwd = password.get()
    confirm = confirm_pass.get()
    
    # Step 1: Check empty fields
    if not user or not pwd or not confirm:
        gui.alert("All fields are required", "Error")
        return
    
    # Step 2: Check username length
    if len(user) < 3:
        gui.alert("Username must be at least 3 characters", "Error")
        return
    
    # Step 3: Check password length
    if len(pwd) < 6:
        gui.alert("Password must be at least 6 characters", "Error")
        return
    
    # Step 4: Check password match
    if pwd != confirm:
        gui.alert("Passwords do not match", "Error")
        return
    
    # Step 5: Final confirmation
    if gui.confirm(f"Create account for {user}?", "Confirm"):
        gui.alert("Account created successfully!", "Success")
        username.clear()
        password.clear()
        confirm_pass.clear()

gui.Button(app, "Register", command=register, x=175, y=275)

app.run()
```

## Usage Tips

### When to Use alert()

- **Success messages**: "File saved successfully"
- **Error messages**: "Invalid input detected"
- **Information**: "Processing complete"
- **Warnings**: "This action cannot be undone"
- **Status updates**: "3 items processed"

### When to Use confirm()

- **Destructive actions**: Deleting, clearing, resetting
- **Important decisions**: Submitting forms, making purchases
- **Exit confirmations**: Closing with unsaved changes
- **Overwriting**: Replacing existing data
- **Final steps**: Completing multi-step processes

### Writing Good Messages

**Be specific and clear:**
```python
# ❌ Not helpful
gui.alert("Error occurred", "Error")

# ✅ Clear and actionable
gui.alert("Could not save file: disk is full", "Save Error")
```

**Use appropriate tone:**
```python
# For errors - clear and direct
gui.alert("Invalid email format. Please include @ and domain.", "Error")

# For success - friendly and positive
gui.alert("Great! Your settings have been saved.", "Success")
```

**Ask clear questions:**
```python
# ❌ Vague
if gui.confirm("Continue?"):

# ✅ Specific
if gui.confirm("Delete all data? This cannot be undone.", "Confirm Delete"):
```

### Multi-line Messages

Use `\n` for line breaks in longer messages:

```python
message = """Operation completed successfully!

Results:
- 15 files processed
- 3 errors found
- 45 seconds elapsed

Check the log for details."""

gui.alert(message, "Complete")
```

## Best Practices

**Don't overuse dialogs.** Too many popups can be annoying. Use in-app labels for less critical feedback.

**Make confirm() questions clear.** Users should immediately understand what "Yes" and "No" mean.

**Keep messages concise.** Users skim dialog text. Get to the point quickly.

**Use appropriate titles.** The title helps users understand the context: "Error", "Success", "Confirm", etc.

**Handle both outcomes.** When using confirm(), always handle both True and False cases.

```python
if gui.confirm("Save changes?", "Unsaved Changes"):
    save_data()
else:
    gui.alert("Changes were not saved", "Info")
```

## See Also

- [Button](button.md) - Trigger alerts and confirmations
- [Event Handling Guide](../guide/events.md)
- [Best Practices Guide](../guide/best-practices.md)