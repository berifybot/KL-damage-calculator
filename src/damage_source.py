from element import Element

class AttackType():

    UNKNOWN = "unknown"
    MELEE = "melee"
    RANGE = "range"
    MAGIC = "magic"
    ABILITY = "ability"
    types = [MELEE, RANGE, MAGIC, ABILITY]

    def __init__(self, type: str) -> None:
        if (type.lower() not in self.types):
            self.type = self.UNKNOWN
        self.type = type.lower()

    def get_type(self) -> str:
        return self.type

    @classmethod
    def is_type_valid(cls, type: str) -> bool:
        return type.lower() in cls.types

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

    def __init__(self, name: str, base_damage: int, element: Element, attack_type: str):
        super().__init__(name, base_damage, element)
        self.attack_type = AttackType(attack_type)
    
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
                      Element.create(dict['element']),
                      dict['damage_type'])
        
    
class Ability(DamageSource):
    # TODO
    pass