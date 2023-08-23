from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    
    cars_interested = relationship("Interest", back_populates="user")
    price_calculations = relationship("Price", back_populates="user")
    appointments = relationship("Appointment", back_populates="user")


class Car(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    
    users_interested = relationship("Interest", back_populates="car")
    price_calculations = relationship("Price", back_populates="car")
    appointments = relationship("Appointment", back_populates="car")

class Interest(Base):
    __tablename__ = 'use_car_interest'

    interest_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    car_id = Column(Integer, ForeignKey('cars.car_id'))
    interest_level = Column(String, nullable=False)

    user = relationship("User", back_populates="cars_interested")
    car = relationship("Car", back_populates="users_interested")

class Price(Base):
    __tablename__ = 'price_calc'

    calc_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    car_id = Column(Integer, ForeignKey('cars.car_id'))
    down_payment = Column(Integer, nullable=False)
    monthly_loan = Column(Integer, nullable=False)
    total_loan = Column(Integer, nullable=False)
    
    user = relationship("User", back_populates="price_calculations")
    car = relationship("Car", back_populates="price_calculations")

class Appointment(Base):
    __tablename__ = 'appointment'

    appointment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    car_id = Column(Integer, ForeignKey('cars.car_id'))
    date_time = Column(DateTime, nullable=False)
    type_appointment = Column(String, nullable=False)
    status = Column(String, nullable=False)
    
    user = relationship("User", back_populates="appointments")
    car = relationship("Car", back_populates="appointments")
