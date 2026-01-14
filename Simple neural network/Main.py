from mlp import *

LEARNING_RATE = 0.5
EPOCHS = 10000

if __name__ == "__main__":
    filename = input().strip()
    test_input = input().strip().split()
    x1, x2 = map(float, test_input)

    data = load_data(filename)

    model = SimpleMLP()
    model.train(data, LEARNING_RATE, EPOCHS)

    output = model.predict(x1, x2)

    print(round(output))
