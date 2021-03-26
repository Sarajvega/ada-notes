
# Intro to functions
## Vocab
- Function: Lines of code that r named and used.
- Invoking: make lines of code in a func happen.
- Define a func: how a func gets defined before invoked.
- Arg: Data delivered to a func when its invoked. 
- Var declaration: line of code where intro var
- Scope: Area of a program where a given var can be accessed. 
  - IF NOT IN SCOPE = NameError
- local var: var w/ smallest scope
- global: largest scope. accessed and moded outside any func or inside any func. 
  
## Whats a func?
- hold sequential logic, have a name, don't do anything until told to, take in data, return something and are reusable. 
- Single responsibility Principle: a func should have 1 resp. 
- Before using a func, know: purpose, what data goes in, computations in func, data that exits.
- name vs invoke: `len` --> `len()`
- Args are positional: args passed have a specific order
- Will creating a function reduce the repetition in my code?
Is there a chunk of code that gets repeated over and over and over again?
Will creating a function here increase the readability of this code?
Is this chunk of code too complex or specialized, and needs a name?
Will creating a function here better the organization of this code?
Will my code be easier to navigate with this function?
Can this function be reused in the future?
Will future developers also benefit from this function, and not just me?
- Return -> ends a function call
- When we pass a value into a function call, it is an argument.

## var scope
determined by kind and location.
parameters are scoped to its func. 
return vals are important. to gal val out of a func, must use return. 

## Documentation
- API - application programming interface: set of rules/tools that allow software to communicate with other software. 
- function signature:func resp, whats returned. explain parameters, special cases

## Vars are refs
- Object Identity: objs unique identity that never changes once its been created. a #. find w/ id(obj).
- Objects = units of data = Value/Data Type/Identity.
  - 33 is an object with a value 33 and a data type of int
- Gets put into memeory each time an obj is created. 
- Vars = refs to objs in memory. 
  - current is a variable that refers to the object 33 in memory
  - can point to same obj
  - ticket = variable, ticket # = obj ID, car = value, parking space = memory space. 

## Immutable/Mutable
- Mutable = changeable (appending/remove item, add key val)
  - list/dict
  - id won't change w/mod, still points to same place.
    - So there can be mult ref to mutable objects
  - ex: appending/adding key-pair val, add two nums to result in a sum
- Immutable = unchangeable 
  - int/num/float/decimal/string/bools
  - id will change w/mod

## Nested Data Structures
- Lists/dicts = containers, contain mutable/immutable data types

