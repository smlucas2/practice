"""
Module for managing the overall game state.
"""
from typing import Literal
from .snake import Snake, Direction
from .dot import Dot

GameState = Literal["RUNNING", "PAUSED", "GAME_OVER", "WON"]

class Game:
    """Manages the overall game state and logic."""
    
    def __init__(self, width: int = 600, height: int = 400, cell_size: int = 20, win_score: int = 20) -> None:
        """
        Initialize a new game.
        
        Args:
            width: Game board width in pixels
            height: Game board height in pixels
            cell_size: Size of each cell in pixels
            win_score: Score needed to win the game
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.win_score = win_score
        
        self.snake = Snake(width, height, cell_size)
        self.dot = Dot(width, height, cell_size)
        self.score = 0
        self.state: GameState = "PAUSED"
    
    def start(self) -> None:
        """Start or restart the game."""
        self.snake = Snake(self.width, self.height, self.cell_size)
        self.dot = Dot(self.width, self.height, self.cell_size)
        self.score = 0
        self.state = "RUNNING"
        # Ensure dot doesn't spawn on snake
        self.dot.reposition(self.snake.segments)
    
    def update(self) -> None:
        """
        Update game state for one tick.
        
        This method is called periodically by the game loop to:
        1. Move the snake
        2. Check for collisions
        3. Check if dot was eaten
        4. Update score and check win condition
        """
        if self.state != "RUNNING":
            return
            
        self.snake.move()
        
        # Check for collisions
        if self.snake.check_collision():
            self.game_over()
            return
        
        # Check if dot was eaten
        if self.snake.segments[0] == self.dot.position:
            self.score += 1
            self.snake.grow()
            self.dot.reposition(self.snake.segments)
            
            # Check win condition
            if self.score >= self.win_score:
                self.win_game()
    
    def change_direction(self, direction: Direction) -> None:
        """
        Change the snake's direction.
        
        Args:
            direction: New direction for the snake
        """
        if self.state == "RUNNING":
            self.snake.change_direction(direction)
    
    def game_over(self) -> None:
        """Handle game over state."""
        self.state = "GAME_OVER"
    
    def win_game(self) -> None:
        """Handle winning the game."""
        self.state = "WON"
    
    def toggle_pause(self) -> None:
        """Toggle between paused and running states."""
        if self.state == "RUNNING":
            self.state = "PAUSED"
        elif self.state == "PAUSED":
            self.state = "RUNNING"
