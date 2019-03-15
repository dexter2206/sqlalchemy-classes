"""Example of issuing UPDATE statement"""
from sqlalchemy import create_engine, MetaData

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()

    genres = meta.tables['genres']

    # As with INSERT, UPDATE statement is created using appropriate method of the table being updated.
    # Note: if used without WHERE clause, we would update EVERY row in the Table, which is rarely what
    # you want to do.
    statement = (genres.update()
                 .where(genres.c.GenreId == 26) # Update only genre with GenreId = 26
                 .values(Name='Disco Polo'))    # Specify values to be updated as keyword arguments.

    result = connection.execute(statement)
    print(f'Affected rows: {result.rowcount}')  # Check how many rows were affected.
