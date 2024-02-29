from entity import Entity
from roll_stats import RollStats
from status_stats import StatusesStats
from damage_source import DamageSource

class AttackStats:

    def __init__(self, attacker: Entity, target: Entity):
        self.attacker = attacker
        self.target = target
        self.damage_dealt = 0
        self.damage_source = None
        self.status_applied = None
        self.hit_weakness = False
        self.base_roll = 0
        self.critical_roll = 0
        self.did_crit = False
        self.statuses_stats = None

    def set_roll_stats(self, roll_stats: RollStats) -> None:
        self.status_applied = roll_stats.get_applied_status()
        self.hit_weakness = roll_stats.get_hit_weakness()
        self.base_roll = roll_stats.get_base_roll()
        self.critical_roll = roll_stats.get_critical_roll()
        self.did_crit = roll_stats.get_did_crit()
        self.damage_source = roll_stats.get_damage_source()
        self.damage_dealt = roll_stats.get_damage_dealt()

    def set_statuses_stats(self, statuses_stats: StatusesStats) -> None:
        self.statuses_stats = statuses_stats

    def get_total_damage(self) -> int:
        status_damage = self.__get_status_damage__()
        return status_damage + self.damage_dealt

    def __get_status_damage__(self) -> int:
        total = 0
        for status in self.statuses_stats.statuses:
            total += status.damage_dealt
        return total
