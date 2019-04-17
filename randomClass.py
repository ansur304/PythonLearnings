import random


def roll():
    print(random.randint(1, 6), random.randint(1, 6))


def execute_random():
    num = int(input("How many times you want to roll ? ::"))
    i = 0
    while i < num:
        roll()
        num -= 1