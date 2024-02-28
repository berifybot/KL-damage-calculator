import math
from entity import Entity
from battle_host import BattleHost
from attack_stats import AttackStats
from roll_stats import RollStats
from status_stats import StatusesStats

class Attack():

    def __init__(self, host: BattleHost, attacker: Entity, target: Entity):
        self.host = host
        self.attacker = attacker
        self.target = target
        self.roll_stats = RollStats()
        self.statuses_stats = StatusesStats()
        self.attack_stats = AttackStats(attacker, target)

    def attack(self) -> AttackStats:
        roll = self.host.roll()
        self.roll_stats.set_base_roll(roll)
        damage_dealt = self.execute_roll(roll) 
        self.attack_stats.set_damage_dealt(damage_dealt, self.attacker.weapon)
        self.attack_stats.set_roll_stats(self.roll_stats)
        self.__end_of_roll_status_handling__()
        self.attack_stats.set_statuses_stats(self.statuses_stats)
        self.host.report_roll_stats(self.attack_stats)

    def execute_roll(self, roll) -> int:
        damage_dealt = self.__get_damage_from_roll__(roll)
        if self.target.is_weak_to_element(self.attacker.weapon.get_element()):
            self.roll_stats.set_hit_weakness(True)
            damage_dealt += 10
            self.target.take_damage(self.attacker.weapon, damage_dealt)
            return damage_dealt
        else:
            self.target.take_damage(self.attacker.weapon, damage_dealt)
            return damage_dealt

    def __get_damage_from_roll__(self, roll) -> int:
        base_dmg = self.attacker.weapon.base_damage
        if (roll == 1):
            return 0
        elif (roll == 2):
            return 0
        elif (roll == 3):
            return math.floor(base_dmg / 2)
        elif (roll == 4):
            return base_dmg
        elif (roll == 5):
            self.__handle_status_roll__(5)
            return base_dmg + 3
        elif (roll == 6):
            self.__handle_status_roll__(6)
            return base_dmg + 5
        else:
            raise Exception("Invalid roll value")
        
    def __handle_status_roll__(self, base_roll):
        status_roll = self.host.roll()
        self.roll_stats.set_critical_roll(status_roll)
        if (self.__did_status_apply__(base_roll, status_roll)):
            element_stats = self.attacker.weapon.element.apply_status(self.attacker, self.target)
            self.roll_stats.set_element_stats(element_stats)
        
    def __did_status_apply__(self, base_roll, status_roll) -> bool:
        if (base_roll == 5):
            did_apply = self.__handle_base_roll_5__(status_roll)
            self.roll_stats.set_did_crit(did_apply)
            return did_apply
        elif (base_roll == 6):
            did_apply = self.__handle_base_roll_6__(status_roll)
            self.roll_stats.set_did_crit(did_apply)
            return did_apply
        return False
    
    def __handle_base_roll_5__(self, status_roll) -> bool:
        if (self.attacker.weapon.element.has_low_chance()):
            return False
        if (self.attacker.has_increased_status_effect_chance()):
            if (status_roll == 5):
                return True
        if (status_roll == 6):
            return True
        return False
    
    def __handle_base_roll_6__(self, status_roll) -> bool:
        if (self.attacker.has_increased_status_effect_chance()):
            if (status_roll == 4):
                return True
        if (status_roll == 5):
            return True
        if (status_roll == 6):
            return True
        return False
    
    def __end_of_roll_status_handling__(self) -> None:
        self.attacker.handle_end_of_turn_statuses(self.statuses_stats)
        self.target.handle_end_of_turn_statuses(self.statuses_stats)
