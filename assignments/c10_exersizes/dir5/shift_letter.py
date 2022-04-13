"""
DO NOT MODIFY THIS FILE!

INSTEAD, IMPLEMENT THE TESTS IN "TEST_SHIFT_LETTER"!
"""


def shift_letter_correct(original_letter, step):
    uppercase_letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    lowercase_letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    if original_letter in lowercase_letters:
        new_index = (lowercase_letters.index(original_letter) + step) % 26
        return lowercase_letters[new_index]
    elif original_letter in uppercase_letters:
        new_index = (uppercase_letters.index(original_letter) + step) % 26
        return uppercase_letters[new_index]
    else:
        return original_letter


def shift_letter_wrong1(letter, step):
    unicode_code_index = ord(letter)
    return chr(unicode_code_index + step)


def shift_letter_wrong2(original_letter, step):
    uppercase_letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "W",
        "X",
        "Y",
        "Z",
    ]
    lowercase_letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "w",
        "x",
        "y",
        "z",
    ]
    if original_letter in lowercase_letters:
        new_index = (lowercase_letters.index(original_letter) + step) % 26
        return lowercase_letters[new_index]
    elif original_letter in uppercase_letters:
        new_index = (uppercase_letters.index(original_letter) + step) % 26
        return uppercase_letters[new_index]
    else:
        return original_letter


def shift_letter_wrong3(original_letter: str, step: int):
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    index = letters.index(original_letter.lower())
    new_index = (index + step) % 26
    return letters[new_index]
