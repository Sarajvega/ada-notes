# Intro to debugging
Errors = 3 types
- **A syntax error** is something caught by the compiler/interpreter and it's incorrect use of the language itself. For example, for:, which is invalid Python.
- **A runtime error** is a problem that cannot be detected before the code runs but causes an issue that is caught during the program run. An example would be x = open("nosuchfile.txt") because the file is checked for existence only at runtime.
- **A logic error** is something that isn't caught, either at compile or runtime but which causes an issue. An example would be working out the sum of all numbers from one to n inclusive with the_sum = sum([x for x in range(n)] - that wouldn't include the n in the sum.

## Stacktrace
- A report of the active stack frames at a certain point of execution of program

## Debugging 
What is happening? What did we expect to happen? What actually happened?
Why is this happening? What line(s) of code are making this happen?
How do we fix it? What do we need to change, add, or delete about our existing code?
