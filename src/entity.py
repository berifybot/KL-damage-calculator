from typing import List
from damage_source import Weapon, DamageSource
from element import Element
from status import Status
from status_stats import StatusesStats
from roll_stats import RollStats

class Entity():


    def __init__(self, name: str, max_health: int, weapon: Weapon, weaknesses: List[str] = []):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.weapon = weapon
        self.weaknesses = self.__convert_weaknesses__(weaknesses)
        self.increased_status_effect_chance = False
        self.statuses: List[Status] = []

    def __convert_weaknesses__(self, weaknesses: List[str]) -> List[Element]:
        converted_weaknesses: List[Element] = []
        for weakness in weaknesses:
            converted_weaknesses.append(Element.create(weakness))
        return converted_weaknesses
        

    def get_name(self) -> str:
        return self.name
    
    def get_max_health(self) -> int:
        return self.max_health
    
    def get_current_health(self) -> int:
        return self.current_health
    
    def get_weapon(self) -> Weapon:
        return self.weapon

    def get_weaknesses(self) -> List[Element]:
        return self.weaknesses
    
    def has_increased_status_effect_chance(self) -> bool:
        return self.increased_status_effect_chance
    
    def set_increased_status_effect_chance(self, value: bool) -> None:
        self.increased_status_effect_chance = value

    def check_weakness(self, attacker, roll_stats: RollStats) -> RollStats:
        if self.is_weak_to_element(attacker.weapon.get_element()):
            roll_stats.set_hit_weakness(True)
            roll_stats.damage_dealt += 10
            self.take_damage(attacker.weapon, roll_stats.damage_dealt)
        else:
            self.take_damage(attacker.weapon, roll_stats.damage_dealt)

    def is_weak_to_element(self, element: Element) -> bool:
        for weakness in self.weaknesses:
            if weakness.get_type() == element.get_type():
                return True
        return False
    
    def handle_end_of_turn_statuses(self, statuses_stats) -> StatusesStats:
        for status in self.statuses:
            status_stats = status.end_of_turn()
            if status.is_expired():
                self.__remove_status__(status)
            if status_stats is not None:
                self.take_damage(status, status_stats.damage_dealt)
                statuses_stats.add_status(status_stats)
        return StatusesStats
    
    def __remove_status__(self, search_status: Status) -> None:
        self.statuses = [status for status in self.statuses if status.type != search_status.type]
    
    def add_status(self, status: Status) -> None:
        if status.type in list(map(lambda status: status.type, self.statuses)):
            return
        self.statuses.append(status)

    def take_damage(self, type: Status | DamageSource, amount: int) -> None:
        self.current_health -= amount
        
    
class Player(Entity):
    def __init__(self, name: str, max_health: int, weapon: Weapon, attack_speed: int, weaknesses: List[str] = []):
        super().__init__(name, max_health, weapon, weaknesses)
        self.attack_speed = attack_speed

    def get_attack_speed(self) -> int:
        return self.attack_speed

NAME = "name"
MAX_HEALTH = "max_health"
DAMAGE_SOURCE = "damage_source"
WEAKNESSES = "weaknesses"

class Enemy(Entity):

    @classmethod
    def __invalid_enemy_exception__(cls, prop) -> str:
        raise Exception("Invalid enemy, missing '{prop}'".format(prop = prop))

    @classmethod
    def from_dict(cls, enemy_dict: dict):
        # TODO: Try to implement a schema validator? This seems messy still
        if (NAME not in enemy_dict):
            cls.__invalid_enemy_exception__(NAME)
        if (MAX_HEALTH not in enemy_dict):
            cls.__invalid_enemy_exception__(MAX_HEALTH)
        if (DAMAGE_SOURCE not in enemy_dict):
            cls.__invalid_enemy_exception__(DAMAGE_SOURCE)
        if (WEAKNESSES not in enemy_dict):
            cls.__invalid_enemy_exception__(WEAKNESSES)
        
        weapon = Weapon.from_dict(enemy_dict["damage_source"])
        return Enemy(enemy_dict['name'], enemy_dict['max_health'], weapon,
                     enemy_dict['weaknesses']) 