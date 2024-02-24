from element_stats import ElementStats
from status import Status

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
        if not self.is_type_valid(type):
            self.type = self.UNKNOWN
        self.type = type

    def get_type(self) -> str:
        return self.type

    def apply_status(self, attacker, target) -> ElementStats:
        pass

    def has_low_chance(self) -> bool:
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
            
    @classmethod
    def is_type_valid(cls, type: str) -> bool:
        return type.lower() in cls.types
            
class WaterElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WATER)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("slip")
        target.add_status(applied_status)
        return ElementStats(applied_status)

    def has_low_chance(self) -> bool:
        return False

class FireElement(Element):

    def __init__(self) -> None:
        super().__init__(self.FIRE)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("burn")
        target.add_status(applied_status)
        return ElementStats(applied_status)

    def has_low_chance(self) -> bool:   
        return False

class LightningElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHTNING)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("paralyze")
        target.add_status(applied_status)
        return ElementStats(applied_status)
    
    def has_low_chance(self) -> bool:
        return True


class EarthElement(Element):

    def __init__(self) -> None:
        super().__init__(self.EARTH)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("rooted")
        target.add_status(applied_status)
        return ElementStats(applied_status)

    def has_low_chance(self) -> bool:
        return False

class LightElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHT)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("blessed")
        attacker.add_status(applied_status)
        return ElementStats(applied_status)

    def has_low_chance(self) -> bool:
        return False

class DarkElement(Element):

    def __init__(self) -> None:
        super().__init__(self.DARK)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("rooted")
        target.add_status(applied_status)
        return ElementStats(applied_status)

    def has_low_chance(self) -> bool:
        return False

class IceElement(Element):

    def __init__(self) -> None:
        super().__init__(self.ICE)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("cursed")
        target.add_status(applied_status)
        return ElementStats(applied_status)
    
    def has_low_chance(self) -> bool:
        return False

class WindElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WIND)

    def apply_status(self, attacker, target) -> ElementStats:
        applied_status = Status.create("airborn")
        target.add_status(applied_status)
        return ElementStats(applied_status)

    def has_low_chance(self) -> bool:
        return True