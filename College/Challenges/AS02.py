#AS02 Linear search
import random
list = []
tempcount = 0
found = 0
tempnum = 0
length = int(input('how long is the list'))
for i in range(length):
    list.append(random.randint(0,999))
target = int(input('what are you looking for in the list?'))
print(list)
print(target)
for i in range(len(list)):
    tempnum = list[i]
    if tempnum == target:
        found = 1
    print(tempnum)
if found == 1:
    print('number was found :)')
else:
    print('number was not found :(')