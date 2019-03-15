"""Example of inserting values into DB"""
from datetime import datetime
from sqlalchemy import create_engine, MetaData

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()

    genres = meta.tables['genres']
    emps = meta.tables['employees']

    # INSERT statement is generated using insert method of Table.
    ins = genres.insert()
    print('Adding new genre')
    print(f'Statement that will be executed: {str(ins)}')
    # Inserting a single row is as simple as specifying keyword args corresponding to inserted values.
    result = connection.execute(ins, Name='disco polo')
    # If some key was generated (and it should in this case), it is available in inserted_primary_key attribute.
    # Note that we access 0-th element (the only one in this case), but in general when composite key is used,
    # inserted_primary_key  may contain more than one item.
    print(f'Auto generated primary key: {result.inserted_primary_key[0]}')

    ins = emps.insert()
    print('Adding new employee')
    result = connection.execute(ins, LastName='Doe', FirstName='John')
    print(f'Auto generated primary key: {result.inserted_primary_key[0]}')

    # Multiple inserts can be done at once - instead of specifying kwargs corresponding to inserted values,
    # specify dictionary for each row you want to insert.
    # Note: when performing multiple inserts at once all dictionaries need to have the same keys!
    print('Inserting multiple employees')
    result = connection.execute(
        ins, [{'FirstName': 'John', 'LastName': 'Adams'},
              {'FirstName': 'Amy', 'LastName': 'Klein'}])
    # The rowcount property tells how many rows were affected (in this case: how many rows were inserted).
    print(f'Inserted this many rows: {result.rowcount}')
