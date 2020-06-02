from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.config import Base, session


class Dream(Base):
    __tablename__ = 'dream'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image_link = Column(String, nullable=True)
    store_link = Column(String, nullable=True)
    is_fulfilled = Column(Boolean)

    def __init__(self, **kwargs):
        self.owner_id = kwargs.get('owner_id')
        self.name = kwargs.get('name')
        self.is_fulfilled = False
        self.description = kwargs.get('description')
        self.image_link = kwargs.get('image_link')
        self.store_link = kwargs.get('store_link')

    def get_id(self) -> int:
        return self.id

    def get_owner_id(self) -> int:
        return self.owner_id

    def set_name(self, _name):
        self.name = _name

    def set_description(self, _description):
        self.description = _description

    # Repo methods

    def save(self):
        try:
            session.add(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def update(self, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
            session.commit()
        except Exception:
            session.rollback()
            raise

    def delete(self):
        try:
            session.delete(self)
            session.commit()
        except Exception:
            session.rollback()
            raise

    @classmethod
    def get_by_id(cls, user_id, dream_id):
        try:
            dream = cls.query.filter_by(owner_id=user_id, id=dream_id).first()
            if not dream:
                raise Exception('Not found this dream')
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dream

    @classmethod
    def get_all(cls, user_id):
        try:
            dreams = cls.query.filter_by(owner_id=user_id).all()
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dreams

