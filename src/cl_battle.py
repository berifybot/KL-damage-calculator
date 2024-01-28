import random
import math
from roll import Roll
from turn import Turn

class CLBattle():

    def __init__(self, enemy, host):
        self.enemy = enemy
        self.host = host

    def run(self) -> None:
        print("\nStarting battle with {enemy_name}".format(enemy_name = self.enemy.name))
        
        while self.enemy.current_health > 0:
            print("The {enemy} has {health_value} HP!".format(enemy = self.enemy.name, health_value = self.enemy.current_health))
            self.__execute_turn()
        
        print("You have defeated the {enemy}".format(enemy = self.enemy.name))
    
    def __execute_turn(self) -> None:
        Turn(self.host, self.enemy).execute_turn()
