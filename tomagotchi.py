"""A Tamagotchi Game"""
class Pet:
    # Class object attribute
    # Same for any instance of a class

    species = 'mammal'
    #Method called upon when creating an instance of a class
    def __init__(self,name,age):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute name
        self.age = age
        self.name = name

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def bark(self):
         print("WOOF! My name is {}".format(self.name))


if __name__ == "__main__":
    my_pet = Pet('Nea', 8)
    print(my_pet)
    my_pet.bark()
