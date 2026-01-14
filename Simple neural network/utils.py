import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

def load_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            line_parts = line.strip().split()
            if len(line_parts) != 3:
                print("RIDA: %s ON VIGANE!" % line.strip())
                continue
            x1, x2, y = map(float, line_parts)
            data.append((x1, x2, y))
    return data