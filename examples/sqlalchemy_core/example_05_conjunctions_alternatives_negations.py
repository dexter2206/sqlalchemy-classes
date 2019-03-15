"""Example of using logical operators to combine conditions."""
from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select, or_, and_, not_

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    media_types = meta.tables['media_types']
    artists = meta.tables['artists']
    invoices = meta.tables['invoices']

    # or_ (alternative) - select artists named James OR Peter
    query = select([artists]).where(or_(
        artists.c.Name.like('James%'),
        artists.c.Name.like('Peter%')))
    for idx, name in connection.execute(query):
        print(f'{idx:3}: {name}')

    # and_ (conjunction) - select invoices with total cost between 10.0 AND 13.0 (exclusive)
    query = select([invoices]).where(and_(
        invoices.c.Total > 10.0,
        invoices.c.Total < 13.0))
    for row in connection.execute(query):
        print(f'{row[invoices.c.Total]}')

    # not_ (negation) - select media types that don't start on P
    query = select([media_types]).where(not_(media_types.c.Name.like('P%')))
    for row in connection.execute(query):
        print(f'{row[media_types.c.Name]}')
