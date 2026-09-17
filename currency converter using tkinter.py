import tkinter as tk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
# Hardcoded rates relative to USD
        self.rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'INR': 87.0, 'JPY': 110.0}
        
        tk.Label(root, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)
        
        tk.Label(root, text="From:").grid(row=1, column=0)
        self.from_var = tk.StringVar(root)
        self.from_var.set('USD')
        tk.OptionMenu(root, self.from_var, *self.rates.keys()).grid(row=1, column=1)
        
        tk.Label(root, text="To:").grid(row=2, column=0)
        self.to_var = tk.StringVar(root)
        self.to_var.set('EUR')
        tk.OptionMenu(root, self.to_var, *self.rates.keys()).grid(row=2, column=1)
        
        tk.Button(root, text="Convert", command=self.convert).grid(row=3, column=0, columnspan=2)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)
    
    def convert(self):
        try:
            amt = float(self.amount_entry.get())
            from_rate = self.rates[self.from_var.get()]
            to_rate = self.rates[self.to_var.get()]
# Convert to USD then to target
            converted = (amt / from_rate) * to_rate
            self.result_label.config(text=f"Result: {converted:.2f}")
        except ValueError:
            self.result_label.config(text="Invalid Input")

root = tk.Tk()
app = CurrencyConverter(root)
root.mainloop()