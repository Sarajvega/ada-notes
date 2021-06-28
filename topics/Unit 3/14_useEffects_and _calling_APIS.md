# UseEffect After Render

During the first time that an instance of a component appears, the component initializes state (if it has any). After that, every time that component's state updates, the component re-renders.

Rhere are certain situations where this feature causes problems. Here are some examples:
1. A Timer component that is responsible for starting and keeping an uninterrupted ten-minute timer, even if the appearance of the timer changes. We don't want to restart the timer any time the visual appearance of the Timer updates.
2. A RestaurantList component that gets a list of restaurants from the Yelp API once. We don't want to retrieve the data again simply because the user marks a restaurant as a "favorite."
3. A VideoPlayer component that loads a large movie file from an API once. We don't want to start downloading the movie again simply because the volume bar is adjusted.

## The Component Lifecycle
Under-the-hood, the React library manages components through a process called the component lifecycle  . The component lifecycle is the name of the three stages that each React component goes through:
- Mounting: Occurs when an instance of a component is being created and inserted into the DOM.
- Updating:Occurs when a component is being re-rendered.
- Unmounting:Occurs when a component is being removed from the DOM.

During each stage, each component calls a set of different and unique functions that are defined under-the-hood. When using React with hooks, these functions are hidden from view, and instead we tie into these events by using other hooks!

**During the mounting stage**, a component will calls these functions, in this exact order (starred functions are not depicted in the simplified chart):
1. constructor()
2. getDerivedStateFromProps()*
3. render()
4. componentDidMount()

**During the updating stage**, components call this different set of functions in this order (starred functions are not depicted in the simplified chart):
1. getDerivedStateFromProps()*
2. shouldComponentUpdate()*
3. render()
4. getSnapshotBeforeUpdate()*
5. componentDidUpdate()

During the unmounting stage, components call this function:
1. componentWillUnmount()

The most important functions to be aware of are:
1. componentDidMount()
2. componentDidUpdate()
3. componentWillUnmount()

We can visit this official interactive diagram showing the [lifecycle methods](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/) as a starting place for more research.

## useEffect Executes After Render
Different React [hooks](https://reactjs.org/docs/hooks-intro.html)  allow us to "hook" into specific parts of the lifecycle.

useEffect is called after a component renders.

The useEffect hook  is a hook function that runs during these lifecycle steps:
- componentDidMount
- componentDidUpdate
- componentWillUnmount

This means that the useEffect hooks runs:
- once in the Mounting stage, after the component is successfully inserted into the DOM and fully renders
- once in the Update stage, after the component fully updates and re-renders
- once in the Unmounting stage, right before the component is removed from the DOM

To use the useEffect hook, we call the useEffect function with two parameters:
1. A function that describes what to do after the component fully renders during componentDidMount and componentDidUpdate.
2. A "dependency" array. This array contains references to any props or state to watch. Whenever any watched props or state update, useEffect will run as part of componentDidUpdate.
   1. If we don't define this array, useEffect will be called during every componentDidUpdate. That is, every time the component re-renders.
   2. This array can be empty [] to indicate we are not watching for any updates.
      1. So function will be called once when DOM is loaded only.

**Syntax: Executing useEffect After Specific Values Change**

First, each file that uses useEffect should import it:
`import { useEffect } from "react";`

```javascript
import { useState, useEffect } from 'react';

function App() {

  const [pieceOfState, setPieceOfState] = useState(0);

  useEffect(() => {
    console.log('I\'m in useEffect!');
    console.log('This will be called whenever an instance of this component mounts');
    console.log('or whenever pieceOfState is updated');
  }, [pieceOfState]);

  return (
    <div>
      <button onClick={() => setPieceOfState(pieceOfState + 1)}>Click Me to Update pieceOfState!</button>
    </div>
  );
}
```
- In this example, we're importing both useState and useEffect from React. Object destructuring syntax lets us list multiple comma-separated values.
- 	As part of this example, we are creating some state named pieceOfState, with an initial value of 0.
- 	Within our component function, we use the useEffect hook by invoking it.

**Dependency Arrays With Selective useEffect Calls**

This example specifies that useEffect should only run when oranges is updated. We accomplish this by passing in [oranges] as the second parameter to useEffect.
```javascript
import { useState, useEffect } from 'react';

function App() {

  const [apples, setApples] = useState(0);
  const [oranges, setOranges] = useState(0);

  useEffect(() => {
    console.log('I\'m in useEffect!');
    console.log('This is called when oranges updates,');
    console.log('NOT when apples updates');
  }, [oranges]);

  return (
    <div>
      <p>Apples: {apples}</p>
      <button onClick={() => setApples(apples + 1)}>Click Me to Update apples!</button>
      <p>Oranges: {oranges}</p>
      <button onClick={() => setOranges(oranges + 1)}>Click Me to Update oranges!</button>
    </div>
  );
}
```

## Executing useEffect Only After Mounting, Not After Updating
Sometimes, we have logic we want to execute only after the component is initially mounted, and we don't need it to run on update.

To achieve this, we should ensure that our second parameter, the dependency list, is an empty array.
```javascript
import { useState, useEffect } from 'react';

function App() {

  useEffect(() => {
    console.log('I\'m in useEffect!');
    console.log('This will be called ONLY when an instance of this component mounts');
    console.log('because our dependency list is empty');
  }, []);

  return (<h1>Demonstration of useEffect only called during mounting stage</h1>);
}
```
- 	The second argument is an empty array, to express that there are no dependencies to watch for. Essentially, there are no dependencies that should cause useEffect to run.

**Example: Changing document**

Recall that in static-site development using HTML, CSS, and vanilla JS, we saw that our JavaScript code can execute before the DOM is completely built. This meant we couldn't be certain that any particular DOM element was available when our script ran.

In vanilla JS, we handled this problem by listening for the "DOMContentLoaded" event:
`document.addEventListener('DOMContentLoaded', () => { console.log('We can manipulate the DOM now!'); });`

We can encounter a similar problem in React.

How can we get a reference to the desired element from the DOM if our JSX hasn't been rendered yet?

## Switching to useEffect

n order to directly manipulate the DOM in our component, we need to wait for the DOM to fully build, and our components to finish rendering.

This sounds like a job for useEffect! We can:
1. Import useEffect
2. Move our logic into a new function, which we pass into useEffect

```javascript
import { useEffect } from 'react';

function App() {

  console.log('The value of document is:', document);

  useEffect(() => {
    console.log('I\'m in useEffect!');
    document.getElementById('title').textContent = 'Not a Violin Practice Log';
  }, []);


  return (
    <div>
      <h1 id="title">Violin Practice Log</h1>
    </div>
  );
}
```

## Using useEffect to call APIs

Our primary use for the useEffect hook will be to make API calls after a component mounts.

We could make API calls inside a component function without caring about the lifecycle, but then API requests would run every time our function was called (i.e., every time the component gets re-rendered).

It's more advantageous to make API calls asynchronously after the app is fully rendered on the screen. The user gets immediate feedback that the page is loaded and data can appear as it is retrieved.

# Calling APIs from Components
In our React front-end layer, for each HTTP request we make, we need to determine:
- When does the web app make an HTTP request
  - What component makes the HTTP request?
  - What happens when we receive an HTTP response
    - How does the UI change?

Two common situations when we make HTTP requests in a React app are:
1. When a container component mounts (initially renders)
2. When an event is handled, such as a button being clicked, or text field being changed

**Using axios in a React Web App**

In order to call APIs in React, we can use the axios package  . To add axios into our project, we can run this command:
`$ yarn add axios`

Every file that uses axios should be sure to import it:
`import axios from 'axios';`

## Calling APIs after Render

Imagine a React app that needs to get a list of student data from an API, or an app that needs to get detailed data about one restaurant from a restaurant API.

In these situations, we should:
1. Determine a container component that is responsible for holding that data
2. Fetch the data when the component is mounted by using useEffect and an empty dependency list

Example:
```javascript
import { useEffect } from 'react';
import axios from 'axios';

const SomeComponent = () => {

  useEffect(() => {
    axios.get('some great url to make an API call to')
      .then((response) => {
        console.log('The data we get back from the HTTP response:', response.data);
      })
      .catch((error) => {
        console.log('Anything that isn\'t status code 2XX is an error:', error.response.status);
        console.log('The data from response with an error:', error.response.data);
      });
  }, []);

  return (<h1>My Perfect Component</h1>);
}
```
- The first argument we pass into useEffect is a function, which by default will execute every time the component mounts or updates.
- When the component renders, we send a GET request with axios.
- Following axios patterns, we chain a then() call to describe what should happen when an HTTP response of status 2XX comes back.
- The argument to then() is a function, which expects a parameter response. response will receive the result from calling axios.get(...), the HTTP response.
- 	Because we want this API call to happen only when the component mounts, and not when any updates are made, our dependency list is an empty array [].

**Prevent useEffect From Running After State Updates**

The goal of this API call is to call it only once, after the component mounts. Therefore, it's important to ensure that our dependency list for useEffect is an empty array [].

**Example: Dog CEO**

Belinda is making a small React app for themself, to quickly cheer themself up with a random dog picture whenever they want one. They want to make use of the Dog CEO API  .

So far, they have an App component. It tracks an imageUrl in its state, the initial value of which is the URL to a dog picture. The component renders this image in an <img> element.

```javascript
import { useState } from 'react';

function App() {
  const [imageUrl, setImageUrl] = useState('https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg');

  return (
    <div>
      <h1>My Dog Log</h1>
      <div>
        <img src={imageUrl} alt="A random dog" />
      </div>
    </div>
  );
}
```
**Working With APIs**
To use the Dog CEO API effectively, Belinda outlines the expected HTTP request and HTTP response first.

When the HTTP response is successful, from the documentation, they expect the response to look like this JSON:
```json
{
    "message": "https://images.dog.ceo/breeds/basenji/n02110806_4216.jpg",
    "status": "success"
}
```
In this situation, they should update the image URL in their React app to the value of "message" in this JSON object.

**Call Within useEffect**
After outlining the desired HTTP request and response, Belinda implements their API call, which updates the value of imageUrl. They introduce a piece of state, errorMessage, as part of this work.

```javascript
import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [imageUrl, setImageUrl] = useState('https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg');
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    axios.get('https://dog.ceo/api/breeds/image/random')
      .then((response) => {
        setImageUrl(response.data.message);
      })
      .catch((error) => {
        setErrorMessage(<section>{error.response.data.message}</section>);
      });
  }, []);

  return (
    <div>
      <h1>My Dog Log</h1>
      {errorMessage}
      <div>
        <img src={imageUrl} alt="A random dog" />
      </div>
    </div>
  );
}
```

**Side note: Styling Opportunity: Error Messages**
Error messages are important for the end user to see, so they can understand what's going on if there's a problem. Great web design should emphasize the importance of an error message! We could add styles such as a red border, yellow background color, large bold text, etc, to make our error message stand out.

## Calling APIs in Functions
Imagine the following situations:
- Clicking a "Share to Twitter" button calls the Twitter API to create a new Tweet
- Pressing the "Search With Filters" button calls the Google API to get more search results
- Click a trash can icon next to a shopping item calls the back-end layer API to delete the shopping item

**Example: Dog CEO API**
Belinda wants to improve their random dog image app. Instead of getting a random dog image every time the App component mounts, they should get it by a button press!

```javascript
import { useState } from 'react';

function App() {
  const [imageUrl, setImageUrl] = useState('https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg');

  return (
    <div>
      <h1>My Dog Log</h1>
      <div>
        <button onClick={() => { console.log("The button was clicked!"); }}>Get New Random Dog Image</button>
        <img src={imageUrl} alt="A random dog" />
      </div>
    </div>
  );
}
```
- The onClick handler for this button is a one-line anonymous arrow function that logs "The button was clicked!" to the console.

**Event Handling With API Calls**

They want to call the API and update state appropriately.
- They put the logic in a new helper method, getRandomImage.
- Belinda makes a dedicated event handler called onButtonClick. The only action it needs to take is to call the getRandomImage helper function to start the process of making the random dog GET request.
- Belinda sets the onClick handler of the button to be the new onButtonClick function.
```javascript
 import { useState } from 'react';
import axios from 'axios';

function App() {
  const [imageUrl, setImageUrl] = useState('https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg');
  const [errorMessage, setErrorMessage] = useState('');

  const getRandomImage = () => {
    axios.get('https://dog.ceo/api/breeds/image/random')
      .then((response) => {
        setImageUrl(response.data.message);
        setErrorMessage('');
      }).catch((error) => {
        setErrorMessage(<section>{error.response.data.message}</section>);
      });
  };

  const onButtonClick = () => {
    getRandomImage();
  };

  return (
    <div>
      <h1>My Dog Log</h1>
      {errorMessage}
      <div>
        <button onClick={onButtonClick}>Get New Random Dog Image</button>
        <img src={imageUrl} alt="A random dog" />
      </div>
    </div>
  );
}
```