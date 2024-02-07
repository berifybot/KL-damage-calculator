from typing import List
from roll import Roll
import math
from damage_source import Weapon, Element, AttackType

class Entity():
    def __init__(self, name: str, max_health: int, weapon: Weapon, weaknesses: List[Element] = []):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.weapon = weapon
        self.weaknesses = weaknesses

    def get_name(self) -> str:
        return self.name
    
    def get_max_health(self) -> int:
        return self.max_health
    
    def get_current_health(self) -> int:
        return self.current_health
    
    def get_weapon(self) -> Weapon:
        return self.weapon

    def get_weaknesses(self) -> List[Element]:
        return self.weaknesses
    
    def attack(self, target, host) -> None:
        roll = Roll().random_roll()
        damage_dealt = self.execute_roll(roll, target)
        host.report_roll_stats(2, damage_dealt, target)

    def execute_roll(self, roll, target) -> int:
        damage_dealt = self.__get_damage_from_roll(roll)
        if self.weapon.attack_type in target.weaknesses:
            damage_dealt += 10
            target.current_health -= damage_dealt
            return damage_dealt
        else:
            target.current_health -= damage_dealt
            return damage_dealt

    def __get_damage_from_roll(self, roll) -> int:
        if (roll == 1):
            return 0
        elif (roll == 2):
            return 0
        elif (roll == 3):
            return math.floor(self.weapon.base_damage / 2)
        elif (roll == 4):
            return self.weapon.base_damage
        elif (roll == 5):
            return self.weapon.base_damage + 3
        elif (roll == 6):
            return self.weapon.base_damage + 5
        else:
            raise Exception("Invalid roll value")
    
class Player(Entity):
    def __init__(self, name: str, max_health: int, weapon: Weapon, attack_speed: int, weaknesses: List[Element] = []):
        super().__init__(name, max_health, weapon, weaknesses)
        self.attack_speed = attack_speed

    def get_attack_speed(self) -> int:
        return self.attack_speed

NAME = "name"
MAX_HEALTH = "max_health"
DAMAGE_SOURCE = "damage_source"
WEAKNESSES = "weaknesses"

class Enemy(Entity):

    @classmethod
    def __invalid_enemy_exception__(cls, prop) -> str:
        raise Exception("Invalid enemy, missing '{prop}'".format(prop = prop))

    @classmethod
    def from_dict(cls, enemy_dict: dict):
        # TODO: Try to implement a schema validator? This seems messy still
        if (NAME not in enemy_dict):
            cls.__invalid_enemy_exception__(NAME)
        if (MAX_HEALTH not in enemy_dict):
            cls.__invalid_enemy_exception__(MAX_HEALTH)
        if (DAMAGE_SOURCE not in enemy_dict):
            cls.__invalid_enemy_exception__(DAMAGE_SOURCE)
        if (WEAKNESSES not in enemy_dict):
            cls.__invalid_enemy_exception__(WEAKNESSES)
        
        weapon = Weapon.from_dict(enemy_dict["damage_source"])
        return Enemy(enemy_dict['name'], enemy_dict['max_health'], weapon,
                     enemy_dict['weaknesses']) 