# Learning another lang


**Function Expressions**
The name "function expression" refers to using the function keyword in an expression to create a new function reference. We often store the reference in a const variable for later use.
```javascript
const increaseQuantity = function(initial_qty) {
    return initial_qty + 1;
}
```

**Function Declarations**
To define increaseQuantity as a function declaration, we leave off the variable assignment part and place the desired name after function, rather than making a separate variable. (Note that even in function expressions, an optional name can be supplied.)

```javascript
function increaseQuantity(initial_qty) {
    return initial_qty + 1;
}
```

**Expressions are preferred**
- Proactively guard against bugs with scope and hoisting, topics not covered in this curriculum
- Set up patterns and habits needed for future, more advanced JavaScript syntax

**Arrays (Lists)**
In JavaScript, an ordered collection of values (elements) is called an array.
`const myPlants = ['Succulent #1', 'Succulent #2', 'Succulent #3'];`


**Falsy Values**
- false
- 0
- ''
- null
- NaN
- undefined

**String Interpolation**
String interpolation must be done inside a string surrounded by backticks (`) (the character typically above the left tab key on the keyboard.) The expression to interpolate goes inside ${ }.
``Access Denied: ${user.name} not authorized.``

# Functions
Arrow functions are especially useful for making anonymous functions, discussed outside this topic.

**Regular function**
```javascript
const sayHello = function() {
  return 'hey there.';
};

console.log(sayHello());
```

**Arrow syntax:**
```javascript
const sayHello = () => {
    return 'hey there.';
}
console.log(sayHello());
```
When an arrow function is responsible for returning something and has a function body thats one line longt, it can be reduced:

```javascript
const sayHello = () => 'hey there.';
```
When we have an arrow function that **takes in one and only one parameter, the parentheses around the single parameter are optional.**

```javascript
const squareNum = number => {
  return number * number;
};
console.log(squareNum(3)); // 9
```
which can be further reduced to:
`const squareNum = number => number * number;`

**One-Line Arrow Functions Returning Objects**
`const makePerson = (id, name) => { id: id, name: name };  // does NOT work!`

Instead wrap the {} in ():
`const makePerson = (id, name) => ({ id: id, name: name });`

## Callback Functions
- function can take in a reference to a function as an argument, and then call that function.
- A callback function is a term for a function that is passed into another function.

```javascript
const calculate = function(a, b, operation){
    return operation(a,b)
}
```
operation would be associated with a function that adds,subtracts,multiplies,etc. and takes in two numbers. 

## Anonymous Functions
Anonymous functions are a useful way to define functions right at the moment they're used. This usage can both be more readable and more convenient.
- has no name: `console.log("The name of this anonymous function is blank!:", (() => 0).name);`
  - Our anonymous function is () => 0. It's defined inside the console.log() statement, which is the only place that this function is used.
- useful to create a certain kind of for-each loop.

```javascript
const myArray = ['red', 'yellow', 'blue'];

myArray.forEach(item => {
  console.log('Inside this anonymous function, each item of myArray will be accessed as item:', item);
});
```
- forEach should only be used when we know that we need to apply the supplied function operations to every item in the array.

Example:
```javascript
const cashTips = [4, 7, 9, 12, 3, 18, 6];
let sum = 0;

cashTips.forEach((tip) => {
  sum += tip;
});

const average = sum / cashTips.length;
console.log(`The average cash tip is ${average}`);
```
 - we call cashTips.forEach(). 
 - The forEach function takes in one argument: another function which is anonymous!
   - tip => { sum += tip;}

Why use an anonymous function here?
- The logic of this function isn't reused anywhere
- The function is more readable in the context of the forEach loop than outside it


## Uses for anonymous functions: map

The responsibility of map is to loop through an array, and create another array whose items are transformed, or mapped, from the original array.

```javascript
const userIds = ['401', '403', '404', '500', '518'];

const parsedUserIds = userIds.map(userId => {
  return parseInt(userId);
});

console.log(parsedUserIds);
```
- map takes in a function. Here is an anonymous arrow function with one parameter, userId. userId will refer to each item in userIds as map goes through it.
- Unlike the forEach loop, this function must return the value that we want in our new array.
- the above converts the strings into ints. 

**forEach vs. map**
The forEach function is useful when we want to execute an identical action for each item. map is useful when we want a result array that is the same length as the original array, and each item in the result array is based on the parallel item (the item in the same position) in the original array.

## Uses for anonymous functions: reduce
The responsibility of reduce is to look through an array and apply some operation to eventually reduce the array into one value.

Revisit:
```javascript
const cashTips = [4, 7, 9, 12, 3, 18, 6];
let sum = 0;

cashTips.forEach((tip) => {
  sum += tip;
});
```
Essentially, we're reducing our cashTips array into one value. This is a great chance to refactor!

The reduce function takes in a function (and an optional starting value). This function takes in two arguments:
- An argument to represent the accumulated value. This will let us avoid updating the sum variable each time through our loop.
- One item from our array.

```javascript
const cashTips = [4, 7, 9, 12, 3, 18, 6];

const sum = cashTips.reduce((total, tip) => {
  return total + tip;
});
```
- 	The first parameter for this function, total, will hold the running value that carries over between the iterated tips.


```javascript
// way one
const isOdd = (num) => {
    if (num % 2 === 0){
        return 0;
    }
    else {
        return 1;
    }
}
// way two
const isOdd = num => {
    return num % 2;
};

// way three
const isOdd = num => num % 2;
```

```javascript
const doubleTheNums = arr => {
  for(let i=0; i<arr.length; i++) {
    arr[i] *= 2;
  }
  return arr;
}
```