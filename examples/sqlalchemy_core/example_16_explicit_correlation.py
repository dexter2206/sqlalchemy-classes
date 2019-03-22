"""Example of correlated subquery with explicitly specified correlation

In this example we would like to replicate the behaviour of the following query:

SELECT Title, Name, Milliseconds
FROM tracks INNER JOIN albums AS outer
WHERE Milliseconds =
	(SELECT Max(Milliseconds)
	 FROM tracks
	 WHERE tracks.AlbumId == outer.AlbumId);

What does this query do?

Note that we can realize this example just like 15 but here we take different
approach - instead of using aliases we specify tables to be correlated
explicitly.
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

    # Step 2: prepare nested query
    inner_query = (select([func.max(tracks.c.Milliseconds)])
                   .where(tracks.c.AlbumId == albums.c.AlbumId)
                   .correlate(albums))

    # Step 3: prepare enclosing query
    enclosing_query = (select([albums.c.Title, tracks.c.Name, tracks.c.Milliseconds])
                       .select_from(tracks.join(albums))
                        .where(tracks.c.Milliseconds == inner_query)
                       .limit(10))

    # Step 4: execute as usually
    for title, name, duration in connection.execute(enclosing_query):
        print(f'{title}, {name}: {duration}')
