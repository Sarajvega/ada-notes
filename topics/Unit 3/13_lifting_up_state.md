# Lifting up State

She has been working hard and learning a lot! She has built the following components:
1. An App component that holds student data and renders a StudentList component
```javascript
import StudentList from './components/StudentList';

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
            <StudentList students={studentData}></StudentList>
        </main>
    );
}

export default App;
```

2. A StudentList component that renders a Student component for each student in the student data
```javascript
import './StudentList.css';
import PropTypes from 'prop-types';
import Student from './Student';

const StudentList = (props) => {

    const studentComponents = props.students.map((student, index) => {
        return (
            <li key={index}>
                <Student name={student.nameData} email={student.emailData}></Student>
            </li>
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

StudentList.propTypes = {
    students: PropTypes.arrayOf(PropTypes.shape({
        nameData: PropTypes.string.isRequired,
        emailData: PropTypes.string.isRequired
    }))
};

export default StudentList;
```
3. A Student component that renders student information, and contains a button that toggles the student's attendance
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

In Sofia's app, each Student component manages a piece of state named isPresent. When the button is clicked, we update isPresent. When isPresent is updated, the component re-renders.

Sofia already sees what she wants to see! When she clicks the button, the appearance of her app changes, and a student's name toggles between red and green.

However, when she considers her student data, Sofia sees a problem.

## Debugging State With React Developer Tool

However, when she marks a student as present or absent, it doesn't affect the student data at all!

**React dev tools are extensions for several browsers**

This extension expands the browser Dev Tools whenever we inspect a page built with React. The extension gives us two new views, "Components" and "Profiler." We'll use this extension to inspect the component structure in a React app, and observe state and props in each component.

When we view the Components tab, we see the component structure of our web app! We see an App component, a StudentList component, and three Student components. We can select any of the components. The panels will update to reflect the props and state of each component.

## Applying Design Patterns
Let's consider how container component and presentational component design patterns appear in Sofia's app:
- App: Container component, because it holds and manages student data and passes it to its children components
- StudentList: Presentational component, because it's responsible for rendering many students
- Student: Presentational component, because it's responsible for rendering student data. But it also owns the isPresent data for each student!

Sofia's app currently manages toggling isPresent in the Student component, but this data has no way to get back up to the App component.

To refactor Sofia's attendance feature, we will follow these steps:
1. Create a "single source of truth"
2. Pass down data and event handlers to presentational components
3. Ensure that our event handlers "lift state up"

## Single Source of Truth
[single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth) is the practice of structuring our code so that data is managed in one place.

In Sofia's app, all components that read student data, should reference it from the same source.
Right now, Sofia's app introduces student data in two places:
1. The App component, which holds student names and emails
2. The Student component, which manages student isPresent details

> Consider for a moment what it would be like if we didn't strive for a single source of truth. As we continued to develop our app, we'd possibly ask the following questions:
> If another component needs to read a student's isPresent state, where do they look for that data? For example, what if another component wanted to count how many students were absent that day? If there are multiple sources of truth, in what situations do we update one source of truth, but don't update the others? What happens if our multiple sources of truth are out of sync with each other?

These questions highlight problems that are challenging to work with!

**Moving isPresent From Student to App**

Sofia chooses to move the data to the App component. She chooses the App component because:
1. It's more appropriate for the responsibility we gave App
2. In React, we pass read-only data through props, which is passed into nested components. Student is more nested than App.

First, Sofia adds isPresent to the student data in App.
While she's there, she also adds id data to each student. This helps the data feel a little more realistic, as if it were coming from a database or API.

```javascript
function App() {
  const studentData = [
    {
      id: 1,
      nameData: 'Ada',
      emailData: 'ada@dev.org',
      isPresentData: false
    },
    {
      id: 2,
      nameData: 'Soo-ah',
      emailData: 'sooah@dev.org',
      isPresentData: false
    },
    {
      id: 3,
      nameData: 'Chrissy',
      emailData: 'chrissy@dev.org',
      isPresentData: true
    }
  ];

  return (
    <main>
      <h1>Attendance</h1>
      <StudentList students={studentData}></StudentList>
    </main>
  );
}
```

**Update PropTypes**

Since Sofia changed the structure of studentData, she also needs to update the PropTypes for the components that receive studentData through their props: StudentList and Student.

She added id and isPresentData to the studentData, so these need to be added to the PropTypes shape.

She updates the PropTypes for StudentList like this:

```javascript
// originally:
// StudentList.propTypes = {
//     students: PropTypes.arrayOf(PropTypes.shape({
//         nameData: PropTypes.string.isRequired,
//         emailData: PropTypes.string.isRequired
//     }))

StudentList.propTypes = {
    students: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.number.isRequired,
        nameData: PropTypes.string.isRequired,
        emailData: PropTypes.string.isRequired,
        isPresentData: PropTypes.bool
    }))
};
```

And for Student she does this:
```javascript
// originally
// Student.propTypes = {
//     name: PropTypes.string.isRequired,
//     email: PropTypes.string.isRequired
// };
Student.propTypes = {
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    email: PropTypes.string.isRequired,
    isPresent: PropTypes.bool
};
```

**Ensure StudentList Passes the New App Data**

The new pieces of data, id and isPresentData, have been added to App. Now Sofia needs to make sure this data gets used in the rest of the app!

The data gets sent from App to StudentList through the prop named students.

StudentList should read students, and send the data for each student to a new Student component.

Sofia updates the code that builds the array of Student components like this:
```javascript
// originally:
// const StudentList = (props) => {

//     const studentComponents = props.students.map((student, index) => {
//         return (
//             <li key={index}>
//                 <Student name={student.nameData} email={student.emailData}></Student>
//             </li>
//         );
//     });

// now:
const StudentList = (props) => {
    const studentComponents = props.students.map((student, index) => {
        return (
            <li key={index}>
                <Student
                    id={student.id}
                    name={student.nameData}
                    email={student.emailData}
                    isPresent={student.isPresentData}
                ></Student>
            </li>
        );
    });

    // ... return some JSX
};
```

**Use isPresent as a prop in Student**

Now, the other "source of truth" has to go! The piece of state isPresent in Student competes with the isPresentData set in the App and needs to be removed.

Sofia removes that piece of state, and updates her code to use isPresent from the read-only props that were set by StudentList.
```javascript
const Student = (props) => {

    const nameColor = props.isPresent ? 'green' : 'red';

    return (
        <div>
            <ul>
                <li className={nameColor}>Nickname: {props.name}</li>
                <li>Email: {props.email}</li>
            </ul>
            <button onClick={/* togglePresence */}>Toggle if {props.name} is present</button>
        </div>
    );
};
```
Here, Sofia:
- Deleted the line that initialized the piece of state isPresent with useState
- Deleted the function togglePresence, which updated isPresent
- Modified how nameColor is set: the conditional logic now reads from props.isPresent
- Commented out the onClick event handler of the button

Sofia removed the togglePresence event handler, so she can't register it with the button anymore. So then what should the button do when it's clicked?

**She'll pass down an event handler!**

## Passing Down Event Handlers

**Move studentData into State**

In the App component, we know we want these two things:
1. We should be able to modify and update studentData
2. Every time studentData is updated, it should affect the UI, and the App component should re-render

These two qualities make it perfect to turn into state.
```javascript
function App() {
  const [studentData, setStudentData] = useState([
    {
      id: 1,
      nameData: 'Ada',
      emailData: 'ada@dev.org',
      isPresentData: false
    },
    {
      id: 2,
      nameData: 'Soo-ah',
      emailData: 'sooah@dev.org',
      isPresentData: false
    },
    {
      id: 3,
      nameData: 'Chrissy',
      emailData: 'chrissy@dev.org',
      isPresentData: true
    }
  ]);

  return (
    <main>
      <h1>Attendance</h1>
      <StudentList students={studentData}></StudentList>
    </main>
  );
}
```
This code:
- Creates a new piece of state named studentData
- Creates a new update function named setStudentData
- Sets the initial value of studentData
- Passes the value of studentData to StudentList in the prop students

**Create a Function to Update studentData in App**

In App, let's create a function named updateStudentData. It will be responsible for taking in the updated data for one student, and updating studentData in state.

Since this function updates one student, it needs to receive the updated student data. This function should accept a parameter, updatedStudent.

This function should go inside the App component, after studentData is defined, and before the return statement.

```javascript
  const updateStudentData = updatedStudent => {
    const students = studentData.map(student => {
      if (student.id === updatedStudent.id) {
        return updatedStudent;
      } else {
        return student;
      }
    });

    setStudentData(students);
  };
  ```
- `const updateStudentData =`: We're creating a function named updateStudentData.
- `updatedStudent`: This function accepts one argument: an object that holds updated student data. Notice that since we use this data to update our student data list, the object should match the structure of our student data that we pass through props.
- `const students = ;`: For this function, we create a helper array, students to contain the updated student data.
- `setStudentData(students);`: Ultimately, we want to update the studentData in our state. We use our state update function, setStudentData, and we update it to our newly formed students array.

**Helping React Notice That studentData Changed**

> Notice that during the update, we made a helper array that is more or less a copy of the data we already had. For every student whose ID does not match the updatedStudent, we reuse the student data that was previously in our state. So why couldn't we simply find the matching student data in our existing state and update that?
> 
> Because React wouldn't notice the change! For container types, like arrays and objects, if we update an inner value (an item in an array, or a field in an object) and then call the relevant set function, React will see that the reference to the object currently in state is the same reference as the object being passed into the set function. For performance reasons, it assumes that if the same reference is passed in to a set function, it is the same object. It will not look within the array or object for changes!
> 
> So to get React to notice that a value in our array or object has changed, we need to make a new outer reference, and copy the existing values into it. Then when we call a set function, it will see the change and trigger a re-render.


**Send This Function to StudentList**

Now that we've defined updateStudentData, imagine if other components could use this function.

If other components could use this function, they'd have the ability to update the studentData in App! We want the Student component to update the studentData in App.

Other components can use the updateStudentData function if they can reference it... and they can, using props. We can pass a reference to the updateStudentData down to a component through its props!

First, let's change App so that it sends this function to StudentList through a new prop named onUpdateStudent.
```javascript
return (
    <main>
      <h1>Attendance</h1>
      <StudentList
        students={studentData}
        onUpdateStudent={updateStudentData}
      ></StudentList>
    </main>
  );
  ```

Let's update the PropTypes for StudentList. Our StudentList component now expects a prop named onUpdateStudent, whose value is a reference to a function.
```javascript
StudentList.propTypes = {
    students: PropTypes.arrayOf(PropTypes.shape({
        id: PropTypes.number.isRequired,
        nameData: PropTypes.string.isRequired,
        emailData: PropTypes.string.isRequired,
        isPresentData: PropTypes.bool
    })),
    onUpdateStudent: PropTypes.func.isRequired
};
```

**Send This Function to Student**

Now, let's send this exact same function reference from the StudentList component to the Student component.

We access this function through props, and we send it to Student through props.

The keys to reading and writing this code are to:
1. Check that we're reading the correct prop that was passed in
2. Recognize that we can use any name for any prop we send to Student

```javascript
const StudentList = (props) => {
    const studentComponents = props.students.map((student, index) => {
        return (
            <li key={index}>
                <Student
                    id={student.id}
                    name={student.nameData}
                    email={student.emailData}
                    isPresent={student.isPresentData}
                    onUpdate={props.onUpdateStudent}
                ></Student>
            </li>
        );
    });

    // ... return some JSX
```

Here, we're saying that each Student component has a prop named onUpdate. The value of onUpdate will be whatever was passed in props.onUpdateStudent, which we expect to be a reference to our updateStudentData function.

Let's update the PropTypes for Student:

```javascript
Student.propTypes = {
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    email: PropTypes.string.isRequired,
    isPresent: PropTypes.bool,
    onUpdate: PropTypes.func.isRequired
};
```

## Lifting Up State
We've made App manage our student data, and we've passed down some event handlers. Let's make our attendance button do something!

Again, our goal is to make the attendance button in Student update the studentData in App.

**Creating a New onClick Handler in Student**

When we click the attendance button in one Student component, we should update that student's data.

The prop named onUpdate references a function that updates a student's data. We can look at App's updateStudentData function if we need to see the implementation.

```javascript
const Student = (props) => {

    const onAttendanceButtonClick = () => {
        const updatedStudent = {
            id: props.id,
            nameData: props.name,
            emailData: props.email,
            isPresentData: !props.isPresent
        };

        // Invoke the function passed in through the prop named "onUpdate"
        // This function is referenced by the name "updateStudentData" in App
        props.onUpdate(updatedStudent);
    };

    // ... other rendering logic
};
```
- `const onAttendanceButtonClick = () => { ... };`: We're creating an event-handling function named onAttendanceButtonClick. We don't need any details about the event, so we don't list event as a parameter.
- `const updatedStudent = { ... };`: We create a variable, updatedStudent, to hold our updated student data.
- `id: props.id, ... emailData: props.email,`: 	The key-value pairs in this object should match exactly what is required in App's updateStudentData function. In that function, we're looking for the keys id, nameData, emailData, and isPresentData, to match the existing studentData format.
- `isPresentData: !props.isPresent`: When we click on the attendance button, we want to toggle the student's present status. So the value of isPresentData should be the opposite of the current props.isPresent.
- `props.onUpdate(...);`:The value of props.onUpdate is a function reference. We invoke this function using parentheses ().
- `updatedStudent`: 	The function referenced by props.onUpdate ultimately accepts one argument, an updated student object. We can pass in our new updatedStudent object here.

**Attaching onAttendanceButtonClick to the Attendance Button**
We need to attach our function to the attendance button's onClick attribute:
```javascript
const Student = (props) => {

    const onAttendanceButtonClick = () => {
        const updatedStudent = {
            id: props.id,
            nameData: props.name,
            emailData: props.email,
            isPresentData: !props.isPresent
        };

        // Invoke the function passed in through the prop named "onUpdate"
        // This function is referenced by the name "updateStudentData" in App
        props.onUpdate(updatedStudent);
    };

    const nameColor = props.isPresent ? 'green' : 'red';

    return (
        <div>
            <ul>
                <li className={nameColor}>Nickname: {props.name}</li>
                <li>Email: {props.email}</li>
            </ul>
            <button onClick={onAttendanceButtonClick}>Toggle if {props.name} is present</button>
        </div>
    );
};
```