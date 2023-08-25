#line 9 and 8 must be changed to the directory you wish to store the files.
#leaving them as 'Math Program Output.txt' and 'Math Program Input.txt' respectivly will also work :)
import random
numbers = []
sortednum = []
exiting = 0
programinfo = 'Welcome to my program, heres what it can do!\n1. Clear output file\n2. Load data from file and solve in console (Syntax!)\n3. Generate random numbers in console\n4. Generate random numbers and store in output file\n5. EXIT\nPlease input the number your number'
WDir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/Math Program/Math Program Output.txt'
RDir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/Math Program/Math Program Input.txt'
def numinput(numlen):
    gennumbers = []
    for i in range(numlen):
        numin = random.randint(1,100)
        gennumbers.append(numin)
    return(gennumbers)
def Bub_sort(numbers):
    templist = numbers
    numlen = len(templist)
    sorted = 0
    pos = 0
    sorts = 0
    while sorted == 0:
        for x in range(numlen-1):
            for i in range(numlen-1):
                temp1 = templist[pos]
                temp2 = templist[pos+1]
                if temp1 > temp2:
                    temptemp = temp1
                    temp1 = temp2
                    temp2 = temptemp
                    templist[pos] = temp1
                    templist[pos+1] = temp2
                pos = pos+1
                sorts = sorts+1
            pos = 0
        sorted = 1
    return(numbers)
def SConvert(inputdat):
    tempstr = '['
    for i in range(len(inputdat)-1):
        tempstr = tempstr + str(inputdat[i]) + ','
    tempstr = tempstr + str(inputdat[i+1])
    tempstr = tempstr + ']'
    return(tempstr)
def FileWrite(numbers):
    temp = SConvert(numbers)
    with open(WDir, 'a') as file:
        line ='Question ' + temp
        file.writelines([line,'\n'])
    file.close()
def FileClear():
    with open(WDir, 'w') as file:
        file.writelines('')
    print('File is cleared!')
    file.close()
def FileRLines():
    lines = 0
    with open(RDir,'rt') as file:
        for line in file:
            lines = lines + 1
    return(lines)
    file.close()
def FileRGrabber(Line):
    with open(RDir, 'rt') as file:
        reader = file.readlines()
        return(reader[Line])
def Str_List(Input):
    SynIn = Input.split()
    syninsplit = SynIn[1]
    temp = syninsplit.strip('][').split(',')
    return(temp)
def quicksort(Input):
    length = len(Input)
    if length <= 1:
        return Input
    pivot = Input.pop()
    greater = []
    less = []
    for number in Input:
        if number > pivot:
            greater.append(number)
        else:
            less.append(number)
    return(quicksort(less)+[pivot]+quicksort((greater)))
print(quicksort([1,5,7,8,4,3,6,8,9,5,4,2,6,8,9]))

#~~~~~~~~~~Main Code~~~~~~~~~~#
print(programinfo)
while exiting != 1:
    userinput = int(input())
    if userinput in [1,2,3,4,5]:
        if userinput !=5:
            if userinput == 1:
                FileClear()
            elif userinput == 2:
                for i in range(FileRLines()-1):
                    print(Bub_sort(Str_List(FileRGrabber(i))))
            elif userinput == 3:
                length = int(input('How many numbers long should your strings be?'))
                quant = int(input('And how many do you want to generate?'))
                for i in range(quant):
                    temp = numinput(length)
                    print(temp)
            elif userinput == 4:
                length = int(input('How many numbers long should your strings be?'))
                quant = int(input('And how many do you want to generate?'))
                for i in range(quant):
                    temp = numinput(length)
                    FileWrite(temp)
                print('File should be written')
            print(programinfo)
        else:
            exiting = 1
    else:
        print('Invalid input. Remember to just use numbers by themselves :)')