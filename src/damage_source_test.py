from damage_source import Weapon, Element, AttackType
import unittest

test_weapon = {
    "name": "test_weapon",
    "base_damage": 25,
    "element": "Fire",
    "damage_type": "Melee"
}

class TestDamageSource(unittest.TestCase):
    
    def test_default_weapon_creation(self):
        weapon = Weapon(test_weapon['name'],
                        test_weapon['base_damage'],
                        test_weapon['element'],
                        test_weapon['damage_type'])
        
        self.assertIsNotNone(weapon)
        self.assertEqual(weapon.name, test_weapon['name'])
        self.assertEqual(weapon.base_damage, test_weapon['base_damage'])
        self.assertEqual(weapon.element, test_weapon['element'])
        self.assertEqual(weapon.attack_type, test_weapon['damage_type'])

    def test_weapon_from_dict_creation(self):
        weapon = Weapon.from_dict(test_weapon)
        
        self.assertEqual(weapon.name, test_weapon['name'])
        self.assertEqual(weapon.base_damage, test_weapon['base_damage'])
        self.assertEqual(weapon.element, getattr(Element, test_weapon['element']))
        self.assertEqual(weapon.attack_type, getattr(AttackType, test_weapon['damage_type']))

if __name__ == '__main__':
    unittest.main()
