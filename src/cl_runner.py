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