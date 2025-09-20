import tkinter as tk

# Function to update expression in the entry box
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate the expression
def calculate():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry box
def clear():
    entry_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=8, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "%", "+"),
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        tk.Button(
            frame,
            text=btn,
            font=("Arial", 16),
            command=lambda key=btn: press(key),
            height=2,
            width=6
        ).pack(side="left", expand=True, fill="both")

# Last row (Clear and Equals)
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

tk.Button(frame, text="C", font=("Arial", 16), command=clear, height=2, width=6, bg="orange").pack(side="left", expand=True, fill="both")
tk.Button(frame, text="=", font=("Arial", 16), command=calculate, height=2, width=12, bg="lightgreen").pack(side="left", expand=True, fill="both")

# Run the application
root.mainloop()
