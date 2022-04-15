"""
Topics: built in methods, lists, sets.
"""


def first_item_equals_last_item(l):
    """
    a) Write a function that takes a list of integers and returns True if the first and last number are equal and False otherwise.
    Example: first_last_equal([1,2,3,2,1]) should return True
    """
    return l[0] == l[-1]


def get_even_indexed_chars(s: str) -> str:
    """
    b) Write a function that...
    - takes a string as input
    - picks only the characters at every even position (e.g. the 0th, 2nd, 4th, ... character)
    - returns the selected characters as a string
    """
    return s[::2]


def remove_chars(s, n):
    """
    c) Write a function that takes a string and a number n. It should remove n characters from a string starting from zero up to n and return the new string.
    Example: remove_chars("python", 2) should return "thon"
    """
    return s[n:]


def one_in_common(s1, s2):
    """
    d) Write a function that takes in two sets and
    returns True if they have at least one element in common
    and False otherwise.
    """
    return len(s1.intersection(s2)) > 0


def is_palindrome_number(n):
    """
    e) Write a function that takes a number and returns True if it is a palindrome number,
    otherwise it returns False. A palindrome number is a number that is same after reverse.
    """
    return str(n) == str(n)[::-1]
