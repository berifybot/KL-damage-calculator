import unittest
from entity import Enemy, Player

dragon_dict = {
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

test_weapon = {
    "name": "test_weapon",
    "base_damage": 25,
    "element": "Fire",
    "damage_type": "Melee"
}

class TestEnemy(unittest.TestCase):

    def test_enemy_default_creation(self):
        enemy = Enemy(dragon_dict['name'],
                      dragon_dict['max_health'],
                      dragon_dict['damage_source'],
                      dragon_dict['weaknesses'])
        self.assertIsNotNone(enemy)
        self.assertEqual(enemy.name, dragon_dict['name'])
        self.assertEqual(enemy.max_health, dragon_dict['max_health'])
        self.assertEqual(enemy.current_health, dragon_dict['max_health'])
        self.assertEqual(enemy.weaknesses, dragon_dict['weaknesses'])

    def test_enemy_from_dict_creation(self):
        enemy = Enemy.from_dict(dragon_dict)
        self.assertEqual(enemy.name, dragon_dict['name'])
        self.assertEqual(enemy.max_health, dragon_dict['max_health'])
        self.assertEqual(enemy.current_health, dragon_dict['max_health'])
        self.assertEqual(enemy.weaknesses, dragon_dict['weaknesses'])

    def test_player_default_creation(self):
        player_name = "test_player"
        max_health = 500
        attack_speed = 5

        player = Player(player_name, max_health, test_weapon, attack_speed)
        self.assertEqual(player.name, player_name)
        self.assertEqual(player.max_health, max_health)
        self.assertEqual(player.attack_speed, attack_speed)

    def test_player_no_optional_creation(self):
        player_name = "test_player"
        max_health = 500
        attack_speed = 5
        weaknesses = []

        player = Player(player_name, max_health, test_weapon, attack_speed, weaknesses)
        self.assertEqual(player.name, player_name)
        self.assertEqual(player.max_health, max_health)
        self.assertEqual(player.attack_speed, attack_speed)
        self.assertEqual(player.weaknesses, weaknesses)

if __name__ == '__main__':
    unittest.main()