Emails:
adelaidenalley@gmail.com
aeronroemer@protonmail.com

# Fundamentals
## Fundamentals Vocab
- Expression: Unit that is evaluated to one val. 
  - A func call is an expression
  - 9 > 0 evals to true
- Statement: code that executes/performs an action
  - return foo
- Var: Name that refs a specific place in memory
- Literal: Value that is the value itself
- All values have data types:
  - Integer: whole pos,neg or zero
  - Float: not whole
  - String: Text
    - A ", will yield a space when printed.
    - "Age:", age -> Age: 26
  - Boolean
  - None: absence of value
  - List
  - Dict: key pair vals
  - Tuple: ordered, unchangeable collection of items
  - Range: sequence of nums with a start, stop and increment.
  - set/frozenset: unordered collection, use loop to access not index/key
  - bytes/bytearray: collection of binary digits.
You can get data type with `type()`

Casting: converting a value to another data type
- int()
- float()
- str()
- bool()

Printing and Formatting strings
- f string

## Conditionals Vocab
- Boolean: True/False
- Conditional expression: expression evals to truthy/falsy. Used w/ if statement.
- Truthy: Value thats True inside conditional.
  - Most values truthy
- Falsy: Value thats False inside conditional.
  - None, 0, 0.0, "", [], {}, (), set(), range(0), false
- None: Defines a null or no value at all. 

If/Elif/Else statments
- Uses truthy/falsiness.

Boolean Operations
- and/or/not: used in conditional to find truthiness/falsiness of expression
  - False or True evals to true if one is true
  - True and True evals to true if both are true

*And* Truth Table
Left	Right	Result
True	True	True
True	False	False
False	True	False
False	False	False

*or* Truth Table
Left	Right	Result
True	True	True
True	False	True
False	True	True
False	False	False

Not
- Negates an expression. infront of truthy expression, becomes falsy.

Order of operations.
`10 < 2 > True`
First expression is false, second is false, whole thing evals to false. 

## Math Primer
Decimals = base-ten number system
N as a variable
average/mean synonymous
floor of n: biggest int lest than or equal to n
ceiling of n: smallest int greater than or equal to n
2.4 -> floor = 2, ceiling = 3
-2.4 -> floor = -3, ceiling = -2
