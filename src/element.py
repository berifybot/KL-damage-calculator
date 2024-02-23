from element_stats import ElementStats

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
            
class WaterElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WATER)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Slip")
        return ElementStats("Slip")

    def has_low_chance(self) -> bool:
        return False

class FireElement(Element):

    def __init__(self) -> None:
        super().__init__(self.FIRE)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Burn")
        return ElementStats("Burn")

    def has_low_chance(self) -> bool:   
        return False

class LightningElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHTNING)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Paralyze")
        return ElementStats("Paralyze")
    
    def has_low_chance(self) -> bool:
        return True


class EarthElement(Element):

    def __init__(self) -> None:
        super().__init__(self.EARTH)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Rooted")
        return ElementStats("Rooted")

    def has_low_chance(self) -> bool:
        return False

class LightElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHT)

    def apply_status(self, attacker, target) -> ElementStats:
        attacker.add_status("Blessed")
        return ElementStats("Blessed")

    def has_low_chance(self) -> bool:
        return False

class DarkElement(Element):

    def __init__(self) -> None:
        super().__init__(self.DARK)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Cursed")
        return ElementStats("Cursed")

    def has_low_chance(self) -> bool:
        return False

class IceElement(Element):

    def __init__(self) -> None:
        super().__init__(self.ICE)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Freeze")
        return ElementStats("Freeze")
    
    def has_low_chance(self) -> bool:
        return False

class WindElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WIND)

    def apply_status(self, attacker, target) -> ElementStats:
        target.add_status("Airborn")
        return ElementStats("Airborn")

    def has_low_chance(self) -> bool:
        return True