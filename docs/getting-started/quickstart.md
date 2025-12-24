# Quick Start

Let's build your first CocoaGUI application in under 5 minutes!

## The Basics

Every CocoaGUI app follows this simple pattern:

1. Create a Window
2. Add widgets to the window
3. Run the app

## Hello World

Create a file called `hello.py`:

```python
import CocoaGUI as gui

# Step 1: Create a window
app = gui.Window("Hello World", width=400, height=200)

# Step 2: Add a label
gui.Label(app, "Hello, World!", x=150, y=80, size=18)

# Step 3: Run the app
app.run()
```

Run it: `python hello.py`

That's it! You've created your first GUI application.

## Adding Interactivity

Let's make it interactive with a button:

```python
import CocoaGUI as gui

app = gui.Window("Interactive Hello", width=400, height=200)

label = gui.Label(app, "Click the button!", x=130, y=60, size=14)

def on_click():
    label.set("Hello, CocoaGUI! 👋")

gui.Button(app, "Click Me", command=on_click, x=150, y=100)

app.run()
```

When you click the button, the label text changes!

## Getting User Input

Now let's get input from the user:

```python
import CocoaGUI as gui

app = gui.Window("Greeter", width=400, height=250)

gui.Label(app, "What's your name?", x=20, y=20, size=12)
name_input = gui.Input(app, x=20, y=50, width=350)

result_label = gui.Label(app, "", x=20, y=120, size=14)

def greet():
    name = name_input.get()
    if name:
        result_label.set(f"Nice to meet you, {name}!")
        gui.alert(f"Hello, {name}!", "Greeting")
    else:
        gui.alert("Please enter your name!", "Oops")

gui.Button(app, "Greet Me", command=greet, x=20, y=85)

app.run()
```

This app:
- Gets text from an Input widget
- Updates a Label based on the input
- Shows an alert dialog

## Core Concepts

### 1. Parent Parameter

Every widget needs to know which window it belongs to. That's the first parameter:

```python
gui.Button(app, ...)  # app is the parent window
```

### 2. Positioning

Widgets are positioned with `x` and `y` coordinates (in pixels):

```python
gui.Label(app, "Top-left", x=10, y=10)
gui.Label(app, "Lower-right", x=300, y=200)
```

### 3. Event Handlers

Buttons need functions to call when clicked:

```python
def my_function():
    print("Button clicked!")

gui.Button(app, "Click", command=my_function, x=10, y=10)
```

### 4. Getting and Setting Values

Most widgets have `.get()` and `.set()` methods:

```python
# Get value
text = my_input.get()

# Set value
my_label.set("New text")
```

## Common Patterns

### Pattern: Form with Validation

```python
import CocoaGUI as gui

app = gui.Window("Login Form", width=400, height=300)

gui.Label(app, "Username:", x=20, y=20)
username = gui.Input(app, x=20, y=50, width=350)

gui.Label(app, "Password:", x=20, y=90)
password = gui.Input(app, x=20, y=120, width=350)

def login():
    user = username.get()
    pwd = password.get()
    
    if not user or not pwd:
        gui.alert("Please fill in all fields!", "Error")
        return
    
    gui.alert(f"Welcome, {user}!", "Success")

gui.Button(app, "Login", command=login, x=20, y=160)

app.run()
```

### Pattern: Counter App

```python
import CocoaGUI as gui

app = gui.Window("Counter", width=300, height=200)

count = 0
count_label = gui.Label(app, "Count: 0", x=110, y=50, size=16)

def increment():
    global count
    count += 1
    count_label.set(f"Count: {count}")

def reset():
    global count
    count = 0
    count_label.set(f"Count: {count}")

gui.Button(app, "Increment", command=increment, x=50, y=100)
gui.Button(app, "Reset", command=reset, x=150, y=100)

app.run()
```

## Next Steps

Now you know the basics! Here's what to explore next:

- [Your First App Tutorial](first-app.md) - Build a complete todo list app
- [API Reference](../api/window.md) - Learn about all available widgets
- [Examples](../examples/calculator.md) - See real-world applications

Ready to dive deeper? Let's [build your first real app](first-app.md)!