# Event Handling

Event handling in Graphica is straightforward: you define functions and pass them to widgets as commands. When the user interacts with a widget, your function gets called.

## Basic Event Handling

### Button Clicks

The most common event is a button click:

```python
import Graphica as gui

app = gui.Window("Button Click", width=400, height=200)

def on_click():
    print("Button was clicked!")
    gui.alert("You clicked the button!", "Click Event")

gui.Button(app, "Click Me", command=on_click, x=150, y=80)

app.run()
```

**Important**: Pass the function itself, not a function call:

```python
# ✅ Correct
gui.Button(app, "Click", command=on_click, x=10, y=10)

# ❌ Wrong - calls the function immediately
gui.Button(app, "Click", command=on_click(), x=10, y=10)
```

### Accessing Widget Values

Event handlers typically need to get or set widget values:

```python
import Graphica as gui

app = gui.Window("Input Event", width=400, height=250)

name_input = gui.Input(app, x=50, y=50, width=300)
result_label = gui.Label(app, "", x=50, y=130, size=12)

def process_input():
    # Get the input value
    name = name_input.get()
    
    # Update the label
    result_label.set(f"Hello, {name}!")

gui.Button(app, "Submit", command=process_input, x=150, y=90)

app.run()
```

## Passing Arguments to Event Handlers

### Using Lambda Functions

Lambda functions let you pass arguments to event handlers:

```python
import Graphica as gui

app = gui.Window("Lambda Events", width=400, height=250)

counter = gui.Label(app, "Count: 0", x=150, y=50, size=14)
count = 0

def change_count(amount):
    global count
    count += amount
    counter.set(f"Count: {count}")

# Lambda functions let us pass arguments
gui.Button(app, "+1", command=lambda: change_count(1), x=100, y=100)
gui.Button(app, "+5", command=lambda: change_count(5), x=170, y=100)
gui.Button(app, "+10", command=lambda: change_count(10), x=240, y=100)

app.run()
```

### Lambda with Widget Values

```python
import Graphica as gui

app = gui.Window("Calculator", width=400, height=300)

num1 = gui.Input(app, x=50, y=50, width=100)
num2 = gui.Input(app, x=200, y=50, width=100)
result = gui.Label(app, "Result: ", x=150, y=150, size=14)

def calculate(operation):
    try:
        a = float(num1.get())
        b = float(num2.get())
        
        if operation == "add":
            answer = a + b
        elif operation == "subtract":
            answer = a - b
        elif operation == "multiply":
            answer = a * b
        elif operation == "divide":
            answer = a / b if b != 0 else "Error"
        
        result.set(f"Result: {answer}")
    except ValueError:
        result.set("Result: Invalid input")

gui.Button(app, "+", command=lambda: calculate("add"), x=80, y=100)
gui.Button(app, "-", command=lambda: calculate("subtract"), x=140, y=100)
gui.Button(app, "×", command=lambda: calculate("multiply"), x=200, y=100)
gui.Button(app, "÷", command=lambda: calculate("divide"), x=260, y=100)

app.run()
```

## Managing State

### Global Variables

For simple apps, global variables work fine:

```python
import Graphica as gui

app = gui.Window("Todo List", width=500, height=400)

# Global state
todos = []

todo_input = gui.Input(app, x=50, y=50, width=400)
todo_display = gui.TextArea(app, x=50, y=120, width=400, height=200)

def add_todo():
    global todos
    
    text = todo_input.get()
    if text:
        todos.append(text)
        update_display()
        todo_input.clear()

def update_display():
    display_text = "\n".join([f"• {todo}" for todo in todos])
    todo_display.set(display_text)

gui.Button(app, "Add Todo", command=add_todo, x=200, y=90)

app.run()
```

### Class-Based State Management

For more complex apps, use a class:

```python
import Graphica as gui

class CounterApp:
    def __init__(self):
        self.app = gui.Window("Counter App", width=400, height=250)
        self.count = 0
        
        self.counter_label = gui.Label(
            self.app, "Count: 0", x=150, y=50, size=16
        )
        
        gui.Button(
            self.app, "Increment", 
            command=self.increment, 
            x=100, y=100
        )
        gui.Button(
            self.app, "Decrement", 
            command=self.decrement, 
            x=210, y=100
        )
        gui.Button(
            self.app, "Reset", 
            command=self.reset, 
            x=155, y=150
        )
    
    def increment(self):
        self.count += 1
        self.update_display()
    
    def decrement(self):
        self.count -= 1
        self.update_display()
    
    def reset(self):
        self.count = 0
        self.update_display()
    
    def update_display(self):
        self.counter_label.set(f"Count: {self.count}")
    
    def run(self):
        self.app.run()

# Create and run the app
app = CounterApp()
app.run()
```

## Advanced Event Patterns

### Confirmation Before Action

Always confirm destructive actions:

```python
import Graphica as gui

app = gui.Window("Delete Example", width=400, height=200)

data = ["Important data here"]

def delete_data():
    if gui.confirm("Are you sure you want to delete all data?", "Confirm"):
        data.clear()
        gui.alert("Data deleted", "Success")
    else:
        gui.alert("Deletion cancelled", "Cancelled")

gui.Button(app, "Delete All", command=delete_data, x=140, y=80)

app.run()
```

### Validation Before Processing

```python
import Graphica as gui

app = gui.Window("Form Validation", width=450, height=350)

name_input = gui.Input(app, x=50, y=80, width=350)
email_input = gui.Input(app, x=50, y=150, width=350)
status = gui.Label(app, "", x=50, y=250, size=11)

def validate_and_submit():
    name = name_input.get()
    email = email_input.get()
    
    # Validation chain
    if not name:
        status.set("❌ Please enter your name")
        return
    
    if not email:
        status.set("❌ Please enter your email")
        return
    
    if "@" not in email:
        status.set("❌ Invalid email format")
        return
    
    # All validations passed
    status.set(f"✅ Welcome, {name}!")
    gui.alert(f"Account created for {email}", "Success")

gui.Label(app, "Name:", x=50, y=50)
gui.Label(app, "Email:", x=50, y=120)
gui.Button(app, "Submit", command=validate_and_submit, x=180, y=200)

app.run()
```

### Multi-Step Processes

```python
import Graphica as gui

app = gui.Window("Multi-Step", width=450, height=300)

step = 1
max_steps = 3

status = gui.Label(app, "Step 1 of 3", x=170, y=50, size=14)
instruction = gui.Label(app, "Enter your name", x=160, y=90, size=11)
user_input = gui.Input(app, x=100, y=130, width=250)

data = {}

def next_step():
    global step
    
    value = user_input.get()
    
    if step == 1:
        if not value:
            gui.alert("Please enter your name", "Required")
            return
        data['name'] = value
        status.set("Step 2 of 3")
        instruction.set("Enter your email")
        user_input.clear()
        step = 2
    
    elif step == 2:
        if not value or "@" not in value:
            gui.alert("Please enter a valid email", "Invalid")
            return
        data['email'] = value
        status.set("Step 3 of 3")
        instruction.set("Enter your phone")
        user_input.clear()
        step = 3
    
    elif step == 3:
        if not value:
            gui.alert("Please enter your phone", "Required")
            return
        data['phone'] = value
        
        summary = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}"
        gui.alert(f"Registration complete!\n\n{summary}", "Success")
        
        # Reset
        step = 1
        status.set("Step 1 of 3")
        instruction.set("Enter your name")
        user_input.clear()

gui.Button(app, "Next", command=next_step, x=190, y=180)

app.run()
```

### Toggle States

```python
import Graphica as gui

app = gui.Window("Toggle Example", width=400, height=250)

is_enabled = True
status = gui.Label(app, "Status: Enabled", x=140, y=80, size=14)
toggle_btn = gui.Button(app, "Disable", command=None, x=150, y=130)

def toggle_state():
    global is_enabled
    is_enabled = not is_enabled
    
    if is_enabled:
        status.set("Status: Enabled")
        toggle_btn.widget.configure(text="Disable")
    else:
        status.set("Status: Disabled")
        toggle_btn.widget.configure(text="Enable")

toggle_btn.widget.configure(command=toggle_state)

app.run()
```

## Timed Events

### Scheduled Updates

Run a function repeatedly:

```python
import Graphica as gui
from datetime import datetime

app = gui.Window("Clock", width=300, height=150)

time_label = gui.Label(app, "", x=80, y=60, size=16)

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.set(current_time)
    
    # Schedule next update in 1000ms (1 second)
    app.root.after(1000, update_time)

# Start the update loop
update_time()

app.run()
```

### Countdown Timer

```python
import Graphica as gui

app = gui.Window("Countdown", width=300, height=200)

seconds_left = 10
timer_label = gui.Label(app, f"{seconds_left} seconds", x=90, y=50, size=18)
status = gui.Label(app, "Waiting to start...", x=90, y=100, size=11)

timer_running = False

def countdown():
    global seconds_left, timer_running
    
    if timer_running and seconds_left > 0:
        seconds_left -= 1
        timer_label.set(f"{seconds_left} seconds")
        
        if seconds_left == 0:
            status.set("Time's up!")
            gui.alert("Countdown complete!", "Done")
            timer_running = False
        else:
            app.root.after(1000, countdown)

def start_timer():
    global seconds_left, timer_running
    
    if not timer_running:
        seconds_left = 10
        timer_running = True
        status.set("Counting down...")
        countdown()

gui.Button(app, "Start", command=start_timer, x=115, y=140)

app.run()
```

## Event Handling Best Practices

### Keep Handlers Focused

```python
# ❌ Bad: Handler does too much
def on_submit():
    value = input.get()
    validate(value)
    process(value)
    update_ui()
    save_to_file()
    send_email()
    cleanup()

# ✅ Good: Handler coordinates focused functions
def on_submit():
    value = input.get()
    
    if not validate(value):
        show_error()
        return
    
    process(value)
    update_ui()
```

### Provide Feedback

Always let users know what happened:

```python
def save_document():
    try:
        # Save logic here
        status_label.set("✅ Document saved")
        gui.alert("Document saved successfully!", "Success")
    except Exception as e:
        status_label.set("❌ Save failed")
        gui.alert(f"Error: {str(e)}", "Error")
```

### Handle Errors Gracefully

```python
def calculate():
    try:
        num = float(input_field.get())
        result = 100 / num
        result_label.set(f"Result: {result}")
    except ValueError:
        gui.alert("Please enter a valid number", "Invalid Input")
    except ZeroDivisionError:
        gui.alert("Cannot divide by zero", "Math Error")
    except Exception as e:
        gui.alert(f"Unexpected error: {str(e)}", "Error")
```

### Validate Early

```python
def submit_form():
    # Validate everything before processing
    name = name_input.get()
    age = age_input.get()
    
    if not name:
        gui.alert("Name is required", "Validation Error")
        return
    
    if not age.isdigit():
        gui.alert("Age must be a number", "Validation Error")
        return
    
    if int(age) < 18:
        gui.alert("Must be 18 or older", "Validation Error")
        return
    
    # Now process the valid data
    process_registration(name, int(age))
```

## Common Patterns

### Save Before Exit

```python
def on_exit():
    if gui.confirm("Save before exiting?", "Confirm"):
        save_data()
    app.close()

gui.Button(app, "Exit", command=on_exit, x=10, y=10)
```

### Clear After Submit

```python
def submit():
    data = input_field.get()
    
    # Process data
    process(data)
    
    # Clear for next entry
    input_field.clear()
    
    # Confirm to user
    gui.alert("Submitted successfully!", "Success")
```

### Disable While Processing

```python
submit_button = gui.Button(app, "Submit", command=None, x=10, y=10)

def process_data():
    # Disable button
    submit_button.widget.configure(state='disabled')
    
    # Do work
    result = expensive_operation()
    
    # Re-enable button
    submit_button.widget.configure(state='normal')
    
    gui.alert(f"Done! Result: {result}", "Complete")

submit_button.widget.configure(command=process_data)
```

## See Also

- [Button API](../api/button.md) - Button event handling
- [Input API](../api/input.md) - Getting user input
- [Best Practices](best-practices.md) - UI design tips
- [Calculator Example](../examples/calculator.md) - Complex event handling