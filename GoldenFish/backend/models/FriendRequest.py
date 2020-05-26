from sqlalchemy import Column, Integer, ForeignKey, Table
from backend.config import Base

friend_requests_association = Table('friend_requests', Base.metadata,
                            Column('sender_id', Integer, ForeignKey('user.id')),
                            Column('recipient_id', Integer, ForeignKey('user.id'))
                            )
