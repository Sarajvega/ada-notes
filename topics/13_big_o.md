# Big O
Algorithm: specific process, set of rules, or solution.
Efficient: quality of code that means it is fast/doesn't take up much memory
Time Complexity: A Measurement of how the amount of time an alg take to run as size of input changes.

Space complexity: measurement of how much mem an algorithm uses as size of input changes. 

Best/Worst/Avg cases
Best = alg finished the most efficiently it can ever be.
Worst = performs inefficiently in one or both aspects: alg takes max time, alg consumes mac memory
Avg = more common, neither best/worst.
Find which is more efficient by comparing the time and space complexity. 

## Big O Notion
Comparing space complexity. 
Big O - a notion to describe how the run time or space reqs grow as the input size grows. "describes the limiting behavior of a function when the argument tends towards infinity."
- Using big O we can make quantitative judgements about efficiency of an alg
- Predict whether the software will meet any efficiency constraints that exist.

O(n) <-- n = mathmatical expression that describes the relationship btwn size input/complexity of alg. 

going from least complex to most complex
going from fastest to slowest in time complexity
going from least operations to most operations in time complexity
going from most space efficent to least space efficent in space complexity
going from slower-growing to faster-growing

1. O(1) - Constant - alg take the same amount of tiem to execute regardless of input size. The algorithm will take the same amount of time to execute regardless of the size of the input.
2. O(log n) - Logarithmic - alg grows in complexity proportional to the base 2 log of the input size. Increase v slowly as input size incr. Usually involv w an alg that excludes 1/2 of the inpyt with each iteration of a loop. The algorithm will grow in complexity proportional to the base 2 log of the input size. Logarithmic algorithms increase very slowly as the size of the input increases. They usually involve an algorithm which excludes 1/2 of the input with each iteration of a loop.
3. O(n) - inear - Grow in time or space directly prop. to the input size.  The algorithm will grow in time or space directly proprotional to the input size. The complexity increases at the same rate that the input increases.
4. O(n log n) - Log Linear - Alg whcih grow in time/space complexitiy prop. to the n log n (input size mult by base 2 log of that input size) of the input size.A term used to describe an algorithm which will grow in time or space complexity proportional to the n log n of the input size. "n log n" means that the input size is multiplied by the base-2 log of the input size. 
5. O(n^2) - Quadratic - Alg have a runtime or memory usage prop to the side of input squared. The algorithm will have a runtime or memory usage proportional to the size of the input squared. This often involves 2 nested loops.
6. O(2^n) - Alg complexity doubles each time input size incr by 1. The algorithm's complexity doubles each time the input size increases by one.

These don't give exact numbers. The curve of expression describes how the alg will perform. 

## Big O Analysis

Time complexity = # of operations. 
Finding a formula that captures how many operat. an alg. executes:
1. Read code n identify all lists that have a variable size. 
   1. One list = n # of elements
2. Ident all operations in alg.
3. Recog which operations are related to the list of size n
   1. oper in a for loop get mult n times
4. Create an equation that reps how many operations there are
   1. use n as a variable
5. Drop constants and finding dominant order
6. Match this Big O to the most relevant compelxity. 

Example:
```python
def linear_search(input_list, item):
    for i in range(len(input_list)):
        if item == input_list[i]:
            return i
    return False
```
1. input_list and its size n. 
2. operations are: `if item == input_list[i]` and `i in range(len(input_list))`
3. Which operations have a relationship to list size: `if item == input_list[i]` can happen n times and so can `i in range(len(input_list))`.
4. two operations can happen n times so 2n
5. Drop constants: 2n, we can drop the 2. so we have n.
6. n matches O(n)

Larger example:
```python
def reverse(input_list):
    if len(input_list) <= 1:
        return input_list

    i = 0
    j = len(input_list) - 1

    while i < j:
        temp = input_list[i]
        input_list[i] = input_list[j]
        input_list[j] = temp

        i += 1
        j -= 1

    return input_list
```

1. One list with a size of n
2. There are 10 operations.
   1. `len(input_list) <= 1`
   2. `i=0`
   3. `j = ... `
   4. `len(input_list) - 1`
   5. `i < j`
   6. `temp = ...`
   7. `input_list[i] = ...`   
   8. `input_list[j] = ...`
   9. `i += 1`
   10. `j -= 1`
3. Which operations have a relat. w/ list size  - 4 operations outside while loop happen only once. 6 operations inside happen n times. 
4. Formula = 4 + (6n)
5. Drop constants - 4+ and 6 * -- gives us n
6. O(n)

What is dropping the constant/Finding dominant order?
In complexity analysis, we want to find the part of the complexity that affects it the most. One step is to drop the constants. Constants don't change the curve significantly.

## Space complexity
Space complex = amount of memory allocated to the alg.
Count number of new values stored. 
Note: lists require more memory than a single value. 

## Generic Steps
1. Read through the code, and identify all places where a variable is initially assigned (initialized).
  1. We do not need to count re-assignment of variables, as the value will occupy the same memory as the initial assignment
2. Recognize which variables have a value that could take a variable amount of memory
  1. Typically, storing a list will require n amount of memory
3. Create an equation that represents how many values are initialized and stored in memory
4. Drop the constants and find the dominant order
5. Match this Big O to a relevant complexity

example:
```python
def linear_search(input_list, item):
    for i in range(len(input_list)):
        if item == input_list[i]:
            return i
    return False
```
1. i, item, input_list
2. Whic vars hold memory: item and i.
3. Equation to rep amount of memory: 1+1, so 2.
4. Drop constant. Drop 2.
5. Leaves us w/ O(1)

## Comparing 2 Algos
Alg a = Time complex = O(n) and Space complex = O(1)
Alg B = O(n) amd O(n)
Therefore Alg A is more performant. 

Alg B work: 
```python
def reverse(input_list):
    if len(input_list) <= 1:
        return input_list

    i = 0
    j = len(input_list) - 1
    # This syntax creates a list of Nones, and has the length of input_list
    temp_list = [None] * len(input_list)

    while i < len(input_list):
        temp_list[i] = input_list[j]
        i += 1
        j -= 1

    i = 0
    while i < len(input_list):
        print(i)
        input_list[i] = temp_list[i]
        i += 1

    return input_list
```

A time complexity analysis:
1. A few operations outside of loops.
2. 2 loops that iterate over n elements
3. Expression would be (some # of op outside loop) + 2n
4. Drop constants to O(n)
5. Alg performs on linear time complexity.

A space complexity analysis:
1. i and j are initialized
2. temp_list has n elements
3. express at 2 + n
4. drop to O(n)
5. Alg performs on linear space complexity. 

Check:
Whats the time complexity of:
```python
def greet_friends(input_list):
    i = 0
    while i < 17:
        print(f"Hello, Friend #{i + 1}!")
        i += 1
```

Answ: O(1), runs 17 times regardless of size. 

Whats the time complexity of:
```python
def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < 17:
        for j in range(count):
            print(f"Hello, Friend #{i+1} in {j+1}!")
        i += 1
```

answ: O(n) - 2 nested loops, outer loop runs 17 times, innner = n. Total = 17 * count times. Drop 17 and you get n. 

Whats the time complexity of:
```python
def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < count:
        for j in range(count):
            print(f"Hello, Friend #{i+1} in {j+1}!")
        i += 1
```

answ: O(n^2) - 2 loops that run n time. so N*n = n^2. This is quadratic. 

Whats the time complexity of:
```python
def search(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            return mid

    if input_list[low] == value:
        return low

    return None
```
Answ: O(log n) - One loop in this method. The times the loop runs is determined by input_lists val. W/each iteration half of items are eliminated. 

* still dont get this one *

Example: Imagine a password of length n that can contain only digit values (numbers)...What will be the time complexity for a brute force solution  to break the password?

Answ: O(10^n) - To break password of n size, each val can only be a digit 0 - 9. We start w/ 0 (this is where the 10 comes from.) So if the password is 3 digits long, each digit could be 1 of 10 possibilities (0-9), resulting in 10*10*10 or 10^3. 
Since the number of digits is unknown in this scenario, O(10^n) best reprensents the time complexity. 

Example:
A traveling salesperson wants to visit n cities. They can start the journey at any city and must visit each city once. How many different possibilities exist for the order in which they could visit all n cities?


Answ: O(n!) - We start by choosing a city to start. there are n possibilites. For each choise of first city, there are n-1 options for the second and n - 3 for the third...etc. If there were only 3 cities to start from, there would be 6 possibilities.

Atlanta → Boston → Chicago
Atlanta → Chicago → Boston
Boston → Atlanta → Chicago
Boston → Chicago → Atlanta
Chicago → Atlanta → Boston
Chicago → Boston → Atlanta

which is the sames as 3 * 2 * 1 or 3!. 


### Extra notes on Logarithms
2^3 = 8, so Log2(8) = 3. --> What do we need to power 2 by to get 8? 3 
x^z = y so LogX(Y)=Z

#### other questions
Why do we consider the worst-case scneario when we measure time/space complexity?
Big O tells us how the time/memory an algo will consume as the size of the input increases. 

Why Does big O not give us an exact #?
How long algs will take depends on external facotirs like speed of machine, other apps, etc.