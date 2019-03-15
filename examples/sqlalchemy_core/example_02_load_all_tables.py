"""Example of autoloading all tables at once"""
from itertools import islice
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine) # This loads information on all tables.
    connection = engine.connect()
    artists = meta.tables['artists'] # No need to define artists table. Definition is already in meta.tables dictionary.
    query = select([artists])
    # IMPORTANT: We use islice here because we haven't seen example with limit yet. Dont't use islice to limit
    # number of results in production code.
    for idx, name in islice(connection.execute(query), 5):
        print(f'{idx:3}: {name}')
    genres = meta.tables['genres']
    query = select([genres])
    for idx, name in islice(connection.execute(query), 5):
        print(f'{idx:3}: {name}')