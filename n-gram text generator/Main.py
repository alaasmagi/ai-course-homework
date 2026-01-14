from process import *
from train import *

if __name__ == "__main__":
    filename = input()
    seed_words = input().split()

    # 2. Train Model
    corpus = read_file(filename)
    tokens = simple_tokenize(corpus)
    model = train_ngrams(tokens)

    # 3. Generate and Print
    result = generate(model, seed_words)
    print(" ".join(result))