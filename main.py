# main.py
# Entry point of the program (console UI)

import time
import os
from grid import Grid
from simulation import Simulation


def clear_console() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def print_grid(grid: Grid) -> None:
    for row in grid.cells:
        print(" ".join(row))
    print()


def main() -> None:
    grid_size = 10

    grid = Grid(grid_size)
    sim = Simulation(grid, p_infect=0.25, seed=123)

    sim.infect_initial_cell()

    while True:
        clear_console()
        print_grid(grid)
        sim.step()
        time.sleep(0.3)


if __name__ == "__main__":
    main()
