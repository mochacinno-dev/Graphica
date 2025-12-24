import CocoaGUI as gui
from tkinter import filedialog

app = gui.Window("CocoEdit", width=800, height=600)

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
        "CocoEdit (Cocoa GUI Text Editor) v1.0\n\n"
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