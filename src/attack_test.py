import unittest
from attack import Attack
from mock_objects import TestBattleHost, TestPlayerCreator, TestEnemyCreator, TestWeaponCreator

class TestAttack(unittest.TestCase):

    def test_default_creation(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        self.assertIsNotNone(attack)

    def test_non_weakness_attack(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 4 )
        enemy = TestEnemyCreator().create(None, max_health=50, weaknesses=["Fire"])
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        roll_stats = attack.execute_roll()

        self.assertEqual(enemy.current_health, 25)
        self.assertEqual(roll_stats.damage_dealt, 25)

    def test_weakness_attack(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 4)
        enemy = TestEnemyCreator().create(None, max_health=50, weaknesses=["Fire"])
        weapon = TestWeaponCreator().create(base_damage=base_damage, element="Fire")
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        roll_stats = attack.execute_roll()
        self.assertEqual(enemy.current_health, 15)
        self.assertEqual(roll_stats.damage_dealt, 35)
        



if __name__ == '__main__':
    unittest.main()