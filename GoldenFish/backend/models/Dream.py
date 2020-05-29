from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from backend.config import Base


class Dream(Base):
    __tablename__ = 'dream'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String)
    description = Column(String, nullable=True)
    image_link = Column(String, nullable=True)
    store_link = Column(String, nullable=True)
    is_fulfilled = Column(Boolean)

    def __init__(self, _owner_id, _name, _is_fulfilled, _description=None, _image_link=None, _store_link=None):
        self.owner_id = _owner_id
        self.name = _name
        self.is_fulfilled = False
        self.description = _description
        self.image_link = _image_link
        self.store_link = _store_link

    def get_id(self) -> int:
        return self.id

    def get_owner_id(self) -> int:
        return self.owner_id

    def set_name(self, _name):
        self.name = _name

    def set_description(self, _description):
        self.description = _description
