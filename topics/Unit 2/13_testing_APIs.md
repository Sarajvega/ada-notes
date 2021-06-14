# Testing APIs

## Environments
In the context of local project development and testing, we will commonly use two environments according to the following pattern:
1. A development environment dedicated to rapid development
   1. Dedicated to rapid development. Things will change often as we work on the project
2. A testing environment dedicated to holding test data
   1. Dedicated to running test suites

## Environment Variables
Environment variables are strings that hold data outside of our application code. The environments we use provide ways to set these kinds of values.

Some examples include:
- The location of a database (a connection string)
- Locations of other resources (such as other services that are part of a larger software system)
- Various configurations about how to run the app, such as debugging mode
- API keys

## Managing Env variables
- Env vars useful for storing sensitive and secret data. 
  - because they are held outside our code/don't get checked into source control. 
    - What is source control? 
      - Committing to a repo. 
- we want to avoid committing environment variables to source control, where nefarious individuals could steal our credentials!

## dotenv and the Test Database
The python-dotenv package (often referred to as simply "dotenv") is a popular, well-used tool for managing environment variables.

We should ensure that python-dotenv is installed by either:
- Checking our requirements.txt and confirming python-dotenv is already listed, or
- Installing it with (venv) $ pip install python-dotenv
  - In this case we should also update our requirements.txt by running (venv) $ pip freeze > requirements.txt

Create a .env file in your root:
`$ touch .env`
- The python-dotenv package expects to find a file named exactly .env in the project root directory.
- .env files folds the environment variables. Stuff that you wouldn't want the user to see. Not uncommon to have some mail usernames / passwords there for when you need to send emails.

Make Git ignore that file:
- There is sensitive info in our .env file that we don't want to share.
- `.gitignore` file tells git to never track whats inside.
- To make Git ignore our .env file, we open .gitignore in our text editor and add .env to the file on its own line.

## Populate the Env Vars
`VARIABLE_NAME=variable value`
- then make a test data base.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.book import Book

    from .routes import books_bp
    app.register_blueprint(books_bp)

    return app
```
- The python-dotenv package specifies to import the package

## Fixtures
Resource here: https://docs.pytest.org/en/stable/fixture.html

When testing Flask APIs we need to:
- Tell our sever to run in test mode
- create a way to issue requests to our server from w/in our tests.
- Share the above set up across mult tests.

Pytest does all that!

- Fixture: Shared code used to perform setup and cleanup for tests.
- Dependency: In this context, a fixture listed as one of the parameters in a test function.
- Dependency Injection: A way for code to explicitly declare and receive the resources it needs to run successfully.

create a fixture w/ `@pytest.fixture` decorator.

Create a dummy file to play with:
```python
import pytest

@pytest.fixture
def empty_list():
    return []

def test_len_of_empty_list(empty_list):
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0
```
- import the pytest module 
- `@pytest.fixture`: Applies the fixture decorator to the empty_list function. pytest will be able to use empty_list as a fixture in subsequent tests.

You should see all tests pass.
- test_len_of_empty_list asserts: 
  - value in the empty_list parameter must be an instance of list.
  - length of the value in empty_list must be zero.

But how did a value get passed in to the the test?
- pytest matches the name of the parameter empty_list to the function empty_list that we registered as a fixture with @pytest.fixture. 
- before pytest runs a test, it looks at the parameters the test declares and tries to find a fixture with a matching name.
- If a matching fixture is found, it is run, and the return value is used as the parameter value. 
- if no matching fixture is found, pytest will report an error during the setup of that test. 

## Fixtures w/Dependencies
Add this:
```python
@pytest.fixture
def one_item(empty_list):
    empty_list.append("item")
    return empty_list

def test_len_of_unary_list(one_item):
    assert isinstance(one_item, list)
    assert len(one_item) == 1
    assert one_item[0] == "item"
```
- one_item reg's as a fixture
- `empty_list`: The parameter to one_item which matches the name of the previously registered empty_list fixture. pytest will call the empty_list fixture, and pass the result in as this parameter whenever this fixture itself is used.

Let's examine what this new test is doing.

We see that the test_len_of_unary_list asserts a few things about the one_item parameter. First, it must be an instance of list. Second, the length of the value in one_item must be one. Finally, it checks that the string "item" is in index zero. All three assertions must have been true.

pytest performed the same parameter name matching step that it did for test_len_of_empty_list. It found the one_item parameter and matched it to the fixture with the same name.

When it went to run that fixture it saw that the one_item fixture itself had a parameter empty_list. It once more checked for a matching fixture, and ran it. The result of empty_list (an empty list) was supplied as the parameter to one_item, which inserted the "item" value and returned the result. This result became the input to test_len_of_unary_list.

As before, if no matching fixture is found at any point in running the fixtures, pytest will report an error during the setup of the test it was trying to run.

## Fixtures w/Cleanup
Fixtures can keep setups and cleanup code together, to ensure that if the setup runs, so will the cleanup. 

Add:
```python
class FancyObject:
    def __init__(self):
        self.fancy = True
        print(f"\nFancyObject: {self.fancy}")

    def or_is_it(self):
        self.fancy = not self.fancy

    def cleanup(self):
        print(f"\ncleanup: {self.fancy}")

@pytest.fixture
def so_fancy():
    fancy_object = FancyObject()

    yield fancy_object

    fancy_object.cleanup()

def test_so_fancy(so_fancy):
    assert so_fancy.fancy
    so_fancy.or_is_it()
    assert not so_fancy.fancy
```
- `class FancyObject:...`: Declares a class that has "setup" code (in __init__), and "cleanup" code (in cleanup). The setup and cleanup code is represented by printing out some messages.
- `@pytest.fixture` registers the following function so_fancy as a fixture
- `yield fancy_object`: halts the so_fancy function returning the fancy_object instance.
- `fancy_object.cleanup()`:This code wil run when the so_fancy function resumes. It will perform the "cleanup" code for this instance.

## Test Setup
```
(venv) $ mkdir tests
(venv) $ touch tests/__init__.py tests/conftest.py tests/test_routes.py
```

Then in conftest.py:
```python
import pytest
from app import create_app
from app import db


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
    # this fixture depends on the fixture above
```
- `@pytest.fixture` creats a fixture named app
- `{"TESTING": True}`: we're passing in a dictionary to represent a "test config" object. The current implementation of create_app() in app/__init__.py uses this argument only to check if it's truthy.
- `with app.app_context()`: following code should have an application context. This lets various functionality in Flask determine what the current running app is. This is particularly important when accessing the database associated with the app.
- `with app....: db.drop_all()`: After the test runs, this code specifies that we should drop all of the tables, deleting any data that was created during the test.
- `def client(app):` fixture = client requests existing app
- `return app.test_client()`: make a test client, which is an object able to simulate a client making HTTP requests.

## Cleint Fixture.
