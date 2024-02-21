from entity import Player, Enemy
from attack import Attack
from damage_source import Weapon

class Turn():
    
    def __init__(self, host, enemy: Enemy, player: Player):
        self.host = host
        self.enemy = enemy
        self.player = player
    
    def execute_turn(self):
        # get base damage
        # get attack speed
        # get attack type
        # get element for attack?
        # create player
        # player attacks enemy x times (x = attack speed)
        # attacks_remaining = self.host.get_attack_speed()
        # damage_per_roll = self.host.get_damage_per_roll()
        # attack_type = self.host.get_attack_type()
        # weapon = Weapon("DefaultWeapon", damage_per_roll, "Dark", attack_type)
        # player = Player("DefaultPlayer", 500, weapon, attacks_remaining)
        attacks_remaining = self.player.get_attack_speed()
        while attacks_remaining > 0:
            Attack(self.host, self.player, self.enemy).attack()
            attacks_remaining -= 1
        return