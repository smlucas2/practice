from typing import Literal

from .snake import Snake, Direction
from .dot import Dot

GameState = Literal["RUNNING", "PAUSED", "GAME_OVER", "WON"]

class Game:
    """
    Represents the game state and logic for the Snake game.
    """

    def __init__(self, width: int = 600, height: int = 400, cell_size: int = 20, win_score: int = 20) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.win_score = win_score

        self.reset_game()

    def reset_game(self) -> None:
        """
        Resets the game to its initial state.
        """
        self.snake = Snake(self.width, self.height, self.cell_size)
        self.dot = Dot(self.width, self.height, self.cell_size)
        self.score = 0
        self.state: GameState = "PAUSED"

    def start(self) -> None:
        """
        Starts the game.
        """
        self.reset_game()
        self.state = "RUNNING"
        self.dot.reposition(self.snake.segments)

    def update(self) -> None:
        """
        Updates the game state.
        """
        if self.state != "RUNNING":
            return

        self.snake.move()

        if self.snake.check_collision():
            self.game_over()
            return

        if self.snake.segments[0] == self.dot.position:
            self.handle_dot_eaten()

    def handle_dot_eaten(self) -> None:
        """
        Handles the event when the snake eats a dot.
        """
        self.score += 1
        self.snake.grow()
        self.dot.reposition(self.snake.segments)

        if self.score >= self.win_score:
            self.win_game()

    def change_direction(self, direction: Direction) -> None:
        """
        Changes the direction of the snake.

        :param direction: The new direction for the snake.
        """
        if self.state == "RUNNING":
            self.snake.change_direction(direction)

    def game_over(self) -> None:
        """
        Ends the game with a game over state.
        """
        self.state = "GAME_OVER"

    def win_game(self) -> None:
        """
        Ends the game with a win state.
        """
        self.state = "WON"

    def toggle_pause(self) -> None:
        """
        Toggles the pause state of the game.
        """
        if self.state == "RUNNING":
            self.state = "PAUSED"
        elif self.state == "PAUSED":
            self.state = "RUNNING"
        if self.state == "RUNNING":
            self.state = "PAUSED"
        elif self.state == "PAUSED":
            self.state = "RUNNING"