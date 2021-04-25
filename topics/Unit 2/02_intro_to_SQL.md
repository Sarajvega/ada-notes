# Intro to SQL

## Vocab
- Database: Orghanized collection of stored and persisted data
- SQL: A query lang specifically designed to talk to relational databases
- Postgres: a specific relational database
- Data entity: a single concept that needs to be stored in a table and database. 
- Primary key: attribute dedicated to being a unique identified for each row in a table 

## Intro to Relational Databases
Data is temp stored on a machine or saved and persisted on a machine.
- persisted = state that outlives the process which created it. 

## SQL Communicates with Relational Databases
- dbs stored on any compatible machine.
- SQL = declarative programming lang specifically designed to talk to relational databses. 
- Declarative programming lang = use the lang to express what we would like to have done byt not how to do it. (We don't tell it how to iterate over table).
- Imperative programming lang = we tell it how to do tasks.

## Relational db's
Relational db's = data as tables.
Tables = one entity.
Columnss = attributes and rows = records.

Examples of relational db's:
- MySQL
- PostgreSQL
- SQLite
- Microsoft SQL Server
- Microsoft Azure SQL Database
- Apache Hive
- MariaDB
- Oracle

PostgreSQL, also known as Postgres (and often seen as psql), is a free and open-source relational database management system.

## Parts of a db
- Can store many db entities (Borrower, Lender, Loan, etc)
- Schema and Tables 

## Schema
The schema usually defines:
- name of each table
- attributes (columns) of each table
- data types of each column
- Any rules and constraints for each column or table

**Summary:**
- Schema provides structure for the database, establishing which tables exist, their attributes, the data type of each attribute and any constraints on them. The schema does not include the data within each table.

The following is a list of some data types available in Postgres. Refer to [official psql documentation](https://www.postgresql.org/docs/9.5/datatype.html) for a full list and their details:

| <div style="width:100px;">Data Type</div> | Notes                                                                                                                          |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `boolean`                                 |
| `varchar`                                 | Text. The user may define a maximum length.                                                                                    |
| `integer`                                 |
| `text`                                    | Text. The user does not define a maximum length.                                                                               |
| `numeric`                                 | A number that allows floats with precision. (Follow your curiosity to explore what precision and floats in databases implies.) |
| `timestamp`                               | Date and time, including time zone                                                                                             |
| `json`                                    | JSON. (This curriculum will not explore `json`. Follow your curiosity!)                                                        |

## IDs and Primary Keys
- Primary key = unique identifier. Tables may have only one. Typically we have an ID column that holds an int. 

## Postgres
handy psql commands
To access: `psql -U postgres`
To quite: `\q`
Help: `help`
psql commands: `\?`
SQL commands: `\h`
execute commands: `\i`
connect to database: `\c db_name`
Show all tables: `\dt`

SQL commands:
Create a database: `CREATE DATABASE db_name;`

## Create tables
template:
```SQL
CREATE TABLE example_table_name (
    column_name data_type constraint_name,
    column_name data_type constraint_name,
    column_name data_type PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
);
```
breaking it down:
- name things w/snake case
- `PRIMARY KEY`: designates that this column id is the primary key of the table
- `GENERATED ALWAYS AS IDENTITY `: designates that postgres always generates this id for us,
- `CREATE TABLE`: SQL for creating a table
- `(...)`: details about table
- `,`: column defs separated by comma. 

example:
```SQL
CREATE TABLE authors (
  author_name VARCHAR(100),
  author_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY
);
```
breaking it down:
- names of table = authors
- two columns:
  - author_name with datatype VARCHAR(100)
  - author_id with int datatype
- author_id is the primary key column

example 2: 
```SQL
CREATE TABLE media (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
--   postgres creates unique id for us. this is a constraint.
  category VARCHAR(50) NOT NULL,
  title VARCHAR(200) NOT NULL,
  creator TEXT,
  publication_year VARCHAR(10),
  description_text TEXT
);
```
breaking it down:
- The name of the table is media
- There are six columns:
  - id with the data type INT
  - category with the data type VARCHAR(50)
    - NOT NULL = cannot be blank.
  - title with the data type VARCHAR(200)
  - creator with the data type TEXT
  - publication_year with the data type VARCHAR(10)
  - description_text with the data type TEXT
- id is the primary key column

## View table contents
`TABLE tablename` or `SELECT * FROM tablename`

## Drop tables and dbs
`DROP TABLE example_table_name;` 
Check this is deleted with `\dt`. 

`DROP DATABASE db_name;`

This is irrecoverable. 

## Adding New Records
Note: SQL uses single quotes only `'hello'`.

Utilize `INSERT`: A SQL keyword that begins to add record.

```SQL
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```
- (...) = list of column names, optional but recommended. If not provided, statement assumes that values are inserted in order. 
  - Makes more readable. Any columns that do not get assigned a val = NULL.
- VALUES: Insert vals into a new record. 
- Order of vals listed must match order of columns
  - value1 is the val for column1. 

You must follow constraints, otherwise INSERT will fail.

**What if We Inserted the Wrong Values?**
There is no "undo." We should remedy this by updating the record, or deleting and adding a new record. 

**Dealing w/ID**
When we have a column that is `GENERATED ALWAYS AS IDENTITY`:
- we should either exclude the column and value from the INSERT statement
- Use the SQL keyword `DEFAULT`, which will pick the next appropriate value

These will do the same thing: 
```SQL
INSERT INTO authors (author_name, author_id)
VALUES ('Octavia E. Butler', DEFAULT);

INSERT INTO authors (author_name)
VALUES ('Octavia E. Butler');
```

Questions:

For:
```SQL
CREATE TABLE hotel_guests (
    guest_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    guest_name VARCHAR(200),
    is_checked_in BOOLEAN
);
```

Can you use:
```SQL
INSERT INTO hotel_guests (guest_id, guest_name, is_checked_in) VALUES (1, 'Shirley Lim', false);
```

Answ: No - `GENERATED ALWAYS` is a constraint, so ID cannot be assigned.

## Retrieving Records
## Vocab
- Result Set: Set of rows from a db, including metadata about the query. 
- Query: Request to access data from a db.

## Using SELECT
When we use SELECT, we get back a result set. From within psql, the result set is displayed as a table of data printed in our terminal.

Syntax:
`SELECT column1, column2, column3, ... FROM table_name;`
- `SELECT` = SQL keyword to retrieve records
- `column1, col...` = list of columns or use another expression.
- `FROM` = SQL keyword to indicate records from sert of tables

To get all columns
`SELECT * FROM table_name;`

Example:
`SELECT media_id, title FROM media;` returns all media ids and all titles. 

## SELECT and WHERE
`SELECT column1, column2 FROM table_name WHERE condition;`
- WHERE - allows us to add conditions that need to be TRUE. 
  - CANNOT USE !=

Examples:
`SELECT title FROM media WHERE media_id < 3;`
- Pulls all titles before 3rd. 

`SELECT * FROM authors WHERE author_name = 'Octavia E. Butler';`
- Retrieve all records where author_name is equal to 'Octavia E. Butler'

`SELECT * FROM drivers WHERE is_available = true;`
- Retrieve all records where is_available is true

## Using WHERE with IS NOT NULL and IS NULL
We can use IS NOT NULL as a condition to only retrieve records with a non-null value for a certain column.

`SELECT * FROM media WHERE description_text IS NULL;`
- Retrieve all records where description_text is null. When it's null, it has no value.

## SQL string comparison
`STRCMP()` - returns 0 if the strings are the same, -1 if the first argument is smaller than the second according to the current sort order, and 1 otherwise.
Ex: `SELECT STRCMP('text', 'text2')` returns -1. 

## Updating Records w SET
We can update mult records and columns in one go!

```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
- UPDATE = begins update statement
- SET = defines set clause.
- column1 = value1 = set column names to new val.
- WHERE is optional, but without ALL records will update. 

ex: 
```SQL
UPDATE media
SET title = '🍀'
WHERE id = 3;
```
- Updates 3rd items title to shamrock.

```SQL
UPDATE media
SET description_text = '🍀';
```
- updates all descriptions to shamrock.

## Deleting Records
We can delete multiple records at once! USe SELECT to identify which we want to delete. All items deleted are unretrievable. 

```SQL
DELETE FROM table_name
WHERE condition;
```
- DELETE = begins deletion statement
- WHERE = optional, but without, all records in table are removed. 

Ex:
```SQL
DELETE FROM media
WHERE id = 3;
```
- 3rd entry is deleted entirely. 

and
`DELETE FROM media;` will delete all entries in the table, leaving all columns without records.

If deletion successful, you will receive `DELETE #` where # is number of records deleted.