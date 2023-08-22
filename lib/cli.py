import click 
from db.models import User, Car
from db.database import Session

@click.group()
def main():
    """CarBud: Your Virtual Dealership"""
    pass 

@click.command()
def display_main_menu():
    click.echo('1. Used Cars')
    click.echo('2. New Cars')

@click.command()
def search_by_criteria():
    model = click.prompt('Enter the model')
    make = click.prompt('Enter the make')
