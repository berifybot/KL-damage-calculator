from entity import Entity
from damage_source import Weapon, Element, AttackType

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
    
temp_dragon_dict = {
    "name": "Dragon",
    "max_health": 500,
    "damage_source": {
        "name": "dragon_breath",
        "base_damage": 25,
        "element": "Fire",
        "damage_type": "Melee",
    },
    "weaknesses": ["Water", "Melee"]
}
    
# print(getattr(Element, temp_dragon_dict['damage_source']['element']))
enemy: Enemy = Enemy.load(temp_dragon_dict)
print(enemy.get_name(), enemy.get_current_health(), enemy.get_max_health(),
      enemy.get_weapon().get_name(), enemy.get_weapon().get_base_damage(),
      enemy.get_weapon().get_element(), enemy.get_weapon().get_attack_type(), enemy.get_weaknesses())