"""Example of using text queries with parameters"""

from sqlalchemy import create_engine
from sqlalchemy.sql import text

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    connection = engine.connect()

    # Step 1: create a string with a query. Place :parameter_name do denote values
    # to be supplied later.
    query = text("SELECT FirstName, LastName FROM customers WHERE City=:city")

    # Step 2: execute query supplying parameters via kwargs
    for first_name, last_name in connection.execute(query, city='Berlin'):
        print(f'{first_name} {last_name}')

    # Step 2 (alternative): execute query supplying parameters via dict
    for first_name, last_name in connection.execute(query, {'city': 'New York'}):
        print(f'{first_name} {last_name}')