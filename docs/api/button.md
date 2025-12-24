# Button

The `Button` class creates clickable buttons that trigger actions when clicked.

## Constructor

```python
Button(parent, text="Button", command=None, x=10, y=10)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Window | Required | The parent window |
| `text` | str | "Button" | Text displayed on the button |
| `command` | function | None | Function to call when clicked |
| `x` | int | 10 | X-coordinate position in pixels |
| `y` | int | 10 | Y-coordinate position in pixels |

### Returns

A `Button` object.

## Methods

### move(x, y)

Move the button to a new position.

```python
button.move(100, 50)
```

#### Parameters
- `x` (int): New x-coordinate
- `y` (int): New y-coordinate

## Examples

### Basic Button

```python
import CocoaGUI as gui

app = gui.Window("Button Demo", width=300, height=200)

def on_click():
    print("Button clicked!")

gui.Button(app, "Click Me", command=on_click, x=100, y=80)

app.run()
```

### Button with Alert

```python
import CocoaGUI as gui

app = gui.Window("Alert Demo", width=300, height=200)

def show_message():
    gui.alert("You clicked the button!", "Message")

gui.Button(app, "Show Alert", command=show_message, x=90, y=80)

app.run()
```

### Multiple Buttons

```python
import CocoaGUI as gui

app = gui.Window("Multiple Buttons", width=400, height=300)

counter = 0
label = gui.Label(app, "Count: 0", x=160, y=50, size=14)

def increment():
    global counter
    counter += 1
    label.set(f"Count: {counter}")

def decrement():
    global counter
    counter -= 1
    label.set(f"Count: {counter}")

def reset():
    global counter
    counter = 0
    label.set(f"Count: {counter}")

gui.Button(app, "Increment", command=increment, x=50, y=100)
gui.Button(app, "Decrement", command=decrement, x=150, y=100)
gui.Button(app, "Reset", command=reset, x=250, y=100)

app.run()
```

### Button with Lambda

For simple operations, use lambda functions:

```python
import CocoaGUI as gui

app = gui.Window("Lambda Demo", width=300, height=200)

label = gui.Label(app, "Not clicked", x=100, y=50)

gui.Button(app, "Click", command=lambda: label.set("Clicked!"), x=100, y=100)

app.run()
```

### Dynamic Button Movement

```python
import CocoaGUI as gui

app = gui.Window("Moving Button", width=400, height=300)

button = gui.Button(app, "Catch Me!", command=None, x=150, y=100)

import random

def move_button():
    new_x = random.randint(50, 300)
    new_y = random.randint(50, 200)
    button.move(new_x, new_y)

button.widget.configure(command=move_button)

app.run()
```

### Button with Confirmation

```python
import CocoaGUI as gui

app = gui.Window("Delete Confirmation", width=400, height=250)

def delete_item():
    if gui.confirm("Are you sure you want to delete?", "Confirm"):
        gui.alert("Item deleted!", "Success")
    else:
        gui.alert("Delete cancelled", "Cancelled")

gui.Button(app, "Delete", command=delete_item, x=150, y=100)

app.run()
```

## Best Practices

### ✅ Do

- Use clear, action-oriented button text ("Save", "Delete", "Submit")
- Define command functions before creating buttons
- Use lambda for simple one-line operations
- Position buttons logically (e.g., "OK" and "Cancel" together)

### ❌ Don't

- Use vague text like "Click Here" or "Button"
- Create buttons without command functions (they'll do nothing)
- Place buttons outside the window boundaries
- Make buttons too close together (leave 10-20px spacing)

## Common Patterns

### Disable/Enable Pattern

```python
import CocoaGUI as gui

app = gui.Window("Enable/Disable", width=400, height=250)

button = gui.Button(app, "Enabled", command=None, x=150, y=100)

def toggle_state():
    current_state = button.widget['state']
    if current_state == 'normal':
        button.widget.configure(state='disabled', text='Disabled')
    else:
        button.widget.configure(state='normal', text='Enabled')

button.widget.configure(command=toggle_state)

app.run()
```

### Submit Form Pattern

```python
import CocoaGUI as gui

app = gui.Window("Form Submit", width=400, height=300)

gui.Label(app, "Name:", x=20, y=20)
name = gui.Input(app, x=20, y=50, width=350)

gui.Label(app, "Email:", x=20, y=90)
email = gui.Input(app, x=20, y=120, width=350)

def submit():
    name_val = name.get()
    email_val = email.get()
    
    if not name_val or not email_val:
        gui.alert("Please fill all fields!", "Error")
        return
    
    gui.alert(f"Submitted!\nName: {name_val}\nEmail: {email_val}", "Success")
    name.clear()
    email.clear()

gui.Button(app, "Submit", command=submit, x=150, y=170)

app.run()
```

## See Also

- [Label](label.md) - Display text that buttons can update
- [Input](input.md) - Get user input for button actions
- [Utilities](utilities.md) - Alert and confirm functions
- [Event Handling Guide](../guide/events.md)