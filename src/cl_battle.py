import random
from roll import Roll

attack_styles = ["dark", "light", "fire", "water", "electric", "earth", "range", "melee"]

class CLBattle():

    def __init__(self, enemy):
        self.enemy = enemy

    def run(self):
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
    
    def __execute_turn(self, damage_per_roll, attack_speed, attack_type):
        attacks_left = attack_speed
        while attacks_left > 0:
            roll = Roll(damage_per_roll, self.enemy, attack_type)
            roll.execute_roll()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("You rolled a {roll}.".format(roll = roll.roll))
            print("You dealt {damage} damage to the enemy!".format(damage = roll.damage_dealt))
            print("The {enemy} now has {health} HP remaining".format(enemy = self.enemy.name, health = self.enemy.current_health))
            attacks_left -= 1
            input("Press 'Enter' to continue...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
    def __get_attack_type(self):
        attack_type = input("Please enter your attack style: ")
        while attack_type not in attack_styles:
            attack_type = input("Please enter your attack style: ")

        return attack_type

