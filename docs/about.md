# About CocoaGUI

CocoaGUI is a Python GUI library designed to make desktop application development accessible to everyone.

## The Story

GUI programming has a reputation for being complicated. Complex frameworks, verbose syntax, and steep learning curves have kept many developers from building desktop applications. CocoaGUI was created to change that.

The goal was simple: create a library where building a GUI feels as natural as writing any other Python code. No complicated layouts, no confusing inheritance hierarchies, no hundred-page manuals. Just straightforward, readable code that does what you expect.

## Design Philosophy

### Simplicity First

Every design decision in CocoaGUI prioritizes simplicity over flexibility. The library intentionally does less so that you can do more.

```python
# One line to create a button
gui.Button(app, "Click Me", command=my_function, x=100, y=50)
```

No classes to inherit, no complex configuration, no surprises.

### Readable Code

CocoaGUI code reads like instructions for a human, not just a computer:

```python
# You can understand what this does without documentation
gui.Label(app, "Welcome!", x=150, y=50, size=16)
name = gui.Input(app, x=100, y=100, width=300)
gui.Button(app, "Submit", command=submit, x=180, y=150)
```

### Beginner Friendly

CocoaGUI is designed for Python beginners. If you understand functions and variables, you can build GUI applications.

## What CocoaGUI Is

**CocoaGUI is for:**

- Learning GUI programming concepts
- Building simple desktop tools quickly
- Creating prototypes and proof-of-concepts
- Teaching Python to beginners
- Personal projects and utilities
- Small business applications

**Example use cases:**

- Todo list managers
- Note-taking apps
- Simple calculators
- Form-based data entry tools
- Configuration utilities
- Text editors
- Personal organizers

## What CocoaGUI Isn't

CocoaGUI makes trade-offs for simplicity. It's not designed for:

- Complex, production-grade applications
- Advanced layout management
- Custom themes and styling
- Mobile or web interfaces
- Games or graphics-intensive applications
- Applications requiring complex widgets

For those needs, consider tkinter directly, PyQt, or other specialized frameworks.

## Technical Details

### Built on tkinter

CocoaGUI is a wrapper around Python's built-in tkinter library. This means:

- **No external dependencies** - works out of the box with Python
- **Cross-platform** - runs on Windows, macOS, and Linux
- **Stable** - tkinter has been around for decades
- **Familiar** - uses standard GUI patterns

### Absolute Positioning

Unlike many GUI frameworks, CocoaGUI uses absolute positioning with x/y coordinates. This:

- **Simplifies** the learning curve (no layout managers to learn)
- **Makes positioning predictable** (you control exactly where things go)
- **Trades flexibility** for simplicity (responsive layouts require more work)

### Single-File Design

CocoaGUI is intentionally kept as a single file (`CocoaGUI.py`). You can:

- Drop it directly into your project
- Understand the entire codebase
- Modify it for your specific needs
- Learn how GUI libraries work under the hood

## Project Status

CocoaGUI is a focused, stable project. It does what it's designed to do and doesn't try to do more.

**Current status:** Stable and feature-complete for its intended use cases.

**Version:** 1.0

**Python compatibility:** Python 3.6+

## Contributing

CocoaGUI is intentionally minimal, but improvements are welcome:

- **Bug fixes** - definitely report these
- **Documentation improvements** - always appreciated
- **Example applications** - help others learn
- **Teaching materials** - tutorials, videos, guides

The goal is not to add features, but to make what exists work perfectly and be perfectly understandable.

## License

CocoaGUI is released under the GNU General Public License v3.0 (GPL-3.0).

This means:

- ✅ **Free to use** for any purpose
- ✅ **Free to modify** and customize
- ✅ **Free to distribute** your modifications
- ⚠️ **Share-alike** - derivatives must also be GPL-3.0

See the [LICENSE](../LICENSE) file for full details.

## Author

Created by **Camila "Mocha" Rose**

CocoaGUI was born from teaching Python to beginners and watching them struggle with existing GUI frameworks. It's built with love for simplicity and a deep respect for people just starting their programming journey.

## Acknowledgments

CocoaGUI builds on the excellent work of:

- The Python Software Foundation and the tkinter developers
- Everyone who makes beginner-friendly programming education possible
- The thousands of developers who've asked "isn't there a simpler way?"

## Philosophy in Practice

The best code is code that doesn't need to be written. The second best is code that anyone can read and understand.

CocoaGUI aims to be the second best.

---

*Happy coding! May your GUIs be simple and your users delighted.*