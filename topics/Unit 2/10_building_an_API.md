# Building an API

## Frameworks
Flask
- Documentation: https://flask.palletsprojects.com/en/1.1.x/

Flask is a package with many of its own dependencies, which can quickly make a mess of our system-wide Python installation!
- no Python project is too small to consider using a virtual environment.

## Virtual Env
At the very beginning of a Python project, we will either:
1. Clone the project repo onto our machine, which creates a project folder
2. Create a new, empty project folder

Once we cd into the project folder, we can create a virtual environment.
`$ python3 -m venv venv`

We can activate and deactivate this virutal environment with these commands:
```zsh
### Activate ###
$ source venv/bin/activate
(venv) $
(venv) $ # should see (venv) now

### Deactivate ###
(venv) $ deactivate
$
$ # should stop seeing (venv)
```

Python projects will conventionally record all of their project dependencies in a file named requirements.txt.
e beginning of the project, or after any updates to this file, we install all dependencies with:
`(venv) $ pip install -r requirements.txt`

To update the requirements.txt file, we use this command:
`(venv) $ pip freeze > requirements.txt`
- Because we can use the above command to ask pip to update our requirements.txt file, there's no need to ever open up the file and edit it directly.

## Running, Stopping, and Restarting the Server
Building an API means that we're building a web server. A web server needs to be running in order to be accessible to clients. Running a web server makes it available to respond to HTTP requests at a particular address and port.
- The address can be thought of as like a street address, while the port is more like an apartment number.

**To run a Flask server, we run this command:**
`(venv) $ flask run`
- By default, running Flask servers will be available on localhost:5000. localhost acts as the address and 5000 is the port. They are separated by a colon. Our clients will send HTTP requests to http://localhost:5000.
- localhost is a special name used to refer to the local computer itself. 

In order for us to run terminal commands like git, we'll need to open an additional Terminal window or tab, or stop the server.

**To stop a Flask server:**
Return to the Terminal tab or window that is running the server
Press ctrl + c

## Where Code Goes: Endpoints
The place we put our code that defines endpoints will depend on the project.

One structure:
```
.
├── app
│   ├── models
│   │   └── __init__.py
│   ├── __init__.py
│   └── routes.py
├── README.md
└── requirements.txt
```
- Routes: Inside the app folder, there will be a file named routes.py. The responsibility of this file is to define the endpoints.
- Models: The app/models directory will be responsible for holding our data models.
- The app/__init__.py File: This is the same file we have used to mark a folder as a package.
  - Can be left blank OR given start-up logic.
  - start-up logic is responsible for locating and applying any app configuration, and getting the server ready to receive requests.

**Dev Workflow**
Our modified dev workflow for Flask development may now look like this:
- cd into a project root folder
- Activate a virtual environment
- Check git status
- Start the server
Cycle frequently between:
- Writing code
- Checking git statuses and making git commits
- Debugging with Postman, server logs, VS Code, and more
- Stop the server
- Deactivate the virtual environment

## Flask app build - hello books

## Def Endpoints with Blueprint
**Blueprint is a Flask class that provides a pattern for grouping related routes (endpoints).** Flask will often refer to these routes using the word "view" due to Flask having the potential of sending HTML views. However, we will be sending back JSON.

- See Flask's def of Bliueprint: https://flask.palletsprojects.com/en/1.1.x/api/#flask.Blueprint
- Flask's tutorial on Blueprint: https://flask.palletsprojects.com/en/1.1.x/tutorial/views/
(notes separate from this doc - unit 2 - 10.5)

in `routes.py` add: 
```python
from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)
```

Every time we instantiate a new Blueprint, Flask requires us to register it with app. This is a fancy way to say that we need to tell the app that it should use the endpoints from hello_world_bp for its routing.

In `app/__init__.py`
```python
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    return app
```
## Def an Endpoint
Recall that the responsibility of an endpoint is to:
- Match the HTTP verb and request URL of an HTTP request
- Form an HTTP response to send back to the client

Generic Syntax:
```python
@blueprint_name.route("/endpoint/path/here", methods=["GET"])
def endpoint_name():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body
```

## Models
Model: rep of a single concept relevant to the application.
- Has states and behavior
- Basically a class. 
- A link between DB and code
  - They are typically pieces of data that should be stored in our db. 

(w/ Flask SQLAlcehmy is used. SQLAlchemy is an ORM. Makes a connection from our Python classes (objects) to tables in a database (relations).)

To use models:
1. Create a database.
   1. `psql -U postgres`: get into postgres
   2. CREATE DATABSE <name>
2. Connect Database to Flask
   1. Supply a connection string
   2. `postgresql+psycopg2://postgres:postgres@localhost:5432/REPLACE_THIS_LAST_PART_WITH_DB_NAME`
      1. tells Flask to connect to our db using the psycopg2 package we installed from our requirements.txt.
   3. Configure db in `app/__init__.py`
  ex: 
  ```python
  from flask import Flask
  from flask_sqlalchemy import SQLAlchemy
  from flask_migrate import Migrate
  db = SQLAlchemy()
  migrate = Migrate()

  def create_app(test_config=None):
      app = Flask(__name__)

      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
      app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

      db.init_app(app)
      migrate.init_app(app, db)

      return app
  ```
  This:
  - Imports and sets up the packages SQLAlchemy and Migrate (a companion package to SQLAlchemy)
  - Sets up db and migrate, which are conventional variables that give us access to database operations
  - Configures the app to include two new SQLAlchemy settings
  - We set app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] to False to hide a warning about a feature in SQLAlchemy that we won't be using.
  - We set app.config['SQLALCHEMY_DATABASE_URI'] to the connection string for our database, hello_books_development
  - Connects db and migrate to our Flask app, using the package's recommended syntax
3. Create model file and class
   1. Create subfolder under apps called models
      1. add `__init__` file 
      2. add `model_name` file (e.g. Planet, Book, Etc.)
         1. Models Are Classes That Inherit From db.Model
          ```python
          from app import db


          class Book(db.Model):
              id = db.Column(db.Integer, primary_key=True, autoincrement=True)
              title = db.Column(db.String)
              description = db.Column(db.String)
              __tablename__="books"
          ```
          This:
          - imports db
          - defines a new class.
          - our model inherits from `db.Model`
          - `id = db.Column()`: Instances of Book have an id which maps to a db column. It also has some keyword arguments that allow SQLAlchemy to understand how to fill in the values for new Book instances. 
          - `__tablename__` allows us to set the table to a specific name. 
4. Make models visible to Flask migration helper
   1. in `__init__.py`
      ```python
      def create_app(test_config=None):
          # app = Flask(__name__)
          # ... app is configured with SQLAlchemy settings
          # ... db and migrate are initialized with app

          from app.models.book import Book

          return app
      ```
      **NOTE:** May result in circular import error.
        1.  Generally we prefer to put import statements at the top of our files. However, doing so here would result in an error called a circular import error. There are a number of ways to avoid this error, but by far the most straight-forward way is to place this import inside a function so that it doesn't run until the function gets called.
5. Generate instructions for modifying our database
   1. `(venv) flask db init`: Once we have created our database and configured the connection string, we can do this one-time setup command:
   2. `(venv) $ flask db migrate -m "adds Book model"` We can generate database migrations with the following command. 
      1. **This command should be run every time there's a change to a file in the models folder.**
6. Apply instructions
   1. `(venv) $ flask db upgrade`: apply the generated migrations.

## Creating Endpoints

`from flask import request`: Flask, the framework, will provide all sorts of things to us. One of those things is the request object. The imported request object represents the current HTTP request.
   - Flask's def of Response: https://flask.palletsprojects.com/en/1.1.x/api/#response-objects
   - Flask response quickstart: https://flask.palletsprojects.com/en/1.1.x/quickstart/#about-responses

Example:
```python
from app import db
from app.models.book import Book
from flask import request, Blueprint, make_response

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)
```
This: 
- Import modules for our book module
- import dependencies w/ comma separation
- creates instance of blueprint. used to group routes starting w/`/books`.
- `url_prefix="/books"` : 	A keyword argument. This url_prefix indicates that every endpoint using this Blueprint should be treated like it starts with /books.
  - RESTful!
- `@books_bp.route("", methods=["POST"])`: A decorator that uses the books_bp Blueprint to define an endpoint and accepted HTTP method. 
- `def handle_books:` : executes whenever a request that matches the decorator is received. 
- `db.session` is the database's way of collecting changes that need to be made.
- so committing makes those changes.

After this we must register the app in the `app/__init__.py` file. 
```python
def create_app():
    app = Flask(__name__)
    # ... existing code that did
    # app config...
    # db initialization...
    # migrate initialization...
    # import models...
    # create the models...

    from .routes import books_bp
    app.register_blueprint(books_bp)
    # ... return app
```
Again, these lines make it so that our Blueprint is recognized by our Flask app. We need to do this step each time we make a new Blueprint.