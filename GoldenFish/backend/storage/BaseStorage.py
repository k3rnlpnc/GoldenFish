from backend.config import session


class BaseStorage:
    @classmethod
    def save(cls, obj):
        try:
            session.add(obj)
            session.commit()
        except Exception:
            session.rollback()
            raise

    @classmethod
    def update(cls, obj, **kwargs):
        try:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            session.commit()
        except Exception:
            session.rollback()
            raise

    @classmethod
    def remove(cls, obj):
        try:
            session.delete(obj)
            session.commit()
        except Exception:
            session.rollback()
            raise
