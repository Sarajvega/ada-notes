
# Python OOP
- Software Design Pattern: Reusable patterns commonly used to solve problems. Usually describes how classes and functions are structured and used. Usually conceptual and language-agnostic.

Common Design Patterns:
- Iterator: A class whose responsibility is to know how to iterate through an object.
- Factory: A class or method whose responsibility is to create instances of some class. If con
- Adaptor: A class whose responsibility is to help two other classes communicate with each other.
- Observer: A class whose responsibility is to watch for changes over many objects, and notify many objects when changes happen.
- Decorator: A class or method whose responsibility is to dynamically alter and extend the behavior of a function or class. Can extend multiple objects without chaning their implementation. 
- Strategy: A class whose responsibility is to represent an algorithm.

When considering a design pattern, the team should consider:
1. Does this make the code more or less maintainable over time?
2. What is the cost of implementing this design pattern?
3. What are the benefits of implementing this design pattern?
4. What are the alternatives?

See https://python-patterns.guide/. 

## Intro to Decorators

See: https://www.python.org/dev/peps/pep-0318/

- Decorator Pattern: A design pattern that dynamically adds behavior to be added to an individual object, as needed
- Wrapper Function: (generic term) A function whose responsibility is to "wrap" another function, or call another function within itself
- Decorator: In Python, a wrapper function applied using decorator syntax
- Wrapped function: In the context of a wrapper function, the function that is being extended

Simple Example:
Ryanne is creating a calculator program. She's made 3 funcs that add, subtract, and multiply numbers.These she will use the decorator syntax to designate the wrapper function and the wrapped function. 
- The decorator (wrapper function) is the function that checks validity, calculates, then prints the results
- The wrapped functions are the calculation functions

Whenever Ryanne's program runs the add, subtract, or multiply functions, their behavior is extended, and automatically always checks validity, calculates, and then prints the result.

## Decorators vs Helper Functions

**How are decorators usefule?**
1. The decorator syntax may be more readable in this situation. It calls attention to itself that something interesting is happening.
2. The decorator syntax can enforce consistency
3. Depending on how often we imagine the decorator logic changing vs. the calculation logic changing, decorators may be easier to use, refactor, update, and maintain, compared to helper functions
4. Static and class methods use decorators
5. Decorators extend the beavior of functions using wrapped funcs...which are like building blocks.


## Synatx
```python
def wrapper_function(wrapped_func):
    def inner():
        # some wrapper logic
        wrapped_func()
        # some wrapper logic
    return inner

@wrapper_function
def wrapped_function():
    pass
```

An medium example:
```python
def display_stars(wrapped_func):
    def inner():
        print("Some stars before we call the wrapped function...")
        print("*************")
        wrapped_func()
        print("Some stars after we call the wrapped function!")
        print("*************")
    return inner

@display_stars
def display_hello_world():
    print("Hello, World!")
```

`display_stars` is the decorator.
`display_hello_world` is a wrapped function. It is decorated with `display_stars` with the line `@display_stars`.

## High Order Functions
We primarily use functions by invoking them, sometimes we use functions as objects.

Whenever a decorated function is invoked, we can imagine that the following steps happen:
1. The decorator is invoked
   1. The argument for this function call is the decorated function
   2. It creates an inner function
2. The decorator returns the inner function
3. The inner function is invoked
   1. The logic for the inner function will eventually call the original decorated function

```python
import random

def display_stars(wrapped_func):
    def inner():
        print("Some stars before we call the wrapped function...")
        print("*************")
        wrapped_func()
        print("Some stars after we call the wrapped function!")
        print("*************")
        print("")
    return inner

@display_stars
def display_hello_world():
    print("Hello, World!")

@display_stars
def display_english_alphabet():
    print("abcdefghijklmnopqrstuvwxyz")

@display_stars
def add_two_random_numbers():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    sum = a + b
    print(f"{a} + {b} = {sum}")
    return sum
```

`display_stars` is our decorator function and it wraps:
- display_hello_world
- display_english_alphabet
- add_two_random_numbers



## Static Methods and Class Methods
- Instance Variable: Also called attributes. stored on a `self` instance.
- Class Variables: defined in the class def outside of any instance method. Accessed w/ dot notation of the class: `ExampleClass.example_class_var`. Holds state. 
- Static Method: A method that does not depend on an instance, and does not access instance or class variables. Essentially a regular function that happens to be stored in a class primarily for namespace purposes. Called using the class name. 
- Class Method: A method that receives a reference to the class itself. This method does not depend on an instance, and cannot access instance variables or methods. Called using class name `Cookie.get_own_temp()`.

![Image demonstrating difference between static and class methods](topics/imgs/static_vs_class_methods.png "Static vs Class")

## Static Methods
- Methods that are typically called from a class, not an instance.
- They can't access attributes/instance vars or class vars.
- They can provide helper functions.
- Don't automatically get self even if we try adding a parameter to receive it.
- Often utility functions that do things not associated w/an instance.

**Syntax:**
```python
class ExampleClass:

    @staticmethod
    def example_method():
        print("I'm inside the static method, example_method!")
```
^^ Notice self is NOT a param. 

To invoke:
`ExampleClass.example_method()`

## Class Methods
- Called from a class, not an instance.
- can access/modify class state 
- have access to class variables.
- Do not have access to instance variables.
- requires cls as first arg 
- can call class methods from an object instance
  -  However, the @classmethod decorator will specify that the first parameter, cls, will always have the value of the class itself.
- Good for mod'ing class state the applies across all instances of the class, doing operations that aren't assoc. w/an instance, doing operations that rely on the class itself. 

**Syntax:**
```python
class ExampleClass:

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("In a class method, cls will be the class itself", cls)
```
^^ Note self is NOT a param. cls is passed as a param, which represents the class itself. 

To invoke:
`ExampleClass.example_method()`

class methods can access any class variables that are defined, using the cls variable:
```python
class ExampleClass:
    example_class_var = "This is an example class variable!"

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("I can access class variables using the cls parameter:", cls.example_class_var)
```

class variables can be accessed without the cls parameter, as long as there's access to the class itself.
```python
class ExampleClass:
    example_class_var = "This is an example class variable!"

    @classmethod
    def example_method(cls):
        print("I'm inside the class method, example_method!")
        print("I can access class variables using the cls parameter:", ExampleClass.example_class_var)
```
cls will always represent the current class itself; specifying ExampleClass could have consequences if class definitions change, or when inheritance is involved.