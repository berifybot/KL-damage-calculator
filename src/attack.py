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

class Status(Enum):
    Burn = 1
    Freeze = 2
    Paralyze = 3
    Rooted = 4
    Blessed = 5
    Cursed = 6
    Bleed = 7
    Poison = 8
    Concussed = 9
    Blinded = 10
    Hysteria = 11
    Agile = 12
    Warded = 13
    Fortified = 14
    Chained = 15
    Volleyed = 17
    Crushed = 18
    Shimmered = 19
    Foresight = 20
    Ambush = 21
    Sneak = 22
    Ruin = 23
    Airborne = 24
    Lucky = 25
    Wisdom = 26
    Charmed = 27
    Whirlwind = 28
    LifeSteal = 29
    Overhealth = 30
    Detached = 31
    Withered = 32
    Slip = 33
    SoulSiphoned = 34
    Boombursted = 35
    Intimidate = 36

class Attack():
    def __init__(self, damage, attack_type, element, status):
        pass