# import the following function into your progarm
def shift_letter(original_letter, step):
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
