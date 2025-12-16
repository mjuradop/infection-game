# grid.py
# Handles grid creation, bounds, and neighbor logic.

from typing import List, Tuple

Cell = str  # ".", "X", "O", "#", "W"
# Legend:
# "." = Susceptible
# "X" = Infected
# "O" = Vaccinated/Immune
# "#" = Dead (optional; not used yet)
# "W" = Wall (blocks spread)


class Grid:
    def __init__(self, size: int):
        self.size = size
        self.cells: List[List[Cell]] = [["." for _ in range(size)] for _ in range(size)]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def neighbors_4(self, x: int, y: int) -> List[Tuple[int, int]]:
        candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [(nx, ny) for nx, ny in candidates if self.in_bounds(nx, ny)]
