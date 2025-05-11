import tkinter as tk
from tkinter import messagebox

def add():
    try:
        z1 = complex(entry1.get())
        z2 = complex(entry2.get())
        wynik = z1 + z2
        add_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid complex numbers like (4+5j)!")

def sub():
    try:
        z3 = complex(entry3.get())
        z4 = complex(entry4.get())
        wynik = z3 - z4
        sub_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid complex numbers like (4+5j)!")

def mult():
    try:
        z5 = complex(entry5.get())
        z6 = complex(entry6.get())
        wynik = z5 * z6
        mult_label.config(text=f"Result: {wynik}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid complex numbers like (4+5j)!")

def div():
    try:
        z7 = complex(entry7.get())
        z8 = complex(entry8.get())
        wynik = z7 / z8
        zaokrąglony = complex(round(wynik.real, 1), round(wynik.imag, 1))
        div_label.config(text=f"Result: {zaokrąglony}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid complex numbers like (4+5j)!")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")


root = tk.Tk()
root.title("Complex Number Calculator")

tk.Label(root, text="Addition").grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(root, text="Number 1:").grid(row=1, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Number 2:").grid(row=2, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Add", command=add).grid(row=3, column=0, columnspan=2, pady=5)
add_label = tk.Label(root, text="Result: ")
add_label.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Subtraction").grid(row=5, column=0, columnspan=2, pady=10)
tk.Label(root, text="Number 1:").grid(row=6, column=0, padx=10, pady=5)
entry3 = tk.Entry(root)
entry3.grid(row=6, column=1, padx=10, pady=5)
tk.Label(root, text="Number 2:").grid(row=7, column=0, padx=10, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=7, column=1, padx=10, pady=5)
tk.Button(root, text="Subtract", command=sub).grid(row=8, column=0, columnspan=2, pady=5)
sub_label = tk.Label(root, text="Result: ")
sub_label.grid(row=9, column=0, columnspan=2, pady=5)

tk.Label(root, text="Multiplication").grid(row=0, column=2, columnspan=2, pady=5)
tk.Label(root, text="Number 1:").grid(row=1, column=2, padx=10, pady=5)
entry5 = tk.Entry(root)
entry5.grid(row=1, column=3, padx=10, pady=5)
tk.Label(root, text="Number 2:").grid(row=2, column=2, padx=10, pady=5)
entry6 = tk.Entry(root)
entry6.grid(row=2, column=3, padx=10, pady=5)
tk.Button(root, text="Multiply", command=mult).grid(row=3, column=2, columnspan=2, pady=5)
mult_label = tk.Label(root, text="Result: ")
mult_label.grid(row=4, column=2, columnspan=2, pady=5)

tk.Label(root, text="Division").grid(row=5, column=2, columnspan=2, pady=10)
tk.Label(root, text="Number 1:").grid(row=6, column=2, padx=10, pady=5)
entry7 = tk.Entry(root)
entry7.grid(row=6, column=3, padx=10, pady=5)
tk.Label(root, text="Number 2:").grid(row=7, column=2, padx=10, pady=5)
entry8 = tk.Entry(root)
entry8.grid(row=7, column=3, padx=10, pady=5)
tk.Button(root, text="Divide", command=div).grid(row=8, column=2, columnspan=2, pady=5)
div_label = tk.Label(root, text="Result: ")
div_label.grid(row=9, column=2, columnspan=2, pady=5)

root.mainloop()
