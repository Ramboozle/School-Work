#TU10
import random
Choose_Name = ["James","John","Mark","Rick"]
for i in range(3):
    chosen = int(random.randint(0,len(Choose_Name)-1))
    name = Choose_Name[chosen]
    print(name)
    keep = input('do you want to keep? y/n')
    if keep == 'n':
        print('removing')
        Choose_Name.remove(name)
    elif keep == 'y':
        print('keeping')
    else:
        print('invalid input')
print(Choose_Name)