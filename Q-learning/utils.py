def visualize_policy(world, Q, n):
    for r in range(n):
        row = []
        for c in range(n):
            cell = world[r][c]

            if cell in ['#', '+', 'X']:
                row.append(cell)
            else:
                best_action = max(Q[(r, c)], key = Q[(r, c)].get)
                row.append(best_action)

        print("| " + " | ".join(row) + " |")

def read_input():
    n = int(input())
    world = []

    for i in range(n):
        row = list(input())
        world.append(row)

    return world, n