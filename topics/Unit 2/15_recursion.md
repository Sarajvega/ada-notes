# Intro to Recursion
### Summary


## Vocab
- Recursion: Process of defining something in terms of itself. 
- Base Case: a condition which will end the rescursion and cause the func to immediately calculate a solution.
- Recursive Case: Situaton in a recursive func that will call the function itself with a smaller problem.
- Stack: A data structure that operatoes as Last-in-First-Out where new data is pushed onto the top and data is popped off the top. 
- Call stack: Part of memory dedicate to storing the medoth calls and local variables of a running program. 

## Base cases
Base Case = stopping condition. 
Recursive algorithms will usually take in at least one argument. A recursive algorithm handles different situations based on the value of the argument. The algorithm should handle:
- At least one base case
  - responsibility of the base case is to immediately answer a particular form of the problem.
- At least one recursive case
  - responsibility of the recursive case is to transform the current problem into one that can be expressed as a "smaller" version of the same problem.