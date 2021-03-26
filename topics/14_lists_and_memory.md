
# Lists and Memory

# Lists and Memory
### Vocab
1. List - ordered list of vals. Items called elements. Also called an array.
2. Memory - info stored and the medium om which its stored for immediate use. Also called RAM.
3. Reference - Value which enables program to directly access a datum.
4. Contiguous - things directly next to one another. 

## Memory
Storing something in a var uses memory. Info is quick to retrieve and temporary. Can see memory address using the `id` function.

## Vars and Refs
Python connets w the OS and allocates a block of memory to a variable. Then that var is given a reference. If we assign another variable to that value, the new variable uses the same reference and refers to the same value in memory. 
```python
 >>> sales_tax = 0.09
>>> fees = sales_tax
>>> id(sales_tax)
4304253904
>>> id(fees)
4304253904 
```
A List's var contains a reference to an object which contains metadata and an array of refs where each element in list refers to a different object in memory. 
A list variable acts as a link to an addressbook. 

## Indexing
`reference_address = start_of_items_collection + size_of_reference * index_number`
If the items collected started at the memory address 100 and each ref is 8 units in size and we find to find the item at index 3...`reference_address = 100 + 8 * 3`.

# Lists as References
### Vocabs
1. Side effect: lasting effect that occurs in a function, which isn't thru the return val.
2. Mutable data type: Type of var which can be modified without changing the ref.

## Lists as Args and Side-Effects
Ints and float vars don't have side-effects.
`+=` changes the ref to a new location in memory for ints (immutable), but for lists(mutable), it doesn't change the container reference, just the sub reference for that specific val. 

## Problems with Side Effects
avoid side effect by creating copies of mutable data types and performing operations on the copies. 
```python
def shorten_names(names):
    shortened_names = []
    for name in names:
        # truncate the strings to 0-5 characters
        shortened_names.append(name[0:5])

    return shortened_names
```
# Lists and Big O
## Time Complexity
Size of inpyt list becomes n used to describe the functions time complexity.

Whats the following funcs time complexity?
```python
def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers
```

O(n^2): 2 for loops that loop n times. 

## Space Complexity
Lists can store an aribitrary amount of data.

Space cpmplexity is not a measure of input size bur rather how memory usage increases with larger input. 

With space complexity, look for: new data structures like dictionaries being created and repeated elemints being added to input data. 

## Python Built-In Functions
- .clear() = removes all elems from a list
- .count() = returns num of elems with a specific val
- .index() = returns the index of the first elem to match the given arg
- .copy() = function makes a copy of the given list. `duplicate = soda.copy()`


### Questions
1. Whats printed by this code:
```python
def mystery(numbers):
    index = 0
    while index < len(numbers):
        numbers[index] *= 2
        index += 1

    return numbers

nums = [1, 2, 3, 4, 5]
mystery(nums)

print(nums[3])
```

Answer: 8

2. What is the time complexity of:
```python
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = int((low + high)/2)
        if numbers[mid] > value:
            high = mid - 1
        elif numbers[mid] < value:
            low = mid + 1
        else:
            return mid


    if numbers[low] == value:
        return low

    return None
```

Answ: O(log n) 

The loop will check the middle of the list and it will either return the item, if found, or change high or low, skipping the half of the list which cannot contain the element. So with each iteration the loop bypasses 1/2 of the remaining elements.

If the list was 16 elements long, we would be searching 16 elements, then 8, then 4, then 2, then 1 and we either find the element or return None.

This algorithm is known as binary search and you can read more about the algorithm by following the link.