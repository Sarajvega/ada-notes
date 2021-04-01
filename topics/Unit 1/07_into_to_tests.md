# Intro to Tests
## Vocab
Package: Collection of python modules
Modules: individual .py files
Version: A state of sftware w/code and dependencies
Release: distrib of new vers

Pkgs = software people can use. provide functionality/design patterns. Need to be managed.
  Make sure versions updated
  make sure teammates have similar installs
PyPi - place where you can get packages
pip is a package that installs packages. 

## automated tests
- automated test: scripts that test specific code for functionality. Tests for correct overall functionality.
- unit test/test case: test the performance of a single function/vert small piece of code.
- Useful: test all possible outcomes from a func, helps w/ scalability, imporves colaboration and refactoring.

## pytest
Assertion - state that something is true. Checks if whatever to right of it is Truthy. 
Tests filename either bigns with test_ or ends with _test.y
tests themselves being w/ `test_` or end with `_test():`
assert = statement that determines a test passing/failing. checks if whats on right is truthy (passes) or falsey (fails). At least one in test.
Test Structure:
- Arrange (at top of test): Creating var/call helper methods, etc. 
- Act (middle): where testing happens. Invoking of function.
- Assert (End) Make assert statments. 

## Expectiong a raised exception
We need to assert than an exception gets raised during a function call.
Errors detected during execution are called exceptions - includes nameErrors, TypeErrors, ZeroDivisionErrors.

