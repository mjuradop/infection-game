# simulation.py
# Handles infection logic and simulation rules

import random
from grid import Grid


class Simulation:
    def __init__(self, grid: Grid, p_infect: float = 0.25, seed: int | None = None):
        self.grid = grid
        self.p_infect = p_infect

        if seed is not None:
            random.seed(seed)

    def infect_initial_cell(self) -> None:
        # Infect a random starting cell
        x = random.randint(0, self.grid.size - 1)
        y = random.randint(0, self.grid.size - 1)
        self.grid.cells[x][y] = "X"

    def step(self) -> None:
        # One simulation step (tick)
        new_infections = []

        for x in range(self.grid.size):
            for y in range(self.grid.size):
                if self.grid.cells[x][y] == "X":
                    for nx, ny in self.grid.neighbors_4(x, y):
                        if self.grid.cells[nx][ny] == ".":
                            if random.random() < self.p_infect:
                                new_infections.append((nx, ny))

        for x, y in new_infections:
            self.grid.cells[x][y] = "X"
