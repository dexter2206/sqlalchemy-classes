"""Example of correlated subquery

In this example we would like to replicate the behaviour of the following query:

SELECT Name, Milliseconds
FROM tracks AS outer
WHERE Milliseconds =
	(SELECT Max(Milliseconds)
	 FROM tracks
	 WHERE tracks.AlbumId == outer.AlbumId);

What does this query do?
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select, func

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()

    albums = meta.tables['albums']
    tracks = meta.tables['tracks']

    # Step 1: create an alias for outer table
    outer = tracks.alias('outer')

    # Step 2: prepare nested query
    inner_query = (select([func.max(tracks.c.Milliseconds)])
                   .where(tracks.c.AlbumId == outer.c.AlbumId))

    # Step 3: prepare enclosing query
    enclosing_query = (select([outer.c.Name, outer.c.Milliseconds])
                       .where(outer.c.Milliseconds == inner_query.as_scalar())
                       .limit(10))

    # Step 4: execute as usually
    for name, duration in connection.execute(enclosing_query):
        print(f'{name}: {duration}')
