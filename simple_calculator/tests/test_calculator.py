import unittest
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_initialization(self):
        self.assertEqual(self.calc.current_value, 0)
        self.assertIsNone(self.calc.pending_operation)
        self.assertTrue(self.calc.new_number)
        self.assertFalse(self.calc.error_state)

    def test_reset(self):
        self._set_calculator_state(42, "+", False, True)
        self.calc.reset()
        self._assert_calculator_state(0, None, True, False)
    def test_handle_number_single_digit(self):
        self.assertEqual(self.calc.handle_number("5"), "5")
        self.assertEqual(self.calc.current_value, 5)

    def test_handle_number_multiple_digits(self):
        self.calc.handle_number("5")
        self.calc.handle_number("3")
        self.assertEqual(self.calc.current_value, 53)

    def test_handle_number_new_number_after_operation(self):
        self.assertEqual(self.calc.handle_number("7"), "7")
        self.assertEqual(self.calc.current_value, 7)

    def test_handle_operation_addition(self):
        self.calc.handle_number("5")
        self.assertEqual(self.calc.handle_operation("+"), "5")
        self.assertTrue(self.calc.new_number)
        self.assertEqual(self.calc.pending_operation, "+")

    def test_handle_operation_multiplication(self):
        self.calc.handle_number("3")
        self.assertEqual(self.calc.handle_operation("*"), "3")
        self.assertEqual(self.calc.pending_operation, "*")

    def test_calculate_result_addition(self):
        self._perform_operation("5", "+", "3")
        self.assertEqual(self.calc.calculate_result(), "8")

    def test_calculate_result_multiplication(self):
        self._perform_operation("4", "*", "2")
        self.assertEqual(self.calc.calculate_result(), "8")

    def test_division_by_zero(self):
        self._perform_operation("5", "/", "0")
        self.assertEqual(self.calc.calculate_result(), "Error: Division by zero")
        self.assertTrue(self.calc.error_state)

    def test_error_state_recovery(self):
        self._perform_operation("5", "/", "0")
        self.calc.calculate_result()
        self.assertEqual(self.calc.handle_number("5"), "5")
        self.assertFalse(self.calc.error_state)

    def test_number_formatting_whole_numbers(self):
        self.assertEqual(self.calc._format_number(5.0), "5")

    def test_number_formatting_decimal_numbers(self):
        self.assertEqual(self.calc._format_number(5.5), "5.5")
        self.assertEqual(self.calc._format_number(5.50), "5.5")

    def test_sequential_operations(self):
        self._perform_operation("5", "+", "3")
        self.calc.handle_operation("*")
        self.calc.handle_number("2")
        self.assertEqual(self.calc.calculate_result(), "16")

    def test_negative_numbers(self):
        self.calc.handle_operation("-")
        self.calc.handle_number("5")
        self.assertEqual(self.calc.calculate_result(), "-5")

    def test_subtraction(self):
        self._perform_operation("8", "-", "3")
        self.assertEqual(self.calc.calculate_result(), "5")

    def test_division(self):
        self._perform_operation("10", "/", "2")
        self.assertEqual(self.calc.calculate_result(), "5")

    def test_decimal_results(self):
        self._perform_operation("5", "/", "2")
        self.assertEqual(self.calc.calculate_result(), "2.5")

    def test_operation_without_second_number(self):
        self.calc.handle_number("5")
        self.calc.handle_operation("+")
        self.assertEqual(self.calc.calculate_result(), "5")

    def test_multiple_operations_precedence(self):
        self._perform_operation("2", "+", "3")
        self.calc.handle_operation("*")
        self.calc.handle_number("4")
        self.assertEqual(self.calc.calculate_result(), "20")
    def test_large_numbers(self):
        max_safe = "9999999999"
        self.calc.handle_number(max_safe)
        self.assertEqual(self.calc.handle_number(max_safe), max_safe)

    def _set_calculator_state(self, value, operation, new_number, error_state):
        self.calc.current_value = value
        self.calc.pending_operation = operation
        self.calc.new_number = new_number
        self.calc.error_state = error_state

    def _assert_calculator_state(self, value, operation, new_number, error_state):
        self.assertEqual(self.calc.current_value, value)
        self.assertEqual(self.calc.pending_operation, operation)
        self.assertEqual(self.calc.new_number, new_number)
        self.assertEqual(self.calc.error_state, error_state)

    def _perform_operation(self, num1, operation, num2):
        self.calc.handle_number(num1)
        self.calc.handle_operation(operation)
        self.calc.handle_number(num2)

if __name__ == '__main__':
    unittest.main()