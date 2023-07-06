#will pick a random challange that hasent been completed before and will print it in console to be completed 
#241 challenges on list
import random, csv

dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Challenges/A level challenges.csv'

with open(dir, 'r') as f:
    reader = csv.reader(f)
    randomNum = random.randint(1, 241)
    lineNum = 0
    for row in reader:
        lineNum = lineNum + 1
        if lineNum == randomNum and row[4] == 'False':
            print(row[0],row[2],row[3])
            exit()