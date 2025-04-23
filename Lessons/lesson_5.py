
from random import randint as generate_number, choice
from utils.calculator import *
from utils.templates import Person
from termcolor import cprint
from decouple import config
print(choice(["one", "two", "three"]))
print(generate_number(5, 15))
print(multiplication(7, 2))

my_friend = Person('Jane', 25)
print(my_friend)
cprint("Hello, World!", "yellow", "on_red")

#
# print(config('DATABASE_URL'))
# commented = config('COMMENTED', default=0, cast=int)
# print(commented * 2)
