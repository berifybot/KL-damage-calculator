from damage_source import Weapon, AttackType
import unittest

test_weapon = {
    "name": "test_weapon",
    "base_damage": 25,
    "element": "fire",
    "damage_type": "melee"
}

class TestDamageSource(unittest.TestCase):
    
    def test_default_weapon_creation(self):
        weapon = Weapon(test_weapon['name'],
                        test_weapon['base_damage'],
                        test_weapon['element'],
                        test_weapon['damage_type'])
        
        self.assertIsNotNone(weapon)
        self.assertEqual(weapon.get_name(), test_weapon['name'])
        self.assertEqual(weapon.get_base_damage(), test_weapon['base_damage'])
        self.assertEqual(weapon.get_element(), test_weapon['element'])
        self.assertEqual(weapon.get_attack_type().get_type(), test_weapon['damage_type'])

    def test_weapon_from_dict_creation(self):
        weapon = Weapon.from_dict(test_weapon)
        
        self.assertEqual(weapon.get_name(), test_weapon['name'])
        self.assertEqual(weapon.get_base_damage(), test_weapon['base_damage'])
        self.assertEqual(weapon.get_element().get_type(), test_weapon['element'])
        self.assertEqual(weapon.get_attack_type().get_type(), test_weapon['damage_type'])

class TestAttackType(unittest.TestCase):

    def test_invalid_attack_type(self):
        valid = AttackType.is_type_valid("invalid")
        self.assertEqual(False, valid)

    def test_valid_attack_types_lower_case(self):
        melee_valid = AttackType.is_type_valid("melee")
        range_valid = AttackType.is_type_valid("range")
        magic_valid = AttackType.is_type_valid("magic")
        ability_valid = AttackType.is_type_valid("ability")

        self.assertEqual(True, melee_valid)
        self.assertEqual(True, range_valid)
        self.assertEqual(True, magic_valid)
        self.assertEqual(True, ability_valid)

    def test_valid_attack_types_random_case(self):
        melee_valid = AttackType.is_type_valid("mElEe")
        range_valid = AttackType.is_type_valid("RAnGe")
        magic_valid = AttackType.is_type_valid("MAgiC")
        ability_valid = AttackType.is_type_valid("ABIliTy")

        self.assertEqual(True, melee_valid)
        self.assertEqual(True, range_valid)
        self.assertEqual(True, magic_valid)
        self.assertEqual(True, ability_valid)

if __name__ == '__main__':
    unittest.main()
