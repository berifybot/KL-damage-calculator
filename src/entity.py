from typing import List
from damage_source import Weapon, Element, AttackType

class Entity():
    def __init__(self, name: str, max_health: int, weapon: Weapon, weaknesses: List[Element] = []):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.weapon = weapon
        self.weaknesses = weaknesses

    def get_name(self) -> str:
        return self.name
    
    def get_max_health(self) -> int:
        return self.max_health
    
    def get_current_health(self) -> int:
        return self.current_health
    
    def get_weapon(self) -> Weapon:
        return self.weapon

    def get_weaknesses(self) -> List[Element]:
        return self.weaknesses
    
class Player():
    def __init__(self, name: str, max_health: int, weapon: Weapon, attack_speed: int, weaknesses: List[Element] = []):
        super().__init__(name, max_health, weapon, weaknesses)
        self.attack_speed = attack_speed

    def get_attack_speed(self) -> int:
        return self.attack_speed
    
class Enemy(Entity):

    @classmethod
    def load(self, enemy_dict: dict) -> None:
        # TODO: Clean this mess up
        if ('name' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'name'")
        if ('max_health' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'max_health'")
        if ('damage_source' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'damage_sources'")
        if ('name' not in enemy_dict['damage_source']):
            raise Exception("Invalid enemy, missing 'name' in 'damage_source'")
        if('base_damage' not in enemy_dict['damage_source']):
            raise Exception("Invalid enemy, missing 'base_damage' in 'damage_source'")
        if('element' not in enemy_dict['damage_source']):
            raise Exception("Invalid enemy, missing 'element' in 'damage_source'")
        if('damage_type' not in enemy_dict['damage_source']):
            raise Exception("Invalid enemy, missing 'damage_type' in 'damage_source'")
        if ('weaknesses' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'weaknesses'")
        weapon = Weapon(enemy_dict['damage_source']['name'], enemy_dict["damage_source"]['base_damage'], 
                        getattr(Element, enemy_dict['damage_source']['element']), 
                        getattr(AttackType, enemy_dict['damage_source']['damage_type']))
        return Enemy(enemy_dict['name'], enemy_dict['max_health'], weapon,
                     enemy_dict['weaknesses'])