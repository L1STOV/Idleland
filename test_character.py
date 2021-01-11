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

    def test_dwarf_set_weapon(self):
        self.assertEqual(self.dwain.set_weapon(True, 'Axe'), 'I will beat them all with this axe!')

    def test_dwarf_set_weapon_not_in_list(self):
        self.assertEqual(self.dwain.set_weapon(True, 'Knife'), 'I\'am unable to use this weapon')

    def test_dwarf_set_weapon_not_armed(self):
        self.assertEqual(self.dwain.set_weapon(False, 'Axe'), 'I have never used a weapon')

    def test_dwarf_set_weapon_incorrect_type_first_argument_int(self):
        with self.assertRaises(ValueError):
            self.dwain.set_weapon(30, 'Axe')

    def test_dwarf_set_weapon_incorrect_type_first_argument_float(self):
        with self.assertRaises(ValueError):
            self.dwain.set_weapon(30.2, 'Axe')

    def test_dwarf_set_weapon_incorrect_type_first_argument_str(self):
        with self.assertRaises(ValueError):
            self.dwain.set_weapon('True', 'Axe')

    def test_dwarf_set_weapon_incorrect_type_first_argument_list(self):
        with self.assertRaises(ValueError):
            self.dwain.set_weapon(['False'], 'Axe')

    def test_dwarf_set_weapon_incorrect_type_first_argument_tuple(self):
        with self.assertRaises(ValueError):
            self.dwain.set_weapon(('True', '22'), 'Axe')

    def test_dwarf_set_weapon_incorrect_type_first_argument_dict(self):
        with self.assertRaises(ValueError):
            self.dwain.set_weapon({'statement': False}, 'Axe')

    def test_elf_set_weapon(self):
        self.assertEqual(self.argalas.set_weapon(True, 'Arrow'), 'What a magnificent arrow!')

    def test_elf_set_weapon_not_in_list(self):
        self.assertEqual(self.argalas.set_weapon(True, 'Hammer'), 'I don\'t know how to use this weapon')

    def test_elf_set_weapon_not_armed(self):
        self.assertEqual(self.argalas.set_weapon(False, 'Arrow'), 'Hm, seriously? I don\'t want!')

    def test_elf_set_weapon_incorrect_type_first_argument_int(self):
        with self.assertRaises(ValueError):
            self.argalas.set_weapon(30, 'Arrow')

    def test_elf_set_weapon_incorrect_type_first_argument_float(self):
        with self.assertRaises(ValueError):
            self.argalas.set_weapon(30.2, 'Arrow')

    def test_elf_set_weapon_incorrect_type_first_argument_str(self):
        with self.assertRaises(ValueError):
            self.argalas.set_weapon('True', 'Arrow')

    def test_elf_set_weapon_incorrect_type_first_argument_list(self):
        with self.assertRaises(ValueError):
            self.argalas.set_weapon(['False'], 'Arrow')

    def test_elf_set_weapon_incorrect_type_first_argument_tuple(self):
        with self.assertRaises(ValueError):
            self.argalas.set_weapon(('True', '22'), 'Arrow')

    def test_elf_set_weapon_incorrect_type_first_argument_dict(self):
        with self.assertRaises(ValueError):
            self.argalas.set_weapon({'statement': False}, 'Arrow')

    def test_orc_set_weapon(self):
        self.assertEqual(self.urathun.set_weapon(True, 'Axe'), 'Urgh, my axe gonna crash them all!')

    def test_orc_set_weapon_not_armed(self):
        self.assertEqual(self.urathun.set_weapon(False, 'Axe'), 'Where is my weapon!?')

    def test_orc_set_weapon_not_in_list(self):
        self.assertEqual(self.urathun.set_weapon(True, 'Stones'), 'Ha-ha, what you want me to do with this?')

    def test_orc_set_weapon_incorrect_type_first_argument_int(self):
        with self.assertRaises(ValueError):
            self.urathun.set_weapon(30, 'Arrow')

    def test_orc_set_weapon_incorrect_type_first_argument_float(self):
        with self.assertRaises(ValueError):
            self.urathun.set_weapon(30.2, 'Arrow')

    def test_orc_set_weapon_incorrect_type_first_argument_str(self):
        with self.assertRaises(ValueError):
            self.urathun.set_weapon('True', 'Arrow')

    def test_orc_set_weapon_incorrect_type_first_argument_list(self):
        with self.assertRaises(ValueError):
            self.urathun.set_weapon(['False'], 'Arrow')

    def test_orc_set_weapon_incorrect_type_first_argument_tuple(self):
        with self.assertRaises(ValueError):
            self.urathun.set_weapon(('True', '22'), 'Arrow')

    def test_orc_set_weapon_incorrect_type_first_argument_dict(self):
        with self.assertRaises(ValueError):
            self.urathun.set_weapon({'statement': False}, 'Arrow')

    def test_human_set_weapon(self):
        self.assertEqual(self.anduin.set_weapon(True, 'Sword'), 'Perfect sword i will crash my enemies')

    def test_human_set_weapon_not_armed(self):
        self.assertEqual(self.anduin.set_weapon(False, 'Axe'), 'I\'am so sorry, i\'am unable to use any weapons')

    def test_human_set_weapon_not_in_list(self):
        self.assertEqual(self.anduin.set_weapon(True, 'Stones'), 'Unfortunately, i don\'t know how to use it')

    def test_human_set_weapon_incorrect_type_first_argument_int(self):
        with self.assertRaises(ValueError):
            self.anduin.set_weapon(30, 'Axe')

    def test_human_set_weapon_incorrect_type_first_argument_float(self):
        with self.assertRaises(ValueError):
            self.anduin.set_weapon(30.2, 'Axe')

    def test_human_set_weapon_incorrect_type_first_argument_str(self):
        with self.assertRaises(ValueError):
            self.anduin.set_weapon('True', 'Axe')

    def test_human_set_weapon_incorrect_type_first_argument_list(self):
        with self.assertRaises(ValueError):
            self.anduin.set_weapon(['False'], 'Axe')

    def test_human_set_weapon_incorrect_type_first_argument_tuple(self):
        with self.assertRaises(ValueError):
            self.anduin.set_weapon(('True', '22'), 'Axe')

    def test_human_set_weapon_incorrect_type_first_argument_dict(self):
        with self.assertRaises(ValueError):
            self.anduin.set_weapon({'statement': False}, 'Axe')

    def test_dwarf_set_armor(self):
        self.assertEqual(self.dwain.set_armor(50), '--- Current armor value - 200 points ---')

    def test_dwarf_set_armor_banned_value(self):
        self.assertEqual(self.dwain.set_armor(15), '--- Armor value for dwarfs must be in [25:75] diapason ---')
        self.assertEqual(self.dwain.set_armor(100), '--- Armor value for dwarfs must be in [25:75] diapason ---')

    def test_dwarf_set_armor_argument_type_str(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor('25')

    def test_dwarf_set_armor_argument_type_float(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor(25.5)

    def test_dwarf_set_armor_argument_type_none(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor(None)

    def test_dwarf_set_armor_argument_type_bool(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor(bool)

    def test_dwarf_set_armor_argument_type_list(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor([25])

    def test_dwarf_set_armor_argument_type_tuple(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor((25, 0))

    def test_dwarf_set_armor_argument_type_dict(self):
        with self.assertRaises(ValueError):
            self.dwain.set_armor({'value': 25})

    def test_orc_set_armor(self):
        self.assertEqual(self.urathun.set_armor(50), '--- Current armor value - 200 points ---')

    def test_orc_set_armor_banned_value(self):
        self.assertEqual(self.urathun.set_armor(15), '--- Armor value for orcs must be in [25:75] diapason ---')
        self.assertEqual(self.urathun.set_armor(100), '--- Armor value for orcs must be in [25:75] diapason ---')

    def test_orc_set_armor_argument_type_str(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor('25')

    def test_orc_set_armor_argument_type_float(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor(25.5)

    def test_orc_set_armor_argument_type_none(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor(None)

    def test_orc_set_armor_argument_type_bool(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor(bool)

    def test_orc_set_armor_argument_type_list(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor([25])

    def test_orc_set_armor_argument_type_tuple(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor((25, 0))

    def test_orc_set_armor_argument_type_dict(self):
        with self.assertRaises(ValueError):
            self.urathun.set_armor({'value': 25})

    def test_elf_set_armor(self):
        self.assertEqual(self.argalas.set_armor(50), '--- Current armor value - 150 points ---')

    def test_elf_set_armor_banned_value(self):
        self.assertEqual(self.argalas.set_armor(15), '--- Armor value for elfs must be in [25:50] diapason ---')
        self.assertEqual(self.argalas.set_armor(100), '--- Armor value for elfs must be in [25:50] diapason ---')

    def test_elf_set_armor_argument_type_str(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor('25')

    def test_elf_set_armor_argument_type_float(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor(25.5)

    def test_elf_set_armor_argument_type_none(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor(None)

    def test_elf_set_armor_argument_type_bool(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor(bool)

    def test_elf_set_armor_argument_type_list(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor([25])

    def test_elf_set_armor_argument_type_tuple(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor((25, 0))

    def test_elf_set_armor_argument_type_dict(self):
        with self.assertRaises(ValueError):
            self.argalas.set_armor({'value': 25})

    def test_human_set_armor(self):
        self.assertEqual(self.anduin.set_armor(50), '--- Current armor value - 150 points ---')

    def test_human_set_armor_banned_value(self):
        self.assertEqual(self.anduin.set_armor(15), '--- Armor value for humans must be in [25:50] diapason ---')
        self.assertEqual(self.anduin.set_armor(100), '--- Armor value for humans must be in [25:50] diapason ---')

    def test_human_set_armor_argument_type_str(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor('25')

    def test_human_set_armor_argument_type_float(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor(25.5)

    def test_human_set_armor_argument_type_none(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor(None)

    def test_human_set_armor_argument_type_bool(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor(bool)

    def test_human_set_armor_argument_type_list(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor([25])

    def test_human_set_armor_argument_type_tuple(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor((25, 0))

    def test_human_set_armor_argument_type_dict(self):
        with self.assertRaises(ValueError):
            self.anduin.set_armor({'value': 25})

    def test_kill_character_dwarf(self):
        pass

    def test_kill_character_orc(self):
        pass

    def test_kill_character_elf(self):
        pass

    def test_kill_character_human(self):
        pass


if __name__ == '__main__':
    unittest.main()
