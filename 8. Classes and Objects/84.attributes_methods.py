class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Soa", 24)
print(person1.name)
print(person1.age)
person1.say_hello()