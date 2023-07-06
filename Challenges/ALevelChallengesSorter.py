import os, csv

#stoes the directory of the files in use
challengeDir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Challenges'
inFileDir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Challenges/A level challenges.csv'
outFileDir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Challenges/Temp.csv'

challengeList = os.listdir(challengeDir)
completedChallenges = []
unCompletedChallenges = []

with open(inFileDir, 'r') as challengeFile:
    reader = csv.reader(challengeFile)
    for row in reader:
        challengeCode = row[0]
        challengeScore = row[1]
        challengeName = row[2]
        challengeDescription = row[3]
        challengeComplete = row[4]
        challengeCode = challengeCode+'.py'
        if challengeCode in challengeList:
            completedChallenges.append(challengeCode)
        else:
            unCompletedChallenges.append(challengeCode)

for i in range(len(completedChallenges)):
    completedChallenges[i] = completedChallenges[i][:-3]
for i in range(len(unCompletedChallenges)):
    unCompletedChallenges[i] = unCompletedChallenges[i][:-3]


with open(outFileDir, 'w') as outFile:
    writer = csv.writer(outFile)
    with open(inFileDir, 'r') as challengeFile:
        reader = csv.reader(challengeFile)
        for row in reader:
            if row[0] == 'Code':
                writer.writerow([row[0], row[1], row[2], row[3], 'Completed'])
                continue
            challengeCode = row[0]
            challengeScore = row[1]
            challengeName = row[2]
            challengeDescription = row[3]
            challengeComplete = row[4]
            if challengeCode in completedChallenges:
                writer.writerow([challengeCode, challengeScore, challengeName, challengeDescription, 'True'])
                #print(challengeCode, 'True')
            else:
                writer.writerow([challengeCode, challengeScore, challengeName, challengeDescription, 'False'])
                #print(challengeCode, 'False')

os.remove(inFileDir)
os.rename(outFileDir, inFileDir)               