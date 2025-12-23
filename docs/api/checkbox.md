# CheckBox

CheckBox widgets let users toggle options on and off. They're ideal for settings, preferences, feature toggles, or anywhere you need a simple yes/no choice.

## Constructor

```python
CheckBox(parent, text="Checkbox", x=10, y=10, checked=False)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `parent` | Window | Required | The parent window |
| `text` | str | "Checkbox" | Label text displayed next to the checkbox |
| `x` | int | 10 | X-coordinate in pixels |
| `y` | int | 10 | Y-coordinate in pixels |
| `checked` | bool | False | Initial state (checked or unchecked) |

### Returns

A `CheckBox` object.

## Methods

### checked()

Check if the checkbox is currently checked.

```python
if checkbox.checked():
    print("Checkbox is checked")
```

#### Returns
- `bool`: `True` if checked, `False` if unchecked

### check()

Programmatically check the checkbox.

```python
checkbox.check()
```

### uncheck()

Programmatically uncheck the checkbox.

```python
checkbox.uncheck()
```

## Examples

### Basic CheckBox

```python
import Graphica as gui

app = gui.Window("CheckBox Demo", width=400, height=200)

remember = gui.CheckBox(app, "Remember me", x=50, y=70)

def check_status():
    if remember.checked():
        gui.alert("Checkbox is checked!", "Status")
    else:
        gui.alert("Checkbox is unchecked", "Status")

gui.Button(app, "Check Status", command=check_status, x=50, y=110)

app.run()
```

### Pre-checked CheckBox

```python
import Graphica as gui

app = gui.Window("Newsletter", width=400, height=200)

# Start checked
newsletter = gui.CheckBox(app, "Subscribe to newsletter", 
                          x=50, y=70, checked=True)

def subscribe():
    if newsletter.checked():
        gui.alert("You're subscribed!", "Success")
    else:
        gui.alert("Subscription skipped", "Info")

gui.Button(app, "Continue", command=subscribe, x=50, y=110)

app.run()
```

### Settings Panel

```python
import Graphica as gui

app = gui.Window("Application Settings", width=450, height=400)

gui.Label(app, "Application Settings", x=140, y=20, size=16)

# Multiple settings checkboxes
notifications = gui.CheckBox(app, "Enable notifications", x=50, y=70)
auto_save = gui.CheckBox(app, "Auto-save every 5 minutes", x=50, y=110)
dark_mode = gui.CheckBox(app, "Dark mode", x=50, y=150)
show_tips = gui.CheckBox(app, "Show tips on startup", 
                         x=50, y=190, checked=True)
check_updates = gui.CheckBox(app, "Check for updates", 
                             x=50, y=230, checked=True)

status = gui.Label(app, "", x=50, y=310, size=11)

def save_settings():
    settings = {
        "notifications": notifications.checked(),
        "auto_save": auto_save.checked(),
        "dark_mode": dark_mode.checked(),
        "show_tips": show_tips.checked(),
        "check_updates": check_updates.checked()
    }
    
    enabled = sum(settings.values())
    status.set(f"✅ Settings saved! ({enabled} features enabled)")
    gui.alert("Settings have been saved", "Success")

gui.Button(app, "Save Settings", command=save_settings, x=160, y=270)

app.run()
```

### Feature Selector

```python
import Graphica as gui

app = gui.Window("Order Pizza", width=450, height=500)

gui.Label(app, "Build Your Pizza", x=160, y=20, size=16)

gui.Label(app, "Select your toppings:", x=50, y=60, size=12)

# Toppings checkboxes
pepperoni = gui.CheckBox(app, "Pepperoni (+$2)", x=50, y=95)
mushrooms = gui.CheckBox(app, "Mushrooms (+$1.50)", x=50, y=130)
olives = gui.CheckBox(app, "Black Olives (+$1)", x=50, y=165)
onions = gui.CheckBox(app, "Onions (+$1)", x=50, y=200)
peppers = gui.CheckBox(app, "Bell Peppers (+$1.50)", x=50, y=235)
cheese = gui.CheckBox(app, "Extra Cheese (+$2)", x=50, y=270)

total_label = gui.Label(app, "Total: $10.00", x=50, y=340, size=14)
order_summary = gui.Label(app, "", x=50, y=370, size=10)

def calculate_total():
    base_price = 10.00
    total = base_price
    toppings = []
    
    if pepperoni.checked():
        total += 2.00
        toppings.append("Pepperoni")
    if mushrooms.checked():
        total += 1.50
        toppings.append("Mushrooms")
    if olives.checked():
        total += 1.00
        toppings.append("Olives")
    if onions.checked():
        total += 1.00
        toppings.append("Onions")
    if peppers.checked():
        total += 1.50
        toppings.append("Peppers")
    if cheese.checked():
        total += 2.00
        toppings.append("Extra Cheese")
    
    total_label.set(f"Total: ${total:.2f}")
    
    if toppings:
        order_summary.set(f"Toppings: {', '.join(toppings)}")
    else:
        order_summary.set("Toppings: Cheese only")

def place_order():
    calculate_total()
    gui.alert("Order placed! Your pizza is on the way!", "Success")

gui.Button(app, "Calculate Total", command=calculate_total, x=130, y=305)
gui.Button(app, "Place Order", command=place_order, x=150, y=420)

app.run()
```

### Terms and Conditions

```python
import Graphica as gui

app = gui.Window("Sign Up", width=500, height=400)

gui.Label(app, "Create Account", x=180, y=20, size=16)

gui.Label(app, "Username:", x=50, y=70)
username = gui.Input(app, x=50, y=95, width=400)

gui.Label(app, "Email:", x=50, y=135)
email = gui.Input(app, x=50, y=160, width=400)

terms = gui.CheckBox(app, "I agree to the Terms and Conditions", 
                     x=50, y=215)
newsletter = gui.CheckBox(app, "Send me promotional emails", 
                          x=50, y=250)

status = gui.Label(app, "", x=50, y=330, size=11)

def create_account():
    if not terms.checked():
        status.set("❌ You must agree to the Terms and Conditions")
        return
    
    user = username.get()
    em = email.get()
    
    if not user or not em:
        status.set("❌ Please fill in all fields")
        return
    
    promo = "with" if newsletter.checked() else "without"
    status.set(f"✅ Account created {promo} newsletter subscription")

gui.Button(app, "Create Account", command=create_account, x=180, y=290)

app.run()
```

### Filter Interface

```python
import Graphica as gui

app = gui.Window("Product Filter", width=500, height=450)

gui.Label(app, "Filter Products", x=180, y=20, size=16)

gui.Label(app, "Categories:", x=50, y=60, size=12)
electronics = gui.CheckBox(app, "Electronics", x=50, y=90)
clothing = gui.CheckBox(app, "Clothing", x=50, y=120)
books = gui.CheckBox(app, "Books", x=50, y=150)
food = gui.CheckBox(app, "Food & Drinks", x=50, y=180)

gui.Label(app, "Price Range:", x=250, y=60, size=12)
under_20 = gui.CheckBox(app, "Under $20", x=250, y=90)
range_20_50 = gui.CheckBox(app, "$20 - $50", x=250, y=120)
range_50_100 = gui.CheckBox(app, "$50 - $100", x=250, y=150)
over_100 = gui.CheckBox(app, "Over $100", x=250, y=180)

results = gui.Label(app, "", x=50, y=250, size=11)

def apply_filters():
    categories = []
    if electronics.checked():
        categories.append("Electronics")
    if clothing.checked():
        categories.append("Clothing")
    if books.checked():
        categories.append("Books")
    if food.checked():
        categories.append("Food")
    
    prices = []
    if under_20.checked():
        prices.append("Under $20")
    if range_20_50.checked():
        prices.append("$20-$50")
    if range_50_100.checked():
        prices.append("$50-$100")
    if over_100.checked():
        prices.append("Over $100")
    
    cat_text = ", ".join(categories) if categories else "All"
    price_text = ", ".join(prices) if prices else "All"
    
    results.set(f"Showing: {cat_text} | Prices: {price_text}")

def clear_filters():
    electronics.uncheck()
    clothing.uncheck()
    books.uncheck()
    food.uncheck()
    under_20.uncheck()
    range_20_50.uncheck()
    range_50_100.uncheck()
    over_100.uncheck()
    results.set("All filters cleared")

gui.Button(app, "Apply Filters", command=apply_filters, x=150, y=220)
gui.Button(app, "Clear All", command=clear_filters, x=270, y=220)

app.run()
```

### Task List with Checkboxes

```python
import Graphica as gui

app = gui.Window("Task List", width=450, height=450)

gui.Label(app, "Today's Tasks", x=160, y=20, size=16)

task1 = gui.CheckBox(app, "Review code changes", x=50, y=70)
task2 = gui.CheckBox(app, "Update documentation", x=50, y=105)
task3 = gui.CheckBox(app, "Reply to emails", x=50, y=140)
task4 = gui.CheckBox(app, "Team meeting at 2 PM", x=50, y=175)
task5 = gui.CheckBox(app, "Deploy to staging", x=50, y=210)

progress = gui.Label(app, "0 of 5 tasks completed", x=50, y=270, size=12)

def update_progress():
    tasks = [task1, task2, task3, task4, task5]
    completed = sum(1 for task in tasks if task.checked())
    
    progress.set(f"{completed} of 5 tasks completed")
    
    if completed == 5:
        gui.alert("All tasks completed! Great work! 🎉", "Success")

def mark_all_complete():
    task1.check()
    task2.check()
    task3.check()
    task4.check()
    task5.check()
    update_progress()

gui.Button(app, "Update Progress", command=update_progress, x=50, y=310)
gui.Button(app, "Complete All", command=mark_all_complete, x=190, y=310)

app.run()
```

## Common Patterns

### Master Checkbox

Control multiple checkboxes with one master checkbox:

```python
import Graphica as gui

app = gui.Window("Select All", width=400, height=350)

select_all = gui.CheckBox(app, "Select All", x=50, y=50)

item1 = gui.CheckBox(app, "Item 1", x=50, y=90)
item2 = gui.CheckBox(app, "Item 2", x=50, y=125)
item3 = gui.CheckBox(app, "Item 3", x=50, y=160)

def toggle_all():
    if select_all.checked():
        item1.check()
        item2.check()
        item3.check()
    else:
        item1.uncheck()
        item2.uncheck()
        item3.uncheck()

gui.Button(app, "Apply", command=toggle_all, x=50, y=200)

app.run()
```

### Mutually Exclusive Options (Radio Button Style)

While Graphica doesn't have radio buttons, you can simulate them:

```python
def select_option1():
    option1.check()
    option2.uncheck()
    option3.uncheck()

def select_option2():
    option1.uncheck()
    option2.check()
    option3.uncheck()

def select_option3():
    option1.uncheck()
    option2.uncheck()
    option3.check()
```

## Best Practices

**Use clear, descriptive labels.** Users should understand exactly what checking the box means.

**Group related checkboxes.** Use visual spacing or labels to group related options together.

**Set sensible defaults.** Pre-check options that most users will want enabled.

**Provide feedback.** Show users the result of their selections, especially for important choices.

**Don't overuse checkboxes.** Too many options can be overwhelming. Group or categorize when possible.

**Consider dependencies.** If one checkbox requires another to be checked, validate this in your code.

## See Also

- [Button](button.md) - Often used with checkboxes for form submission
- [Label](label.md) - Add section labels to group checkboxes
- [Event Handling Guide](../guide/events.md)
- [Best Practices Guide](../guide/best-practices.md)