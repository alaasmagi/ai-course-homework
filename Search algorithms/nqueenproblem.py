import random

def count_conflicts(state):
    n = len(state)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1
    return count

def get_best_neighbor(state):
    n = len(state)
    best = list(state)
    best_conflicts = count_conflicts(state)

    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue
            new_state = list(state)
            new_state[col] = row
            conflicts = count_conflicts(new_state)
            if conflicts < best_conflicts:
                best_conflicts = conflicts
                best = new_state
    return best, best_conflicts

def hill_climb_nqueens(n):
    while True:
        state = [random.randint(0, n - 1) for _ in range(n)]
        current_conflicts = count_conflicts(state)

        while True:
            neighbor, neighbor_conflicts = get_best_neighbor(state)
            if neighbor_conflicts < current_conflicts:
                state, current_conflicts = neighbor, neighbor_conflicts
            else:
                break

        if current_conflicts == 0:
            return state