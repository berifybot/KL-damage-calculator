from typing import List

class StatusStats():

    def __init__(self, status_type: str, status_category: str):
        self.type = status_type
        self.category = status_category
        self.damage_dealt = 0
        self.rolls_remaining = 0

class StatusesStats():

    def __init__(self):
        self.statuses: List[StatusStats]  = []

    def add_status(self, status: StatusStats):
        self.statuses.append(status)


UNKNOWN_STAT_STRING = "Unknown"
class StatusStatPrinter():

    def __init__(self, stats: StatusStats):
        self.stats = stats

    def get_stats_string(self) -> str:
        return UNKNOWN_STAT_STRING
    
    @classmethod
    def create(cls, stats: StatusStats) -> None:
        match stats.category:
            case "flat_end":
                return FlatEndOfTurnPrinter(stats)
            case _:
                return None
            
class FlatEndOfTurnPrinter(StatusStatPrinter):

    def __init__(self, stats: StatusStats):
        super().__init__(stats)

    def get_stats_string(self) -> str:
        str = ""
        stats = self.stats
        str += "{damage} damage was taken from {status}\n".format(damage = stats.damage_dealt, status = stats.type)
        str += "\t{status} has {rolls} rolls remaining".format(status=stats.type, rolls=stats.rolls_remaining)
        return str

    