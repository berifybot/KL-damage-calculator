from entity import Entity
from roll_stats import RollStats
from status_stats import StatusesStats

class AttackStats:

    def __init__(self, attacker: Entity, target: Entity):
        self.attacker = attacker
        self.target = target
        self.damage_dealt = 0
        self.status_applied = None
        self.hit_weakness = False
        self.base_roll = 0
        self.critical_roll = 0
        self.did_crit = False
        self.statuses_stats = None

    def set_damage_dealt(self, damage) -> None:
        self.damage_dealt = damage

    def set_roll_stats(self, roll_stats: RollStats) -> None:
        self.status_applied = roll_stats.get_applied_status()
        self.hit_weakness = roll_stats.get_hit_weakness()
        self.base_roll = roll_stats.get_base_roll()
        self.critical_roll = roll_stats.get_critical_roll()
        self.did_crit = roll_stats.get_did_crit()

    def set_statuses_stats(self, statuses_stats: StatusesStats) -> None:
        self.statuses_stats = statuses_stats
