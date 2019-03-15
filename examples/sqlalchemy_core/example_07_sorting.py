"""Example of using ORDER BY clause."""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=False)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()
    invoices = meta.tables['invoices']

    # Order is speceified with order_by method. Note: by default sorting is done in ASCENDING order.
    query = (select([invoices.c.InvoiceDate, invoices.c.Total])
                 .order_by(invoices.c.Total)
                 .limit(10))
    for date, total in connection.execute(query):
        print(f'{date} {total}')

    # Sorting in descending order can be done by using desc method of column used in order_by.
    query = (select([invoices.c.InvoiceDate, invoices.c.Total])
                 .order_by(invoices.c.Total.desc())
                 .limit(10))
    for date, total in connection.execute(query):
        print(f'{date} {total}')
