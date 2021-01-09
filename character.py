class Character:
    def __init__(self, name, health, armor, force):
        self.name = name
        self.health = health
        self.armor = armor
        self.force = force


class Dwarf(Character):
    pass


class Orc(Character):
    pass


class Elf(Character):
    pass


class Human(Character):
    pass
