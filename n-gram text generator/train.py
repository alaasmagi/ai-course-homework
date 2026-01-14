import re
from collections import defaultdict, Counter


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()


def simple_tokenize(text):
    sentences = re.split(r'[?!.]', text)
    tokens = []

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        words = re.split(r'[\s,\-\'\"/\\]+', s)
        words = [w for w in words if w]

        tokens.append(words + ["<EOS>"])
    return tokens

def train_ngrams(sentences, ngram_sizes=(2, 3, 4)):
    models = {n: defaultdict(dict) for n in ngram_sizes}

    for words in sentences:
        for n in ngram_sizes:
            if len(words) < n:
                continue

            for i in range(len(words) - n + 1):
                history = tuple(words[i:i + n - 1])
                next_word = words[i + n - 1]

                if next_word not in models[n][history]:
                    models[n][history][next_word] = 0
                models[n][history][next_word] += 1

    return models
