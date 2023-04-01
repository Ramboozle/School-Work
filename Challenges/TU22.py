import datetime
FOX = 'the lazy fox jumped over the brown dog'
print('type out "',FOX,'"',"then press enter as soon as youre done") #prints whats in the FOX variable
start = datetime.datetime.now()  # Starts the timer
userin = input()
timer = datetime.datetime.now() - start #caluclates the time it took to write the sentence
if userin == FOX: #checks if it matches the original sentence
    print('you typed it correctly in',timer)
else:
    print("you diddn't quite type it right but you did it in", timer)