# Handling Forms

## Controlled Forms

To handle clicks, we can expect:
1. We will need a button with an onClick event handler.
2. If the button is inside a presentational component, it should invoke a function that updates another component's state. This function is usually passed through props.
However, there are a variety of other form input fields, and working with them may require observing new patterns.

**More About input Elements**
Each `<input>` element type (such as text, checkbox, radio button, or number field) has its own set of attributes and logic to work with. 
- Text: value: Contains the current value of the text entered into the text field.
- Checkbox: checked: Boolean which indicates whether the checkbox is currently checked.
- Radio Button: checked: Boolean which indicates whether the radio button is currently checked.
- Number: value: Contains the current value of the number entered into the input.

When an `<input>` element is changed, it emits an event specifically named "change". This emitted "change" event is an object that contains all details about the event.

**The `<form>` Element**

The `<form>` element itself is unique. This element usually contains one or more `<input>` elements.
`<form>`s have default HTML behavior. If the `<form>` element ever receives an event called "submit", it will bundle all of the form data together (looking through the `<input>` elements), and then send an HTTP request.
This default behavior can be changed by setting either the `<form>` tag's method and/or action attributes, or with JavaScript.

**Controlled Forms Control `<input>` Values**

[Controlled components](https://reactjs.org/docs/forms.html#controlled-components) follow a design pattern that states that a form's values should be controlled by the component's state, not by user interaction.

Instead, user interaction will update the component's state, which will in turn be reflected in the form input's value.

Therefore, we can summarize controlled forms as having these elements:
- The component holds state
- For every input, its value comes from the component's state
- For every input, every time it handles an event, it updates the component's state

**The Alternative Requires Multiple Updates**

Without using controlled components, user interaction would need to update the component's state and the `<input>`'s state. Surprisingly, this can get out of sync really quickly! 

**Syntax Example: Generic Form**

```javascript
import { useState } from 'react';

const CityNameInput = () => {
    const [cityName, setCityName] = useState('Seattle');

    return (
        <section>
            <h2>{cityName}</h2>
            <input type="text" />
        </section>
    );
};
```
In order to complete this form, we will do the following:
1. Ensure that our text input field's value comes from the component's state
2. Ensure that when our text input field changes, it updates the component's state

```javascript
import { useState } from 'react';

const CityNameInput = () => {
    const [cityName, setCityName] = useState('Seattle');

    const renameCity = (changeEvent) => {
        console.log('Details about the element that fired the event:', changeEvent.target);
        console.log('The value of that element:', changeEvent.target.value);
        setCityName(changeEvent.target.value);
    };

    return (
        <section>
            <h2>{cityName}</h2>
            <input type="text" value={cityName} onChange={renameCity} />
        </section>
    );
};
```
- Because component's re-render every time state updates, we can trust that the appearance of the text field will always be aligned with state.
- we need to create our event handler for the "change" event that will update the component state.
  -  we added the attribute onChange to our text field. Then, we created an event handler function called renameCity.
  - renameCity takes in one argument, changeEvent, which we expect to be information about the event that triggered our event handler.
  - every event-handling function is automatically passed an [Event object](https://developer.mozilla.org/en-US/docs/Web/API/Event), whether we use it or not!
- Our goal is to update our cityName piece of state to whatever value is in the text field. To achieve this, we use our update function, setCityName, and pass in changeEvent.target.value.

**Extended Example: The Attendance App**

Sofia is developing some new features to her attendance app. She wants to be able to add a new student to her class whenever she wants!

Sofia's app currently has the following components:
- An App component, responsible for managing all the student data

```javascript
import { useState } from 'react';
import StudentList from './components/StudentList';

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

    return (
        <main>
            <h1>Attendance</h1>
            <StudentList
                students={studentData}
                onUpdateStudent={updateStudentData}
                ></StudentList>
        </main>
    );
}

export default App;
```

- A StudentList component, responsible for displaying a list of students
```javascript
import './StudentList.css';
import PropTypes from 'prop-types';
import Student from './Student';

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
        id: PropTypes.number.isRequired,
        nameData: PropTypes.string.isRequired,
        emailData: PropTypes.string.isRequired,
        isPresentData: PropTypes.bool
    })),
    onUpdateStudent: PropTypes.func
};

export default StudentList;
```

- A Student component, responsible for displaying the details of one student. It contains a button that toggles whether the student is present or not.

```javascript
import PropTypes from 'prop-types';
import './Student.css';

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
    }

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

Student.propTypes = {
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    email: PropTypes.string.isRequired,
    isPresent: PropTypes.bool,
    onUpdate: PropTypes.func.isRequired
};

export default Student;
```

Sofia is putting her new student form into its own component: NewStudentForm.
Each new student should have a name and an email. Her form contains one text input field for name, one for email, and a final submit button.
```javascript
const NewStudentForm = () => {

    return (
        <form>
            <div>
                <label htmlFor="fullName">Name:</label>
                <input name="fullName" />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input name="email" />
            </div>
            <input
                type="submit"
                value="Add Student" />
        </form>
    );
};

export default NewStudentForm;
```
Recall that the steps for creating a controlled form are:
1. Ensure that our text input field's value comes from the component's state.
2. Ensure that when our text input field changes, it updates the component's state.

Sofia will:
1. Create a new piece of state to hold all of her form data, and make all input values read from state.
2. Create an event handler for each input field. Each event handler will update state.

**New Piece of State: An Object of formFields**

Sofia needs to introduce state into the NewStudentForm component.
Her vision is that formFields will be an easy, nice way to organize the different form fields. By default, a new student's name and email should be blank. The initial state of formFields should be:

Therefore, introducing this new piece of state will look like:
```javascript
import { useState } from 'react';

const NewStudentForm = () => {

    const [formFields, setFormFields] = useState({
        name: '',
        email: ''
    });
```

Now she needs to make the input fields read from this state. Since formFields is an object, she can use dot notation to access the name and email values from the object stored in state.

```javascript
    return (
        <form>
            <div>
                <label htmlFor="fullName">Name:</label>
                <input
                    name="fullName"
                    value={formFields.name} />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input
                    name="email"
                    value={formFields.email} />
            </div>
            <input
                type="submit"
                value="Add Student" />
        </form>
    );
```

**Event Handling To Update formFields**

She can create two event handlers, onNameChange and onEmailChange. These event handlers need to do two things:
1. Read the current value inside the input field
2. Update state to that current value

```javascript
 const onNameChange = (event) => {
        setFormFields({
            ...formFields,
            name: event.target.value
        })
    };

    const onEmailChange = (event) => {
        setFormFields({
            ...formFields,
            email: event.target.value
        })
    };
```
Sofia uses spread syntax  for a quick way to clone the original formFields object. Each event handler should add a specific key-value pair. onNameChange adds the key-value pair name: event.target.value, while onEmailChange adds email: event.target.value.

**Cloning the State Object Lets React See the Change**
> Recall that when Sofia modified the student data to update a student's isPresentData, she had to copy the entire array of student data, replacing only the student value whose presence was updated. This was necessary so that React would notice that the array reference changed, meaning the state had changed, causing the control to be re-rendered. Sofia must do the same thing here. If she doesn't clone the current state to get a new object, React won't notice that the state has changed, and won't re-render the component.

```javascript
    return (
        <form>
            <div>
                <label htmlFor="fullName">Name:</label>
                <input
                    name="fullName"
                    value={formFields.name}
                    onChange={onNameChange} />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input name="email"
                    value={formFields.email}
                    onChange={onEmailChange} />
            </div>
            <input
                type="submit"
                value="Add Student" />
        </form>
    );
```

# Submitting Forms
he NewStudentForm component is all well and good. It follows the controlled component pattern, so its state is in sync with the input fields.

However, all student data is managed in the App component. Our new student form doesn't actually add a student!

To handle form submissions, and bring the data to the App component, we need to lift state up.

**Sofia's goal is to get the data from the NewStudentForm up to the App component.**

The App component is already the single source of truth for her student data, so the remaining steps of her plan are:
1. Pass down event handlers from App to the NewStudentForm
2. Configure the form submission in NewStudentForm to lift state up

## Passing Down New Student Handlers
Sofia starts by making a method in App that adds a new student to the student data:
```javascript
    const addStudentData = newStudent => {
        // Duplicate the student list
        const newStudentList = [...studentData];

        // Logic to generate the next valid student ID
        const nextId = Math.max(...newStudentList.map(student => student.id)) + 1;

        newStudentList.push({
            id: nextId,
            nameData: newStudent.nameData,
            emailData: newStudent.emailData,
            isPresentData: false,
        });

        setStudentData(newStudentList);
    };
```

Sofia chose to implement addStudentData this way:
1. The function receives a new student object, newStudent.
2. She duplicates the studentData array into newStudentList, which will help React detect the change to the list of students.
3. She generates a new ID number, nextId.
   1. [Math.max](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max) expects a variable number of numeric arguments, not a single array. Sofia spreads the array generated by mapping the student list to their IDs to match this expectation. The next ID is then one more than the max from this list.
4. She pushes a new object into newStudentList. The shape of this object matches the other objects in studentData.
5. The newStudentList now contains an object with the newStudent data. She updates studentData in state with setStudentData.

Now, Sofia needs to actually use her new function. She passes it into an instance of NewStudentForm, through a new prop named addStudentCallback.
```javascript
    return (
        <main>
            <h1>Attendance</h1>
            <StudentList
                students={studentData}
                onUpdateStudent={updateStudentData}
            ></StudentList>
            <NewStudentForm
                addStudentCallback={addStudentData}
            ></NewStudentForm>
        </main>
    );

```
Sofia updates the PropTypes of NewStudentForm to now anticipate this prop:
```javascript
import PropTypes from 'prop-types';

const NewStudentForm = (props) => {
    // ...
};

NewStudentForm.propTypes = {
    addStudentCallback: PropTypes.func.isRequired
};
```

Sofia's next step is to get NewStudentForm to call the supplied addStudentCallback prop when the form submits.

She starts by creating a new event-handler function, onFormSubmit.
And she sets it as the handler for the onSubmit event of the control's form.

onFormSubmit is being used as an event handler. This means that an Event object will be passed in as the first parameter, which Sofia has named event. Since onFormSubmit is registered for onSubmit, the object in event will represent the submit event, which if left alone will allow the form's default submit behavior to occur!

With this in mind, Sofia writes the following implementation for onFormSubmit:

```javascript
    const onFormSubmit = (event) => {
        event.preventDefault();

        props.addStudentCallback({
            nameData: formFields.name,
            emailData: formFields.email
        });

        setFormFields({
            name: '',
            email: '',
        });
    };
```

Her implementation of onFormSubmit works like this:
1. She uses the passed in event object and calls event.preventDefault(). This prevents the unwanted default behavior of HTML forms.
2. She invokes the addStudentCallback function, which was passed in as part of the props, with props.addStudentCallback(). This prop was passed in by App, and holds a reference to App's addStudentData function.
3. She knows that props.addStudentCallback (really, App's addStudentData function) receives an object, newStudent. She knows that this object should have the keys nameData and emailData. She passes in an object literal, where the keys are nameData and emailData, with the values read from the formFields state.
4. She resets the form by updating the members of formFields to empty strings.


**Prevent the Form's Default Behavior**
> HTML forms have default behavior: when a form receives a "submit" event, it will make an HTTP request. This creates an effect where our web app reloads every time we submit a form! Be sure to include event.preventDefault(); in any form submission event handler.