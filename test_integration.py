import pytest
import tkinter as tk
from unittest.mock import MagicMock
from calculator import Calculator
from gui import CalculatorGUI

class TestCalculatorIntegration:
    """Integration tests - testing interaction between GUI and Calculation logic"""
    
    @pytest.fixture
    def app(self):
        """Create GUI instance for testing"""
        root = tk.Tk()
        app = CalculatorGUI(root)
        yield app
        root.destroy()
    
    def test_full_calculation_workflow_addition(self, app):
        """
        Integration Test 1: Simulate full user interaction
        Enter 5, press +, enter 3, press =, result should be 8
        """
        app.simulate_input(['5', '+', '3', '='])
        
        result = app.calc.get_display()
        assert result == "8", f"Expected 8, got {result}"
    
    def test_clear_after_calculation(self, app):
        """
        Integration Test 2: Verify Clear functionality
        After calculation, pressing C should reset display to 0
        """
        app.simulate_input(['5', '+', '3', '='])
        assert app.calc.get_display() == "8"
  
        app.simulate_input(['C'])
        
        result = app.calc.get_display()
        assert result == "0", f"Expected 0 after clear, got {result}"
        assert app.calc.previous is None
        assert app.calc.operation is None
    
    def test_complex_workflow_multiplication(self, app):
        """Additional integration test: multiplication workflow"""
        app.simulate_input(['6', '*', '7', '='])
        assert app.calc.get_display() == "42"
    
    def test_division_by_zero_integration(self, app):
        """Integration test: division by zero handling in GUI"""
        app.simulate_input(['1', '0', '/', '0', '='])
        assert app.calc.get_display() == "Error"
    
        assert app.calc.reset_next == True