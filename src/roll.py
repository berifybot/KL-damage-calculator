import random

die_roller = lambda: random.choice([1, 2, 3, 4, 5, 6])

class Roll():

    @classmethod
    def random_roll(cls):
        return die_roller()


    # Todo: Add defined_roll, passing in the host to perform the roll input
    