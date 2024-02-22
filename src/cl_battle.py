from battle_host import BattleHost
from roll import Roll
from damage_source import AttackType
from turn import Turn
from typing import List
from entity import Player, Enemy

class CLBattle(BattleHost):

    def __init__(self, enemy: Enemy, players: List[Player]):
        self.enemy = enemy
        self.players = players

    def run(self) -> None:
        print("\nStarting battle with {enemy_name}".format(enemy_name = self.enemy.name))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        self.current_player = self.select_player()
        
        while self.enemy.current_health > 0:
            self.__execute_turn__()
            print("Player {player} has finished their turn!".format(player=self.current_player.get_name()))
            if (self.enemy.current_health > 0):
                print("Who will be attacking next?")
                self.current_player = self.select_player()
        print("You have defeated the {enemy}".format(enemy = self.enemy.name))

    def select_player(self):
        print("Please select a player...")
        print("Active Players: ")
        for player in self.players:
            print("\t " + player.get_name())
        selected_player = self.get_player(input("Select a player: "))
        while selected_player is None:
            selected_player = self.get_player(input("Select a player: "))
        return selected_player
        
    def get_player(self, player_name: str):
        for player in self.players:
            if player.get_name() == player_name:
                return player
        return None

    def __execute_turn__(self) -> None:
        Turn(self, self.enemy, self.current_player).execute_turn()
    
    def get_attack_speed(self) -> int:
        return int(input("Enter attack speed: ") or 0)

    def get_damage_per_roll(self) -> int:
        return int(input("Enter damage per roll: ") or 0)

    def get_attack_type(self) -> str:
        attack_type = input("Please enter your attack style: ")
        while not AttackType.is_type_valid(attack_type):
            attack_type = input("Please enter your attack style: ")

        return attack_type
    
    def roll(self) -> int:
        # return int(input("Enter Roll Value: "))
        return Roll.random_roll()
    
    def report_roll_stats(self, roll_value, damage_dealt, enemy):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You rolled a {roll}.".format(roll = roll_value))
        print("You dealt {damage} damage to the enemy!".format(damage = damage_dealt))
        print("The {enemy} now has {health} HP remaining".format(enemy = enemy.name, health = enemy.current_health))
        input("Press 'Enter' to continue...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")