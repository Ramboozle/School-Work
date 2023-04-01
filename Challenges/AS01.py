numbers = []
sorted = 0
temp1 = 0
temp2 = 0
temptemp = 0
pos = 0
sorts = 0
numamount = int(input('how many numbers do you have?'))
for i in range(numamount):
    print('please input number', i+1)
    numin = input() #accepts an input from the user
    numbers.append(numin) #adds the inputted number to the end of the list
#print(numbers)
#start of actual code
while sorted == 0:
    for x in range(numamount-1):
        for i in range(numamount-1):
            #print('pos',pos)
            temp1 = numbers[pos]
            temp2 = numbers[pos+1]
            #print('temp 1 & 2: ',temp1,temp2)
            if temp1 > temp2:
                temptemp = temp1
                temp1 = temp2
                temp2 = temptemp
                #print(temp1,temp2,temptemp)
                numbers[pos] = temp1
                numbers[pos+1] = temp2
            pos = pos+1
            sorts = sorts+1
        pos = 0
    sorted = 1
    print('numbers after sort',numbers,'in ',sorts,'sorts')
