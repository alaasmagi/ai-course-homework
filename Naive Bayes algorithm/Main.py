from train import *
from process import *

if __name__ == "__main__":
    training_file = input()

    num_queries = int(input())
    queries_raw = [input() for _ in range(num_queries)]

    model = train(training_file)

    results = predict(model, queries_raw)
    for result in results:
        print(result)