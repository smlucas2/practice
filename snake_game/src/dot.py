from typing import List, Tuple
import random

class Dot:
    """
    Represents a dot in a grid-based game.

    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        cell_size (int): The size of each cell in the grid.
        position (Tuple[int, int]): The current position of the dot.
    """

    def __init__(self, width: int = 600, height: int = 400, cell_size: int = 20) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = self._generate_random_position()

    def _generate_random_position(self) -> Tuple[int, int]:
        max_x = (self.width // self.cell_size) - 1
        max_y = (self.height // self.cell_size) - 1
        return (
            random.randint(0, max_x) * self.cell_size,
            random.randint(0, max_y) * self.cell_size
        )

    def reposition(self, snake_positions: List[Tuple[int, int]]) -> None:
        """
        Repositions the dot to a valid position that is not occupied by the snake.

        Args:
            snake_positions (List[Tuple[int, int]]): The positions occupied by the snake.
        """
        self.position = self._find_valid_position(snake_positions)

    def _find_valid_position(self, snake_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        while True:
            new_position = self._generate_random_position()
            if new_position not in snake_positions:
                return new_position