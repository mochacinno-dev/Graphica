# Text Editor Example

A complete text editor application demonstrating file operations, real-time updates, and practical UI patterns. This is a real-world example you can actually use.

## Features

- Create, open, and save text files
- Real-time character, word, and line counting
- Clean, intuitive interface
- File dialog integration
- Status bar with current file info

## Complete Code

```python
import CocoaGUI as gui
from tkinter import filedialog

app = gui.Window("CocoaGUI Text Editor", width=800, height=600)

# Status bar
status_label = gui.Label(app, "New Document - Ready", x=10, y=10, size=10)

# Track current file
current_file = None

# Main text editor
text_editor = gui.TextArea(app, x=10, y=40, width=780, height=480)

# Statistics display
char_count_label = gui.Label(app, "Characters: 0", x=10, y=535, size=9)
word_count_label = gui.Label(app, "Words: 0", x=150, y=535, size=9)
line_count_label = gui.Label(app, "Lines: 1", x=250, y=535, size=9)

def update_counts():
    """Update statistics every 500ms"""
    content = text_editor.get()
    
    # Character count (excluding trailing newline)
    chars = len(content.rstrip('\n'))
    char_count_label.set(f"Characters: {chars}")
    
    # Word count
    words = len(content.split()) if content.strip() else 0
    word_count_label.set(f"Words: {words}")
    
    # Line count
    lines = content.count('\n')
    line_count_label.set(f"Lines: {lines}")
    
    # Schedule next update
    app.root.after(500, update_counts)

def new_file():
    """Create a new document"""
    global current_file
    
    if gui.confirm("Create new file? Unsaved changes will be lost.", "New File"):
        text_editor.clear()
        current_file = None
        status_label.set("New Document - Ready")
        gui.alert("New document created!", "Success")

def open_file():
    """Open an existing file"""
    global current_file
    
    filename = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if filename:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            text_editor.set(content)
            current_file = filename
            status_label.set(f"Opened: {filename}")
            gui.alert(f"File opened successfully!\n{filename}", "Success")
        except Exception as e:
            gui.alert(f"Error opening file:\n{str(e)}", "Error")

def save_file():
    """Save the current file"""
    global current_file
    
    if current_file:
        try:
            content = text_editor.get()
            with open(current_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            status_label.set(f"Saved: {current_file}")
            gui.alert("File saved successfully!", "Success")
        except Exception as e:
            gui.alert(f"Error saving file:\n{str(e)}", "Error")
    else:
        save_file_as()

def save_file_as():
    """Save with a new filename"""
    global current_file
    
    filename = filedialog.asksaveasfilename(
        title="Save File As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if filename:
        try:
            content = text_editor.get()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            current_file = filename
            status_label.set(f"Saved: {filename}")
            gui.alert(f"File saved successfully!\n{filename}", "Success")
        except Exception as e:
            gui.alert(f"Error saving file:\n{str(e)}", "Error")

def clear_text():
    """Clear all text"""
    if gui.confirm("Clear all text? This cannot be undone.", "Clear"):
        text_editor.clear()
        status_label.set("Text cleared - Ready")

def about():
    """Show about dialog"""
    gui.alert(
        "CocoaGUI Text Editor v1.0\n\n"
        "A simple text editor built with CocoaGUI.\n\n"
        "Features:\n"
        "• Create, open, and save text files\n"
        "• Real-time statistics\n"
        "• Clean interface",
        "About"
    )

# Menu buttons
gui.Button(app, "New", command=new_file, x=10, y=565)
gui.Button(app, "Open", command=open_file, x=80, y=565)
gui.Button(app, "Save", command=save_file, x=150, y=565)
gui.Button(app, "Save As", command=save_file_as, x=220, y=565)
gui.Button(app, "Clear", command=clear_text, x=310, y=565)
gui.Button(app, "About", command=about, x=390, y=565)

# Help text
gui.Label(app, "Start typing or open a file to begin", x=480, y=570, size=9)

# Start statistics updater
update_counts()

app.run()
```

## How It Works

### File Management

The editor tracks the current file in a global variable:

```python
current_file = None  # No file when starting

# After opening or saving:
current_file = "/path/to/file.txt"
```

This allows:
- **Save** to overwrite the current file
- **Save As** to create a new file
- Status bar to show which file is open

### Real-time Statistics

The `update_counts()` function runs every 500ms:

```python
def update_counts():
    content = text_editor.get()
    
    # Count characters, words, lines
    chars = len(content.rstrip('\n'))
    words = len(content.split())
    lines = content.count('\n')
    
    # Update labels
    char_count_label.set(f"Characters: {chars}")
    # ... etc
    
    # Schedule next update
    app.root.after(500, update_counts)
```

This pattern is useful for any real-time updates in your app.

### File Dialogs

CocoaGUI uses tkinter's file dialogs for file operations:

```python
from tkinter import filedialog

# Open file dialog
filename = filedialog.askopenfilename(
    title="Open File",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

# Save file dialog
filename = filedialog.asksaveasfilename(
    title="Save File As",
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)
```

### Error Handling

Always wrap file operations in try-except:

```python
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Success!
except Exception as e:
    gui.alert(f"Error: {str(e)}", "Error")
```

## Key Learning Points

### 1. Global State Management

```python
current_file = None  # Global variable

def save_file():
    global current_file  # Access global
    # Use and modify current_file
```

Use globals sparingly, but they're fine for simple apps like this.

### 2. Scheduled Updates

```python
def update_function():
    # Do something
    app.root.after(500, update_function)  # Run again in 500ms

# Start the loop
update_function()
```

This pattern is perfect for live updates, timers, animations, etc.

### 3. Confirmation Before Destructive Actions

```python
if gui.confirm("Clear all text?", "Confirm"):
    text_editor.clear()
```

Always ask before deleting or clearing user data.

### 4. Status Feedback

```python
status_label.set(f"Saved: {filename}")
```

Keep users informed about what's happening.

## Possible Improvements

Here are ways you could extend this editor:

### 1. Find and Replace

```python
def find_text():
    search = gui.Input(...)
    # Search through text_editor.get()
    # Highlight matches
```

### 2. Word Wrap Toggle

```python
def toggle_wrap():
    current = text_editor.widget.cget('wrap')
    new_wrap = 'none' if current == 'word' else 'word'
    text_editor.widget.configure(wrap=new_wrap)
```

### 3. Font Size Controls

```python
def increase_font():
    current_font = text_editor.widget.cget('font')
    # Parse and increase size
    text_editor.widget.configure(font=new_font)
```

### 4. Undo/Redo

```python
history = []

def save_to_history():
    history.append(text_editor.get())

def undo():
    if history:
        text_editor.set(history.pop())
```

### 5. Auto-save

```python
def auto_save():
    if current_file:
        save_file()
    app.root.after(60000, auto_save)  # Every minute

auto_save()
```

### 6. Syntax Highlighting

```python
def highlight_python():
    content = text_editor.get()
    # Use regex to find keywords
    # Apply text tags for colors
```

### 7. Recent Files

```python
recent_files = []

def add_to_recent(filename):
    if filename not in recent_files:
        recent_files.insert(0, filename)
        recent_files = recent_files[:5]  # Keep 5 most recent
```

## Usage Tips

### Keyboard Shortcuts

While CocoaGUI doesn't have built-in keyboard shortcut support, tkinter does:

```python
app.root.bind('<Control-s>', lambda e: save_file())
app.root.bind('<Control-o>', lambda e: open_file())
app.root.bind('<Control-n>', lambda e: new_file())
```

### Window Closing Handler

Warn about unsaved changes:

```python
def on_closing():
    if gui.confirm("Exit? Unsaved changes will be lost.", "Exit"):
        app.close()

app.root.protocol("WM_DELETE_WINDOW", on_closing)
```

### Larger Text Area

For a full-screen editor:

```python
text_editor = gui.TextArea(app, x=0, y=30, width=800, height=540)
```

## Design Patterns Used

**Status Bar Pattern**: Keep users informed with a status label at the top.

**Toolbar Pattern**: Row of buttons for common actions.

**Statistics Panel**: Show live information at the bottom.

**Global State**: Simple state management for current file.

**Scheduled Updates**: Regular polling for live statistics.

## See Also

- [TextArea API](../api/textarea.md) - Complete TextArea documentation
- [Calculator Example](calculator.md) - Another complete application
- [File I/O Guide](../guide/best-practices.md) - Best practices for file handling