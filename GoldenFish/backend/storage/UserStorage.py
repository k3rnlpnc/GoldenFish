from passlib.hash import bcrypt

from backend.config import session
from backend.storage.BaseStorage import BaseStorage
from backend.models.User import User


class UserStorage(BaseStorage):
    model = User

    def get_by_id(self, user_id):
        try:
            user = self.model.query.filter_by(id=user_id).first()
            if not user:
                raise Exception('Not found user')
            session.commit()
        except Exception:
            session.rollback()
            raise
        return user

    def get_by_username(self, username):
        try:
            user = self.model.query.filter_by(username=username).first()
            if not user:
                raise Exception('Not found user')
            session.commit()
        except Exception:
            session.rollback()
            raise
        return user

    def authenticate(self, email, password):
        user = self.model.query.filter_by(email=email).first()
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this email or/and password')
        return user