from battle_host import BattleHost
from roll import Roll
from turn import Turn

class CLBattle(BattleHost):

    def __init__(self, enemy):
        self.enemy = enemy

    def run(self) -> None:
        print("\nStarting battle with {enemy_name}".format(enemy_name = self.enemy.name))
        
        while self.enemy.current_health > 0:
            print("The {enemy} has {health_value} HP!".format(enemy = self.enemy.name, health_value = self.enemy.current_health))
            self.__execute_turn__()
        
        print("You have defeated the {enemy}".format(enemy = self.enemy.name))

    def __execute_turn__(self) -> None:
        Turn(self, self.enemy).execute_turn()
    
    def get_attack_speed(self) -> int:
        return int(input("Enter attack speed: ") or 0)

    def get_damage_per_roll(self) -> int:
        return int(input("Enter damage per roll: ") or 0)

    def get_attack_type(self) -> str:
        attack_styles = ["Magic", "Range", "Melee"]
        attack_type = input("Please enter your attack style: ")
        while attack_type not in attack_styles:
            attack_type = input("Please enter your attack style: ")

        return attack_type
    
    def roll(self) -> int:
        return int(input("Enter Roll Value: "))
        # return Roll.random_roll()
    
    def report_roll_stats(self, roll_value, damage_dealt, enemy):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You rolled a {roll}.".format(roll = roll_value))
        print("You dealt {damage} damage to the enemy!".format(damage = damage_dealt))
        print("The {enemy} now has {health} HP remaining".format(enemy = enemy.name, health = enemy.current_health))
        input("Press 'Enter' to continue...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")