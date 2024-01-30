from entity import Entity

class Enemy(Entity):
    name = ""
    max_health = 0
    current_health = 0
    base_damage = 0
    damage_type = ""
    weaknesses = []

    @classmethod
    def load(self, enemy_dict: dict) -> None:
        if ('name' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'name'")
        if ('max_health' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'max_health'")
        if ('base_damage' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'base_damage'")
        if ('damage_type' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'damage_type'")
        if ('weaknesses' not in enemy_dict):
            raise Exception("Invalid enemy, missing 'weaknesses'")
        return Enemy(enemy_dict['name'], enemy_dict['max_health'],
                     enemy_dict['base_damage'], enemy_dict['damage_type'],
                     enemy_dict['weaknesses'])