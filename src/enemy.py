class Enemy():
    name = ""
    max_health = 0
    current_health = 0
    base_damage = 0
    damage_type = ""
    weaknesses = []
    def load(self, enemy_dict):
        self.name = enemy_dict['name']
        self.max_health = enemy_dict['max_health']
        self.current_health = self.max_health
        self.base_damage = enemy_dict['base_damage']
        self.damage_type = enemy_dict['damage_type']
        self.weaknesses = enemy_dict['weaknesses']