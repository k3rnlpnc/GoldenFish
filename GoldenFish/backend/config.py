from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:fyrfyr@localhost:5432/goldenfish1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'salt4567$%&'

engine = create_engine('postgresql://postgres:fyrfyr@localhost:5432/goldenfish1')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()