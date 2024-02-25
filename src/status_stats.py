from typing import List

class StatusStats():

    def __init__(self, type: str):
        self.type = type
        self.damage_dealt = 0
        self.rolls_remaining = 0

class StatusesStats():

    def __init__(self):
        self.statuses: List[StatusStats]  = []

    def add_status(self, status: StatusStats):
        self.statuses.append(status)
