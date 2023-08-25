dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/wrexham.txt'
class Wrexham:
    def __init__(self,playername,forename,surname,position,injured,communityinvolvement):
        self.__PlayerNumber = playername
        self.__Forename = forename
        self.__Surname = surname
        self.__Position = position
        self.__CommunityInvolvement = communityinvolvement
        self.__Injured = injured

    def GetPlayerInfo(self):
        return self.__PlayerNumber,self.__Position

    def CommunityInvolvement(self):
        return self.__CommunityInvolvement

    def ChangeInjured(self):
        if self.__injured == True:
            self.__injured = False
        else:
            self.__injured = True

Team = []
with open (dir,"r") as file:
    Lines = int(len(file.readlines())/6)
    file.seek(0)
    for i in range(Lines):
        playername = file.readline().strip()
        forename = file.readline().strip()
        surname = file.readline().strip()
        position = file.readline().strip()
        injured = file.readline().strip()
        communityinvolvement = file.readline().strip()
        Team.append(Wrexham(playername,forename,surname,position,injured,communityinvolvement))

for i in range(len(Team)):
    print(Team[i].GetPlayerInfo())