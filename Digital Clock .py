import tkinter as tk
from time import strftime

def time():
    string = strftime('Time- %H : %M : %S %p\nDate- %d/%m/%y')
    label.config(text=string)
    label.after(1000, time)
    
root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('arial black', 40,'italic','bold'),
                 background='black', foreground='red')
label.pack(anchor='center')

time()
root.mainloop()