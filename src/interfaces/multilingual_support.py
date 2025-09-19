from abc import ABC, abstractmethod

class MultilingualSupportInterface(ABC):
    @abstractmethod
    def translate(self, text, target_language):
        pass
