# Input

The Input widget creates single-line text entry fields where users can type information like names, passwords, email addresses, or search queries.

## Constructor

```python
Input(parent, x=10, y=10, width=200, default="")
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Window | Required | The parent window |
| `x` | int | 10 | X-coordinate in pixels |
| `y` | int | 10 | Y-coordinate in pixels |
| `width` | int | 200 | Width in pixels |
| `default` | str | "" | Initial text value |

### Returns

An `Input` object.

## Methods

### get()

Retrieve the current text in the input field.

```python
text = input_field.get()
```

#### Returns
- `str`: The current text content

### set(text)

Replace the input field's text with new text.

```python
input_field.set("New value")
```

#### Parameters
- `text` (str): The text to set

### clear()

Remove all text from the input field.

```python
input_field.clear()
```

## Examples

### Basic Input

```python
import CocoaGUI as gui

app = gui.Window("Basic Input", width=400, height=200)

gui.Label(app, "Enter your name:", x=50, y=50)
name = gui.Input(app, x=50, y=80, width=300)

def submit():
    value = name.get()
    gui.alert(f"You entered: {value}", "Input")

gui.Button(app, "Submit", command=submit, x=50, y=120)

app.run()
```

### Input with Default Value

```python
import CocoaGUI as gui

app = gui.Window("Preset Input", width=400, height=200)

gui.Label(app, "Your website:", x=50, y=50)
website = gui.Input(app, x=50, y=80, width=300, default="https://")

def show_url():
    url = website.get()
    gui.alert(f"Website: {url}", "URL")

gui.Button(app, "Show URL", command=show_url, x=50, y=120)

app.run()
```

### Form with Multiple Inputs

```python
import CocoaGUI as gui

app = gui.Window("Registration Form", width=450, height=400)

gui.Label(app, "Registration Form", x=150, y=20, size=16)

# Name field
gui.Label(app, "Full Name:", x=50, y=60)
name = gui.Input(app, x=50, y=85, width=350)

# Email field
gui.Label(app, "Email:", x=50, y=125)
email = gui.Input(app, x=50, y=150, width=350)

# Username field
gui.Label(app, "Username:", x=50, y=190)
username = gui.Input(app, x=50, y=215, width=350)

result = gui.Label(app, "", x=50, y=300, size=11)

def register():
    n = name.get()
    e = email.get()
    u = username.get()
    
    if not n or not e or not u:
        result.set("❌ Please fill in all fields")
        return
    
    result.set(f"✅ Registered {u} successfully!")
    
    # Clear the form
    name.clear()
    email.clear()
    username.clear()

gui.Button(app, "Register", command=register, x=175, y=260)

app.run()
```

### Search Box

```python
import CocoaGUI as gui

app = gui.Window("Search", width=500, height=250)

gui.Label(app, "Search for anything:", x=50, y=40, size=12)
search = gui.Input(app, x=50, y=70, width=400, default="")

results = gui.Label(app, "", x=50, y=140, size=11)

def perform_search():
    query = search.get()
    if query:
        results.set(f'Searching for "{query}"...')
    else:
        results.set("Please enter a search term")

gui.Button(app, "Search", command=perform_search, x=50, y=105)

app.run()
```

### Input Validation

```python
import CocoaGUI as gui

app = gui.Window("Age Validator", width=400, height=250)

gui.Label(app, "Enter your age:", x=50, y=50)
age_input = gui.Input(app, x=50, y=80, width=150)

feedback = gui.Label(app, "", x=50, y=160, size=11)

def validate_age():
    age = age_input.get()
    
    # Check if it's a number
    if not age.isdigit():
        feedback.set("❌ Please enter a valid number")
        return
    
    age_num = int(age)
    
    if age_num < 0:
        feedback.set("❌ Age cannot be negative")
    elif age_num < 13:
        feedback.set("⚠️ You must be 13 or older")
    elif age_num > 120:
        feedback.set("❌ Please enter a realistic age")
    else:
        feedback.set(f"✅ Valid age: {age_num} years old")

gui.Button(app, "Validate", command=validate_age, x=50, y=120)

app.run()
```

### Password-style Input (Workaround)

While CocoaGUI's Input doesn't have built-in password masking, you can guide users:

```python
import CocoaGUI as gui

app = gui.Window("Login", width=400, height=250)

gui.Label(app, "Username:", x=50, y=40)
username = gui.Input(app, x=50, y=65, width=300)

gui.Label(app, "Password:", x=50, y=105)
password = gui.Input(app, x=50, y=130, width=300)
gui.Label(app, "(Note: Password will be visible)", x=50, y=160, size=9)

def login():
    user = username.get()
    pwd = password.get()
    
    if user and pwd:
        gui.alert(f"Logging in as {user}", "Login")
        username.clear()
        password.clear()

gui.Button(app, "Login", command=login, x=150, y=190)

app.run()
```

### Calculator Input

```python
import CocoaGUI as gui

app = gui.Window("Simple Calculator", width=400, height=300)

gui.Label(app, "First Number:", x=50, y=40)
num1 = gui.Input(app, x=50, y=65, width=280)

gui.Label(app, "Second Number:", x=50, y=105)
num2 = gui.Input(app, x=50, y=130, width=280)

result_label = gui.Label(app, "Result: ", x=50, y=220, size=14)

def calculate(operation):
    try:
        a = float(num1.get())
        b = float(num2.get())
        
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                result_label.set("Error: Cannot divide by zero")
                return
            result = a / b
        
        result_label.set(f"Result: {result}")
    except ValueError:
        result_label.set("Error: Please enter valid numbers")

gui.Button(app, "+", command=lambda: calculate("+"), x=50, y=175)
gui.Button(app, "-", command=lambda: calculate("-"), x=110, y=175)
gui.Button(app, "×", command=lambda: calculate("*"), x=170, y=175)
gui.Button(app, "÷", command=lambda: calculate("/"), x=230, y=175)

app.run()
```

### Unit Converter

```python
import CocoaGUI as gui

app = gui.Window("Temperature Converter", width=400, height=300)

gui.Label(app, "Temperature Converter", x=110, y=20, size=16)

gui.Label(app, "Celsius:", x=50, y=70)
celsius = gui.Input(app, x=150, y=70, width=180)

gui.Label(app, "Fahrenheit:", x=50, y=110)
fahrenheit = gui.Input(app, x=150, y=110, width=180)

def celsius_to_fahrenheit():
    try:
        c = float(celsius.get())
        f = (c * 9/5) + 32
        fahrenheit.set(f"{f:.2f}")
    except ValueError:
        gui.alert("Please enter a valid number", "Error")

def fahrenheit_to_celsius():
    try:
        f = float(fahrenheit.get())
        c = (f - 32) * 5/9
        celsius.set(f"{c:.2f}")
    except ValueError:
        gui.alert("Please enter a valid number", "Error")

gui.Button(app, "C → F", command=celsius_to_fahrenheit, x=100, y=160)
gui.Button(app, "F → C", command=fahrenheit_to_celsius, x=200, y=160)

app.run()
```

## Input Validation Patterns

### Email Validation

```python
def is_valid_email(email):
    return "@" in email and "." in email.split("@")[1]

def check_email():
    email = email_input.get()
    if is_valid_email(email):
        status.set("✅ Valid email")
    else:
        status.set("❌ Invalid email format")
```

### Number Validation

```python
def is_number(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def validate_number():
    value = number_input.get()
    if is_number(value):
        status.set("✅ Valid number")
    else:
        status.set("❌ Please enter a number")
```

### Length Validation

```python
def check_length():
    text = text_input.get()
    if len(text) < 3:
        status.set("❌ Too short (minimum 3 characters)")
    elif len(text) > 50:
        status.set("❌ Too long (maximum 50 characters)")
    else:
        status.set(f"✅ Valid ({len(text)} characters)")
```

## Best Practices

**Always validate user input.** Never trust that users will enter what you expect. Check for empty values, invalid formats, and unexpected characters.

**Provide clear labels.** Users should immediately understand what to enter in each field.

**Give helpful feedback.** When validation fails, tell users exactly what's wrong and how to fix it.

**Clear inputs after successful submission.** Helps users know their action was completed and prepares the form for the next entry.

**Consider default values carefully.** They can speed up data entry but might confuse users if not obvious.

**Set appropriate widths.** Short fields for short inputs (like age), long fields for emails or URLs.

## Common Issues

### Getting Empty String

If `get()` returns an empty string, the user hasn't entered anything:

```python
text = input_field.get()
if not text:
    gui.alert("Please enter a value", "Required Field")
```

### Type Conversion

Input always returns strings. Convert to numbers when needed:

```python
age_str = age_input.get()
age = int(age_str)  # May raise ValueError if not a number
```

Always use try-except for safety:

```python
try:
    age = int(age_input.get())
except ValueError:
    gui.alert("Please enter a number", "Invalid Input")
```

## See Also

- [Label](label.md) - Label your input fields
- [Button](button.md) - Submit input data
- [TextArea](textarea.md) - Multi-line text input
- [Event Handling Guide](../guide/events.md)