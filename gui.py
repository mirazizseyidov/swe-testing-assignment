import tkinter as tk
from tkinter import ttk
from calculator import Calculator

class CalculatorGUI:
    """Tkinter GUI for Quick-Calc"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Quick-Calc")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.calc = Calculator()
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        self.display_var = tk.StringVar(value="0")
        display = ttk.Entry(
            self.root, 
            textvariable=self.display_var, 
            justify="right",
            font=("Arial", 24),
            state="readonly"
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('%', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2, 2)
        ]
        
        for btn in buttons:
            text, row, col = btn[0], btn[1], btn[2]
            colspan = btn[3] if len(btn) > 3 else 1
            
            button = ttk.Button(
                self.root, 
                text=text, 
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
        
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char.isdigit():
            result = self.calc.input_digit(int(char))
        elif char == '.':
            result = self.calc.input_decimal()
        elif char in '+-*/':
            result = self.calc.set_operation(char)
        elif char == '=':
            result = self.calc.calculate()
        elif char == 'C':
            result = self.calc.clear()
        else:
            return
        
        self.display_var.set(result)
    
    def simulate_input(self, sequence):
        """Simulate button presses for testing (integration testing hook)"""
        for char in sequence:
            self.on_button_click(char)
        return self.calc.get_display()

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()