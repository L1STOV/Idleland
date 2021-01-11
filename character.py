class Character:
    def __init__(self, name, health, armor, force):
        self.name = name
        self.health = health
        self.armor = armor
        self.force = force

    def greetings(self):
        raise NotImplementedError

    def talk_to(self):
        raise NotImplementedError

    def set_weapon(self, isArmed, weapon):
        raise NotImplementedError

    def set_armor(self, added_armor_points):
        raise NotImplementedError

    def wear_shield(self, shield_armor_points):
        raise NotImplementedError

    def kill_character(self, character):
        raise NotImplementedError

    def use_force_potion(self):
        raise NotImplementedError

    def battle_roar(self):
        raise NotImplementedError


class Dwarf(Character):

    amount_of_dwarfs = 0

    def __init__(self, name, health, armor, force, money):
        super().__init__(name, health, armor, force)
        self.money = money
        Dwarf.amount_of_dwarfs += 1

    def greetings(self):
        return f'Ho-ho, my name is {self.name}. What are you staring at?'

    def talk_to(self):
        pass

    def set_weapon(self, isArmed, weapon):
        weapons_list = ['Axe', 'Hammer', 'Sword', 'Rifle', 'Spear']
        if not isinstance(isArmed, bool):
            raise ValueError
        if not isinstance(weapon, str):
            raise ValueError
        if isArmed:
            if weapon in weapons_list:
                return f'I will beat them all with this {weapon.lower()}!'
            else:
                return f'I\'am unable to use this weapon'
        else:
            return f'I have never used a weapon'

    def set_armor(self, added_armor_points):
        if not isinstance(added_armor_points, int):
            raise ValueError
        if 25 <= added_armor_points <= 75:
            self.armor += added_armor_points
            return f'--- Current armor value - {self.armor} points ---'
        else:
            return '--- Armor value for dwarfs must be in [25:75] diapason ---'

    def wear_shield(self, shield_armor_points):
        pass

    def kill_character(self, character):
        pass

    def use_force_potion(self):
        pass

    def battle_roar(self):
        pass


class Orc(Character):

    amount_of_orcs = 0

    def __init__(self, name, health, armor, force):
        super().__init__(name, health, armor, force)
        Orc.amount_of_orcs += 1

    def greetings(self):
        return f'Bir ti gi dym, {self.name} will kill you!'

    def talk_to(self):
        pass

    def set_weapon(self, isArmed, weapon):
        weapons_list = ['Axe', 'Hammer', 'Sword', 'Arrow', 'Spear']
        if not isinstance(isArmed, bool):
            raise ValueError
        if not isinstance(weapon, str):
            raise ValueError
        if isArmed:
            if weapon in weapons_list:
                return f'Urgh, my {weapon.lower()} gonna crash them all!'
            else:
                return f'Ha-ha, what you want me to do with this?'
        else:
            return f'Where is my weapon!?'

    def set_armor(self, added_armor_points):
        if not isinstance(added_armor_points, int):
            raise ValueError
        if 25 <= added_armor_points <= 75:
            self.armor += added_armor_points
            return f'--- Current armor value - {self.armor} points ---'
        else:
            return '--- Armor value for orcs must be in [25:75] diapason ---'

    def wear_shield(self, shield_armor_points):
        pass

    def kill_character(self, character):
        pass

    def use_force_potion(self):
        pass

    def battle_roar(self):
        pass


class Elf(Character):

    amount_of_elfs = 0

    def __init__(self, name, health, armor, force, money):
        super().__init__(name, health, armor, force)
        self.money = money
        Elf.amount_of_elfs += 1

    def greetings(self):
        return f'Nae saian luume, my name is {self.name}. I was expecting to see someone bigger'

    def talk_to(self):
        pass

    def set_weapon(self, isArmed, weapon):
        weapons_list = ['Sword', 'Arrow', 'Knife']
        if not isinstance(isArmed, bool):
            raise ValueError
        if not isinstance(weapon, str):
            raise ValueError
        if isArmed:
            if weapon in weapons_list:
                return f'What a magnificent {weapon.lower()}!'
            else:
                return f'I don\'t know how to use this weapon'
        else:
            return f'Hm, seriously? I don\'t want!'

    def set_armor(self, added_armor_points):
        if not isinstance(added_armor_points, int):
            raise ValueError
        if 25 <= added_armor_points <= 50:
            self.armor += added_armor_points
            return f'--- Current armor value - {self.armor} points ---'
        else:
            return '--- Armor value for elfs must be in [25:50] diapason ---'

    def wear_shield(self, shield_armor_points):
        pass

    def kill_character(self, character):
        pass

    def use_force_potion(self):
        pass

    def battle_roar(self):
        pass


class Human(Character):

    amount_of_humans = 0

    def __init__(self, name, health, armor, force, money):
        super().__init__(name, health, armor, force)
        self.money = money
        Human.amount_of_humans += 1

    def greetings(self):
        return f'Greetings, my name is {self.name}. How are you?'

    def talk_to(self):
        pass

    def set_weapon(self, isArmed, weapon):
        weapons_list = ['Sword', 'Arrow', 'Knife', 'Axe', 'Spear']
        if not isinstance(isArmed, bool):
            raise ValueError
        if not isinstance(weapon, str):
            raise ValueError
        if isArmed:
            if weapon in weapons_list:
                return f'Perfect {weapon.lower()} i will crash my enemies'
            else:
                return f'Unfortunately, i don\'t know how to use it'
        else:
            return f'I\'am so sorry, i\'am unable to use any weapons'

    def set_armor(self, added_armor_points):
        if not isinstance(added_armor_points, int):
            raise ValueError
        if 25 <= added_armor_points <= 50:
            self.armor += added_armor_points
            return f'--- Current armor value - {self.armor} points ---'
        else:
            return '--- Armor value for humans must be in [25:50] diapason ---'

    def wear_shield(self, shield_armor_points):
        pass

    def kill_character(self, character):
        pass

    def use_force_potion(self):
        pass

    def battle_roar(self):
        pass


if __name__ == '__main__':
    pass
