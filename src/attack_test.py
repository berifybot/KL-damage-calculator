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

    def test_1_roll_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(1, 1)
        self.assertEqual(applied, False)

    def test_4_roll_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(4, 1)
        self.assertEqual(applied, False)

    def test_5_then_5_roll_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(5, 5)
        self.assertEqual(applied, False)
    
    def test_5_then_6_does_apply_status_for_normal_elements(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(5, 6)
        self.assertEqual(applied, True)

    def test_6_then_4_does_not_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(6, 4)
        self.assertEqual(applied, False)

    def test_6_then_5_does_apply_status(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(6, 5)
        self.assertEqual(applied, True)

    def test_5_then_6_does_not_apply_status_for_low_chance_elements(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon1 = TestWeaponCreator().create(element = "Wind")
        player1 = TestPlayerCreator.create(weapon1)
        attack1 = Attack(host, player1, enemy)

        applied1 = attack1.__did_status_apply__(5, 6)
        self.assertEqual(applied1, False)

        weapon2 = TestWeaponCreator.create(element = "Lightning")
        player2 = TestPlayerCreator().create(weapon2)
        attack2 = Attack(host, player2, enemy)

        applied2 = attack2.__did_status_apply__(5, 6)
        self.assertEqual(applied2, False)
        
    def test_5_then_5_applies_status_with_increased_chance(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        player.increased_status_effect_chance = True
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(5, 5)
        self.assertEqual(applied, True)

    def test_6_then_4_applies_status_with_increased_chance(self):
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create()
        player = TestPlayerCreator.create(weapon)
        player.increased_status_effect_chance = True
        attack = Attack(host, player, enemy)

        applied = attack.__did_status_apply__(6, 4)
        self.assertEqual(applied, True)

    def test_damage_from_roll_1(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda a: 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        damage = attack.__get_damage_from_roll__(1)
        self.assertEqual(0, damage)

    def test_damage_from_roll_2(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        damage = attack.__get_damage_from_roll__(2)
        self.assertEqual(0, damage)

    def test_damage_from_roll_3(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        damage = attack.__get_damage_from_roll__(3)
        self.assertEqual(12, damage)

    def test_damage_from_roll_4(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", 1)
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        damage = attack.__get_damage_from_roll__(4)
        self.assertEqual(25, damage)

    def test_damage_from_roll_5(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 1 )
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        damage = attack.__get_damage_from_roll__(5)
        self.assertEqual(28, damage)

    def test_damage_from_roll_6(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 1 )
        enemy = TestEnemyCreator().create(None)
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        damage = attack.__get_damage_from_roll__(6)
        self.assertEqual(30, damage)

    def test_non_weakness_attack(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 1 )
        enemy = TestEnemyCreator().create(None, max_health=50, weaknesses=["Fire"])
        weapon = TestWeaponCreator().create(base_damage=base_damage)
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        attack.execute_roll(4)

        self.assertEqual(enemy.current_health, 25)

    def test_weakness_attack(self):
        base_damage = 25
        host = TestBattleHost(2, 25, "Melee", lambda: 1 )
        enemy = TestEnemyCreator().create(None, max_health=50, weaknesses=["Fire"])
        weapon = TestWeaponCreator().create(base_damage=base_damage, element="Fire")
        player = TestPlayerCreator.create(weapon)
        attack = Attack(host, player, enemy)

        attack.execute_roll(4)
        self.assertEqual(enemy.current_health, 15)




if __name__ == '__main__':
    unittest.main()