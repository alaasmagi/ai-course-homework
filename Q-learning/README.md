# EX07

## Reinforcement Learning (Q-Learning)

This project implements the **Q-Learning** algorithm, a fundamental model-free reinforcement learning method. The agent independently learns to navigate an $N \times N$ grid world, avoiding walls and traps to reach the goal via the most efficient path.

Unlike the previous task (EX06), where a neural network learned from labeled "correct" answers, this agent learns through **experience** by receiving feedback from the environment in the form of rewards and penalties.

---

## Architecture & Approach

This solution utilizes the **Tabular Q-Learning** approach.

| Component | Description |
|-----------|-------------|
| **State** | The agent's current coordinates $(r, c)$ in the grid. |
| **Actions** | Four possible directions: `U` (Up), `D` (Down), `L` (Left), `R` (Right). |
| **Q-Table** | A dictionary-based structure storing values $Q(s, a)$. |
| **Strategy** | $\epsilon$-greedy (balancing Exploration vs. Exploitation). |



---

## How the System Works

### 1. Reward Function
The agent receives feedback at every step to guide its learning process:
- **Goal (+):** $+100$ (Terminal state, episode ends successfully).
- **Trap (X):** $-100$ (Terminal state, episode ends in failure).
- **Wall (#):** Blocking state; the agent's position remains unchanged.
- **Step Cost:** $-1$ per move (encourages finding the shortest possible path).

### 2. Q-Value Update Rule
The agent's "knowledge" is updated using the Bellman equation after every action:
$$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$

This ensures that the Q-value for a specific state-action pair gradually converges toward the actual expected cumulative reward.

### 3. Training Loop
- The model trains for **50,000 episodes**.
- **Exploring Starts:** The agent starts each episode at a random traversable location. This ensures the agent learns the optimal policy for the entire map, not just a single path from the designated starting point 'O'.
- **Epsilon Decay:** The exploration rate starts at 1.0 and decays over time to shift from random discovery to optimal movement.

---

## Hyperparameter Analysis

The following parameters were chosen to ensure stable convergence and optimal pathfinding:

| Parameter | Value | Analysis |
|-----------|-------|----------|
| **Learning Rate ($\alpha$)** | **0.1** | Determines how much new information overrides old information. A low value ensures stability and prevents the agent from overreacting to single experiences. |
| **Discount Factor ($\gamma$)** | **0.9** | Determines the importance of future rewards. A value of 0.9 encourages long-term planning while still prioritizing faster goal reach. |
| **Initial Epsilon ($\epsilon$)** | **1.0** | The agent begins with 100% exploration to thoroughly discover the map layout. |
| **Epsilon Decay** | **0.99995** | Gradually reduces exploration. By the end of training, $\epsilon \approx 0.08$, meaning the agent primarily relies on its learned optimal policy. |

**Observations:**
- **Lower $\gamma$:** If the discount factor was too low (e.g., 0.1), the agent became "short-sighted," struggling to find paths that required many steps to reach a reward.
- **Higher $\alpha$:** If the learning rate was too high (e.g., 0.9), the Q-values fluctuated wildly, making the policy unstable and causing the agent to "forget" safe paths.

---

## File Structure

- **Main.py:** Entry point of the program. Reads the grid input, initiates the training process, and prints the final policy.
- **learning.py:** Contains the core `train_q_learning` logic and the Q-table update implementation.
- **conf.py:** Contains all the macros for the solution.
- **environment.py:** Defines the world rules, reward structures, and the `step` function logic.
- **utils.py:** Handles standard input parsing and formatting the final policy grid for output.

---

## Example Usage

**Input Map:**  
```
4  
...+  
.##.  
.X..  
O#.#
```

**Output Policy:**
```
| R | R | R | + |   
| U | # | # | U |  
| U | X | R | U |  
| U | # | U | # |
```
---

## Links

* [Defense slides](https://docs.google.com/presentation/d/1UH9YgCLfn7jIDcAuElS37PdPPF7LeM6H/edit?usp=sharing&ouid=109200742404759735467&rtpof=true&sd=true)