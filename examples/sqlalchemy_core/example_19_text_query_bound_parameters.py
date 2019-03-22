"""Example of using text queries with parameter binding"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import text

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    connection = engine.connect()

    # Step 1: create a string with a query. Place :parameter_name do denote values
    # to be supplied later.
    query = text("""
    SELECT FirstName, LastName
    FROM customers 
    WHERE State=:state AND FirstName LIKE :pattern""")

    # Step 2: bind some of the parameters, i.e. fix their value
    query = query.bindparams(state='SP')

    # Step 3: execute query and supply remaining parameters
    for first_name, last_name in connection.execute(query, pattern='%d%'):
        print(f'{first_name} {last_name}')
