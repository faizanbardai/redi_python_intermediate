# Dog example for Object-oriented Programming from Lesson 11.

# A class is created with the class keyword.
# All attributes and methods associated with the class are written indented within the class.
class Dog:

    # The keyword for the class constructor is def __init__(self, ...) in Python.
    # The constructor describes how an instance of a class can be created.
    # Here we pass each parameter (name, age, bread) to the constructor and
    # assign it to an attribute of the object instance (self.name, self.age, self.bread).
    #
    # The constructor is later called by using the class name and passing the parameters
    # for the constructor in parentheses:
    # chloe = Dog("Chloe", 5, "Schnauzer")
    def __init__(self, name, age, breed):
        # The constructor does not only have to contain assignments to attributes, but can
        # also call functions that are required before starting to use the object instance.
        self.name = name
        self.age = age
        self.breed = breed
        # Here we assign a separate class attribute for the dog's age equivalent
        # to human years (in terms of body development).
        # This is very loosely based on this graphic from the web:
        # https://www.akc.org/wp-content/uploads/2015/11/Dog_Age_Chart_Proof_01Blue.jpg
        self.age_human_equivalent = 15 + self.age * 7

    # This is the description of a method of the class Dog. You can tell its a class method,
    # because the first parameter of the function is 'self'.
    # When later calling the function, you don't have to pass on 'self' explicitly.
    # This is done implicitly by specifying the object instance that calls the function:
    # rex = Dog("Rex", 2, "Dobermann")
    # rex.bark()   # here we specify that the object instance rex of class Dog is calling the bark() function
    def bark(self):
        print("wuff-wuff")

    # Here's an example of passing a parameter as part of the class method.
    # Here you also have the pass the parameter 'self' first.
    # It otherwise follow the same rules for named arguments like mentioned in a previous class
    # (arguments with a default parameter).
    def bark_a_name(self, name_of_owner):
        print(f"wuff-wuff {name_of_owner}")

    # The __str__() method is also a special method for describing instances of a class.
    # It defines what kind of string output is produced when calling an instance of the class Dog
    # with the built-in print(...) function.
    # Notice that __str__() should not do the printing itself, but only define the string that is printed.
    # Therefore, the __str__() function returns a string.
    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.breed}"

benny = Dog("Benny", 2, "Pug")

print(benny)


# if isinstance(benny, Dog):
# 	print(f"{benny.name} is a dog.")
# else:
# 	print(f"{benny.name} is NOT a dog.")
