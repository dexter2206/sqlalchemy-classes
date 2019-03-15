"""Using column definitions for reading results"""
from itertools import islice
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    artists = meta.tables['artists']
    query = select([artists])
    results = connection.execute(query)
    for row in islice(results, 5):
        print(f'{row[artists.c.ArtistId]}: {row[artists.c.Name]}')
    # We haven't used all results, so we close the results object explicitly. Usually there is no need to do it.
    results.close()
