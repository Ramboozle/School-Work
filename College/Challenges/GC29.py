import random
comments=['Wow!you did a good job','Great detail in this work','Good job with this one!','Good work!','good quality work','you are a special student','this work is mediocre','cool','alright work']
students=int(input("how many students?"))
for i in range(students):
    ran = random.randint(0, 8)
    print(comments[ran])

