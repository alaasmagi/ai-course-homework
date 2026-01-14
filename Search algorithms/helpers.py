def parse_map(map_lines):
    grid = [list(row) for row in map_lines]
    start = None
    destination = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 's':
                start = (x, y)
            elif cell == 'D':
                destination = (x, y)
    return grid, start, destination

def print_board(state):
    n = len(state)
    board = [["."] * n for _ in range(n)]

    for col, row in enumerate(state):
        board[row][col] = "Q"

    for row in board:
        print("".join(row))

def print_additional_info(method_name, start, destination, visited, start_time, end_time, nodes_expanded, path_length):
    print(f"Start(x,y): {start}; Destination(x,y): {destination}")
    if destination not in visited:
        print("No path found!")
    print(f"\n{method_name} stats:")
    print(f"Time taken: {end_time - start_time:.9f} seconds")
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Path length: {path_length}")