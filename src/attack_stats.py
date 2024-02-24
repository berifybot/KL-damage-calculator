from entity import Entity
from roll_stats import RollStats

class AttackStats:

    def __init__(self, attacker: Entity, target: Entity):
        self.attacker = attacker
        self.target = target
        self.damage_dealt = 0
        self.status_applied = ""
        self.hit_weakness = False
        self.base_roll = 0
        self.critical_roll = 0
        self.did_crit = False

    def set_damage_dealt(self, damage) -> None:
        self.damage_dealt = damage

    def set_roll_stats(self, roll_stats: RollStats) -> None:
        self.status_applied = roll_stats.get_applied_status()
        self.hit_weakness = roll_stats.get_hit_weakness()
        self.base_roll = roll_stats.get_base_roll()
        self.critical_roll = roll_stats.get_critical_roll()
        self.did_crit = roll_stats.get_did_crit()
