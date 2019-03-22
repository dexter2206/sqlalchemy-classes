"""Example: creating a mapping and defining schema using SQLAlchemy ORM"""
from sqlalchemy import Integer, String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

emp_proj = Table('emp_proj', Base.metadata,
                 Column('emp_id', ForeignKey('employees.emp_id'), primary_key=True),
                 Column('proj_id', ForeignKey('projects.proj_id'), primary_key=True))


class Employee(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dept_id = Column(Integer, ForeignKey('departments.dept_id'))

    department = relationship('Department', back_populates='employees')
    projects = relationship('Project', secondary=emp_proj, back_populates='employees')

    def __repr__(self):
        return f'{self.first_name} {self.last_name} <id {self.emp_id}>'

class Project(Base):

    __tablename__ = 'projects'
    proj_id = Column(Integer, auto_increment=True, primary_key=True)
    name = Column(String)

    employees = relationship('Employee', secondary=emp_proj, back_populates='projects')

class Department(Base):
    __tablename__ = 'departments'

    dept_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, autoincrement=True)

    employees = relationship('Employee', back_populates='department', order_by=Employee.emp_id)
