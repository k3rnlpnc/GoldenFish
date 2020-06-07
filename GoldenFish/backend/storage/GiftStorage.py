from backend.config import session
from backend.storage.BaseStorage import BaseStorage
from backend.models.Gift import Gift


class GiftStorage(BaseStorage):
    model = Gift

    def get_giver(self):
        pass

    def add_gift(self):
        pass

    def update_gift(self):
        pass

    def delete_gift(self):
        pass

    def get_all(self):
        pass