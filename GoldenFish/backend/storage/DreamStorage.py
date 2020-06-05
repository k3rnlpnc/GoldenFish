from backend.config import session
from backend.storage.BaseStorage import BaseStorage
from backend.models.Dream import Dream


class DreamStorage(BaseStorage):
    model = Dream

    def get_gifts(self, giver_id):
        try:
            dreams = self.model.query.filter_by(giver_id=giver_id, is_fulfilled=False).all()
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dreams

    def get_gift(self, giver_id, dream_id):
        try:
            gift = self.model.query.filter_by(id=dream_id, giver_id=giver_id, is_fulfilled=False).first()
            session.commit()
        except Exception:
            session.rollback()
            raise
        return gift

    def get_fulfilled_dreams(self, user_id):
        try:
            dreams = self.model.query.filter_by(owner_id=user_id, is_fulfilled=True).all()
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dreams

    def get_unfulfilled_dreams(self, user_id):
        try:
            dreams = self.model.query.filter_by(owner_id=user_id, is_fulfilled=False).all()
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dreams

    def get_all(self, user_id):
        try:
            dreams = self.model.query.filter_by(owner_id=user_id).all()
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dreams

    def get_by_id(self, user_id, dream_id):
        try:
            dream = self.model.query.filter_by(owner_id=user_id, id=dream_id).first()
            if not dream:
                raise Exception('Not found this dream')
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dream

    def get_by_id_only(self, dream_id):
        try:
            dream = self.model.query.filter_by(id=dream_id).first()
            if not dream:
                raise Exception('Not found this dream')
            session.commit()
        except Exception:
            session.rollback()
            raise
        return dream
