"""Fighter subclass that deals double damage at half health or lower."""
from .fighter import Fighter

class Berserker(Fighter):
    def __init__(self):
        super().__init__(name="Berserker", cost=200)
        
    def act(self, ally_team, enemy_team):
        """
        Perform the Berserker's combat action.

        - If health is above half, act like a normal Fighter.
        - If health is half or below, enter Berserk mode
        and deal double strength damage.
        """
        if self.health <= self.max_health / 2:
            print(f'Team {ally_team.name} member {self.name} acts.')
            enemy = enemy_team.get_rand_alive()
            
            # print action to console
            print(f'Berserk mode! Attack double!')
            double_strength = int(self.strength * 2)
            print(f'Hurt enemy {enemy.get_name()} for {double_strength} damage.')
            enemy.receive_damage(double_strength)
        else:
            super().act(ally_team, enemy_team)