import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.calc = Calculator()

    def test_initialization(self):
        """Test calculator initialization."""
        self.assertEqual(self.calc.current_value, 0)
        self.assertIsNone(self.calc.pending_operation)
        self.assertTrue(self.calc.new_number)
        self.assertFalse(self.calc.error_state)

    def test_reset(self):
        """Test calculator reset functionality."""
        self.calc.current_value = 42
        self.calc.pending_operation = "+"
        self.calc.new_number = False
        self.calc.error_state = True
        
        self.calc.reset()
        
        self.assertEqual(self.calc.current_value, 0)
        self.assertIsNone(self.calc.pending_operation)
        self.assertTrue(self.calc.new_number)
        self.assertFalse(self.calc.error_state)

    def test_handle_number_single_digit(self):
        """Test number input handling for a single digit."""
        self.assertEqual(self.calc.handle_number("5"), "5")
        self.assertEqual(self.calc.current_value, 5)

    def test_handle_number_multiple_digits(self):
        """Test number input handling for multiple digits."""
        self.calc.handle_number("5")
        self.calc.handle_number("3")
        self.assertEqual(self.calc.current_value, 53)

    def test_handle_number_new_number_after_operation(self):
        """Test number input handling for a new number after an operation."""
        self.assertEqual(self.calc.handle_number("7"), "7")
        self.assertEqual(self.calc.current_value, 7)

    def test_handle_operation_addition(self):
        """Test addition operation handling."""
        self.calc.handle_number("5")
        self.assertEqual(self.calc.handle_operation("+"), "5")
        self.assertTrue(self.calc.new_number)
        self.assertEqual(self.calc.pending_operation, "+")

    def test_handle_operation_multiplication(self):
        """Test multiplication operation handling."""
        self.calc.handle_number("3")
        self.assertEqual(self.calc.handle_operation("*"), "3")
        self.assertEqual(self.calc.pending_operation, "*")

    def test_calculate_result_addition(self):
        """Test result calculation for addition."""
        # Test addition
        self.calc.handle_number("5")
        self.calc.handle_operation("+")
        self.calc.handle_number("3")
        self.assertEqual(self.calc.calculate_result(), "8")

    def test_calculate_result_multiplication(self):
        """Test result calculation for multiplication."""
        # Test multiplication
        self.calc.handle_number("4")
        self.calc.handle_operation("*")
        self.calc.handle_number("2")
        self.assertEqual(self.calc.calculate_result(), "8")

    def test_division_by_zero(self):
        """Test division by zero error handling."""
        self.calc.handle_number("5")
        self.calc.handle_operation("/")
        self.calc.handle_number("0")
        self.assertEqual(self.calc.calculate_result(), "Error: Division by zero")
        self.assertTrue(self.calc.error_state)

    def test_error_state_recovery(self):
        """Test recovery from error state."""
        # Cause an error
        self.calc.handle_number("5")
        self.calc.handle_operation("/")
        self.calc.handle_number("0")
        self.calc.calculate_result()
        
        # Recover from error
        self.assertEqual(self.calc.handle_number("5"), "5")
        self.assertFalse(self.calc.error_state)

    def test_number_formatting_whole_numbers(self):
        """Test number formatting for whole numbers."""
        # Test whole numbers
        self.calc.handle_number("5")
        self.assertEqual(self.calc._format_number(5.0), "5")

    def test_number_formatting_decimal_numbers(self):
        """Test number formatting for decimal numbers."""
        # Test decimal numbers
        self.calc.handle_number("5")
        self.assertEqual(self.calc._format_number(5.5), "5.5")
        self.assertEqual(self.calc._format_number(5.50), "5.5")

    def test_sequential_operations(self):
        """Test multiple operations in sequence."""
        self.calc.handle_number("5")
        self.calc.handle_operation("+")
        self.calc.handle_number("3")
        self.calc.handle_operation("*")
        self.calc.handle_number("2")
        self.assertEqual(self.calc.calculate_result(), "16")

    def test_negative_numbers(self):
        """Test handling of negative numbers."""
        self.calc.handle_operation("-")
        self.calc.handle_number("5")
        self.assertEqual(self.calc.calculate_result(), "-5")

    def test_subtraction(self):
        """Test subtraction operation."""
        self.calc.handle_number("8")
        self.calc.handle_operation("-")
        self.calc.handle_number("3")
        self.assertEqual(self.calc.calculate_result(), "5")

    def test_division(self):
        """Test division operation."""
        self.calc.handle_number("10")
        self.calc.handle_operation("/")
        self.calc.handle_number("2")
        self.assertEqual(self.calc.calculate_result(), "5")

    def test_decimal_results(self):
        """Test handling of decimal results."""
        self.calc.handle_number("5")
        self.calc.handle_operation("/")
        self.calc.handle_number("2")
        self.assertEqual(self.calc.calculate_result(), "2.5")

    def test_operation_without_second_number(self):
        """Test behavior when calculating without a second number."""
        self.calc.handle_number("5")
        self.calc.handle_operation("+")
        self.assertEqual(self.calc.calculate_result(), "5")

    def test_multiple_operations_precedence(self):
        """Test multiple operations with different precedence."""
        self.calc.handle_number("2")
        self.calc.handle_operation("+")
        self.calc.handle_number("3")
        self.calc.handle_operation("*")
        self.calc.handle_number("4")
        self.assertEqual(self.calc.calculate_result(), "20")  # Should evaluate as (2+3)*4

    def test_large_numbers(self):
        """Test handling of large numbers."""
        max_safe = "9999999999"  # 10 digits
        self.calc.handle_number(max_safe)
        self.assertEqual(self.calc.handle_number(max_safe), max_safe)

if __name__ == '__main__':
    unittest.main()
