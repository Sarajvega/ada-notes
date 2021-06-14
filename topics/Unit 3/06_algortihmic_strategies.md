# Algorithmic Strategies

When we understand the kind of solution or algorithm we are using or can use, we can more easily read and understand it.

- Divide and Conquer Algorithm: An algorithm design strategy based on multi-branched recursion. We recursively break down a problem into two or more subproblems of the same or related type, until these become simple enough to be solved directly. The solutions to the subproblems are then combined to give a solution to the original problem.
- Pivot: An element used in QuickSort to divide the array into two sections, one section less than the pivot and the other greater than the pivot. The choice of the pivot has enormous implications for the efficiency of QuickSort.


## Divid and Conquer
Divide and Conquer is an approach to problem solving that breaks down a large problem into multiple, smaller subproblems.

When we write a divide-and-conquer solution we can follow these steps:
1. Break the problem into subproblems of the same type
2. Recursively solve the subproblems
3. Combine the solved subproblems to solve the larger problem

In this case, the distinction between a general recursive algorithm, and one that might be called "divide and conquer," is largely based on how much we're able to divide the original problem at each recursive step.

**Example: Binary Search**
Binary search can be considered a divide-and-conquer algorithm because it divides the array in half with each step. No matter how large the original array was, at each step we'll be able to discard half the remaining data from consideration!

Description:
1. Starting with a sorted array, we check whether it contains a particular value by comparing the search value with the element in the middle of the array.
2. If we find the value we return the position where it was found.
3. If we don't find the value, we determine whether it would be in the left or right half of the array by seeing whether it is smaller or larger than the middle element. Remember, we can make this decision because we assume the array is sorted! Then we perform a binary search on the selected half.
4. If at any point, we end up with an empty range, we know the value was not in the array, and we can return a result indicating the value was not found, such as None. Other variations of binary search may return the index of where the value should have been, but as a negative value to indicate that it was missing.
5. Each recursion divides the array in half and performs the binary search on a smaller subproblem.

Code example:
```python
def recursive_binary_search(array, to_find, low=0, high=None):
    if high is None:
        high = len(array)

    if high <= low:
        return None

    mid = (high + low) // 2

    if array[mid] == to_find:
        return mid
    # to use binary search the array must be sorted. 
    elif array[mid] > to_find:
        high = mid
    else:
        low = mid + 1

    return recursive_binary_search(array, to_find, low, high)

```

**Example: QuickSort**
QuickSort is an algorithm which takes a divide-and-conquer approach to sorting an array by using the following steps:
1. If the array is only one element or empty, we are done, the array is sorted.
2. Pick an element from the array as the pivot.\
3. Move all elements smaller than the pivot to the left and all elements larger than the pivot to the right. Note that the pivot is now in the correct index. **Picking a pivot and rearranging the elements is referred to as partitioning.**
4. Perform QuickSort on the left and right sides of the pivot.

In terms of divide and conquer, we pick a pivot and move smaller elements to the left, and larger elements to the right. This leaves us with two smaller subproblems: sorting the elements on the left, and those on the right. **We call QuickSort on each side.**

**Weakness of QuickSort: The Pivot**
Again, QuickSort is O(n log n) if the pivot is well-chosen. If the pivot does not break the list into two relatively equal subarrays, it will not arrive at a O(n log n) runtime. Instead, it will approach a O(n2) runtime.

For example, if with each iteration the pivot is the smallest remaining element in an array, rather than splitting the array into approximately n/2 sized pieces, instead we have one subarray of size n-1.

code example:
```python
def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array)

    # if the array has 0 or 1 elements, it's already sorted
    if high - low <= 1:
        return

    # partition the current list to find where one element goes
    partition_pos = partition(array, low, high)

    # sort the left and right sides
    quicksort(array, low, partition_pos)
    quicksort(array, partition_pos + 1, high)

def partition(array, low, high):
    # take the last item as the pivot
    # high - 1 bc first index = 0
    last = high - 1
    pivot = array[last]

    # assume pivot will end up at the start
    # conceptually, this position marks the end of the smaller list
    p_index = low

    # iterate over the values not including the pivot
    i = low
    while i < last:
        # if the current value should be to the left of the pivot, swap
        # this value to the potential pivot location and advance that
        # location. conceptually this adds the value to the end of the
        # smaller list and tracks the new end of this list
        if array[i] < pivot:
            temp = array[i]
            array[i] = array[p_index]
            array[p_index] = temp
            p_index += 1
        i += 1

    # swap the pivot value to the end of the smaller list. after this
    # swap, we know that all values to the left of the pivot are smaller,
    # and all values to the right of the pivot are greater or equal
    temp = array[i]
    array[i] = array[p_index]
    array[p_index] = temp

    return p_index
```

There are a variety of strategies for selecting the pivot, and for how to rearrange the elements around the pivot. 
(make notes here)

**Example: Merge Sort**
Merge sort is another divide-and-conquer algorithm. It involves the following three stages:
1. Divide the array into two subarrays at each step until each subarray is of size one.
   1. starting index to 0.
   2. ending index is one past the last elem bc the ending index is exclusive.
   3. midway index is calc'd by
      1. `midway index = ⌊(starting index + ending index) / 2⌋`
      2.  ⌊⌋ denotes the mathematical floor operation, or integer truncation.
2. Sort each subarray with the merge sort algorithm. (An array of size one is trivially sorted.)
3. Merge the subarrays into one array by combining two subarrays into one at each step.

**Complexity**
- Since merge sort always divides the list in half at each divide step, there will be log n levels in the division phase. 
- By keeping data in place, and only adjusting indices to keep track of where the subarrays are located, at each level, there are at most n calculations, for a time complexity of the division phase of O(n log n).
- In the merge phase, there will still be log n levels of mergers, and at each level of the merge, there are n copies from the split arrays into the auxiliary array, and n copies back into the original array, giving a total complexity for the merge phase of O(2n log n).
- Combining the divide and merge phases, we get a total complexity of O(3n log n), which after dropping the coefficient gives us O(n log n).

Code example: 
```python
def merge_sort(array, low=0, high=None):
    if high is None:
        high = len(array)

    # if the array has 0 or 1 elements, it's already sorted
    if high - low <= 1:
        return

    # find the midway point where we will divide
    mid = (low + high) // 2

    # apply merge sort to each half of the array
    merge_sort(array, low, mid)
    merge_sort(array, mid, high)

    # merge the sorted left and right subarrays
    merge(array, low, mid, high)

def merge(array, low, mid, high):
    merged = []
    l = low
    r = mid

    # continue merging by comparison until one subarray is empty
    while l < mid and r < high:
        # take either the left or right value
        if array[l] <= array[r]:
            merged.append(array[l])
            l += 1
        else:
            merged.append(array[r])
            r += 1

    # if there was data remaining in the left array take the rest
    while l < mid:
        merged.append(array[l])
        l += 1

    # or if there was data remaining in the right array take the rest
    while r < high:
        merged.append(array[r])
        r += 1

    # copy from the auxiliary array back to the main array
    m = 0
    l = low
    while l < high:
        array[l] = merged[m]
        l += 1
        m += 1
```

## Dynamic Programming
- Dynamic Programming:An algorithmic strategy of breaking a problem down into subproblems that need to be calculated multiple times, allowing us to improve performance by storing results and reusing them.
- Memoizing: 	An optimization technique used primarily to speed up algorithms by storing the results of subproblems and returning the cached result when the same subproblem occurs again.
The key concept of dynamic programming is to recognize subproblems we solve again and again, and store the solutions to those problems. **This is called memoizing**. Then we use the stored solutions to help solve the larger problems.

A dynamic-programming problem breaks the problem into subproblems and saves the solutions to those subproblems. **The key difference is that in dynamic programming the subproblems are often overlapping, such that we need the solution to a particular subproblem multiple times.**

In a nutshell:
```*writes down "11111111" on a sheet of paper*
"How many 1s are there?"
*counting* "Eight!"
*writes down another "1"*
"How about now?"
*quickly* "Nine!"
"How'd you know it was nine so fast?"
"You just wrote one more"
"So you didn't need to recount because you remembered there were eight!
  Dynamic programming is just a fancy way to say:
  'remembering stuff to save time later'"
```
**Example: Fibonacci**
Let's recall what the Fibonacci sequence is fibonacci(n):

fibonacci(0) = 0, for 
fibonacci(1) = 1, for 
fibonacci(n) = fibonacci(n-1) + fibonacci(n-2), for n>1.

You could use recursion:
```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```
But its inefficient. fibonacci(1) and fibonacci(0) will be called with every function call. 

Instead of solving the same problems over and over again we can solve these problems by storing them in a memo and using the stored subproblems to make calculating the larger problem more efficient.

Example solutions:
**Iterative**
```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    solutions = [0, 1]
    current = 2

    while current <= n:
        solutions.append(solutions[current - 1] + solutions[current - 2])
        current += 1

    return solutions[n]
```

**Recursive**
```python
def fibonacci_recursive(n, solutions=None, current=None):
    if solutions is None:
        solutions = [0, 1]
        current = 2

    solutions.append(solutions[current - 1] + solutions[current - 2])

    if n <= current:
        return solutions[n]

    return fibonacci_recursive(n, solutions, current + 1)
```

**'Fixed' recursive**
```python
def fibonacci_recursive(n, solutions=None):
    if solutions is None:
        solutions = {}

    if n in solutions:
        return solutions[n]

    if n == 0 or n == 1:
        solutions[n] = n
    else:
        solutions[n] = (fibonacci_recursive(n - 1, solutions) +
            fibonacci_recursive(n - 2, solutions))

    return solutions[n]
```


**Example: Longest Common Subsequence**

Let's create a function named lcs, which stands for "longest common subsequence." The longest common subsequence problem is relevant to a lot of different subjects, such as comparing gene sequences, or even creating Git diffs!

**idea**
str1 = "abcde"
str2 = "ace"
subsequence = "ace"
length(result) = 3

One approach we might take to solve this problem is at each position, to consider the current letter in each string and the remaining portion of each string. If the current characters match, they contribute one matched character count to our total length, plus however many matches there are in the remainders of the strings.

**recursive example:**
```python
def lcs(str1, str2):
    if not str1 or not str2:
        return 0

    # split the first character from the rest
    first1 = str1[0]
    rest1 = str1[1:]
    first2 = str2[0]
    rest2 = str2[1:]

    # is this spot a match?
    if first1 == first2:
        current_score = 1
    else:
        current_score = 0

    # the result for this position is the max of the current score
    # and each of the maxes from the three possibilities:
    # 1. advance both characters (adding to score if a match)
    # 2. advance only the first character
    # 3. advance only the second character
    result = max(
        current_score + lcs(rest1, rest2),
        lcs(rest1, str2),
        lcs(str1, rest2)
    )

    return result
```
But the above is inefficient. 

Use memos! 

```python
# include a parameter to receive the memo
def lcs(str1, str2, memo=None):
    if not str1 or not str2:
        return 0

    # initialize the memo or lookup the current values
    if memo is None:
        memo = {}
    elif str1 not in memo:
        memo[str1] = {}
    elif str2 in memo[str1]:
        return memo[str1][str2]

    first1 = str1[0]
    rest1 = str1[1:]
    first2 = str2[0]
    rest2 = str2[1:]

    if first1 == first2:
        current_score = 1
    else:
        current_score = 0

    result = max(
        # include the memo in the recursive calls
        current_score + lcs(rest1, rest2, memo),
        lcs(rest1, str2, memo),
        lcs(str1, rest2, memo)
    )

    # store this calculation for later
    memo[str1][str2] = result

    return result
```