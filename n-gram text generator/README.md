# EX05

## N-Gram Text Generator

This project implements a simple **deterministic n-gram language model** (supporting 2-, 3-, and 4-grams) that learns word sequences from a training corpus and generates new text based on seed words.

---

## How the System Works

### 1. **Tokenization**

The tokenizer:

* Splits text into sentences using `. ? !`
* Splits sentences into words using spaces and punctuation
* Appends `<EOS>` to mark sentence boundaries
  This results in a clean word-level token stream.

### 2. **Training**

`train_ngrams()` builds frequency tables for:

* **2-grams**, **3-grams**, **4-grams**
  Each model maps:

```
(history) -> { next_word: count }
```

### 3. **Deterministic Generation**

`generate()` tries:

1. 4-gram continuation
2. fallback to 3-gram
3. fallback to 2-gram
4. stop if no continuation or if `<EOS>` appears

The next word is selected using:

```
highest frequency → alphabetical tiebreak
```

This ensures fully deterministic output.

---

## Model Output Comparison

Below is an example of how the same seed can behave differently across n-gram sizes.

### **2-gram output**

* Uses only one previous word.
* Sentences tend to be jumpy and less grammatical.

Example:

```
cat is small and the dog is...
```

### **3-gram output**

* More context improves coherence.

Example:

```
cat is small and the cat eats fish...
```

### **4-gram output**

* Longest histories → most grammatical and stable.
* Often reconstructs real sentences from the corpus.

Example:

```
cat is small and the cat eats fish <EOS>
```

### **Summary**

| Model  | Context Size | Typical Quality                    |
| ------ | ------------ | ---------------------------------- |
| 2-gram | 1 word       | choppy, random transitions         |
| 3-gram | 2 words      | more coherent                      |
| 4-gram | 3 words      | most natural, closest to real text |

Increasing **n** → more structure, fewer unexpected jumps.

---

## Deterministic vs Random Sampling

### Deterministic (your implementation)

* Always picks the most frequent next word
* Uses alphabetical tiebreak
* **Same input → same output every time**

Example:

```
("cat", "is") → {"small": 3, "hungry": 1}
→ always "small"
```

### Random Sampling (not implemented, theoretical comparison)

Selecting based on probability distribution:

```
small: 75%
hungry: 25%
```

Example outputs with randomness:

```
cat is small and...
cat is hungry and...
cat is small and...
```

Deterministic: predictable
Random: more creative but inconsistent

---

## Files Used in This Solution

### **main.py**

* reads filename and seed words
* trains the model
* generates text deterministically

### **process.py**

Includes:

* `deterministic_choice()`
* `generate()`

### **train.py**

Includes:

* tokenizer
* file loader
* n-gram training logic

---

## Example Usage

```
$ python3 main.py
train.txt
cat is
```

Output:

```
cat is small and the cat eats fish
```

## Links

* [Defense slides](https://docs.google.com/presentation/d/1MxRmsqW8Nm_W-wf59My2M8ewfzdpNNmK/edit?usp=sharing&ouid=109200742404759735467&rtpof=true&sd=true)

