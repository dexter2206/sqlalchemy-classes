"""Example of using (inner) JOIN."""
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, or_, and_, not_

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    tracks = meta.tables['tracks']
    albums = meta.tables['albums']

    query = (select([albums.c.Title, tracks.c.Name, tracks.c.Milliseconds])
             .select_from(tracks.join(albums))
             .where(albums.c.Title == 'Big Ones')
             .order_by(tracks.c.Milliseconds.desc()))

    for album_title, track_name, duration in connection.execute(query):
        print(f'{album_title} - {track_name}: {duration}')
