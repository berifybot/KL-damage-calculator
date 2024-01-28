import random
import math
from roll import Roll

attack_styles = ["magic", "range", "melee"]

class CLBattle():

    def __init__(self, enemy):
        self.enemy = enemy

    def run(self) -> None:
        print("\nStarting battle with {enemy_name}".format(enemy_name = self.enemy.name))
        
        while self.enemy.current_health > 0:
            print("The {enemy} has {health_value} HP!".format(enemy = self.enemy.name, health_value = self.enemy.current_health))
            damage_per_roll, attack_speed, attack_type = self.__get_turn_data()
            self.__execute_turn(damage_per_roll, attack_speed, attack_type)
        
        print("You have defeated the {enemy}".format(enemy = self.enemy.name))


    def __get_turn_data(self):
        damage_per_roll = int(input("Enter damage per roll: ") or 0)
        attack_speed = int(input("Enter attack speed: ") or 0)
        attack_type = self.__get_attack_type()
        print("\n")
        return (damage_per_roll, attack_speed, attack_type)
    
    def __execute_turn(self, damage_per_roll, attack_speed, attack_type) -> None:
        attacks_left = attack_speed
        while attacks_left > 0:
            roll = Roll.random_roll()
            damage_dealt = self.execute_roll(damage_per_roll, attack_type, roll)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("You rolled a {roll}.".format(roll = roll))
            print("You dealt {damage} damage to the enemy!".format(damage = damage_dealt))
            print("The {enemy} now has {health} HP remaining".format(enemy = self.enemy.name, health = self.enemy.current_health))
            attacks_left -= 1
            input("Press 'Enter' to continue...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
    def __get_attack_type(self) -> str:
        attack_type = input("Please enter your attack style: ")
        while attack_type not in attack_styles:
            attack_type = input("Please enter your attack style: ")

        return attack_type
    
    # Todo: Move to Turn/Attack classes        
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

