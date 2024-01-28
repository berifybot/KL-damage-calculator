from roll import Roll
import math

class Turn():
    
    def __init__(self, host, enemy):
        self.host = host
        self.enemy = enemy
    
    def execute_turn(self):
        attacks_remaining = self.host.get_attack_speed()
        damage_per_roll = self.host.get_damage_per_roll()
        attack_type = self.host.get_attack_type()
        while attacks_remaining > 0:
            self.execute_attack(damage_per_roll, attack_type)
            attacks_remaining -= 1
        return
    
    def execute_attack(self, damage_per_roll, attack_type):
        roll = Roll().random_roll()
        damage_dealt = self.execute_roll(damage_per_roll, attack_type, roll)
        self.host.report_roll_stats(roll, damage_dealt, self.enemy)

    def execute_roll(self, damage_per_roll, attack_type, roll) -> int:
        damage_dealt = self.__get_damage_from_roll(roll, damage_per_roll)
        if attack_type in self.enemy.weaknesses:
            damage_dealt += 10
            self.enemy.current_health -= damage_dealt
            return damage_dealt
        else:
            self.enemy.current_health -= damage_dealt
            return damage_dealt

    def __get_damage_from_roll(self, roll, damage) -> int:
        if (roll == 1):
            return 0
        elif (roll == 2):
            return 0
        elif (roll == 3):
            return math.floor(damage / 2)
        elif (roll == 4):
            return damage
        elif (roll == 5):
            return damage + 3
        elif (roll == 6):
            return damage + 5
        else:
            raise Exception("Invalid roll value")