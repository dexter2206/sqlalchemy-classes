"""Solution to N+1 select problem"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from examples.sqlalchemy_orm.model_enhanced import Base, Employee, Project, Department

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_02.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Specifying
    departments = session.query(Department).options(joinedload(Department.employees))

    print('Employees by department:')
    for dept in departments:
        print(f'[{dept.name}]')
        for emp in dept.employees:
            print(emp)

    session.close()
