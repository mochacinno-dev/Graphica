# Best Practices

This guide covers proven patterns and techniques for building great Graphica applications.

## Code Organization

### Start Simple

Begin with a single file. Don't overcomplicate:

```python
import Graphica as gui

# Create window
app = gui.Window("My App", width=400, height=300)

# Add widgets
# ... your code here

# Run app
app.run()
```

### Use Constants

Define layout values as constants:

```python
import Graphica as gui

# Window configuration
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Layout constants
MARGIN = 20
SPACING = 40
LABEL_WIDTH = 100
INPUT_WIDTH = 300

app = gui.Window("Organized App", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Now use the constants
gui.Label(app, "Name:", x=MARGIN, y=MARGIN)
gui.Input(app, x=MARGIN + LABEL_WIDTH, y=MARGIN, width=INPUT_WIDTH)

app.run()
```

### Group Related Code

Keep related functionality together:

```python
import Graphica as gui

app = gui.Window("Task Manager", width=500, height=400)

# === UI Elements ===
task_input = gui.Input(app, x=50, y=50, width=400)
task_list = gui.TextArea(app, x=50, y=120, width=400, height=200)
status_label = gui.Label(app, "", x=50, y=340, size=11)

# === Data ===
tasks = []

# === Functions ===
def add_task():
    task = task_input.get()
    if task:
        tasks.append(task)
        update_display()
        task_input.clear()

def update_display():
    display = "\n".join([f"• {task}" for task in tasks])
    task_list.set(display)
    status_label.set(f"{len(tasks)} tasks")

# === Buttons ===
gui.Button(app, "Add Task", command=add_task, x=200, y=90)

app.run()
```

### Use Classes for Complex Apps

```python
import Graphica as gui

class TodoApp:
    def __init__(self):
        self.app = gui.Window("Todo App", width=500, height=400)
        self.tasks = []
        self.setup_ui()
    
    def setup_ui(self):
        """Create all UI elements"""
        self.input = gui.Input(self.app, x=50, y=50, width=400)
        self.display = gui.TextArea(self.app, x=50, y=120, width=400, height=200)
        gui.Button(self.app, "Add", command=self.add_task, x=200, y=90)
    
    def add_task(self):
        """Add a new task"""
        task = self.input.get()
        if task:
            self.tasks.append(task)
            self.update_display()
            self.input.clear()
    
    def update_display(self):
        """Refresh the task list"""
        text = "\n".join([f"• {t}" for t in self.tasks])
        self.display.set(text)
    
    def run(self):
        """Start the application"""
        self.app.run()

# Usage
app = TodoApp()
app.run()
```

## User Interface Design

### Keep It Simple

Don't add features just because you can:

```python
# ❌ Too much clutter
app = gui.Window("Overloaded", width=800, height=600)
gui.Button(app, "Feature 1", command=None, x=10, y=10)
gui.Button(app, "Feature 2", command=None, x=100, y=10)
gui.Button(app, "Feature 3", command=None, x=190, y=10)
# ... 20 more buttons

# ✅ Clean and focused
app = gui.Window("Simple", width=400, height=300)
gui.Label(app, "What would you like to do?", x=100, y=50, size=14)
gui.Button(app, "New Document", command=new_doc, x=130, y=100)
gui.Button(app, "Open Document", command=open_doc, x=125, y=150)
```

### Use Visual Hierarchy

Guide users' attention with size and position:

```python
import Graphica as gui

app = gui.Window("Visual Hierarchy", width=500, height=400)

# Large title draws attention first
gui.Label(app, "Welcome to My App", x=130, y=30, size=20)

# Medium subtitle
gui.Label(app, "Please enter your information", x=140, y=70, size=12)

# Standard form labels
gui.Label(app, "Name:", x=50, y=120, size=11)
gui.Input(app, x=120, y=120, width=330)

gui.Label(app, "Email:", x=50, y=170, size=11)
gui.Input(app, x=120, y=170, width=330)

# Prominent action button
gui.Button(app, "Continue", command=None, x=200, y=230)

app.run()
```

### Provide Clear Feedback

Always let users know what's happening:

```python
import Graphica as gui

app = gui.Window("Feedback Example", width=450, height=300)

name_input = gui.Input(app, x=50, y=80, width=350)
status = gui.Label(app, "", x=50, y=170, size=11)

def save_name():
    name = name_input.get()
    
    if not name:
        status.set("❌ Please enter a name")
        return
    
    # Show processing
    status.set("⏳ Saving...")
    
    # Simulate work
    import time
    time.sleep(0.5)
    
    # Show success
    status.set(f"✅ Saved: {name}")
    gui.alert(f"Welcome, {name}!", "Success")

gui.Label(app, "Enter your name:", x=50, y=50)
gui.Button(app, "Save", command=save_name, x=180, y=120)

app.run()
```

### Use Consistent Styling

Maintain consistent spacing, sizes, and alignment:

```python
import Graphica as gui

# Define style constants
TITLE_SIZE = 16
LABEL_SIZE = 11
STATUS_SIZE = 10

FORM_LABEL_X = 50
FORM_INPUT_X = 150
FORM_WIDTH = 300

app = gui.Window("Consistent Style", width=500, height=400)

# Title
gui.Label(app, "User Profile", x=180, y=30, size=TITLE_SIZE)

# Form with consistent layout
y = 80
for field in ["Name", "Email", "Phone", "Address"]:
    gui.Label(app, f"{field}:", x=FORM_LABEL_X, y=y, size=LABEL_SIZE)
    gui.Input(app, x=FORM_INPUT_X, y=y, width=FORM_WIDTH)
    y += 50

# Status bar
gui.Label(app, "Status: Ready", x=20, y=370, size=STATUS_SIZE)

app.run()
```

## Input Validation

### Validate Early and Often

Check input as soon as possible:

```python
import Graphica as gui

app = gui.Window("Validation", width=400, height=300)

age_input = gui.Input(app, x=50, y=80, width=300)
feedback = gui.Label(app, "", x=50, y=160, size=11)

def validate_age():
    age_str = age_input.get()
    
    # Check 1: Not empty
    if not age_str:
        feedback.set("❌ Age is required")
        return False
    
    # Check 2: Is a number
    if not age_str.isdigit():
        feedback.set("❌ Age must be a number")
        return False
    
    age = int(age_str)
    
    # Check 3: In valid range
    if age < 0:
        feedback.set("❌ Age cannot be negative")
        return False
    
    if age > 150:
        feedback.set("❌ Please enter a realistic age")
        return False
    
    feedback.set(f"✅ Valid age: {age}")
    return True

gui.Label(app, "Your age:", x=50, y=50)
gui.Button(app, "Validate", command=validate_age, x=150, y=120)

app.run()
```

### Show Helpful Error Messages

Be specific about what's wrong:

```python
# ❌ Not helpful
gui.alert("Error", "Error")

# ✅ Clear and actionable
gui.alert("Email must contain an @ symbol and domain (e.g., user@example.com)", "Invalid Email")
```

### Prevent Invalid Input

Guide users toward valid input:

```python
import Graphica as gui

app = gui.Window("Guided Input", width=450, height=300)

# Provide example format
gui.Label(app, "Phone Number (format: 555-1234):", x=50, y=50, size=11)
phone = gui.Input(app, x=50, y=75, width=300, default="555-")

def validate_phone():
    number = phone.get()
    
    # Check format
    if len(number) != 8 or number[3] != "-":
        gui.alert("Phone must be in format: 555-1234", "Invalid Format")
        return
    
    gui.alert("Phone number saved!", "Success")

gui.Button(app, "Submit", command=validate_phone, x=165, y=120)

app.run()
```

## Error Handling

### Always Use Try-Except

Wrap risky operations:

```python
import Graphica as gui

app = gui.Window("Safe File Operations", width=500, height=300)

def save_file():
    try:
        # File operations
        with open("data.txt", "w") as f:
            f.write("Some data")
        gui.alert("File saved successfully!", "Success")
    except PermissionError:
        gui.alert("Permission denied. Try a different location.", "Error")
    except IOError as e:
        gui.alert(f"Could not save file:\n{str(e)}", "Error")
    except Exception as e:
        gui.alert(f"Unexpected error:\n{str(e)}", "Error")

gui.Button(app, "Save", command=save_file, x=200, y=130)

app.run()
```

### Fail Gracefully

Don't crash the app:

```python
def process_data():
    try:
        # Risky operation
        result = complex_calculation()
        display.set(f"Result: {result}")
    except Exception as e:
        # Log error, show message, but keep app running
        print(f"Error: {e}")
        display.set("Error occurred. Please try again.")
        gui.alert("Processing failed. Please check your input.", "Error")
```

### Log Errors for Debugging

```python
import logging

logging.basicConfig(level=logging.INFO)

def save_data():
    try:
        # Save operation
        pass
    except Exception as e:
        logging.error(f"Save failed: {e}")
        gui.alert("Could not save data", "Error")
```

## Performance Tips

### Don't Block the UI

For long operations, provide feedback:

```python
import Graphica as gui

app = gui.Window("Processing", width=400, height=200)

status = gui.Label(app, "Ready", x=150, y=80, size=12)

def long_operation():
    status.set("Processing...")
    app.root.update()  # Force UI update
    
    # Do work
    import time
    time.sleep(2)
    
    status.set("Complete!")
    gui.alert("Operation complete!", "Done")

gui.Button(app, "Start", command=long_operation, x=155, y=120)

app.run()
```

### Update UI Efficiently

Don't update too frequently:

```python
# ❌ Bad: Updates on every keystroke
def on_change():
    expensive_operation()
    update_display()

# ✅ Good: Update on button click or after pause
def on_submit():
    expensive_operation()
    update_display()
```

### Use Appropriate Widget Sizes

Don't make TextAreas huge if not needed:

```python
# ❌ Wasteful for short text
notes = gui.TextArea(app, x=10, y=10, width=1000, height=800)

# ✅ Appropriate size
notes = gui.TextArea(app, x=10, y=10, width=400, height=200)
```

## Testing Your App

### Test Edge Cases

```python
# Test with:
# - Empty input
# - Very long input
# - Special characters
# - Numbers vs text
# - Negative numbers
# - Zero
# - Maximum values
```

### Test User Flows

```python
# Complete realistic scenarios:
# 1. New user creates account
# 2. User enters invalid data
# 3. User corrects and submits
# 4. User edits existing data
# 5. User deletes data
```

### Test Error Conditions

```python
# Verify error handling:
# - File not found
# - Permission denied
# - Network unavailable
# - Invalid file format
# - Disk full
```

## Documentation

### Comment Complex Logic

```python
def calculate_total(items):
    """Calculate total with discount and tax"""
    
    # Subtotal
    subtotal = sum(item.price for item in items)
    
    # Apply 10% discount for orders over $100
    if subtotal > 100:
        subtotal *= 0.9
    
    # Add 8% sales tax
    tax = subtotal * 0.08
    
    return subtotal + tax
```

### Use Descriptive Names

```python
# ❌ Unclear
def proc(x):
    return x * 1.08

# ✅ Clear
def calculate_price_with_tax(subtotal):
    TAX_RATE = 0.08
    return subtotal * (1 + TAX_RATE)
```

## Common Pitfalls

### Don't Forget app.run()

```python
# ❌ Window never appears
app = gui.Window("Test", width=400, height=300)
gui.Label(app, "Hello", x=10, y=10)
# Missing app.run()!

# ✅ Correct
app = gui.Window("Test", width=400, height=300)
gui.Label(app, "Hello", x=10, y=10)
app.run()
```

### Pass Functions, Not Calls

```python
# ❌ Calls function immediately
gui.Button(app, "Click", command=my_function(), x=10, y=10)

# ✅ Passes function to be called later
gui.Button(app, "Click", command=my_function, x=10, y=10)

# ✅ With arguments, use lambda
gui.Button(app, "Click", command=lambda: my_function(arg), x=10, y=10)
```

### Remember Global Keyword

```python
count = 0

def increment():
    global count  # Don't forget this!
    count += 1
```

### Check for Empty Input

```python
# ❌ Assumes input exists
name = name_input.get()
print(f"Hello, {name}!")  # Prints "Hello, !" if empty

# ✅ Validates first
name = name_input.get()
if name:
    print(f"Hello, {name}!")
else:
    gui.alert("Please enter your name", "Required")
```

## Quick Checklist

Before releasing your app, verify:

- [ ] All buttons do something useful
- [ ] Empty inputs are handled
- [ ] Invalid inputs show clear errors
- [ ] Success actions show confirmation
- [ ] Destructive actions require confirmation
- [ ] File operations handle errors
- [ ] Window size fits all widgets
- [ ] Text is readable and clear
- [ ] Spacing is consistent
- [ ] App doesn't crash on bad input
- [ ] Exit button actually exits
- [ ] Help/About information is present

## See Also

- [Layout Guide](layout.md) - Organizing your UI
- [Event Handling](events.md) - Responding to user actions
- [Examples](../examples/calculator.md) - Real applications to study