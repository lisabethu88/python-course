"""Physical combat subclass of Villager that uses strength to attack."""
from .villager import Villager

class Fighter(Villager):
    def __init__(self, name="Fighter", health=1200, strength=100, cost=100):
        super().__init__(
            name=name,
            health=health,
            strength=strength,
            cost=cost
        )

    def act(self, ally_team, enemy_team):
        """
        Perform the Fighter's combat action.

        Selects a random living enemy and deals damage
        equal to the Fighter's strength.
        """
        print(f'Team {ally_team.name} member {self.name} acts.')
        enemy = enemy_team.get_rand_alive()
      
        # print action to console
        print(f'Hurt enemy {enemy.name} for {self.strength} damage.')
        enemy.receive_damage(self.strength)

    def equip_weapon(self, weapon):
        """
        Equip a weapon if possible.

        - Can equip Sword or default Fist.
        - Buffs strength based on the weapon's attack value.
        - Prints confirmation or rejection message.
        """
        if weapon.name == 'Sword' or weapon.name == 'Fist':
            self.weapon = weapon
            self.strength = int(self.weapon.buff_strength(self.strength))
            print(f'{self.name} equipped {weapon.name}.')
        else:
            print(f'{self.name} cannot equip {weapon.name}!')