"""Manages the battle simulation, team setup, and turn based combat."""

import random
from classes.team import Team
from classes.weapons.sword import Sword
from classes.weapons.staff import Staff
class Game:
    def __init__(self, gold, avail_types, play=False, seed=None):
        self.gold = gold
        self.avail_types = avail_types
        self.play = play
        self.seed = seed
        
        if seed is not None:
            random.seed(seed)

        # create teams
        self.team_a = None
        self.team_b = None
        
        self.turn = 0

        self.team_a = self.user_choose_team()
        self.team_b = self.create_rand_team()
    
    def simulate(self):
        """
        Run the battle simulation until one team is defeated.

        - Teams take turns selecting a random alive member to act.
        - Displays turn number, actions, and remaining mana/health.
        - If play=True, waits for user input between turns.
        - Announces the winning team at the end.
        """    
        print("\nBattle Start!\n")
        round = 1
        while not self.team_a.is_defeated() and not self.team_b.is_defeated():
            print('-------')
            print(f'Turn {round}')
            print('-------')

            # teams take turns
            if self.turn % 2 == 0:
                acting_team = self.team_a
                enemy_team = self.team_b
            else:
                acting_team = self.team_b
                enemy_team = self.team_a
            # get a random attacker thats alive and act
            attacker = acting_team.get_rand_alive()
            attacker.act(acting_team, enemy_team)

            if self.play:
                input("Press Enter to continue...")

            self.turn += 1
            round+=1

        print('\n')
        print('------------')
        if self.team_a.is_defeated():
            print("Team B wins, better luck next time!")
        else:
            print("Team A wins, congratulations!")
        print('-------------')



    def create_rand_team(self):
        """
        Create a random team using available gold.

        - Randomly selects characters from available types.
        - Adds them to the team as long as there is enough gold.
        - Returns the Team object.
        """
        team = Team("B")
        remaining_gold = self.gold

        while remaining_gold > 0:
            char_type = random.choice(self.avail_types)
            character = char_type()

            if character.get_cost() <= remaining_gold:
                team.add_villager(character)
                remaining_gold -= character.get_cost()

        return team

    def user_choose_team(self):
        """
        Allow the user to build their team within the gold budget.

        - Displays available character types and their costs.
        - Lets the user select characters by index.
        - Prompts to equip a weapon if possible.
        - Subtracts character and weapon costs from remaining gold.
        - Returns the Team object.
        """
        team = Team("A")
        remaining_gold = self.gold

        print(f"You have {remaining_gold} gold.")

        while remaining_gold >= 100:
            print("\nAvailable characters:")
            for i, char_type in enumerate(self.avail_types):
                temp = char_type()
                print(f"{i}. {temp.get_name()} (Cost: {temp.get_cost()})")
            
            choice = None

            while True:
                # give user an option to start battle even if they didn't spend all their gold
                try:
                    choice = int(input("Choose character index: "))
                    
                    if 0 <= choice < len(self.avail_types):
                        break
                    else:
                        print(f"Please enter a number between 0-{len(self.avail_types)-1}")
                
                except ValueError:
                    print(f"Please enter a number between 0-{len(self.avail_types)-1}")
            
            character = self.avail_types[choice]()

            if character.get_cost() <= remaining_gold:
                # ask player if they want to equip weapon
                team.add_villager(character)
                print(f"{character.get_name()} added.")
                remaining_gold -= character.get_cost()
                print(f"Gold left: {remaining_gold}")
                if remaining_gold > 0:
                    if hasattr(character, "equip_weapon"):
                        weapon_choice = input("Equip weapon for 50 gold? (y/n): ")
                        if weapon_choice.lower() == "y":
                            if character.get_name() == "Fighter" or character.get_name() == "Berserker" :
                                character.equip_weapon(Sword())
                            elif character.get_name() == "Mage" or character.get_name() == "Archmage" or character.get_name() == "Necromancer":
                                character.equip_weapon(Staff())
                            remaining_gold -= character.get_weapon().cost
                            print(f"Gold left: {remaining_gold}")
            else:
                print("Not enough gold!")

        return team
