import unittest
from roll_damage import RollDamage
from mock_objects import TestBattleHost, TestPlayerCreator, TestEnemyCreator, TestWeaponCreator

class RollDamageTest(unittest.TestCase):
    
    def test_1_roll_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(1, 1)
        self.assertEqual(applied, False)

    def test_4_roll_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(4, 1)
        self.assertEqual(applied, False)

    def test_5_then_5_roll_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(5, 5)
        self.assertEqual(applied, False)
    
    def test_5_then_6_does_apply_status_for_normal_elements(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(5, 6)
        self.assertEqual(applied, True)

    def test_6_then_4_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(6, 4)
        self.assertEqual(applied, False)

    def test_6_then_5_does_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(6, 5)
        self.assertEqual(applied, True)

    def test_5_then_6_does_not_apply_status_for_low_chance_elements(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon1 = TestWeaponCreator().create(element = "Wind")
        player1 = TestPlayerCreator.create(weapon1)
        roll_damage1 = RollDamage(host, player1, enemy)

        applied1 = roll_damage1.__did_status_apply__(5, 6)
        self.assertEqual(applied1, False)

        weapon2 = TestWeaponCreator.create(element = "Lightning")
        player2 = TestPlayerCreator().create(weapon2)
        roll_damage2 = RollDamage(host, player2, enemy)

        applied2 = roll_damage2.__did_status_apply__(5, 6)
        self.assertEqual(applied2, False)
        
    def test_5_then_5_applies_status_with_increased_chance(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        player.increased_status_effect_chance = True
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(5, 5)
        self.assertEqual(applied, True)

    def test_6_then_4_applies_status_with_increased_chance(self):
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        player.increased_status_effect_chance = True
        roll_damage = RollDamage(host, player, enemy)

        applied = roll_damage.__did_status_apply__(6, 4)
        self.assertEqual(applied, True)

    def test_damage_from_roll_1(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        stats = roll_damage.get_damage_from_roll()
        self.assertEqual(0, stats.damage_dealt)

    def test_damage_from_roll_2(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 2)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        stats = roll_damage.get_damage_from_roll()
        self.assertEqual(0, stats.damage_dealt)

    def test_damage_from_roll_3(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 3)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        stats = roll_damage.get_damage_from_roll()
        self.assertEqual(12, stats.damage_dealt)

    def test_damage_from_roll_4(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 4)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        stats = roll_damage.get_damage_from_roll()
        self.assertEqual(25, stats.damage_dealt)

    def test_damage_from_roll_5(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 5)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        stats = roll_damage.get_damage_from_roll()
        self.assertEqual(28, stats.damage_dealt)

    def test_damage_from_roll_6(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 6)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        roll_damage = RollDamage(host, player, enemy)

        stats = roll_damage.get_damage_from_roll()
        self.assertEqual(30, stats.damage_dealt)


if __name__ == '__main__':
    unittest.main()