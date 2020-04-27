from abc import ABCMeta, abstractmethod, abstractproperty


class IController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def check_user_validity(self):
        pass

    @abstractmethod
    def bad_request(self):
        pass

    @abstractmethod
    def ok(self):
        pass
