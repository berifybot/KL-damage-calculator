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


class Element():

    UNKNOWN = "unknown"
    FIRE = "fire"
    WATER = "water"
    LIGHTNING = "lightning"
    EARTH = "earth"
    LIGHT = "light"
    DARK = "dark"
    ICE = "ice"
    WIND = "wind"
    types = [FIRE, WATER, LIGHTNING, EARTH, LIGHT, DARK, ICE, WIND]

    def __init__(self, type):
        self.type = type

    def get_type(self) -> str:
        return self.type

    def apply_status(self, attacker, target) -> None:
        pass

    @classmethod
    def create(cls, type: str) -> None:
        match type.lower():
            case cls.FIRE:
                return FireElement()
            case cls.WATER:
                return WaterElement()
            case cls.LIGHTNING:
                return LightningElement()
            case cls.EARTH:
                return EarthElement()
            case cls.LIGHT:
                return LightElement()
            case cls.DARK:
                return DarkElement()
            case cls.ICE:
                return IceElement()
            case cls.WIND:
                return WindElement()
            case _:
                return None
            
class WaterElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WATER)

    def apply_status(self, attacker, target) -> None:
        pass

class FireElement(Element):

    def __init__(self) -> None:
        super().__init__(self.FIRE)

    def apply_status(self, attacker, target) -> None:
        pass

class LightningElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHTNING)

    def apply_status(self, attacker, target) -> None:
        pass

class EarthElement(Element):

    def __init__(self) -> None:
        super().__init__(self.EARTH)

    def apply_status(self, attacker, target) -> None:
        pass

class LightElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHT)

    def apply_status(self, attacker, target) -> None:
        pass

class DarkElement(Element):

    def __init__(self) -> None:
        super().__init__(self.DARK)

    def apply_status(self, attacker, target) -> None:
        pass

class IceElement(Element):

    def __init__(self) -> None:
        super().__init__(self.ICE)

    def apply_status(self, attacker, target) -> None:
        pass

class WindElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WIND)

    def apply_status(self, attacker, target) -> None:
        pass


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