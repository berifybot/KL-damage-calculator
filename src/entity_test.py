import unittest
from entity import Enemy, Player
from element import Element
from mock_objects import TestEnemyCreator
from status import Status
from status_stats import StatusesStats


dragon_dict = {
        "name": "Dragon",
        "max_health": 500,
        "damage_source": {
            "name": "dragon_breath",
            "base_damage": 25,
            "element": "Fire",
            "damage_type": "Melee",
        },
        "weaknesses": ["Water", "Melee"]
}

test_weapon = {
    "name": "test_weapon",
    "base_damage": 25,
    "element": "Fire",
    "damage_type": "Melee"
}

class TestEntity(unittest.TestCase):

    def test_is_weak_to_non_weakness(self):
        enemy = TestEnemyCreator.create(None, weaknesses=["Fire"])

        element = Element.create("Water")

        is_weak_to = enemy.is_weak_to_element(element)

        self.assertEqual(is_weak_to, False)

    def test_is_weak_to_weakness(self):
        enemy = TestEnemyCreator.create(None, weaknesses=["Fire"])

        element = Element.create("Fire")
    
        is_weak_to = enemy.is_weak_to_element(element)

        self.assertEqual(is_weak_to, True)

    def test_end_of_turn_statuses_expire(self):
        enemy = TestEnemyCreator.create(None)
        status = Status.create("burn")
        enemy.add_status(status)

        self.assertTrue(len(enemy.statuses) == 1)

        status.rolls_remaining = 1
        enemy.handle_end_of_turn_statuses(StatusesStats())

        self.assertTrue(len(enemy.statuses) == 0)

    def test_end_of_turn_statuses_deal_damage(self):
        enemy = TestEnemyCreator.create(None, max_health=50)
        status = Status.create("burn")
        enemy.add_status(status)
        status.rolls_remaining = 2
        enemy.handle_end_of_turn_statuses(StatusesStats())
        self.assertTrue(enemy.current_health == 45)

    def test_end_of_turn_statuses_deal_damage_before_expiring(self):
        enemy = TestEnemyCreator.create(None, max_health=50)
        status = Status.create("burn")
        enemy.add_status(status)
        status.rolls_remaining = 1
        enemy.handle_end_of_turn_statuses(StatusesStats())
        self.assertTrue(len(enemy.statuses) == 0)
        self.assertTrue(enemy.current_health == 45)


class TestEnemy(unittest.TestCase):

    def test_enemy_default_creation(self):
        enemy = Enemy(dragon_dict['name'],
                      dragon_dict['max_health'],
                      dragon_dict['damage_source'],
                      dragon_dict['weaknesses'])
        self.assertIsNotNone(enemy)
        self.assertEqual(enemy.get_name(), dragon_dict['name'])
        self.assertEqual(enemy.get_max_health(), dragon_dict['max_health'])
        self.assertEqual(enemy.get_current_health(), dragon_dict['max_health'])
        self.assertEqual(len(enemy.get_weaknesses()), 2)

    def test_enemy_from_dict_creation(self):
        enemy = Enemy.from_dict(dragon_dict)
        self.assertEqual(enemy.get_name(), dragon_dict['name'])
        self.assertEqual(enemy.get_max_health(), dragon_dict['max_health'])
        self.assertEqual(enemy.get_current_health(), dragon_dict['max_health'])
        self.assertEqual(len(enemy.get_weaknesses()), 2)

class TestPlayer(unittest.TestCase):

    def test_player_default_creation(self):
        player_name = "test_player"
        max_health = 500
        attack_speed = 5

        player = Player(player_name, max_health, test_weapon, attack_speed)
        self.assertEqual(player.get_name(), player_name)
        self.assertEqual(player.get_max_health(), max_health)
        self.assertEqual(player.get_attack_speed(), attack_speed)

    def test_player_no_optional_creation(self):
        player_name = "test_player"
        max_health = 500
        attack_speed = 5
        weaknesses = ["Water", "Fire"]

        player = Player(player_name, max_health, test_weapon, attack_speed, weaknesses)
        self.assertEqual(player.get_name(), player_name)
        self.assertEqual(player.get_max_health(), max_health)
        self.assertEqual(player.get_attack_speed(), attack_speed)
        self.assertEqual(len(player.get_weaknesses()), 2)

if __name__ == '__main__':
    unittest.main()