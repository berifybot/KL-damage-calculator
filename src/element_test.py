import unittest
from element import Element
from mock_objects import TestEnemyCreator, TestPlayerCreator, TestWeaponCreator

class TestElement(unittest.TestCase):

    def test_invalid_element_type(self):
        valid = Element.is_type_valid("invalid")
        self.assertFalse(valid)

    def test_valid_element_type(self):
        valid = Element.is_type_valid("fire")
        self.assertTrue(valid)

    def test_invalid_creation(self):
        invalid_element = Element.create("Invalid")
        self.assertEqual(invalid_element, None)

    def test_valid_creation_lower_case(self):
        valid_element = Element.create("fire")
        self.assertEqual(valid_element.get_type(), "fire")

    def test_valid_creation_capital_case(self):
        valid_element = Element.create("Fire")
        self.assertEqual(valid_element.get_type(), "fire")

    def test_valid_creation_mixed_case(self):
        valid_element = Element.create("fIRe")
        self.assertEqual(valid_element.get_type(), "fire")

    def test_apply_status_returns_valid_status(self):
        weapon = TestWeaponCreator.create()
        player = TestPlayerCreator.create(weapon=weapon)
        enemy = TestEnemyCreator.create(weapon=None)
        fire_elem: Element = Element.create("fire")
        stats = fire_elem.apply_status(player, enemy)
        self.assertTrue(stats.applied_status.type == "burn")


if __name__ == '__main__':
    unittest.main()