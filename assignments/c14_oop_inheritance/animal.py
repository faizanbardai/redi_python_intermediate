class Animal:
    def __init__(self, name, category, age) -> None:
        self.name = name
        self.category = category
        self.age = age

    def print(self) -> None:
        print(self._get_message())

    def _get_message(self):
        return f"{self.name} is a {self.age} year old {self.category}"


class Mammal(Animal):
    def __init__(self, name, category, age, number_of_legs) -> None:
        super().__init__(name, category, age)
        self.number_of_legs = number_of_legs


class Bird(Animal):
    def __init__(self, name, category, age, number_of_legs) -> None:
        super().__init__(name,  category, age)
        self.number_of_legs = number_of_legs


class Fish(Animal):
    def __init__(self, name, category, age,  number_of_fins) -> None:
        super().__init__(name, category, age, )
        self.number_of_fins = number_of_fins


def count_legs(animal_list):
    leg_count = 0
    for animal in animal_list:
        # use instance check (this is better)
        if isinstance(animal, Mammal) or isinstance(animal, Bird):
            # if animal.category in ["Mammal", "Bird"]:
            leg_count += animal.number_of_legs
    return leg_count


def count_category(animal_list):
    categories = {}
    for animal in animal_list:
        if animal.category in categories:
            categories[animal.category] += 1
        else:
            categories[animal.category] = 1
    return categories


animal_list = [
    Fish('Nemo', 'Fish', 2, 7),
    Fish("Marti", "Fish", 2, 7),
    Mammal("Bambi", "Mammal", 1, 4),
    Mammal("Simba", "Mammal", 3, 4),
    Bird("Iago", "Bird", 4, 2)
]


if __name__ == "__main__":
    animal = Animal("Lion",   "Mammal", 10)
    animal.print()

    nemo = Fish('Nemo',  'Fish', 2, 7)
    nemo.print()

    bambi = Mammal('Bambi', 'Mammal', 1, 4)
    bambi.print()

    lago = Bird('Lago', 'Bird', 4, 2)
    lago.print()

    legs = count_legs(animal_list)
    print(f'legs = {legs}')

    category = count_category(animal_list)
    print(category)
