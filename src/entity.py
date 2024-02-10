from typing import List
from damage_source import Weapon
from element import Element

class Entity():

    statuses: List[str] = []

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
    
    def add_status(self, status: str) -> None:
        self.statuses.append(status)
    
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