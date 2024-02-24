from element_stats import ElementStats
from status import Status

class RollStats:
    
    def __init__(self):
        self.applied_status = None
        self.hit_weakness = False
        self.base_roll = 0
        self.critical_roll = 0
        self.did_crit = False
        

    def set_element_stats(self, element_stats: ElementStats) -> None:
        self.applied_status = element_stats.get_applied_status()

    def get_applied_status(self) -> Status:
        return self.applied_status
    
    def set_hit_weakness(self, hit_weakness: bool) -> None:
        self.hit_weakness = hit_weakness

    def get_hit_weakness(self) -> bool:
        return self.hit_weakness

    def set_base_roll(self, base_roll: int) -> None:
        self.base_roll = base_roll

    def get_base_roll(self) -> int:
        return self.base_roll    
    
    def set_critical_roll(self, critical_roll: int) -> None:
        self.critical_roll = critical_roll

    def get_critical_roll(self) -> int:
        return self.critical_roll

    def set_did_crit(self, did_crit: bool) -> None:
        self.did_crit = did_crit

    def get_did_crit(self) -> bool:
        return self.did_crit
    
