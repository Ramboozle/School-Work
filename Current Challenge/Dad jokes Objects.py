import random
dad_jokes = []

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

