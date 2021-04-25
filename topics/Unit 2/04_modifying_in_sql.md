# Modifying Tables
Sometimes we need to modify the tables in our databases!
- You can DROP then CREATE

## Adding a New Col
```SQL
ALTER TABLE table_name
ADD COLUMN column_name data_type constraint_name;
```
- `ALTER TABLE`: alter existing table
- Adding a column affects every row in the table. By default, the value for the new column in each record will be NULL. 

Example:
```SQL
ALTER TABLE books
ADD COLUMN nyt_weeks INT NOT NULL DEFAULT 0;
```
- table = books
- new column = nyt_weeks
- 0 is inserted as default val.
- The DEFAULT constraint will also affect future INSERT commands. If we insert a new record without providing nyt_weeks, Postgres will use the DEFAULT value that we set in the constraint: 0.

## Removing a Col
```SQL
ALTER TABLE books
DROP COLUMN author_name;
```
- Drops author_name from books table.

## Modifying Data Type
```SQL
ALTER TABLE table_name
ALTER COLUMN column_name
TYPE new_data_type
USING conversion_expr;
```

Example:
```SQL
ALTER TABLE books
ALTER COLUMN nyt_weeks
TYPE BOOLEAN
USING nyt_weeks::boolean;
```
- the table is named books
- We change nyt_weeks to boolean.
- provide the conversion expression as `nyt_weeks::boolean` which is equivalent to `CAST (nyt_weeks) AS boolean`. 

## Renaming a col
```SQL
ALTER TABLE table_name
RENAME COLUMN column_name
TO new_column_name;
```

## Rename a table
```SQL
ALTER TABLE table_name
RENAME TO new_table_name;
```

# Modifying db's
```SQL
ALTER DATABASE database_name
RENAME TO new_database_name;
```
- we cannot rename a database to which we are currently connected.