from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from backend.config import Base


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    dream_id = Column(Integer, ForeignKey('dream.id'))
    dream = relationship("Dream", backref=backref("gift", uselist=False))
    dreamer_id = Column(Integer, ForeignKey('user.id'))
    giver_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, _dream, _dreamer_id, _giver_id):
        self.dream = _dream
        self.dreamer_id = _dreamer_id
        self.giver_id = _giver_id

    def get_id(self) -> int:
        return self.id

    def get_dreamer_id(self) -> int:
        return self.dreamer_id

    def get_giver_id(self) -> int:
        return self.giver_id

    def get_dream_id(self) -> int:
        return self.dream_id
