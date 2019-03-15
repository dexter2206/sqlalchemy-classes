"""Basic SQLAlchemy example - SELECTing everything from some table"""
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

if __name__ == '__main__':
    # The below illustrates basic usage of SQLAlchemy core.
    # Step 1: create engine responsible for connecting to DB.
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    # Step 2: create metadata object.
    meta = MetaData()
    # Step 3: actually connect.
    connection = engine.connect()
    # Step 4: define your tables or, as in this case, load table definition.
    artists = Table('artists', meta, autoload=True, autoload_with=engine)
    # Step 5: create basic query. The one here is equivalent to "SELECT * FROM artists".
    query = select([artists])
    # Step 6: execute query using the above acquired connection and print the results.
    for idx, name in connection.execute(query):
        print(f'{idx:3}: {name}')