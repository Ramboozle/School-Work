import os
monster_collecton = []

class Monster:
    def __init__(self,id,Name,Origin,Description,Attack,Magical_Force,Magical_Defence,Defence,Intelligence,Health):
        self.id = id
        self.Name = Name
        self.Origin = Origin
        self.Description = Description
        self.Attack = Attack
        self.Magical_Force = Magical_Force
        self.Magical_Defence = Magical_Defence
        self.Defence = Defence
        self.Intelligence = Intelligence
        self.Health = Health

    def print_me(self):
        print(self.id, self.Name, self.Origin, self.Description, self.Attack, self.Magical_Force, self.Magical_Defence,
              self.Defence, self.Intelligence, self.Health)

def read_monsters():
        try:
            with open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/Monsters/Monsters class.txt') as f:
                for line in f:
                    parts = line.split(",")
                    id = parts[0]
                    Name = parts [1]
                    Origin = parts [2]
                    Description = parts [3]
                    Attack = parts [4]
                    Magical_Force = parts [5]
                    Magical_Defence = parts [6]
                    Defence = parts [7]
                    Intelligence = parts [8]
                    Health = parts [9]
                    monster_collecton.append(Monster(id,Name,Origin,Description,Attack,Magical_Force,Magical_Defence,Defence, Intelligence,Health))
        except OSError:
            print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())

read_monsters()

print(monster_collecton)
for i in monster_collecton:
    print()