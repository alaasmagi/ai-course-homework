# EX04

## Description

* **EX04 implements a Naive Bayes text classifier:**
  * Trains on BBC news articles dataset containing five topics: business, entertainment, politics, sport, and tech.
  * Reads a training CSV file and builds a statistical model by counting word occurrences per topic.
  * Predicts the most likely topic for query words using probabilistic calculations.
  * Uses Laplace smoothing to handle words not seen in training data.
  * Calculates probabilities in log space to prevent numerical underflow.
* **Naive Bayes algorithm:**
  * For each query, calculates P(topic | words) = P(topic) × P(word1|topic) × P(word2|topic) × ...
  * Uses the independence assumption: words are treated as independent given the topic.
  * Applies Laplace smoothing: P(w|c) = (N_{w,c} + 1) / (N_c + |V|)
  * Computes prior probability: P(c) = documents_in_topic / total_documents
  * Selects the topic with the highest log probability.
* **Input/Output:**
  * Reads training file name from standard input.
  * Reads number of queries and the query words.
  * Prints predicted topic with log probability for each query: `topic | word1 word2 = -X.XX`

## Model Statistics

After training on `bbc_train.csv`, the model calculated the following statistics. Run `python get_stats.py` to generate these values:

### N_c (Total Word Count per Topic)

| Topic | Total Words (N_c) | Number of Documents |
|-------|------------------|---------------------|
| business | [VALUE] | [VALUE] |
| entertainment | [VALUE] | [VALUE] |
| politics | [VALUE] | [VALUE] |
| sport | [VALUE] | [VALUE] |
| tech | [VALUE] | [VALUE] |

### Vocabulary Size

**|V|** = [VALUE] unique words (filtered to 4+ characters)

## Example Calculation: Query "fifa"

This section demonstrates the step-by-step calculation for predicting the topic of the query word "fifa".

### Step 1: Preprocess the Query

* Original query: `fifa`
* After preprocessing: `fifa` (converted to lowercase, length ≥ 4)
* Query words: `["fifa"]`

### Step 2: Gather Statistics for Each Topic

For the word "fifa" in each topic, we need:
* **N_{fifa,c}**: Count of "fifa" in that topic
* **N_c**: Total words in that topic
* **[V]**: Total vocabulary size (same for all topics)

| Topic | N_{fifa,c} | N_c | [V] |
|-------|-----------|-----|-----|
| business | [VALUE] | [VALUE] | [VALUE] |
| entertainment | [VALUE] | [VALUE] | [VALUE] |
| politics | [VALUE] | [VALUE] | [VALUE] |
| sport | [VALUE] | [VALUE] | [VALUE] |
| tech | [VALUE] | [VALUE] | [VALUE] |

### Step 3: Calculate P(fifa|c) with Laplace Smoothing

Using the formula: **P(w|c) = (N_{w,c} + 1) / (N_c + |V|)**

Example for **sport** (using hypothetical values):
```
N_{fifa,sport} = 44
N_sport = 500,000
|V| = 10,000

P(fifa|sport) = (44 + 1) / (500,000 + 10,000)
              = 45 / 510,000
              = 0.00008824

log P(fifa|sport) = log(0.00008824) = -9.34
```

### Step 4: Calculate Prior Probability P(c)

The prior represents how common each topic is in the training set.

Using the formula: **P(c) = documents_in_topic / total_documents**

Example for **sport** (assuming 510 sport documents out of 2225 total):
```
P(sport) = 510 / 2225 = 0.2292
log P(sport) = log(0.2292) = -1.47
```

### Step 5: Calculate Total Log Probability

The complete formula in log space: **log P(c | w) = log P(c) + log P(w|c)**

Example for **sport**:
```
log P(sport | fifa) = log P(sport) + log P(fifa|sport)
                    = -1.47 + (-9.34)
                    = -10.81
```

### Complete Calculation Table

| Topic | N_{w,c} | P(w\|c) | log P(w\|c) | P(c) | log P(c) | Total log P |
|-------|---------|---------|-------------|------|----------|-------------|
| business | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| entertainment | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| politics | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| sport | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| tech | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |

### Result

The topic with the **highest** (least negative) log probability wins.

**Output**: `sport | fifa = -10.81`

(Your actual values will differ - use output from `get_stats.py`)

## Multi-Word Query Example: "minister Londo"

For queries with multiple words, we apply the Naive Bayes independence assumption.

### Calculation

**Formula**: log P(c | w1, w2) = log P(c) + log P(w1|c) + log P(w2|c)

### Steps:
1. Preprocess: `["minister", "londo"]` (both ≥ 4 characters, original case preserved for output)
2. For each topic, calculate:
   ```
   log P(politics | minister, Londo) = log P(politics) + log P(minister|politics) + log P(londo|politics)
   ```
3. Select topic with highest total probability

**Output**: `politics | minister Londo = -16.39`

## Implementation Details

### File Structure

```
EX04/
├── Main.py          # Entry point, handles input/output
├── train.py         # Training function, builds statistical model
├── process.py       # Preprocessing and prediction functions
├── README.md        # This file
└── get_stats.py     # Helper script to generate statistics
```

### Data Structures

* **word_counts**: `defaultdict(lambda: defaultdict(int))`
  * Nested dictionary: `{"sport": {"fifa": 44, "goal": 123, ...}, ...}`
  * Stores N_{w,c} for all word-topic pairs
* **total_words**: `defaultdict(int)`
  * Dictionary: `{"sport": 500000, "politics": 450000, ...}`
  * Stores N_c for each topic
* **vocabulary**: `set()`
  * Set of all unique words: `{"fifa", "goal", "minister", ...}`
  * Size gives us |V|
* **doc_counts**: `defaultdict(int)`
  * Dictionary: `{"sport": 510, "politics": 417, ...}`
  * Number of documents per topic, used to calculate P(c)

### Text Preprocessing Pipeline

1. **Lowercase conversion**: All text converted to lowercase for consistent matching
2. **Tokenization**: Split text on whitespace
3. **Filtering**: Keep only words with 4 or more characters
4. **Case preservation**: Query words maintain original capitalization in output

Example:
```python
preprocess_text("FIFA World Cup 2024!")
# Returns: ["fifa", "world", "2024"]
# Removes "!" (1 character)

preprocess_query("FIFA World")
# Returns: (["FIFA", "World"], ["fifa", "world"])
# Original case for output, lowercase for calculation
```

### Probability Calculation

The algorithm follows these steps:

1. **Calculate prior P(c)** for each topic:
   ```python
   log_prob = log(doc_counts[topic] / total_docs)
   ```

2. **Add log probability for each word** in the query:
   ```python
   for word in words:
       N_wc = word_counts[topic].get(word, 0)  # Default 0 if unseen
       N_c = total_words[topic]
       V = len(vocabulary)
       
       # Apply Laplace smoothing
       p_w_given_c = (N_wc + 1) / (N_c + V)
       log_prob += log(p_w_given_c)
   ```

3. **Select topic** with highest total log probability

### Why Use Logarithms?

Multiplying many small probabilities can cause **numerical underflow** (values become too small to represent).

**Solution**: Use logarithms to convert multiplication to addition:
```
log(a × b × c) = log(a) + log(b) + log(c)
```

**Benefits**:
* Numerically stable (avoids underflow)
* Preserves ordering: if a > b, then log(a) > log(b)
* Makes calculations with very small numbers manageable

Example:
```
Direct multiplication:
P(sport | fifa, goal, match) = 0.23 × 0.000088 × 0.00015 × 0.00012
                              ≈ 3.6e-13  (extremely small!)

Log space:
log P(sport | fifa, goal, match) = -1.47 + (-9.34) + (-8.81) + (-8.93)
                                  = -28.55  (manageable!)
```

### Why Use Laplace Smoothing?

**Problem**: If a word never appears in a topic's training data, the probability becomes zero, which causes the entire calculation to fail.

**Without smoothing**:
```
P(cryptocurrency|sport) = 0 / 500000 = 0
→ P(sport | cryptocurrency, goal) = P(sport) × 0 × P(goal|sport) = 0
```

**With Laplace smoothing**:
```
P(w|c) = (N_{w,c} + 1) / (N_c + |V|)

P(cryptocurrency|sport) = (0 + 1) / (500000 + 10000) = 1/510000 ≈ 0.000002
→ Small but non-zero probability, calculation can continue
```

**How it works**:
* Adds 1 to the numerator (gives unseen words a count)
* Adds |V| to the denominator (balances across all words in vocabulary)
* Ensures all probabilities > 0
* Known words still get higher probabilities based on actual counts

## Testing

### Generate Statistics

```bash
python get_stats.py
```

This outputs all the statistics you need to fill in the README values.

### Run the Classifier

```bash
python Main.py
```

**Example Input**:
```
bbc_train.csv
3
fifa
minister Londo
phones technology
```

**Example Output**:
```
sport | fifa = -10.38
politics | minister Londo = -16.39
tech | phones technology = -14.11
```

## Key Implementation Notes

* Model learns word frequencies from training data
* Laplace smoothing prevents zero probabilities for unseen words
* Log space calculations prevent numerical underflow
* Prior probability P(c) accounts for different topic frequencies in training data
* Case preserved in output but matching is case-insensitive
* Words under 4 characters are filtered out to reduce noise

## Links

* [Defense slides](https://docs.google.com/presentation/d/1-a3gZaHT4CMoP6O8ROS_2QEaN8Db8IAGdPjMfs910zw/edit?usp=sharing)