"""Illustration of Session workflow in SQLAlchemy ORM"""
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from examples.sqlalchemy_orm.model import Employee

def print_session_state(session):
    print(f'New: {session.new}')
    print(f'Dirty: {session.dirty}')
    print(f'Deleted: {session.deleted}')
    print(f'Identity map: {session.identity_map.values()}')

def print_separator():
    print(40 * '=')

def object_state(obj):
    insp = inspect(obj)
    if insp.transient:
        return 'transient'
    if insp.persistent:
        return 'persistent'
    if insp.deleted:
        return 'deleted'
    if insp.detached:
        return 'detached'
    if insp.pending:
        return 'pending'
    raise RuntimeError('Object has to be in some state...')

if __name__ == '__main__':
    engine = create_engine('sqlite:///../employees_01.db', echo=False)

    # Session objects serve for tracking objects' state.
    # The sessionmaker object creates new Session class that we need to instantiate.
    Session = sessionmaker(bind=engine)
    session = Session()

    # Print internal state of the session.
    # new: new objects that were added to session and are not yet stored in DB
    # dirty: modified objecst that are tracked by session.
    # At first both of those should be empty...
    print('Initial state of session:')
    print_session_state(session)

    employee = Employee(first_name='Andrew', last_name='Nowak')

    print_separator()

    print('After creating employee:')
    print(f'Current employee ID: {employee.emp_id}')
    print(f'Current employee state: {object_state(employee)}')

    # State of the session should not change after creating an employee
    # After all, we haven't instructed session to track it yet!
    print_session_state(session)

    # The add method tells session to keep track of our object
    session.add(employee)

    print_separator()

    print('After adding the employee:')
    print('State of session after adding the employee:')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    # Observe DB before continuing...
    input('Observe state of the DB. Press enter to continue...')

    session.commit()

    print_separator()

    print('After commit:')
    print(f'Current employee ID: {employee.emp_id}')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    input('Press enter to continue...')

    # Let's modify our employee.
    employee.first_name = 'Ann'

    print_separator()

    print('After changing employee')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    input('Observe state of the DB. Press enter to continue...')

    # And now save the changes.
    session.commit()

    print_separator()

    print('After commmitting change in employee:')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    # Let's detach employee for a while.
    # Detached objects are not tracked by session.
    session.expunge(employee)

    print_separator()

    print('After expunging employee:')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    # And add it again
    employee = session.merge(employee)

    print_separator()

    print('After merging employee:')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    # Finally delete the employee
    session.delete(employee)

    print_separator()

    print('After deleting employee:')
    print_session_state(session)
    print(f'Current employee state: {object_state(employee)}')

    # Observe DB - employee is not deleted yet!
    input('Observe state of the DB. Press enter to continue...')

    session.commit()

    print_separator()

    print('After commiting deletion employee:')
    print(f'Current employee state: {object_state(employee)}')
    print_session_state(session)

    session.close()