from db.database import SessionLocal
from db.models import Car

def add_car(make, model, year, color, price, status, car_type):
    session = SessionLocal()

    car = Car(make=make, model=model, year=year, color=color, price=price, status=status, type=car_type)
    session.add(car)
    session.commit()
    session.close()

if __name__ == "__main__":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    color = input("Enter car color: ")
    price = int(input("Enter car price: "))
    car_type = input("Enter car type: ")
    status = 'Available'

    add_car(make, model, year, color, price, status, car_type)
    print("Car added successfully!")
