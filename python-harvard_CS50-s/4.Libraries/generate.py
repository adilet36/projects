"""
from random import choice

coin = choice(["heads", "tails"])
print(coin)
"""

"""
import random as r 

number = r.randint(1,10)
print(number)
"""

import random as r

cards = ["jack", "queen", "king"]
r.shuffle(cards)
for card in cards:
    print(card)
