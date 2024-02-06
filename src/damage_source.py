from enum import Enum

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

class DamageSource():
    def __init__(self, name: str, base_damage: int, element: Element):
        self.name = name
        self.base_damage = base_damage
        self.element = element

    def get_name(self) -> str:
        return self.name
    
    def get_base_damage(self) -> int:
        return self.base_damage
    
    def get_element(self) -> Element:
        return self.element
    
NAME = "name"
BASE_DAMAGE = "base_damage"
ELEMENT = "element"
DAMAGE_TYPE = "damage_type"

class Weapon(DamageSource):
    def __init__(self, name: str, base_damage: int, element: Element, attack_type: AttackType):
        super().__init__(name, base_damage, element)
        self.attack_type = attack_type
    
    def get_attack_type(self) -> AttackType:
        return self.attack_type
    
    @classmethod
    def __invalid_weapon_exception__(cls, prop) -> str:
        raise Exception("Invalid Weapon, missing '{prop}'".format(prop = prop))
    
    @classmethod
    def from_dict(cls, dict: dict):
        if (NAME not in dict):
            cls.__invalid_weapon_exception__(NAME)
        if (BASE_DAMAGE not in dict):
            cls.__invalid_weapon_exception__(BASE_DAMAGE)
        if (ELEMENT not in dict):
            cls.__invalid_weapon_exception__(ELEMENT)
        if (DAMAGE_TYPE not in dict):
            cls.__invalid_weapon_exception__(DAMAGE_TYPE)
        return Weapon(dict['name'],
                      dict['base_damage'],
                      getattr(Element, dict['element']),
                      getattr(AttackType, dict['damage_type']))
        
    
class Ability(DamageSource):
    # TODO
    pass

test_weapon = {
    "name": "test_weapon",
    "base_damage": 25,
    "element": "Fire",
    "damage_type": "Melee"
}

weapon = Weapon.from_dict(test_weapon)
print(weapon.name, weapon.base_damage, weapon.element, weapon.attack_type)
