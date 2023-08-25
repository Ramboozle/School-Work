word = input('Input your word to be translated into Rövarspråket')
length = len(word)
i = 0
counter = 0
output = []
for i in range(length):
    temp = word[i]
    #print(temp)
    if temp == ' ':
        output.append(temp)
    elif temp in ['a','e','i','o','u','A','E','I','O','U']:
        #print('vowel')
        output.append(temp)
        #print(counter,output)
    else:
        output.append(temp)
        output.append('o')
        output.append(temp)
        #print('not vowel')
counter = 0
#print(output)
print('youre Rövarspråket translation is:')
for lengthans in range(len(output)):
    print(output[counter], end='')
    counter = counter + 1