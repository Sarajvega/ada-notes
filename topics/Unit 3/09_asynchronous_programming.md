# Asynchronous Programming
- Asynchronous programming: A method of programming that intentionally executes actions and processes outside of the typical program flow, so that the program doesn't stop and wait for a result.
- Flow of control: The order of execution of programming statements.

To write GOOD asynchronous code, determine:
- What is the asynchronous function we are invoking?
- What do we do after the asynchronous call finishes?
- What do we do if the async call doesn't finish successfully?
- How can we ensure that every other part of the program runs correctly, without bugs, even if the asynchronous call hasn't finished?

To write asynchronous code, we'll need to anticipate four things:
- How do we make an asynchronous call?
- What should happen if the asynchronous call finishes successfully?
- What should happen if the asynchronous call doesn't finish successfully?
- What other pieces of code depend on this asynchronous call?

## General Concepts

**Blocking Code**
When a web app runs in a browser and it executes an intensive chunk of code without returning control to the browser, the browser can appear to be frozen. This is called blocking;

**Thread**
A thread is basically a single process that a program can use to complete tasks. Each thread can only do a single task at once:`Task A --> Task B --> Task C`

Many computers now have multiple cores, so can do multiple things at once.
`Thread 1: Task A --> Task B`
`Thread 2: Task C --> Task D`

**JavaScript is single-threaded**
Even with multiple cores, you could only get it to run tasks on a single thread, called the main thread.

More about asynchronous Javascript: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous

## GET requests with axios
API calls in JavaScript typically execute asynchronously!

axios documentation: https://github.com/axios/axios

Example call:
```javascript
const axios = require('axios');

axios
  .get('some URL')
  .then((response) => {
    // Code that executes with a successful response goes here
  })
  .catch((error) => {
    // Code that executes with an unsuccessful response goes here
  });
```
- We will use the const variable axios to hold the axios library functionality.
- The require function finds the exported objects defined in another module or file, and imports them. In this case, we are importing the exported objects defined in the axios module.
- `.catch()` - This function call, which is chained off of axios.get().then(), determines what happens if the request is unsuccessful and throws an error. This function also expects one argument: a function.

Simple working example:
```javascript
const axios = require('axios');

axios
  .get('https://dog.ceo/api/breeds/list/all')
  .then(() => {
    console.log('success!');
  })
  .catch(() => {
    console.log('error!');
  });
```
- Simply from looking at this code, we can't really tell what kind of object is returned from the call to axios.get(), but we can tell that it must at least have a method called then. Similarly, we can't tell what kind of object is return from the call to axios.get().then(), but we can tell that it must at least have a method called catch.
  - Both objects are of a type called a Promise

**then and catch Accept Anonymous or Named Functions**
Anonymous:
```javascript
axios
  .get('https://dog.ceo/api/breeds/list/all')
  .then((response) => {
    // ...
  })
  .catch((error) => {
    // ...
  });
```

Named:
```javascript
const axios = require('axios');

const printSuccess = (response) => {
  console.log('success!');
};
const printError = (error) => {
  console.log('error!');
};

axios
  .get('https://dog.ceo/api/breeds/list/all')
  .then(printSuccess)
  .catch(printError);
```

**Response and error objects**
Docs: https://github.com/axios/axios#response-schema

Demonstration of shape w/o documentation:
```javascript
const axios = require('axios');

axios
  .get('https://dog.ceo/api/breeds/list/all')
  .then((response) => {
    console.log('The value of response is:', response);

    console.log('The value of status inside of response is:', response.status);

    console.log(
      'The date inside header inside response is:',
      response.headers.date
    );

    console.log('The data given back by the API response is:', response.data);
  })
  .catch((error) => {
    console.log('The value of error is:', error);

    console.log(
      'The value of status inside of response is:',
      error.response.status
    );

    console.log(
      'The data given back by the API response is:',
      error.response.data
    );
  });
```
**Finally**
- axios supports a finally clause, which will run after either the then or catch no matter what.
- The finally clause does not receive any parameters, so we should only use finally for logic that should always run, regardless of the reason for success or failure, such as resetting some application state.

**sending query parameters**
```javascript
const axios = require('axios');

axios
  .get('https://us1.locationiq.com/v1/search.php', {
    params: {
      key: process.env['api_key'],  // discussed below
      q: 'Seattle, Washington, USA',
      format: 'json',
    },
  })
  .then((response) => {
    console.log('success!', response.data);
  })
  .catch((error) => {
    console.log('error!', error.response.data);
  });
```

- JS does not wait for HTTP response to come back, after sending the GET request, the program proceeds.

Research "JavaScript Promises" and "JavaScript async await."

## Managing Asynchronous Calls