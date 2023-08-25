import os
dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/TreasureChestData.txt'
arrayTreasure = []

class TreasureChest:
    def __init__(self, question, answer, points):
        self.question = question
        self.answer = answer
        self.points = points

    def getQuestion(self):
        return self.question

    def checkAnswer(self):
        return self.answer

def readData():
    try:
        with open(dir,'r') as f:
            line_num = len(f.readlines()) #counts lines
            f.seek(0) #puts the seek back to the start ( the seek is like a cursor)
            for line in range(line_num//3):
                q = f.readline().strip()
                a = f.readline().strip()
                p = f.readline().strip()
                #print(q,a,p)
                arrayTreasure.append(TreasureChest(q, a, p))


    except OSError:
        print("couldn't find file")

readData()

#3B
arrayTreasure[0].getQuestion()

#3Ci
while input() ==
arrayTreasure[0].checkAnswer()