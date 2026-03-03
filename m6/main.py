"""
Main script launches a simulated battle between two teams.
It creates the starting gold budget and the character classes that can
be recruited (Fighter, Mage, Berserker, Necromancer, and Archmage).
A Game object is created with a fixed random seed to make sure there are consistent
results across runs, and the simulate() method is run to perform
the battle.
"""

from classes.characters.fighter import Fighter
from classes.characters.mage import Mage
from classes.game import Game
from classes.characters.berserker import Berserker
from classes.characters.necromancer import Necromancer
from classes.characters.archmage import Archmage

def main():
    gold = 600
    available_types = [Fighter, Mage, Berserker, Necromancer, Archmage] 
    
    game = Game(gold, available_types, play=False, seed=42)
    game.simulate()

if __name__ == "__main__":
    main()