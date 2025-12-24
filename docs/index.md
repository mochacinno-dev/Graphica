# Welcome to CocoaGUI

**The simplest Python GUI library ever created.**

CocoaGUI makes building desktop applications incredibly easy. No complex setup, no confusing APIs - just clean, intuitive Python code that anyone can understand.

## Why Cocoa?

**Simple Syntax** - Create widgets in one line with intuitive parameters

**Fast Development** - Build complete applications in minutes, not hours

**Easy to Learn** - If you know basic Python, you already know CocoaGUI

**Clean Code** - Your GUI code is readable and maintainable

## Quick Example

```python
import CocoaGUI as gui

# Create a window
app = gui.Window("My App", width=400, height=300)

# Add widgets
gui.Label(app, "Enter your name:", x=20, y=20)
name_input = gui.Input(app, x=20, y=50, width=300)

def greet():
    name = name_input.get()
    gui.alert(f"Hello, {name}!")

gui.Button(app, "Greet", command=greet, x=20, y=90)

# Run the app
app.run()
```

That's it! Just 13 lines to create a working GUI application.

## Key Features

- **Window** - Create application windows with custom sizes
- **Button** - Interactive buttons with click handlers
- **Label** - Display text with customizable sizes
- **Input** - Single-line text input fields
- **TextArea** - Multi-line text editing
- **CheckBox** - Toggle checkboxes with state management
- **Utilities** - Alert and confirmation dialogs

## Get Started

Ready to build something amazing? Head over to the [Installation Guide](getting-started/installation.md) to get started!

## Philosophy

CocoaGUI was designed with one goal: **make GUI development as simple as possible**.