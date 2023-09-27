class Dog:
    def make_sound(self):
        print("Woof")

class Cat:
    def make_sound(self):
        print("Meow")

def animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)