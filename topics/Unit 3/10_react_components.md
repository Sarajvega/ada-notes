# React Components
- User Interface (UI): The elements with which a user interacts in order to make a machine do something. UI elements are usually visual, but UI also describes how a user interacts with a webapp, such as buttons, text fields, or sliders.
- Components (React): Independent, reusable pieces of UI.

We run into the term component a lot when programming. It doesn't always mean exactly the same thing in every situation. When we are discussing React, we should focus on components as being independent, reusable pieces of UI, regardless of what component might mean in other contexts.

## Using a Toolchain
We will use a specific tool to help us begin a minimal React app: the [Create React App](https://create-react-app.dev/)  tool.
`npx create-react-app hello-world` 
- `npx` = A CLI tool that runs packages. 

index.js is the starting point of our app as it renders the first JSX!
```
<React.StrictMode>
  <App />
</React.StrictMode>
```
- This code indicates that when we start our React webapp, it will render an App component using `<App />`.

App.js Defines Our App Component
The App function defines a component named App.
The responsibility of the App function is to return how to render the App component whenever the App component is declared and used.

## JSX
JSX is used to declare HTML-like UI in React JS. It determines what our webapp's rendered HTML looks like.

[JSX](https://reactjs.org/docs/introducing-jsx.html)  is a syntax extension to JavaScript that isn't normally available in vanilla JavaScript projects. It may look like HTML, but it's really JavaScript in disguise!

An object in JSX contains at least one element.
`const welcomeMessage = <span>Welcome~</span>;`

It can have many children:
```javascript
const welcomeMessage = (
  <section>
    <h1>Welcome~</h1>
    <p>It's nice to hear from you again!</p>
  </section>
);
```

## JSX classes
While HTML elements use the class attribute, in JSX we use the className attribute.
`<header className="App-header"></header>`

## Components
All components can be rendered to the page, hold data, manage their own state, handle events, and contain other elements and components.
- Conventionally, React components are named with CapitalCamelCase.

All components are:
- Functions
- Responsible for returning one JSX object, which determines how it's rendered

In order to "use" a component, there are three steps:
1. Plan the component
2. Define the component
3. Render that component at least once

## Defining a Component
1. Create a new file
2. Import React, and any other dependencies
3. Create a function
4. Export the component

## Creating a new file
- Each component definition will have its own .js file
- Each file will be named after the name of the component
- All component definitions besides App will live in a new folder, src/components
- import React at top of .js file: `import React from 'react';`

**Creating a function** 
Each component begins with a function.

Each component function should:
- be named after the component
- return one JSX object that represents how to render this component

Example
Way 1:
```javascript
const StudentList = () => {
  return <h2>Student List</h2>;
};
```
Way 2:
```javascript
const StudentList = () => {
  return (
    <h2>Student List</h2>
  );
}
```

Way 3:
```javascript
const StudentList = () => {
  const studentListHeader = <h2>Student List</h2>;
  return studentListHeader;
}
```

**Export the component**
To export the component, we make an export statement at the bottom of our file, and specify the name of our component function.
`export default StudentList;`

## Rendering a Component Once
Determine where and when we want to show the component
- at the top of that file import it:
- ex: `import StudentList from './components/StudentList';`
Import the component
Declare the component at least once


**Declare the Compnent at Least Once**
To render this component, we can include it in any JSX object. If a component returns a JSX object that includes this component, then the component will render it.

To include a component once in a JSX object, we use the following syntax:
`<ComponentName></ComponentName>`

Example:
```javascript
import StudentList from './components/StudentList';

function App() {
  return (
    <main>
      <h1>Attendance</h1>
      <StudentList></StudentList>
    </main>
  );
}

export default App;
```
Embed as a variable example:
```javascript
import StudentList from './components/StudentList';

function App() {
  const studentList = <StudentList></StudentList>;
  return (
    <main>
      <h1>Attendance</h1>
      {studentList}
    </main>
  );
}

export default App;
```

## Rendering More Than One
We render a component more than once by declaring it in multiple places.
```javascript
import StudentList from './components/StudentList';
import ClassInfo from './components/ClassInfo';

function App() {
  return (
    <main>
      <h1>Attendance</h1>
      <ClassInfo></ClassInfo>
      <StudentList></StudentList>
    </main>
  );
}

export default App;
```

## Styling Components
There are two ways we can add styles to a component:
- Create and import an external CSS file, and use attributes like className
- Create inline style objects, and use the style attribute

**External CSS File**
This CSS file will share the name of the component, and will live in the same folder as the component.

ex: Following these guidelines, to style her StudentList component, she'll create a file src/components/StudentList.css.
- To include the new CSS file, Sofia should import it into the StudentList component file.

However, we must be careful of one thing: in order to set the CSS class attribute on any HTML element when using JSX, we must use the attribute className.


```javascript
const StudentList = () => {
    return (
        <section>
            <h2 className="student-list__heading">Student List</h2>
            <ul className="student-list">
                <li>Student A</li>
                <li>Student B</li>
                <li>Student C</li>
            </ul>
        </section>
    )
}
```
- student-list__heading = BEM styling, you list your component name first then the element you are styling. Avoids overlapping styles.
- 
**Injecting CSS**
We can store our CSS class names in variables, then inject them into our JSX as follows:
```javascript
const StudentList = () => {
    const headingClass = 'student-list__heading';
    const listClass = 'student-list';

    return (
        <section>
            <h2 className={headingClass}>Student List</h2>
            <ul className={listClass}>
                <li>Student A</li>
                <li>Student B</li>
                <li>Student C</li>
            </ul>
        </section>
    )
}
```
- Saving CSS in a variable is helpful for dark/light mode. 
  
**Inline Style Object**
**DISCOURAGED METHOD**
The style attribute takes in a JavaScript object. This JS object should contain property-value pairs, where the property name is equivalent to a CSS style property, but camelCase.
```javascript
const helloWorldStyle = {
  color: 'blue',
  backgroundImage: 'url(' + imgUrl + ')',
};

const someComponent = () => {
  return <h1 style={helloWorldStyle}>Hello World!</h1>;
}
```