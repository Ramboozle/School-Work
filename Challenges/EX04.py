Morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....',
         'i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.',
         'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
         'y':'-.--','z':'--..',' ':'/'}
Txt = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h',
         '..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p',
         '--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
         '-.--':'y','--..':'z','/':' '}
output = []
def txt_mor():
    userin = input('Input String -->')
    for i in range(len(userin)):
        output.append(Morse[userin[i].lower()])
    print(' '.join(output))
def mor_txt():
    userinput = input('Input Morse with spaces in between and "/" for a space -->')
    userin = userinput.split(' ')
    for i in range(len(userin)):
        output.append(Txt[userin[i]])
    print(''.join(output))
print('Welcome to my morse code translator! What would you like to do? \n1. Convert Morse code to Text \n2. Convert Text to Morse code')
userin = int(input())
if userin == 1:
    mor_txt()
elif userin == 2:
    txt_mor()
else:
    print('invalid input')