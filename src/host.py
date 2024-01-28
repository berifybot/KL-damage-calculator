from abc import ABC, abstractmethod

class Host(ABC):
    @abstractmethod
    def get_roll(self) -> int:
        pass