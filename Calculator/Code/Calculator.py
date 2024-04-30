import tkinter as tk  # Import the tkinter library
from tkinter import messagebox  # Import the messagebox module from tkinter

# Function to handle button clicks and update the display accordingly
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

# Function to clear the display
def button_clear():
    entry.delete(0, tk.END)

# Functions to handle arithmetic operations, store the first number entered, and set the operation type
def button_add():
    first_number = entry.get()
    if first_number:
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a number.")

def button_subtract():
    first_number = entry.get()
    if first_number:
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a number.")

def button_multiply():
    first_number = entry.get()
    if first_number:
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a number.")

def button_divide():
    first_number = entry.get()
    if first_number:
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a number.")

# Function to perform the arithmetic operation based on the stored operation type
def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    try:
        if math == "addition":
            entry.insert(0, f_num + float(second_number))
        elif math == "subtraction":
            entry.insert(0, f_num - float(second_number))
        elif math == "multiplication":
            entry.insert(0, f_num * float(second_number))
        elif math == "division":
            if float(second_number) != 0:
                entry.insert(0, f_num / float(second_number))
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="gray15")

# Create an entry widget to display input and output
entry = tk.Entry(root, width=30, borderwidth=5, bg="white", fg="black", font=("Times New Roman", 25))
entry.grid(row=0, column=0, columnspan=10, padx=20, pady=30, sticky="nsew")

# Define the layout of number buttons
buttons = [
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
    ("0", 5, 1)
]

# Create number buttons and assign their functionality
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=50, pady=30, bg="black", fg="white", font=("Times New Roman", 25), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Define the layout of operation buttons
operations = [
    ("+", button_add), ("-", button_subtract), ("*", button_multiply),
    ("/", button_divide), ("=", button_equal), ("Clear", button_clear)
]

# Create operation buttons and assign their functionality
row = 2
for (text, command) in operations:
    button = tk.Button(root, text=text, padx=20, pady=15, bg="darkgreen", fg="white", font=("Times New Roman", 25), command=command)
    button.grid(row=row, column=3, padx=5, pady=5, sticky="nsew")
    row += 1

# Configure the grid to make it expandable
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
