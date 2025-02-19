"""
Test module for game logic.
"""
import unittest
from ..snake import Snake
from ..dot import Dot
from ..game import Game

class TestSnake(unittest.TestCase):
    """Test cases for Snake class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.snake = Snake(width=100, height=100, cell_size=20)
    
    def test_initial_state(self):
        """Test snake initialization."""
        self.assertEqual(len(self.snake.segments), 3)
        self.assertEqual(self.snake.direction, "RIGHT")
        self.assertFalse(self.snake.growing)
    
    def test_movement(self):
        """Test basic snake movement."""
        initial_head = self.snake.segments[0]
        self.snake.move()
        new_head = self.snake.segments[0]
        
        # Moving right should increase x by cell_size
        self.assertEqual(new_head[0], initial_head[0] + self.snake.cell_size)
        self.assertEqual(new_head[1], initial_head[1])
        
        # Length should remain the same when not growing
        self.assertEqual(len(self.snake.segments), 3)
    
    def test_growth(self):
        """Test snake growth."""
        initial_length = len(self.snake.segments)
        self.snake.grow()
        self.snake.move()
        
        self.assertEqual(len(self.snake.segments), initial_length + 1)
    
    def test_collision_detection(self):
        """Test collision detection."""
        # Move snake to wall
        self.snake.segments[0] = (0, 0)
        self.snake.direction = "LEFT"
        self.snake.move()
        
        self.assertTrue(self.snake.check_collision())

class TestDot(unittest.TestCase):
    """Test cases for Dot class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.dot = Dot(width=100, height=100, cell_size=20)
    
    def test_initial_position(self):
        """Test dot initialization."""
        x, y = self.dot.position
        
        # Position should be aligned to grid
        self.assertEqual(x % self.dot.cell_size, 0)
        self.assertEqual(y % self.dot.cell_size, 0)
        
        # Position should be within bounds
        self.assertLess(x, self.dot.width)
        self.assertLess(y, self.dot.height)
        self.assertGreaterEqual(x, 0)
        self.assertGreaterEqual(y, 0)
    
    def test_reposition(self):
        """Test dot repositioning."""
        initial_pos = self.dot.position
        snake_positions = [(0, 0), (20, 0), (40, 0)]
        
        self.dot.reposition(snake_positions)
        new_pos = self.dot.position
        
        # Position should change
        self.assertNotEqual(initial_pos, new_pos)
        # New position should not be in snake
        self.assertNotIn(new_pos, snake_positions)

class TestGame(unittest.TestCase):
    """Test cases for Game class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.game = Game(width=100, height=100, cell_size=20)
    
    def test_initial_state(self):
        """Test game initialization."""
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.state, "PAUSED")
    
    def test_start_game(self):
        """Test game start."""
        self.game.start()
        self.assertEqual(self.game.state, "RUNNING")
        self.assertEqual(self.game.score, 0)
    
    def test_eating_dot(self):
        """Test snake eating dot."""
        self.game.start()
        # Place dot at snake's next position
        head = self.game.snake.segments[0]
        self.game.dot.position = (head[0] + self.game.cell_size, head[1])
        
        initial_score = self.game.score
        initial_length = len(self.game.snake.segments)
        
        self.game.update()
        
        self.assertEqual(self.game.score, initial_score + 1)
        self.assertEqual(len(self.game.snake.segments), initial_length + 1)
    
    def test_game_over(self):
        """Test game over condition."""
        self.game.start()
        # Force collision
        self.game.snake.segments[0] = (-20, 0)
        self.game.update()
        
        self.assertEqual(self.game.state, "GAME_OVER")

if __name__ == '__main__':
    unittest.main()
