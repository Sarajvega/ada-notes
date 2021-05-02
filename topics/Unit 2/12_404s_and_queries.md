# 404's and Queries

## Get a missing book
This feature is a variation on our existing endpoint that reads a record, but it uses an invalid id!
We want to inform the client that the record was not found. The most appropriate response status code is 404 Not Found. 

Here's how we fetch a single book:
```python
@books_bp.route("/<book_id>", methods=["GET"], strict_slashes=False)
def get_single_book(book_id):
    # try to grab book w/ specific id
    book = Book.query.get(book_id)

    if book:
        return{
            "id": book.id,
            "title":book.title
        }, 200

    return{
        "message" : "Book not found",
        "success" : False,
    }, 404
```
**Note:** when `Model.query.get(primary_key)` (what we used above) doesn't find a matching record, it returns None!

Let's modify our endpoint code to report a not found status when trying to GET a book.
```python
@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)

    if request.method == "GET":
        if book is None:
            return make_response("", 404)
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    # ... existing code for updating a single book
    # ... existing code for deleting a single book
```
This:
- `if book is None`: This checks if Book.query.get(book_id) returned None because there was no matching book.
- Sends back empty string as response.

Futher simplify by checking book object before taking a look at the request method:
```python
@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return make_response("", 404)

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }
    # ... existing code for updating a single book
    # ... existing code for deleting a single book
```

## More about Queries
Resources: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records

## Filter by:
`filter_by()`: method which filters our search query.
- Give keyword args to describte the attribute and val on which we're filtering. 
Example: `Book.query.filter_by(title="Fictional Book Title")`. 

## Limit
We can limit the number of results in our queries by using limit(). Consider this example that gets the first 100 Book records.
`Book.query.limit(100).all()`.

## Query Params
Query params provide extra information to an HTTP request.
Common uses for query params include:
- Sorting and filtering search results\
- Limiting the amount of data that comes back
**single param**:
`https://my-beautiful.site/search?category=novels`
- everything after the ? is a query string. 
**multiple query param pairs**:
`https://my-beautiful.site/search?category=novels&minimum_pages=800&maximum_pages=8000`
- utilize the `&`

## URL encoding
- characters, like spaces, colons :, or commas ,, aren't valid in URLs.
- `https://my-beautiful.site/search?name=Hand-crafted%20exclusive%3A%20finest%20tote%20bag%21`
  - (space) = %20
  - : = %3A
  - ! = %21

## Read Params from a Request
Get any query param w:
`query_param_value = request.args.get(query_param_key)`

## Finding Books by Title
```python
@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        # this code replaces the previous query all code
        title_query = request.args.get("title")
        if title_query:
            books = Book.query.filter_by(title=title_query)
        else:
            books = Book.query.all()
        # end of the new code

        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })

        return jsonify(books_response)
    # ... existing code for creating a new book
```
- `title_query =`: stores result of looking for the title query param in the var. 
- `... = request.args.get("title")`: Try to get a query param called title from the request. 
- `... = Book.query.filter_by( ... )`: If we got a query param, we will make a filter_by call to filter the results.
- `title=title_query`: Filter the book query results to those whose titles match the query param
- `... = Book.query.all()`: If we didn't get a query param, get all the books as before

