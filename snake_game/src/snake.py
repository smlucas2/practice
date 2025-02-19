from typing import List, Tuple, Literal

Direction = Literal["UP", "DOWN", "LEFT", "RIGHT"]

class Snake:
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
        head = self.segments[0]
        new_head = {
            "UP": (head[0], head[1] - self.cell_size),
            "DOWN": (head[0], head[1] + self.cell_size),
            "LEFT": (head[0] - self.cell_size, head[1]),
            "RIGHT": (head[0] + self.cell_size, head[1])
        }[self.direction]

        self.segments.insert(0, new_head)
        if not self.growing:
            self.segments.pop()
        else:
            self.growing = False

    def grow(self) -> None:
        self.growing = True

    def change_direction(self, new_direction: Direction) -> None:
        opposites = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }
        if opposites[new_direction] != self.direction:
            self.direction = new_direction

    def check_collision(self) -> bool:
        head = self.segments[0]

        if head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height:
            return True

        if head in self.segments[1:]:
            return True

        return False