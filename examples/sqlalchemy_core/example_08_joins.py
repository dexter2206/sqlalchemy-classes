"""Example of using (inner) JOIN."""
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, or_, and_, not_

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    artists = meta.tables['artists']
    albums = meta.tables['albums']

    # Note select_from method call.
    # Specifying artists.join(albums) tells SQLAlchemy to use (LEFT) INNER JOIN instead of FULL JOIN.
    query = (select([artists.c.Name, albums.c.Title])
             .select_from(artists.join(albums))
             .limit(20))
    for artist_name, album_title in connection.execute(query):
        print(f'{artist_name}: {album_title}')
