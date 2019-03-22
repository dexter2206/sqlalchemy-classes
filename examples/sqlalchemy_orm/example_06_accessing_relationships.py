"""Example: accessing relationship data"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from examples.sqlalchemy_orm.model_enhanced import Base, Employee, Project, Department

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_02.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rambo = session.query(Employee).filter_by(last_name='Rambo').first()

    print('Employee we found:')
    print(rambo)

    print('Rambo participates in following projects:')
    for project in rambo.projects:
        print(project)

    it = session.query(Department).filter_by(name='IT').first()

    print('Employees in IT department')
    for employee in it.employees:
        print(employee)

    session.close()
