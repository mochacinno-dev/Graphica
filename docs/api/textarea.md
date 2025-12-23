# TextArea

The TextArea widget provides a multi-line text editing area. Perfect for notes, comments, code editors, chat interfaces, or any situation where users need to enter more than a single line of text.

## Constructor

```python
TextArea(parent, x=10, y=10, width=300, height=150)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Window | Required | The parent window |
| `x` | int | 10 | X-coordinate in pixels |
| `y` | int | 10 | Y-coordinate in pixels |
| `width` | int | 300 | Width in pixels |
| `height` | int | 150 | Height in pixels |

### Returns

A `TextArea` object.

## Methods

### get()

Retrieve all text from the text area, including line breaks.

```python
text = textarea.get()
```

#### Returns
- `str`: The complete text content with newline characters

### set(text)

Replace the entire contents of the text area.

```python
textarea.set("New content here\nWith multiple lines")
```

#### Parameters
- `text` (str): The text to set (can include `\n` for line breaks)

### clear()

Remove all text from the text area.

```python
textarea.clear()
```

## Examples

### Basic TextArea

```python
import Graphica as gui

app = gui.Window("Text Editor", width=600, height=400)

gui.Label(app, "Write your notes:", x=20, y=20, size=12)
notes = gui.TextArea(app, x=20, y=50, width=560, height=300)

app.run()
```

### Simple Note-Taking App

```python
import Graphica as gui

app = gui.Window("Quick Notes", width=600, height=450)

gui.Label(app, "Quick Notes", x=250, y=15, size=16)

notes = gui.TextArea(app, x=20, y=50, width=560, height=300)
notes.set("Start typing your notes here...")

def save_notes():
    content = notes.get()
    if content.strip():
        gui.alert("Notes saved to memory!", "Saved")
    else:
        gui.alert("No notes to save", "Empty")

def clear_notes():
    if gui.confirm("Clear all notes?", "Confirm"):
        notes.clear()

gui.Button(app, "Save", command=save_notes, x=200, y=370)
gui.Button(app, "Clear", command=clear_notes, x=290, y=370)

app.run()
```

### Character Counter

```python
import Graphica as gui

app = gui.Window("Character Counter", width=600, height=450)

gui.Label(app, "Text Analysis", x=240, y=15, size=16)

text = gui.TextArea(app, x=20, y=50, width=560, height=280)

char_label = gui.Label(app, "Characters: 0", x=20, y=350, size=11)
word_label = gui.Label(app, "Words: 0", x=150, y=350, size=11)
line_label = gui.Label(app, "Lines: 0", x=250, y=350, size=11)

def analyze():
    content = text.get()
    
    # Count characters (excluding trailing newline)
    chars = len(content.rstrip('\n'))
    
    # Count words
    words = len(content.split()) if content.strip() else 0
    
    # Count lines
    lines = content.count('\n')
    
    char_label.set(f"Characters: {chars}")
    word_label.set(f"Words: {words}")
    line_label.set(f"Lines: {lines}")

gui.Button(app, "Analyze", command=analyze, x=260, y=390)

app.run()
```

### Text Transformation Tool

```python
import Graphica as gui

app = gui.Window("Text Transformer", width=700, height=500)

gui.Label(app, "Original Text:", x=20, y=20, size=12)
original = gui.TextArea(app, x=20, y=45, width=660, height=180)

gui.Label(app, "Transformed Text:", x=20, y=245, size=12)
transformed = gui.TextArea(app, x=20, y=270, width=660, height=180)

def to_uppercase():
    text = original.get()
    transformed.set(text.upper())

def to_lowercase():
    text = original.get()
    transformed.set(text.lower())

def reverse_text():
    text = original.get()
    transformed.set(text[::-1])

def word_count():
    text = original.get()
    words = len(text.split())
    transformed.set(f"This text contains {words} words.")

gui.Button(app, "UPPERCASE", command=to_uppercase, x=100, y=465)
gui.Button(app, "lowercase", command=to_lowercase, x=220, y=465)
gui.Button(app, "Reverse", command=reverse_text, x=340, y=465)
gui.Button(app, "Count Words", command=word_count, x=440, y=465)

app.run()
```

### Simple Journal Entry

```python
import Graphica as gui
from datetime import datetime

app = gui.Window("Daily Journal", width=650, height=500)

gui.Label(app, "Daily Journal Entry", x=240, y=15, size=16)

date_label = gui.Label(app, datetime.now().strftime("%B %d, %Y"), 
                       x=260, y=45, size=11)

entry = gui.TextArea(app, x=25, y=80, width=600, height=350)

entries = []

def save_entry():
    content = entry.get().strip()
    if not content:
        gui.alert("Please write something first!", "Empty Entry")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries.append(f"[{timestamp}]\n{content}\n")
    
    gui.alert("Journal entry saved!", "Saved")
    entry.clear()

def view_entries():
    if not entries:
        gui.alert("No entries yet!", "Empty Journal")
        return
    
    all_entries = "\n---\n".join(entries)
    entry.set(all_entries)

gui.Button(app, "Save Entry", command=save_entry, x=220, y=450)
gui.Button(app, "View All", command=view_entries, x=330, y=450)

app.run()
```

### Code Snippet Manager

```python
import Graphica as gui

app = gui.Window("Code Snippets", width=700, height=550)

gui.Label(app, "Code Snippet Manager", x=260, y=15, size=16)

gui.Label(app, "Snippet Name:", x=25, y=50, size=11)
name = gui.Input(app, x=140, y=50, width=400)

gui.Label(app, "Code:", x=25, y=85, size=11)
code = gui.TextArea(app, x=25, y=110, width=650, height=350)

snippets = {}

def save_snippet():
    snippet_name = name.get().strip()
    snippet_code = code.get().strip()
    
    if not snippet_name:
        gui.alert("Please enter a snippet name", "Error")
        return
    
    if not snippet_code:
        gui.alert("Please enter some code", "Error")
        return
    
    snippets[snippet_name] = snippet_code
    gui.alert(f"Saved snippet: {snippet_name}", "Success")
    name.clear()
    code.clear()

def list_snippets():
    if not snippets:
        gui.alert("No snippets saved yet", "Empty")
        return
    
    snippet_list = "\n\n".join([f"=== {n} ===\n{c}" 
                                 for n, c in snippets.items()])
    code.set(snippet_list)

gui.Button(app, "Save Snippet", command=save_snippet, x=250, y=480)
gui.Button(app, "View All", command=list_snippets, x=370, y=480)

app.run()
```

### Markdown Preview (Simplified)

```python
import Graphica as gui

app = gui.Window("Markdown Editor", width=800, height=600)

gui.Label(app, "Markdown Input:", x=20, y=20, size=12)
markdown = gui.TextArea(app, x=20, y=50, width=360, height=450)

markdown.set("# Welcome\n\nWrite your **markdown** here!\n\n- Item 1\n- Item 2")

gui.Label(app, "Preview:", x=420, y=20, size=12)
preview = gui.TextArea(app, x=420, y=50, width=360, height=450)

def update_preview():
    # Simple markdown-like preview (not full markdown)
    text = markdown.get()
    
    # Replace # headers
    text = text.replace("# ", "[H1] ")
    text = text.replace("## ", "[H2] ")
    
    # Replace **bold**
    while "**" in text:
        text = text.replace("**", "[B]", 1).replace("**", "[/B]", 1)
    
    preview.set(text)

gui.Button(app, "Update Preview", command=update_preview, x=330, y=520)

app.run()
```

### Chat Interface

```python
import Graphica as gui
from datetime import datetime

app = gui.Window("Simple Chat", width=600, height=550)

gui.Label(app, "Chat Room", x=260, y=15, size=16)

# Chat history display
chat_display = gui.TextArea(app, x=20, y=50, width=560, height=380)
chat_display.set("Welcome to the chat!\n")

# Message input
gui.Label(app, "Your message:", x=20, y=445, size=11)
message_input = gui.Input(app, x=130, y=445, width=350)

def send_message():
    msg = message_input.get().strip()
    if not msg:
        return
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    current_chat = chat_display.get()
    new_message = f"[{timestamp}] You: {msg}\n"
    
    chat_display.set(current_chat + new_message)
    message_input.clear()

gui.Button(app, "Send", command=send_message, x=490, y=442)

app.run()
```

## Working with Text Content

### Reading Line by Line

```python
content = textarea.get()
lines = content.split('\n')

for line in lines:
    print(line)
```

### Appending Text

```python
current = textarea.get()
new_line = "New text here"
textarea.set(current + new_line + "\n")
```

### Replacing Text

```python
content = textarea.get()
modified = content.replace("old", "new")
textarea.set(modified)
```

### Finding Text

```python
content = textarea.get()
if "search term" in content:
    gui.alert("Found!", "Search")
else:
    gui.alert("Not found", "Search")
```

## Best Practices

**Size appropriately for content.** Make the TextArea large enough for users to comfortably read and edit their text without excessive scrolling.

**Provide clear context.** Use labels to explain what the TextArea is for.

**Consider default text.** Helpful placeholder text can guide users, but make sure it's clearly different from actual content.

**Handle line breaks.** Remember that `get()` returns text with `\n` characters. Process them appropriately for your needs.

**Scrolling is automatic.** TextArea automatically provides scrollbars when content exceeds the visible area.

**Save user work.** For text editors or note apps, consider implementing auto-save or warning users before clearing content.

## Common Patterns

### Template System

```python
templates = {
    "Letter": "Dear [Name],\n\nBest regards,\n[Your Name]",
    "Email": "Subject: \n\nHi,\n\n\n\nThanks,",
    "Code": "def function_name():\n    # Your code here\n    pass"
}

def load_template(template_name):
    textarea.set(templates[template_name])
```

### Undo Functionality (Simple)

```python
history = []

def save_to_history():
    current = textarea.get()
    history.append(current)

def undo():
    if len(history) > 0:
        previous = history.pop()
        textarea.set(previous)
```

## See Also

- [Input](input.md) - Single-line text input
- [Label](label.md) - Display text
- [Text Editor Example](../examples/text-editor.md) - Complete implementation
- [Best Practices Guide](../guide/best-practices.md)