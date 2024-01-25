import random
from roll import Roll

class CLBattle():

    def __init__(self, enemy):
        self.enemy = enemy

    def run(self):
        print("\nStarting battle with {enemy_name}".format(enemy_name = self.enemy.name))
        
        while self.enemy.current_health > 0:
            print("The {enemy} has {health_value} HP!".format(enemy = self.enemy.name, health_value = self.enemy.current_health))
            damage_per_roll, attack_speed = self.__get_turn_data()
            self.__execute_turn(damage_per_roll, attack_speed)
        
        print("You have defeated the {enemy}".format(enemy = self.enemy.name))


    def __get_turn_data(self):
        damage_per_roll = int(input("Enter damage per roll: ") or 0)
        attack_speed = int(input("Enter attack speed: ") or 0)
        print("\n")
        return (damage_per_roll, attack_speed)
    
    def __execute_turn(self, damage_per_roll, attack_speed):
        attacks_left = attack_speed
        while attacks_left > 0:
            roll = Roll(damage_per_roll)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("You rolled a {roll}.".format(roll = roll.roll))
            damage = roll.execute_roll()
            self.enemy.current_health -= damage
            print("You dealt {damage} damage to the enemy!".format(damage = damage))
            print("The {enemy} now has {health} HP remaining".format(enemy = self.enemy.name, health = self.enemy.current_health))
            attacks_left -= 1
            input("Press 'Enter' to continue...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
