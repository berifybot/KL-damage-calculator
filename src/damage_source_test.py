from damage_source import Weapon, Element
import unittest

test_weapon = {
    "name": "test_weapon",
    "base_damage": 25,
    "element": "Fire",
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
        self.assertEqual(weapon.get_element(), getattr(Element, test_weapon['element']))
        self.assertEqual(weapon.get_attack_type().get_type(), test_weapon['damage_type'])

if __name__ == '__main__':
    unittest.main()
