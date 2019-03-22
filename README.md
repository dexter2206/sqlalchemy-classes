# Relayr Advanced Python class 01 and 02 - accessing SQL databases using SQLAlchemy

## Prerequisities:
1. SQLite and (optionally) SQLiteBrowser installed
2. Download chinook database from here: http://www.sqlitetutorial.net/sqlite-sample-database/

## Exercises for SQLAlchemy `core` part
1. Display all first name and last name of every employee.
2. Display all employees with Job title 'Sales Support Agent'
3. Dispaly all employees that are Managers born before 1970-01-01.
4. Modify 2. and 3. so that only the displayed fields are selected.
5. Pick some album. Display all its tracks in descending order of duration (look at Miliseconds field).
6. Create new album (i.e. add new row in Albums table as well as Tracks referencing it).
7. Supprise time! Change the genre of all Pop records to Opera.

## Exercises for SQLAlchemy `ORM` part
1. For simplified model:
    - Add several employees.
    - Verify that the employees were added successfully.
2. For enhanced model:
    - Add several employees, departments and projects.
    - Verify that objects above were added successfuly.
    - Illustrate N+1 select problem on a different example than the one presented during classes. Then apply eager loading to mitiate it.
    
## Final exercise

Write a simple text-based application for logging expenses. The expenses should have their title, category/categories, value (i.e. amount of money spent) and date when it took place. You should design appropriate schemas, define `Table` objects or ORM mapping for that schema. The application should expose the followin functoinallities:

- adding new expenses
- adding category (if you choose that categories are stored in a separate table)
- querying expenses by category
- querying expenses by date (i.e. showing expenses that occured between two dates)

There are no restrictions on the interface of the application, just don't spend too much time on it - remember that the main goal of this class is learning how to interact with a database.

There are some variants of this exercise with different difficulties:
- Easiest: categories are stored as strings.
- Medium: categories are treated as different entities (have their separate table), mapping between expenses and categories is many-to-one.
- Hardest: categories are treated as diffrent entities, mapping between expenses and categories is many-to-many.

As a side note: why (in production code) it would be a better option to NOT use the first alternative above? What are its drawbacks and limitations?
