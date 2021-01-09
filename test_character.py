import unittest
from character import Dwarf, Elf, Orc, Human


class TestCharacter(unittest.TestCase):
    def setUp(self):
        dwain = Dwarf('Dwain', 100, 150, 100, 1500)
        argalas = Elf('Argalas', 100, 100, 100, 2000)
        urathun = Orc('Urathun', 100, 150, 125)
        anduin = Human('Anduin', 100, 100, 90, 1250)

    def test_dwarf_greetings(self):
        pass

    def test_elf_greetings(self):
        pass

    def test_orc_greetings(self):
        pass

    def test_human_greetings(self):
        pass

