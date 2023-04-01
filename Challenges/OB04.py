catarray = []
dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/CutestCats.txt'
class cats:
    def __init__(self,name,description,weight,length,lifeexpectancy,imageurl):
        self.__name = name
        self.__description = description
        self.__weight = weight
        self.__length = length
        self.__lifeexpectancy = lifeexpectancy
        self.__imageurl = imageurl

    def GetCatDetails(self):
        return self.__name,self.__description,self.__weight,self.__length,self.__lifeexpectancy,self.__imageurl

    def GetCatLife(self):
        return self.__name, self.__lifeexpectancy

with open (dir,"r") as file:
    Lines = int(len(file.readlines())/7)
    file.seek(0)
    for i in range(5):
        name = file.readline().strip()
        description = file.readline().strip()
        w = file.readline().strip()
        weightarray=[int(s) for s in str.split(w) if s.isdigit()]
        if len(weightarray) < 3:
            weight = (weightarray[1]+weightarray[0])/2
        else:
            weight = (weightarray[2]+weightarray[1]+weightarray[0])/3
        l = file.readline().strip()
        lengtharray = [int(s) for s in str.split(l) if s.isdigit()]
        if len(lengtharray) ==0:
            length = (18*2.54)
        if len(lengtharray) ==1:
            length = (lengtharray[0]*30.48)
        if len(lengtharray) ==2:
            length = (((lengtharray[1]+lengtharray[0])/2)*2.54)
        cnc = file.readline().strip()
        lfe = file.readline().strip()
        lifearray = [int(s) for s in str.split(lfe) if s.isdigit()]
        lifeexpectancy = (lifearray[1]+lifearray[0])/2
        imageurl = file.readline().strip()
        catarray.append(cats(name,description,weight,length,lifeexpectancy,imageurl))
for i in range(0,5):
    print(catarray[i].GetCatDetails())
for i in range(0,5):
    print(catarray[i].GetCatLife())