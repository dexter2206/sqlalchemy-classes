"""Example: populating DB using ORM with our enhanced model"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from examples.sqlalchemy_orm.model_enhanced import Base, Employee, Project, Department

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_02.db', echo=True)
    Base.metadata.create_all(engine)

    sales = Department(name='Sales')
    hr = Department(name='hr')
    it = Department(name='IT')

    john = Employee(first_name='John', last_name='Doe', department=it)
    bart = Employee(first_name='Bart', last_name='Simpson', department=hr)
    ann = Employee(first_name='Ann', last_name='Nowak', department=it)
    rambo = Employee(first_name='John', last_name='Rambo')

    rambo.department = sales

    proj_x = Project(name='Project x')
    proj_z = Project(name='Project z')

    rambo.projects.append(proj_x)
    rambo.projects.append(proj_z)
    proj_z.employees.append(john)
    proj_x.employees.append(ann)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add_all([sales, hr, it, john, bart, ann, rambo])

    session.commit()

    session.close()