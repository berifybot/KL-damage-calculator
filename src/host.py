from abc import ABC, abstractmethod

class Host(ABC):
    @abstractmethod
    def run(self) -> None:
        pass