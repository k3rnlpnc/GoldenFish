from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from backend.config import Base


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    dream_id = Column(Integer, ForeignKey('dream.id'))
    giver_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, _dream_id, _giver_id):
        self.dream_id = _dream_id
        self.giver_id = _giver_id

    def get_id(self) -> int:
        return self.id

    def get_giver_id(self) -> int:
        return self.giver_id

    def get_dream_id(self) -> int:
        return self.dream_id
