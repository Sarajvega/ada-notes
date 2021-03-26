# Raising and Handling Exceptions
Exception: Event/Error that may cause the program to stop if not hangled properly. A DataType which holds data like what specific error occurred and where.
Code that recognizes a thrown exception is often called catching an exception.
Types of exceptions:
- NameError: global/local variable not found
- ZeroDivisonError: 2nd arg of div/modulo is 0
- OverflowError: Arithmetic operation too large to be rep'd.
- SyntaxError: 
- TypeError:Operation/funct applied to an obj of inappropriate type.
  
`raise` allows us to manually raise exceptions.
can pass in a message - `raise ZeroDivisionError('Tried to divide by zero')`

`try:`
   ` any_number_of_python_lines_that_may_raise_an_error()`
`except ExampleError as error_as_a_variable:`
    `print(f"An exception occurred. Here are the error details: {error_as_a_variable}")`

Example:
```python
def calculate_circumference(radius):
    try:
        circumference = 2*3.14*radius
       print(f"Circumference of circle is: {circumference}")
        return circumference
   except TypeError as err:
        print(f"Calculation input has an incorrect data type, {err}.")
```
 `try...except`: Python lets us catch raised exceptions before they crash our program— and then handle them!
-`try`: If any exception is raised by any code executed inside the try-clause, the rest of the try-clause is skipped, and code execution moves to the except clause.
- Try-clause: includes all code that has the poss of raising an exception that we want to handle. 
- `except`: begins except-clause. runs if a matching exception is raised from try clause
- `as` : shows that exception is caught in variable to right of it. 
- body of except clause: code executed if error is raised. 
*Mutliple Exception types with one handler*
try:
    # ...
except (ZeroDivisionError, UnboundLocalError, NameError) as err:
    print(f"Either a ZeroDivisionError, UnboundLocalError, or NameError happened. Details: {err}")

## Exceptions in test
Pytest syntax:
1. What func call and input do we expet to raise the exception?
2. What kind of exception do we expect from this function call?

`def test_exceptional_function():` 
    `with pytest.raises(SomeTypeOfException):` tells pytest we expect exception
       ` exceptional_function(exceptional_argument)` replace w/ func call that will raise the exception.

