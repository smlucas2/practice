import sys
from PySide6.QtWidgets import QApplication
from src.gui import GameWindow

def main():
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()