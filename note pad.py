import tkinter as tk
from tkinter import filedialog,messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    
def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if file:
        root.title(f"Text Editor - {file}")
        text_area.delete(1.0, tk.END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())

def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))
            
root = tk.Tk()
root.title("Simple Text Editor Made by PB")
root.geometry("800x400")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label="New", command=new_file)
menu_bar.add_command(label="Open", command=open_file)
menu_bar.add_command(label="save", command=save_file)
file_menu.add_separator()
menu_bar.add_command(label="Exit", command=root.quit)

text_area = tk.Text(root, font=("", 12))
text_area.pack(expand=True, fill='both')

root.mainloop()








