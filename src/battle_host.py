from abc import ABC, abstractmethod
from attack_stats import AttackStats

class BattleHost(ABC):

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
    def roll(self) -> int:
        pass

    @abstractmethod
    def report_roll_stats(self, attack_stats: AttackStats):
        pass