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
        target.add_status("Slip")

class FireElement(Element):

    def __init__(self) -> None:
        super().__init__(self.FIRE)

    def apply_status(self, attacker, target) -> None:
        target.add_status("Burn")

class LightningElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHTNING)

    def apply_status(self, attacker, target) -> None:
        target.add_status("Paralyze")

class EarthElement(Element):

    def __init__(self) -> None:
        super().__init__(self.EARTH)

    def apply_status(self, attacker, target) -> None:
        target.add_status("Rooted")

class LightElement(Element):

    def __init__(self) -> None:
        super().__init__(self.LIGHT)

    def apply_status(self, attacker, target) -> None:
        attacker.add_status("Blessed")

class DarkElement(Element):

    def __init__(self) -> None:
        super().__init__(self.DARK)

    def apply_status(self, attacker, target) -> None:
        target.add_status("Cursed")

class IceElement(Element):

    def __init__(self) -> None:
        super().__init__(self.ICE)

    def apply_status(self, attacker, target) -> None:
        target.add_status("Freeze")

class WindElement(Element):

    def __init__(self) -> None:
        super().__init__(self.WIND)

    def apply_status(self, attacker, target) -> None:
        target.add_status("Airborn")