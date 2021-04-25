# Intermediate SQL

## Database Relationships
- Relational databases let us establish relationships btwn tables. 

## Vocab
- One to many relationship: a relationship btwn two tables in a database where one record in a table can be assocaited w/ one or more records.
- Many to many relationship: A relationship btwn two tables in a db where one record can relate to many records in the other table.
- One to One relationship: Two tables in a db were one record relates to one record. 
- Join table: table used to connect two other tables
- Entity relationship diagram: a graphical representation of data models using entities, their attributes and relationship between those entities. 

## ERD Diagrams
- To make a database schema, or design, easier to understand we use a type of diagram known as an entity relationship diagram (ERD).
- An ERD diagram consists of rectangles, each one representing a table in the database. Within each rectangle, we list each column name. We can choose to include additional information about each field, such as its data type, or whether it has any special constraints, like being the primary key.

## One-to-One
- each record in one table, Table A, can relate to at most one record in another, Table B, and each record in Table B can relate to at most one record in Table A. 

## One-to-Many
- each record in one table can relate to zero, one or many records in the other table. We often call this type of relationship a has-many relationship.

## Many-to-Many
- There are scenarios where each row in one table is related to many rows in another, and the reverse is also true. This is a many to many relationship.
- building a many to many relationship requires a table called a join table.

## Establishing Relationships
- Foreign Key: A col in a db that comes from another table, whos val is either a primary key/unique key.

## Tables w Foreign Keys
```SQL
CREATE TABLE books (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  title VARCHAR(32),
  description TEXT,
  isbn VARCHAR(32),
  author_id INT,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);
```
- books has a col `author_id` which has the constraint of `FOREIGN KEY (author_id) REFERENCES authors(id)`, making it a foreign key.
  - Notice the comma preceding the statement...this tells Postgres that every author_id must ref an existing id in authors table.

If we have:
| id   |	first_name  |	last_name |	bio |
|------|----------------|-------------|-----|
|  14  |  Michelle      |  Obama      |	Becoming is the memoir of former First Lady of the United States Michelle Oba...|

We can create a book related by:
```SQL
INSERT INTO books (title, description, isbn, author_id)
VALUES ('Becoming', 'Becoming is the memoir of...', '978-3-16-148410-0', 14);
```
- Now this book has an `author_id` of 14 which matches Michelle Obama's `id` field. They are now related.
- If you wanted to delete Michelle, Postgres will thrown and error because the book `Becoming` is referenced to her author entry.

**NOTE: The Foreign Key Must Exist In The Referenced Table**
-  any rows inserted into the table must include a value for that column and that value must exist in the referenced table.
-  This prevents an entry in one table from referencing a row which does not exist in the other table.

## Join Tables
```SQL
CREATE TABLE books_genres (
  book_id INT,
  FOREIGN KEY (book_id) REFERENCES books(id),
  genre_id INT,
  FOREIGN KEY (genre_id) REFERENCES genres(id),
  PRIMARY KEY (book_id, genre_id)
);
```
- table has no `id` field as the primary key.
- table has two foreign key fields
- `books_genres` table uses a combo of 2 columns as primary keys
  - this means no two rows can exist w/identical `book_id` and `genre_id` vals.
- We name the join table `books_genres`.

## Two Col Primary Keys
- two-field primary key has an advantage.
- Using the combination of book_id and genre_id prevents duplicate entries. 
- No book listed in same genre twice then.

## DB Joins
- Join: SQL operation which combines cols from one or more tables in relational db.

## SELECT w/ Join
```SQL
SELECT field1, field2, field3, ...
FROM table_name_a
INNER JOIN table_name_b
  ON condition
/* Optional WHERE clause */
```

We can use this style of query to retrieve the combined information from both the books and authors tables.
```SQL
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors
  ON books.author_id = authors.id;
```
- Return all the rows in both tables w/matching keys.
- INNER JOIN combines books and authors tables by comparing author_id to id in authors table. 
- From combo data we retireve title of each book, first and last name of each book's author. 

To retrieve all books written by one person, use `WHERE`:
```SQL
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors
  ON books.author_id = authors.id
WHERE authors.first_name = 'Kaja' and
  authors.last_name = 'Howell';
```

Another example of a one to many relationship:
```SQL
SELECT clients.name, rentals.check_in_date
FROM clients
INNER JOIN rentals
  ON rentals.client_id = clients.id;
```
- Here, the client's id is attached to the client's rental information
- We can grab all clients and their check in dates using the above query.

**table_name.column_name Syntax**
- this is optional but explicitly referring to the table can help remind us of the data source. 

## JOIN with Many-to-Many relationships
- Many to many relationships require 3 tables. (books, book_genres, genres)
- If we want to retrieve a list of all books and the genres in which they are classified, we need to involve three tables. How can we do this?
- use multiple `INNER JOIN`s 

```SQL
SELECT books.title, genres.name
FROM books
INNER JOIN books_genres
  ON books_genres.book_id = books.id
INNER JOIN genres
  ON books_genres.genre_id = genres.id;
```
- This connects all tables via ids!

``SQL
SELECT 

```