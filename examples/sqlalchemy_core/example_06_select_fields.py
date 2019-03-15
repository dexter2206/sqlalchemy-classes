"""Example of selecting only specific fields."""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    customers = meta.tables['customers']

    # Instead of specifying customers as a whole we only list specific columns.
    query = select([customers.c.FirstName,
                    customers.c.LastName]).limit(10)
    for first_name, last_name in connection.execute(query):
        print(f'{first_name} {last_name}')

    for row in connection.execute(query):
        print(f'{row[customers.c.FirstName]} {row[customers.c.LastName]}')

    # This would fail - rows in results object don't have Company column.
    # Note that if we change query so that whole Customer object is included, this would work.
    for row in connection.execute(query):
        print(f'{row[customers.c.FirstName]} {row[customers.c.LastName]} {row[customers.c.Company]}')
