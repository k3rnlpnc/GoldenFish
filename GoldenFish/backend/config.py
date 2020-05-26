from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:fyrfyr@localhost:5432/goldenfish')


class SecurityConfig:
    SECRET_KEY = 'salt4567$%&'
