from collections import defaultdict
from process import *
import csv


def train(training_file):
    word_counts = defaultdict(lambda: defaultdict(int))
    total_words = defaultdict(int)
    vocabulary = set()
    doc_counts = defaultdict(int)

    with open(training_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue

            topic = row[0]
            text = row[1]

            doc_counts[topic] += 1

            words = preprocess_text(text)

            for word in words:
                word_counts[topic][word] += 1
                total_words[topic] += 1
                vocabulary.add(word)

    return word_counts, total_words, vocabulary, doc_counts