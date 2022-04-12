import pathlib
import csv

de_en_dict = dict()
en_de_dict = dict()

path = pathlib.Path(__file__).parent.resolve() / 'pokemon.csv'


def init_translation_dictionaries():
    if len(de_en_dict) != 0 or len(en_de_dict) != 0:
        print("Dictionaries already initialized.")
        return

    with open(path, 'r') as pokemon_file:
        csv_reader = csv.reader(pokemon_file)
        for row in csv_reader:
            de_en_dict[row[1]] = row[2]
            en_de_dict[row[2]] = row[1]


def pokemon_to_english(german_name):
    return en_de_dict.get(german_name.capitalize())
    # return ""


def pokemon_to_german(english_name):
    return de_en_dict.get(english_name.capitalize())
    # return ""


init_translation_dictionaries()


if __name__ == '__main__':
    print("Hello, I'm the poke_ubersetzung module.")
