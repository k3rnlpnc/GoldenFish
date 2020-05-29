from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from sqlalchemy.ext.declarative import declarative_base

#from backend.app import db
from backend.config import Base
from backend.models.Friend import friends_association
from backend.models.FriendRequest import friend_requests_association

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(40))
    password = Column(String(20))
    username = Column(String(30))
    name = Column(String(20))
    surname = Column(String(20))
    birthday = Column(Date, nullable=True)

    friends = relationship("User", secondary=friends_association)
    friend_requests = relationship("User", secondary=friend_requests_association)
    gifts = relationship("Gift", backref="user", lazy=True)
    dreams = relationship("Dream", backref="user", lazy=True)

    def __init__(self, **kwargs):
        self.email = kwargs.get('email')
        self.password = generate_password_hash(kwargs.get('password'))
        self.username = kwargs.get('username')
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.birthday = kwargs.get('dob')

    def get_id(self) -> int:
        return self.id

    def get_email(self) -> str:
        return self.email

    def set_email(self, _email):
        self.email = _email

    def check_password(self, _password):
        return check_password_hash(self.password, _password)

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not check_password_hash(password, user.password):
            raise Exception('No user with this email or/and password')
        return user
