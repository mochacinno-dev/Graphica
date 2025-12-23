# Label

Labels display text in your application. They're perfect for titles, instructions, status messages, or any other text that needs to be shown to users.

## Constructor

```python
Label(parent, text="Label", x=10, y=10, size=12)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Window | Required | The parent window |
| `text` | str | "Label" | Text to display |
| `x` | int | 10 | X-coordinate in pixels |
| `y` | int | 10 | Y-coordinate in pixels |
| `size` | int | 12 | Font size in points |

### Returns

A `Label` object.

## Methods

### set(text)

Update the text displayed by the label.

```python
label.set("New text here")
```

#### Parameters
- `text` (str): The new text to display

### move(x, y)

Move the label to a new position.

```python
label.move(150, 200)
```

#### Parameters
- `x` (int): New x-coordinate
- `y` (int): New y-coordinate

## Examples

### Basic Label

```python
import Graphica as gui

app = gui.Window("Label Example", width=400, height=200)

gui.Label(app, "Welcome to Graphica!", x=120, y=80, size=14)

app.run()
```

### Dynamic Label Updates

Labels really shine when you update them based on user actions:

```python
import Graphica as gui

app = gui.Window("Counter", width=300, height=200)

count = 0
counter_label = gui.Label(app, "Count: 0", x=100, y=50, size=16)

def increment():
    global count
    count += 1
    counter_label.set(f"Count: {count}")

gui.Button(app, "+1", command=increment, x=120, y=100)

app.run()
```

### Multiple Font Sizes

Use different sizes for hierarchy:

```python
import Graphica as gui

app = gui.Window("Welcome Screen", width=450, height=350)

# Large title
gui.Label(app, "Graphica Text Editor", x=100, y=30, size=20)

# Medium subtitle
gui.Label(app, "Simple. Fast. Powerful.", x=135, y=70, size=14)

# Small description
gui.Label(app, "Create and edit text files with ease", x=110, y=110, size=11)

# Tiny footer
gui.Label(app, "Version 1.0.0", x=180, y=300, size=9)

app.run()
```

### Status Messages

Labels are great for showing status or feedback:

```python
import Graphica as gui

app = gui.Window("Login", width=400, height=300)

gui.Label(app, "Username:", x=50, y=50)
username = gui.Input(app, x=50, y=80, width=300)

gui.Label(app, "Password:", x=50, y=120)
password = gui.Input(app, x=50, y=150, width=300)

status = gui.Label(app, "", x=50, y=230, size=11)

def login():
    user = username.get()
    pwd = password.get()
    
    if not user or not pwd:
        status.set("❌ Please fill in all fields")
    elif len(pwd) < 6:
        status.set("❌ Password must be at least 6 characters")
    else:
        status.set(f"✅ Welcome, {user}!")

gui.Button(app, "Login", command=login, x=50, y=190)

app.run()
```

### Form Labels

Labels help guide users through forms:

```python
import Graphica as gui

app = gui.Window("Contact Form", width=450, height=400)

gui.Label(app, "Contact Information", x=150, y=20, size=16)

gui.Label(app, "Full Name:", x=50, y=70, size=11)
name = gui.Input(app, x=50, y=95, width=350)

gui.Label(app, "Email Address:", x=50, y=135, size=11)
email = gui.Input(app, x=50, y=160, width=350)

gui.Label(app, "Message:", x=50, y=200, size=11)
message = gui.TextArea(app, x=50, y=225, width=350, height=100)

def submit():
    gui.alert("Form submitted!", "Success")

gui.Button(app, "Send Message", command=submit, x=170, y=340)

app.run()
```

### Timer Display

Update labels in real-time:

```python
import Graphica as gui
import time

app = gui.Window("Timer", width=300, height=150)

start_time = time.time()
timer_label = gui.Label(app, "00:00", x=110, y=50, size=24)

def update_timer():
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60
    timer_label.set(f"{minutes:02d}:{seconds:02d}")
    app.root.after(1000, update_timer)

update_timer()

app.run()
```

## Styling Tips

### Text Alignment

While Graphica uses absolute positioning, you can calculate centered positions:

```python
import Graphica as gui

app = gui.Window("Centered Text", width=400, height=200)

# Rough centering calculation
text = "This is centered"
# Each character is roughly 7-8 pixels wide at size 12
text_width = len(text) * 7
x_position = (400 - text_width) // 2

gui.Label(app, text, x=x_position, y=90, size=12)

app.run()
```

### Font Size Guidelines

- **9-10pt**: Small text, footnotes, version numbers
- **11-12pt**: Regular body text, form labels
- **14-16pt**: Section headers, emphasis
- **18-24pt**: Page titles, main headlines
- **28pt+**: Large display text (use sparingly)

## Common Patterns

### Loading Indicator

```python
import Graphica as gui

app = gui.Window("Loading", width=300, height=150)

status = gui.Label(app, "Loading", x=120, y=60, size=14)

dots = 0
def animate_loading():
    global dots
    dots = (dots + 1) % 4
    status.set("Loading" + "." * dots)
    app.root.after(500, animate_loading)

animate_loading()

app.run()
```

### Validation Feedback

```python
import Graphica as gui

app = gui.Window("Email Validator", width=400, height=200)

gui.Label(app, "Enter your email:", x=50, y=30)
email_input = gui.Input(app, x=50, y=60, width=300)

feedback = gui.Label(app, "", x=50, y=130, size=11)

def validate():
    email = email_input.get()
    if "@" in email and "." in email:
        feedback.set("✅ Valid email address")
    else:
        feedback.set("❌ Invalid email address")

gui.Button(app, "Validate", command=validate, x=50, y=95)

app.run()
```

### Multi-line Information

For multiple lines of text, consider using separate labels:

```python
import Graphica as gui

app = gui.Window("About", width=400, height=300)

gui.Label(app, "About This Application", x=110, y=30, size=16)
gui.Label(app, "Version 1.0.0", x=155, y=70, size=11)
gui.Label(app, "Created with Graphica", x=130, y=95, size=11)
gui.Label(app, "© 2024 Your Name", x=145, y=120, size=10)

app.run()
```

## Best Practices

**Use clear, concise text.** Labels should be easy to scan and understand at a glance.

**Choose appropriate sizes.** Don't make everything huge or tiny. Use size to create visual hierarchy.

**Update labels thoughtfully.** When changing label text, make sure the new text fits in the available space.

**Consider text length.** Very long text might get cut off. Test with your longest expected strings.

**Use labels for static text.** If users need to select or copy text, consider using a TextArea instead.

## See Also

- [Button](button.md) - Labels often work alongside buttons
- [Input](input.md) - Labels typically describe input fields
- [Layout Guide](../guide/layout.md) - Positioning labels effectively