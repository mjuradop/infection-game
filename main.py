# main.py
# Turn-based console game: you play against the infection.

from grid import Grid
from simulation import Simulation


def print_grid(grid: Grid) -> None:
    """
    Console render.
    Legend:
      . = Susceptible
      X = Infected
      O = Vaccinated/Immune
      W = Wall
    """
    for row in grid.cells:
        print(" ".join(row))
    print()


def read_int(prompt: str) -> int:
    # Read an integer safely from user input
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    size = 10
    grid = Grid(size)
    sim = Simulation(grid, p_infect=0.25, seed=123)
    sim.infect_initial_cell()

    # Simple balancing: limited actions
    vaccines_left = 12
    treatments_left = 8
    walls_left = 10

    # Lose condition: if infection reaches this many cells
    lose_infected_limit = int(size * size * 0.60)

    while True:
        counts = sim.counts()

        # Win condition
        if counts["I"] == 0:
            print_grid(grid)
            print(f"You win! Infection eliminated in {sim.turn} turns.")
            break

        # Lose condition
        if counts["I"] >= lose_infected_limit:
            print_grid(grid)
            print(f"You lose! Infection reached {counts['I']} cells.")
            break

        # Display state
        print("\n" * 2)
        print(f"Turn: {sim.turn}")
        print(f"Counts: S={counts['S']} I={counts['I']} V={counts['V']} W={counts['W']}")
        print(f"Actions left: vaccinate={vaccines_left}, treat={treatments_left}, wall={walls_left}")
        print_grid(grid)

        # Player chooses an action
        print("Choose action:")
        print("  1) vaccinate (.) -> (O)")
        print("  2) treat (X) -> (.)")
        print("  3) build wall (.) -> (W)")
        print("  4) skip")
        choice = input("Enter 1/2/3/4: ").strip()

        action_done = False

        if choice == "1":
            if vaccines_left <= 0:
                print("No vaccines left.")
            else:
                x = read_int("Row (0-9): ")
                y = read_int("Col (0-9): ")
                action_done = sim.vaccinate(x, y)
                if action_done:
                    vaccines_left -= 1
                else:
                    print("Invalid move. You can only vaccinate '.' cells.")

        elif choice == "2":
            if treatments_left <= 0:
                print("No treatments left.")
            else:
                x = read_int("Row (0-9): ")
                y = read_int("Col (0-9): ")
                action_done = sim.treat(x, y)
                if action_done:
                    treatments_left -= 1
                else:
                    print("Invalid move. You can only treat 'X' cells.")

        elif choice == "3":
            if walls_left <= 0:
                print("No walls left.")
            else:
                x = read_int("Row (0-9): ")
                y = read_int("Col (0-9): ")
                action_done = sim.build_wall(x, y)
                if action_done:
                    walls_left -= 1
                else:
                    print("Invalid move. You can only build walls on '.' cells.")

        elif choice == "4":
            action_done = True  # skipping is allowed

        else:
            print("Invalid option.")

        # If player made a valid action (or skip), infection spreads
        if action_done:
            sim.step_infection()
        else:
            # If invalid, let the player try again without advancing the infection
            input("Press Enter to try again...")

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
