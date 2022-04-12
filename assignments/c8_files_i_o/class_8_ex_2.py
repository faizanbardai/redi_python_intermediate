# 1. Create a text file and copy&paste the contents of `story.txt` (it’s in the Google Classroom folder)
# 2. Print the dictionary where keys consist of the words in the text and values are
# how many times a particular word appears in the text
# Hint: string.split() returns a list of words from a string of text

import pathlib
path = pathlib.Path(__file__).parent.resolve() / 'story.txt'

word_dict = {}

with open(path) as file:
    for line in file.readlines():
        # remove /n at the end
        line = line.strip()

        # access individual word by space separator
        words = line.split(' ')

        for word in words:
            # not counting capital words separately
            value = word_dict.get(word.lower())

            # set initial value to 0 if the word is not yet in dictionary
            if (value == None):
                value = 0

            # increment count
            word_dict[word] = value + 1

print(word_dict)
