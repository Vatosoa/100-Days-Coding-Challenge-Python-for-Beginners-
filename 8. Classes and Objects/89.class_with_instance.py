class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Camry", 2020)
print(f"Make: {car1.make}, Model: {car1.model}, Year: {car1.year}")