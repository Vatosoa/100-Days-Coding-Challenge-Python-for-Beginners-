class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def show_student_info(self):
        print(f"Student ID: {self.student_id}")

student1 = Student("Soa", 24, 1234 )
student1.say_hello()
student1.show_student_info()