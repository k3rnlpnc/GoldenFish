from sqlalchemy import Column, Integer, String, Date
from config import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(40))
    password = Column(String(20))
    username = Column(String(30))
    name = Column(String(20))
    surname = Column(String(20))
    birthday = Column(Date, nullable=True)

    def __init__(self, _email, _password, _username, _name, _surname, _dob=None):
        self.email = _email
        self.password = _password
        self.username = _username
        self.name = _name
        self.surname = _surname
        self.birthday = _dob

    def get_id(self) -> int:
        return self.id

    def get_email(self) -> str:
        return self.email

    def set_email(self, _email):
        self.email = _email
