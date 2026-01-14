import math

def preprocess_text(text):
    words = text.lower().split()
    filtered_words = [word for word in words if len(word) >= 4]
    return filtered_words

def preprocess_query(query):
    original_words = query.split()
    filtered_original = [word for word in original_words if len(word) >= 4]
    filtered_lowercase = [word.lower() for word in filtered_original]
    return filtered_original, filtered_lowercase

def calculate_log_probability(words, topic, word_counts, total_words, vocab_size, doc_counts, total_docs):
    log_prior = math.log(doc_counts[topic] / total_docs)
    log_prob = log_prior

    for word in words:
        n_wc = word_counts[topic].get(word, 0)
        n_c = total_words[topic]

        prob = (n_wc + 1) / (n_c + vocab_size)
        log_prob += math.log(prob)
    return log_prob

def predict(model, queries):
    word_counts, total_words, vocabulary, doc_counts = model
    vocab_size = len(vocabulary)
    topics = list(total_words.keys())
    total_docs = sum(doc_counts.values())

    results = []

    for query in queries:
        original_words, lowercase_words = preprocess_query(query)

        if not lowercase_words:
            continue

        best_topic = None
        best_log_prob = float('-inf')

        for topic in topics:
            log_prob = calculate_log_probability(lowercase_words, topic, word_counts, total_words, vocab_size,
                                                 doc_counts, total_docs)

            if log_prob > best_log_prob:
                best_log_prob = log_prob
                best_topic = topic

        words_str = ' '.join(original_words)
        prob_rounded = round(best_log_prob, 2)
        results.append(f"{best_topic} | {words_str} = {prob_rounded}")

    return results