import unittest
from roll import Roll

class TestRoll(unittest.TestCase):
    def test_default_creation(self):
        roll = Roll(50)
        self.assertEqual(roll.damage, 50)

    def test_1_roll(self):
        roll = Roll(50, lambda: 1)
        self.assertEqual(roll.roll, 1)
        self.assertEqual(roll.execute_roll(), 0)

    def test_2_roll(self):
        roll = Roll(50, lambda: 2)
        self.assertEqual(roll.roll, 2)
        self.assertEqual(roll.execute_roll(), 0)

    def test_3_roll_no_round(self):
        roll = Roll(50, lambda: 3)
        self.assertEqual(roll.roll, 3)
        self.assertEqual(roll.execute_roll(), 25)

    def test_3_roll_with_round(self):
        # Round down
        roll = Roll(51, lambda: 3)
        self.assertEqual(roll.roll, 3)
        self.assertEqual(roll.execute_roll(), 25)

    def test_4_roll(self):
        roll = Roll(50, lambda: 4)
        self.assertEqual(roll.roll, 4)
        self.assertEqual(roll.execute_roll(), 50)

    def test_5_roll(self):
        roll = Roll(50, lambda: 5)
        self.assertEqual(roll.roll, 5)
        self.assertEqual(roll.execute_roll(), 53)

    def test_6_roll(self):
        roll = Roll(50, lambda: 6)
        self.assertEqual(roll.roll, 6)
        self.assertEqual(roll.execute_roll(), 55)

    def test_invalid_roll_raises_exception(self):
        roll = Roll(50, lambda: 7)
        self.assertRaises(Exception, roll.execute_roll)

if __name__ == '__main__':
    unittest.main()