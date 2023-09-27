class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
person1 = Person("Soa", 24)
print(person1.get_name())
print(person1.get_age())