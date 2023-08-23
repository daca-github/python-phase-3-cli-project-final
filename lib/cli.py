import click
from db.models import User, Car
from db.database import SessionLocal as Session

@click.group()
def main():
    """CarBud: Your Virtual Dealership"""
    pass 

@main.command()
def menu():
    click.echo('Welcome to CarBud!')
    click.echo('1. Used Cars')
    click.echo('2. New Cars')
    click.echo('3. Search by criteria')
    click.echo('4. Exit')

    choice = click.prompt('Please enter your choice', type=int)

    if choice == 1:
        display_cars('Used')
    elif choice == 2:
        display_cars('New')
    elif choice == 3:
        search_by_criteria()
    elif choice == 4:
        exit()
    else:
        click.echo('Invalid choice. Please try again.')

def display_cars(make):
    click.echo(f'Displaying {make} cars...')

@main.command()
def search_by_criteria():
    model = click.prompt('Enter the model')
    make = click.prompt('Enter the make')
    
    click.echo(f'Searching for cars with model: {model} and make: {make}')


if __name__ == '__main__':
    menu()
