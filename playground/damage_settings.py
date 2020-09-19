import random


def damage_rand(start, stop, crit_mult = 1.3, crit_odds = 0.1):
    crit_odds = int(((crit_odds * 100) / 10) + 1)
    crit_num = random.randint(1, 10)
    crit_chance = range(1,crit_odds)
    if crit_num in crit_chance:
        return int(stop * crit_mult)
    else:
        return int(random.randint(start, stop))

