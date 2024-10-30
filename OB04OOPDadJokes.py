from random import choice


class DadJokes():
   def __init__(self):
       self.__prompt = "" # string
       self.__answer = "" # string


   def setter(self, prompt, answer):
       self.__prompt = prompt
       self.__answer = answer


   def get_prompt(self):
       return self.__prompt


   def get_answer(self):
       return self.__answer


TheGreatListOfDadJokes = []


def Constructor():
   try:
       with open("DadJokes.txt") as f:
           for line in f:
               TheGreatListOfDadJokes.append(DadJokes())
               TheGreatListOfDadJokes[-1].setter(line, next(f))


   except OSError:
       print(f"ERROR 404 File Not Found")


def PrintRandomJoke():
   RandomChoice = choice(TheGreatListOfDadJokes)
   answer = input(RandomChoice.get_prompt())


   print(RandomChoice.get_answer())
