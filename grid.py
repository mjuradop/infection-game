# grid.py
# Handles grid creation and neighbor logic

from typing import List, Tuple

Cell = str  # ".", "X", "O", "#"


class Grid:
    def __init__(self, size: int):
        self.size = size
        self.cells = [["." for _ in range(size)] for _ in range(size)]

    def in_bounds(self, x: int, y: int) -> bool:
        # Check if coordinates are inside the grid
        return 0 <= x < self.size and 0 <= y < self.size

    def neighbors_4(self, x: int, y: int) -> List[Tuple[int, int]]:
        # Up, Down, Left, Right neighbors
        directions = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]
        return [(nx, ny) for nx, ny in directions if self.in_bounds(nx, ny)]
