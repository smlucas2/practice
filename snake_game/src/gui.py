from typing import Optional

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor, QKeyEvent
from PySide6.QtWidgets import QMainWindow, QApplication

from .game import Game

class SnakeGameWindow(QMainWindow):
    """
    Main window for the Snake game.
    """

    def __init__(self) -> None:
        super().__init__()
        self.game = Game()
        self._initialize_window()
        self._initialize_timer()

    def _initialize_window(self) -> None:
        self.setWindowTitle("Snake Game")
        self.setFixedSize(self.game.width, self.game.height)

    def _initialize_timer(self) -> None:
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_game)
        self.timer.start(100)
        self.game.start()

    def _update_game(self) -> None:
        self.game.update()
        self.update()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Handle key press events to control the game.
        Overrides the keyPressEvent method from QMainWindow.
        """
        key_map = {
            Qt.Key.Key_Up: "UP",
            Qt.Key.Key_Down: "DOWN",
            Qt.Key.Key_Left: "LEFT",
            Qt.Key.Key_Right: "RIGHT"
        }
        if event.key() == Qt.Key.Key_Space:
            self.game.toggle_pause()
        elif event.key() == Qt.Key.Key_R and self.game.state in ["GAME_OVER", "WON"]:
            self.game.start()
        elif event.key() in key_map:
            self.game.change_direction(key_map[event.key()])

    def paintEvent(self, event) -> None:
        """
        Handle paint events to draw the game on the window.
        Overrides the paintEvent method from QMainWindow.
        """
        painter = QPainter(self)
        self._draw_background(painter)
        self._draw_snake(painter)
        self._draw_dot(painter)
        self._draw_score(painter)
        self._draw_game_state_messages(painter)

    def _draw_background(self, painter: QPainter) -> None:
        painter.fillRect(0, 0, self.width(), self.height(), QColor(0, 0, 0))

    def _draw_snake(self, painter: QPainter) -> None:
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(0, 255, 0))
        for segment in self.game.snake.segments:
            painter.drawRect(
                segment[0],
                segment[1],
                self.game.cell_size - 1,
                self.game.cell_size - 1
            )

    def _draw_dot(self, painter: QPainter) -> None:
        painter.setBrush(QColor(255, 0, 0))
        painter.drawRect(
            self.game.dot.position[0],
            self.game.dot.position[1],
            self.game.cell_size - 1,
            self.game.cell_size - 1
        )

    def _draw_score(self, painter: QPainter) -> None:
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(10, 20, f"Score: {self.game.score}")

    def _draw_game_state_messages(self, painter: QPainter) -> None:
        if self.game.state == "PAUSED":
            self._draw_centered_text(painter, "PAUSED - Press SPACE to continue")
        elif self.game.state == "GAME_OVER":
            self._draw_centered_text(painter, "GAME OVER - Press R to restart")
        elif self.game.state == "WON":
            self._draw_centered_text(painter, "YOU WIN! - Press R to play again")

    def _draw_centered_text(self, painter: QPainter, text: str) -> None:
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(
            0, 0, self.width(), self.height(),
            Qt.AlignmentFlag.AlignCenter,
            text
        )