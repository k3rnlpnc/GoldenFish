from sqlalchemy import Column, Integer, ForeignKey, Table
from backend.config import Base

friends_association = Table('friends', Base.metadata,
                            Column('friend_one_id', Integer, ForeignKey('user.id')),
                            Column('friend_two_id', Integer, ForeignKey('user.id'))
                            )
