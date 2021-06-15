# Event Handling
- Event: An action in a browser

**Summary:**
1. Select HTML event event will occur on
2. Make function to run when that event occurs
   1. could be skipped by giving an anonymous function as 2nd parameter in step 3.
3. Register that function to an event listener

## Event Driven Programming
We can write JavaScript to more specifically handle events. 

Examples are:
- When a user clicks on a darkmode button - the website's appearance changes
- When a user submits a share to social media form - API calls are made to Facebook/Twitter/Github
- Scrolling to bottom of page reveals more articles

In JavaScript:
- Events have names, like click or scroll
- Events always happen on an HTML element. For example, a click event happens on a <button>... or a <section>... or a <body>. 
- Every event happens on at least one element.
- Events need a way to be fired/triggered/activated at the time of the event
- Events need a way to be listened to

Default Events [https://developer.mozilla.org/en-US/docs/Web/Events]
- keydown: any key pressed
- keyup: any key released
- click: pointing device pressed and released on elem

## Onclick Handling
- Event Handler: A function whose responsibility is to perform necessary, required, or desired actions after a certain event is fired.

**Building an Event Handler**

Create the response to an event:
```javascript
// a function that takes no params 
const addCrab = () => {
    // creates a span elem
  const newCrab = document.createElement("span");
//   grabs the elem with the ID crabContainer
  const crabContainer = document.querySelector("#crabContainer");
//   puts the emoji in the span
  newCrab.textContent = "🦀";
//   add the span to the parent container
  crabContainer.appendChild(newCrab);
};
```
Register our event handler to the event:
`someElement.addEventListener("some event name", reactToEvent);`
- reactionToEvent is NOT reactioToEvent() because we only want to pass in the function, which will run only when the desired action is registered. 

Thise code registers our event handler in response to handling a different event: DOMContentLoaded.
```javascript
// create helper func which connects elems to event handlers
const registerEventHandlers = () => {
    // constant to hold button
  const crabButton = document.querySelector("#addCrabButton");
    // call addEventListener on crab button.
  crabButton.addEventListener("click", addCrab);
};
// After defining the registerEventHandler function, we call this function. We want the document itself to react to an event.
document.addEventListener("DOMContentLoaded", registerEventHandlers);
// The name of the event that fires when the DOM has loaded completely is "DOMContentLoaded."
// registerEventHandlers execute when document receives an event called DOMContentLoaded
```

- Why listen for: DOMContentLoaded?
  - We need to ask our document to wait and register the event handlers after the DOM has been completely loaded. This is because the JavaScript file often loads faster than the DOM does!

**Event Objs**
"Events" are themselves objects. Event objects contain all the information about the event, such as what type of event it is, and where it happened. 

By default, our browser will pass in the event object (the object that represents the event) into every event-handler function.

## State
State is a general term to describe the information held in a web app at one specific moment in time.
- in OOP, obj state is its attributes.
- in Web App, its data stored is the state.

we're making state a const variable, even though we will be modifying it, remember that the const applies only to whether we can change which object the variable references. By declaring that state is a const, we can't change state to point at a different object, but we can still modify the key-value pairs within state!

