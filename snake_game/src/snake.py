from typing import List, Tuple, Literal

Direction = Literal["UP", "DOWN", "LEFT", "RIGHT"]

class Snake:
    """
    Represents a snake in a grid-based game.

    Attributes:
        width (int): The width of the game grid.
        height (int): The height of the game grid.
        cell_size (int): The size of each cell in the grid.
        direction (Direction): The current direction of the snake.
        segments (List[Tuple[int, int]]): The list of segments representing the snake's body.
        growing (bool): Flag indicating if the snake is growing.
    """

    def __init__(self, width: int = 600, height: int = 400, cell_size: int = 20) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.direction: Direction = "RIGHT"
        start_x = (width // cell_size // 2) * cell_size
        start_y = (height // cell_size // 2) * cell_size
        self.segments: List[Tuple[int, int]] = [
            (start_x, start_y),
            (start_x - cell_size, start_y),
            (start_x - cell_size * 2, start_y)
        ]
        self.growing = False

    def move(self) -> None:
        """
        Moves the snake in the current direction.
        """
        head = self.segments[0]
        new_head = self._get_new_head(head)
        self.segments.insert(0, new_head)
        if not self.growing:
            self.segments.pop()
        else:
            self.growing = False

    def grow(self) -> None:
        """
        Makes the snake grow by one segment.
        """
        self.growing = True

    def change_direction(self, new_direction: Direction) -> None:
        """
        Changes the direction of the snake.

        Args:
            new_direction (Direction): The new direction for the snake.
        """
        opposites = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if opposites[new_direction] != self.direction:
            self.direction = new_direction

    def check_collision(self) -> bool:
        """
        Checks if the snake has collided with itself or the boundaries.

        Returns:
            bool: True if a collision has occurred, False otherwise.
        """
        head = self.segments[0]

        if head in self.segments[1:]:
            return True
        return self._is_out_of_bounds(head)

    def _get_new_head(self, head: Tuple[int, int]) -> Tuple[int, int]:
        return {
            "UP": (head[0], head[1] - self.cell_size),
            "DOWN": (head[0], head[1] + self.cell_size),
            "LEFT": (head[0] - self.cell_size, head[1]),
            "RIGHT": (head[0] + self.cell_size, head[1])
        }[self.direction]

    def _is_out_of_bounds(self, head: Tuple[int, int]) -> bool:
        return head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height