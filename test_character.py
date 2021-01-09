import unittest
from character import Dwarf, Elf, Orc, Human


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.dwain = Dwarf('Dwain', 100, 150, 100, 1500)
        self.argalas = Elf('Argalas', 100, 100, 100, 2000)
        self.urathun = Orc('Urathun', 100, 150, 125)
        self.anduin = Human('Anduin', 100, 100, 90, 1250)

    def test_dwarf_greetings(self):
        self.assertEqual(self.dwain.greetings(), 'Ho-ho, my name is Dwain. What are you staring at?')

    def test_elf_greetings(self):
        self.assertEqual(self.argalas.greetings(), 'Nae saian luume, my name is Argalas. I'
                                                   ' was expecting to see someone bigger')

    def test_orc_greetings(self):
        self.assertEqual(self.urathun.greetings(), 'Bir ti gi dym, Urathun will kill you!')

    def test_human_greetings(self):
        self.assertEqual(self.anduin.greetings(), 'Greetings, my name is Anduin. How are you?')


if __name__ == '__main__':
    unittest.main()