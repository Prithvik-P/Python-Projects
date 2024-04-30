import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

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

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="gray13")

entry = tk.Entry(root, width=30, borderwidth=5, bg="white", fg="black", font=("Times New Roman", 25))
entry.grid(row=0, column=0, columnspan=10, padx=20, pady=30, sticky="nsew")

buttons = [
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
    ("0", 5, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=50, pady=30, bg="black", fg="white", font=("Times New Roman", 25), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

operations = [
    ("+", button_add), ("-", button_subtract), ("*", button_multiply),
    ("/", button_divide), ("=", button_equal), ("Clear", button_clear)
]

row = 2
for (text, command) in operations:
    button = tk.Button(root, text=text, padx=20, pady=15, bg="black", fg="white", font=("Times New Roman", 25), command=command)
    button.grid(row=row, column=3, padx=5, pady=5, sticky="nsew")
    row += 1

for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()