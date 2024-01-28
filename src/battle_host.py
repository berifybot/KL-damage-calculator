from abc import ABC, abstractmethod

class BattleHost(ABC):

    @abstractmethod
    def get_roll(self) -> int:
        pass

    @abstractmethod
    def get_attack_speed(self) -> int:
        pass

    @abstractmethod
    def get_damage_per_roll(self) -> int:
        pass

    @abstractmethod
    def get_attack_type(self) -> str:
        pass

    @abstractmethod
    def report_roll_stats(self, roll_value, damage_dealt, enemy):
        pass