# In your code, create a Dictionary that contains 3 secret words as keys. Use anything as values.
secret_words = {'Avada Kedavra': 'The Killing Curse',
                'Crucio': 'The Cruciatus Curse', 'Imperio': 'The Imperius Curse'}


# Ask the user to input the any word.
user_word = input('Enter a word: ')

# If the word works as a key for the dictionary, print the key and the value
# If the word does NOT work as a key for the dictionary, catch the resulting exception and
# inform the user about the error using a print or logging statement
# Important: Don’t use if clauses. Try to access the dictionary by key and handle the error.


try:
    print(f'{user_word}: {secret_words[user_word]}')
except KeyError:
    print('This word is not part of my secret dictionary :)')
