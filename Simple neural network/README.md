# EX06

## Simple Neural Network (MLP)
This project implements a small fully connected neural network (Multi-Layer Perceptron) that learns to reproduce the behavior of 2-input logic gates (AND, OR, NAND, XOR).  
All training is done from scratch, without machine-learning frameworks — only NumPy is used.

The network supports:

- Forward propagation  
- Backpropagation with gradient descent  
- Training on custom datasets  
- Predicting the logical output for a given 2-variable input  

---

## Network Architecture

The MLP structure is fixed:

| Layer  | Neurons | Notes                              |
|--------|---------|-------------------------------------|
| Input  | 2       | x₁, x₂                              |
| Hidden | 2       | sigmoid activation                  |
| Output | 1       | sigmoid activation → probability    |

- All weights are initialized randomly in range **[-1, 1]**  
- All biases are initialized to **0** (as required by the assignment)

---

## How the System Works

### 1. Forward Propagation

Each neuron computes:

g(-b + Σwᵢxᵢ),   g(x) = 1 / (1 + e⁻ˣ)

Steps:

1. Compute hidden layer activations  
2. Compute output layer activation  
3. Output is a probability between 0…1  
4. Final program output = round(output) → **0 or 1**  

---

## 2. Loss Function

The model uses mean-squared error (with ½ factor):

L = 1/2 * (y - ŷ)²

This simplifies derivatives during backpropagation.

---

## 3. Backpropagation

### Output neuron error:
δₒ = (ŷ - y) * ŷ * (1 - ŷ)

### Output layer weight updates:
Wₒ = Wₒ - η(δₒ hᵀ)  
bₒ = bₒ - η(δₒ ⋅ -1)

### Hidden layer error:
δₕ = (Wₒᵀ δₒ) ⋅ h(1 - h)

### Hidden layer updates:
Wₕ = Wₕ - η(δₕ xᵀ)  
bₕ = bₕ - η(δₕ ⋅ -1)

These formulas match the assignment specification.

---

## 4. Training Loop

- The dataset is read from a text file structured as:

  x1 x2 y  

  Example:
  0 1 1  
  1 1 0  

- Each epoch iterates over the entire dataset  
- The model trains for **10,000 epochs**  
- Default learning rate: **0.5**

This is sufficient for learning all logic gates, including XOR.

---

## Why XOR Requires a Hidden Layer

AND, OR, and NAND are **linearly separable** — a single straight line can divide their 0-outputs and 1-outputs.

XOR is **not** linearly separable:

- No single line divides the XOR classes  
- A hidden layer provides **non-linearity**  
- Two hidden neurons are enough to model XOR perfectly  

---

## Accuracy on the XOR Problem

After 10,000 training epochs:

- The model converges reliably  
- All four XOR cases are predicted correctly  
- Accuracy reaches **100%**

Example model outputs (before rounding):

| Input | Target | Output |
|--------|--------|---------|
| 0 0    | 0      | ~0.02 |
| 0 1    | 1      | ~0.97 |
| 1 0    | 1      | ~0.98 |
| 1 1    | 0      | ~0.01 |

---

## Hyperparameter Observations

### Learning Rate (η)

| η value | Behavior |
|---------|----------|
| too low (< 0.1) | training very slow, may stagnate |
| optimal (~0.5)  | fast, stable convergence |
| too high (> 1.0) | loss oscillates, may diverge |

### Epoch Count

- AND / OR / NAND learn within hundreds of epochs  
- XOR stabilizes between 2000–8000 epochs  
- 10,000 epochs ensures stable convergence  

---

## Files Used in This Solution

### Main.py
- Reads training filename and test input  
- Loads dataset  
- Trains the MLP  
- Prints round(prediction)

### mlp.py
Contains:
- Initialization  
- Forward propagation  
- Backpropagation  
- Training loop  
- Prediction  

### utils.py
Contains sigmoid, derivative, and data loader.

---

## Example Usage

Input:
```
test_xor.txt
1 0
```

Output:
```
1
```

---

## Summary

This project demonstrates how a simple neural network can be implemented entirely from scratch using only NumPy.  
The model successfully learns all 2-input logic gates, including **XOR**, showcasing the power of hidden layers and gradient-based optimization.


## Links

* [Defense slides](https://docs.google.com/presentation/d/1zvRoD5dW3bWITmwI18T-xgC6H66ggb_J/edit?usp=sharing&ouid=109200742404759735467&rtpof=true&sd=true)