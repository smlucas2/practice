import unittest
from src.dot import Dot
from src.game import Game
from src.snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(width=100, height=100, cell_size=20)

    def test_initial_state(self):
        self.assertEqual(len(self.snake.segments), 3)
        self.assertEqual(self.snake.direction, "RIGHT")
        self.assertFalse(self.snake.growing)

    def test_movement(self):
        initial_head = self.snake.segments[0]
        self.snake.move()
        new_head = self.snake.segments[0]

        self.assertEqual(new_head[0], initial_head[0] + self.snake.cell_size)
        self.assertEqual(new_head[1], initial_head[1])
        self.assertEqual(len(self.snake.segments), 3)

    def test_growth(self):
        initial_length = len(self.snake.segments)
        self.snake.grow()
        self.snake.move()

        self.assertEqual(len(self.snake.segments), initial_length + 1)

    def test_collision_detection(self):
        self.snake.segments[0] = (0, 0)
        self.snake.direction = "LEFT"
        self.snake.move()

        self.assertTrue(self.snake.check_collision())

    def test_self_collision(self):
        self.snake.segments = [(20, 20), (20, 40), (20, 60), (40, 60), (60, 60)]
        self.snake.direction = "UP"
        self.snake.move()
        self.snake.change_direction("RIGHT")
        self.snake.move()
        self.snake.change_direction("DOWN")
        self.snake.move()
        self.snake.change_direction("LEFT")
        self.snake.move()

        self.assertTrue(self.snake.check_collision())

    def test_change_direction(self):
        self.snake.change_direction("UP")
        self.assertEqual(self.snake.direction, "UP")

        self.snake.change_direction("LEFT")
        self.assertEqual(self.snake.direction, "LEFT")

        self.snake.change_direction("DOWN")
        self.assertEqual(self.snake.direction, "DOWN")

        self.snake.change_direction("RIGHT")
        self.assertEqual(self.snake.direction, "RIGHT")

    def test_invalid_direction_change(self):
        self.snake.change_direction("UP")
        self.snake.move()
        self.snake.change_direction("DOWN")
        self.assertEqual(self.snake.direction, "UP")

        self.snake.change_direction("LEFT")
        self.snake.move()
        self.snake.change_direction("RIGHT")
        self.assertEqual(self.snake.direction, "LEFT")

        self.snake.change_direction("DOWN")
        self.snake.move()
        self.snake.change_direction("UP")
        self.assertEqual(self.snake.direction, "DOWN")

        self.snake.change_direction("RIGHT")
        self.snake.move()
        self.snake.change_direction("LEFT")
        self.assertEqual(self.snake.direction, "RIGHT")

class TestDot(unittest.TestCase):
    def setUp(self):
        self.dot = Dot(width=100, height=100, cell_size=20)

    def test_initial_position(self):
        x, y = self.dot.position

        self.assertEqual(x % self.dot.cell_size, 0)
        self.assertEqual(y % self.dot.cell_size, 0)
        self.assertLess(x, self.dot.width)
        self.assertLess(y, self.dot.height)
        self.assertGreaterEqual(x, 0)
        self.assertGreaterEqual(y, 0)

    def test_reposition(self):
        initial_pos = self.dot.position
        snake_positions = [(0, 0), (20, 0), (40, 0)]

        self.dot.reposition(snake_positions)
        new_pos = self.dot.position

        self.assertNotEqual(initial_pos, new_pos)
        self.assertNotIn(new_pos, snake_positions)

    def test_reposition_avoid_snake(self):
        snake_positions = [(20, 20), (40, 20), (60, 20)]
        self.dot.reposition(snake_positions)
        new_pos = self.dot.position

        self.assertNotIn(new_pos, snake_positions)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(width=100, height=100, cell_size=20)

    def test_initial_state(self):
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.state, "PAUSED")

    def test_start_game(self):
        self.game.start()
        self.assertEqual(self.game.state, "RUNNING")
        self.assertEqual(self.game.score, 0)

    def test_eating_dot(self):
        self.game.start()
        initial_score = self.game.score
        initial_length = len(self.game.snake.segments)

        head = self.game.snake.segments[0]
        # Move the dot to a position where the snake's head will be after moving right
        self.game.dot.position = (head[0] + self.game.cell_size, head[1])

        # Moves the snake to eat the dot, then extends the snake after eating it
        self.game.update()
        self.game.update()

        self.assertEqual(self.game.score, initial_score + 1)
        self.assertEqual(len(self.game.snake.segments), initial_length + 1)

    def test_game_over(self):
        self.game.start()

        # Move the snake's head to the outer boundary of the game area
        self.game.snake.segments[0] = (-20, 0)
        self.game.snake.direction = "LEFT"

        self.game.update()

        self.assertEqual(self.game.state, "GAME_OVER")

    def test_pause_game(self):
        self.game.start()
        self.game.toggle_pause()
        self.assertEqual(self.game.state, "PAUSED")

    def test_resume_game(self):
        self.game.start()
        self.game.toggle_pause()
        self.assertEqual(self.game.state, "PAUSED")
        self.game.toggle_pause()
        self.assertEqual(self.game.state, "RUNNING")

    def test_reset_game(self):
        self.game.start()
        self.game.update()
        self.game.reset_game()
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.state, "PAUSED")
        self.assertEqual(len(self.game.snake.segments), 3)

if __name__ == '__main__':
    unittest.main()