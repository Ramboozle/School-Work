import random
list = ['word','longword','longerword']
hiddenword = []

def Str_List(Input):
    temp = []
    temp[:0] = Input
    return(temp)

rannum = random.randint(0,len(list)-1)
wordselected = list[rannum]
word = Str_List(wordselected)

for i in range(len(word)):
    hiddenword.append('_')
print('you have 10 guesses to guess the word im thinking')
fail = 0
g = 2

while g != 0:
    letterguess = input("Guess a letter")
    if letterguess in word:
        for i in range(len(word)):
            tempcount = 0
            if letterguess == word[i]:
                hiddenword[i] = word[i]
                tempcount = tempcount + 1
            if tempcount != 0:
                g = g + 1
        print(hiddenword)
        print(g)
    else:
        print('try again')
    if word == hiddenword:
        print('you win')
        break
    g = g - 1
print('you loose :(')
