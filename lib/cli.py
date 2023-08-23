import click
from db.models import User, Car
from db.database import SessionLocal as Session

def get_user(session):
    username = click.prompt('Please enter your username')
    user = session.query(User).filter_by(username=username).first()
    return user

@click.group()
def main():
    """CarBud: Your Virtual Dealership"""
    pass 

@main.command()
def menu():
    session = Session()
    user = get_user(session)
    session.close()

    if user:
        click.echo(f'Welcome, {user.username}!')
    else:
        click.echo('User not found. Please register.')

    click.echo('1. Display Available Cars')
    click.echo('2. Search by criteria')
    click.echo('3. Exit')

    choice = click.prompt('Please enter your choice', type=int)

    if choice == 1:
        display_available_cars()
    elif choice == 2:
        search_by_criteria()
    elif choice == 3:
        exit()
    else:
        click.echo('Invalid choice. Please try again.')

def display_available_cars():
    session = Session()
    available_cars = session.query(Car).filter_by(status='Available').all()
    session.close()

    if available_cars:
        click.echo('Available Cars:')
        for car in available_cars:
            click.echo(f'{car.make} {car.model}, Year: {car.year}, Price: {car.price}')
    else:
        click.echo('No available cars at the moment.')

def search_by_criteria():
    session = Session()
    model = click.prompt('Enter the model')
    make = click.prompt('Enter the make')
    
    cars = session.query(Car).filter_by(model=model, make=make).all()
    session.close()

    if cars:
        click.echo(f'Found {len(cars)} cars matching your criteria:')
        for car in cars:
            click.echo(f'{car.make} {car.model}, Year: {car.year}, Price: {car.price}')
    else:
        click.echo('No cars matching the criteria.')

if __name__ == '__main__':
    menu()
