# simulation.py
# Turn-based infection simulation with player actions.

import random
from grid import Grid


class Simulation:
    def __init__(self, grid: Grid, p_infect: float = 0.25, seed: int | None = None):
        self.grid = grid
        self.p_infect = p_infect
        self.turn = 0

        if seed is not None:
            random.seed(seed)

    def infect_initial_cell(self) -> None:
        # Infect a random starting cell
        x = random.randint(0, self.grid.size - 1)
        y = random.randint(0, self.grid.size - 1)
        self.grid.cells[x][y] = "X"

    def counts(self) -> dict[str, int]:
        # Count each type for win/lose logic
        count = {"S": 0, "I": 0, "V": 0, "W": 0}
        for row in self.grid.cells:
            for cell in row:
                if cell == ".": count["S"] += 1
                elif cell == "X": count["I"] += 1
                elif cell == "O": count["V"] += 1
                elif cell == "W": count["W"] += 1
        return count

    # ---------------------------
    # Player actions (your turn)
    # ---------------------------

    def vaccinate(self, x: int, y: int) -> bool:
        """
        Vaccinate a susceptible cell: "." -> "O"
        Returns True if action was applied, False otherwise.
        """
        if not self.grid.in_bounds(x, y):
            return False
        if self.grid.cells[x][y] != ".":
            return False
        self.grid.cells[x][y] = "O"
        return True

    def treat(self, x: int, y: int) -> bool:
        """
        Treat an infected cell: "X" -> "."
        Returns True if action was applied, False otherwise.
        """
        if not self.grid.in_bounds(x, y):
            return False
        if self.grid.cells[x][y] != "X":
            return False
        self.grid.cells[x][y] = "."
        return True

    def build_wall(self, x: int, y: int) -> bool:
        """
        Build a wall on a susceptible cell: "." -> "W"
        Walls cannot be infected and block spread through them.
        """
        if not self.grid.in_bounds(x, y):
            return False
        if self.grid.cells[x][y] != ".":
            return False
        self.grid.cells[x][y] = "W"
        return True

    # ---------------------------
    # Infection step (after you)
    # ---------------------------

    def step_infection(self) -> None:
        """
        Infection spreads from infected cells to susceptible neighbors.
        Rules:
          - "." can become "X"
          - "O" (vaccinated) cannot be infected
          - "W" (wall) cannot be infected and acts like a blocker
        """
        new_infections = []
        for x in range(self.grid.size):
            for y in range(self.grid.size):
                if self.grid.cells[x][y] == "X":
                    for nx, ny in self.grid.neighbors_4(x, y):
                        if self.grid.cells[nx][ny] == ".":  # only susceptible infects
                            if random.random() < self.p_infect:
                                new_infections.append((nx, ny))

        for x, y in new_infections:
            self.grid.cells[x][y] = "X"

        self.turn += 1
