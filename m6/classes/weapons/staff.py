"""Staff weapon that reduces mana cost of abilities."""
from .weapon import Weapon

class Staff(Weapon):
    def __init__(self):
        super().__init__(attack=100, mana_reduction=5, cost=50, name='Staff')