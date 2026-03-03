"""
Weapon base class represents a weapon that characters can equip.
A weapon can increase attack power, reduce mana cost,
and has a purchase cost.

Weapons modify a character’s strength or intelligence
by applying a multiplier based on the weapon’s attack value.
They can also reduce the mana cost of abilities.
"""

class Weapon:
    def __init__(self, attack = 100, mana_reduction = 0, cost = 0, name = 'Weapon'):
        self.attack = attack
        self.mana_reduction = mana_reduction
        self.cost = cost
        self.name = name

    # Getters
    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost
    
    # Setters
    def set_attack(self, attack):
        self.attack = attack
    
    def set_mana_reduction(self, mana_reduction):
        self.mana_reduction = mana_reduction

    def set_cost(self, cost):
        self.cost = cost

    # Actions
    def buff_strength(self, strength):
        """Return modified strength based on the weapon's attack multiplier."""
        multiplier = self.attack / 100
        return strength * multiplier
    
    def buff_intelligence(self, intelligence):
        """Return modified intelligence based on the weapon's attack multiplier."""
        multiplier = self.attack / 100
        return intelligence * multiplier
    
    def reduce_mana_cost(self, mana_cost):
        """Reduce a mana cost by the weapon's mana_reduction value (minimum 0)."""
        reduction = mana_cost - self.mana_reduction
        if reduction < 0:
            return 0
        else:
            return reduction