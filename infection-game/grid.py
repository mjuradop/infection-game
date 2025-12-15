# grid.py
# Responsible for the grid representation and neighbor lookup.

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple

Cell = int  # 0=Susceptible, 1=Infected, 2=Recovered, 3=Dead


@dataclass
class Grid:
    rows: int
    cols: int
    cells: List[List[Cell]]

    @staticmethod
    def create(rows: int, cols: int, fill: Cell = 0) -> "Grid":
        # Create a rows x cols grid filled with 'fill'
        return Grid(rows, cols, [[fill for _ in range(cols)] for _ in range(rows)])

    def in_bounds(self, r: int, c: int) -> bool:
        # Check if (r,c) is inside the grid
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors_4(self, r: int, c: int) -> List[Tuple[int, int]]:
        # Von Neumann neighbors (up, down, left, right)
        candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        return [(rr, cc) for rr, cc in candidates if self.in_bounds(rr, cc)]
