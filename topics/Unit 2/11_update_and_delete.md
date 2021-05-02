# Update and Delete

## Updating an Endpoint
```python
@books_bp.route("/<book_id>", methods=["GET", "PUT"])
def handle_book(book_id):
    book = Book.query.get(book_id)

    if request.method == "GET":
        # ... existing code that returned a dictionary
    elif request.method == "PUT":
        form_data = request.get_json()

        book.title = form_data["title"]
        book.description = form_data["description"]

        db.session.commit()

        return make_response(f"Book #{book.id} successfully updated")
```
This: 
- `methods=["GET", "PUT"]`: routes matching methods now need to be updated to handle PUT reqs.
- Both the GET and PUT actions need to find the Book instance based on book_id, so we'll declare book at the beginning

## Deleting in instance of a Model
Add:
```python
@books_bp.route("/<book_id>", methods=["GET", "PUT", "DELETE"])
#    ..def handle_books()
# ....rest of code
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"Book #{book.id} successfully deleted")
```
