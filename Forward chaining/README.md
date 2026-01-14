# EX03

## Description

* **EX03's task:**
  * Implement an algorithm that can **prove** the truth of a given statement (**query**) based on a **knowledge base**
  * Use *forward chaining*
* ***Forward chaining:***
  * Forward chaining is a data-driven inference strategy that works as follows:
    * **Start with the known facts.**
    * **Attempt to infer new facts based on the rules.** (i.e., if a rule's premises are met by the known facts, the conclusion is added to the set of new facts.)
    * **The process continues until:**
      * a) **The query is confirmed** (i.e., it is a proven fact).
      * b) **No new facts can be inferred** (i.e., it's no longer possible to prove new statements from the knowledge base).
* **Input/Output:**
  * First line contains the number of facts and rules provided
  * Last line is a query for the algorithm to solve
  * Output can be YES(true) or NO(false)

## Examples
### The whole input:  
```
6
Egg is fragile
Egg falls down  
Egg contains liquid  
Egg is fragile & Egg falls down -> Egg breaks  
Egg breaks & Egg contains liquid -> Egg makes a mess  
Egg is spoiled & Egg breaks -> Egg smells  
[QUERY] 
```

### Example #1
* **Query:**
```
Egg breaks
```
* **Answer:**
``
YES
``
### Example #2
* **Query:**
```
Egg makes a mess
```
* **Answer:**
``
YES
``
### Example #3
* **Query:**
```
Egg smells
```
* **Answer:**
``
NO
``  

### Step-by-Step Reasoning for "Egg makes a mess" Query (Example #2):  
The forward chaining algorithm attempts to prove the query "Egg makes a mess" by systematically inferring new facts from the initial set of known facts.

**Initially known Facts:**
1) F1: Egg is fragile
2) Egg falls down
3) Egg contains liquid

**Rules:**

1) R1: Egg is fragile & Egg falls down → Egg breaks
2) R2: Egg breaks & Egg contains liquid → Egg makes a mess
3) R3: Egg is spoiled & Egg breaks → Egg smells

**Query:**
* Q: Egg makes a mess

**Step 1: Infer a new fact using Rule R1**
 
Check Rule R1: (Egg is fragile & Egg falls down → Egg breaks)

Verify Premises:

[Egg is fragile] is known (F1).

[Egg falls down] is known (F2).

Action: Since both premises are met, the conclusion is added as a New Fact (F4): Egg breaks.

**Step 2: Check all rules again with the updated facts (including F4):**
  
Check Rule R1: No new facts can be generated.

Check Rule R2: (Egg breaks & Egg contains liquid → Egg makes a mess)

Verify Premises:

[Egg breaks] is known (Inferred as F4)

[Egg contains liquid] is known (F3)

Action: Since both premises are met, the conclusion is added as a New Fact (F5): Egg makes a mess.

**Step 3: Termination:**  
  
The fact "Egg makes a mess" (New Fact F5) matches the original query (Q).

The algorithm terminates and concludes the statement is **true**.

**Answer: YES**


## Links
* [Defense slides](https://docs.google.com/presentation/d/1aX88AWbcGVD-bVvfeBiAVbutUBWeWn36NRh11_35Nvk/edit?usp=sharing)
