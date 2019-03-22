"""Example of adding multiple objects to session at once."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from examples.sqlalchemy_orm.model import Employee

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_01.db', echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    # The add_all method, as the name suggests, adds all objects
    # that are in a list passed as an argument.
    session.add_all([
        Employee(first_name='John', last_name='Doe'),
        Employee(first_name='Bart', last_name='Simpson'),
        Employee(first_name='Ann', last_name='Nowak'),
        Employee(first_name='John', last_name='Rambo')
    ])

    session.commit()

    session.close()
