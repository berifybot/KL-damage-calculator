from entity import Entity

class AttackStats:
    
    base_roll_value = 0
    damage_dealt = 0

    def __init__(self, attacker: Entity, target: Entity):
        self.attacker = attacker
        self.target = target

    def set_base_roll(self, value) -> None:
        self.base_roll_value = value

    def set_damage_dealt(self, damage) -> None:
        self.damage_dealt = damage
