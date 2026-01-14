from helpers import *
from pathfinding import *
from nqueenproblem import *
import time


def solve_pathfinding(map_data):
    grid, start, destination = parse_map(map_data)
    start_time = time.time()

    # Select algorithm by uncommenting the preferred option below
    visited, nodes_expanded = bfs(grid, start, destination)
    #visited, nodes_expanded = greedy(grid, start, destination)
    #visited, nodes_expanded = astar(grid, start, destination)

    end_time = time.time()
    solved_grid, path_length = reconstruct_path(grid, visited, start, destination)

    for row in solved_grid:
        print("".join(c for c in row))

    # NB! For debugging/logging purposes only. Tests will not pass if following block is being left uncommented!
    #print_additional_info("BFS", start, destination, visited, start_time, end_time, nodes_expanded, path_length)
    #print_additional_info("Greedy", start, destination, visited, start_time, end_time, nodes_expanded, path_length)
    #print_additional_info("A*", start, destination, visited, start_time, end_time, nodes_expanded, path_length)



def solve_nqueens(n):
    solution = hill_climb_nqueens(n)
    print_board(solution)

if __name__ == "__main__":
    # Read the first line to determine which part of the assignment to run
    first_line = input()
    value = int(first_line)

    if value < 0:
        board_size = -value
        solve_nqueens(board_size)
    else:
        num_rows = value
        map_lines = []
        for _ in range(num_rows):
            map_lines.append(input())
        solve_pathfinding(map_lines)