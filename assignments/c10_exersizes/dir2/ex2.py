"""
Topics: i/o, loops, exceptions

PLEASE OBSERVE THE FOLLOWING THINGS TO MAKE THE TESTS WORK
- use "import random" and "random.randint(a,b)" instead of "from random import randint"
- use print instead of logging
- use "bigger", "smaller" and "congratulations" in your print statements (plus more words)
"""
import random


class NotAnIntegerError(Exception):
    pass


class EmptyRangeError(Exception):
    pass


def number_guessing_game():
    """
    In this exercise, you will program a simple game. The goal of the game is to guess a randomly generated number.
    First, the user is asked to give a range for the random number (two integers):
        - First, a lower bound
        - Secondly, an upper bound
    Then, the program will randomly generate an integer number within that range and ask the user to guess that number.

    Each time the user inputs a number, the program prints whether that number was "bigger" or
    "smaller" than the secret (random) number. The user can guess as many times as he or she wants. If the user input is equal
    to the random number, the program will print "Congratulations!" and terminate.

    Also, the program should deal with the following "problematic" input using TRY/EXCEPT (not with IF/ELSE!!!):
    - Given an input which cannot be converted to a integer,
        try to convert it anyhow, catch the resulting exception and raise a "NotAnIntegerError".
    - When the upper bound is lower than the lower bound, random.randint will throw a ValueError.
        Catch it and throw an "EmptyRangeError" instead.

    Tip: random.randint(a, b) will return a random integer n such that a <= n <= b.
    """
    pass
