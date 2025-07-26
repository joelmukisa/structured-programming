import tkinter as tk
from tkinter import font as tkfont

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.resizable(0, 0)
        
        # Custom font
        custom_font = tkfont.Font(size=15)
        
        # Entry widget for display
        self.entry = tk.Entry(root, width=14, font=custom_font, borderwidth=5, 
                            justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=10, font=custom_font,
                             command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')
        
        # Make buttons expand with window
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()