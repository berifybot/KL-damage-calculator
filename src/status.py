from status_stats import StatusStats

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
        self.category = ""
        self.applier = None
        self.rolls_remaining = 0

    def end_of_turn(self) -> StatusStats:
        return None

    def set_applier(self, applier) -> None:
        self.applier = applier

    def is_expired(self) -> bool:
        return False

    @classmethod
    def create(cls, type: str) -> None:
        match type.lower():
            case cls.BURN:
                return Burn()
            case cls.FREEZE:
                return Freeze()
            case cls.PARALYZE:
                return Paralize()
            case cls.ROOTED:
                return Rooted()
            case cls.BLESSED:
                return Blessed()
            case cls.CURSED:
                return Cursed()
            case cls.BLEED:
                return Bleed()
            case cls.POISON:
                return Poison()
            case cls.CONCUSSED:
                return Concussed()
            case cls.BLINDED:
                return Blinded()
            case cls.HYSTERIA:
                return Hysteria()
            case cls.AGILE:
                return Agile()
            case cls.WARDED:
                return Warded()
            case cls.FORTIFIED:
                return Fortified()
            case cls.CHAINED:
                return Chained()
            case cls.VOLLEYED:
                return Volleyed()
            case cls.CRUSHED:
                return Crushed()
            case cls.SHIMMERED:
                return Shimmered()
            case cls.FORESIGHT:
                return Foresight()
            case cls.AMBUSH:
                return Ambush()
            case cls.SNEAK:
                return Sneak()
            case cls.RUIN:
                return Ruin()
            case cls.AIRBORNE:
                return Airborne()
            case cls.LUCKY:
                return Lucky()
            case cls.WISDOM:
                return Wisdom()
            case cls.CHARMED:
                return Charmed()
            case cls.WHIRLWIND:
                return Whirlwind()
            case cls.LIFESTEAL:
                return Lifesteal()
            case cls.OVERHEALTH:
                return Overhealth()
            case cls.DETACHED:
                return Detached()
            case cls.WITHERED:
                return Withered()
            case cls.SLIP:
                return Slip()
            case cls.SOULSIPHONED:
                return Soulsiphoned()
            case cls.BOOMBURSTED:
                return Boombursted()
            case cls.INTIMIDATE:
                return Intimidate()
            case _:
                return None

    @classmethod
    def is_type_valid(cls, type: str) -> bool:
        return type.lower() in cls.types

class Burn(Status):
    def __init__(self) -> None:
        super().__init__(self.BURN)
        self.rolls_remaining = 4
        self.category = "flat_end"

    def end_of_turn(self) -> StatusStats:
        stats = StatusStats(self.type, self.category)
        stats.damage_dealt = 5
        self.rolls_remaining -= 1
        stats.rolls_remaining = self.rolls_remaining
        return stats

    def is_expired(self) -> bool:
        return self.rolls_remaining == 0


class Freeze(Status):
    def __init__(self) -> None:
        super().__init__(self.FREEZE)
        self.rolls_remaining = 4

    def end_of_turn(self) -> StatusStats:
        stats = StatusStats(self.type, self.category)
        stats.damage_dealt = 4
        self.rolls_remaining -= 1
        stats.rolls_remaining = self.rolls_remaining
        return stats

    def is_expired(self) -> bool:
        return self.rolls_remaining == 0

class Paralize(Status):
    def __init__(self) -> None:
        super().__init__(self.PARALYZE)

class Rooted(Status):
    def __init__(self) -> None:
        super().__init__(self.ROOTED)

class Blessed(Status):
    def __init__(self) -> None:
        super().__init__(self.BLESSED)

class Cursed(Status):
    def __init__(self) -> None:
        super().__init__(self.CURSED)

class Bleed(Status):
    def __init__(self) -> None:
        super().__init__(self.BLEED)

class Poison(Status):
    def __init__(self) -> None:
        super().__init__(self.POISON)
        self.rolls_remaining = 10

    def end_of_turn(self) -> StatusStats:
        stats = StatusStats(self.type, self.category)
        stats.damage_dealt = 3
        self.rolls_remaining -= 1
        stats.rolls_remaining = self.rolls_remaining
        return stats

    def is_expired(self) -> bool:
        return self.rolls_remaining ==  0

class Concussed(Status):
    def __init__(self) -> None:
        super().__init__(self.CONCUSSED)

class Blinded(Status):
    def __init__(self) -> None:
        super().__init__(self.BLINDED)

class Hysteria(Status):
    def __init__(self) -> None:
        super().__init__(self.HYSTERIA)

class Agile(Status):
    def __init__(self) -> None:
        super().__init__(self.AGILE)

class Warded(Status):
    def __init__(self) -> None:
        super().__init__(self.WARDED)

class Fortified(Status):
    def __init__(self) -> None:
        super().__init__(self.FORTIFIED)

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