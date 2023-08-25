numin = input('input your numbers -->')
check = int(numin[len(numin)-1])

numbers = []
for i in range(len(numin)-1):
    numbers.append(int(numin[i]))

tempmult = []
for i in range(len(numin)-1):
    tempmult.append(int(numin[i])+1)
    mult = tempmult[::-1]

multout = []
for i in range(len(numbers)):
    multout.append(numbers[i]*mult[i])

addednum = 0
for i in range(len(multout)):
    addednum = multout[i] + addednum

mod11 = addednum%11

mod11 = 11 - mod11

if check == mod11:
    print('The value passes the checksum :)')
else:
    print('The value did not pass the checksum :(')