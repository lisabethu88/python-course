"""Default weapon for villagers with standard attack and no cost."""
from .weapon import Weapon

class Fist(Weapon):
    def __init__(self):
        super().__init__(attack=100, mana_reduction=0, cost=0, name="Fist")