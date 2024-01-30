import unittest
from enemy import Enemy

dragon_dict = {
        "name": "Dragon",
        "max_health": 500,
        "base_damage": 25,
        "damage_type": "melee",
        "weaknesses": ["water", "melee"]
    }

class TestEnemy(unittest.TestCase):

    def test_default_creation(self):
        enemy = Enemy(dragon_dict['name'], dragon_dict['max_health'],
                      dragon_dict['base_damage'], dragon_dict['damage_type'],
                      dragon_dict['weaknesses'])
        self.assertIsNotNone(enemy)
        self.assertEqual(enemy.name, dragon_dict['name'])
        self.assertEqual(enemy.max_health, dragon_dict['max_health'])
        self.assertEqual(enemy.current_health, dragon_dict['max_health'])
        self.assertEqual(enemy.base_damage, dragon_dict['base_damage'])
        self.assertEqual(enemy.damage_type, dragon_dict['damage_type'])
        self.assertEqual(enemy.weaknesses, dragon_dict['weaknesses'])

    def test_load_creation(self):
        enemy = Enemy.load(dragon_dict)
        self.assertEqual(enemy.name, dragon_dict['name'])
        self.assertEqual(enemy.max_health, dragon_dict['max_health'])
        self.assertEqual(enemy.current_health, dragon_dict['max_health'])
        self.assertEqual(enemy.base_damage, dragon_dict['base_damage'])
        self.assertEqual(enemy.damage_type, dragon_dict['damage_type'])
        self.assertEqual(enemy.weaknesses, dragon_dict['weaknesses'])


if __name__ == '__main__':
    unittest.main()