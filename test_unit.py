import pytest
import sys
import math
from calculator import Calculator

class TestCalculatorUnit:
    """Unit tests for Calculator class - testing individual methods in isolation"""
    
    # Setup fixture
    @pytest.fixture
    def calc(self):
        return Calculator()

    
    def test_addition(self, calc):
        """Test basic addition functionality"""
        assert Calculator.add(5, 3) == 8
        assert Calculator.add(-5, 3) == -2
        assert Calculator.add(0, 0) == 0
    
    def test_subtraction(self, calc):
        """Test basic subtraction functionality"""
        assert Calculator.subtract(10, 4) == 6
        assert Calculator.subtract(5, 10) == -5
        assert Calculator.subtract(0, 0) == 0
    
    def test_multiplication(self, calc):
        """Test basic multiplication functionality"""
        assert Calculator.multiply(6, 7) == 42
        assert Calculator.multiply(-6, 7) == -42
        assert Calculator.multiply(0, 100) == 0
    
    def test_division(self, calc):
        """Test basic division functionality"""
        assert Calculator.divide(10, 2) == 5.0
        assert Calculator.divide(7, 2) == 3.5
        assert Calculator.divide(0, 5) == 0.0
    
    
    def test_division_by_zero(self, calc):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            Calculator.divide(10, 0)

        calc.input_digit(5)
        calc.set_operation("/")
        calc.input_digit(0)
        result = calc.calculate()
        assert result == "Error"
    
    def test_negative_numbers(self, calc):
        """Test operations with negative numbers"""
        assert Calculator.add(-5, -3) == -8
        assert Calculator.subtract(-10, -4) == -6
        assert Calculator.multiply(-6, -7) == 42
        assert Calculator.divide(-10, 2) == -5.0
    
    def test_decimal_numbers(self, calc):
        """Test operations with decimal numbers"""
        assert Calculator.add(5.5, 3.2) == 8.7
        assert Calculator.subtract(10.5, 4.2) == 6.3
        assert abs(Calculator.multiply(2.5, 4.2) - 10.5) < 0.0001
    
    def test_large_numbers(self, calc):
        """Test operations with very large numbers"""
        large = 1e308
        assert Calculator.add(large, large) == float('inf')
        assert Calculator.multiply(large, 2) == float('inf')
    
    
    def test_clear_functionality(self, calc):
        """Test clear resets calculator state"""
        calc.input_digit(5)
        calc.set_operation("+")
        calc.input_digit(3)
        result = calc.clear()
        assert result == "0"
        assert calc.current == "0"
        assert calc.previous is None
        assert calc.operation is None
    
    def test_chained_operations(self, calc):
        """Test chained operations (e.g., 5 + 3 + 2)"""
        calc.input_digit(5)
        calc.set_operation("+")
        calc.input_digit(3)
        calc.set_operation("+") 
        calc.input_digit(2)
        result = calc.calculate()
        assert result == "10"
    
    def test_floating_point_precision(self, calc):
        """Test that floating point results are formatted correctly"""
        calc.input_digit(1)
        calc.input_decimal()
        calc.input_digit(1)
        calc.set_operation("+")
        calc.input_digit(2)
        calc.input_decimal()
        calc.input_digit(2)
        result = calc.calculate()
        assert result == "3.3" 
    
    def test_display_formatting(self, calc):
        """Test display formatting for integers vs floats"""
        calc.input_digit(5)
        calc.set_operation("*")
        calc.input_digit(2)
        result = calc.calculate()
        assert result == "10"  # Should be "10", not "10.0"