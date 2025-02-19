"""
Main entry point for the snake game.
"""
import sys
from PySide6.QtWidgets import QApplication
from .gui import SnakeGameWindow

def main() -> None:
    """Initialize and run the snake game."""
    # Create the Qt Application
    app = QApplication(sys.argv)
    
    # Create and show the game window
    window = SnakeGameWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
