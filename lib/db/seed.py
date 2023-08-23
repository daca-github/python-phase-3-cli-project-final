from database import SessionLocal as Session
from models import User, Car


def seed_data():
    session = Session()

    user1 = User(username="daniel")
    user2 = User(username="maria")

    car1 = Car(make="Toyota", model="Camry", color="Black", year=2024, price=24000, status="Available")
    car2 = Car(make="Honda", model="Civic", color="Red", year=2020, price=21000, status="Available")

    session.add(user1)
    session.add(user2)
    session.add(car1)
    session.add(car2)

    session.commit()
    session.close()

if __name__ == "__main__":
    seed_data()
