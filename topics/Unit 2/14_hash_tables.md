# Hash Tables Overview

### Summary
**What is a hash table?**
- Hash tables (also called hash map) are a data structure which allow quick lookup of a value by using a key. Each key is mapped to an index of an internal array with a specialized method called a hash function. The average-case lookup is O(1) and the worst-case is O(n). However, most good implementations use a hash function which attempts to uniformly distribute elements and prevent collisions.
- index is related to the data. 
- Used in data base indexing, error checking, etc.
- Used to store key val pairs. Like name and DOB. 
**What is a hash function?**
- Calc applied to a key to transform it into a relatively small index number that corresponds to a position in the hash table. 

**How does a hash table resolve a collision?** 
- Can look for next avail position = open addressing. Any location open to any item. 
  - linear probing = if calc address occupied a linear search is used to find the next slot. 
  - Finding an item will also involve linear probing. 
- More items = more collisions. 
- Load factor = total num of items stored / size of array.
  - Can use to resize an array. If load factor is certain threshold, add more slots. 

`% len(hash_array)` = a good way to limit inputs to size of array.

Iteration through a list = O(n) if unsorted.
If sorted = Log(n).
Else if in a key/val pair (dict), is O(1)! A constant time. 
 - this is a hash table in action.

## Vocab
- Hash Table: Data structure that implements an associatvie array that maps unique key identified to values
  - Associative Array: Abstract data type. Theoretical data structure that describes collections that store key-value pairs. 
    - Use a key to look up a corresponding value. 
  - Abstract data type: any theoretical data structure that is described not by its concrete implementation, but by its behavior and how it's used.
- Hash Function: Function used by a hash table to map a key to an index.
- Collision: Whem multiple keys map to the same elem in a hash table internal array. 

## Hash Tables
- Data structue that stores key/val pairs. 
- Have a method to look up a val but its key (find)/add a key-val pair(insert) and delete a key-val pair (remove).
- Time complexity = O(1)
  - searching for an item in an array using linear search has a time complexity of O(n)...how is this possible?
    - Store key vals in pairs. 
    -  take advantage of how arrays have O(1) lookup operations when given an index.
    -  Hash table has an internal array used for storage.
    -  When key/val pair inserted - its stored in the internal array at a specific position.
    - Uses hash functions to convert a key into an index in the invernal array. 

## Time Complexity
- Operations of inserting, finding, and deleting values, hash tables have a O(1) time complexity on avg.
  - Worst Case = O(n). 
  - **Why do we describe it by the average case?**
    - A well-designed hash table will attempt to prevent the worst-case scenario from occurring. Therefore when we work with hash tables we assume the average case. 

## Hash Functions
- map a given key into an integer index in the internal array
- Example:
  - Imagine that we have a hash table which holds "name"-"job title" key-value pairs. This hash table needs a hash function to transform the "name" into an index.
  - This could use the algorithm:
    - Convert the key to a string
    - Convert the string to a numeric value by grabbing its length
    - Calculate the length of the string modulo the length of the internal array
    - Use this result as the index
```python
  def hash_code(key):
  return len(str(key)) % len(hash_array)
```
 - **Why use modulo?**
   - Arrays have fixed size, reading/writing beyond = IndexError. 
   - Using `len(str(key)) % len(hash_array)` will always result in an index between 0 and the length of the array, meaning it will always be a valid index!'
  
## Collisions
- At some point, any hash function will result in some keys being mapped to the same index. When this occurs, it is called a collision.
-  Collisions = predicated by the **Pigeon Hole Principl**
   -  n + 1 items into n positions, we will be unable to put each item into a unique positions. 
- Example:
  - Using same hash function. The hash table's internal hash_array has a length of 15.
  - "Kirk" and "Nora" would both get the index of 4. If we insert Nora first, then kirk, it will attempt to add kirk even tho Nora was there first. 
  - To resolve:  make each element of the hash array a collection itself, and then store new elements in the collection rather than directly in the hash array.
  - **Effective Hash Functions:**
  - What would happen if we inserted 600 items, and our hash function happened to calculate the same hash value for all 600 of them? If the hash function does not adequately spread values out over the length of the array, we'll have long chains of key-value pairs and a O(n) worst case runtime to find items.
  - Effective hash functions attempt to spread all possible values over the entire data structure to avoid assigning multiple keys to the same index.

Example code:
```Python
class HashTable:
    def __init__():
        self.internal_array = list(100)
        self.internal_size = 100
        self.size = 0
    
    def hash_function(self,key):
        return len(str(key))
    
    def add(self, key, val):
        index = self.hash_function(key)
        index = index % self.internal_size

        if self.internal_array.get(index) is None:
            self.internal_array[index] = [key, val]
        elif self.internal_array.get(index)[0] != key:
            #Resolve the Collision in whatever way
    
```

# Using Hash Functions
Overall, here are some general strategies to consider when using a hash table to solve a problem:

1. Are there any pieces of data that we need to tie together, such as counting the frequency of some value, or attaching a description to some name?
2. Could we turn those into key-value pairs?
3. For those key-value pairs, what keys and values would help us find the answer?
4. For those key-value pairs, what is the initial state of the key-value pairs?

## Python Dicts = Hash Tables
We can practice using hash tables to solve problems by thinking about how to use a Python dictionary.

Python dictionaries can be used in many ways:
- Creating a frequency map that counts how frequently...
  - A character occurs in a string
  - A word occurs in a list
  - A value occurs in a collection

**Example: Missing Elems in a Range**
Write a function named `get_missing_numbers_in_range`. This function takes in an array of distinct integers, an integer low which is the lowest (inclusive) number in a range, and an integer high which is the highest (exclusive) number in a range.

This function returns a list of all numbers that are between low (inclusive) and high (exclusive) and are not in array.

The missing elements should be returned in order they appeared in the original list.

Are there any pieces of data that we can tie together here to create key-value pairs? Consider:
- A value and the number of occurrences of that value
- A value and True or False to associate with that value
- What keys and values would help us find the answer?
- What is the initial state of the key-value pairs?

Therefore, we have the following pieces of data we could keep track of:
- Each number in the input array
- Each number within the range of low and high
- Whether each number in array is within the range of low and high
- Whether each number within the range is accounted for in array

We are looking for numbers where their presence in the range is False.

Pseudocode:
- Create a hash table (using a dictionary) that maps a number in an array to True, to show that it is present
- Create an empty list to hold all missing numbers
- For each number in the range between low and high, check the value in the map:
  - If the number exists as a key in the dictionary, then the number is present
  - If the number does not exist as a key in the dictionary, then the number is missing
    - Append it to our list that holds all missing numbers

**For loop way:**
```python
# Time complexity of O(n*m)
def get_missing_numbers_in_range(numbers, low, high):
    # This function returns a list of all numbers that are between low (inclusive) 
    # and high (exclusive) and are not in array.

    missing_numbers = []
    for num in range(low,high): # goes n times
        if not num in numbers: # goes n times
            missing_numbers.append(num)

    return missing_numbers

array = [10, 12, 11, 15]
get_missing_numbers_in_range(array, 10, 15)
```

**Hash table way:**
```python
# Time complexity = O(n + m)
# Space Complexity = O(n)
def get_missing_numbers_in_range(numbers, low, hi):
    missing_nums = []

    # list comprehension way:
    # numbers_found = {i : True for i in numbers}

    # non-list comprehension way
    numbers_found = {}
    # n times where n = len of numbers
    for num in numbers: 
        numbers_found[num] = True
    #  compare nums in range to keys
    #  m times where m is high - low
    for num in range(low,hi):
        # O(1)
        if not numbers_found.get(num): #gives none if not found
            missing_nums.append(num)
    return (missing_nums)
```

**Example: Find all symmetric pairs**
Two pairs [a, b] and [c, d] are said to be symmetric if a is equal to d and b is equal to c. For example, [10, 20] and [20, 10] are symmetric.

Write a function named get_symmetric_pairs. This function takes in a list (pairs) of lists. Each sub-list is a list of two elements.

This function should return a list of all symmetric pairs. A pair should only be listed once (without its symmetric counterpart). So for the example above, the result would include [10, 20] (the first pair), but not [20, 10] (the symmetric pair).

Are there any pieces of data that we can tie together here to create key-value pairs? Consider:
- A list and the number of times a word occurs in that list
- A string and a second string or integer value associated with it
- What keys and values would help us find the answer?
- What is the initial state of the key-value pairs?

Consider the following possible pieces of data to keep track of in a hash table:
- The first item in the pair and the second item in the pair
- The first item in the pair and the number of times it occurs in any sub-list


Pseudocode
Our solution will take this approach:
- Create a hash table that maps every pair's first item to its second item
- Create an empty list to hold all symmetric pairs
- Iterate over the pair list again to ensure we process pairs in order:
  - Check the hash table if the symmetric pair exists:
    - Take the current second item, and use it as a key in the hash table
  - Look up the value of the current second item in the hash table, and check whether its value is equal to the current key (current first item)
    - If it's equal, then there's a symmetric pair!
      - Append it to our list of symmetric pairs
  - Remove the current pair from the hash table so that it can't be matched by the symmetric pair when we reach it in the list.

```python

def get_symmetric_pairs(pairs):
    pairs_dict = {}
    symmetric_pairs = []
    # build dict
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        # first value = unique, so save as key.
        pairs_dict[first] = second

    for pair in pairs:
        first = pair[0]
        print(f"first is {first}")
        second = pair[1]
        print(f"second is {second}")
        # gets the key from the dict. 
        print(pairs_dict.get(second))
        if pairs_dict.get(second) == first:
            symmetric_pairs.append([first,second])
            pairs_dict[first] = None
            pairs_dict [second] = None
        print(pairs_dict)

    return symmetric_pairs

    pass

answer = get_symmetric_pairs([[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]])
print(answer == [[30, 40], [5, 10]])

```


Reshape matrix problem w/hash table:
```python
def reshape_matrix(matrix, r, c):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows * num_cols != r * c:
        return matrix

    new_matrix = []
    scalar_index = 0
    
    for current_row in range(r):
        current_row = []
        for current_col in range(c):
          # below is good algo for finding info in a grid.
            row = scalar_index  // num_cols
            col = scalar_index  % num_cols
            current_row.append(matrix[row][col])
            scalar_index += 1
        new_matrix.append(current_row)

    return new_matrix


original_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]

print(reshape_matrix(original_matrix, 3, 4))


original_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12],
  [13, 14, 15]
]

print(reshape_matrix(original_matrix, 3, 5))
```
