class Enemy():
    name = ""
    max_health = 0
    current_health = 0
    base_damage = 0
    damage_type = ""
    weaknesses = []

    def __init__(self, enemy_dict = {}):
        self.load(enemy_dict)

    def load(self, enemy_dict: dict):
        if ('name' in enemy_dict):
            self.name = enemy_dict['name']
        if ('max_health' in enemy_dict):
            self.max_health = enemy_dict['max_health']
            self.current_health = self.max_health
        if ('base_damage' in enemy_dict):
            self.base_damage = enemy_dict['base_damage']
        if ('damage_type' in enemy_dict):
            self.damage_type = enemy_dict['damage_type']
        if ('weaknesses' in enemy_dict):
            self.weaknesses = enemy_dict['weaknesses']