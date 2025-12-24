# Calculator Example

A fully functional calculator built with CocoaGUI demonstrating button handling, state management, and user interaction.

## Layout

```
┌─────────────────────────────────┐
│  Simple Calculator              │
├─────────────────────────────────┤
│                                 │
│  ┌─────────────────────────┐    │
│  │ 0                       │    │
│  └─────────────────────────┘    │
│                                 │
│   [7]  [8]  [9]         [+]     │
│   [4]  [5]  [6]         [-]     │
│   [1]  [2]  [3]         [*]     │
│   [0]  [.]  [=]         [/]     │
│                                 │
│        [Clear]                  │
└─────────────────────────────────┘
```

## Complete Code

```python
"""
Simple Calculator Application
Using the CocoaGUI GUI Library
"""

import CocoaGUI as gui

# Create the main window
app = gui.Window("Simple Calculator", width=350, height=450)

# Title label
gui.Label(app, "Simple Calculator", x=90, y=20, size=18)

# Display area for the calculation
display = gui.TextArea(app, x=25, y=60, width=300, height=60)
display.set("0")

# Global variable to track calculation state
current_value = ""
operator = None
first_number = None

def add_to_display(value):
    """Add a number or decimal to the display"""
    global current_value
    current_text = display.get().strip()
    
    if current_text == "0" or current_text == "Error":
        current_value = str(value)
    else:
        current_value = current_text + str(value)
    
    display.set(current_value)

def clear_display():
    """Clear the calculator display"""
    global current_value, operator, first_number
    current_value = ""
    operator = None
    first_number = None
    display.set("0")

def set_operator(op):
    """Set the mathematical operator"""
    global operator, first_number, current_value
    current_text = display.get().strip()
    
    try:
        first_number = float(current_text)
        operator = op
        current_value = ""
        display.set(f"{first_number} {op}")
    except:
        display.set("Error")

def calculate():
    """Perform the calculation"""
    global first_number, operator, current_value
    
    if first_number is None or operator is None:
        return
    
    current_text = display.get().strip()
    
    # Extract the second number from display
    try:
        parts = current_text.split(operator)
        if len(parts) > 1 and parts[1].strip():
            second_number = float(parts[1].strip())
        else:
            return
        
        # Perform calculation
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                display.set("Error: Division by zero")
                first_number = None
                operator = None
                return
            result = first_number / second_number
        
        # Display result
        display.set(str(result))
        first_number = result
        operator = None
        current_value = str(result)
    except:
        display.set("Error")
        first_number = None
        operator = None

# Number buttons - ultra simple syntax!
button_positions = [
    (7, 25, 150), (8, 100, 150), (9, 175, 150),
    (4, 25, 200), (5, 100, 200), (6, 175, 200),
    (1, 25, 250), (2, 100, 250), (3, 175, 250),
    (0, 25, 300)
]

for num, x, y in button_positions:
    gui.Button(app, str(num), command=lambda n=num: add_to_display(n), x=x, y=y)

# Decimal point button
gui.Button(app, ".", command=lambda: add_to_display("."), x=100, y=300)

# Operator buttons
gui.Button(app, "+", command=lambda: set_operator("+"), x=250, y=150)
gui.Button(app, "-", command=lambda: set_operator("-"), x=250, y=200)
gui.Button(app, "*", command=lambda: set_operator("*"), x=250, y=250)
gui.Button(app, "/", command=lambda: set_operator("/"), x=250, y=300)

# Equals button
gui.Button(app, "=", command=calculate, x=175, y=300)

# Clear button
gui.Button(app, "Clear", command=clear_display, x=25, y=360)

# Info label
gui.Label(app, "Created with CocoaGUI GUI Library", x=60, y=415, size=10)

# Run the application
app.run()
```

## Key Features

### State Management
The calculator maintains three pieces of state:
- `current_value`: The number being typed
- `operator`: The selected operation (+, -, *, /)
- `first_number`: The first operand

### Error Handling
- Division by zero detection
- Invalid input handling
- Error state recovery with Clear button

### User Experience
- Clear visual feedback
- Decimal point support
- Continuous calculations (result becomes first number)

## How It Works

### 1. Number Input
When you click a number button:
```python
def add_to_display(value):
    # Appends digit to current display
    # Handles "0" and "Error" states
```

### 2. Operator Selection
When you click an operator:
```python
def set_operator(op):
    # Stores the first number
    # Shows the operation in display
    # Prepares for second number
```

### 3. Calculation
When you click equals:
```python
def calculate():
    # Extracts second number from display
    # Performs the operation
    # Shows result
    # Allows chaining operations
```

### 4. Clear Function
Resets all state:
```python
def clear_display():
    # Resets all variables
    # Sets display to "0"
```

## Improvements You Could Make

1. **Keyboard Support**: Add keyboard event handlers
2. **History**: Keep track of previous calculations
3. **Advanced Operations**: Add sqrt, power, percentage
4. **Better Layout**: Use calculated positions instead of hardcoded
5. **Styling**: Customize button colors and sizes

## Learning Points

This example demonstrates:
- ✅ Managing application state with global variables
- ✅ Using lambda functions for button commands
- ✅ Creating multiple similar widgets with loops
- ✅ Error handling in user interactions
- ✅ String parsing and type conversion
- ✅ Building a complete, functional application

## Try It Yourself

**Challenge 1**: Add a backspace button to delete the last digit

**Challenge 2**: Add support for negative numbers

**Challenge 3**: Show calculation history in a TextArea

**Challenge 4**: Add memory functions (M+, M-, MR, MC)

## See Also

- [Text Editor Example](text-editor.md) - File operations and live updates
- [Button API](../api/button.md) - Learn more about buttons
- [TextArea API](../api/textarea.md) - Display widget documentation