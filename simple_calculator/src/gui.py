import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from src.calculator import Calculator

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        self._create_central_widget()
        self._create_display()
        self._create_button_grid()

    def _create_central_widget(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

    def _create_display(self):
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setText("0")
        self.display.setMinimumHeight(50)
        self.centralWidget().layout().addWidget(self.display)

    def _create_button_grid(self):
        button_grid = QGridLayout()
        self.centralWidget().layout().addLayout(button_grid)
        self._add_buttons(button_grid)

    def _add_buttons(self, button_grid):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)
            button.setObjectName(button_text)
            button_grid.addWidget(button, row, col)

            if button_text.isdigit():
                button.clicked.connect(lambda checked, text=button_text: self._handle_number(text))
            elif button_text in ['+', '-', '*', '/']:
                button.clicked.connect(lambda checked, op=button_text: self._handle_operation(op))
            elif button_text == '=':
                button.clicked.connect(self._calculate_result)
            elif button_text == 'C':
                button.clicked.connect(self._clear_display)

    def _handle_number(self, number: str):
        result = self.calculator.handle_number(number)
        self.display.setText(result)

    def _handle_operation(self, operation: str):
        result = self.calculator.handle_operation(operation)
        self.display.setText(result)

    def _calculate_result(self):
        result = self.calculator.calculate_result()
        self.display.setText(result)

    def _clear_display(self):
        self.calculator.reset()
        self.display.setText("0")

    def show(self):
        super().show()
