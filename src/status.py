class Status():

    BURN = "burn"
    FREEZE = "freeze"
    PARALYZE = "paralyze"
    ROOTED = "rooted"
    BLESSED = "blessed"
    CURSED = "cursed"
    BLEED = "bleed"
    POISON = "poison"
    CONCUSSED = "concussed"
    BLINDED = "blinded"
    HYSTERIA = "hysteria"
    AGILE = "agile"
    WARDED = "warded"
    FORTIFIED = "fortified"
    CHAINED = "chained"
    VOLLEYED = "volleyed"
    CRUSHED = "crushed"
    SHIMMERED = "shimmered"
    FORESIGHT = "foresight"
    AMBUSH = "ambush"
    SNEAK = "sneak"
    RUIN = "ruin"
    AIRBORNE = "airborne"
    LUCKY = "lucky"
    WISDOM = "wisdom"
    CHARMED = "charmed"
    WHIRLWIND = "whirlwind"
    LIFESTEAL = "lifesteal"
    OVERHEALTH = "overhealth"
    DETACHED = "detached"
    WITHERED = "withered"
    SLIP = "slip"
    SOULSIPHONED = "soulsiphoned"
    BOOMBURSTED = "boombursted"
    INTIMIDATE = "intimidate"
    types = [BURN, FREEZE, PARALYZE, ROOTED, BLESSED, CURSED,
             BLEED, POISON, CONCUSSED, BLINDED, HYSTERIA, AGILE,
             WARDED, FORTIFIED, CHAINED, VOLLEYED, CRUSHED, SHIMMERED, 
             FORESIGHT, AMBUSH, SNEAK, RUIN, AIRBORNE, LUCKY, WISDOM, 
             CHARMED, WHIRLWIND, LIFESTEAL, OVERHEALTH, DETACHED, 
             WITHERED, SLIP, SOULSIPHONED, BOOMBURSTED, INTIMIDATE]
    
    def __init__(self, type: str):
        self.type = type

    @classmethod
    def create(cls, type: str) -> None:
        pass

class Burn(Status):
    def __init__(self) -> None:
        super.__init__(self.BURN)

class Freeze(Status):
    def __init__(self) -> None:
        super.__init__(self.FREEZE)

class Paralize(Status):
    def __init__(self) -> None:
        super.__init__(self.PARALYZE)

class Rooted(Status):
    def __init__(self) -> None:
        super.__init__(self.ROOTED)

class Blessed(Status):
    def __init__(self) -> None:
        super.__init__(self.BLESSED)

class Cursed(Status):
    def __init__(self) -> None:
        super.__init__(self.CURSED)

class Bleed(Status):
    def __init__(self) -> None:
        super.__init__(self.BLEED)

class Poison(Status):
    def __init__(self) -> None:
        super.__init__(self.POISON)

class Concussed(Status):
    def __init__(self) -> None:
        super.__init__(self.CONCUSSED)

class Blinded(Status):
    def __init__(self) -> None:
        super.__init__(self.BLINDED)

class Hysteria(Status):
    def __init__(self) -> None:
        super.__init__(self.HYSTERIA)

class Agile(Status):
    def __init__(self) -> None:
        super.__init__(self.AGILE)

class Warded(Status):
    def __init__(self) -> None:
        super.__init__(self.WARDED)

class Fortified(Status):
    def __init__(self) -> None:
        super.__init__(self.FORTIFIED)

class Chained(Status):
    def __init__(self) -> None:
        super().__init__(self.CHAINED)

class Volleyed(Status):
    def __init__(self) -> None:
        super().__init__(self.VOLLEYED)

class Crushed(Status):
    def __init__(self) -> None:
        super().__init__(self.CRUSHED)

class Shimmered(Status):
    def __init__(self) -> None:
        super().__init__(self.SHIMMERED)

class Foresight(Status):
    def __init__(self) -> None:
        super().__init__(self.FORESIGHT)

class Ambush(Status):
    def __init__(self) -> None:
        super().__init__(self.FORESIGHT)

class Sneak(Status):
    def __init__(self) -> None:
        super().__init__(self.SNEAK)

class Ruin(Status):
    def __init__(self) -> None:
        super().__init__(self.RUIN)

class Airborne(Status):
    def __init__(self) -> None:
        super().__init__(self.AIRBORNE)

class Lucky(Status):
    def __init__(self) -> None:
        super().__init__(self.LUCKY)

class Wisdom(Status):
    def __init__(self) -> None:
        super().__init__(self.WISDOM)

class Charmed(Status):
    def __init__(self) -> None:
        super().__init__(self.CHARMED)

class Whirlwind(Status):
    def __init__(self) -> None:
        super().__init__(self.WHIRLWIND)

class Lifesteal(Status):
    def __init__(self) -> None:
        super().__init__(self.LIFESTEAL)

class Overhealth(Status):
    def __init__(self) -> None:
        super().__init__(self.OVERHEALTH)

class Detached(Status):
    def __init__(self) -> None:
        super().__init__(self.DETACHED)

class Withered(Status):
    def __init__(self) -> None:
        super().__init__(self.WITHERED)

class Slip(Status):
    def __init__(self) -> None:
        super().__init__(self.SLIP)

class Soulsiphoned(Status):
    def __init__(self) -> None:
        super().__init__(self.SOULSIPHONED)

class Boombursted(Status):
    def __init__(self) -> None:
        super().__init__(self.BOOMBURSTED)

class Intimidate(Status):
    def __init__(self) -> None:
        super().__init__(self.INTIMIDATE)