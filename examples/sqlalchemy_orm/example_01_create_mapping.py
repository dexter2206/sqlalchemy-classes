"""Example: creating schema using SQLAlchemy ORM"""
from sqlalchemy import create_engine
from examples.sqlalchemy_orm.model import Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_01.db', echo=True)
    Base.metadata.create_all(engine)