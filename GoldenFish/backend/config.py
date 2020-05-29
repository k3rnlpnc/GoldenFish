from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:5432@localhost:5432/goldenfish')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class SecurityConfig:
    SECRET_KEY = 'salt4567$%&'
