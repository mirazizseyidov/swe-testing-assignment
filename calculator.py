# calculator.py
class Calculator:
    """Core calculator logic - handles all mathematical operations"""
    
    def __init__(self):
        self.current = "0"
        self.previous = None
        self.operation = None
        self.reset_next = False
    
    def input_digit(self, digit):
        """Handle digit input (0-9)"""
        if self.reset_next:
            self.current = str(digit)
            self.reset_next = False
        else:
            if self.current == "0":
                self.current = str(digit)
            else:
                self.current += str(digit)
        return self.current
    
    def input_decimal(self):
        """Handle decimal point input"""
        if self.reset_next:
            self.current = "0."
            self.reset_next = False
        elif "." not in self.current:
            self.current += "."
        return self.current
    
    def set_operation(self, op):
        """Set operation (+, -, *, /)"""
        if self.operation is not None and not self.reset_next:
            self.calculate()
        
        self.previous = float(self.current)
        self.operation = op
        self.reset_next = True
        return self.current
    
    def calculate(self):
        """Execute calculation based on stored operation"""
        if self.operation is None or self.previous is None:
            return self.current
        
        try:
            current_val = float(self.current)
            
            if self.operation == "+":
                result = self.previous + current_val
            elif self.operation == "-":
                result = self.previous - current_val
            elif self.operation == "*":
                result = self.previous * current_val
            elif self.operation == "/":
                if current_val == 0:
                    self.current = "Error"
                    self.operation = None
                    self.previous = None
                    self.reset_next = True
                    return "Error"
                result = self.previous / current_val
            else:
                return self.current
            
            # Format result (avoid floating point artifacts)
            if result == int(result):
                self.current = str(int(result))
            else:
                self.current = str(round(result, 10)).rstrip('0').rstrip('.')
            
            self.operation = None
            self.previous = None
            self.reset_next = True
            return self.current
            
        except (ValueError, OverflowError):
            self.current = "Error"
            self.operation = None
            self.previous = None
            self.reset_next = True
            return "Error"
    
    def clear(self):
        """Reset calculator to initial state"""
        self.current = "0"
        self.previous = None
        self.operation = None
        self.reset_next = False
        return self.current
    
    def get_display(self):
        """Get current display value"""
        return self.current
    
    # Direct calculation methods for unit testing
    @staticmethod
    def add(a, b):
        """Static method for addition"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Static method for subtraction"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Static method for multiplication"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Static method for division with zero check"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b