from abc import ABC, abstractmethod

class UserInteractionInterface(ABC):
    @abstractmethod
    def update_name(self, user_id, name):
        pass

    @abstractmethod
    def update_age(self, user_id, age):
        pass
