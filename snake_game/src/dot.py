"""
Module for managing the dot (food) in the snake game.
"""
from typing import List, Tuple
import random

class Dot:
    """Represents the dot (food) that the snake tries to eat."""
    
    def __init__(self, width: int = 600, height: int = 400, cell_size: int = 20) -> None:
        """
        Initialize a new dot with random position.
        
        Args:
            width: Game board width in pixels
            height: Game board height in pixels
            cell_size: Size of each cell in pixels
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = self._get_random_position()
    
    def _get_random_position(self) -> Tuple[int, int]:
        """
        Generate a random position for the dot.
        
        Returns:
            Tuple of (x, y) coordinates aligned to the grid
        """
        max_x = (self.width // self.cell_size) - 1
        max_y = (self.height // self.cell_size) - 1
        return (
            random.randint(0, max_x) * self.cell_size,
            random.randint(0, max_y) * self.cell_size
        )
    
    def reposition(self, snake_positions: List[Tuple[int, int]]) -> None:
        """
        Move the dot to a new random position not occupied by the snake.
        
        Args:
            snake_positions: List of (x, y) coordinates occupied by snake segments
        """
        while True:
            new_position = self._get_random_position()
            if new_position not in snake_positions:
                self.position = new_position
                break
