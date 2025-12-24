# Layout & Positioning

CocoaGUI uses absolute positioning with x and y coordinates. While this is simpler than complex layout systems, it requires some planning to create organized interfaces.

## Understanding Coordinates

CocoaGUI positions widgets using pixel coordinates from the top-left corner:

```
(0,0) ────────────────────────► X-axis
  │
  │    [Widget at x=50, y=30]
  │
  │
  ▼
Y-axis
```

- **X increases** moving right
- **Y increases** moving down
- Top-left of window is (0, 0)

## Basic Positioning

```python
import CocoaGUI as gui

app = gui.Window("Position Demo", width=400, height=300)

# Top-left corner
gui.Label(app, "Top Left", x=10, y=10)

# Top-right area
gui.Label(app, "Top Right", x=310, y=10)

# Bottom-left area
gui.Label(app, "Bottom Left", x=10, y=270)

# Center area
gui.Label(app, "Center", x=175, y=135)

app.run()
```

## Layout Patterns

### Vertical Stack

Place widgets in a vertical column:

```python
import CocoaGUI as gui

app = gui.Window("Vertical Stack", width=400, height=350)

x = 50  # Fixed x position
y = 20  # Starting y position
spacing = 40  # Space between items

gui.Label(app, "Name:", x=x, y=y)
gui.Input(app, x=x, y=y+25, width=300)

y += spacing + 25  # Move down

gui.Label(app, "Email:", x=x, y=y)
gui.Input(app, x=x, y=y+25, width=300)

y += spacing + 25

gui.Label(app, "Message:", x=x, y=y)
gui.TextArea(app, x=x, y=y+25, width=300, height=100)

app.run()
```

### Horizontal Row

Place widgets side-by-side:

```python
import CocoaGUI as gui

app = gui.Window("Horizontal Row", width=500, height=200)

y = 80  # Fixed y position
x = 50  # Starting x position
spacing = 80  # Space between buttons

gui.Button(app, "New", command=None, x=x, y=y)
x += spacing

gui.Button(app, "Open", command=None, x=x, y=y)
x += spacing

gui.Button(app, "Save", command=None, x=x, y=y)
x += spacing

gui.Button(app, "Exit", command=None, x=x, y=y)

app.run()
```

### Grid Layout

Create a grid of widgets:

```python
import CocoaGUI as gui

app = gui.Window("Grid Layout", width=450, height=400)

start_x = 50
start_y = 50
cell_width = 120
cell_height = 80

# Create a 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        x = start_x + (col * cell_width)
        y = start_y + (row * cell_height)
        
        label = f"R{row+1}C{col+1}"
        gui.Button(app, label, command=None, x=x, y=y)

app.run()
```

### Form Layout

Labels on the left, inputs on the right:

```python
import CocoaGUI as gui

app = gui.Window("Form Layout", width=450, height=400)

label_x = 50
input_x = 150
start_y = 50
row_height = 60

# Row 1
gui.Label(app, "First Name:", x=label_x, y=start_y)
gui.Input(app, x=input_x, y=start_y-3, width=250)

# Row 2
gui.Label(app, "Last Name:", x=label_x, y=start_y + row_height)
gui.Input(app, x=input_x, y=start_y + row_height - 3, width=250)

# Row 3
gui.Label(app, "Email:", x=label_x, y=start_y + row_height*2)
gui.Input(app, x=input_x, y=start_y + row_height*2 - 3, width=250)

# Row 4
gui.Label(app, "Phone:", x=label_x, y=start_y + row_height*3)
gui.Input(app, x=input_x, y=start_y + row_height*3 - 3, width=250)

# Submit button centered below form
gui.Button(app, "Submit", command=None, x=180, y=start_y + row_height*4 + 20)

app.run()
```

### Sidebar Layout

Sidebar on the left, main content on the right:

```python
import CocoaGUI as gui

app = gui.Window("Sidebar Layout", width=700, height=500)

sidebar_width = 150
sidebar_x = 20
content_x = sidebar_width + 40

# Sidebar title
gui.Label(app, "Menu", x=sidebar_x + 40, y=20, size=14)

# Sidebar buttons (vertical stack)
button_y = 60
for label in ["Home", "Profile", "Settings", "Help", "Exit"]:
    gui.Button(app, label, command=None, x=sidebar_x, y=button_y)
    button_y += 50

# Content area
gui.Label(app, "Main Content Area", x=content_x, y=20, size=16)
gui.TextArea(app, x=content_x, y=60, width=480, height=400)

app.run()
```

### Header-Body-Footer Layout

```python
import CocoaGUI as gui

app = gui.Window("Three Section Layout", width=600, height=500)

# Header
header_y = 20
gui.Label(app, "Application Title", x=220, y=header_y, size=18)

# Body
body_y = 70
gui.TextArea(app, x=20, y=body_y, width=560, height=350)

# Footer
footer_y = 440
gui.Label(app, "Status: Ready", x=20, y=footer_y, size=10)
gui.Button(app, "Action", command=None, x=480, y=footer_y-5)

app.run()
```

## Centering Widgets

### Horizontal Centering

Calculate the center position:

```python
window_width = 400
widget_width = 200

# Center horizontally
x = (window_width - widget_width) // 2

gui.Input(app, x=x, y=100, width=widget_width)
```

### Center a Button

```python
window_width = 400
button_width = 60  # Approximate button width

x = (window_width - button_width) // 2

gui.Button(app, "Click", command=None, x=x, y=150)
```

### Center Text Label

Text centering requires estimating text width:

```python
text = "Hello, World!"
font_size = 14
# Rough estimate: 7-8 pixels per character at size 12-14
char_width = 8

text_width = len(text) * char_width
window_width = 400

x = (window_width - text_width) // 2

gui.Label(app, text, x=x, y=100, size=font_size)
```

## Spacing Guidelines

### Recommended Spacing

- **Margin from window edge**: 10-20 pixels
- **Between related widgets**: 5-10 pixels
- **Between widget groups**: 20-30 pixels
- **Between rows in forms**: 40-60 pixels

### Example with Good Spacing

```python
import CocoaGUI as gui

app = gui.Window("Good Spacing", width=450, height=350)

margin = 20
group_spacing = 30
item_spacing = 40

y = margin

# Group 1: Personal Info
gui.Label(app, "Personal Information", x=margin, y=y, size=14)
y += group_spacing

gui.Label(app, "Name:", x=margin, y=y)
gui.Input(app, x=margin + 100, y=y, width=300)
y += item_spacing

gui.Label(app, "Age:", x=margin, y=y)
gui.Input(app, x=margin + 100, y=y, width=100)
y += item_spacing + group_spacing

# Group 2: Contact Info
gui.Label(app, "Contact Information", x=margin, y=y, size=14)
y += group_spacing

gui.Label(app, "Email:", x=margin, y=y)
gui.Input(app, x=margin + 100, y=y, width=300)
y += item_spacing

gui.Label(app, "Phone:", x=margin, y=y)
gui.Input(app, x=margin + 100, y=y, width=300)

app.run()
```

## Responsive Design Workarounds

CocoaGUI uses fixed positioning, but you can make layouts more flexible:

### Calculate Positions from Window Size

```python
import CocoaGUI as gui

width = 600
height = 400

app = gui.Window("Flexible Layout", width=width, height=height)

# Calculate positions based on window size
margin = 20
center_x = width // 2
center_y = height // 2

# Center a button
button_width = 80
button_x = center_x - (button_width // 2)

gui.Button(app, "Centered", command=None, x=button_x, y=center_y)

# Bottom-right button
gui.Button(app, "Exit", command=None, x=width-100, y=height-60)

app.run()
```

### Use Variables for Maintainability

```python
import CocoaGUI as gui

app = gui.Window("Maintainable Layout", width=500, height=400)

# Define layout constants
MARGIN = 20
LABEL_WIDTH = 100
INPUT_WIDTH = 350
ROW_HEIGHT = 50

# Calculate x positions
label_x = MARGIN
input_x = MARGIN + LABEL_WIDTH + 10

# Calculate y positions
y = MARGIN
for field in ["Name", "Email", "Address", "City", "Country"]:
    gui.Label(app, f"{field}:", x=label_x, y=y)
    gui.Input(app, x=input_x, y=y, width=INPUT_WIDTH)
    y += ROW_HEIGHT

app.run()
```

## Common Layout Mistakes

### Too Close to Edges

```python
# ❌ Bad: No margin
gui.Label(app, "Text", x=0, y=0)

# ✅ Good: Proper margin
gui.Label(app, "Text", x=20, y=20)
```

### Inconsistent Spacing

```python
# ❌ Bad: Random spacing
gui.Label(app, "Name:", x=50, y=40)
gui.Input(app, x=120, y=38, width=200)
gui.Label(app, "Email:", x=50, y=95)  # Random jump
gui.Input(app, x=125, y=92, width=200)  # Different offset

# ✅ Good: Consistent spacing
spacing = 50
y = 40

gui.Label(app, "Name:", x=50, y=y)
gui.Input(app, x=120, y=y, width=200)

y += spacing

gui.Label(app, "Email:", x=50, y=y)
gui.Input(app, x=120, y=y, width=200)
```

### Hardcoded Positions

```python
# ❌ Bad: Magic numbers everywhere
gui.Button(app, "OK", command=None, x=237, y=418)

# ✅ Good: Calculated positions
window_width = 500
window_height = 450
button_width = 60

x = (window_width - button_width) // 2
y = window_height - 50

gui.Button(app, "OK", command=None, x=x, y=y)
```

## Layout Planning Tips

1. **Sketch first**: Draw your layout on paper before coding
2. **Use constants**: Define margins, spacing as variables
3. **Group related widgets**: Keep related items close together
4. **Leave breathing room**: Don't cram everything together
5. **Test different window sizes**: Make sure it looks good
6. **Align elements**: Line up widgets for visual clarity
7. **Use consistent spacing**: Same spacing for similar elements

## Advanced Techniques

### Dynamic Positioning

Create widgets in loops with calculated positions:

```python
import CocoaGUI as gui

app = gui.Window("Dynamic Layout", width=600, height=400)

items = ["Home", "About", "Services", "Products", "Contact"]

start_x = 50
y = 100
spacing = 100

for i, item in enumerate(items):
    x = start_x + (i * spacing)
    gui.Button(app, item, command=None, x=x, y=y)

app.run()
```

### Reusable Layout Functions

```python
def create_form_row(app, label_text, y_position):
    """Create a label-input row"""
    gui.Label(app, label_text, x=50, y=y_position)
    input_field = gui.Input(app, x=150, y=y_position, width=300)
    return input_field

# Use it
name = create_form_row(app, "Name:", 50)
email = create_form_row(app, "Email:", 100)
phone = create_form_row(app, "Phone:", 150)
```

## See Also

- [Best Practices](best-practices.md) - General UI design tips
- [Window API](../api/window.md) - Window configuration
- [Examples](../examples/calculator.md) - Real-world layouts