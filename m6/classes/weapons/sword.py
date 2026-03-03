"""
Sword weapon that increases physical attack power.
"""

from .weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__(attack=150, cost=50, name='Sword')