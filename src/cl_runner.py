from cl_battle import CLBattle
from enemy import Enemy
from host import Host

WAITING_COMMAND = "w"
START_BATTLE_COMMAND = "s"
QUIT_COMMAND = "q"

temp_dragon_dict = {
        "name": "Dragon",
        "max_health": 500,
        "base_damage": 25,
        "damage_type": "melee",
        "weaknesses": ["water", "melee"]
    }

class CLRunner(Host):
    current_command = WAITING_COMMAND
    
    def run(self) -> None:
        print("Welcome to the Kyrons Legacy Damage Calculator!\n"
              + "List of Commands:\n"
              + "\t s: Start Battle\n"
              + "\t q: Quit")
        while self.current_command != QUIT_COMMAND:
            new_command = input("Enter Command: ")
            self.process_command(new_command)
            self.current_command = new_command

    def get_roll(self) -> int:
        return int(input("Enter roll value: "))
    
    def get_attack_speed(self) -> int:
        return int(input("Enter attack speed: ") or 0)

    def get_damage_per_roll(self) -> int:
        return int(input("Enter damage per roll: ") or 0)

    def get_attack_type(self) -> str:
        attack_styles = ["magic", "range", "melee"]
        attack_type = input("Please enter your attack style: ")
        while attack_type not in attack_styles:
            attack_type = input("Please enter your attack style: ")

        return attack_type
    
    def report_roll_stats(self, roll_value, damage_dealt, enemy):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You rolled a {roll}.".format(roll = roll_value))
        print("You dealt {damage} damage to the enemy!".format(damage = damage_dealt))
        print("The {enemy} now has {health} HP remaining".format(enemy = enemy.name, health = enemy.current_health))
        input("Press 'Enter' to continue...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    def process_command(self, command) -> None:
        if command == WAITING_COMMAND:
            pass
        elif command == START_BATTLE_COMMAND:
            enemy_name = input("Choose enemy: ")
            enemy = self.__find_enemy(enemy_name)
            CLBattle(enemy, self).run()
        elif command == QUIT_COMMAND:
            print("Thanks for playing!")
        else:
            print("{command} is not a valid command, please try again".format(command = command))

    def __find_enemy(self, enemy_name) -> Enemy:
        return Enemy(temp_dragon_dict)

if __name__ == "__main__":
    CLRunner().run()