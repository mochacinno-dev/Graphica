"""
Simple Text Editor Application
Using the Graphica GUI Library
"""

import Graphica as gui
from tkinter import filedialog

# Create the main window
app = gui.Window("Graphica Text Editor", width=800, height=600)

# Status bar at the top
status_label = gui.Label(app, "New Document - Ready", x=10, y=10, size=10)

# File path tracking
current_file = None

# Main text area for editing
text_editor = gui.TextArea(app, x=10, y=40, width=780, height=480)

# Character and word count labels
char_count_label = gui.Label(app, "Characters: 0", x=10, y=535, size=9)
word_count_label = gui.Label(app, "Words: 0", x=150, y=535, size=9)
line_count_label = gui.Label(app, "Lines: 1", x=250, y=535, size=9)

def update_counts():
    """Update character, word, and line counts"""
    content = text_editor.get()
    
    # Character count (excluding the trailing newline tkinter adds)
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
    """Create a new file"""
    global current_file
    
    if gui.confirm("Create new file? Any unsaved changes will be lost.", "New File"):
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
    """Save the file with a new name"""
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
    """Clear all text from the editor"""
    if gui.confirm("Clear all text? This cannot be undone.", "Clear Text"):
        text_editor.clear()
        status_label.set("Text cleared - Ready")

def find_text():
    """Simple find text function"""
    search_term = gui.confirm("Feature coming soon!", "Find Text")

def about():
    """Show about dialog"""
    gui.alert(
        "Graphica Text Editor v1.0\n\n"
        "A simple and elegant text editor\n"
        "built with the Graphica GUI Library.\n\n"
        "Features:\n"
        "• Create, open, and save text files\n"
        "• Real-time character/word/line count\n"
        "• Clean and intuitive interface",
        "About Graphica Text Editor"
    )

# Menu buttons
gui.Button(app, "New", command=new_file, x=10, y=565)
gui.Button(app, "Open", command=open_file, x=80, y=565)
gui.Button(app, "Save", command=save_file, x=150, y=565)
gui.Button(app, "Save As", command=save_file_as, x=220, y=565)
gui.Button(app, "Clear", command=clear_text, x=310, y=565)
gui.Button(app, "About", command=about, x=390, y=565)

# Instructions label
gui.Label(app, "Start typing or open a file to begin editing!", x=480, y=570, size=9)

# Start the count updater
update_counts()

# Run the application
app.run()