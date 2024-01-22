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
        enemy = Enemy()
        self.assertIsNotNone(enemy)

    def test_load_creation(self):
        enemy = Enemy()
        enemy.load(dragon_dict)
        self.assertEquals(enemy.name, "Dragon")
        self.assertEquals(enemy.max_health, 500)
        self.assertEquals(enemy.base_damage, 25)
        self.assertEquals(enemy.damage_type, "melee")
        self.assertEquals(enemy.weaknesses, ['water', 'melee'])


if __name__ == '__main__':
    unittest.main()