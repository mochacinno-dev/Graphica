# Installation

Getting CocoaGUI up and running is incredibly simple!

## Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

## Verify tkinter Installation

CocoaGUI uses tkinter, which is included with most Python installations. To verify you have it:

```python
python -m tkinter
```

If a small window appears, you're good to go! If not, see the troubleshooting section below.

## Installing CocoaGUI

### Method 1: Download the File

1. Download `CocoaGUI.py` from the [GitHub repository](https://github.com/yourusername/CocoaGUI)
2. Place it in your project folder
3. Import it: `import CocoaGUI as gui`

That's it! No pip install needed.

### Method 2: Clone from GitHub

```bash
git clone https://github.com/yourusername/CocoaGUI.git
cd CocoaGUI
```

Then copy `CocoaGUI.py` to your project directory.

### Method 3: Direct Import (Future)

Once published to PyPI, you'll be able to:

```bash
pip install CocoaGUI
```

## Verify Installation

Create a test file `test.py`:

```python
import CocoaGUI as gui

app = gui.Window("Test", width=300, height=200)
gui.Label(app, "CocoaGUI works!", x=80, y=80, size=16)
app.run()
```

Run it:

```bash
python test.py
```

If a window appears with the text "CocoaGUI works!", you're all set! 🎉

## Troubleshooting

### tkinter Not Found (Linux)

On some Linux distributions, tkinter needs to be installed separately:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

### tkinter Not Found (macOS)

tkinter should come with Python on macOS. If it's missing, reinstall Python from [python.org](https://www.python.org/downloads/).

### tkinter Not Found (Windows)

When installing Python on Windows, make sure "tcl/tk and IDLE" is checked in the installer.

If you already have Python installed, run the installer again and choose "Modify" to add tkinter.

## Next Steps

Now that CocoaGUI is installed, let's create your first app! Continue to the [Quick Start Guide](quickstart.md).