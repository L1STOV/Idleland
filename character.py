class Character:
    def __init__(self, name, health, armor, force):
        self.name = name
        self.health = health
        self.armor = armor
        self.force = force


class Dwarf(Character):

    amount_of_dwarfs = 0

    def __init__(self, name, health, armor, force):
        super().__init__(name, health, armor, force)
        Dwarf.amount_of_dwarfs += 1


class Orc(Character):

    amount_of_orcs = 0

    def __init__(self, name, health, armor, force):
        super().__init__(name, health, armor, force)
        Orc.amount_of_orcs += 1


class Elf(Character):

    amount_of_elfs = 0

    def __init__(self, name, health, armor, force):
        super().__init__(name, health, armor, force)
        Elf.amount_of_elfs += 1


class Human(Character):

    amount_of_humans = 0

    def __init__(self, name, health, armor, force):
        super().__init__(name, health, armor, force)
        Human.amount_of_humans += 1
        