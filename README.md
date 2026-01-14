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

Or for specific projects:
```bash
python3 Main.py
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

**Key Features:**
- Grid-based pathfinding with obstacle avoidance
- Performance benchmarks comparing search efficiency
- Visual path representation

**Files:**
- `Main.py` - Entry point
- `pathfinding.py` - Pathfinding algorithm implementations
- `nqueenproblem.py` - N-Queens solver
- `helpers.py` - Utility functions
- `map-generator.py` - Grid generation tool

### 2. **Monte Carlo Method** (EX02)
AI agent for Connect Four game using Monte Carlo simulation:
- Random playouts for move evaluation
- Win-rate based decision making
- Human vs AI gameplay

**Key Features:**
- Simulates thousands of random games per move
- Selects moves with highest win probability
- No machine learning required - pure simulation-based

**Files:**
- `Main.py` - Game controller
- `gameplay.py` - Monte Carlo simulation logic
- `helpers.py` - Board state management

### 3. **Forward Chaining** (EX03)
Logical inference engine using forward chaining:
- Knowledge base with facts and rules
- Automated theorem proving
- Query validation system

**Key Features:**
- Data-driven inference strategy
- Rule-based fact derivation
- Supports complex logical expressions with conjunctions

**Files:**
- `Main.py` - Entry point
- `forwardchaining.py` - Inference algorithm
- `helpers.py` - Parsing and logic utilities

### 4. **Naive Bayes Classifier** (EX04)
Text classification using probabilistic methods:
- Trains on BBC news articles (5 topics: business, entertainment, politics, sport, tech)
- Laplace smoothing for unseen words
- Log-space probability calculations

**Key Features:**
- Word frequency-based topic prediction
- Handles vocabulary with preprocessing (4+ character words)
- Prevents numerical underflow with logarithmic probabilities

**Files:**
- `Main.py` - Entry point
- `train.py` - Model training logic
- `process.py` - Text preprocessing and tokenization

### 5. **N-Gram Text Generator** (EX05)
Language model using n-gram statistics:
- Supports 2-gram, 3-gram, and 4-gram models
- Deterministic text generation
- Corpus-based learning

**Key Features:**
- Tokenizes text into words and sentences
- Builds frequency tables for context prediction
- Deterministic next-word selection (highest frequency → alphabetical tiebreak)

**Files:**
- `Main.py` - Entry point
- `train.py` - N-gram model training
- `process.py` - Tokenization and text processing
- `train.txt` - Sample training corpus

### 6. **Simple Neural Network** (EX06)
Multi-Layer Perceptron (MLP) implemented from scratch:
- Learns logic gates (AND, OR, NAND, XOR)
- Forward and backward propagation
- No ML frameworks - pure NumPy implementation

**Architecture:**
- Input layer: 2 neurons
- Hidden layer: 2 neurons (sigmoid activation)
- Output layer: 1 neuron (sigmoid activation)

**Key Features:**
- Backpropagation with gradient descent
- Mean squared error loss function
- Trains for 10,000 epochs
- Demonstrates XOR non-linear separability

**Files:**
- `Main.py` - Entry point
- `mlp.py` - Neural network implementation
- `utils.py` - Data loading and helper functions

### 7. **Q-Learning** (EX07)
Reinforcement learning agent for grid navigation:
- Tabular Q-Learning implementation
- ε-greedy exploration strategy
- Reward-based learning

**Key Features:**
- Learns optimal policies through experience
- Avoids traps and walls autonomously
- Exploring starts for comprehensive learning
- 50,000 training episodes

**Hyperparameters:**
- Learning rate (α): 0.1
- Discount factor (γ): 0.9
- Initial epsilon (ε): 1.0
- Epsilon decay: 0.99995

**Files:**
- `Main.py` - Entry point
- `learning.py` - Q-Learning algorithm
- `environment.py` - Grid world simulation
- `conf.py` - Configuration parameters
- `utils.py` - Input/output utilities

## Project Benchmarks

### Search Algorithms Performance (200×200 grid)

**Start:** [87,26] | **Goal:** [115,196] | **Lava probability:** 0.35

| Algorithm | Time (s) | Nodes Expanded | Path Length |
|-----------|----------|----------------|-------------|
| BFS       | 0.033    | 22,688         | 260         |
| Greedy    | 0.002    | 692            | 364         |
| A*        | 0.020    | 6,439          | 260         |

**Analysis:** A* provides optimal paths with significantly fewer node expansions than BFS. Greedy is fastest but produces suboptimal paths.

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

## Defense Presentations

Several projects include defense presentation slides (linked in individual READMEs):
- [EX01 - Search Algorithms](https://docs.google.com/presentation/d/1LLHqAwiHtb3kUajXVXnLnadFLqeH3Rv9Awebn9bnVcw/edit?usp=sharing)
- [EX02 - Monte Carlo](https://docs.google.com/presentation/d/11NeFq6YwH5VXAWuGpyZxR0zS-nFsz0ahuftSIGlHaNc/edit?usp=sharing)
- [EX07 - Q-Learning](https://docs.google.com/presentation/d/1UH9YgCLfn7jIDcAuElS37PdPPF7LeM6H/edit?usp=sharing&ouid=109200742404759735467&rtpof=true&sd=true)

## Further Reading

Each project folder contains its own detailed README with:
- Specific algorithm explanations
- Mathematical formulas and derivations
- Step-by-step examples
- Input/output formats
- Usage instructions

For detailed documentation, navigate to the respective project folder.