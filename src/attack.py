import math
from entity import Entity
from element import Element
from battle_host import BattleHost

class Attack():

    def __init__(self, host: BattleHost, attacker: Entity, target: Entity):
        self.host = host
        self.attacker = attacker
        self.target = target

    def attack(self):
        roll = self.host.roll()
        damage_dealt = self.execute_roll(roll)
        self.host.report_roll_stats(roll, damage_dealt, self.target)

    def execute_roll(self, roll) -> int:
        damage_dealt = self.__get_damage_from_roll__(roll)
        if self.target.is_weak_to_element(self.attacker.weapon.get_element()):
            damage_dealt += 10
            self.target.current_health -= damage_dealt
            return damage_dealt
        else:
            self.target.current_health -= damage_dealt
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
        if (self.__did_status_apply__(base_roll, status_roll)):
            self.attacker.weapon.element.apply_status(self.attacker, self.target)
        
    def __did_status_apply__(self, base_roll, status_roll) -> bool:
        if (base_roll == 5):
            return self.__handle_base_roll_5__(status_roll)
        elif (base_roll == 6):
            return self.__handle_base_roll_6__(status_roll)
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