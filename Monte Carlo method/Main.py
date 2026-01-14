from gameplay import *

# NB! This constant controls the total work done by the algorithm
TOTAL_SIMULATIONS = 300

# The number of consecutive pieces needed to win the game
WIN_CONDITION = 4

if __name__ == "__main__":
    lines = [input() for _ in range(9)]

    if len(lines) != 9:
        print("Error: Expected 9 lines of input.")
        exit(1)

    board = [list(line[1:-1]) for line in lines[0:6]]

    player = lines[7].split(": ")[1]
    solve_monte_carlo(board, player, TOTAL_SIMULATIONS)