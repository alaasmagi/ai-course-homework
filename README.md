# AI Course Homework - Collection of Artificial Intelligence Algorithms

## Description

**Language:** Python  
**Development year:** 2025  
**Languages and technologies:** Python 3, NumPy

This repository contains a collection of fundamental artificial intelligence and machine learning algorithms implemented from scratch as part of an AI course. Each project demonstrates core concepts in different areas of AI, including search algorithms, inference systems, probabilistic models, neural networks, and reinforcement learning.

## How to Run

Each project can be executed independently via terminal/cmd by navigating to its folder and running:

```bash
python Main.py
```

## Prerequisites

- Python 3.7 or higher
- NumPy (for neural network project)
- No external ML frameworks required (all algorithms implemented from scratch)

## Repository Structure

This repository contains 7 distinct AI projects:

### 1. **Search Algorithms** (EX01)
Implements fundamental pathfinding and constraint satisfaction algorithms:
- **Pathfinding Algorithms:**
  - BFS (Breadth-First Search)
  - Greedy Best-First Search
  - A* Search Algorithm
- **Constraint Satisfaction:**
  - Hill Climbing for N-Queens Problem

### 2. **Monte Carlo Method** (EX02)
AI agent for Connect Four game using Monte Carlo simulation:
- Random playouts for move evaluation
- Win-rate based decision making
- Human vs AI gameplay

### 3. **Forward Chaining** (EX03)
Logical inference engine using forward chaining:
- Knowledge base with facts and rules
- Automated theorem proving
- Query validation system

### 4. **Naive Bayes Classifier** (EX04)
Text classification using probabilistic methods:
- Trains on BBC news articles (5 topics: business, entertainment, politics, sport, tech)
- Laplace smoothing for unseen words
- Log-space probability calculations

### 5. **N-Gram Text Generator** (EX05)
Language model using n-gram statistics:
- Supports 2-gram, 3-gram, and 4-gram models
- Deterministic text generation
- Corpus-based learning

### 6. **Simple Neural Network** (EX06)
Multi-Layer Perceptron (MLP) implemented from scratch:
- Learns logic gates (AND, OR, NAND, XOR)
- Forward and backward propagation
- No ML frameworks - pure NumPy implementation

### 7. **Q-Learning** (EX07)
Reinforcement learning agent for grid navigation:
- Tabular Q-Learning implementation
- ε-greedy exploration strategy
- Reward-based learning

## Educational Value

Each project demonstrates fundamental concepts:

1. **Search Algorithms** - Pathfinding and optimization
2. **Monte Carlo** - Simulation-based decision making
3. **Forward Chaining** - Logical inference and symbolic AI
4. **Naive Bayes** - Probabilistic classification
5. **N-Gram** - Statistical language modeling
6. **Neural Network** - Deep learning fundamentals
7. **Q-Learning** - Reinforcement learning

## Implementation Philosophy

All algorithms are implemented **from scratch** without relying on high-level ML frameworks. This approach ensures:
- Deep understanding of algorithm internals
- Transparency in how each method works
- Educational clarity over production efficiency
- Minimal dependencies

## Further Reading

Each project folder contains its own detailed README with:
- Specific algorithm explanations
- Mathematical formulas and derivations
- Step-by-step examples
- Input/output formats
- Usage instructions

For detailed documentation, navigate to the respective project folder.
