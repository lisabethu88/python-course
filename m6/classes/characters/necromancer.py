from .mage import Mage

class Necromancer(Mage):
    def __init__(self):
        super().__init__(name="Necromancer", cost=400)
    
    def act(self, ally_team, enemy_team):
        # check if 20 mana and at least one dead ally
        if self.mana >= 20 and ally_team.get_num_dead() >= 1:
            print(f'Team {ally_team.get_name()} member {self.name} acts.')
            rand_ally = ally_team.get_rand_dead()
            rand_ally.heal(int(rand_ally.get_max_health() / 2))
            self.use_mana(self.mana_cost)
            print(f'Reviving {rand_ally.get_name()} with {rand_ally.get_health()} hp.')
        else: # act as a regular mage
            super().act(ally_team, enemy_team)
