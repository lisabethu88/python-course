"""
Villager base class represents a generic character (villager) in the game.
It stores basic stats such as health, mana, strength, intelligence,
and the character's weapon. 

Villager provides methods to:
- Check if alive
- Heal or take damage
- Use and regenerate mana
- Equip weapons
- Get and set character attributes

The act() method is meant to be overridden by subclasses to define that character's behavior in combat.
"""

from classes.weapons.fist import Fist

class Villager:
    def __init__(self, health=0, mana=0, strength=0, intelligence = 0, cost = 0, weapon = Fist(), name='Villager', mana_cost=0):
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.strength = strength 
        self.intelligence = intelligence
        self.name = name
        self.cost = cost
        self.weapon = weapon
        self.mana_cost = mana_cost
       
# Actions
    def is_alive(self):
        """Return True if the villager's health is greater than 0."""
        return self.health > 0
    
    def heal(self, points):
        """Increase health by a given amount, up to max_health."""
        self.health += points
        if self.health > self.max_health:
            self.health = self.max_health

    def use_mana(self, points):
        """Decrease mana by a given amount, but not below 0."""
        self.mana -= points
        if self.mana < 0:
            self.mana = 0

    def regen_mana(self, points):
        """Increase mana by a given amount, up to max_mana."""
        self.mana += points
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def receive_damage(self, points):
        """Reduce health by the damage amount, not going below 0. Prints status messages if the villager is hurt or dies."""
        self.health -= points
        if self.health < 0:
            self.health = 0
        print(f'{self.name} hurt with remaining hp {self.health}.')
        if not self.is_alive():
            print(f'{self.name} died!')
    
    def act(self, ally_team, enemy_team):
        """Placeholder method for character actions during combat. Must be implemented by subclasses."""
        raise NotImplementedError("This act has not been implemented yet.")
    
    def equip_weapon(self, weapon):
        """Equip a weapon to the villager."""
        self.weapon = weapon

    
# Getters
    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def get_max_health (self):
        return self.max_health
    
    def get_mana (self):
        return self.mana
    
    def get_max_mana(self):
        return self.max_mana
    
    def get_strength(self):
        return self.strength
    
    def get_intelligence(self):
        return self.intelligence
    
    def get_cost(self):
        return self.cost
    
    def get_weapon(self):
        return self.weapon
    
# Setters
    def set_max_health(self, health):
        self.max_health = health

    def set_max_mana(self, mana):
        self.max_mana = mana

    def set_strength(self, strength):
        self.strength = strength

    def set_intelligence(self, intelligence):
        self.intelligence = intelligence

    def set_cost(self, cost):
        self.cost = cost

    def set_weapon(self, weapon):
        self.weapon = weapon