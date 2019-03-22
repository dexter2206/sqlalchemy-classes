"""Example: creating a mapping and defining schema using SQLAlchemy ORM"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} <id {self.emp_id}>'