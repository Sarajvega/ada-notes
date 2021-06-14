# Tests

- Test Suite: A collection of tests that are typically validating a common feature, or should be run together. One test suite can contain many tests and setup or breakdown steps.
  
## Jest
There are many JavaScript testing frameworks out there. To name a few:
Mocha
Jest --> used w/React
Jasmine
Protractor
Karma
Selenium

# Test Syntax

## describe Blocks
Describe blocks:
- Can contain unit tests (details below), other describe blocks, and helper functions.
- Are optional! A test suite doesn't require a describe block to exist.
```javascript
describe('fizzBuzz', () => {
    // Placeholder Content
});
```
- A describe block begins with the Jest function describe. This function takes in two arguments: a name for this describe block, and a function that contains our unit tests.

## test blocks
```javascript
describe('fizzBuzz', () => {
  test('returns Buzz on multiples of 5', () => {
    expect(fizzBuzz(25)).toEqual('Buzz');
  });
});
```
- test blocks define one distinct test.
- first argument to test is a description string. This string should describe the specific scenario that we're targeting and testing.
- The second argument is a function that ultimately contains the assertion lines.

## expect and Matchers
In order to define the conditions under which a test passes or fails, we combine an expect call and a matcher.
`expect(someReceivedValue).toEqual(someExpectedValue);`

Jest matchers [https://jestjs.io/docs/expect] are methods that describe how our received value relates to our expected value.

**Examples:**
expect(x).toEqual(y);	Compares objects x and y and passes if they are equivalent
expect(x).toBeNull();	Passes if x is null
expect(x).toBeTruthy();	Passes if x evaluates to true
expect(x).toBeFalsy();	Passes if x evaluates to false
expect(x).toContain(y);	Passes if the array or string x contains y
expect(x).toBeDefined();	Passes if x is not undefined
expect(x).toBeLessThan(y);	Passes if x is less than y
expect(x).toBeGreaterThan(y);	Passes if x is greater than y
expect(x).toBe(y);	Compares objects x and y and passes if they are the same object, do not use this to test two objects or arrays for equality.
expect(x).toMatch(pattern);	Compares x to the string or regular expression in pattern and passes if they match
expect(fn).toThrow(e);	Passes if a function, fn, throws exception e when executed

Jest website: https://jestjs.io/
Jest introduction to matchers: https://jestjs.io/docs/using-matchers