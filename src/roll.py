import random

die_roller = lambda: random.choice([1, 2, 3, 4, 5, 6])

class Roll():

    @classmethod
    def random_roll(cls) -> int:
        return die_roller()
    