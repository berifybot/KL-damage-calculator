from entity import Entity
from battle_host import BattleHost
from attack_stats import AttackStats
from roll_stats import RollStats
from status_stats import StatusesStats
from roll_damage import RollDamage

class Attack():

    def __init__(self, host: BattleHost, attacker: Entity, target: Entity):
        self.host = host
        self.attacker = attacker
        self.target = target
        self.statuses_stats = StatusesStats()
        self.attack_stats = AttackStats(attacker, target)

    def attack(self) -> AttackStats:
        roll_stats = self.execute_roll() 
        self.attack_stats.set_roll_stats(roll_stats)
        self.__end_of_roll_status_handling__()
        self.attack_stats.set_statuses_stats(self.statuses_stats)
        self.host.report_roll_stats(self.attack_stats)

    def execute_roll(self) -> RollStats:
        roll_stats = self.__get_damage_from_roll__()
        # Move this logic to entity
        if self.target.is_weak_to_element(self.attacker.weapon.get_element()):
            roll_stats.set_hit_weakness(True)
            roll_stats.damage_dealt += 10
            self.target.take_damage(self.attacker.weapon, roll_stats.damage_dealt)
        else:
            self.target.take_damage(self.attacker.weapon, roll_stats.damage_dealt)
        return roll_stats
        
    def __get_damage_from_roll__(self) -> RollStats:
        return RollDamage(
            self.host,
            self.attacker,
            self.target).get_damage_from_roll()

    def __end_of_roll_status_handling__(self) -> None:
        self.attacker.handle_end_of_turn_statuses(self.statuses_stats)
        self.target.handle_end_of_turn_statuses(self.statuses_stats)
