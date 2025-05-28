from tkinter import  *;

# Function to update the expression
def press(key):
    current = entry.get()
    entry.delete(0, "end")
    entry.insert("end", current + key)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", result)
    except Exception as e:
        entry.delete(0, "end")
        entry.insert("end", "Error")

# Function to clear the input field
def clear():
    entry.delete(0, "end")

# Create the main window
root=Tk()
root.title("Calculator")

# Create an input field
entry = Entry(root, width=25, font=("Arial", 16), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("//", 5, 0), ("**", 5, 1) ]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = Button(root, text=text, width=3, height=1, font=("Arial", 12), command=evaluate)
    else:
        button = Button(root, text=text, width=3, height=1, font=("Arial", 12), command=lambda t=text:press(t))
    button.grid(row=row, column=col, padx=3, pady=3)

# Create the clear button
clear_button = Button(root, text="C", width=3, height=2, font=("Arial", 12), command=clear)
clear_button.grid(row=6, column=0, columnspan=4, padx=3, pady=3)

# Run the GUI event loop
root.mainloop()
