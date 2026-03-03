"""Mage subclass with a powerful area attack (KABOOM!) when they are the last ally standing."""
from .mage import Mage

class Archmage(Mage):
    def __init__(self):
        super().__init__(name="Archmage", cost=600)

    def act(self, ally_team, enemy_team):
        """
        Perform the Archmage's combat action.

        - If the Archmage is the only living ally and has enough mana,
        cast "KABOOM!" to deal double intelligence damage to all
        living enemies.
        - Otherwise, behave like a regular Mage.
        """
        if ally_team.get_num_alive() == 1 and self.is_alive() and self.mana >= self.mana_cost:
            print(f'Team {ally_team.get_name()} member {self.name} acts.')
            # cast KABOOM! 
            enemies = enemy_team.get_all_alive()
            print(f'Only one standing. Cast KABOOM! on every enemy alive!')
            for enemy in enemies:
                double_intelligence = 2 * self.intelligence
                print(f'Hurt enemy {enemy.get_name()} for {double_intelligence} damage.')
                enemy.receive_damage(double_intelligence)
            self.use_mana(self.mana_cost)
        else: # act as a regular mage
            super().act(ally_team, enemy_team)
