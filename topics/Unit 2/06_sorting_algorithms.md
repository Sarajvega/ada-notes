# Sorting Algorithms

## Vocab
- In-Place Sorting: Sorting an array using only a small, constant amount of extra sotrage space (O(1)). 
  - Modifies the array to be sorted directly rather than making a new array.
- Stable: guarantees that the relative ordering of two values having the same sort key is the same after the sort as it was before the sort.

## In-Place and Stable Sorting
### In-Place
- In-Place uses the array itself for worksapce. It takes more time and ends up modifying the initial list. 
- We may need to copy the list first to avoid over writing it. 

### Stable
- Maintains realtive order of items after sorting.
- Useful for collection of records on multiple attributes
- Ex: sort a list of people by ages, and two have same age, by their name:
  - `Jean (25), Vickie (39), Karla (33), Patricia (25), Becky (39)` 
  - Then sort by name: `Becky (39), Jean (25), Karla (33), Patricia (25), Vickie (39)`
  - Then sort by age: `Jean (25), Patricia (25), Karla (33), Becky (39), Vickie (39)`
- Order of the names with identical ages is preserved between the second and third lists.

## O(n^2) Algorithms
- ex: bubble sort, selection sort, and insertion sort.
- when the array length n is small, but quickly cease to be useful as the size of the array increases. 

## Bubble Sort
Bubble sort works by repeatedly:
- Stepping through the list to be sorted
- Comparing each pair of adjacent items, and
- Swapping the adjacent items if they are in the wrong order
So the largest element gets bubbled to the top of the array after each iteration through the outer loop.

To optimize:
- We can consider the length of the unsorted list to shorten by one with each pass. After each pass, one more item is guaranteed to be in the proper order at the end of the list.
- If we track the unsorted list length, we never have to perform the final bubble pass (when the unsorted list has one item). There is nothing else left unsorted with which to swap that item!

## Big O Complexity
When analyzing sorting algorithms, consider:
- num of comparisons
- num of swaps

Big O assunes worst case scenario.

Bubble sort could finish in one pass, but not likely.
- We have two loops
  - Out loop = total num of passes = runs n times.
    - more accurately n-1 times
  - Inner loop = comparisons and swaps = runs n times.
    - more accurately n-2 times.

Therefore bubble sort has a time complexity of O(n^2).

## Stability
- Bubble sort = stable.
  - Shift vals by one position, never jump over one another. 
  - if we had two 10's, the leftmost 10 would stay on the left.

Consider the following:
```python
def bubble_sort(array):
    i = 0
    # Begin the outer loop
    while i < len(array) - 1:
        j = 0
        # Begin the inner loop
        while j < (len(array) - i - 1):
            # Compare two adjacent items
            if array[j] > array[j+1]:
                # Swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
            j += 1
        i += 1
```
- Create an outer loop that loops while i is smaller than the length of the array - 1 since we don't need to bubble the final value.
  - j = 0
  - Create an inner loop that loops while j is smaller than len(array) - i - 1 since we want to avoid the i sorted elements at the end, and we need to leave one extra value for the pairwise comparisons.
  - Compare the items at index j and j+1. If they're out of order:
    - Swap the items at array[j] and array[j+1] using a temporary variable, temp
  - increment j
  - repreat until j reaches its limit
  - increment i
- repeat until i reaches its limit. 

Note: Because the original array is modified, no return statement is needed!

Summary: 
Bubble sort is a stable sorting algorithm that compares two items next to one another and swaps them if the one proceeding the first is smaller. This algorithm is unique because it contains two loops and is stable, so if we have two of the same number, the left most remains on the left. It's time complexity is O(n^2) because of its two loops and its space complexity is 1 because only a single additional memory space is required i.e. for temp variable. 

## Selection Sort
- selects the smallest unsorted item in the list, and swapping it with index 0, then finding the next smallest and swapping it into index 1, and so on.

## Big O Complexity
- O(n^2)
- Our outer loop runs about n times. The first pass through, we must perform n-1 comparisons to find the minimum value, and then perform a single swap for that value.
- Why slightly better than bubble sort?
  - bubble sort would perform both n-1 comparisons, as well as n-1 swaps.
  - This does not affect our overall complexity analysis since the inner loop does still run n-1 times.

## Stability
- Not stable
- Swaps performed can result in equivalent vals jumping over one another. 
  - Loses info about relative initial orderings.

```python
def selection_sort(array):
    i = 0
    while i < len(array) - 1:
        min_index = i
        j = i + 1
        while j < len(array):
            if array[j] < array[min_index]:
                min_index = j
            j += 1
        if min_index != i:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp
        i += 1
```
- Create an outer loop that loops while i is smaller than the length of the array - 1 since we don't need to swap the final value
  - Start with the assumption that the minimum value is already in the right place by setting min_index to i
  - Start a variable j at the position one past i to look for the smallest element in the rest of the array
  - Create an inner loop that loops j over the remainder of the array
    - If the current inspected value is smaller than the current smallest value, update min_index with the current index j
  - Repeat until j reaches the end of the list
  - If i and min_index are not the same, then swap the elements at index i and index min_index using a temporary variable temp
  - incr i
- Repeat until i = end of list. 

Summary:
Selection sort finds the smallest item then places it at the head of the array, then finds the second smallest, and so on. Its time complexity is O(n^2) as its contains two loops and its space complexity is 1, as there is one temporary variable used.. It is more efficient than bubble sort as it performs a smaller number of swaps.

## Insertion Sort
Insertion sort works with two list structures:
- The unsorted source list
- A list into which sorted items are inserted

To save memory, most insertion sort implementations use an in-place sort that works by treating a portion of the existing list as sorted (often the beginning) and moving each item in the unsorted portion to its proper location in the sorted portion.

Explanation: 
- Treat the first item as a list of length one, which is sorted by definition.
- Consider each item in the unsorted portion of the list.
- Step backwards through the sorted list, swapping the new item, until we find a value less than the current item. This item is now in its proper location (for the time being).
- Continue with the next unsorted item, swapping it forward into the sorted portion until we find its proper location.
- Continue with the remainder of the unsorted list, until the entire list has become sorted.

## Big O Complexity
- O(n^2)
  - The insertion sort algorithm requires (in the worst case):
  - 0 comparisons to insert the first element
  - 1 comparison to insert the second element
  - 2 comparisons to insert the third element
  - ... and so on
- n-1 comparisons to insert the last element

insertion sort, like bubble sort, has a best case time complexity of O(n) if the list is already sorted. 

Insertion sort generally improves in complexity the closer the list is to being sorted, that is, the more items are already relatively in their correct places. In other words, insertion sort runs in nearly linear time on a nearly sorted list of elements.

## Stability 
- Stable: we only move items in the list using adjacent swaps, and then only when they are strictly out of order.

```python
def insertion_sort(array):
    i = 1
    while i < len(array):
        to_insert = array[i]
        j = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while j > 0 and array[j-1] > to_insert:
            array[j] = array[j-1]
            j -= 1
        array[j] = to_insert
        i += 1
```

- Loop through the entire list with i representing the first position of the unsorted sub-array
- Store the first element of the unsorted list in a temporary variable called to_insert
- Find the correct index to insert the value to_insert
- Loop through the sorted list from back to front
- Compare the values between the item at the position we're inspecting, and to_insert
- Swap if needed
- Increase the outer index i so that the sorted list grows, and the unsorted list shrinks

Note: This implementation sorts the array in-place. Because the original array is modified, no return statement is needed.

Tracks unsorted and unsorted. Index 0 = sorted. Next index is compared, if less than goes before index 0 val. Know index 0 and index 1 are sorted. 

## Merge Sort
- Divide-and-Conquer-Algorithm: A strategy of solving a big problem by breaking it into smaller, more manageable subproblems. It can also lead to recursive solutions.
- Recursive Algorithm: A method of solving a problem where the solution depends on solving smaller instances of the same problem. This approach can be applied to many types of problems.
- Utilize binary search in a sorted array.
  - Cuts array in half.
  - Check val in middle. 
  - Then compare to val in middle of other half.
  - do again and again.

Merge sort is a divide-and-conquer algorithm. It involves the following three stages:
1. Divide the array into two sub-arrays repeatedly until each sub-array is of size one.
2. Sort each sub-array. (An array of size one is sorted by default.)
3. Merge the sub-arrays into one array by combining two sub-arrays into one at each step.

Dividing:
- In the first divide step, the original array of size eight gets divided into two sub-arrays of size four each. The arrays are divided at a calculated halfway point.
- In the next divide step, we have two sub-arrays. Both of these arrays have four elements. They aren't of size one yet! So, the same action gets repeated. We calculate the halfway point, and divide the sub-arrays in half.
- This divide stage continues until the original array of size n is reduced to sub-arrays of size 1 each.

Sort and Merge:
- The merge stage starts by combining two sub-arrays at a time.
- How does the merge sort algorithm merge and sort two sub-arrays into one? The algorithm compares an item from each sub-array, and uses a third, temporary, auxiliary array.
- This is the process of sorting and merging at the same time, which repeats until there are no more-sub arrays and the original array is completely sorted.
- Finally, the auxiliary array gets linearly copied back to the original array.

## Stability
- Merge sort is a stable sorting algorithm, though we have to be a little careful to ensure this.
  - for a sorting algorithm to be stable, the sorted array must preserve the relative ordering between equivalent values that existed in the unsorted array. 
  - To ensure this, we need to guarantee that if there are two items with the same value, that the instance that started on the left, stays on the left.
  - For the stable O(n2) algorithms, we did this bys ensuring that we never swapped "through" an equivalent value. But with all our dividing and merging, how can we ensure this remains true in merge sort?
  - when we divide a sub-array, there is always a left side and a right side.
  - Anything that goes into the left array will originally have preceded anything in the right array. This is true all the way down during the divide phase. So if we encounter two equivalent values during the merge phase, one from the left and one from the right, we need only prefer the value from the left. As long as we do this all the way up through the merging, we will preserve the relative ordering required for a stable sort.

## Big O Complexity
- O(n log n)

How?

Divid Step:
- Each divide finds the midpoitn from start adn end. 
- This step takes constant time regardelss of subarray size. 
- Total divides = n-1.
- Contributes n-1, a linear term, which we can ignore.

Merge step:
- mergin n elements takes O(n) time.
- If there are two sub-arrays of size n/2 each, then we compare one element from subarray with another from the second, and one of the two is copied. 
- This continues until all are copied, tkaing O(n) time. 

Count of levels:
- Starting w/n elements and reducing by half at each level until we reach arrays with a single elem, takes log n steps. 
- Similarly, starting with sub-arrays of one element each and combining two sub-arrays at a time until we reach an array of n elements also takes log n steps.

Conclusion:
- each level takes O(n) time. There are O(log n) such levels.
- O(n) merges times O(log n) levels results in an overall time complexity of O(n log n).

Summary:
Merge sort is a divide-and-conqer algorithm, which means it divides arrays into sub arrays to make comparison more manageable. This algorithm is recursive, meaning the ultimate solution depends on the solving of smaller sub problems. It's time complexity is O(n log n) as it divides the list in half again and again to manage small comparisons - O(log n) and each level takes O(n) time. It's space complexity is O(n), since the amount of subarrays depends on the number of items in the array.

### Selection sort vs. Insertion sort
- Selection: Given a list, take the current element and exchange it with the smallest element on the right hand side of the current element.
- Insertion: Given a list, take the current element and insert it at the appropriate position of the list, adjusting the list every time you insert. It is similar to arranging the cards in a Card game.
- Time Complexity of selection sort is always n(n - 1)/2, whereas insertion sort has better time complexity as its worst case complexity is n(n - 1)/2. Generally it will take lesser or equal comparisons then n(n - 1)/2.

## Performance
- how can merge sort have a time complexity of O(n log n) while the simpler insertion sort has a time complexity of O(n2)?
  -  big O is not a measure of absolute performance. It tells us how the performance grows with the size of the input.
  -  This means that for small arrays, insertion sort may absolutely perform better than merge sort. However, as the size of the input grows, merge sort will tend to outperform insertion sort.

## Other O(n log n) sorting algorithms

### Quick sort

### Heap sort

### Recursion