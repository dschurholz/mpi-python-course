"""
Defining a class Animal and a class Pet that inherits from it.
"""


class Animal:
    type_of_animal = "llama"  # this is an attribute with default value "llama"

    def __init__(self, name):  # Run only when an object is created
        self.name = name

    def feed(self, food):     # this is a method
        print("Eating", food)

    def sleep(self, time):    # this is another method
        print("Sleeping for", time, "hours.")


class Pet(Animal):
    def pet_me(self):
        print("Petting the animal.")


llama = Animal("Bobby")
dog = Animal("Fido")
dog.type_of_animal = "dog"

llama.feed("ichu")
dog.feed("meat")

cat = Animal("Garfield")
cat.type_of_animal = "cat"

cat.pet_me()
cat.feed("fish")
