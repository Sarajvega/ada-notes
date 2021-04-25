# More Selecting

## Compound Conditions
- Compound Condition: Condition formed from mult simple comparisons. `AND`,`OR` or `NOT`. 
`WHERE` restricts our `SELECT` results. We can utilize compound conditions w/`WHERE`. 

## Using AND
```SQL
SELECT * from books
WHERE author = 'Madie McClure'
AND genre = 'Nonfiction';
```
- Pulls all books by Madie with the genre of Nonfiction.

## Using OR
```SQL
SELECT * from books
WHERE author = 'Madie McClure'
OR author = 'Tim McDermott';
```
- Pulls all books by Madie or Tim.

## Using NOT
```SQL
SELECT * from books
WHERE NOT author = 'Bret Bergstrom';
```
- Pulls all books not written by Bret.

## Combining
- Order of precendence: NOT, AND, OR.

```SQL
SELECT * from books
WHERE author = 'Madie McClure'
OR author = 'Tim McDermott'
AND genre = 'Intrigue';
-- Above will not work as expected. To Fix:
SELECT * from books
WHERE (author = 'Madie McClure' OR author = 'Tim McDermott')
AND genre = 'Intrigue';
```
- `AND` has a higher precedence. So in the first query, the results for Tim are restricted to Intrigue but all of Madie's books are selected. 

## Ordering
- Postgres determined the order of rows.
- Default = order depends on what data is in db and how its sotred.
- We must treat results as unspecificed:
  - `ORDER BY` allows us to explicitly order results. 

## ORDER BY
```SQL
SELECT
    columns_desired
FROM
    table_name
(additional optional clauses)
ORDER BY
    sort_expression1 sort_direction,
    sort_expression2 sort_direction,
    ... ;

```
- `ORDER BY`: SQL keyword
- `sort_expression_1` = most common exp are column names.
- `sort_direction` = ASC/DESC for ascending/descending. NULL FIRST/LAST to display lack of input first or last. 

Example:
```SQL
SELECT title, price
FROM books
ORDER BY price DESC;
```
- Here books will be ordered by price, most expensive to least.

Example 2:
```SQL
SELECT title, price
FROM books
ORDER BY price NULLS LAST;
```
- Items without a price are last. 

## LIMIT
- db's can be huge. `LIMIT` allows us to show only a certain num of results at once. 

```SQL
SELECT columns_desired
FROM table_name
(additional optional clauses)
LIMIT row_count;
```

Example:
```SQL
SELECT title
FROM books
WHERE genre = 'sci-fi'
LIMIT 10;
```
- Limits 10 results of books with the genre 'sci-fi'.

You can combine with `ORDER BY`!
```SQL
SELECT title, price
FROM books
ORDER BY price DESC
LIMIT 5;
```
- This will show the 5 most expensive books.


## OFFSET
- If we want to see 11 - 20 after the first limit designated number of results?

```SQL
SELECT title
FROM books
WHERE genre = 'sci-fi'
LIMIT 10 OFFSET 10;
```
- OFFSET tells SQL to start after the first 10 matches.

Challenge Question:
```SQL
CREATE TABLE states (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name VARCHAR(64),
  area_sq_mi FLOAT,
  population INT
);
```
Write a SELECT statement that retrieves the name and area of the third largest state.


ANSWER:
```SQL
SELECT name, area_sq_mi
FROM states
ORDER BY area_sq_mi DESC
LIMIT 1 OFFSET 2;
```

## Aggregate Functions
When we perform a SELECT query, we are gathering a group of records. Maybe we'd like to get all the books by a particular author and find out how many there are. Maybe we'd like to get a list of books in a certain genre, and then the average price of that list.

## MAX and MIN
```SQL
SELECT MAX(price)
FROM books;
```
- Pulls most expensive from list. 

```SQL
SELECT MIN(title)
FROM books;
```
- Pulls first alphabetical title. 

```SQL
SELECT title
FROM books
WHERE price = (
  SELECT MAX(price)
  FROM books
);
```
- `WHERE` can be used with the min max.
- Here it will pull the title of the most expensive book.

## SUM, COUNT and AVG
```SQL
SELECT SUM(price)
FROM books
WHERE author_id = 3;
```
- pulls total price for all books written by a specifc author.

```SQL
SELECT COUNT(*)
FROM books
WHERE price > 15;
```
- Returns number of rows watching a specific query. 

```SQL
SELECT title
FROM books
WHERE price > (
  SELECT AVG(price)
  FROM books
);
```
- This query retrieve the title field from any row where the book's price is higher than the avg of all book prices. 

## Grouping
What if we wanted to get the count of products sold by each vendor in our database?
We can use: `GROUP BY`!

```SQL
SELECT cohort
FROM alumni
GROUP BY cohort;
```
- Returns a unique list of values in the cohort field. 
- If we GROUP BY some column in the data, and list that column in our SELECT results, we will receive a unique list of the values found in that column. We can use GROUP BY to get distinct entries from our data.

## GROUP BY and Aggregate Functions
```SQL
SELECT *
FROM alumni
GROUP BY cohort;
```
- Will throw an error. WHY?

SQL returns tables of results. When we group by a column, all records that share that value for that column are grouped.

Say we have several people. We group them by their cohort, getting cohort 8. If we try to include their first_name data, the table would need to be:
```SQL
cohort   | first_name
----------+----------------------------------------
 Cohort 8 | Felicia, Lorena, Vera, Agnes, Courtney
(1 rows???)
```

Which we cannot do. 

The general syntax for SELECT w/grouping:
```SQL
SELECT
   column_desired_1,
   column_desired_2,
   ...,
   aggregate_function(column_to_aggregate)
FROM
   table_name
GROUP BY
   column_desired_1,
   column_desired_2,
   ...;
```
- SELECT portion are either columns corresponding to the columns listed in the GROUP BY, or they are an aggregate function applied to a non-grouped column.

Example:
```SQL
SELECT author_id, MAX(price)
FROM BOOKS
GROUP BY author_id
ORDER BY author_id;
```
- This will pull the most expensive price for each author. 

Example 2:
```SQL
SELECT state, count(*)
FROM alumni
GROUP BY state;
```
- pulls the number of alumni from each state. 
- -`count(*)`: Counts number of instances of alumni

