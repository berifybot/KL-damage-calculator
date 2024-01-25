import random

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
            die_roll = random.choice([1, 2, 3, 4, 5, 6])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("You rolled a {roll}.".format(roll = die_roll))
            damage = self.__get_damage_from_roll(damage_per_roll, die_roll)
            self.enemy.current_health -= damage
            print("You dealt {damage} damage to the enemy!".format(damage = damage))
            print("The {enemy} now has {health} HP remaining".format(enemy = self.enemy.name, health = self.enemy.current_health))
            attacks_left -= 1
            input("Press 'Enter' to continue...")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    def __get_damage_from_roll(self, damage_per_roll, roll_value):
        if (roll_value == 1):
            return 0
        elif (roll_value == 2):
            return 0
        elif (roll_value == 3):
            return damage_per_roll / 2
        elif (roll_value == 4):
            return damage_per_roll
        elif (roll_value == 5):
            return damage_per_roll + 3
        elif (roll_value == 6):
            return damage_per_roll + 5
        else:
            print("Invalid Dice Value: {die_value}!!!".format(die_value = roll_value))
