N_GRAM_2 = 2
N_GRAM_3 = 3
N_GRAM_4 = 4

def deterministic_choice(counts):
    if not counts:
        return None
    max_count = max(counts.values())
    candidates = [word for word, c in counts.items() if c == max_count]
    return sorted(candidates)[0]



def generate(models, seed_words):
    result = seed_words[:]

    ngram_order = [
        (3, N_GRAM_4),
        (2, N_GRAM_3),
        (1, N_GRAM_2),
    ]

    while True:
        next_word = None

        for hist_size, key in ngram_order:
            if len(result) >= hist_size:
                hist = tuple(result[-hist_size:])
                next_word = deterministic_choice(models[key].get(hist, {}))
                if next_word is not None:
                    break

        if next_word is None or next_word == "<EOS>":
            break

        result.append(next_word)

    return result
