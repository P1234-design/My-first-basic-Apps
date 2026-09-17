import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My python Desktop App")
root.geometry("300x150")

def on_button_click():
    user_text = entry.get()
    messagebox.showinfo("Greeting",f'Hellow!, {user_text} !')
    
label = tk.Label(root,text="Enter Your Name: ",font=("Areal", 15))
label.pack(pady=10)

entry = tk.Entry(root,font=("Comic Sans", 15))
entry.pack(pady=5)

button = tk.Button(root,text="Sumbit",command=on_button_click,background="cyan",foreground="black")
button.pack(pady=15)

root.mainloop()
