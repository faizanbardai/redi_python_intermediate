"""
Topics: files, modules, testing.

a) Write a program that will do the following:
    1. import the shift_letter function from shift_module.
    2. Open the secret_message.txt file and save all of its content in a string variable.
    3. Implement the function "caesar_encrypt(original_text, step)" that will take a string as input and return (not print!) the string with all letters shifted by [step] places.
    4. Use your caesar_encrypt(original_text, step) function to decrypt your friends message and write the result in a new file, „decrypted_message.txt", using the file handling from previous lessons. Tipp: your friends favorite number is 5!

"""
# TODO: 1. import the shift_letter function from shift_module.
from .shift_module import shift_letter


def caesar_encrypt(original_text: str, step: int) -> str:
    """
    TODO: 3. Implement the function "caesar_encrypt(original_text, step)"
     that will take a string as input and return (not print!)
     the string with all letters shifted by [step] places.
    """
    pass


def decypher_file(input_file_path: str, output_file_path: str) -> None:
    # TODO: 2. Open the secret_message.txt file
    #  and save all of its content in a string variable.
    pass

    # TODO 4. Use your caesar_encrypt(original_text, step) function
    #  to decrypt your friends message and write the result in a new file,
    #  „decrypted_message.txt", using the file handling from previous lessons.
    #  Tipp: your friends favorite number is 5!
    pass
