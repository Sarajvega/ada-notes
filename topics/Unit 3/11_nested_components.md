# Nested Components

When components are rendered, they can contain one or more elements or other components.
- App component is an example

```javascript
function App() {
  return (
    <main>
      <h1>Attendance</h1>
      <ClassInfo></ClassInfo>
      <StudentList></StudentList>
    </main>
  );
}
```
- Here ClassInfo and StudentList are siblings. 

Deciding how to design a React webapp and its components can be challenging. We can learn about and apply two design patterns to help us:
- Presentational components
  - Display data
  - Don't modify data
- Container components
  - Use presentation components
  - Hold data
  - Modify data
  - Send data to presentation components
  - Have presentation components nested inside.

Example:
```javascript
import React from 'react';
import './StudentList.css';

const StudentList = () => {
    return (
        <section>
            <h2>Student List</h2>
            <ul>
                <li>Student A</li>
                <li>Student B</li>
                <li>Student C</li>
            </ul>
        </section>
    )
}

export default StudentList;
```
Sofia can apply the container and presentational component design patterns, and:
- Create a Student component, which will act as a presentational component
- Use the Student component in StudentList, which will act as a container component

## Props
Props are pieces of data that a component can read. They are one of the two ways that React components manage and share their data. "Props" is short for properties.
- Data cannot be modified w/in a component. 
- Are name/value pairs

**Example:**
We can imagine creating two components, Library and Book. Library is a container component responsible for displaying books. Book is a presentational component responsible for displaying a book's title and author. Library could hold all the data about books. The Library component can pass data about a book title and an author to each Book component using props.

## Syntax
**Passing props from ComponentA to ComponentB**
- ComponentB is designed to be used in a variety of situations and expects to be given a prop called varName that it uses during its rendering.
-  ComponentA uses ComponentB as part of its own rendering, so ComponentA must provide the expected varName prop value to ComponentB where it uses ComponentB as a JSX element.

Generic:
```javascript
import ComponentB from './ComponentB';

const ComponentA = () => {
  return <ComponentB varName="value goes here"></ComponentB>;
};

export default ComponentA;
```
- Component B is imported
- varName = name of prop passing into instance of ComponentB
- "value goes here" value of the varName

Applied Example:
```javascript
const Library = () => {
  return (
    <div>
      <Book title="Hello Web App" author="Tracy Osborn" isbn="978-0986365911"></Book>
      <Book title="JavaScript Cookbook" author="Shelley Powers" isbn="9781491901885"></Book>
    </div>
  );
};
```
**Reading props in ComponentB**
Within the ComponentB definition, we can read props by taking these steps:
1. Change the function signature of ComponentB to accept one argument, an object named props
2. Access values in the props object using dot notation or square-bracket notation

Way 1:
```javascript
const ComponentB = (props) => {
  return <div>The value of varName: {props.varName}</div>;
};
```
- takes props as an arg.
- nstead of props.varName, we could alternatively use props["varName"].

Way 2:
```javascript
const ComponentB = (props) => {
  const valueOfVarName = props.varName;
  return <div>The value of varName: {valueOfVarName}</div>;
};
```
- save value inside of a variable. 

With book example:
```javascript
const Book = (props) => {
  return (
    <section>
      <h2>{props.title}</h2>
      <ul>
        <li>by {props.author}</li>
        <li>ISBN: {props.isbn}</li>
      </ul>
    </section>
  );
};
```

## Iterating over data structurs
Can Sofia use this data structure to create Student components inside her StudentList component?
```javascript
[
    {
        nameData: 'Ada',
        emailData: 'ada@dev.org'
    },
    {
        nameData: 'Soo-ah',
        emailData: 'sooah@dev.org'
    },
    {
        nameData: 'Chrissy',
        emailData: 'chrissy@dev.org'
    }
]
```

Yes! She can iterate through this data and create an array of JSX elements with the correct props. Then, she'll embed that array of elements in her component output.
```Javascript
const StudentList = () => {
    const studentData = [
        {
            nameData: 'Ada',
            emailData: 'ada@dev.org'
        },
        {
            nameData: 'Soo-ah',
            emailData: 'sooah@dev.org'
        },
        {
            nameData: 'Chrissy',
            emailData: 'chrissy@dev.org'
        }
    ];

    const studentComponents = studentData.map(student => {
        return (
            <li key={ student.emailData }><Student name={student.nameData} email={student.emailData}></Student></li>
        );
    });

    return (
        <section>
            <h2>Student List</h2>
            <ul>
                {studentComponents}
            </ul>
        </section>
    );
};
```
- `studentData.map(...)` sets studentComponents to an array of JSX elements. It does this by iterating over each object in studentData, passing each value, one at a time, into our anonymous function as the student parameter. The JSX element we return is used to fill in the result array assigned to studentComponents.
- assign a key otherwise console yells at you! Key can be anything, another option is {index}
**Sending props From App**
Sofia anticipates that she may want to display student information for multiple classes.

She defines studentData in the App component.
```javascript
function App() {
  const studentData = [
    {
      nameData: 'Ada',
      emailData: 'ada@dev.org'
    },
    {
      nameData: 'Soo-ah',
      emailData: 'sooah@dev.org'
    },
    {
      nameData: 'Chrissy',
      emailData: 'chrissy@dev.org'
    }
  ];

  return (
    <main>
      <h1>Attendance</h1>
      <ClassInfo></ClassInfo>
      <StudentList students={studentData}></StudentList>
    </main>
  );
}
```
StudentList receives a prop named students.

**Reading props in StudentList**
```javascript
const StudentList = (props) => {
    const studentComponents = props.students.map(student => {
        return (
            <li><Student name={student.nameData} email={student.emailData}></Student></li>
        );
    });

    return (
        <section>
            <h2>Student List</h2>
            <ul>
                {studentComponents}
            </ul>
        </section>
    );
};
```