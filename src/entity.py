from enum import Enum
from typing import List

class AttackType(Enum):
    Range = 1
    Mage = 2
    Melee = 3

class Element(Enum):
    Fire = 1
    Water = 2
    Lightning = 3
    Earth = 4
    Light = 5
    Dark = 6
    Ice = 7
    Wind = 8

class Weapon():
    def __init__(self, name: str, base_damage: int, attack_type: AttackType, element: Element):
        self.name = name
        self.base_damage = base_damage
        self.attack_type = attack_type
        self.element = element

    def get_name(self) -> str:
        return self.name
    
    def get_base_damage(self) -> int:
        return self.base_damage
    
    def get_element(self) -> Element:
        return self.element
    
    def get_attack_type(self) -> AttackType:
        return self.attack_type


class Entity():
    def __init__(self, name: str, max_health: int, base_damage: int, damage_type: str, weaknesses: List[str] = []):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        # TODO: remove the following two types in favor of using weapon
        self.base_damage = base_damage
        self.damage_type = damage_type
        # self.weapon = weapon
        self.weaknesses = weaknesses

    def get_name(self) -> str:
        return self.name
    
    def get_max_health(self) -> int:
        return self.max_health
    
    def get_current_health(self) -> int:
        return self.current_health
    
    # def get_weapon(self) -> Weapon:
    #     return self.get_weapon

    def get_base_damage(self) -> int:
        return self.base_damage
    
    def get_damage_type(self) -> str:
        return self.damage_type
    
    # TODO: Change this to be a list of 'Elements'
    def get_weaknesses(self) -> List[str]:
        return self.weaknesses