"""
Main Entry Point

This module serves as the entry point for the Hot-Cold number guessing game,
initializing the PySide6 application and creating the main window.
"""

import sys
from PySide6.QtWidgets import QApplication
from gui import GameWindow

def main():
    """Initialize and run the application."""
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = GameWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
