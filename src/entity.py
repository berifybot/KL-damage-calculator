from typing import List
from damage_source import Weapon, Element

class Entity():
    def __init__(self, name: str, max_health: int, weapon: Weapon, weaknesses: List[Element] = []):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.weapon = weapon
        self.weaknesses = weaknesses

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