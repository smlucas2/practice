import sys
import unittest

from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt

from src.gui import CalculatorWindow

class TestCalculatorWindow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def setUp(self):
        self.window = CalculatorWindow()
        self.window.show()
        QTest.qWait(100)

    def tearDown(self):
        self.window.close()

    def test_initial_display(self):
        self.assertEqual(self.window.display.text(), "0")

    def test_number_buttons(self):
        clear_button = self.window.findChild(QPushButton, 'C')
        for i in range(10):
            self._click_button(clear_button)
            button = self.window.findChild(QPushButton, str(i))
            self._click_button(button)
            self.assertEqual(self.window.display.text(), str(i))

    def test_operation_buttons(self):
        operations = ['+', '-', '*', '/']
        for op in operations:
            button = self.window.findChild(QPushButton, op)
            self._click_button(button)
            if op == '-':
                self.assertEqual(self.window.display.text(), "-")
            else:
                self.assertEqual(self.window.display.text(), "0")

    def test_clear_button(self):
        button = self.window.findChild(QPushButton, 'C')
        self._click_button(button)
        self.assertEqual(self.window.display.text(), "0")

    def test_calculate_result(self):
        self._perform_calculation(['1', '+', '2', '='], "3")

    def test_window_properties(self):
        self.assertEqual(self.window.windowTitle(), "Calculator")
        self.assertEqual(self.window.size().width(), 300)
        self.assertEqual(self.window.size().height(), 400)

    def test_division_by_zero_error(self):
        self._perform_calculation(['5', '/', '0', '='], "Error: Division by zero")

    def test_complex_calculation(self):
        self._perform_calculation(['2', '+', '3', '*', '4', '='], "20")

    def test_negative_number_input(self):
        self._perform_calculation(['-', '5', '='], "-5")

    def test_sequential_operations_without_equals(self):
        self._perform_calculation(['2', '+', '3', '*'], "5")

    def test_rapid_button_clicks(self):
        button_1 = self.window.findChild(QPushButton, '1')
        for _ in range(5):
            self._click_button(button_1, wait_time=10)
        self.assertEqual(self.window.display.text(), "11111")

    def test_decimal_result_display(self):
        self._perform_calculation(['5', '/', '2', '='], "2.5")

    def _click_button(self, button, wait_time=100):
        QTest.mouseClick(button, Qt.LeftButton)
        QTest.qWait(wait_time)
    def _perform_calculation(self, sequence, expected_result):
        buttons = {str(i): self.window.findChild(QPushButton, str(i)) for i in range(10)}
        buttons.update({op: self.window.findChild(QPushButton, op) for op in ['+', '-', '*', '/', '=']})
        for button in sequence:
            self._click_button(buttons[button])
        self.assertEqual(self.window.display.text(), expected_result)

if __name__ == '__main__':
    unittest.main()