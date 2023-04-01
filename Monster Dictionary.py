import csv # imports the CVS library
dictionary = {} #creates an empty dictionary 
filein = open('/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Python/School Work/Things used for code/Monsters.csv','r') #opens the CSV file in read mode
reader = csv.reader(filein) #creates an object that will read every line for the loop  
for row in reader: #repeats the code below for the amount of rows (845 times in this case)
    dictionary[row[0]] = row[1] #stores whatever is in row 0 and 1 in the dictionary respecitivly
userin = input('please input the id of the beast you wish to look up') #takes an input from the user as to the id to lookup
print(dictionary[userin]) #prints the dictinary item in question 
