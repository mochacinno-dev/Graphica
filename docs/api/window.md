# Window

The `Window` class creates the main application window that holds all your widgets.

## Constructor

```python
Window(title="GUI Window", width=400, height=300)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `title` | str | "GUI Window" | The window title shown in the title bar |
| `width` | int | 400 | Window width in pixels |
| `height` | int | 300 | Window height in pixels |

### Returns

A `Window` object that serves as the parent for all widgets.

## Methods

### run()

Start the application's event loop. This must be called to display the window and make it interactive.

```python
app.run()
```

!!! warning
    This method blocks execution. Place it at the end of your script.

### close()

Programmatically close the window and end the application.

```python
app.close()
```

## Attributes

### root

Access the underlying tkinter root window for advanced customization.

```python
app.root.configure(bg='white')  # Change background color
```

!!! tip
    For most use cases, you won't need to access `root` directly.

## Examples

### Basic Window

```python
import CocoaGUI as gui

app = gui.Window("My App", width=500, height=400)
app.run()
```

### Custom Size Window

```python
import CocoaGUI as gui

# Small window
small_app = gui.Window("Small", width=300, height=200)

# Large window
large_app = gui.Window("Large", width=1200, height=800)

small_app.run()
```

### Window with Exit Confirmation

```python
import CocoaGUI as gui

app = gui.Window("Confirm Exit", width=400, height=300)

def on_exit():
    if gui.confirm("Are you sure you want to exit?", "Exit"):
        app.close()

gui.Button(app, "Exit", command=on_exit, x=150, y=130)

app.run()
```

### Multiple Windows (Not Recommended)

While technically possible, CocoaGUI is designed for single-window applications:

```python
import CocoaGUI as gui

# This works but is not the intended use case
app1 = gui.Window("Window 1", width=300, height=200)
gui.Label(app1, "First Window", x=100, y=80)

# Only the last .run() call will execute
app1.run()
```

!!! note
    For complex multi-window applications, consider using tkinter directly or another framework.

## Best Practices

### ✅ Do

- Create one window per application
- Set appropriate dimensions for your content
- Call `run()` at the end of your script
- Use descriptive window titles

### ❌ Don't

- Create multiple windows in one application
- Make windows too small (minimum 200x150 recommended)
- Call `run()` multiple times
- Forget to call `run()` - your window won't appear!

## Common Issues

### Window doesn't appear

Make sure you called `app.run()` at the end:

```python
app = gui.Window("Test", width=400, height=300)
# Add your widgets here
app.run()  # Don't forget this!
```

### Window is too small/large

Adjust the `width` and `height` parameters:

```python
# Calculate based on your widgets
app = gui.Window("My App", width=600, height=400)
```

## See Also

- [Button](button.md) - Add interactive buttons
- [Label](label.md) - Display text
- [Layout Guide](../guide/layout.md) - Positioning widgets