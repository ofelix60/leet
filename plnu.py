# Program to generate a random number between 0 and 9

# importing the random module
import random
from functools import reduce


def rand():
    return random.randint(0, 9999999999)


def roll(dice, number_of_dice):
    acc = [[], 0]
    for i in range(number_of_dice):
        acc[0].append((rand() % dice) + 1)
    acc[1] = reduce(lambda a, b: a + b, acc[0])
    return acc


print(roll(6, 2))
