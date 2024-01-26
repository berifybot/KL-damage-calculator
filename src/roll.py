import random
import math

die_roller = lambda: random.choice([1, 2, 3, 4, 5, 6])

class Roll():

    def __init__(self, damage, enemy, attack_type, die_roller = die_roller):
        self.damage = damage
        self.enemy = enemy
        self.attack_type = attack_type
        self.roll = die_roller()

    def execute_roll(self):
        self.damage_dealt = self.__get_damage_from_roll()
        if self.attack_type in self.enemy.weaknesses:
            self.damage_dealt += 10
            self.enemy.current_health -= self.damage_dealt
        else:
            self.enemy.current_health -= self.damage_dealt
    
    def __get_damage_from_roll(self):
        if (self.roll == 1):
            return 0
        elif (self.roll == 2):
            return 0
        elif (self.roll == 3):
            return math.floor(self.damage / 2)
        elif (self.roll == 4):
            return self.damage
        elif (self.roll == 5):
            return self.damage + 3
        elif (self.roll == 6):
            return self.damage + 5
        else:
            raise Exception("Invalid roll value")