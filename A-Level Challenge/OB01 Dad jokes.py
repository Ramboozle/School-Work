import random
dad_jokes = []
dad_answers =[]
dir = '/Users/ramboozle/Library/Mobile Documents/com~apple~CloudDocs/Coding/School Work/Things used for code/DadJokes.txt'

class DadJokes:
    def __init__(self,Prompt,Answer):
        self.__prompt = Prompt
        self.__answer = Answer

    def PrintRandomJoke(self,joke_list,answer_list):
        random_joke = random.choice(joke_list)
        print(random_joke)
        answer = input()
        joke_answer = answer_list[joke_list.index(random_joke)]
        print(joke_answer)

    def constructor(self):
        with open(dir,"r") as f:
            for line in f:
                dad_jokes.append(line)
                dad_answers.append(f.readline())

    def PrintRandomJoke(self):
        random_joke = random.choice(dad_jokes)
        print(random_joke)
        answer = input()
        joke_answer = dad_answers[dad_jokes.index(random_joke)]
        print(joke_answer)

DadJokes.constructor(DadJokes)
DadJokes.PrintRandomJoke(DadJokes)
