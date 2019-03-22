"""Example of basic query patterns using ORM"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from examples.sqlalchemy_orm.model import Employee

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_01.db', echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Case 1: get all employees
    print('All employees:')
    for employee in session.query(Employee):
        print(employee)

    # Case 2: select all employees with first name John
    print('==== Employees named John:')
    for employee in session.query(Employee).filter_by(first_name='John'):
        print(employee)

    # Case 3: select all employees with first name John (another way)
    print('==== Employees named John:')
    for employee in session.query(Employee).filter(Employee.first_name=='John'):
        print(employee)

    # Case 4: select all employees, order by first name
    print('==== Employees ordered by first name:')
    for employee in session.query(Employee).order_by(Employee.first_name):
        print(employee)

    # Case 5: select employees whose last name contains "a"
    print('==== Employees with an "a" in their name:')
    for employee in session.query(Employee).filter(Employee.last_name.like('%a%')):
        print(employee)
