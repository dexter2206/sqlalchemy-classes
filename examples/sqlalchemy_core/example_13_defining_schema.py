"""Example showing how to manually define tables and CREATE them. """
from sqlalchemy import create_engine, Table, MetaData, Integer, String, Column, ForeignKey

if __name__ == '__main__':
    engine = create_engine('sqlite:///employees.db', echo=True)
    meta = MetaData()

    # The basic procedure goes as follows:
    # 1. Create MetaData object that will be used by all tables.
    # 2. For each table specify its name and this MetaData object along with column definitions.
    # 3. Column definitions may containt column name, type and constraints + additional attributes
    # (e.g. PK, FK, autoincrement).
    # After you defined all the Tables this way, run meta.create_all(engine) and then ues your tables as usual.
    departments = Table(
        'departments',
        meta,
        Column('dept_id', Integer, primary_key=True, autoincrement=True),
        Column('dept_name', String(length=20), nullable=True)
    )

    employees = Table(
        'employees',
        meta,
        Column('emp_id', Integer, primary_key=True, autoincrement=True),
        Column('first_name', String(length=20), nullable=False),
        Column('last_name', String(length=20), nullable=False),
        Column('dept_id', Integer, ForeignKey('departments.dept_id'))
    )

    meta.create_all(engine)