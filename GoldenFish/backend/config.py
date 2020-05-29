from sqlalchemy import create_engine

<<<<<<< HEAD
engine = create_engine('postgresql://postgres:5432@localhost:5432/goldenfish')
Session = sessionmaker(bind=engine)
=======
engine = create_engine('postgresql://postgres:fyrfyr@localhost:5432/goldenfish')
>>>>>>> 0c4968a9654cd5361c44870c680c5c38428e7883


class SecurityConfig:
    SECRET_KEY = 'salt4567$%&'
