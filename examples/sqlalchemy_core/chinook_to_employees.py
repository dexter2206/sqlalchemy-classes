"""Insert employees present in Chinook into our new custom DB"""
from datetime import datetime
from sqlalchemy import create_engine, MetaData

if __name__ == '__main__':
    chinook_engine = create_engine('sqlite:///../chinook.db', echo=True)
    emp_engine = create_engine('sqlite:///employees.db', echo=True)

    new_emps = [{'first_name': first_name, 'last_name': last_name}
                for first_name, last_name in chinook_engine.execute('SELECT FirstName, LastName FROM employees')]

    insert = emp_engine

    meta = MetaData()
    meta.reflect(bind=emp_engine)
    emps = meta.tables['employees']

    emp_engine.execute(emps.insert(), new_emps)