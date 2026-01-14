from learning import train_q_learning
from utils import *

if __name__ == "__main__":
    world, n = read_input()
    Q = train_q_learning(world, n)
    visualize_policy(world, Q, n)

