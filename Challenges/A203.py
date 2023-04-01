#A202 Insertion Sort
numbers = []
temp = 0
x = 0

numamount = int(input('how many numbers do you have?'))
for i in range(numamount):
    print('please input number', i+1)
    numin = input() #accepts an input from the user
    numbers.append(numin) #adds the inputted number to the end of the list

#code begins

for i in range(1, len(numbers)):
    temp = numbers[i]
    x = i-1
    while x >= 0 and temp < numbers[x] :
            numbers[x + 1] = numbers[x]
            x -= 1
    numbers[x + 1] = temp
print(numbers)