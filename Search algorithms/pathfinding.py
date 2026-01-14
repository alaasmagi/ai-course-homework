from collections import deque
from heapq import heappush, heappop

def get_valid_neighbors(pos, grid):
    x, y = pos
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            if grid[ny][nx] != '*':
                neighbors.append((nx, ny))
    return neighbors


def bfs(grid, start, destination):
    queue = deque([start])
    visited = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1
        if current == destination:
            return visited, nodes_expanded
        for neighbor in get_valid_neighbors(current, grid):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
    return visited, nodes_expanded

def manhattan(a, b):
 return abs(a[0]-b[0]) + abs(a[1]-b[1])

def greedy(grid, start, destination):

    open_set = []
    heappush(open_set, (manhattan(start, destination), start))
    visited = {start: None}
    nodes_expanded = 0

    while open_set:
        _, current = heappop(open_set)
        nodes_expanded += 1
        if current == destination:
            return visited, nodes_expanded
        for neighbor in get_valid_neighbors(current, grid):
            if neighbor not in visited:
                visited[neighbor] = current
                heappush(open_set, (manhattan(neighbor, destination), neighbor))
    return visited, nodes_expanded


def astar(grid, start, destination):
    open_set = []
    heappush(open_set, (manhattan(start, destination), start))
    visited = {start: None}
    g_score = {start: 0}
    nodes_expanded = 0

    while open_set:
        _, current = heappop(open_set)
        nodes_expanded += 1

        if current == destination:
            return visited, nodes_expanded

        for neighbor in get_valid_neighbors(current, grid):
            tentative_g = g_score[current] + 1  # Every step in the grid costs 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g + manhattan(neighbor, destination)
                heappush(open_set, (f, neighbor))
                visited[neighbor] = current

    return visited, nodes_expanded


def reconstruct_path(grid, visited, start, destination):
    path_length = 0

    if destination not in visited:
        return grid, path_length
    current = destination
    while current != start:
        x, y = current
        if grid[y][x] == ' ':
            grid[y][x] = '.'
        current = visited[current]
        path_length += 1

    return grid, path_length