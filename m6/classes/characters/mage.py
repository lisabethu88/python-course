"""
A Mage is a magic-based villager that uses intelligence to attack
enemies and consumes mana for abilities. Mages can equip a Staff
or default Fist to boost intelligence and reduce mana costs.
"""
from .villager import Villager

class Mage(Villager):
    def __init__(self, name="Mage", health=800, intelligence=400, mana=50, cost=200, mana_cost=20):
        super().__init__(
            name=name,
            health=health,
            intelligence=intelligence,
            mana=mana,
            cost=cost,
            mana_cost=mana_cost
        )

    def act(self, ally_team, enemy_team):
        """Perform the Mage's action in combat.

        - If the Mage lacks enough mana, meditate to regain 30 mana.
        - Otherwise, consume mana and deal damage equal to intelligence
        to a random living enemy.
        - Prints action and remaining mana.
        """    
        enemy = enemy_team.get_rand_alive()
        
        if self.mana < self.mana_cost:
            self.regen_mana(30) # meditate and add mana, skip attack
            print(f'Recovered mana to {self.mana}.')
        else:
            self.use_mana(self.mana_cost) # consume mana
            
            # print action to console
            print(f'Team {ally_team.get_name()} member {self.name} acts.')
            print(f'Hurt enemy {enemy.get_name()} for {self.intelligence} damage.')
            enemy.receive_damage(self.intelligence) # attack
        print(f'{self.name} has {self.mana} mana remaining.')
        
    def equip_weapon(self, weapon):
        """Equip a weapon if possible.
        - Can equip Staff or default Fist.
        - Buffs intelligence and reduces mana cost according to the weapon.
        - Prints confirmation or rejection message.
        """
        if weapon.name == 'Staff' or weapon.name == 'Fist':
            self.weapon = weapon
            self.intelligence = int(self.weapon.buff_intelligence(self.intelligence))
            self.mana_cost = self.weapon.reduce_mana_cost(self.mana_cost)
            print(f'{self.name} equipped {weapon.name}.')
        else:
            print(f'{self.name} cannot equip {weapon.name}!')