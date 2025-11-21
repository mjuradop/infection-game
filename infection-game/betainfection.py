import random
import time
import os

GRID_SIZE = 10

def create_grid():
    return [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def infect_initial_cell(grid):
    x = random.randint(0, GRID_SIZE - 1)
    y = random.randint(0, GRID_SIZE - 1)
    grid[x][y] = "X"  # X = infected
    return x, y

def spread_infection(grid):
    new_infections = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == "X":
                neighbors = [
                    (i-1, j), (i+1, j),
                    (i, j-1), (i, j+1)
                ]
                for x, y in neighbors:
                    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                        if grid[x][y] == "." and random.random() < 0.25:
                            new_infections.append((x, y))
    for x, y in new_infections:
        grid[x][y] = "X"

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    grid = create_grid()
    infect_initial_cell(grid)

    while True:
        clear_console()
        print_grid(grid)
        spread_infection(grid)
        time.sleep(0.3)

if __name__ == "__main__":
    main()