"""
Team class represents a team of characters (villagers) in the game.
It stores the team name and keeps track of all members on the team.

The Team class has methods to:
- Add villagers to the team
- Check whether the team has been defeated
- Get all living or dead villagers
- Count how many are alive or dead
- Select a random living or dead villager

It is used by the Game class and character classes to manage
combat interactions between teams.
"""

from random import choice
class Team:
    def __init__(self, name):
        self.name = name
        self.villagers = []

    # Actions
    def add_villager(self,villager):
        self.villagers.append(villager)
    
    def is_defeated(self):
        """Return True if the team has no living villagers remaining."""
        if self.get_num_alive() == 0:
            return True
        else: 
            return False
    

    # Getters
    def get_name(self):
        return self.name
    
    def get_all_alive(self):
        """Return a list of villagers whose health is greater than 0."""
        living_villagers = []
        for villager in self.villagers:
            if villager.health > 0:
                living_villagers.append(villager)
        return living_villagers
    
    def get_all_dead(self):
        """Return a list of villagers whose health is exactly 0."""
        dead_villagers = []
        for villager in self.villagers:
            if villager.health == 0:
                dead_villagers.append(villager)
        return dead_villagers
    
    def get_num_alive(self):
        """Return number of living villagers."""
        return len(self.get_all_alive())
    
    def get_num_dead(self):
        """Return number of dead villagers."""
        return len(self.get_all_dead())
    
    def get_rand_alive(self):
        """Return a random living villager, or None if no one is alive."""
        all_alive = self.get_all_alive()
        if not all_alive:
            return None
        return choice(all_alive)
    
    def get_rand_dead(self):
        """Return a random dead villager."""
        all_dead = self.get_all_dead()
        return choice(all_dead)