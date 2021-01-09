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


class Dwarf(Character):

    amount_of_dwarfs = 0

    def __init__(self, name, health, armor, force, money):
        super().__init__(name, health, armor, force)
        self.money = money
        Dwarf.amount_of_dwarfs += 1

    def greetings(self):
        pass

    def talk_to(self):
        pass


class Orc(Character):

    amount_of_orcs = 0

    def __init__(self, name, health, armor, force):
        super().__init__(name, health, armor, force)
        Orc.amount_of_orcs += 1

    def greetings(self):
        pass

    def talk_to(self):
        pass


class Elf(Character):

    amount_of_elfs = 0

    def __init__(self, name, health, armor, force, money):
        super().__init__(name, health, armor, force)
        self.money = money
        Elf.amount_of_elfs += 1

    def greetings(self):
        pass

    def talk_to(self):
        pass


class Human(Character):

    amount_of_humans = 0

    def __init__(self, name, health, armor, force, money):
        super().__init__(name, health, armor, force)
        self.money = money
        Human.amount_of_humans += 1

    def greetings(self):
        pass

    def talk_to(self):
        pass
