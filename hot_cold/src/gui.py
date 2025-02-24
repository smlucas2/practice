"""
GUI Module

This module manages the graphical user interface components using PySide6,
including the start/feedback button and input field for the Hot-Cold game.
"""

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QVBoxLayout,
    QLineEdit, QLabel, QMessageBox
)
from PySide6.QtCore import Qt, QTimer
from game_logic import GameLogic

class GameWindow(QMainWindow):
    """Main window for the Hot-Cold game interface."""
    
    def __init__(self):
        """Initialize the game window and UI components."""
        super().__init__()
        self.game_logic = GameLogic()
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface components."""
        self.setWindowTitle("Hot Cold Game")
        self.setFixedSize(400, 300)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        # Create title label
        title_label = QLabel("Hot Cold Game")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")
        layout.addWidget(title_label)

        # Create input field
        self.guess_input = QLineEdit()
        self.guess_input.setPlaceholderText("Enter your guess (1-100)")
        self.guess_input.setAlignment(Qt.AlignCenter)
        self.guess_input.setFixedWidth(200)
        self.guess_input.returnPressed.connect(self.handle_guess)
        layout.addWidget(self.guess_input)

        # Create feedback/start button
        self.feedback_button = QPushButton("Start Game")
        self.feedback_button.setFixedWidth(200)
        self.feedback_button.clicked.connect(self.start_game)
        layout.addWidget(self.feedback_button)

        # Initialize game state
        self.game_active = False
        self.reset_timer = QTimer()
        self.reset_timer.setSingleShot(True)
        self.reset_timer.timeout.connect(self.reset_to_start)

    def start_game(self):
        """Start a new game."""
        if not self.game_active:
            self.game_logic.reset_game()
            self.game_active = True
            self.feedback_button.setText("Make a guess!")
            self.guess_input.setEnabled(True)
            self.guess_input.setFocus()

    def handle_guess(self):
        """Process the user's guess."""
        if not self.game_active:
            return

        guess = self.guess_input.text()
        feedback, is_winner = self.game_logic.check_guess(guess)
        
        if is_winner:
            self.feedback_button.setStyleSheet("background-color: #4CAF50; color: white;")
            self.feedback_button.setText("WINNER!")
            self.game_active = False
            self.guess_input.setEnabled(False)
            self.reset_timer.start(2000)  # Reset after 2 seconds
        else:
            if feedback in ["hot", "cold"]:
                color = "#FF4444" if feedback == "hot" else "#2196F3"
                self.feedback_button.setStyleSheet(f"background-color: {color}; color: white;")
            self.feedback_button.setText(feedback)

        self.guess_input.clear()

    def reset_to_start(self):
        """Reset the game to its initial state."""
        self.feedback_button.setStyleSheet("")
        self.feedback_button.setText("Start Game")
        self.guess_input.clear()
