from conf import *

def is_terminal(cell):
    return cell in ['+', 'X']

def is_valid_move(world, n, r, c):
    return 0 <= r < n and 0 <= c < n and world[r][c] != '#'


def take_action(world, n, state, action):
    r, c = state
    dr, dc = ACTIONS[action]
    nr, nc = r + dr, c + dc

    if not is_valid_move(world, n, nr, nc):
        nr, nc = r, c

    cell = world[nr][nc]

    if cell == '+':
        return (nr, nc), REWARD_GOAL, True
    elif cell == 'X':
        return (nr, nc), REWARD_TRAP, True
    else:
        return (nr, nc), REWARD_STEP, False