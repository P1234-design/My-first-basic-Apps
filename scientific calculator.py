import tkinter as tk
from math import sqrt, pow, log, sin, cos, tan, radians, e,  fmod

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator made by Prashant")
        self.entry = tk.Entry(root, width=40, borderwidth=10)
        self.entry.grid(row=0, column=0, columnspan=6, padx=20, pady=10)
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('CE', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('^', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('log', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('(', 5, 3), (')', 5, 4),
            ('e', 6, 0), ('sec', 6, 1), ('cot', 6, 2), ('cosec',6, 3), ('mod', 6, 4),
        ]
        for (text, row, col) in buttons:
            tk.Button(self.root, text=text, padx=18, pady=15,
                      command=lambda t=text: self.on_click(t)).grid(row=row, column=col)
    
    def on_click(self, char):
        if char == "CE":
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get().replace("^", "**")
                result = eval(expression, {"__builtins__": None},
                              {"sqrt": sqrt, "log": log, "sin": lambda x: sin(radians(x)),"e": e,"cosec": lambda x: 1/sin(radians(x)), "sec": lambda x: 1/cos(radians(x)),
                               "^": pow, "cot": lambda x: 1/tan(radians(x)), "mod": fmod, "cos": lambda x: cos(radians(x)), "tan": lambda x: tan(radians(x))})
                      
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error!")
                
        else:
            self.entry.insert(tk.END, char)
            
if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
    