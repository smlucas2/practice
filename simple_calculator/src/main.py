import sys
from PySide6.QtWidgets import QApplication
from src.gui import CalculatorWindow

def main():
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
