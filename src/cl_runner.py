from cl_battle import CLBattle
from entity import Enemy, Player
from host import Host
from damage_source import Weapon, AttackType
from element import Element
from typing import List
from mock_objects import TestPlayerCreator

WAITING_COMMAND = "w"
START_BATTLE_COMMAND = "s"
ADD_PLAYER = "p"
LIST_PLAYERS = "lp"
QUIT_COMMAND = "q"

temp_dragon_dict = {
        "name": "Dragon",
        "max_health": 500,
        "damage_source": {
            "name": "dragon_breath",
            "base_damage": 25,
            "element": "Fire",
            "damage_type": "Melee",
        },
        "weaknesses": ["Water"]
}

class CLRunner(Host):

    current_command = WAITING_COMMAND

    players: List[Player] = [TestPlayerCreator.createDefaultPlayer()]
    commands =  "List of Commands:\n" + "\t s: Start Battle\n" + "\t p: Add Player\n" + "\t lp: List Players\n" + "\t q: Quit"
    
    def run(self) -> None:
        print("Welcome to the Kyrons Legacy Damage Calculator!\n")
        while self.current_command != QUIT_COMMAND:
            print(self.commands)
            new_command = input("Enter Command: ")
            self.process_command(new_command)
            self.current_command = new_command

    def process_command(self, command) -> None:
        if command == WAITING_COMMAND:
            pass
        elif command == START_BATTLE_COMMAND:
            # enemy_name = input("Choose enemy: ")
            enemy = self.__find_enemy("Dragon")
            CLBattle(enemy, self.players).run()
        elif command == ADD_PLAYER:
            print("Creating player, please enter values for the following fields:")
            name = input("Enter Name: ")
            health = int(input("Enter Health: "))
            attack_speed = int(input("Enter attack speed: "))
            weapon_name = input("Enter weapon name: ")
            damage = int(input("Enter weapon damage: "))
            element = self.get_element()
            attack_type = self.get_attack_type()
            weapon = Weapon(weapon_name, damage, element, attack_type)
            player = Player(name, health, weapon, attack_speed)
            self.players.append(player)
        elif command == LIST_PLAYERS:
            for player in self.players:
                print(player.get_name())
        elif command == QUIT_COMMAND:
            print("Thanks for playing!")
        else:
            print("{command} is not a valid command, please try again".format(command = command))

    def __find_enemy(self, enemy_name) -> Enemy:
        return Enemy.from_dict(temp_dragon_dict)

    def get_attack_type(self) -> str:
        attack_type = input("Please enter your attack style: ")
        while not AttackType.is_type_valid(attack_type):
            attack_type = input("Please enter your attack style: ")

        return attack_type
    
    def get_element(self) -> str:
        element = input("Please enter element: ")
        while not Element.is_type_valid(element):
            element = input("Please enter element: ")

        return element

if __name__ == "__main__":
    CLRunner().run()