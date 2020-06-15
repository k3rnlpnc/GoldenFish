from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://oxlusapabhafxw:07d1637d85f836d7e6e93fae1f8f011e986e031de55a6edac909e1007d198c08@ec2-52-72-221-20.compute-1.amazonaws.com:5432/d56b5lkri5d5rj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'salt4567$%&'

engine = create_engine('postgres://oxlusapabhafxw:07d1637d85f836d7e6e93fae1f8f011e986e031de55a6edac909e1007d198c08@ec2-52-72-221-20.compute-1.amazonaws.com:5432/d56b5lkri5d5rj')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()