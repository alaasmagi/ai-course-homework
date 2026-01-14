import random
from conf import *
from environment import is_terminal, take_action


def train_q_learning(world, n):
    epsilon = EPSILON

    Q = {}
    for r in range(n):
        for c in range(n):
            if world[r][c] != '#':
                Q[(r, c)] = {a: 0.0 for a in ACTION_LIST}

    valid_starts = []
    for r in range(n):
        for c in range(n):
            if world[r][c] not in ['#', '+', 'X']:
                valid_starts.append((r, c))

    for _ in range(EPISODES):
        state = random.choice(valid_starts)

        for _ in range(MAX_STEPS):
            if is_terminal(world[state[0]][state[1]]):
                break

            if random.random() < epsilon:
                action = random.choice(ACTION_LIST)
            else:
                max_q = max(Q[state].values())
                best_actions = [a for a in ACTION_LIST if Q[state][a] == max_q]
                action = random.choice(best_actions)

            next_state, reward, done = take_action(world, n, state, action)

            if is_terminal(world[next_state[0]][next_state[1]]):
                max_next_q_value = 0
            else:
                max_next_q_value = max(Q[next_state].values())

            Q[state][action] += ALPHA * (
                    reward + GAMMA * max_next_q_value - Q[state][action]
            )

            state = next_state
            if done:
                break

        epsilon = max(EPSILON_MIN, epsilon * EPSILON_DECAY)

    return Q
