import random as rn
class character:
    def __init__(self):
        self.name = ''
        self.attack = rn.randint(0,50)
        self.defence = rn.randint(0,50)
        self.health = rn.randint(0,50)
        self.experience = rn.randint(0,50)
    def print_basics(self):
        print('name: ',self.name)
        print('attack ',self.attack)
        print('defence: ',self.defence)
        print('health: ',self.health)
        print('experience: ',self.experience)

oliver = character()
oliver.name = 'Oliver'
oliver.health = 2
oliver.print_basics()

katie = character()
katie.name = 'Katie'
katie.health = 1
katie.print_basics()

class wizard(character):
    def __init__(self):
        character.__init__(self)
        self.magic = rn.randint(0,50)
    def print_me(self):
        self.print_basics()
        print('magic: ',self.magic)

merlin = wizard()
merlin.name = 'Merlin'
merlin.print_me()

class knight(character):
    def __init__(self):
        character.__init__(self)
        self.armour = rn.randint(0,50)
    def print_me(self):
        self.print_basics()
        print('armour: ',self.armour)

arthor = knight()
arthor.name = 'Arthor'
arthor.print_me