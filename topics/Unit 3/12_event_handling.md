# Event Handling

## Event Listeners
To handle events in React, the proper attribute follows the pattern of `"on<blank>"` in camelCase, where `<blank>` is the name of the event. 
`<SomeElement onClick={...}></SomeElement>`

## Event Handling Functions
**The value of our event listener should be a function.**
```javascript
const Post = () => {
    const printMessage = () => {
        console.log('Hello! We\'re in printMessage!');
    };

    return (
        <section>
            <button onClick={printMessage}>Like</button>
        </section>
    );
};
```
- The "like" button listens for click events. 
- By setting the value of onClick to printMessage, our web app invokes printMessage whenever we click the like button.

**Event Handling Functions Can Accept `event`**
As with vanilla JavaScript event handling, we usually name this parameter event to remind us what to expect in that parameter. Also like vanilla JavaScript, this is merely convention, and we can name the parameter whatever we would like.
```javascript
const Post = () => {
    const printMessage = (event) => {
        console.log('Hello! We\'re in printMessage!');
        console.log('This event object contains details about the event:', event);
    };

    return (
        <section>
            <button onClick={printMessage}>Like</button>
        </section>
    );
};
```

**Event Handling Functions Are Functions**

```javascript
const Post = () => {
    const printName = (name) => {
        console.log('We\'re in printName!');
        console.log(`Hello, ${name}!`);
    };

    const printMessage = () => {
        printName('Ada Lovelace');
        console.log('Now, we\'re in printMessage!');
    };

    return (
        <section>
            <button onClick={printMessage}>Like</button>
        </section>
    );
};
```
Consider this Post component. It:
- Defines a function, printName, which takes in a name argument
- Defines another function, printMessage. It calls printName with the argument "Ada Lovelace".
- Sets printMessage as the click event handler for a "Like" button

## Pattern: Anonymous Functions
**Our event handlers can be anonymous functions.**

```javascript
const Post = () => {
    const printName = (name) => {
        console.log('We\'re in printName!');
        console.log(`Hello, ${name}!`);
    };

    return (
        <section>
            <button onClick={() => printName('Ada Lovelace')}>Like</button>
        </section>
    );
};
```
Every time we click on our "like" button, our anonymous function will fire. This, in turn, invokes printName('Ada Lovelace')!

Using anonymous functions for event handlers is a common pattern in React, especially when the function we want to call needs us to pass in some parameters.

A common mistake when trying to call a function that takes an argument as an event handler is to try to write the function call, in this case printName('Ada Lovelace'), directly as the even handler.

But this does not have the desired result! Instead, it:
1. Calls printName('Ada Lovelace') as the button is being rendered rather than when it is clicked. This causes the output message to appear while the page is still being rendered. Not what we wanted!
2. Sets the result of calling printName('Ada Lovelace') as the click handler. Since printName returns nothing, the result is undefined. So no event handler is registered for onClick, and the button does nothing when it is clicked. Also not what we wanted!
3. So when our desired behavior takes at least one parameter, we can use this technique of wrapping it in an anonymous function.

**Why us anonymous functions?**
An anonymous function lets us call arbitrary code exactly where the event registration occurs, which can be good for understandability. But we may find that, if we need to do more than one or two things in the event handler, then using a named function may still be more understandable.

## Using State
- `prop` passes data between components. 
- props are read-only!

If we:
Build a weather web app, and need a button that increases the temperature displayed from 31 to 32.

We need to capture the change of state of our front-end. 

## React Treats State Specially Because of Re-Rendering
Under the hood, React achieves its speed by detecting changes in state, and re-rendering only those components that depend on that state.

Whenever we introduce state in a component, we will need two things:
1. a variable to hold that piece of state
2. a way to update that piece of state

For example, let's imagine a CollapsibleForm component. This component needs to manage if the form is collapsed or expanded. For this piece of state, we need:
1. a variable such as isCollapsed, which can hold true or false
2. a way to update isCollapsed

## The useState Hook Generates a Variable and Update Function
React hooks are functions that provide different features by cleverly hooking into the under-the-hood React component lifecycle.

The most common React hook we will use is the useState hook. It gives us the ability to manage and maintain state.

useState is a function. It returns an array of two things.
1. In index 0 of the returned array, there is a variable that references the piece of state we're managing
2. In index 1, there is a reference to a function for updating that piece of state

useState also takes a single argument.
1. The value used to initialize the piece of state, used only the first time the component instance is rendered. This will become important when we look at updating our state value later.

Example:
```javascript
import { useState } from 'react';

function App() {
  const resultFromUseStateHook = useState('initial value of a piece of state');

  console.log('A reference to the piece of state:', resultFromUseStateHook[0]);
  console.log('A function to update this piece of state:', resultFromUseStateHook[1]);
}

export default App;
```

## Using useState
The conventional way to use useState is to take advantage of destructuring assignment.

For every piece of state we want a component to have, we need to call useState:
```javascript
import { useState } from 'react';

function App() {
    // pieceOfState = data
    // setPieceofState = func that updates state. 
    const [pieceOfState, setPieceOfState] = useState('Initial value for pieceOfState.');
}
```

Example:
```javascript
import { useState } from 'react';

const Post = () => {
    const [likesCount, setLikesCount] = useState(0);

    return (
        <section>
            <p>What is the number of likes we should display? {likesCount}</p>
        </section>
    );
};

export default Post;
```
-  we use likesCount inside our returned JSX. We can read likesCount just like any other variable.

## Updating State
Let's assume that we have a component that has initialized a piece of state named pieceOfState:
`const [pieceOfState, setPieceOfState] = useState('Initial value for pieceOfState.');`

In order to update state, we call the update function, and pass in the new value.
`setPieceOfState('New value of pieceOfState.');`

**Updating State Re-Renders the Component**
Re-rendering a component is hard work! Firstly, setting state is asynchronous. Secondly, to repeat, every time that state updates, the component re-renders. These two facts will aid us when debugging state.

## Updating State As Part of Event Handling
The best time to update state is in response to handling user events.

**Example:**
Let's imagine a Post component. It's responsible for displaying the number of likes that a post has.

Each post starts with zero likes. When we click the "like" button, the number of likes increases.

Let's consider the code we need to write for this:
1. The Post component should have a piece of state, likesCount. likesCount is data that changes within the component, so we should represent it with a piece of state rather than a prop.
2. We should get a reference to the update function for this piece of state, and store it in a variable with a good name like setLikesCount.
3. The "like" button should listen for click events, using the attribute onClick.
4. When the "like" button is clicked, we should call an event handler function. We can name this function increaseLikes.
5. When our component increases likes in increaseLikes, we should update our state using setLikesCount.
   
```javascript
import { useState } from 'react';

const Post = () => {
    const [likesCount, setLikesCount] = useState(0);
    const increaseLikes = () => {
        console.log('We\'re inside increaseLikes!');
        setLikesCount(likesCount + 1);
    };

    return (
      <section>
        <p>The number of likes is {likesCount}.</p>
        <button onClick={increaseLikes}>Like</button>
      </section>
    );
};

export default Post;
```

Example:
Sofia wants to add a feature of toggling the presence of a student.

When a student is present, their name is green. When a student is absent, their name is red.

She'll need to update her app in the following ways:
1. Create two CSS classes: one that sets the name to green, and another to set the name to red
2. Create a piece of state in Student to hold whether the student is present
3. Create a button in Student to toggle whether the student is present
4. Create an event handler that updates state whenever the button is clicked
5. Use the CSS class in Student. One CSS class should be applied if the student is present, and the other CSS class should be applied if they're absent.

**CSS**
In src/components/Student.css, Sofia adds these two classes:
```css
.green {
  background-color: greenyellow;
}

.red {
  background-color: lightcoral;
}
```

**isPresent state in Student**
In src/components/Student.js, Sofia adds these two lines to create isPresent state:
`import { useState } from 'react';`

This line is in the Student component function, before the return statement:
`const [isPresent, setIsPresent] = useState(false);`

**Create Toggle presence Button in Student**
Sofia updates the returned JSX in Student. She adds this `<button>` just after the `</ul>` tag, with an appropriate label.
```javascript
    return (
        <div>
            <ul>
                <li>Nickname: {props.name}</li>
                <li>Email: {props.email}</li>
            </ul>
            <button>Toggle if {props.name} is present</button>
        </div>
    );
```

**Create Event Handler**
Sofia now creates the event handler, which updates the isPresent state. This function is in the Student component function, before the return statement.
```javascript
    const togglePresence = () => {
        setIsPresent(!isPresent);
    };
```

**Attach the Event Handler to the Button**
`<button onClick={togglePresence}>Toggle if {props.name} is present</button>`

**Modify the JSX to Use Conditional CSS Classes**
Now, Sofia needs to conditionally select which CSS class to apply to the student's name.

In her Student component, she will create a variable to hold the value of the appropriate CSS class. This value will use:
- The value of isPresent
- The names of the CSS classes she created earlier

First, she ensures that her CSS file is imported:
`import './Student.css';`

Then, she creates a variable that holds the name of the (CSS) classes. She uses a ternary to express this. If isPresent is true, the variable should be 'green'. If isPresent is false, it should be 'red'.
`const nameColor = isPresent ? 'green' : 'red';`

Finally, she ensures that this variable is used as a class name in her JSX.
`<li className={nameColor}>Nickname: {props.name}</li>`

Final result of Student component:
```javascript
import { useState } from 'react';
import PropTypes from 'prop-types';
import './Student.css';

const Student = (props) => {
    const [isPresent, setIsPresent] = useState(false);

    const togglePresence = () => {
        setIsPresent(!isPresent);
    };

    const nameColor = isPresent ? 'green' : 'red';

    return (
        <div>
            <ul>
                <li className={nameColor}>Nickname: {props.name}</li>
                <li>Email: {props.email}</li>
            </ul>
            <button onClick={togglePresence}>Toggle if {props.name} is present</button>
        </div>
    );
};

Student.propTypes = {
    name: PropTypes.string.isRequired,
    email: PropTypes.string.isRequired
};

export default Student;
```