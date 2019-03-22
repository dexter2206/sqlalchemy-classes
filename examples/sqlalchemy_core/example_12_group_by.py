"""Example of using GROUP BY, HAVING and aggregate functions."""
from sqlalchemy import create_engine, MetaData, func
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()

    albums = meta.tables['albums']
    tracks = meta.tables['tracks']

    # GROUP BY clause is specified by group_by method.
    # The below query is roughly equivalent to
    # SELECT Title, SUM(UnitPrice) as Price
    # FROM Albums
    # JOIN Tracks ON Albums.AlbumId = Tracks.AlbumId GROUP BY albums.AlbumId
    # LIMIT 5
    query = (select([albums.c.Title, func.sum(tracks.c.UnitPrice).label('Price')])
             .select_from(albums.join(tracks))
             .group_by(albums.c.AlbumId)
             .limit(5))

    print('Five albums along with their total prices: ')
    for row in connection.execute(query):
        print(f'{row["Title"]} : {row["Price"]}')

    # Similarly we can use having method to specify HAIVNG clause.
    # In the example below we use price to filter the result.
    # In order to not specify the same func twice, we define
    # aggregated column beforehand and then use it in select(...) and having(...)
    # Also notice call to label method, which allows us to give our aggregated column
    # Some alias.
    price = func.sum(tracks.c.UnitPrice)
    query = (select([albums.c.Title, price.label('Price')])
             .select_from(albums.join(tracks))
             .group_by(albums.c.AlbumId)
             .having(price >= 40.00)
             .order_by(price.desc()))

    print('Albums that cost more than 40.00: ')
    for row in connection.execute(query):
        print(f'{row["Title"]} : {row["Price"]}')
