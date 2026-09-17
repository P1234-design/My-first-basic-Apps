import tkinter as tk
import random
import string


def generate_password():
    length = int(lenght_entry.get())
    chars = string.ascii_lowercase
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation
      
    password = "".join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk. END)
    result_entry.insert(0, password)


root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text='Length:').pack()
lenght_entry = tk.Entry(root)
lenght_entry.insert(0, "8")
lenght_entry.pack()


use_upper = tk.BooleanVar(value=True)
tk.Checkbutton(root, text='Uppercase', variable=use_upper).pack()

use_digits = tk.BooleanVar(value=True)
tk.Checkbutton(root, text='Digits', variable=use_digits).pack()

use_symbols = tk.BooleanVar(value=True)
tk.Checkbutton(root, text='Symbols', variable=use_symbols).pack()


tk.Button(root, text='Generate', command=generate_password).pack(pady=10)
btn_frame = tk.Frame(root)
result_entry = tk.Entry(root, width=100)
result_entry.pack()
root.mainloop()




