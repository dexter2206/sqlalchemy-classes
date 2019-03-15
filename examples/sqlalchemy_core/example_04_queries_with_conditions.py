"""Example of SELECT query with WHERE clause"""
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    tracks = meta.tables['tracks']

    # Notice that fluent API - we chain where and limit calls.
    query = select([tracks]).where(tracks.c.UnitPrice > 0.99).limit(5)
    print('First five tracks that cost more than 0.99:')
    for row in connection.execute(query):
        print(f'{row[tracks.c.Name]}: {row[tracks.c.UnitPrice]}')

    # Another example - instead of comparing using one of the operators, we use column's like method to
    # construct SQL LIKE clause
    query = select([tracks]).where(tracks.c.Name.like('Exodus%'))
    print('Trakcs that start with "Exodus"')
    for row in connection.execute(query):
        print(f'{row[tracks.c.Name]}: {row[tracks.c.UnitPrice]}')

    invoices = meta.tables['invoices']
    # In this example we use datetime object to provide lower bound for dates in invoices table.
    # Btw. this one would work even when datetime object is replaced with string. Why is that so?
    # What are the reasons not to use strings when comparing to dates stored in DB?
    query = select([invoices]).where(invoices.c.InvoiceDate > datetime(2013, 11, 30))
    print('Dates and totals of invoices billed after November 30th 2013:')
    for row in connection.execute(query):
        print(f'{row[invoices.c.InvoiceDate]}, total {row[invoices.c.Total]}')


