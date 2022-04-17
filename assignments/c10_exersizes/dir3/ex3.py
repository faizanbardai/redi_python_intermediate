"""
Topics: files, modules, testing.

a) Write a program that will do the following:
    1. import the shift_letter function from shift_module.
    2. Open the secret_message.txt file and save all of its content in a string variable.
    3. Implement the function "caesar_encrypt(original_text, step)" that will take a string as input and return (not print!) the string with all letters shifted by [step] places.
    4. Use your caesar_encrypt(original_text, step) function to decrypt your friends message and write the result in a new file, „decrypted_message.txt", using the file handling from previous lessons. Tipp: your friends favorite number is 5!

"""
from .shift_module import shift_letter
import pathlib


def caesar_encrypt(original_text: str, step: int) -> str:
    """
     Implement the function "caesar_encrypt(original_text, step)"
     that will take a string as input and return (not print!)
     the string with all letters shifted by [step] places.
    """

    return ''.join([shift_letter(x, step) for x in original_text])


def decypher_file(input_file_path: str, output_file_path: str) -> None:
    #  2. Open the secret_message.txt file
    #  and save all of its content in a string variable.
    secret_message_file = pathlib.Path(
        __file__).parent.resolve() / input_file_path

    with open(secret_message_file, 'r') as secret_message:
        decrypt_message_txt = caesar_encrypt(secret_message.read(), 5)

    #  4. Use your caesar_encrypt(original_text, step) function
    #  to decrypt your friends message and write the result in a new file,
    #  „decrypted_message.txt", using the file handling from previous lessons.
    #  Tipp: your friends favorite number is 5!
    decrypt_message_file = pathlib.Path(
        __file__).parent.resolve() / output_file_path

    with open(decrypt_message_file, 'w') as decrypt_message:
        decrypt_message.write(decrypt_message_txt)


decypher_file('secret_message.txt', 'output.txt')
