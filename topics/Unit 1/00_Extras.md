# Extra

Things that I've needed to learn about outside of class.

## List Comprehensions
### How to create lists?

**For Loops:**
```python
>>> squares = []
>>> for i in range(10):
...     squares.append(i * i)
>>> squares
```

**map() Objects**
`map(function, iterable, ...)`:Returns an iterator that applies function to every item of iterable, yielding the results.

```python
>>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(txn):
...     return txn * (1 + TAX_RATE)
>>> final_prices = map(get_price_with_tax, txns)
>>> list(final_prices)
```
You may convert the map object into a list w/`list()`

**List Comprehensions**

Example:
```python
>>> squares = [i * i for i in range(10)]
>>> squares
```
Doing the above bypasses makkng an empty list. Here's the format:
`new_list = [expression for member in iterable]`

Every list comp has:
1. expression = member itself, a call to a method, or any other valid expression that returns a value.
2. member = obj or val in list. 
3. iterable = is a list, set, sequence, generator, or any other object that can return its elements one at a time.

Can be used to replace `map()`:
```python
>>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(txn):
...     return txn * (1 + TAX_RATE)
>>> final_prices = [get_price_with_tax(i) for i in txns]
>>> final_prices
```

The soluton above would return a list. 

**Utilizing Conditonal Logic**
`new_list = [expression for member in iterable (if conditional)]`

This logic in action:
```python
>>> vowels = [i for i in sentence if i in 'aeiou']
>>> vowels
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']
```

if you want to change a member value instead of filtering it out
`new_list = [expression (if conditional) for member in iterable]`

```python
>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> prices = [i if i > 0 else 0 for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]
```

Here, your expression i contains a conditional statement, if i > 0 else 0. This tells Python to output the value of i if the number is positive, but to change i to 0 if the number is negative.

**Set/Dict Comprehensions**
Set comprehensions make sure the output contains no duplicates and stores output in no particular order.
```python
>>> quote = "life, uh, finds a way"
>>> unique_vowels = {i for i in quote if i in 'aeiou'}
>>> unique_vowels
{'a', 'e', 'u', 'i'}
```
Dictionary comprehensions are similar: 
`{key: value for (key, value) in iterable}`

Ecample:
```python
>>> squares = {i: i * i for i in range(10)}
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

