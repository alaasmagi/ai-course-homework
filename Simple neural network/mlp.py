from utils import *

WEIGHT_LOWER = -1
WEIGHT_UPPER = 1

class SimpleMLP:
    def __init__(self):
        self.W_h = np.random.uniform(WEIGHT_LOWER, WEIGHT_UPPER, (2, 2))
        self.b_h = np.zeros((2, 1))

        self.W_o = np.random.uniform(WEIGHT_LOWER, WEIGHT_UPPER, (1, 2))
        self.b_o = np.zeros((1, 1))


    def forward(self, x):
        self.h_raw = self.W_h @ x - self.b_h
        self.h = sigmoid(self.h_raw)

        self.y_raw = self.W_o @ self.h - self.b_o
        self.y = sigmoid(self.y_raw)

        return self.h, self.y


    def train_step(self, x, target, lr):
        h, y = self.forward(x)

        delta_o = (y - target) * sigmoid_derivative(y)

        self.W_o -= lr * delta_o @ h.T
        self.b_o -= lr * delta_o * (-1)

        delta_h = (self.W_o.T @ delta_o) * sigmoid_derivative(h)

        self.W_h -= lr * delta_h @ x.T
        self.b_h -= lr * delta_h * (-1)


    def train(self, data, learning_rate, epochs):
        for _ in range(epochs):
            for x1, x2, y in data:
                x = np.array([[x1], [x2]])
                target = np.array([[y]])
                self.train_step(x, target, learning_rate)


    def predict(self, input_x1, input_x2):
        x = np.array([[input_x1], [input_x2]])
        _, y = self.forward(x)
        return y[0, 0]