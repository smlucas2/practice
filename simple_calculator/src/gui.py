import sys
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from src.calculator import Calculator

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.setup_ui()

    def setup_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setText("0")
        self.display.setMinimumHeight(50)
        layout.addWidget(self.display)

        # Create button grid
        button_grid = QGridLayout()
        layout.addLayout(button_grid)

        # Button text and positions
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        # Create and connect buttons
        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)
            button.setObjectName(button_text)  # Set object name for findChild
            button_grid.addWidget(button, row, col)

            if button_text.isdigit():
                button.clicked.connect(lambda checked, text=button_text: self.handle_number(text))
            elif button_text in ['+', '-', '*', '/']:
                button.clicked.connect(lambda checked, op=button_text: self.handle_operation(op))
            elif button_text == '=':
                button.clicked.connect(self.calculate_result)
            elif button_text == 'C':
                button.clicked.connect(self.clear_display)

    def handle_number(self, number: str):
        """Handle numeric button clicks."""
        result = self.calculator.handle_number(number)
        self.display.setText(result)

    def handle_operation(self, operation: str):
        """Handle operation button clicks."""
        result = self.calculator.handle_operation(operation)
        self.display.setText(result)

    def calculate_result(self):
        """Calculate and display result."""
        result = self.calculator.calculate_result()
        self.display.setText(result)

    def clear_display(self):
        """Clear calculator display."""
        self.calculator.reset()
        self.display.setText("0")

    def show(self):
        """Show the window without starting the event loop."""
        super().show()

    def start_event_loop(self):
        """Start the Qt event loop. Use this for running the actual application."""
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
        self.app.exec()
