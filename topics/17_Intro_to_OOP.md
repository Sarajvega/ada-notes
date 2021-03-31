
# Intro to OOP

Imperative programming is a programming paradigm that says programmers should solve problems by defining instructions for a computer to follow.

Object-oriented programming is a programming paradigm that is a subset of imperative programming that focuses on how we arrange and operate on data.

## Vocab
- Object-oriented programming: paradigm based on objects which contain state (attributes) and behavior (methods).
- Object: A collection of structured data along with the operations that can be performed on that data. An object is one instance of a class.
- Class: A template or blueprint used to create objects of a specific data type.
- Instance: One particular object of a certain data type/class.
- State:  generic term for the data that an object "knows" at one point in time
- Attribute: A named property of a class. Attributes are used to keep track of state.
- Behavior: A generic term for what an object can "do."
- Method: A function that is defined inside of a class

## OOP
Objects - things the represent ideas as data, hold distinct state and carry out behaviors.

## Defining Classes
Creating a class means to create our own data type and its plans, much like a template, blueprint, or recipe.  
Classes contain: 
- a class name
- attributes - specific piece of data)
- methods - function that describes behavior/action.

## Creating Instances of Classes
The class definition is used to build instances. Instances = single example of a class. 

Example: I'm making an instance of an Album. This instance represents one album, named "Purple Rain."

## State, Behavior, Attributes, and Methods. 
- State is used to refer to all the variables packaged within a class. The collection of attributes attached to an object holds that instance's state. 
- Behavior is used to refer to all the functions packaged within a class.
- Attribute is a specific kind of variable: one defined within a class.
- Method is a specific kind of function: one defined within a class.

What is the diff between behavior and state?
Behavior = actions that objects can do, while state = data or attributes of an obj that hsould be kept. 

## Defining Classes
- Constructor: Method used to create objects.
- `__init__`: Name of method used by Python as the constructor. 
- `self`: conventional name for a parameter that refers to an instance itself. 

Some considerations for making a class:
- Is there a concept that is used frequently in this project?
- Is there a major concept that holds a bunch of data?
- Is there a major concept that has certain behaviors?
- Will defining a class increase the readability?
- Will defining a class organize the code better?

Before we create a class, we should do our best to determine:
- What concept is this class responsible for representing?
- What is a descriptive name for this class?
- The name should be singular, e.g., Album not Albums


Define (instantiate) by:
```python
class ClassName:
    pass
```

## The Constructor
To create object instances that have a customized initial state:
```python
class ClassName:

    def __init__(self):
        pass
```
the `__init__` method should always take one parameter. Additional parameters in the constructor mean that we expect additional arguments whenever we instantiate a new object.

There is a common initialization pattern in OOP where we do the following:
1. Define the parameters needed for every instance of a class
2. Use those parameters to make instance attributes in the constructor method

Example:
```python
class Album:

    def __init__(self, title, release_date, tracks):
        self.title = title
        self.release_date = release_date
        self.track_list = tracks
```

Attributes are like variables but they can be accessed via `self`. 

To assign values to an attribute:
`self.attribute_name = value_expression` Which utilizes the dot operator.

Example:
```python
class Album:

    def __init__(self):
        self.title = "Purple Rain"
        print(f"We can also read the value of the title attribute")
        print(f"by writing self.title: {self.title}")
```

## Creating Instances
An instance is a concrete example of a class. Each instance has its own state, stored in its attributes, with its own unique ID (most of the time). `ExampleClassName()` creates an instance of a class.

The constructor inside of the class determines what arguments are needed whenever we instantiate the class.

We can read and use an instance of a class just like any other variable, including using the `type()` function: `print(type(purple_rain))` which would return `<class '__main__.Album'>` which indicates that it's of class Album (located inside a namespace named __main__. 

Example: Return the second trip of this instance.
```python
class Driver:
    def __init__(self, trips):
        self.trips = trips

def get_specific_second_trip():
    new_driver = Driver(["trip 1","trip 2","trip 3"])
    return new_driver.trips[1]
```

We can re-assign the values of attributes on instances. We do so with the assignment operator: `example_instance.attribute_name = new_attribute_value`

To use multiple instances effectively, we must remember that each instance keeps track of its own values for the attributes defined by the class. The values of these attributes for each instance makes up that instance's state. The state of each instance occupies its own place in memory, separate from any other instance.

## Instance Methods
```python
class ExampleClassName:

    def example_instance_method(self):
        pass
```

Methods: Function inside of a class.
Instance methods: behaviors that instances of classes can do. They must be insdie the class definition and first parameter must be `self` and we can have as many as we'd like after that. 

Example:
```python
class Album:

    def __init__(self, title, release_date, tracks):
        self.title = title
        self.release_date = release_date
        self.track_list = tracks

    def get_audio_data(self, track_index):
        if 0 < track_index <= len(self.track_list):
            return self.track_list[track_index - 1]
        else:
            return "Invalid track"****
```
The instance method `get_audio_data` takes an additional parameter `track_index`. We must pass in an argument for track_index. track_index represents the index track we want audio data from.

Inside the `get_audio_data` method, we use the attribute `self.track_list` and the argument `track_index` when we call this method. We assume `self.track_list` is a list, and we use it in a conditional statement. We use `track_index` in the line return `self.track_list[track_index - 1]`.

## Calling Instance Methods
`name_of_instance.name_of_instance_method()` --> We never specify that the first parameter is self.

Example:
```python
class Driver:

    def __init__(self, trips):
        self.trips = trips

    def get_number_of_trips(self):
        return len(self.trips)

    def get_avg_rating(self):
        total_rating = 0
        for trip_rating in self.trips:
            total_rating += trip_rating

        avg_rating = total_rating / self.get_number_of_trips()
        return avg_rating
```

## Testing Objects
- Unit Test: Scripts designed to test the performance of a single function
- Arrange: Top section of a test designed to include things to arrange or set up like creating variables or instances.
- Act: A statement that is true or calls the method that we are testing
- Assert: Statements that verify whether the method being tested behaves as expected
- Import: A keyword that makes code in one module accessible in another

## Unit Tests Verify State and Behavior
Unit tests should focus on two questions:
1. For all relevant cases, are the attributes of an instance correct?
2. For all relevant cases, do the methods on an instance work as expected?

**Example:**
Scarlet is making a ride share app, which has three classes, Driver, Passenger, and Trip. Every driver has a name, VIN, and list of trips they've driven. Every driver can calculate their average rating and add a new trip.

Scarlet will likely test the Driver class's initial state by checking:
- Initial value of name
- Initial value of vin
- Initial value of trips

She can test an instance method named calculate_avg_rating by checking:
- Return value of calculate_avg_rating for a Driver instance with 2+ trips
- Return value of calculate_avg_rating for a Driver instance with 1 trip
- Return value of calculate_avg_rating for a Driver instance with 0 trips

She can test an instance method named add_trip by checking:
- When passing a valid new_trip into the method...
  - Return value of add_trip
  - The state of the trips attribute should change
    - The length is increased
    - The trips list contains the new_trip
- When passing an invalid new_trip into the method...
  - Return value of add_trip
  - The state of the trips attribute should not change
    - The length is the same
    - The trips list does not contain the new_trip

**Example 2:**
Imagine an app that manages the customers and orders of a grocery store. There are two classes, Customer and Order.

Each Customer has:
- name
- email_address

Each Order has:
- products
- customer
- add_product method
- remove_product method


From the given project description, make a list of all relevant test cases. Make up reasonable assumptions about the logic of add_product and remove_product, particularly around the edge cases.

Answer:
You can create an instance of Customer with Customer() and verify the valid name and email_address initial values.
You can create an Order and verify the initial values of:
- products
- customer
You can test add_product by adding a product and
- verifying that the length increases
- verifying that the added product shows up in products
You can test remove_product by
- adding a product and removing it and verifying that the length decreases and the product no longer appears in products.
- trying to remove a product which is not in the list and verifying that the method performs as you expect (raising an error for example).


## Back to Pytest

Used syntax:
```python
def test_some_example_test_case():
    # Arrange
    # Create an instance of the class
    # and set up any other necessary test variables

    # Act
    # Call the method that we are testing

    # Assert
    # Verify all relevant return values and state changes
```

Example for Scarlet's app:
```python
def test_new_valid_driver():
    name = "Batman"
    vin = "NAN4NAN4NA"
    trip_a = Trip()
    trip_b = Trip()
    trips = [trip_a, trip_b]

    batman = Driver(name=name, vin=vin, trips=trips)

    assert batman.name == name
    assert batman.vin == vin
    assert len(batman.trips) == 2
    assert trip_a in batman.trips
    assert trip_b in batman.trips
```

In our Arrange step, we set up the name, vin, trip_a, trip_b, and trips variables
In our Act step, we instantiate batman
In our Assert step, we check:
1. batman's name attr
2. batman's vin attr
3. The length of batman's trips
4. The contents of batman's trips

We can test the calculate_avg_rating instance method with the following test:
```python
def test_driver_calculate_avg_rating():
    good_trip = Trip(rating=4)
    bad_trip = Trip(rating=2)
    batman = Driver(trips=[good_trip, bad_trip])

    avg_rating = batman.calculate_avg_rating()

    assert avg_rating == 3

def test_driver_calculate_avg_rating_is_zero_with_no_trips():
    batman = Driver(trips=[])

    avg_rating = batman.calculate_avg_rating()

    assert avg_rating == 0
```
We should notice:
1. There are two tests for this one instance method
   1. The first checks the average rating between two trips
   2. The second checks what happens if there are zero trips
2. In our Arrange step, we must make an instance of Driver
   1. The tests did not pass in a name or vin because they are optional and not relevant to the test
3. In our Act step, we call the instance method we're testing

## Projects with Many Files
- Module: Any .py file that contains functions, classes, variables, and/or other runnable code. Any python file can be called a module. 
- Package: A collection of modules. Contains a filed names `__init__.py` which can be empty.

It's conventional to place each class definition in its own .py file. But then how does one class find out about another that it needs to use?

Here's a common project structure:
```python
project_name/
├── README.md
├── requirements.txt
├── main.py
├── project_package_name
│   ├── __init__.py
│   ├── example_class_a.py
│   └── example_class_b.py
└── tests
    ├── __init__.py
    ├── example_class_a_test.py
    └── example_class_b_test.py
```
Note:
- Project Root: Same name as proj, folder holds all the files realted to the currect project.
- Files such as README.md, requirements.txt, and any virtual environment folders
- In the main.py file (also located in the project root) we can put just enough code to start up the rest of our project. Run with `python3 main.py`
- package folder: Under the project root, single folder to contain all of our project classes, one class per .py file.
- Tests live in tests folder. 

## Packages and Modules
```python3
ride-share-app/
├── README.md
├── requirements.txt
├── main.py
├── ride_share_app
│   ├── __init__.py
│   ├── driver.py
│   └── passenger.py
└── tests
    ├── __init__.py
    ├── driver_test.py
    └── passenger_test.py
```

Access passenger module w/ `.passenger` or `ride_share_app.passenger` depending on relative location. 

## Importing
We must import any resources that we need from another module before we can use them in the current module, otherwise Python will report a NameError.

1. Importing a module by name
   1. `import random`
2. Importing a package module by full name
   1. To import the driver module from the ride_share_app package example above: `import raide_share_app.driver`
   2. `driver = ride_share_app.driver.Driver()` loos in the app package for the driver module to find the Driver identifier and calls it w/ (). Then that new instance is stored in driver. 
3. Importing module identifiers using relative names
   1. use `from .driver import Driver` to import the driver module to the passengar module
   2. They are in the same folder. 
      1. `from` names the module from which we want to import
      2. `.` tells python to look for the module in the folder containing the current file
      3. `import` names the indetifier we want python to import. 
   3. How do we import a module that is inside a different folder, but within the same package?
      1. `..driver` - Goes up two folders. 

Importing duplicate named classes
```python
from module_two import UsefulClass as UsefulClassTwo
from module_one import UsefulClass as UsefulClassOne
```

## Debugging Imports
1. `ModuleNotFoundError` = There's an import statement that can't find the specified module
   1. Check the `from` part of the import
2. `ImportError` = There's an import statement that can't find what to import within the module.
   1. Double-check that the module defines what we're trying to import with the exact same name
   2. The name should refer to a top-level class, function, or variable defined in the module
