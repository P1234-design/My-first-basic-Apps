import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint")
        
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.bind("<B1-Motion>", self.paint)
        
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="Clear", command=self.clear).pack(side="right")
        
    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", width=0)
        
    def clear(self):
        self.canvas.delete("all")
        
root = tk.Tk()
app = PaintApp(root)
root.mainloop()