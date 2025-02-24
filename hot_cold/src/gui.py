from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PySide6.QtCore import Qt, QTimer
from src.game_logic import GameLogic

class GameWindow(QMainWindow):
    RED = "#FF4444"
    BLUE = "#2196F3"
    GREEN = "#4CAF50"

    def __init__(self):
        super().__init__()
        self.game_logic = GameLogic()
        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface for the GameWindow.
        """
        self.setWindowTitle("Hot Cold Game")
        self.setFixedSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)

        self.title_label = QLabel("Hot or Cold!", alignment=Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; margin-bottom: 20px;")
        layout.addWidget(self.title_label)

        self.guess_input = QLineEdit(placeholderText="", alignment=Qt.AlignCenter, fixedWidth=200)
        self.guess_input.returnPressed.connect(self.handle_guess)
        layout.addWidget(self.guess_input, alignment=Qt.AlignCenter)

        self.feedback_button = QPushButton("Start Game", fixedWidth=200)
        self.feedback_button.clicked.connect(self.start_game)
        layout.addWidget(self.feedback_button, alignment=Qt.AlignCenter)

        self.game_active = False
        self.reset_timer = QTimer(singleShot=True)
        self.reset_timer.timeout.connect(self.start_game)

    def _start_game(self):
        self.game_logic.reset_game()
        self.update_button("Make your initial guess!", enabled=True, focus=True)
        self.guess_input.clear()

    def _handle_guess(self):
        guess = self.guess_input.text()
        feedback, is_winner = self.game_logic.check_guess(guess)

        if is_winner:
            self.update_button(feedback, style=f"background-color: {self.GREEN}; color: white;", enabled=False)
            self.reset_timer.start(2000)
        else:
            color = self.RED if feedback == self.game_logic.HOT else self.BLUE
            self.update_button(feedback, style=f"background-color: {color}; color: white;")
        self.guess_input.clear()
        
    def _update_button(self, text, style="", enabled=True, focus=False):
        self.feedback_button.setText(text)
        self.feedback_button.setStyleSheet(style)
        self.feedback_button.setEnabled(enabled)
        if focus:
            self.guess_input.setFocus()