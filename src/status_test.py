import unittest
from status import Status

class TestStatus(unittest.TestCase):

    def test_invalid_status_type(self):
        valid = Status.is_type_valid("invalid")
        self.assertFalse(valid)

    def test_vaild_status_type(self):
        valid = Status.is_type_valid("burn")
        self.assertTrue(valid)

    def test_invalid_creation(self):
        invalid_status = Status.create("Invalid")
        self.assertIsNone(invalid_status)

    def test_valid_creation(self):
        valid_status = Status.create("burn")
        self.assertIsNotNone(valid_status)

    def test_status_expires(self):
        burn = Status.create("burn")
        burn.rolls_remaining = 1
        burn.end_of_turn()
        self.assertTrue(burn.is_expired)

if __name__ == '__main__':
    unittest.main()