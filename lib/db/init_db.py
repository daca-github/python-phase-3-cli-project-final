from db.database import engine, Base
from db.models import User, Car, Interest, Price, Appointment

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
