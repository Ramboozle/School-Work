import random
comments=['you smell','you stink','your teeth arnt straight','your hair is knotty','you are a special student','youre bmi is above everage']
student=(input("whats your name?"))
ran = random.randint(0, 8)
print(student,comments[ran])