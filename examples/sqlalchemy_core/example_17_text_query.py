"""Example of using text queries"""

from sqlalchemy import create_engine
from sqlalchemy.sql import text

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    connection = engine.connect()

    # Step 1: create a string with a query
    query = text("SELECT AlbumId, Title FROM albums")

    # Step 2: just use it
    for id_, title in connection.execute(query):
        print(f'{id_} {title}')
