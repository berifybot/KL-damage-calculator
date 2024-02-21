from battle_host import BattleHost
from damage_source import Weapon
from entity import Enemy, Player

class TestBattleHost(BattleHost):

    def __init__(self, attack_speed, damage_per_roll, attack_type, roll):
        self.attack_speed = attack_speed
        self.get_damage_per_roll = damage_per_roll
        self.attack_type = attack_type
        self.roll = roll

    def get_attack_speed(self) -> int:
        return self.attack_speed
    
    def get_damage_per_roll(self) -> int:
        return self.get_damage_per_roll
    
    def get_attack_type(self) -> int:
        return self.attack_type
    
    def roll(self) -> int:
        return self.roll()
    
    def report_roll_stats(self, roll_value, damage_dealt, enemy):
        pass

class TestEnemyCreator():

    @classmethod
    def create(cls, weapon: Weapon, name = "TestEnemy", max_health = 500, weaknesses = []) -> Enemy:
        return Enemy(name, max_health, weapon, weaknesses)
    
class TestPlayerCreator():

    @classmethod
    def create(cls, weapon: Weapon, name = "TestPlayer", max_health = 500, attack_speed = 1, weaknesses= []) -> Player:
        return Player(name, max_health, weapon, attack_speed, weaknesses)
    
    @classmethod
    def createDefaultPlayer(cls):
        weapon = Weapon("Sword", 50, "fire", "melee")
        return Player("Default", 500, weapon, 3)
    
class TestWeaponCreator():

    @classmethod
    def create(cls, name = "TestWeapon", base_damage = 50, element = "Light", attack_type = "Melee"):
        return Weapon(name, base_damage, element, attack_type)