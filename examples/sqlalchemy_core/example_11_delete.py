"""Example of DELETEing rows"""
from sqlalchemy import create_engine, MetaData

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()

    genres = meta.tables['genres']
    # DELETE statement is created using delete method. Note that same rule as with UPDATE applies - if you didn't
    # specify WHERE clause you would (possibly) wipe all the records.
    statement = genres.delete().where(genres.c.GenreId >= 26)

    result = connection.execute(statement)
    print('Number of deleted rows: {result.rows}')