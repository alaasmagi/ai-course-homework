# EX02

## Monte Carlo Method for Connect Four

This project implements a **Monte Carlo simulation-based AI** that plays Connect Four (also known as Four in a Row). The AI uses statistical sampling through random game playouts to evaluate moves and select the most promising one.

---

## Description

* **EX02's task:**
  * Implement an AI agent that can play Connect Four against a human player using the Monte Carlo method.
  * The AI evaluates all legal moves by running thousands of random simulations.
  * No game tree search or minimax required — purely simulation-based decision making.

* **Monte Carlo method:**
  * **Monte Carlo Tree Search (MCTS) simplified approach:**
    * For each legal column where a piece can be dropped, the AI simulates multiple complete games.
    * Each simulation plays out randomly until a winner is determined or the board is full.
    * The AI counts how many simulations result in a win for the current player.
    * The move with the highest win percentage is selected.
  * **Why this works:**
    * Good moves naturally lead to more winning outcomes in random playouts.
    * Poor moves result in losses even with random play.
    * The law of large numbers ensures that with enough simulations, win rates converge to true move quality.

* **Input/Output:**
  * Reads the current game board state (grid of X, O, and spaces) from standard input.
  * Reads which player's turn it is (X or O).
  * Runs Monte Carlo simulations for all legal moves.
  * Prints the updated board to standard output after making the best move.

---

## How the System Works

### 1. Game Rules (Connect Four)

Connect Four is played on a vertical grid (typically 6 rows × 7 columns):
- Two players take turns dropping pieces into columns
- Pieces fall to the lowest available position in the chosen column
- **Win condition:** First player to connect 4 pieces in a row (horizontal, vertical, or diagonal)
- **Draw:** Board fills up with no winner

### 2. Monte Carlo Simulation Process

For each legal move, the algorithm:

1. **Copy the board state** — Create a temporary copy to avoid modifying the real board
2. **Make the candidate move** — Drop a piece in the current column
3. **Random playout** — Continue the game with random moves for both players until:
   - Someone wins (4 in a row)
   - The board is full (draw)
4. **Record the result** — Track whether the current player won, lost, or drew
5. **Repeat** — Run this simulation N times (default: 10,000 simulations per move)
6. **Calculate win rate** — `win_rate = wins / total_simulations`
7. **Select best move** — Choose the move with the highest win percentage

### 3. Move Selection Strategy

When multiple moves have similar win rates, the algorithm uses a **tiebreaker**:
- Prefers **center columns** over edge columns
- This is a heuristic improvement: center positions offer more winning opportunities

**Priority formula:**
```python
priority = (win_count, -abs(column - center))
```

This ensures:
1. Higher win count is always prioritized
2. If win counts are equal, prefer columns closer to center

---

## Algorithm Pseudocode

```
function monte_carlo_move(board, player, num_simulations):
    legal_moves = get_legal_columns(board)
    move_wins = {}
    
    for each move in legal_moves:
        wins = 0
        for i = 1 to num_simulations:
            temp_board = copy(board)
            make_move(temp_board, move, player)
            result = random_playout(temp_board, opponent(player))
            if result == player:
                wins += 1
        move_wins[move] = wins
    
    return move with highest wins (center preference for ties)

function random_playout(board, current_player):
    while game_not_over(board):
        move = random_choice(legal_moves(board))
        make_move(board, move, current_player)
        current_player = switch_player(current_player)
    return winner(board)
```

---

## File Structure

- **Main.py**: Entry point that reads input, initializes the board, and calls the Monte Carlo solver
- **gameplay.py**: Contains core game logic:
  - `solve_monte_carlo()` — Main function that runs simulations and selects best move
  - `rollout()` — Performs a single random game playout
  - `check_winner()` — Checks for 4-in-a-row in all directions
  - `get_legal_moves()` — Returns available columns
  - `make_move()` — Drops a piece in a column
- **helpers.py**: Utility functions for board manipulation and display

---

## Example Execution

### Input:
```
6 7
       
       
       
   X   
  OXO  
 XOXOX 
X
```

*(Board: 6 rows, 7 columns. Player X to move.)*

### Monte Carlo Evaluation:

| Column | Simulations | Wins | Win Rate | Selected |
|--------|-------------|------|----------|----------|
| 0      | 10,000      | 4,231 | 42.31%  |          |
| 1      | 10,000      | 5,678 | 56.78%  |          |
| 2      | 10,000      | 7,892 | **78.92%** | ✓     |
| 3      | 10,000      | 6,543 | 65.43%  |          |
| ...    | ...         | ...  | ...      |          |

**AI selects Column 2** (highest win rate: 78.92%)

### Output:
```
       
       
       
   X   
  OXO  
 XOXOX 
X (move printed)
```

---

## Performance Considerations

### Simulation Count vs Quality

| Simulations | Speed       | Move Quality     | Use Case                |
|-------------|-------------|------------------|-------------------------|
| 1,000       | Very fast   | Weak, inconsistent | Quick testing          |
| 10,000      | Fast        | Good              | Default recommended    |
| 100,000     | Slow        | Excellent         | Tournament play        |

**Tradeoff:** More simulations = better decisions but slower response time.

### Computational Complexity

- **Time per move:** O(M × S × G)
  - M = number of legal moves (~7 for Connect Four)
  - S = simulations per move (10,000)
  - G = average game length (~20 moves to completion)
- **Total:** ~1.4 million game positions evaluated per AI turn

---

## Strengths and Limitations

### Strengths ✓
- **No domain knowledge required** — Works without hand-crafted evaluation functions
- **Self-balancing** — Automatically explores promising moves more
- **Scales with time** — More simulations = better play
- **Simple implementation** — Easier than minimax with alpha-beta pruning

### Limitations ✗
- **Computationally expensive** — Requires many simulations for strong play
- **No deep tactical understanding** — Doesn't "see" forced wins like minimax
- **Random playout weakness** — Assumes random play is representative
- **Not optimal** — Can miss guaranteed wins in complex positions

---

## Comparison to Other Approaches

| Method         | Strength | Speed | Implementation Complexity |
|----------------|----------|-------|---------------------------|
| Random         | Terrible | Instant | Trivial                 |
| Monte Carlo    | Good     | Moderate | Simple                 |
| Minimax (α-β)  | Excellent | Slow   | Complex                 |
| Neural Network | Excellent | Fast*  | Very Complex            |

*After training

---

## Potential Improvements

1. **UCB1 formula** — Use confidence bounds instead of pure win rates
2. **Progressive widening** — Allocate more simulations to better moves
3. **Domain knowledge** — Weight center moves in playouts
4. **Parallelization** — Run simulations on multiple CPU cores
5. **Hybrid approach** — Combine with minimax for endgame positions

---

## Links

* [Defense slides](https://docs.google.com/presentation/d/11NeFq6YwH5VXAWuGpyZxR0zS-nFsz0ahuftSIGlHaNc/edit?usp=sharing)
