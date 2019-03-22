"""Example of nested query"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select, func

if __name__ == '__main__':
    engine = create_engine('sqlite:///../chinook.db', echo=True)
    meta = MetaData()
    meta.reflect(bind=engine)
    connection = engine.connect()

    invoices = meta.tables['invoices']

    # This query computes an average total of invoices
    avg_total_query = select([func.avg(invoices.c.Total).label('average')])

    result = connection.execute(avg_total_query).fetchone()
    print(result['average'])

    # This will select invoices that have Total > the average that the
    # query above computes.
    outer_query = (select([invoices.c.InvoiceId, invoices.c.Total])
                   .where(invoices.c.Total > avg_total_query.as_scalar()))

    for _id, total in connection.execute(outer_query):
        print(f'{_id} {total}')
