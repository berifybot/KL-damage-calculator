import unittest
from enemy import Enemy
from roll import Roll

test_dragon_dict = {
        "name": "Dragon",
        "max_health": 500,
        "base_damage": 25,
        "damage_type": "melee",
        "weaknesses": ["water", "melee"]
}

class TestRoll(unittest.TestCase):
    def setUp(self):
        self.test_dragon = Enemy(test_dragon_dict)

    def test_default_creation(self):
        roll = Roll(50, self.test_dragon)
        self.assertEqual(roll.damage, 50)

    def test_1_roll(self):
        roll = Roll(50, self.test_dragon, lambda: 1)
        roll.execute_roll()
        self.assertEqual(roll.roll, 1)
        self.assertEqual(roll.damage_dealt, 0)
        self.assertEqual(roll.enemy.current_health, 500)

    def test_2_roll(self):
        roll = Roll(50, self.test_dragon, lambda: 2)
        roll.execute_roll()
        self.assertEqual(roll.roll, 2)
        self.assertEqual(roll.damage_dealt, 0)
        self.assertEqual(roll.enemy.current_health, 500)

    def test_3_roll_no_round(self):
        roll = Roll(50, self.test_dragon, lambda: 3)
        roll.execute_roll()
        self.assertEqual(roll.roll, 3)
        self.assertEqual(roll.damage_dealt, 25)
        self.assertEqual(roll.enemy.current_health, 475)

    def test_3_roll_with_round(self):
        # Round down
        roll = Roll(51, self.test_dragon, lambda: 3)
        roll.execute_roll()
        self.assertEqual(roll.roll, 3)
        self.assertEqual(roll.damage_dealt, 25)
        self.assertEqual(roll.enemy.current_health, 475)

    def test_4_roll(self):
        roll = Roll(50, self.test_dragon, lambda: 4)
        roll.execute_roll()
        self.assertEqual(roll.roll, 4)
        self.assertEqual(roll.damage_dealt, 50)
        self.assertEqual(roll.enemy.current_health, 450)

    def test_5_roll(self):
        roll = Roll(50, self.test_dragon, lambda: 5)
        roll.execute_roll()
        self.assertEqual(roll.roll, 5)
        self.assertEqual(roll.damage_dealt, 53)
        self.assertEqual(roll.enemy.current_health, 447)

    def test_6_roll(self):
        roll = Roll(50, self.test_dragon, lambda: 6)
        roll.execute_roll()
        self.assertEqual(roll.roll, 6)
        self.assertEqual(roll.damage_dealt, 55)
        self.assertEqual(roll.enemy.current_health, 445)

    def test_invalid_roll_raises_exception(self):
        roll = Roll(50, self.test_dragon, lambda: 7)
        self.assertRaises(Exception, roll.execute_roll)

if __name__ == '__main__':
    unittest.main()