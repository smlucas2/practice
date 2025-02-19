"""
Module for the game's graphical user interface.
"""
from typing import Optional
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor, QKeyEvent
from .game import Game

class SnakeGameWindow(QMainWindow):
    """Main window for the snake game."""
    
    def __init__(self) -> None:
        """Initialize the game window."""
        super().__init__()
        
        # Initialize game
        self.game = Game()
        
        # Set up window properties
        self.setWindowTitle("Snake Game")
        self.setFixedSize(self.game.width, self.game.height)
        
        # Set up game timer (controls game speed)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.game_update)
        self.timer.start(100)  # Update every 100ms (10 fps)
        
        # Start game
        self.game.start()
    
    def game_update(self) -> None:
        """Update game state and refresh display."""
        self.game.update()
        self.update()  # Trigger repaint
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """
        Handle keyboard input.
        
        Args:
            event: The key event to process
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
        Paint the game state.
        
        Args:
            event: The paint event (unused)
        """
        painter = QPainter(self)
        
        # Draw background
        painter.fillRect(0, 0, self.width(), self.height(), QColor(0, 0, 0))
        
        # Draw snake
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(0, 255, 0))  # Green snake
        for segment in self.game.snake.segments:
            painter.drawRect(
                segment[0],
                segment[1],
                self.game.cell_size - 1,
                self.game.cell_size - 1
            )
        
        # Draw dot
        painter.setBrush(QColor(255, 0, 0))  # Red dot
        painter.drawRect(
            self.game.dot.position[0],
            self.game.dot.position[1],
            self.game.cell_size - 1,
            self.game.cell_size - 1
        )
        
        # Draw score
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(10, 20, f"Score: {self.game.score}")
        
        # Draw game state messages
        if self.game.state == "PAUSED":
            self._draw_centered_text(painter, "PAUSED - Press SPACE to continue")
        elif self.game.state == "GAME_OVER":
            self._draw_centered_text(painter, "GAME OVER - Press R to restart")
        elif self.game.state == "WON":
            self._draw_centered_text(painter, "YOU WIN! - Press R to play again")
    
    def _draw_centered_text(self, painter: QPainter, text: str) -> None:
        """
        Draw text centered on the screen.
        
        Args:
            painter: The QPainter to use
            text: The text to draw
        """
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(
            0, 0, self.width(), self.height(),
            Qt.AlignmentFlag.AlignCenter,
            text
        )
