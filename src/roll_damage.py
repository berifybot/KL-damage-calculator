import math
from damage_source import DamageSource
from entity import Entity
from battle_host import BattleHost
from roll_stats import RollStats 

class RollDamage:

    def __init__(self, host: BattleHost, attacker: Entity, target: Entity):
        self.host = host
        self.attacker = attacker
        self.target = target
        self.roll_stats = RollStats()

    def get_damage_from_roll(self) -> RollStats:
        initial_roll = self.__get_initial_roll__()
        dmg_source = self.attacker.weapon
        base_dmg = dmg_source.base_damage
        if (initial_roll == 1):
            self.__update_damage__(0, dmg_source)
        elif (initial_roll == 2):
            self.__update_damage__(0, dmg_source)
        elif (initial_roll == 3):
            dmg = math.floor(base_dmg / 2) 
            self.__update_damage__(dmg, dmg_source)
        elif (initial_roll == 4):
            self.__update_damage__(base_dmg, dmg_source)
        elif (initial_roll == 5):
            self.__handle_status_roll__(5)
            self.__update_damage__(base_dmg + 3, dmg_source)
        elif (initial_roll == 6):
            self.__handle_status_roll__(6)
            self.__update_damage__(base_dmg + 5, dmg_source)
        else:
            raise Exception("Invalid roll value") 
        return self.roll_stats
    
    def __get_initial_roll__(self) -> int:
        initial_roll = self.host.roll()
        self.roll_stats.base_roll = initial_roll
        return initial_roll
    
    def __update_damage__(self, dmg: int, source: DamageSource) -> None:
        self.roll_stats.damage_dealt = dmg
        self.roll_stats.damage_source = source

    def __handle_status_roll__(self, base_roll):
        status_roll = self.__get_critical_roll__()
        if (self.__did_status_apply__(base_roll, status_roll)):
            element_stats = self.attacker.weapon.element.apply_status(self.attacker, self.target)
            self.roll_stats.set_element_stats(element_stats)

    def __get_critical_roll__(self) -> int:
        critical_roll = self.host.roll()
        self.roll_stats.critical_roll = critical_roll
        return critical_roll
        
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