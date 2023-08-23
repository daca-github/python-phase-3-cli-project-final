from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 

DATABASE_URL = os.path.join(os.path.dirname(__file__), 'carbud.db')
engine = create_engine(f"sqlite:///{DATABASE_URL}")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
