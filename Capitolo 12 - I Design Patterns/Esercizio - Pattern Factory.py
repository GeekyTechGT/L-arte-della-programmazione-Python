from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type.")

# Utilizzo del Factory per creare gli oggetti Animal

animal_factory = AnimalFactory()

dog = animal_factory.create_animal("dog")
print(dog.sound())  # Output: "Woof!"

cat = animal_factory.create_animal("cat")
print(cat.sound())  # Output: "Meow!"
