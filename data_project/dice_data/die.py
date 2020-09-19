from random import randint

class Die(object):
    """A class to represent a dice"""
    def __init__(self, num_sides=6):
        """Assume a six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Returns a value for a roll"""
        return randint(1, self.num_sides)