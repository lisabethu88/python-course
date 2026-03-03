"""
Unit tests for the RPG

This file tests the behavior of different character classes
(Fighter, Mage, Berserker, Archmage, and Necromancer) and
their interactions during combat.

The tests check that:
- Characters deal the correct amount of damage.
- Health and mana values update correctly.
- Weapons can or cannot be equipped depending on the character.
- Special abilities (like Berserker mode, Archmage KABOOM,
  and Necromancer revive) work as expected.
- The correct messages are printed during actions.

Printed output is captured using redirect_stdout so it can
be checked in each test.

Running this file directly will execute all unit tests.
"""

from classes.characters.fighter import Fighter
from classes.team import Team
from classes.characters.mage import Mage
from classes.weapons.sword import Sword
from classes.weapons.staff import Staff
from classes.characters.archmage import Archmage
from classes.characters.necromancer import Necromancer
from classes.characters.berserker import Berserker
import unittest
import io
from contextlib import redirect_stdout

class Test(unittest.TestCase):

    def test_fighter_act_on_fighter(self):
        t1 = Team("A")
        t2 = Team("B")

        f1 = Fighter()
        f2 = Fighter()

        t1.add_villager(f1)
        t2.add_villager(f2)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            f1.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f2.health, 1100)
        self.assertIn("Hurt enemy Fighter for 100 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 1100.", output)

    def test_mage_act_on_fighter(self):
        t1 = Team("A")
        t2 = Team("B")

        m = Mage()
        f = Fighter()

        t1.add_villager(m)
        t2.add_villager(f)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            m.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f.health, 800)
        self.assertEqual(m.mana, 30)
        self.assertIn("Hurt enemy Fighter for 400 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 800.", output)
        self.assertIn("Mage has 30 mana remaining.", output)

        # get the printed output
        file2 = io.StringIO()
        with redirect_stdout(file2):
            m.act(t1, t2)

        output2 = file2.getvalue()

        self.assertEqual(f.health, 400)
        self.assertEqual(m.mana, 10)
        self.assertIn("Hurt enemy Fighter for 400 damage.", output2)
        self.assertIn("Fighter hurt with remaining hp 400.", output2)
        self.assertIn("Mage has 10 mana remaining.", output2)

        # get the printed output
        file3 = io.StringIO()
        with redirect_stdout(file3):
            m.act(t1, t2)

        output3 = file3.getvalue()

        self.assertEqual(m.mana, 40)
        self.assertIn("Recovered mana to 40.", output3)
        self.assertIn("Mage has 40 mana remaining.", output3)

    def test_fighter_equipped_with_sword(self):
        t1 = Team("A")
        t2 = Team("B")
        f1, f2 = Fighter(), Fighter()
        sword = Sword()

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            f1.equip_weapon(sword)
            t1.add_villager(f1)
            t2.add_villager(f2)
            f1.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f2.health, 1050)
        self.assertIn("Fighter equipped Sword.", output)
        self.assertIn("Hurt enemy Fighter for 150 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 1050.", output)
    
    def test_fighter_equipped_with_staff(self):
        f = Fighter()
        staff = Staff()

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            f.equip_weapon(staff)

        output = file.getvalue()

        self.assertIn("Fighter cannot equip Staff!", output)

    def test_mage_equipped_with_sword(self):
        # Mage tries to equip Sword (not allowed)
        m = Mage()
        sword = Sword()

        file = io.StringIO()
        with redirect_stdout(file):
            m.equip_weapon(sword)

        output = file.getvalue()
        self.assertIn("Mage cannot equip Sword!", output)

    def test_mage_equipped_with_staff_acts_on_fighter(self):
        # Team A Mage equipped with a Staff acts on an opponent fighter
        t1 = Team("A")
        t2 = Team("B")

        m = Mage()
        f = Fighter()
        staff = Staff()

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            m.equip_weapon(staff)
            t1.add_villager(m)
            t2.add_villager(f)
            m.act(t1, t2)


        output = file.getvalue()
        self.assertEqual(f.health, 800)
        self.assertEqual(m.mana, 35)
        self.assertIn("Mage equipped Staff.", output)
        self.assertIn("Hurt enemy Fighter for 400 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 800.", output)
        self.assertIn("Mage has 35 mana remaining.", output)

        # Team A Mage with a Staff acts on opponent fighter again
        file2 = io.StringIO()
        with redirect_stdout(file2):
            m.act(t1, t2)

        output2 = file2.getvalue()
        self.assertEqual(f.health, 400)
        self.assertEqual(m.mana, 20)
        self.assertIn("Hurt enemy Fighter for 400 damage.", output2)
        self.assertIn("Fighter hurt with remaining hp 400.", output2)
        self.assertIn("Mage has 20 mana remaining.", output2)

        # Team A Mage equipped with Staff still has enough mana
        file3 = io.StringIO()
        with redirect_stdout(file3):
            m.act(t1, t2)

        output3 = file3.getvalue()
        self.assertEqual(f.health, 0)
        self.assertEqual(m.mana, 5)
        self.assertIn("Hurt enemy Fighter for 400 damage.", output3)
        self.assertIn("Fighter hurt with remaining hp 0.", output3)
        self.assertIn("Mage has 5 mana remaining.", output3)

    def test_berserker_with_more_than_half_health_on_fighter(self):
        t1 = Team("A")
        t2 = Team("B")

        b,f = Berserker(), Fighter()

        t1.add_villager(b)
        t2.add_villager(f)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            b.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f.health, 1100)
        self.assertIn("Hurt enemy Fighter for 100 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 1100.", output)

    def test_berserker_with_half_health_or_less_on_fighter(self):
        t1 = Team("A")
        t2 = Team("B")

        b,f = Berserker(), Fighter()

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            b.receive_damage(600)
            t1.add_villager(b)
            t2.add_villager(f)
            b.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f.health, 1000)
        self.assertEqual(b.health, 600)
        self.assertIn("Berserker hurt with remaining hp 600.", output)
        self.assertIn("Berserk mode! Attack double!", output)
        self.assertIn("Hurt enemy Fighter for 200 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 1000.", output)

    def test_archmage_acts_with_ally_alive(self):
        t1, t2 = Team("A"), Team("B")

        a,f1,f2, f3 = Archmage(), Fighter(), Fighter(), Fighter()
        t1.add_villager(a)
        t1.add_villager(f1)
        t2.add_villager(f2)
        t2.add_villager(f3)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            a.act(t1, t2)

        output = file.getvalue()
        
        self.assertIn("Hurt enemy Fighter for 400 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 800.", output)


    def test_archmage_acts_with_no_ally_alive(self):
        t1, t2 = Team("A"), Team("B")

        a,f1,f2,f3 = Archmage(), Fighter(), Fighter(), Fighter()
        t1.add_villager(a)
        t1.add_villager(f1)
        t2.add_villager(f2)
        t2.add_villager(f3)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            f1.receive_damage(9999)
            a.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f1.health, 0)
        self.assertEqual(f1.is_alive(), False)
        self.assertIn("Fighter hurt with remaining hp 0.", output)
        self.assertIn("Fighter died!", output)
        self.assertIn("Only one standing. Cast KABOOM! on every enemy alive!", output)
        self.assertEqual(
            output.count("Hurt enemy Fighter for 800 damage."),
            2
        )
        self.assertEqual(
            output.count("Fighter hurt with remaining hp 400."),
            2
        )

    def test_necromancer_acts_with_no_ally_dead(self):
        t1, t2 = Team("A"), Team("B")

        n, f1, f2 = Necromancer(), Fighter(), Fighter()
        t1.add_villager(n)
        t1.add_villager(f1)
        t2.add_villager(f2)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            n.act(t1, t2)

        output = file.getvalue()
        self.assertIn("Hurt enemy Fighter for 400 damage.", output)
        self.assertIn("Fighter hurt with remaining hp 800.", output)

    def test_necromancer_acts_with_no_ally_dead(self):
        t1, t2 = Team("A"), Team("B")

        n, f1, f2, f3 = Necromancer(), Fighter(), Fighter(), Fighter()
        t1.add_villager(n)
        t1.add_villager(f1)
        t2.add_villager(f2)
        t2.add_villager(f3)

        # get the printed output
        file = io.StringIO()
        with redirect_stdout(file):
            f1.receive_damage(9999)
            n.act(t1, t2)

        output = file.getvalue()

        self.assertEqual(f1.health, 600)
        self.assertEqual(f1.is_alive(), True)
        self.assertIn("Fighter hurt with remaining hp 0.", output)
        self.assertIn("Fighter died!", output)
        self.assertIn("Reviving Fighter with 600 hp.", output)




if __name__ == "__main__":
    unittest.main()
