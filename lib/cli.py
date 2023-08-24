import click
from db.models import User, Car, Appointment
from db.database import SessionLocal as Session
from datetime import datetime

def get_user(session, username):
    user = session.query(User).filter_by(username=username).first()
    return user

def register_user(session, username):
    user = User(username=username)
    session.add(user)
    session.commit()
    click.echo(f'User {username} has been registered!')

def calculate_estimate(car_price, downpayment):
    interest_rate = 0.05  
    loan_amount = car_price - downpayment
    monthly_interest_rate = interest_rate / 12
    num_months = 48  

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_months)
    total_payment = monthly_payment * num_months

    return monthly_payment, total_payment

def display_menu(session, user):
    while True:
        click.echo(f'Welcome, {user.username}!')
        click.echo('1. Display Available Cars')
        click.echo('2. Search by criteria')
        click.echo('3. Set Appointment')
        click.echo('4. Get Estimate')
        click.echo('5. Exit')

        choice = click.prompt('Please enter your choice', type=int)

        if choice == 1:
            display_available_cars(session)
        elif choice == 2:
            search_by_criteria(session)
        elif choice == 3:
            set_appointment(session, user)
        elif choice == 4:
            get_estimate()
        elif choice == 5:
            click.echo('Goodbye!')
            break
        else:
            click.echo('Invalid choice. Please try again.')

def display_available_cars(session):
    available_cars = session.query(Car).filter_by(status='Available').all()

    if available_cars:
        click.echo('Available Cars:')
        for car in available_cars:
            click.echo(f'{car.make} {car.model}, Year: {car.year}, Price: {car.price}')

    else:
        click.echo('No available cars at the moment.')

def search_by_criteria(session):
    model = click.prompt('Enter the model')
    make = click.prompt('Enter the make')
    
    cars = session.query(Car).filter_by(model=model, make=make).all()

    if cars:
        click.echo(f'Found {len(cars)} cars matching your criteria:')
        for car in cars:
            click.echo(f'{car.make} {car.model}, Year: {car.year}, Price: {car.price}')
    else:
        click.echo('No cars matching the criteria.')

def set_appointment(session, user):
    make = click.prompt('Enter the car make')
    model = click.prompt('Enter the car model')
    date_time = click.prompt('Enter the appointment date and time (YYYY-MM-DD HH:MM)')
    appointment_type = click.prompt('Enter the appointment type (e.g., Test Drive)')

    car = session.query(Car).filter_by(make=make, model=model).first()

    if car is None:
        click.echo('Car not found.')
        return

    appointment = Appointment(user=user, car=car, date_time=datetime.strptime(date_time, '%Y-%m-%d %H:%M'), type_appointment=appointment_type, status='Scheduled')
    session.add(appointment)
    session.commit()

    click.echo('Appointment set successfully!')

def get_estimate():
    car_price = click.prompt('Enter the car price', type=float)
    downpayment = click.prompt('Enter the downpayment amount', type=float)

    monthly_payment, total_payment = calculate_estimate(car_price, downpayment)
    click.echo(f'Estimated Monthly Payment: ${monthly_payment:.2f}')
    click.echo(f'Total Payment over 48 months: ${total_payment:.2f}')

@click.group()
def main():
    """CarBud: Your Virtual Dealership"""
    pass

@main.command()
@click.option('--username', prompt=True)
def menu(username):
    session = Session()
    user = get_user(session, username)

    if user:
        display_menu(session, user)
    else:
        click.echo('User not found. Would you like to register? [y/N]')
        if click.confirm(''):
            register_user(session, username)
            user = get_user(session, username)
            display_menu(session, user)

if __name__ == '__main__':
    menu()
