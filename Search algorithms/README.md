# EX01

## Search Algorithms

This project implements fundamental search algorithms for two classic AI problems:
1. **Pathfinding** — Finding optimal routes through grid-based environments
2. **N-Queens** — Placing N chess queens on an N×N board without conflicts

---

## Description

* **EX01 consists of two problems:**
  * **Pathfinding problem** — Navigate from start to goal while avoiding obstacles
  * **N-Queen problem** — Place N queens on a chessboard such that no two queens threaten each other

* **Pathfinding algorithms implemented:**
  * **BFS (Breadth-First Search)** — Guarantees shortest path, explores uniformly
  * **Greedy Best-First Search** — Fast but suboptimal, uses heuristic
  * **A\* algorithm** — Optimal and efficient, combines BFS and Greedy

* **N-Queen problem solved using:**
  * **Hill Climbing** — Local search optimization with random restarts

---

## Problem 1: Pathfinding

### Grid World Environment

The agent navigates a 2D grid containing:
- **`.`** (dot) — Traversable cell (cost: 1)
- **`*`** (asterisk) — Lava/obstacle (impassable)
- **`S`** — Start position
- **`G`** — Goal position

**Objective:** Find the shortest path from S to G while avoiding lava.

---

### Algorithm Details

#### 1. Breadth-First Search (BFS)

**Strategy:** Explore all neighbors at distance *d* before exploring distance *d+1*

**Properties:**
- ✓ **Complete:** Always finds a solution if one exists
- ✓ **Optimal:** Guarantees shortest path (assuming uniform cost)
- ✗ **Slow:** Explores many unnecessary nodes

**Implementation:**
```python
def bfs(grid, start, goal):
    queue = deque([start])
    visited = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == goal:
            return reconstruct_path(visited, start, goal)
        
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
```

**Time Complexity:** O(V + E) where V = cells, E = edges  
**Space Complexity:** O(V)

---

#### 2. Greedy Best-First Search

**Strategy:** Always move toward the goal using a heuristic (Manhattan distance)

**Heuristic (Manhattan Distance):**
```
h(n) = |x_goal - x_current| + |y_goal - y_current|
```

**Properties:**
- ✓ **Fast:** Explores far fewer nodes than BFS
- ✓ **Intuitive:** Moves "toward" the goal
- ✗ **Not optimal:** Can find suboptimal paths
- ✗ **Incomplete:** May get stuck in local minima

**Implementation:**
```python
def greedy(grid, start, goal):
    open_set = [(manhattan(start, goal), start)]
    visited = {start: None}
    
    while open_set:
        _, current = heappop(open_set)
        if current == goal:
            return reconstruct_path(visited, start, goal)
        
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                visited[neighbor] = current
                heappush(open_set, (manhattan(neighbor, goal), neighbor))
```

**Time Complexity:** O(E log V) — depends on heuristic quality  
**Space Complexity:** O(V)

---

#### 3. A* Search

**Strategy:** Combine BFS's optimality with Greedy's speed using *f(n) = g(n) + h(n)*

**Cost Function:**
```
f(n) = g(n) + h(n)
```
- **g(n):** Cost from start to current node (like BFS)
- **h(n):** Estimated cost from current to goal (like Greedy)

**Properties:**
- ✓ **Complete:** Always finds a solution
- ✓ **Optimal:** Guarantees shortest path (with admissible heuristic)
- ✓ **Efficient:** Expands fewer nodes than BFS
- ✓ **Best of both worlds:** Combines BFS and Greedy strengths

**Implementation:**
```python
def astar(grid, start, goal):
    open_set = [(manhattan(start, goal), start)]
    g_score = {start: 0}
    visited = {start: None}
    
    while open_set:
        _, current = heappop(open_set)
        if current == goal:
            return reconstruct_path(visited, start, goal)
        
        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f = tentative_g + manhattan(neighbor, goal)
                heappush(open_set, (f, neighbor))
                visited[neighbor] = current
```

**Time Complexity:** O(E log V) — better than BFS in practice  
**Space Complexity:** O(V)

---

## Problem 2: N-Queens

### Problem Statement

Place N queens on an N×N chessboard such that:
- No two queens share the same **row**
- No two queens share the same **column**
- No two queens share the same **diagonal**

**Example (4-Queens Solution):**
```
. Q . .
. . . Q
Q . . .
. . Q .
```

---

### Hill Climbing Algorithm

**Strategy:** Start with a random configuration and iteratively improve it

**Process:**
1. **Initialize:** Place queens randomly (one per column)
2. **Evaluate:** Count conflicts (pairs of attacking queens)
3. **Generate neighbors:** Try moving each queen in its column
4. **Select best:** Choose the neighbor with fewest conflicts
5. **Repeat:** Continue until no improvement possible
6. **Restart:** If stuck in local minimum, restart with new random state

**Conflict Counting:**
```python
def count_conflicts(state):
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            # Same row
            if state[i] == state[j]:
                conflicts += 1
            # Same diagonal
            if abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts
```

**Implementation:**
```python
def hill_climb_nqueens(n):
    while True:
        state = random_state(n)
        current_conflicts = count_conflicts(state)
        
        while True:
            neighbor, neighbor_conflicts = get_best_neighbor(state)
            if neighbor_conflicts < current_conflicts:
                state = neighbor
                current_conflicts = neighbor_conflicts
            else:
                break  # Local minimum reached
        
        if current_conflicts == 0:
            return state  # Solution found
        # Otherwise restart
```

**Properties:**
- ✓ **Memory efficient:** Only stores current state
- ✓ **Fast for large N:** Doesn't explore full search space
- ✗ **Incomplete:** May get stuck in local minima
- ✗ **Not guaranteed:** Random restarts required

---

## Benchmarks (Pathfinding)

### Test 1: 200×200 grid (lava probability: 0.35)

**Start:** [87, 26] | **Goal:** [115, 196]

| Algorithm | Time (s)  | Nodes Expanded | Path Length | Optimal? |
|-----------|-----------|----------------|-------------|----------|
| BFS       | 0.033046  | 22,688         | 260         | ✓        |
| Greedy    | 0.001662  | 692            | 364         | ✗        |
| A*        | 0.020030  | 6,439          | 260         | ✓        |

**Analysis:**
- **BFS:** Optimal but explores many unnecessary nodes
- **Greedy:** 20× faster but path is 40% longer
- **A\*:** Best balance — optimal path with 3.5× fewer expansions than BFS

---

### Test 2: 1000×1000 grid (lava probability: 0.35)

**Start:** [603, 961] | **Goal:** [852, 566]

| Algorithm | Time (s)  | Nodes Expanded | Path Length | Optimal? |
|-----------|-----------|----------------|-------------|----------|
| BFS       | 0.359707  | 216,801        | 698         | ✓        |
| Greedy    | 0.006977  | 1,392          | 898         | ✗        |
| A*        | 0.132606  | 36,735         | 698         | ✓        |

**Analysis:**
- **Greedy:** 50× faster than BFS but 28% longer path
- **A\*:** 2.7× faster than BFS while maintaining optimality
- **Scalability:** A* efficiency advantage increases with grid size

---

## Algorithm Comparison Summary

### Pathfinding Algorithms

| Feature            | BFS      | Greedy   | A*       |
|--------------------|----------|----------|----------|
| **Completeness**   | Yes      | No       | Yes      |
| **Optimality**     | Yes      | No       | Yes      |
| **Speed**          | Slow     | Fast     | Medium   |
| **Memory**         | High     | Medium   | High     |
| **Use Case**       | Small grids | Quick approximate | Production |

### When to Use Each:

- **BFS:** Small grids, guaranteed shortest path, no time constraints
- **Greedy:** Real-time applications, "good enough" paths acceptable
- **A\*:** Production systems, balance of speed and optimality

---

## File Structure

- **Main.py**: Entry point that reads input and calls appropriate algorithms
- **pathfinding.py**: Implements BFS, Greedy, and A* algorithms
- **nqueenproblem.py**: Hill climbing implementation for N-Queens
- **helpers.py**: Utility functions for grid manipulation and visualization
- **map-generator.py**: Tool to generate random test grids with configurable obstacle density

---

## Running the Algorithms

### Pathfinding:
```bash
python Main.py < input.txt
```

### N-Queens:
```bash
python nqueenproblem.py
```

---

## Key Concepts Demonstrated

1. **Search Strategy Trade-offs**: Speed vs optimality
2. **Heuristic Design**: Manhattan distance for grid navigation
3. **Informed vs Uninformed Search**: Using domain knowledge
4. **Local Search**: Hill climbing for constraint satisfaction
5. **Random Restarts**: Escaping local minima

---

## Links

* [Defense slides](https://docs.google.com/presentation/d/1LLHqAwiHtb3kUajXVXnLnadFLqeH3Rv9Awebn9bnVcw/edit?usp=sharing)
